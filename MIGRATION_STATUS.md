# Migration status

Последнее обновление: **15.09.2026**.

## Цель
Перенести физически доступный проект в репозиторий с сохранением рабочих документов, исходных текстов, медиа и истории Git. Статус `migrated` используется только при наличии физического содержимого в GitHub напрямую либо в проверяемой lossless-реконструируемой форме.

## VERIFIED в GitHub
- рабочая база проекта присутствует в ветке `live-updates-2026-08`;
- `sources/chatgpt/2026-09-15_CURRENT_CHAT_ARCHIVE.md`;
- `sources/chatgpt/2026-09-15_CHAT_ARCHIVE_DELTA_AFTER_TRANSFER.md`;
- `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.md`;
- `sources/chatgpt/02_Хронология_Крис.txt`;
- `sources/chatgpt/07_Ключевые_цитаты.txt`;
- `sources/chatgpt/PROJECT_FILE_INVENTORY_2026-09-15.md`;
- три разные Project-source версии `Психология отношений с Крис.txt` под уникальными именами в `sources/project_snapshot_2026-09-15/`;
- дополнительная ветка `Ветка · Ветка · Ветка · Ветка · Флирт и доверие.txt`;
- читаемое содержимое `Гороскоп для Скорпиона.txt` двумя последовательными частями + `RECONSTRUCT.md`;
- `26_TIMELINE_MARCH_APRIL_2026.zip` как **точный бинарный Git blob**;
- `messages12.html` как **lossless-reconstructable exact-v2** архив.

## Исправление ошибочного binary bundle
Ранее путь `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz` был ошибочно объявлен полным snapshot размером 98456 байт. Фактическая проверка GitHub показала **8138 байт**. Усечённый artifact удалён из рабочей ветки; его история сохранена в Git и не считается доказательством миграции.

## `messages12.html` — VERIFIED
Исходный Project source:
- размер HTML: **630716 байт**;
- строк при аудите: **27380**;
- SHA-256 HTML: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Старый `sources/messages12/b64/` действительно неполон и не используется как completion evidence.

Создан новый канонический архив:
`sources/messages12/exact-v2/`

Он содержит 5 последовательных бинарных частей: 12000 + 12000 + 12000 + 12000 + 6856 = **54856 байт** XZ.

SHA-256 объединённого XZ:
`b3ad5c8bd5ea53ebb494ab6b1dbe7e7b1a32df91684d19418a8f4ebdf9d1fa45`.

GitHub подтвердил ожидаемые Git blob SHA для всех пяти частей и размеры частей в дереве. Команды реконструкции и контрольные суммы находятся в `sources/messages12/exact-v2/README.md`.

Статус: **VERIFIED / LOSSLESS-RECONSTRUCTABLE**.

## Generated ZIP — VERIFIED
`26_TIMELINE_MARCH_APRIL_2026.zip`:
- размер: **4530 байт**;
- SHA-256: `692d0093bf05864162dfe76bff3a5c0d17d371bb93adb3529d4608443aab7987`;
- ожидаемый Git blob SHA: `e7d709ffe876eee831c8d5cb81a479015cb4073f`;
- GitHub `create_blob` вернул тот же Git blob SHA, после чего blob был прикреплён к `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.zip`.

Статус: **VERIFIED BYTE-EXACT**.

## Скриншоты — HARD GATE
В репозитории есть:
- `sources/screenshots/original_manifest.csv` для **161** канонического скриншота;
- часть optimized/bundle данных;
- документация, имена, размеры и хэши.

Но физические exact bytes всех 161 originals не доступны текущей Files surface и не подтверждены в GitHub. Manifest сам по себе не является переносом бинарников.

Статус: **BLOCKED_BY_HARD_GATE** до повторного предоставления оригинальных изображений либо архива с ними.

## Видео — HARD GATE
Текущая Files surface показывает **17 старых uploaded MP4**. Попытка `materialize` первых пяти вернула `The requested Library file does not have a downloadable backing file yet.` Независимая попытка скопировать первый MP4 через Library закончилась `source_file_not_found / exact exported file unavailable or expired`. Это подтверждает не обычную трудность, а отсутствие доступных raw bytes у старого upload-класса.

Также ранее зарегистрированный `1000029050.mp4` (2752754 байт; SHA-256 `7257e6c3ab58295160bb41cb29ffc18e7f8e5546c4d352ac20ba9ffaaade7bf2`) остаётся без доступного бинарника.

Статус: **BLOCKED_BY_HARD_GATE** до повторного предоставления raw MP4/архива.

## Итог по Definition of Done
- доступные текстовые/проектные документы: **VERIFIED**;
- архив текущего чата и delta: **VERIFIED**;
- `messages12.html`: **VERIFIED LOSSLESS-RECONSTRUCTABLE**;
- generated timeline ZIP: **VERIFIED BYTE-EXACT**;
- исходные 161 screenshots: **BLOCKED_BY_HARD_GATE**;
- 17 старых MP4 + `1000029050.mp4`: **BLOCKED_BY_HARD_GATE**.

## Текущий общий статус
**ALL INDEPENDENT / PHYSICALLY ACCESSIBLE WORK VERIFIED; ONLY RAW-MEDIA HARD GATES REMAIN.**

Полный физический DONE по формулировке «все документы, скриншоты, файлы и т.д.» невозможен без самих недоступных raw media bytes. Это не программный или аналитический блокер: источник байтов отсутствует в доступных поверхностях.
