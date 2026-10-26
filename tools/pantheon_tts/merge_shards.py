from __future__ import annotations

from pathlib import Path
import json
import subprocess

from pydub import AudioSegment, effects

ROOT = Path(__file__).resolve().parents[2]
TTS_DIR = ROOT / "tools" / "pantheon_tts"
BUILD = ROOT / "build" / "pantheon_ch01"
INPUT = BUILD / "downloaded_shards"
SEGMENTS_JSON = TTS_DIR / "ch01_segments.json"


def main() -> int:
    segments = json.loads(SEGMENTS_JSON.read_text(encoding="utf-8"))
    timeline = AudioSegment.silent(duration=300, frame_rate=24000)
    manifest = []

    files = {int(p.stem): p for p in INPUT.rglob("[0-9][0-9][0-9].wav")}
    missing = [i for i in range(1, len(segments) + 1) if i not in files]
    if missing:
        raise RuntimeError(f"Missing rendered segments: {missing}")

    shard_manifests = {}
    for p in INPUT.rglob("manifest.json"):
        for item in json.loads(p.read_text(encoding="utf-8")):
            shard_manifests[int(item["index"])] = item

    for i, seg in enumerate(segments, start=1):
        audio = AudioSegment.from_file(files[i]).set_channels(1).set_frame_rate(24000)
        timeline += audio
        timeline += AudioSegment.silent(duration=int(seg.get("pause_ms", 300)), frame_rate=24000)
        item = shard_manifests.get(i, {"index": i, "voice": seg["voice"], "role": seg["role"], "source_text": seg["text"]})
        manifest.append(item)

    raw_mix = BUILD / "Pantheon_S01_P01_Ch01_raw.wav"
    final_wav = BUILD / "Pantheon_S01_P01_Ch01_FINAL.wav"
    final_mp3 = BUILD / "Pantheon_S01_P01_Ch01_FINAL.mp3"
    BUILD.mkdir(parents=True, exist_ok=True)
    timeline.export(raw_mix, format="wav")

    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_mix),
        "-af", "highpass=f=55,loudnorm=I=-16:TP=-1.5:LRA=9",
        "-ar", "24000", "-ac", "1", str(final_wav),
    ], check=True)
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(final_wav),
        "-codec:a", "libmp3lame", "-b:a", "192k", str(final_mp3),
    ], check=True)

    (BUILD / "render_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(final_wav)
    print(final_mp3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
