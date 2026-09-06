# Pantheon session snapshot — part 20

DATE: 2026-09-06
SOURCE_CLASS: mixed chat provenance snapshot
PROJECT: relationship-psychology / Семейный пантеон

## User directives added since part 19

### Audio completion rule repeated

The user again explicitly required that:

- `audio-ready` is only a preparation state and never counts as actual voicing;
- a part counts as voiced only after a real playable audio file (MP3/WAV/other actual sound file) has been created;
- the earliest still-unvoiced ready part has priority;
- if actual synthesis is technically impossible in the current run, the part must remain clearly marked `НЕ ОЗВУЧЕНА`; preparation may continue, but it must not be called completed;
- after the audio attempt, literary work continues strictly in sequence, without skipping ahead;
- literary canon, audio scripts and final audio files remain separate;
- all substantive project messages from the working chat are saved into `sources/chat/` before each run finishes;
- user project instructions are directives; user descriptions of real events remain `user-report` until corroborated; assistant-written fiction is provenance only and never evidence of real events, motives or feelings;
- if a full literary text already exists canonically, the chat snapshot should point to it rather than duplicating the entire canon text.

These are project directives, not claims about real third-party events.

## Audio attempt in this run

The earliest unvoiced first-book item remained:

- literary source: `Семейный пантеон/Семейный пантеон. Начало. Книга первая/01_Семейная_связь.md`
- audio script: `narrative/audio_scripts/BOOK1_01_FAMILY_CONNECTION_FISH.md`
- status: `audio-ready`, but **НЕ ОЗВУЧЕНА** until real audio exists.

Repository inspection of GitHub Actions run `33845691042` showed that the previous Fish render had not failed because of billing: its runner started successfully, the secret was present, and the render step failed inside `render_fish_book1.py` because the parser split the script at the literal `---` token mentioned in a header instruction and interpreted part of that header as a speaker.

The parser was corrected in:

- `narrative/audio_tools/render_fish_book1.py`

Commit: `59aae4a17c13bb001ad1416836aa796bc6845c78`

That change automatically triggered GitHub Actions run `34016136098` (`Render Book 1 Part 01 with Fish Audio`). The parser then successfully reached the first real TTS block, proving the separator bug was removed. Fish Audio itself returned HTTP `401` with `{"status":401,"message":"Invalid Token"}` on the first synthesis request.

Therefore the current blocker is specifically the repository secret/API credential accepted into the workflow environment but rejected by Fish Audio as an invalid token. No MP3/WAV was produced and the commit-audio step was skipped.

Expected final paths remain absent at snapshot time:

- `narrative/audio/pantheon/book1/Pantheon_BOOK1_P01_FAMILY_CONNECTION_FINAL.mp3`
- `narrative/audio/pantheon/book1/Pantheon_BOOK1_P01_FAMILY_CONNECTION_FINAL.wav`

Accordingly **Book 1 Part 01 remains НЕ ОЗВУЧЕНА**.

## Assistant-created fictional material in this run

After the factual audio attempt failed, literary work continued from the exact current first-book endpoint, chapter 12.

The existing draft:

- `narrative/drafts/pantheon_ch13_three_short_one_long.md`

was reviewed. Its own author note warned that the line where Кри́с said she had already seen the mark required an earlier planted callback. To avoid retroactively inventing an earlier canonical observation, the canonical version was adjusted so Кри́с proposes checking an old wooden outbuilding as an evidence-preserving surface and discovers the matching mark there for the first time.

The next sequential canonical chapter was then created:

- `Семейный пантеон/Семейный пантеон. Начало. Книга первая/13_Три_коротких_один_длинный.md`

Full text is stored only in that canonical literary file; this source snapshot does not duplicate it.

`00_Содержание.md` was updated. The current literary endpoint is now: after the answering rhythm from the Forest of the Boundary, the group returns to the human world; a second `three short — one long` mark is found on an old wooden outbuilding; contact with it causes Gvozdar to say involuntarily, `После третьего раза метку уже не снимали`; the next vector is an archive check into the mark and the meaning of the “third time”.

All of this chapter material is **fictional provenance only**. It is not factual evidence about real people, real places, motives, feelings or events.

## Status at end of snapshot

- First-book literary line: canonically continues through `13_Три_коротких_один_длинный.md` plus the earlier combined-book material indexed by `00_Содержание.md`.
- First-book audio-ready: Part 01 `Семейная связь`.
- First-book actually voiced: NONE confirmed.
- Earliest unvoiced first-book part: Part 01 `Семейная связь`.
- Current actual audio blocker: Fish Audio returns HTTP 401 `Invalid Token` for the configured `FISH_API_KEY`; no playable final file exists.
- Next literary continuation after this run: chapter 14, beginning with the archive check into the mark and the phrase about the “third time”.
