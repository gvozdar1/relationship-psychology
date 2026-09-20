#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

SUPPORTED = {".mp4", ".mov", ".mkv", ".webm", ".m4a", ".mp3", ".wav", ".ogg", ".opus", ".aac", ".flac"}


@dataclass
class Segment:
    start: float | None
    end: float | None
    text: str


@dataclass
class Result:
    source: str
    duration: float | None
    engine: str
    language: str | None
    text: str
    segments: list[Segment]
    status: str = "ok"
    error: str | None = None


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def require_ffmpeg() -> None:
    missing = [x for x in ("ffmpeg", "ffprobe") if shutil.which(x) is None]
    if missing:
        raise RuntimeError(f"Missing required executable(s): {', '.join(missing)}")


def media_duration(path: Path) -> float | None:
    try:
        cp = run([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ])
        return float(cp.stdout.strip())
    except Exception:
        return None


def extract_audio(path: Path, out_wav: Path) -> None:
    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(path),
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(out_wav),
    ])


def collect_inputs(items: list[str], recursive: bool) -> list[Path]:
    out: list[Path] = []
    for item in items:
        p = Path(item).expanduser().resolve()
        if p.is_file():
            if p.suffix.lower() in SUPPORTED:
                out.append(p)
            continue
        if p.is_dir():
            it: Iterable[Path] = p.rglob("*") if recursive else p.glob("*")
            out.extend(sorted(x.resolve() for x in it if x.is_file() and x.suffix.lower() in SUPPORTED))
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in out:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


def pick_engine(requested: str) -> str:
    if requested != "auto":
        return requested
    try:
        import faster_whisper  # noqa: F401
        return "local"
    except Exception:
        pass
    if os.getenv("OPENAI_API_KEY"):
        try:
            import openai  # noqa: F401
            return "openai"
        except Exception:
            pass
    raise RuntimeError(
        "No transcription engine available. Install faster-whisper for local mode, "
        "or install openai and set OPENAI_API_KEY for cloud mode."
    )


def fmt_ts(seconds: float | None) -> str:
    if seconds is None:
        return "??:??.???"
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
    return f"{m:02d}:{s:02d}.{ms:03d}"


def transcribe_local(audio: Path, language: str | None, model_name: str, prompt: str | None) -> tuple[str, list[Segment], str | None]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as e:
        raise RuntimeError("faster-whisper is not installed. Install requirements-local.txt") from e

    model = WhisperModel(model_name, device="auto", compute_type="int8")
    seg_iter, info = model.transcribe(
        str(audio),
        language=language,
        vad_filter=True,
        beam_size=5,
        initial_prompt=prompt or None,
    )
    segments: list[Segment] = []
    parts: list[str] = []
    for s in seg_iter:
        text = (s.text or "").strip()
        if not text:
            continue
        segments.append(Segment(float(s.start), float(s.end), text))
        parts.append(text)
    detected = getattr(info, "language", None) or language
    return " ".join(parts).strip(), segments, detected


def transcribe_openai(audio: Path, language: str | None, model_name: str, prompt: str | None) -> tuple[str, list[Segment], str | None]:
    try:
        from openai import OpenAI
    except ImportError as e:
        raise RuntimeError("openai package is not installed. Install requirements-openai.txt") from e
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set")

    client = OpenAI()
    kwargs = {"model": model_name, "response_format": "json"}
    if language:
        kwargs["language"] = language
    if prompt:
        kwargs["prompt"] = prompt
    with audio.open("rb") as fh:
        resp = client.audio.transcriptions.create(file=fh, **kwargs)
    text = getattr(resp, "text", None)
    if text is None and isinstance(resp, dict):
        text = resp.get("text", "")
    return (text or "").strip(), [], language


def write_result(result: Result, out_dir: Path) -> None:
    src = Path(result.source)
    stem = src.stem
    txt_path = out_dir / f"{stem}.txt"
    json_path = out_dir / f"{stem}.json"

    lines = [f"# {src.name}", f"engine: {result.engine}", f"language: {result.language or 'unknown'}"]
    if result.duration is not None:
        lines.append(f"duration_seconds: {result.duration:.3f}")
    lines.append("")
    if result.segments:
        for s in result.segments:
            lines.append(f"[{fmt_ts(s.start)} - {fmt_ts(s.end)}] {s.text}")
    else:
        lines.append(result.text)
    txt_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    payload = asdict(result)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch-transcribe Telegram video circles and audio/video files.")
    ap.add_argument("inputs", nargs="+", help="Files and/or directories, kept in the order given")
    ap.add_argument("--output-dir", default="transcripts")
    ap.add_argument("--engine", choices=["auto", "local", "openai"], default="auto")
    ap.add_argument("--language", default="ru", help="ISO language code; use empty string for autodetect")
    ap.add_argument("--local-model", default="small", help="faster-whisper model name, e.g. small/medium/large-v3")
    ap.add_argument("--openai-model", default="gpt-4o-mini-transcribe")
    ap.add_argument("--prompt", default=None, help="Names/terms/context to improve recognition")
    ap.add_argument("--recursive", action="store_true")
    args = ap.parse_args()

    require_ffmpeg()
    files = collect_inputs(args.inputs, args.recursive)
    if not files:
        print("No supported media files found.", file=sys.stderr)
        return 2

    out_dir = Path(args.output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    engine = pick_engine(args.engine)
    language = args.language or None

    results: list[Result] = []
    with tempfile.TemporaryDirectory(prefix="tg-transcribe-") as td:
        temp_dir = Path(td)
        for idx, src in enumerate(files, 1):
            duration = media_duration(src)
            print(f"[{idx}/{len(files)}] {src.name} ({duration or 0:.1f}s) via {engine}", file=sys.stderr)
            audio = temp_dir / f"{idx:04d}_{src.stem}.wav"
            try:
                extract_audio(src, audio)
                if engine == "local":
                    text, segments, detected = transcribe_local(audio, language, args.local_model, args.prompt)
                else:
                    text, segments, detected = transcribe_openai(audio, language, args.openai_model, args.prompt)
                result = Result(str(src), duration, engine, detected, text, segments)
            except Exception as exc:
                result = Result(str(src), duration, engine, language, "", [], status="error", error=str(exc))
                print(f"ERROR {src.name}: {exc}", file=sys.stderr)
            write_result(result, out_dir)
            results.append(result)

    bundle: list[str] = []
    for i, r in enumerate(results, 1):
        bundle.append(f"===== {i:02d}. {Path(r.source).name} =====")
        if r.status != "ok":
            bundle.append(f"[ERROR] {r.error}")
        elif r.segments:
            bundle.extend(f"[{fmt_ts(s.start)} - {fmt_ts(s.end)}] {s.text}" for s in r.segments)
        else:
            bundle.append(r.text)
        bundle.append("")
    (out_dir / "bundle.txt").write_text("\n".join(bundle).rstrip() + "\n", encoding="utf-8")

    with (out_dir / "manifest.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["order", "file", "duration_seconds", "engine", "language", "status", "error"])
        for i, r in enumerate(results, 1):
            w.writerow([i, r.source, "" if r.duration is None else f"{r.duration:.3f}", r.engine, r.language or "", r.status, r.error or ""])

    failed = sum(r.status != "ok" for r in results)
    print(f"Done: {len(results)-failed} ok, {failed} failed. Output: {out_dir}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
