# Telegram Media Transcriber

Batch transcription for Telegram video circles, voice messages, and ordinary audio/video files.

## What it does

- accepts MP4/MOV/WebM/M4A/MP3/WAV/OGG/OPUS;
- extracts audio with ffmpeg;
- transcribes Russian speech;
- preserves per-file order;
- writes `.txt` and `.json` per file;
- writes a combined `bundle.txt` and `manifest.csv`;
- supports local `faster-whisper` and OpenAI API fallback.

## Requirements

- Python 3.10+
- `ffmpeg` and `ffprobe` on PATH

### Local, private mode

```bash
pip install -r requirements-local.txt
```

The Whisper model is downloaded on first use by faster-whisper.

### OpenAI API mode

```bash
pip install -r requirements-openai.txt
export OPENAI_API_KEY="..."
```

Default cloud model: `gpt-4o-mini-transcribe`.

## Usage

```bash
python scripts/transcribe_media.py ./media --language ru --engine auto --output-dir ./transcripts
```

With project names as recognition hints:

```bash
python scripts/transcribe_media.py ./media \
  --language ru \
  --prompt "Крис, Гвоздарь, Евгений, Юра, Никита, Минск" \
  --output-dir ./transcripts
```

Process files in explicit order:

```bash
python scripts/transcribe_media.py 01.mp4 02.mp4 03.mp4 --output-dir transcripts
```

## Output

For `01.mp4`:

- `01.txt` human-readable transcript
- `01.json` structured data

Batch files:

- `bundle.txt` all transcripts in input order
- `manifest.csv` file, duration, engine, language, status

## Privacy

`--engine local` keeps media on the machine running the script. `--engine openai` sends extracted audio to the OpenAI API for transcription.
