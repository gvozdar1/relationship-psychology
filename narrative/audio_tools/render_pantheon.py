#!/usr/bin/env python3
import argparse
import asyncio
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from pydub import AudioSegment

try:
    import edge_tts
except Exception:
    edge_tts = None

VOICE_MAP = {
    "РАССКАЗЧИК": ("ru-RU-DmitryNeural", "+0%", "+0Hz", 155, 48),
    "СТАНИСЛАВ": ("ru-RU-DmitryNeural", "+2%", "+0Hz", 165, 52),
    "КРИС": ("ru-RU-SvetlanaNeural", "+1%", "+0Hz", 178, 62),
    "ЯРИЛО": ("ru-RU-DmitryNeural", "+14%", "+18Hz", 195, 70),
    "СВАРОГ": ("ru-RU-DmitryNeural", "-8%", "-22Hz", 125, 30),
    "МОКОШЬ": ("ru-RU-SvetlanaNeural", "-8%", "-12Hz", 145, 38),
    "ВЕЛЕС": ("ru-RU-DmitryNeural", "-4%", "+8Hz", 150, 45),
    "РОД": ("ru-RU-DmitryNeural", "-14%", "-35Hz", 110, 22),
    "ВОЛК": ("ru-RU-DmitryNeural", "-10%", "-28Hz", 120, 28),
    "ГОЛОС ИЗ ТРЕЩИНЫ": ("ru-RU-DmitryNeural", "-12%", "-8Hz", 112, 26),
    "ЖЕНСКИЙ ГОЛОС": ("ru-RU-SvetlanaNeural", "-5%", "-5Hz", 150, 60),
}


def norm_speaker(raw: str) -> str:
    raw = raw.strip().upper()
    raw = raw.split(",", 1)[0].strip()
    if raw.startswith("ЖЕНСКИЙ ГОЛОС"):
        return "ЖЕНСКИЙ ГОЛОС"
    if raw.startswith("ГОЛОС ИЗ ТРЕЩИНЫ"):
        return "ГОЛОС ИЗ ТРЕЩИНЫ"
    return raw


def stage_silence_ms(line: str) -> int:
    low = line.lower()
    m = re.search(r"(\d+)\s*сек", low)
    if m:
        return int(m.group(1)) * 1000
    if "тишина" in low:
        return 1800
    if "пауза" in low:
        return 900
    if "sfx" in low or "треск" in low or "щелчок" in low:
        return 450
    return 350


def parse_script(text: str):
    body = text.split("---", 1)[1] if "---" in text else text
    items = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            items.append(("silence", stage_silence_ms(line), line))
            continue
        if ":" not in line:
            continue
        speaker_raw, spoken = line.split(":", 1)
        speaker = norm_speaker(speaker_raw)
        spoken = spoken.strip()
        if speaker in VOICE_MAP and spoken:
            items.append(("speech", speaker, spoken))
    return items


async def synth_edge(text: str, voice: str, rate: str, pitch: str, out: Path):
    if edge_tts is None:
        raise RuntimeError("edge-tts is unavailable")
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out))


def synth_espeak(text: str, speed: int, pitch: int, out: Path):
    if not shutil.which("espeak"):
        raise RuntimeError("espeak is unavailable")
    subprocess.run(
        ["espeak", "-v", "ru", "-s", str(speed), "-p", str(pitch), "-w", str(out), text],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


async def render(script: Path, mp3_out: Path, wav_out: Path):
    text = script.read_text(encoding="utf-8")
    items = parse_script(text)
    if not items:
        raise RuntimeError("No renderable dialogue found")

    master = AudioSegment.silent(duration=350)
    used_fallback = False
    with tempfile.TemporaryDirectory() as td_raw:
        td = Path(td_raw)
        idx = 0
        for item in items:
            if item[0] == "silence":
                master += AudioSegment.silent(duration=item[1])
                continue
            _, speaker, spoken = item
            voice, rate, pitch, speed, espeak_pitch = VOICE_MAP[speaker]
            edge_chunk = td / f"{idx:04d}.mp3"
            wav_chunk = td / f"{idx:04d}.wav"
            try:
                await synth_edge(spoken, voice, rate, pitch, edge_chunk)
                audio = AudioSegment.from_file(edge_chunk, format="mp3")
            except Exception as exc:
                used_fallback = True
                print(f"edge-tts failed for chunk {idx}; using eSpeak fallback: {exc}")
                synth_espeak(spoken, speed, espeak_pitch, wav_chunk)
                audio = AudioSegment.from_wav(wav_chunk)
            master += audio + AudioSegment.silent(duration=180)
            idx += 1

    mp3_out.parent.mkdir(parents=True, exist_ok=True)
    master = master.set_channels(1).set_frame_rate(22050)
    master.export(mp3_out, format="mp3", bitrate="64k")
    master.export(wav_out, format="wav")
    print(f"Rendered {idx} speech chunks")
    print(f"Fallback used: {used_fallback}")
    print(f"MP3: {mp3_out} ({mp3_out.stat().st_size} bytes)")
    print(f"WAV: {wav_out} ({wav_out.stat().st_size} bytes)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("script", type=Path)
    p.add_argument("mp3", type=Path)
    p.add_argument("wav", type=Path)
    args = p.parse_args()
    asyncio.run(render(args.script, args.mp3, args.wav))


if __name__ == "__main__":
    main()
