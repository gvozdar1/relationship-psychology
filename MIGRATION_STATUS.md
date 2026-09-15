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
- `sources/chatgpt/PROJECT_FILE_INVENTORY_2026-09-15.md`;
- три разные Project-source версии `Психология отношений с Крис.txt` сохранены под уникальными именами в `sources/project_snapshot_2026-09-15/`;
- дополнительная ветка `Ветка · Ветка · Ветка · Ветка · Флирт и доверие.txt` сохранена в `sources/project_snapshot_2026-09-15/`;
- читаемое содержимое Project-source `Гороскоп для Скорпиона.txt` сохранено двумя последовательными частями + `RECONSTRUCT.md`;
- manifest/документация по ранее зарегистрированным медиа и источникам.

## Исправление по ошибочному binary bundle
Ранее был создан путь
`sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz`
и ошибочно объявлен полным 98456-byte snapshot.

Фактическая проверка GitHub показала размер **8138 bytes**, то есть перенос был усечён. Неполный artifact **удалён из рабочей ветки**. Его история остаётся в Git для аудита.

Он больше нигде не должен использоваться как доказательство сохранности исходников.

## `messages12.html`
Project source был успешно materialized в рабочей среде:
- размер: **630716 bytes**;
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`;
- читаемый источник содержит **27380 строк**.

Но legacy `sources/messages12/b64/` неполон: отсутствует `part03`.
GitHub connector принимает только текстовое поле `content` и не принимает local file/file_ref напрямую; container/Python bridge во время аудита возвращал инфраструктурную ошибку. Поэтому безопасный byte-exact upload 630716-byte HTML из materialized backing file этим сеансом не доказан.

Статус exact bytes в GitHub: **BLOCKED_BY_TOOL_TRANSFER_GATE / NOT CONFIRMED**.

## Скриншоты
В репозитории есть:
- `sources/screenshots/original_manifest.csv` для 161 канонического скриншота;
- часть optimized/bundle данных;
- документация и контрольные данные.

Физические exact bytes всех 161 originals не подтверждены. Raw screenshot files недоступны текущей Files surface.

Статус: **BLOCKED_BY_HARD_GATE** до повторного предоставления исходных изображений/архива.

## Видео
Текущая Files surface показывает 17 старых uploaded MP4. Попытка materialize первых пяти вернула `The requested Library file does not have a downloadable backing file yet.` Полные байты этих видео не доступны модели для записи в GitHub. Остальные 12 относятся к тому же old-upload классу и не считаются перенесёнными без raw bytes.

Также ранее зарегистрированный `1000029050.mp4` остаётся без подтверждённого бинарника.

Статус: **BLOCKED_BY_HARD_GATE**.

## Generated ZIP
`26_TIMELINE_MARCH_APRIL_2026.zip` существует как generated файл текущего чата. Его MD-содержимое перенесено отдельно и проверено, но connector не предоставляет безопасный прямой binary-file upload из этого backing file в GitHub.

Статус ZIP binary: **BLOCKED_BY_TOOL_TRANSFER_GATE / NOT CONFIRMED**.

## Что было сделано вместо ложного DONE
- удалён усечённый tar.xz;
- исправлены audit/status/registry;
- сохранены читаемые текстовые Project-source документы, которые можно было безопасно перенести без подмены байтов;
- создан полный inventory 35 файлов текущей surface;
- отдельно зафиксированы все недоступные бинарники и причина блокировки.

## Полный аудит
См. `MIGRATION_AUDIT_2026-09-15.md`.

## Итоговый статус
**MAXIMUM REACHED WITH CURRENT TOOL ACCESS / NOT FULLY COMPLETE.**

Всё, что можно было надёжно записать в GitHub через доступные текстовые операции, перенесено или зарегистрировано. Полный физический `DONE` запрещён до появления raw bytes недостающих видео/скриншотов либо файлового upload-моста для exact `messages12.html` и ZIP.