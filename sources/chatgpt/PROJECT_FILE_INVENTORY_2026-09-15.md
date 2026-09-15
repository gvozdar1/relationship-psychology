# Current Project / chat file inventory — 2026-09-15

Источник инвентаря: Files surface текущего проекта/чата. Всего обнаружено **35** файлов: 17 old user-uploaded MP4, 1 generated ZIP, 17 Project-backed sources.

## A. Old user-uploaded MP4 — raw bytes currently unavailable

| # | Name | Size bytes | Migration status |
|---:|---|---:|---|
| 1 | `video (2).mp4` | 1437918 | BLOCKED: no downloadable backing file |
| 2 | `video (3).mp4` | 2977147 | BLOCKED: no downloadable backing file |
| 3 | `video (4).mp4` | 1788026 | BLOCKED: no downloadable backing file |
| 4 | `1775173257172.mp4` | 6033784 | BLOCKED: no downloadable backing file |
| 5 | `1775173257210.mp4` | 2487952 | BLOCKED: no downloadable backing file |
| 6 | `video (5).mp4` | 565275 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 7 | `1775173223574.mp4` | 8017053 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 8 | `1775177812987.mp4` | 8122236 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 9 | `1775177813015.mp4` | 1793450 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 10 | `1775177813030.mp4` | 3630642 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 11 | `1775177813054.mp4` | 3852023 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 12 | `1775177813068.mp4` | 1329135 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 13 | `1775177812388.mp4` | 4251938 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 14 | `1775177812520.mp4` | 4459235 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 15 | `1775177812561.mp4` | 3490992 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 16 | `1775177812582.mp4` | 5187035 | BLOCKED: same old-upload source class; raw bytes unavailable |
| 17 | `1775177812610.mp4` | 2593480 | BLOCKED: same old-upload source class; raw bytes unavailable |

Materialization was actually attempted for items 1–5; each returned: `The requested Library file does not have a downloadable backing file yet.`

## B. Generated artifact

| Name | Status |
|---|---|
| `26_TIMELINE_MARCH_APRIL_2026.zip` | ZIP raw binary not independently transferred; extracted MD is VERIFIED in GitHub as `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.md` |

## C. Project-backed source files

These files are readable/materializable from the Project source. Some already have canonical or baseline copies in GitHub; three files share the same display name but are different contents.

| # | Project file | Size bytes | Repository handling |
|---:|---|---:|---|
| 1 | `09_COMBINED_MASTER.md` | 38249 | current Project source available; repo has canonical + baseline history |
| 2 | `00_INDEX.md` | 2890 | repo has canonical + baseline history |
| 3 | `01_PROJECT_CORE.md` | 5713 | repo has canonical + baseline history |
| 4 | `02_TIMELINE.md` | 5175 | repo has canonical + baseline history |
| 5 | `03_HYPOTHESES_AND_CONFIDENCE.md` | 5125 | repo has canonical + baseline history |
| 6 | `05_COMMUNICATION_PROTOCOL.md` | 5226 | repo has canonical + baseline history |
| 7 | `11_STRONGEST_FACTS_AGAINST_HIDDEN_WARM_UNION_WITH_EVGENY.md` | 5406 | repo contains document |
| 8 | `10_STRONGEST_FACTS_FOR_KRIS_TO_GVOZDAR.md` | 6323 | repo contains document |
| 9 | `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` | 5195 | repo contains current/baseline variants |
| 10 | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` | 7255 | repo contains document |
| 11 | `messages12.html` | 630716 | Project raw source readable; legacy GitHub multipart is incomplete (`part03` missing) |
| 12 | `Ветка · Ветка · Флирт и доверие.txt` | 12773 | repo contains source text |
| 13 | `Психология отношений с Крис.txt` — variant A | 3311 | repo contains one 3311-byte source with this display name |
| 14 | `Психология отношений с Крис.txt` — variant B | 1681 | distinct Project source; needs unique archival filename for byte-exact snapshot |
| 15 | `Гороскоп для Скорпиона.txt` | 42730 | Project source readable; not proven byte-for-byte archived in repo |
| 16 | `Психология отношений с Крис.txt` — variant C | 20072 | distinct Project source; needs unique archival filename for byte-exact snapshot |
| 17 | `Ветка · Ветка · Ветка · Ветка · Флирт и доверие.txt` | 15744 | Project source readable; not proven byte-for-byte archived in repo |

## D. Screenshot corpus already known to repository

Repository metadata records **161 canonical screenshots** plus manifests/bundles. The current Files surface does not expose their individual raw image bytes, so physical transfer of all exact originals cannot be re-proven or completed from this session.

## Evidence rule
`manifest exists` ≠ `binary transferred`.
`file is readable from Project` ≠ `byte-exact GitHub copy exists`.
`path exists in GitHub` ≠ `content is the expected complete binary`.

This inventory is intentionally conservative: anything without physical or checksum evidence remains `not confirmed` / `blocked`, not magically promoted to DONE because humans enjoy green checkmarks.
