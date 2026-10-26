from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess

import torch
import torchaudio as ta
from pydub import AudioSegment, effects

try:
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
except Exception:
    from chatterbox import ChatterboxMultilingualTTS

ROOT = Path(__file__).resolve().parents[2]
TTS_DIR = ROOT / "tools" / "pantheon_tts"
BUILD = ROOT / "build" / "pantheon_ch01"
SEG_DIR = BUILD / "segments"
REF_DIR = TTS_DIR / "refs"
SEGMENTS_JSON = TTS_DIR / "ch01_segments.json"

BUILD.mkdir(parents=True, exist_ok=True)
SEG_DIR.mkdir(parents=True, exist_ok=True)

# Pronunciation layer only. Literary text in ch01_segments.json is NOT rewritten.
# Combining acute accents are supplied directly so important names and slang do
# not depend on Chatterbox's optional automatic Russian stress package.
STRESS_OVERRIDES = [
    (r"\bГвоздарик\b", "Гвозда́рик"),
    (r"\bГвоздарич\b", "Гвозда́рич"),
    (r"\bГвоздарь\b", "Гвозда́рь"),
    (r"\bЯрило\b", "Яри́ло"),
    (r"\bСварогу\b", "Сваро́гу"),
    (r"\bСварог\b", "Сваро́г"),
    (r"\bЭверест\b", "Эвере́ст"),
    (r"\bмедовуху\b", "медову́ху"),
    (r"\bсъебать\b", "съеба́ть"),
    (r"\bЗаебался\b", "Заеба́лся"),
    (r"\bзаебался\b", "заеба́лся"),
    (r"\bблагодарку\b", "благода́рку"),
    (r"\bпялишься\b", "пя́лишься"),
]


def stressify(text: str) -> str:
    out = text
    for pattern, replacement in STRESS_OVERRIDES:
        out = re.sub(pattern, replacement, out)
    return out


def load_model(device: str):
    try:
        return ChatterboxMultilingualTTS.from_pretrained(device=device, t3_model="v3")
    except TypeError:
        return ChatterboxMultilingualTTS.from_pretrained(device=device)


def pause_after(unit: str) -> int:
    s = unit.rstrip()
    if s.endswith("...") or s.endswith("…"):
        return 520
    if s.endswith("!") or s.endswith("?"):
        return 360
    if s.endswith("."):
        return 330
    if s.endswith(";") or s.endswith(":"):
        return 260
    if s.endswith(","):
        return 190
    return 90


def _spoken_core_len(part: str) -> int:
    # Ignore punctuation and the combining acute accent when deciding whether a
    # fragment is too tiny for Chatterbox to render safely.
    core = re.sub(r"[^0-9A-Za-zА-Яа-яЁё]+", "", part)
    return len(core)


def _coalesce_micro_fragments(parts: list[str]) -> list[str]:
    """Never send one-letter interjections such as 'О,' or 'Я!' alone.

    Chatterbox can crash in its alignment analyzer on ultra-short standalone
    fragments. We glue only micro-fragments (less than 3 spoken characters) to
    the following phrase. Normal comma clauses stay separate and retain real
    audio pauses after them.
    """
    out: list[str] = []
    carry = ""

    for part in parts:
        if _spoken_core_len(part) < 3:
            carry = f"{carry} {part}".strip() if carry else part
            continue

        if carry:
            part = f"{carry} {part}".strip()
            carry = ""
        out.append(part)

    if carry:
        if out:
            out[-1] = f"{out[-1]} {carry}".strip()
        else:
            out.append(carry)

    return out


def prosodic_units(text: str, limit: int = 145) -> list[tuple[str, int]]:
    """Split on meaningful punctuation and enforce real pauses in the waveform.

    Tiny interjections are kept with a neighbouring phrase so the neural model
    remains stable. Source text itself is untouched; this is pronunciation-only.
    """
    text = stressify(re.sub(r"\s+", " ", text).strip())
    if not text:
        return []

    raw = [
        p.strip()
        for p in re.findall(r"[^,;:!?…。]+(?:\.\.\.|[,:;.!?…]|$)", text)
        if p.strip()
    ]
    raw = _coalesce_micro_fragments(raw)
    units: list[tuple[str, int]] = []

    for part in raw:
        if len(part) <= limit:
            units.append((part, pause_after(part)))
            continue

        final_punct = ""
        m = re.search(r"(\.\.\.|[,:;.!?…])$", part)
        core = part
        if m:
            final_punct = m.group(1)
            core = part[: -len(final_punct)].rstrip()

        words = core.split()
        buf = ""
        pieces: list[str] = []
        for word in words:
            candidate = f"{buf} {word}".strip()
            if buf and len(candidate) > limit:
                pieces.append(buf)
                buf = word
            else:
                buf = candidate
        if buf:
            pieces.append(buf)

        for idx, piece in enumerate(pieces):
            is_last = idx == len(pieces) - 1
            spoken = piece + (final_punct if is_last else ",")
            units.append((spoken, pause_after(spoken) if is_last else 170))

    return units


def save_tensor(path: Path, wav: torch.Tensor, sr: int) -> None:
    wav = wav.detach().cpu()
    if wav.ndim == 1:
        wav = wav.unsqueeze(0)
    ta.save(str(path), wav, sr)


def synth_piece(model, text: str, voice: str, role: str, ref_v01: Path, ref_v02: Path, yarilo_ref: Path | None):
    kwargs = {"language_id": "ru"}
    if voice == "V01":
        kwargs.update(
            audio_prompt_path=str(ref_v01),
            exaggeration=0.34 if role == "РАССКАЗЧИК" else 0.46,
            cfg_weight=0.54,
            temperature=0.69,
        )
    elif voice == "V02":
        kwargs.update(
            audio_prompt_path=str(ref_v02),
            exaggeration=0.38,
            cfg_weight=0.53,
            temperature=0.69,
        )
    elif voice == "V03":
        if yarilo_ref is not None and yarilo_ref.exists():
            kwargs["audio_prompt_path"] = str(yarilo_ref)
        kwargs.update(
            exaggeration=0.66,
            cfg_weight=0.43,
            temperature=0.76,
        )
    else:
        raise ValueError(f"Unknown voice: {voice}")

    try:
        return model.generate(text, **kwargs)
    except TypeError:
        kwargs.pop("temperature", None)
        return model.generate(text, **kwargs)


def wav_to_audio(path: Path) -> AudioSegment:
    return AudioSegment.from_file(path).set_channels(1)


def make_yarilo_seed(model, sr: int) -> Path:
    path = BUILD / "V03_Yarilo_virtual_seed.wav"
    seed_text = "Ну что, брата́н? Живо́й? Тогда́ погна́ли. Яри́ло на свя́зи."
    try:
        wav = model.generate(
            seed_text,
            language_id="ru",
            exaggeration=0.62,
            cfg_weight=0.44,
            temperature=0.74,
        )
    except TypeError:
        wav = model.generate(seed_text, language_id="ru")
    save_tensor(path, wav, sr)

    processed = BUILD / "V03_Yarilo_virtual_seed_processed.wav"
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
            "-af", "asetrate=24000*1.025,aresample=24000,atempo=0.976",
            str(processed),
        ],
        check=True,
    )
    return processed


def main() -> int:
    ref_v01 = REF_DIR / "V01.wav"
    ref_v02 = REF_DIR / "V02.wav"
    if not ref_v01.exists() or not ref_v02.exists():
        raise FileNotFoundError("Voice references were not reconstructed before generation")

    segments = json.loads(SEGMENTS_JSON.read_text(encoding="utf-8"))
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"device={device}", flush=True)
    model = load_model(device)
    sr = int(model.sr)
    print(f"model_sr={sr}", flush=True)

    yarilo_ref = make_yarilo_seed(model, sr)

    timeline = AudioSegment.silent(duration=300, frame_rate=sr)
    manifest = []

    for i, seg in enumerate(segments, start=1):
        voice = seg["voice"]
        role = seg["role"]
        original_text = seg["text"]
        segment_pause_ms = int(seg.get("pause_ms", 300))
        units = prosodic_units(original_text)
        rendered = AudioSegment.silent(duration=0, frame_rate=sr)
        spoken_units = []

        for j, (unit, punctuation_pause_ms) in enumerate(units, start=1):
            raw_path = SEG_DIR / f"{i:03d}_{j:02d}_{voice}_{role}.wav"
            print(
                f"render {i}/{len(segments)} {voice} {role} unit {j}/{len(units)}: {unit}",
                flush=True,
            )
            wav = synth_piece(model, unit, voice, role, ref_v01, ref_v02, yarilo_ref)
            save_tensor(raw_path, wav, sr)
            audio = wav_to_audio(raw_path)

            if voice == "V03":
                tmp = SEG_DIR / f"{i:03d}_{j:02d}_{voice}_{role}_bright.wav"
                subprocess.run(
                    [
                        "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_path),
                        "-af", f"asetrate={sr}*1.018,aresample={sr},atempo=0.982",
                        str(tmp),
                    ],
                    check=True,
                )
                audio = wav_to_audio(tmp)

            audio = effects.normalize(audio, headroom=2.0)
            rendered += audio
            rendered += AudioSegment.silent(duration=punctuation_pause_ms, frame_rate=sr)
            spoken_units.append({"text": unit, "pause_ms": punctuation_pause_ms})

        rendered = effects.normalize(rendered, headroom=1.8)
        seg_path = SEG_DIR / f"{i:03d}_{voice}_{role}.wav"
        rendered.export(seg_path, format="wav")
        timeline += rendered
        timeline += AudioSegment.silent(duration=segment_pause_ms, frame_rate=sr)

        manifest.append({
            "index": i,
            "voice": voice,
            "role": role,
            "source_text": original_text,
            "spoken_units": spoken_units,
            "file": seg_path.name,
            "duration_ms": len(rendered),
            "segment_pause_ms": segment_pause_ms,
        })

    raw_mix = BUILD / "Pantheon_S01_P01_Ch01_raw.wav"
    timeline.export(raw_mix, format="wav")

    final_wav = BUILD / "Pantheon_S01_P01_Ch01_FINAL.wav"
    final_mp3 = BUILD / "Pantheon_S01_P01_Ch01_FINAL.mp3"
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_mix),
            "-af", "highpass=f=55,loudnorm=I=-16:TP=-1.5:LRA=9",
            "-ar", "24000", "-ac", "1", str(final_wav),
        ],
        check=True,
    )
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(final_wav),
            "-codec:a", "libmp3lame", "-b:a", "192k", str(final_mp3),
        ],
        check=True,
    )

    (BUILD / "render_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(final_wav)
    print(final_mp3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
