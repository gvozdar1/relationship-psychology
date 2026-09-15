# Pantheon session snapshot — part 19

DATE: 2026-09-04
SOURCE_CLASS: mixed chat provenance snapshot
PROJECT: relationship-psychology / Семейный пантеон

## User directives added since part 18

### Repository-line correction

The user explicitly corrected the assistant after it had continued the wrong Pantheon branch. The user stated that `Семейный пантеон` is only the general title and that the repository already contains several parts/versions belonging to the first book. The user instructed the assistant to inspect the GitHub repository instead of treating `narrative/mini_stories/pantheon/` as the first book.

This is a project-structure directive, not a real-world factual claim about third parties.

Repository inspection confirmed the book pointer in:

- `Семейный пантеон/Семейный пантеон. Начало. Книга первая/00_Содержание.md`
- combined early-edition file: `Семейный пантеон/Семейный пантеон. Начало. Книга первая.md`
- current separated chapters under `Семейный пантеон/Семейный пантеон. Начало. Книга первая/`

Therefore, future sequential literary work for **the first book** must follow this book line rather than automatically extending `narrative/mini_stories/pantheon/`.

### Audio rule repeated for this run

The user again required:

- `audio-ready` does not mean voiced;
- a part is voiced only if a real playable audio file (MP3/WAV/etc.) exists;
- earliest unvoiced ready part has priority;
- if real synthesis is technically impossible, mark it `НЕ ОЗВУЧЕНА` and continue preparation without claiming completion;
- after audio priority, continue the next literary part strictly in sequence;
- literary files, audio scripts and final audio binaries remain separate;
- current-chat project messages must be snapshotted to `sources/chat/` before the run ends;
- assistant-created fiction is provenance only and never factual evidence.

## Authoritative first-book state checked in this run

`00_Содержание.md` identifies the first-book line as **«Семейный пантеон. Начало. Книга первая»**. Its canonical first part is `01_Семейная_связь.md`. The combined early-edition file contains the next early scenes, and the later continuations are stored as separate chapters `04_...` through `11_...`.

The previous automation work on `narrative/mini_stories/pantheon/14...15` is therefore not treated here as the sequential continuation of this first book.

## Audio work in this run

Prepared a Fish Audio S2 Pro render script for the actual first-book opening:

- `narrative/audio_scripts/BOOK1_01_FAMILY_CONNECTION_FISH.md`
- literary source: `Семейный пантеон/Семейный пантеон. Начало. Книга первая/01_Семейная_связь.md`
- script status: `audio-ready`
- script explicitly states `AUDIO_STATUS: НЕ ОЗВУЧЕНА` until a real output file exists.

Added Fish renderer and workflow:

- `narrative/audio_tools/render_fish_book1.py`
- `.github/workflows/render-book1-part01-fish.yml`

The renderer routes voices internally so voice IDs are not placed in the copy/paste audio script. It uses the current project voice routing for Станислав/Гвоздарь, Крис and Ярило and enforces the 750-character block limit.

A render-trigger commit was made. At the time of this snapshot, no final file existed at the expected output location:

- `narrative/audio/pantheon/book1/Pantheon_BOOK1_P01_FAMILY_CONNECTION_FINAL.mp3`
- `narrative/audio/pantheon/book1/Pantheon_BOOK1_P01_FAMILY_CONNECTION_FINAL.wav`

Therefore **Part 01 remains НЕ ОЗВУЧЕНА**. The absence of output is not converted into a completed-audio status.

Historical repository notes already record GitHub Actions billing/run blocking on earlier Fish attempts. This snapshot does not claim a newly confirmed billing diagnosis for the present trigger; it records only the observable result: no actual final audio file was produced before snapshot completion.

## Assistant-created fictional material in this run

After the audio attempt, the assistant continued the corrected first-book line from the exact ending of:

- `Семейный пантеон/Семейный пантеон. Начало. Книга первая/11_Тот_кто_остался.md`

and created the next sequential literary chapter:

- `Семейный пантеон/Семейный пантеон. Начало. Книга первая/12_Страж_который_не_слезал.md`

The chapter continues the scene with the Great Guardian of the Last Boundary holding the stolen nail. The Guardian is released from a condition imposed through the nail; the nail is recovered; an old Gvozdar mark `three short — one long` is discovered and points toward the next nail; an unknown presence in the Forest responds with the same rhythm.

This material is **fictional provenance only**. It must never be used as factual evidence about real people, motives, events or relationships.

`00_Содержание.md` was updated to include chapter 12 and the new current plot endpoint.

## Status at end of snapshot

- First-book literary line: continues through chapter `12_Страж_который_не_слезал.md` plus the earlier combined-book scenes documented by `00_Содержание.md`.
- First-book audio-ready: Part 01 `Семейная связь`.
- First-book actually voiced: NONE confirmed.
- Earliest unvoiced first-book part: Part 01 `Семейная связь`.
- Next literary continuation after this run: chapter 13, from the answering rhythm in the Forest of the Boundary.
