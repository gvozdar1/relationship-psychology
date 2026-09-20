---
name: telegram-media-transcriber
description: Transcribe Telegram video circles, voice messages, and other audio/video files, preserve file order and timestamps, then make the transcript available for analysis together with the visual video context.
---

# Telegram Media Transcriber

Use this skill whenever the user uploads Telegram video circles, voice messages, or audio/video files and asks to understand, analyze, compare, or archive what was said.

## Workflow

1. Keep the user's file order. If screenshots show the order, use that order rather than guessing from filenames.
2. Run `scripts/transcribe_media.py` on every audio/video file.
3. Prefer local transcription when `faster-whisper` is installed. This keeps media local.
4. If local transcription is unavailable and `OPENAI_API_KEY` exists, use the OpenAI transcription API.
5. Default language is Russian (`ru`) unless the audio clearly uses another language.
6. Produce both per-file transcripts and one combined `bundle.txt`.
7. Never claim to have heard speech unless a transcript was actually produced.
8. When analyzing a video circle, separate:
   - exact transcript;
   - visual observations from the video;
   - inference/interpretation.
9. Preserve uncertainty. Mark unclear words as `[неразборчиво]` rather than inventing them.
10. For relationship-project analysis, keep factual transcript separate from hypotheses.

## Typical command

```bash
python scripts/transcribe_media.py /path/to/circles --language ru --engine auto --output-dir transcripts
```

For names/terms that speech recognition may distort:

```bash
python scripts/transcribe_media.py /path/to/circles \
  --language ru \
  --prompt "Крис, Гвоздарь, Евгений, Юра, Никита, Минск" \
  --output-dir transcripts
```

## Engine behavior

- `auto`: use `faster-whisper` if available; otherwise use OpenAI API if configured.
- `local`: require `faster-whisper`.
- `openai`: require the `openai` package and `OPENAI_API_KEY`.

Do not silently switch to guessed lip-reading if neither transcription engine is available.
