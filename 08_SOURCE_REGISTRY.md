# Реестр источников

| ID | Дата/период | Тип | Участники | Краткое содержание | Путь/ссылка | Статус |
|---|---|---|---|---|---|---|
| SRC-0001 | до 2026-05 | project-package | Гвоздарь, Крис, др. | Базовый комбинированный мастер и аналитические документы | `09_COMBINED_MASTER.md`, `01_PROJECT_CORE.md`, `02_TIMELINE.md`, `03_HYPOTHESES_AND_CONFIDENCE.md` | imported-working |
| SRC-0002 | 2026-04-29 и далее по файлу | text-transcript | Гвоздарь, Kriss | Текстовая ветка переписки | `sources/Ветка · Ветка · Флирт и доверие.txt` | migrated-text |
| SRC-0003 | 2026-04/05 и далее | chat-export | Гвоздарь, Kriss | `messages12.html`; legacy XZ/base64 набор неполон из-за отсутствующего part03, но exact исходник сохранён в SRC-0014 | `sources/messages12/`; `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz` | preserved-via-SRC-0014; legacy-b64-incomplete |
| SRC-0004 | 2026-06-17–2026-08-02 | project-chat-screenshots | Гвоздарь, Крис | Минск, июльская переписка, больница, сон 30.07, прямая проверка 01.08, повторные «Ау?» 02.08 | `kris/2026-06-17_to_2026-08-02_UPDATE.md`; `sources/screenshots/original_manifest.csv` | reviewed; originals-binary-pending |
| SRC-0005 | 2026-05 | analysis-log | проект | Журнал смещения гипотезы после майских данных | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` | imported-working |
| SRC-0006 | текущий | analysis-current | проект | Текущая рабочая гипотеза | `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` | imported-working |
| SRC-0007 | локальный физический архив | screenshot-manifest | проект | 161 уникальный канонический скриншот, имена/размеры/SHA-256/геометрия/формат | `sources/screenshots/original_manifest.csv` | verified-manifest |
| SRC-0008 | локальный физический архив | screenshot-preview-archive | проект | Оптимизированные WebP-копии | `sources/screenshots/optimized/`; `sources/screenshots/bundles/` | partial-migration |
| SRC-0009 | локальный физический архив | video | проект | `1000029050.mp4`, SHA-256 зарегистрирован | `sources/video/README.md` | binary-pending |
| SRC-0010 | до синхронизации 02.08 | project-baseline | проект | Исходное локальное состояние рабочих документов до новой синхронизации | `archive/baseline/` | content-archived; byte-exact-09-pending |
| SRC-0011 | 2026-08-03 | project-chat-screenshots | Гвоздарь, Крис | Выписка, Луна/ветклиника, плохое настроение, подробный вечерний апдейт | `kris/2026-08-03_UPDATE.md`; `sources/screenshots/live/2026-08-03_manifest.csv` | reviewed; current-upload-binary-pending |
| SRC-0012 | 2026-08-04–05 | project-chat-screenshot | Гвоздарь, Крис | Усталость после ветеринарки, уважение границы, «Пиши завтра» как явное продолжение контакта | `kris/2026-08-04_to_05_UPDATE.md`; `sources/screenshots/live/2026-08-04_to_05_manifest.csv` | reviewed; current-upload-binary-pending |
| SRC-0013 | текущий чат, зафиксирован 2026-09-15 | chatgpt-chat-archive | Гвоздарь, ChatGPT; обсуждение Крис/Евгения | Весь доступный модели контекст текущего чата: ретроспектива связи, март–апрель, Минск, Евгений, флирт, эмоциональный срыв, поездка, протоколы и рабочие гипотезы. `Skipped`-участки восстановлены по контексту и не считаются дословной стенограммой. | `sources/chatgpt/2026-09-15_CURRENT_CHAT_ARCHIVE.md` | migrated-text; mixed-verbatim-reconstructed |
| SRC-0014 | 2026-09-15 | exact-byte-project-snapshot | проект/текущий чат | 17 raw Project-backed файлов + generated ZIP/MD, включая точные байты `messages12.html`; внутри `MANIFEST.json` | `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz` | verified-exact-byte-bundle |
| SRC-0015 | 2026-09-15 | migration-audit | проект | Проверка фактической полноты переноса, выявление missing `messages12 part03`, недоступных MP4 и неполного набора screenshot originals | `MIGRATION_AUDIT_2026-09-15.md` | verified-audit |

## Статусы
- `migrated-text` — текст реально хранится в GitHub;
- `verified-exact-byte-bundle` — точные байты физически записаны в GitHub внутри архива с manifest/SHA-256;
- `preserved-via-SRC-0014` — исходник физически сохранён через новый exact-byte bundle;
- `legacy-b64-incomplete` — исторический multipart-набор неполон и не должен использоваться как proof-of-completion;
- `verified-manifest` — реестр локальных первичных файлов проверен, но manifest не заменяет сами бинарники;
- `partial-migration` — часть физического содержимого уже записана, весь набор ещё не закрыт;
- `binary-pending` — первичный бинарник зарегистрирован, но полное содержимое ещё не перенесено;
- `current-upload-binary-pending` — исходник зарегистрирован/описан, но его бинарные байты не подтверждены в GitHub;
- `reviewed` — источник просмотрен и использован;
- `mixed-verbatim-reconstructed` — часть текста дословная, а недоступные как стенограмма места восстановлены по доступному контексту и должны использоваться как REPORT/контекст;
- `conflicting` — есть противоречие;
- `incomplete` — источник неполный.

## Правило
Статус источника описывает **физическую сохранность**, а не истинность психологической интерпретации. `SOURCE` не становится `FACT` автоматически, а `FACT` не доказывает мотив без отдельной `HYPOTHESIS`.
