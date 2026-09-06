#!/usr/bin/env python3
import argparse
import os
import re
import sys
import time
from pathlib import Path

import requests
from pydub import AudioSegment

API_URL = "https://api.fish.audio/v1/tts"
MODEL = "s2-pro"

# Voice routing lives here, not in the copy/paste audio script.
VOICE_IDS = {
    "СТАНИСЛАВ": "3f3aedcd66b44082a8d4802ed3c41722",
    "ГВОЗДАРЬ": "3f3aedcd66b44082a8d4802ed3c41722",
    "РАССКАЗЧИК": "3f3aedcd66b44082a8d4802ed3c41722",
    "КРИС": "8e562ef6ef7f4174985c9fd04bec4b3b",
    "ЯРИЛО": "2078202b8fd047b3bbc260d501bc2d6e",
}


def parse_script(path: Path):
    text = path.read_text(encoding="utf-8")
    # The header itself documents the literal token `---`, so splitting on the
    # first occurrence is unsafe. Only a standalone Markdown separator starts
    # the TTS body.
    match = re.search(r"(?m)^---\s*$", text)
    body = text[match.end():] if match else text
    blocks = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or ":" not in line:
            continue
        speaker, spoken = line.split(":", 1)
        speaker = speaker.strip().upper()
        spoken = spoken.strip()
        if not spoken:
            continue
        if speaker not in VOICE_IDS:
            raise RuntimeError(f"Unknown speaker: {speaker}")
        if len(spoken) > 750:
            raise RuntimeError(f"Block exceeds 750 chars for {speaker}: {len(spoken)}")
        blocks.append((speaker, spoken))
    if not blocks:
        raise RuntimeError("No TTS blocks found")
    return blocks


def synth_block(session: requests.Session, api_key: str, speaker: str, text: str, out: Path):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "model": MODEL,
    }
    payload = {
        "text": text,
        "reference_id": VOICE_IDS[speaker],
        "format": "mp3",
    }
    last = None
    for attempt in range(1, 4):
        r = session.post(API_URL, headers=headers, json=payload, timeout=180)
        last = r
        if r.status_code == 200 and r.content:
            out.write_bytes(r.content)
            return
        if r.status_code in (429, 500, 502, 503, 504) and attempt < 3:
            time.sleep(4 * attempt)
            continue
        snippet = r.text[:1000] if "text" in r.headers.get("content-type", "") else r.content[:300]
        raise RuntimeError(f"Fish TTS failed speaker={speaker} status={r.status_code}: {snippet}")
    raise RuntimeError(f"Fish TTS failed after retries: {getattr(last, 'status_code', 'unknown')}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("script", type=Path)
    p.add_argument("mp3", type=Path)
    p.add_argument("wav", type=Path)
    args = p.parse_args()

    api_key = os.environ.get("FISH_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("FISH_API_KEY is missing")

    blocks = parse_script(args.script)
    tmp = Path(".fish_chunks")
    tmp.mkdir(exist_ok=True)
    session = requests.Session()
    master = AudioSegment.silent(duration=300)

    for idx, (speaker, spoken) in enumerate(blocks, start=1):
        chunk = tmp / f"{idx:03d}_{speaker}.mp3"
        print(f"[{idx}/{len(blocks)}] {speaker}: {len(spoken)} chars")
        synth_block(session, api_key, speaker, spoken, chunk)
        audio = AudioSegment.from_file(chunk, format="mp3")
        master += audio + AudioSegment.silent(duration=220)

    args.mp3.parent.mkdir(parents=True, exist_ok=True)
    master = master.set_channels(1).set_frame_rate(44100)
    master.export(args.mp3, format="mp3", bitrate="128k")
    master.export(args.wav, format="wav")

    if args.mp3.stat().st_size <= 0 or args.wav.stat().st_size <= 0:
        raise RuntimeError("Rendered output is empty")
    print(f"Rendered {len(blocks)} Fish blocks")
    print(f"MP3 {args.mp3} {args.mp3.stat().st_size} bytes")
    print(f"WAV {args.wav} {args.wav.stat().st_size} bytes")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
