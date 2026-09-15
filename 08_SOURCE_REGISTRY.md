# Реестр источников

| ID | Дата/период | Тип | Участники | Краткое содержание | Путь/ссылка | Статус |
|---|---|---|---|---|---|---|
| SRC-0001 | до 2026-05 | project-package | Гвоздарь, Крис, др. | Базовый комбинированный мастер и аналитические документы | `09_COMBINED_MASTER.md`, `01_PROJECT_CORE.md`, `02_TIMELINE.md`, `03_HYPOTHESES_AND_CONFIDENCE.md` | imported-working |
| SRC-0002 | 2026-04-29 и далее по файлу | text-transcript | Гвоздарь, Kriss | Текстовая ветка переписки | `sources/Ветка · Ветка · Флирт и доверие.txt` | migrated-text |
| SRC-0003 | 2026-04/05 и далее | chat-export | Гвоздарь, Kriss | `messages12.html`; исходник 630716 bytes, SHA-256 проверен; сохранён новым exact-v2 XZ multipart | `sources/messages12/exact-v2/` | migrated-lossless-reconstructable; exact-v2-verified |
| SRC-0004 | 2026-06-17–2026-08-02 | project-chat-screenshots | Гвоздарь, Крис | Минск, июльская переписка, больница, сон 30.07, прямая проверка 01.08, повторные «Ау?» 02.08 | `kris/2026-06-17_to_2026-08-02_UPDATE.md`; `sources/screenshots/original_manifest.csv` | reviewed; originals-binary-hard-gate |
| SRC-0005 | 2026-05 | analysis-log | проект | Журнал смещения гипотезы после майских данных | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` | imported-working |
| SRC-0006 | текущий | analysis-current | проект | Текущая рабочая гипотеза | `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` | imported-working |
| SRC-0007 | локальный физический архив | screenshot-manifest | проект | 161 уникальный канонический скриншот, имена/размеры/SHA-256/геометрия/формат | `sources/screenshots/original_manifest.csv` | verified-manifest; originals-binary-hard-gate |
| SRC-0008 | локальный физический архив | screenshot-preview-archive | проект | Оптимизированные WebP-копии / partial bundles | `sources/screenshots/optimized/`; `sources/screenshots/bundles/` | partial-migration |
| SRC-0009 | локальный физический архив | video | проект | `1000029050.mp4`, size/SHA зарегистрированы, raw bytes недоступны | `sources/video/README.md` | binary-hard-gate |
| SRC-0010 | до синхронизации 02.08 | project-baseline | проект | Исходное локальное состояние рабочих документов до новой синхронизации | `archive/baseline/` | content-archived |
| SRC-0011 | 2026-08-03 | project-chat-screenshots | Гвоздарь, Крис | Выписка, Луна/ветклиника, плохое настроение, подробный вечерний апдейт | `kris/2026-08-03_UPDATE.md`; `sources/screenshots/live/2026-08-03_manifest.csv` | reviewed; current-upload-binary-hard-gate |
| SRC-0012 | 2026-08-04–05 | project-chat-screenshot | Гвоздарь, Крис | Усталость после ветеринарки, уважение границы, «Пиши завтра» как явное продолжение контакта | `kris/2026-08-04_to_05_UPDATE.md`; `sources/screenshots/live/2026-08-04_to_05_manifest.csv` | reviewed; current-upload-binary-hard-gate |
| SRC-0013 | текущий чат, зафиксирован 2026-09-15 | chatgpt-chat-archive | Гвоздарь, ChatGPT | Доступный модели контекст текущего чата; `Skipped`-участки реконструированы и не считаются дословной стенограммой | `sources/chatgpt/2026-09-15_CURRENT_CHAT_ARCHIVE.md`; `sources/chatgpt/2026-09-15_CHAT_ARCHIVE_DELTA_AFTER_TRANSFER.md` | migrated-text; mixed-verbatim-reconstructed |
| SRC-0014 | 2026-09-15 | failed-binary-transfer | проект/текущий чат | Ошибочный snapshot: ожидалось 98456 bytes, фактически GitHub blob 8138 bytes; удалён после проверки | Git history, удалённый `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz` | failed-and-removed |
| SRC-0015 | 2026-09-15 | migration-audit | проект | Evidence-based проверка физической полноты переноса и hard gates | `MIGRATION_AUDIT_2026-09-15.md`; `MIGRATION_STATUS.md` | verified-audit |
| SRC-0016 | 2026-09-15 | generated-md+zip | проект | Таймлайн март–апрель как MD и исходный generated ZIP | `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.md`; `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.zip` | md-migrated; zip-byte-exact-verified |
| SRC-0017 | 2026-09-15 | file-inventory | проект/чат | Текущий inventory: 17 old MP4 + generated ZIP + 17 Project-backed source files | `sources/chatgpt/PROJECT_FILE_INVENTORY_2026-09-15.md` | verified-inventory |
| SRC-0018 | 2026-09-15 | project-source-snapshot | проект | Три разные Project-source версии с одинаковым display-name `Психология отношений с Крис.txt`, сохранены под уникальными именами | `sources/project_snapshot_2026-09-15/Психология_отношений_с_Крис_variant_A.txt`; `...variant_B.txt`; `...variant_C.txt` | migrated-text |
| SRC-0019 | 2026-09-15 | project-source-snapshot | проект | Дополнительная ветка `Ветка · Ветка · Ветка · Ветка · Флирт и доверие.txt` | `sources/project_snapshot_2026-09-15/Ветка_Ветка_Ветка_Ветка_Флирт_и_доверие.txt` | migrated-text |
| SRC-0020 | 2026-09-15 | old-upload-video-set | проект/чат | 17 старых MP4 отображаются Files surface, но raw backing bytes недоступны; materialize и Library-copy проверены на классе и не сработали | `BLOCKED_RAW_FILES_2026-09-15.md`; issue #12 | binary-hard-gate |

## Статусы
- `migrated-text` — текст реально хранится в GitHub;
- `migrated-lossless-reconstructable` — исходные байты могут быть восстановлены из физически записанного и проверенного архива;
- `exact-v2-verified` — новый canonical exact multipart проверен по размерам, Git blob SHA и исходным контрольным суммам;
- `zip-byte-exact-verified` — ZIP записан точным Git blob, идентичность подтверждена Git SHA + локальным SHA-256;
- `failed-and-removed` — ошибочный неполный artifact выявлен и удалён из рабочей ветки; история сохранена Git;
- `verified-manifest` — manifest проверен, но не заменяет сами бинарники;
- `verified-inventory` — список доступных/недоступных файлов подтверждён Files surface и repository evidence;
- `partial-migration` — часть содержимого перенесена, полный набор не закрыт;
- `binary-hard-gate` / `originals-binary-hard-gate` — raw bytes отсутствуют в доступной файловой поверхности; физический перенос невозможен без повторного источника;
- `reviewed` — источник просмотрен и использован;
- `mixed-verbatim-reconstructed` — часть текста дословная, недоступные места восстановлены по контексту как REPORT.

## Правило
Статус источника описывает **физическую сохранность**, а не истинность психологической интерпретации. Manifest или запись в реестре не равны физическому переносу exact bytes. `FACT`, `REPORT`, `HYPOTHESIS`, `CONCLUSION` и `UNKNOWN` не повышаются по статусу только потому, что источник архивирован.