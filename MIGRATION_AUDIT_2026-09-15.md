# Migration audit — 2026-09-15

## Objective
Проверить фактическое выполнение переноса текущего чата и связанных файлов в GitHub.

## Evidence rule
`DONE` допускается только при наблюдаемом доказательстве физического наличия данных в GitHub. Manifest, описание или локально подготовленный файл не равны переносу байтов в репозиторий.

## Подтверждено
- `sources/chatgpt/2026-09-15_CURRENT_CHAT_ARCHIVE.md` присутствует в GitHub.
- `sources/chatgpt/2026-09-15_CHAT_ARCHIVE_DELTA_AFTER_TRANSFER.md` присутствует в GitHub.
- `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.md` присутствует отдельно, размер 12773 bytes.
- `sources/chatgpt/02_Хронология_Крис.txt` присутствует.
- `sources/chatgpt/07_Ключевые_цитаты.txt` присутствует.
- legacy-набор `sources/messages12/b64/` неполон: `part03` отсутствует.

## Критическая поправка по exact-byte bundle
В предыдущей версии этого файла было ошибочно указано, что
`sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz`
имеет размер 98456 bytes и содержит полный exact-byte snapshot.

Фактическая проверка GitHub contents показывает для файла, реально находящегося в ветке:
- размер: **8138 bytes**;
- Git blob SHA: `b09281144681b90372fa3bbf91ca89180baf2ba3`.

Коммит `21d3e34cab5df9f60407ec3545e6e87988d6c7ed` изменил `08_SOURCE_REGISTRY.md`, но не заменил бинарный tar.xz. Поэтому утверждение `verified-exact-byte-bundle` было ложноположительным.

## Project-backed files
17 Project-backed файлов удалось получить локально через Files/materialize. Это подтверждает, что они были доступны рабочей среде на момент аудита, но само по себе **не доказывает**, что их exact bytes записаны в GitHub.

`messages12.html` был локально materialized:
- размер: **630716 bytes**;
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Поскольку legacy multipart неполон, а текущий tar.xz в GitHub не соответствует заявленному full bundle, exact-byte сохранность `messages12.html` в GitHub сейчас **не подтверждена**.

## MP4
Текущая Files surface показывает 17 старых uploaded MP4. Попытка materialize первых пяти вернула ошибку `The requested Library file does not have a downloadable backing file yet.`

Статус: **BLOCKED_BY_HARD_GATE** до повторной загрузки или появления доступного raw source.

## Скриншоты
В репозитории есть manifest для 161 канонического скриншота и часть производных данных. Полный набор exact original bytes не подтверждён, а raw screenshot files на текущей Files surface недоступны.

Статус: **BLOCKED_BY_HARD_GATE** до предоставления исходных изображений/архива.

## Generated ZIP
`26_TIMELINE_MARCH_APRIL_2026.zip` существует как generated файл текущего чата, но отдельный подтверждённый binary blob ZIP в GitHub не найден. MD из него перенесён отдельно.

## Completion matrix
| Requirement | Status |
|---|---|
| Текстовый архив доступного контекста чата | VERIFIED |
| Post-transfer delta | VERIFIED |
| `26_TIMELINE_MARCH_APRIL_2026.md` | VERIFIED |
| Хронология / ключевые цитаты | VERIFIED |
| 17 Project-backed файлов exact-byte snapshot | NOT CONFIRMED IN GITHUB |
| `messages12.html` exact bytes | NOT CONFIRMED IN GITHUB |
| Generated ZIP binary | NOT CONFIRMED IN GITHUB |
| 17 старых MP4 | BLOCKED_BY_HARD_GATE |
| 161 original screenshots | BLOCKED_BY_HARD_GATE |
| Legacy messages12 multipart | FAILED AS COMPLETION PROOF |

## Final verdict
**PARTIALLY VERIFIED / NOT FULLY COMPLETE.**

Полный `DONE` запрещён, пока не появится доказательство физического наличия оставшихся exact bytes в GitHub.