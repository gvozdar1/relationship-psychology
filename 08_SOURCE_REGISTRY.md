# Реестр источников

| ID | Дата/период | Тип | Участники | Краткое содержание | Путь/ссылка | Статус |
|---|---|---|---|---|---|---|
| SRC-0001 | до 2026-05 | project-package | Гвоздарь, Крис, др. | Базовый комбинированный мастер и аналитические документы | `09_COMBINED_MASTER.md`, `01_PROJECT_CORE.md`, `02_TIMELINE.md`, `03_HYPOTHESES_AND_CONFIDENCE.md` | imported-working |
| SRC-0002 | 2026-04-29 и далее по файлу | text-transcript | Гвоздарь, Kriss | Текстовая ветка переписки | `sources/Ветка · Ветка · Флирт и доверие.txt` | migrated-text |
| SRC-0003 | 2026-04/05 и далее | chat-export | Гвоздарь, Kriss | Полный `messages12.html`, сохранённый без потерь через XZ + base64 | `sources/messages12/` | migrated-lossless-reconstructable |
| SRC-0004 | 2026-06-17–2026-08-02 | project-chat-screenshots | Гвоздарь, Крис | Минск, июльская переписка, больница, сон 30.07, прямая проверка 01.08, повторные «Ау?» 02.08 | `kris/2026-06-17_to_2026-08-02_UPDATE.md`; `sources/screenshots/original_manifest.csv` | reviewed; originals-binary-pending |
| SRC-0005 | 2026-05 | analysis-log | проект | Журнал смещения гипотезы после майских данных | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` | imported-working |
| SRC-0006 | текущий | analysis-current | проект | Текущая рабочая гипотеза | `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` | imported-working |
| SRC-0007 | локальный физический архив | screenshot-manifest | проект | 161 уникальный канонический скриншот, имена/размеры/SHA-256/геометрия/формат | `sources/screenshots/original_manifest.csv` | verified-manifest |
| SRC-0008 | локальный физический архив | screenshot-preview-archive | проект | Оптимизированные WebP-копии | `sources/screenshots/optimized/`; `sources/screenshots/bundles/` | partial-migration |
| SRC-0009 | локальный физический архив | video | проект | `1000029050.mp4`, SHA-256 зарегистрирован | `sources/video/README.md` | binary-pending |
| SRC-0010 | до синхронизации 02.08 | project-baseline | проект | Исходное локальное состояние рабочих документов до новой синхронизации | `archive/baseline/` | content-archived; byte-exact-09-pending |
| SRC-0011 | 2026-08-03 | project-chat-screenshots | Гвоздарь, Крис | Выписка, Луна/ветклиника, плохое настроение, подробный вечерний апдейт | `kris/2026-08-03_UPDATE.md`; `sources/screenshots/live/2026-08-03_manifest.csv` | reviewed; current-upload-binary-pending |
| SRC-0012 | 2026-08-04–05 | project-chat-screenshot | Гвоздарь, Крис | Усталость после ветеринарки, уважение границы, «Пиши завтра» как явное продолжение контакта | `kris/2026-08-04_to_05_UPDATE.md`; `sources/screenshots/live/2026-08-04_to_05_manifest.csv` | reviewed; current-upload-binary-pending |

## Статусы
- `migrated-text` — текст реально хранится в GitHub;
- `migrated-lossless-reconstructable` — полный исходник побайтово восстанавливается из записанных частей и проверяется SHA-256;
- `verified-manifest` — реестр локальных первичных файлов проверен, но manifest не заменяет сами бинарники;
- `partial-migration` — часть физического содержимого уже записана, весь набор ещё не закрыт;
- `binary-pending` — первичный бинарник зарегистрирован, но полное содержимое ещё не перенесено;
- `current-upload-binary-pending` — новый исходник присутствует в текущей рабочей среде и зарегистрирован по размеру/SHA-256, но его бинарное содержимое ещё не записано в GitHub;
- `reviewed` — источник просмотрен и использован;
- `conflicting` — есть противоречие;
- `incomplete` — источник неполный.

## Правило
Статус источника описывает **физическую сохранность**, а не истинность психологической интерпретации. `SOURCE` не становится `FACT` автоматически, а `FACT` не доказывает мотив без отдельной `HYPOTHESIS`.
