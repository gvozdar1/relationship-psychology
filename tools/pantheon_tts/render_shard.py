from __future__ import annotations

from pathlib import Path
import argparse
import json
import subprocess
import sys

import torch
from pydub import AudioSegment, effects

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
import generate_ch01 as core


def synth_with_retry(model, text: str, voice: str, role: str, ref_v01: Path, ref_v02: Path, yarilo_ref: Path | None, attempts: int = 3):
    """Retry the SAME stressed text. Never remove accents to force success."""
    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            return core.synth_piece(model, text, voice, role, ref_v01, ref_v02, yarilo_ref)
        except Exception as exc:
            last_exc = exc
            print(
                f"accented_retry attempt={attempt}/{attempts} text={text!r}; "
                f"error={type(exc).__name__}: {exc}",
                flush=True,
            )
    raise last_exc


def render_whole_segment_fallback(model, stressed_text: str, voice: str, role: str, ref_v01: Path, ref_v02: Path, yarilo_ref: Path | None, out_dir: Path, index: int, sr: int):
    """Fallback keeps the exact stressed pronunciation text intact."""
    fallback_path = out_dir / f"{index:03d}_whole_fallback.wav"
    wav = synth_with_retry(
        model, stressed_text, voice, role, ref_v01, ref_v02, yarilo_ref, attempts=4
    )
    core.save_tensor(fallback_path, wav, sr)
    audio = core.wav_to_audio(fallback_path)
    if voice == "V03":
        tmp = out_dir / f"{index:03d}_whole_fallback_bright.wav"
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(fallback_path),
            "-af", f"asetrate={sr}*1.018,aresample={sr},atempo=0.982",
            str(tmp),
        ], check=True)
        audio = core.wav_to_audio(tmp)
    return effects.normalize(audio, headroom=1.8)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard-index", type=int, required=True)
    ap.add_argument("--shard-count", type=int, required=True)
    args = ap.parse_args()

    ref_v01 = core.REF_DIR / "V01.wav"
    ref_v02 = core.REF_DIR / "V02.wav"
    if not ref_v01.exists() or not ref_v02.exists():
        raise FileNotFoundError("Voice references are missing")

    segments = json.loads(core.SEGMENTS_JSON.read_text(encoding="utf-8"))
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = core.load_model(device)
    sr = int(model.sr)
    yarilo_ref = core.make_yarilo_seed(model, sr)

    out_dir = core.BUILD / "shards" / f"shard_{args.shard_index}"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []

    for i, seg in enumerate(segments, start=1):
        if (i - 1) % args.shard_count != args.shard_index:
            continue

        voice = seg["voice"]
        role = seg["role"]
        stressed_text = seg["text"]
        source_text = seg.get("source_text", stressed_text)
        units = core.prosodic_units(stressed_text)
        rendered = AudioSegment.silent(duration=0, frame_rate=sr)
        spoken_units = []
        unit_mode_ok = True

        try:
            for j, (unit, punctuation_pause_ms) in enumerate(units, start=1):
                raw_path = out_dir / f"{i:03d}_{j:02d}_{voice}.wav"
                print(
                    f"shard={args.shard_index} segment={i} unit={j}/{len(units)} "
                    f"{voice}: {unit}",
                    flush=True,
                )
                wav = synth_with_retry(
                    model, unit, voice, role, ref_v01, ref_v02, yarilo_ref
                )
                core.save_tensor(raw_path, wav, sr)
                audio = core.wav_to_audio(raw_path)

                if voice == "V03":
                    tmp = out_dir / f"{i:03d}_{j:02d}_{voice}_bright.wav"
                    subprocess.run([
                        "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_path),
                        "-af", f"asetrate={sr}*1.018,aresample={sr},atempo=0.982",
                        str(tmp),
                    ], check=True)
                    audio = core.wav_to_audio(tmp)

                audio = effects.normalize(audio, headroom=2.0)
                rendered += audio
                rendered += AudioSegment.silent(duration=punctuation_pause_ms, frame_rate=sr)
                spoken_units.append({
                    "text": unit,
                    "pause_ms": punctuation_pause_ms,
                    "mode": "prosodic-unit",
                })
        except Exception as exc:
            unit_mode_ok = False
            print(
                f"segment_fallback_with_accents index={i}; "
                f"error={type(exc).__name__}: {exc}",
                flush=True,
            )
            rendered = render_whole_segment_fallback(
                model, stressed_text, voice, role, ref_v01, ref_v02, yarilo_ref,
                out_dir, i, sr,
            )
            spoken_units = [{
                "text": stressed_text,
                "pause_ms": 0,
                "mode": "whole-segment-fallback-with-accents",
            }]

        rendered = effects.normalize(rendered, headroom=1.8)
        seg_path = out_dir / f"{i:03d}.wav"
        rendered.export(seg_path, format="wav")
        manifest.append({
            "index": i,
            "voice": voice,
            "role": role,
            "source_text": source_text,
            "pronunciation_text": stressed_text,
            "spoken_units": spoken_units,
            "render_mode": "prosodic-units" if unit_mode_ok else "whole-segment-fallback-with-accents",
            "file": seg_path.name,
            "duration_ms": len(rendered),
            "segment_pause_ms": int(seg.get("pause_ms", 300)),
        })

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
