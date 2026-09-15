# Pantheon session snapshot — part 21

DATE: 2026-09-07
SOURCE_CLASS: mixed chat provenance snapshot
PROJECT: relationship-psychology / Семейный пантеон

## User directives added since part 20

The user again explicitly required the project workflow to proceed sequentially to completion with these binding rules:

- `audio-ready` is preparation only and is never equivalent to an actually voiced part;
- a part is counted as voiced only after a real playable audio file exists (MP3/WAV/other actual audio);
- actual audio production has priority, beginning with the earliest still-unvoiced ready part;
- if actual synthesis cannot be completed in a run, the part must remain explicitly `НЕ ОЗВУЧЕНА`; text preparation must not be substituted for audio completion;
- after the audio attempt, literary continuation proceeds strictly in sequence, without skipping;
- literary canon, audio scripts, and final audio files are stored separately;
- substantive working-chat messages are snapshotted into `sources/chat/` before the run ends;
- user project instructions are directives; user reports of real events remain `user-report` pending confirmation; assistant-created fiction is provenance only and must never be treated as factual evidence;
- if a full canonical literary text already exists, source snapshots should point to it rather than duplicate it.

These are project directives, not claims about real third-party events.

## Audio status and attempt in this run

The earliest first-book audio target remains:

- literary source: `Семейный пантеон/Семейный пантеон. Начало. Книга первая/01_Семейная_связь.md`
- audio script: `narrative/audio_scripts/BOOK1_01_FAMILY_CONNECTION_FISH.md`
- script status: `audio-ready`
- explicit audio status in the script: `НЕ ОЗВУЧЕНА до появления фактического MP3/WAV`.

The expected final MP3 path was checked again:

- `narrative/audio/pantheon/book1/Pantheon_BOOK1_P01_FAMILY_CONNECTION_FINAL.mp3`

It is still absent from the repository. The previous run's verified Fish Audio blocker remains HTTP 401 `Invalid Token` for the configured `FISH_API_KEY`; this run had no new valid credential available to replace it. Therefore no real MP3/WAV was produced.

Accordingly **Book 1 Part 01 remains НЕ ОЗВУЧЕНА**.

## Assistant-created fictional material in this run

After confirming the audio target is still blocked and unvoiced, literary work continued strictly from the current canonical endpoint in chapter 13.

The next sequential canonical chapter was created:

- `Семейный пантеон/Семейный пантеон. Начало. Книга первая/14_После_третьего_раза.md`

Full text is stored only in that canonical literary file; this source snapshot does not duplicate it.

Chapter 14 follows the archive vector established in chapter 13. The fictional investigation finds older records associated with the `three short — one long` mark, references to a `third case`, and a pattern involving people who returned after absences. Svarog identifies an old principle in which three repetitions can закрепить связь/правило; Gvozdar experiences a vision of three fires; Svarog recognizes an old prohibition: `никогда не зажигать третий костёр одному`. The chapter ends when the mark reappears on the nail in front of the group, and Kris proposes that this may indicate the first fire is already active.

`00_Содержание.md` was updated to index chapter 14 and record the next literary vector: determine what counts as a `fire`, who started the first, and whether the sequence can be stopped before the second and third.

All chapter 14 material is **fictional provenance only**. It is not factual evidence about real people, real places, motives, feelings, or events.

## Status at end of snapshot

- First-book literary line: canonically continues through `14_После_третьего_раза.md` plus the earlier combined-book material indexed by `00_Содержание.md`.
- First-book audio-ready: Part 01 `Семейная связь`.
- First-book actually voiced: NONE confirmed.
- Earliest unvoiced first-book part: Part 01 `Семейная связь`.
- Current actual audio blocker: Fish Audio credential remains invalid based on the last verified synthesis attempt; no playable final file exists.
- Next literary continuation after this run: chapter 15, beginning with the attempt to identify what the first `fire` actually is and whether the sequence has already started.
