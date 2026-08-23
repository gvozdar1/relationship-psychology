#!/usr/bin/env python3
import argparse
import asyncio
import re
import tempfile
from pathlib import Path

import edge_tts
from pydub import AudioSegment

VOICE_MAP = {
    "РАССКАЗЧИК": ("ru-RU-DmitryNeural", "+0%", "+0Hz"),
    "СТАНИСЛАВ": ("ru-RU-DmitryNeural", "+2%", "+0Hz"),
    "КРИС": ("ru-RU-SvetlanaNeural", "+1%", "+0Hz"),
    "ЯРИЛО": ("ru-RU-DmitryNeural", "+14%", "+18Hz"),
    "СВАРОГ": ("ru-RU-DmitryNeural", "-8%", "-22Hz"),
    "МОКОШЬ": ("ru-RU-SvetlanaNeural", "-8%", "-12Hz"),
    "ВЕЛЕС": ("ru-RU-DmitryNeural", "-4%", "+8Hz"),
    "РОД": ("ru-RU-DmitryNeural", "-14%", "-35Hz"),
    "ВОЛК": ("ru-RU-DmitryNeural", "-10%", "-28Hz"),
    "ГОЛОС ИЗ ТРЕЩИНЫ": ("ru-RU-DmitryNeural", "-12%", "-8Hz"),
    "ЖЕНСКИЙ ГОЛОС": ("ru-RU-SvetlanaNeural", "-5%", "-5Hz"),
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


async def synth(text: str, voice: str, rate: str, pitch: str, out: Path):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out))


async def render(script: Path, mp3_out: Path, wav_out: Path):
    text = script.read_text(encoding="utf-8")
    items = parse_script(text)
    if not items:
        raise RuntimeError("No renderable dialogue found")

    master = AudioSegment.silent(duration=350)
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        idx = 0
        for item in items:
            if item[0] == "silence":
                master += AudioSegment.silent(duration=item[1])
                continue
            _, speaker, spoken = item
            voice, rate, pitch = VOICE_MAP[speaker]
            chunk = td / f"{idx:04d}.mp3"
            await synth(spoken, voice, rate, pitch, chunk)
            audio = AudioSegment.from_file(chunk, format="mp3")
            master += audio + AudioSegment.silent(duration=180)
            idx += 1

    mp3_out.parent.mkdir(parents=True, exist_ok=True)
    master.export(mp3_out, format="mp3", bitrate="192k")
    master.export(wav_out, format="wav")
    print(f"Rendered {idx} speech chunks")
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
