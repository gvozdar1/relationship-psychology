# Migration status

Последнее обновление: **15.09.2026**.

## Цель
Перенести физически доступный проект в репозиторий с сохранением рабочих документов, исходных текстов, медиа и истории Git.

## Подтверждено в GitHub
- рабочая база проекта присутствует в ветке;
- `sources/chatgpt/2026-09-15_CURRENT_CHAT_ARCHIVE.md`;
- `sources/chatgpt/2026-09-15_CHAT_ARCHIVE_DELTA_AFTER_TRANSFER.md`;
- `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.md`;
- `sources/chatgpt/02_Хронология_Крис.txt`;
- `sources/chatgpt/07_Ключевые_цитаты.txt`;
- manifest/документация по ранее зарегистрированным медиа и источникам.

## Исправление по exact-byte bundle
Ранее этот статус ошибочно утверждал, что файл
`sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz`
содержит полный snapshot размером 98456 bytes.

Фактически GitHub показывает для реально записанного blob:
- размер: **8138 bytes**;
- Git blob SHA: `b09281144681b90372fa3bbf91ca89180baf2ba3`.

Поэтому полный exact-byte snapshot 17 Project-backed файлов **не подтверждён как записанный в GitHub**.

## `messages12.html`
Исходный файл удалось materialize локально в ходе аудита:
- размер: **630716 bytes**;
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Но legacy `sources/messages12/b64/` неполон: отсутствует `part03`.
Текущий 8138-byte tar.xz не является доказательством наличия полного HTML.

Статус exact bytes в GitHub: **NOT CONFIRMED**.

## Скриншоты
В репозитории есть:
- `sources/screenshots/original_manifest.csv` для 161 канонического скриншота;
- часть optimized/bundle данных;
- документация и контрольные данные.

Физические exact bytes всех 161 originals не подтверждены. Raw screenshot files недоступны текущей Files surface.

Статус: **BLOCKED_BY_HARD_GATE** до повторного предоставления исходных изображений/архива.

## Видео
Текущая Files surface показывает 17 старых uploaded MP4. Попытка materialize первых пяти вернула ошибку отсутствующего downloadable backing file. Полные байты этих видео не доступны модели для записи в GitHub.

Также ранее зарегистрированный `1000029050.mp4` остаётся без подтверждённого бинарника.

Статус: **BLOCKED_BY_HARD_GATE**.

## Generated ZIP
`26_TIMELINE_MARCH_APRIL_2026.zip` существует как generated файл текущего чата. Его MD-содержимое перенесено отдельно, но отдельный binary ZIP blob в GitHub не подтверждён.

Статус: **NOT CONFIRMED IN GITHUB**.

## Полный аудит
См. `MIGRATION_AUDIT_2026-09-15.md`.

## Итоговый статус
**PARTIALLY VERIFIED / NOT FULLY COMPLETE**.

Подтверждённые текстовые артефакты перенесены. Полный физический `DONE` запрещён до появления доступных raw bytes недостающих бинарников и подтверждения exact-byte Project snapshot.