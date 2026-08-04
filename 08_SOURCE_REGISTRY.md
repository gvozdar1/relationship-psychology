# Реестр источников

| ID | Дата/период | Тип | Участники | Краткое содержание | Путь/ссылка | Статус |
|---|---|---|---|---|---|---|
| SRC-0001 | до 2026-05 | project-package | Гвоздарь, Крис, др. | Базовый комбинированный мастер и аналитические документы | `09_COMBINED_MASTER.md`, `01_PROJECT_CORE.md`, `02_TIMELINE.md`, `03_HYPOTHESES_AND_CONFIDENCE.md` | imported-working |
| SRC-0002 | 2026-04-29 и далее по файлу | text-transcript | Гвоздарь, Kriss | Текстовая ветка переписки | `sources/chats/Ветка · Ветка · Флирт и доверие.txt` | migrated-text |
| SRC-0003 | 2026-04/05 и далее | chat-export | Гвоздарь, Kriss | Полный `messages12.html`; прямой файл плюс резервная lossless-реконструкция | `sources/messages12/messages12.html`; `sources/messages12/` | migrated-direct+verified |
| SRC-0004 | 2026-06-17–2026-08-02 | project-chat-screenshots | Гвоздарь, Крис | Минск, июльская переписка, больница, сон 30.07, прямая проверка 01.08, повторные «Ау?» 02.08 | `kris/2026-06-17_to_2026-08-02_UPDATE.md`; `sources/screenshots/original_manifest.csv` | reviewed; originals-migrated |
| SRC-0005 | 2026-05 | analysis-log | проект | Журнал смещения гипотезы после майских данных | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` | imported-working |
| SRC-0006 | текущий | analysis-current | проект | Текущая рабочая гипотеза | `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` | imported-working |
| SRC-0007 | архив до 02.08 | screenshot-archive | проект | 161 уникальный канонический исходный скриншот + SHA-256/геометрия/формат | `sources/screenshots/originals/`; `sources/screenshots/original_manifest.csv` | migrated-direct+verified |
| SRC-0008 | архив до 02.08 | screenshot-preview-archive | проект | 161 оптимизированная WebP-копия | `sources/screenshots/optimized/` | migrated-direct+verified |
| SRC-0009 | архив до 02.08 | video | проект | `1000029050.mp4`, 2 752 754 байта, SHA-256 `7257e6c3...` | `sources/video/1000029050.mp4` | migrated-direct+verified |
| SRC-0010 | до синхронизации 02.08 | project-baseline | проект | Исходное локальное состояние рабочих документов до новой синхронизации; старый master сохранён byte-exact | `archive/baseline/` | migrated+verified |
| SRC-0011 | 2026-08-03 | project-chat-screenshots | Гвоздарь, Крис | Выписка, Луна/ветклиника, плохое настроение, вечерний подробный апдейт, поездка в Минск 04.08 по ветеринарной теме | `kris/2026-08-03_UPDATE.md`; `sources/screenshots/2026-08-03_manifest.csv` | reviewed; current-upload-binary-pending |

## Статусы
- `migrated-text` — текст реально хранится в GitHub;
- `migrated-direct+verified` — полный исходник реально хранится в GitHub и проверен контрольной суммой/аудитом;
- `migrated+verified` — архивное содержимое сохранено и проверено;
- `current-upload-binary-pending` — новый исходный файл присутствует в текущем проектном чате, его SHA-256 и характеристики зарегистрированы, но бинарник ещё не записан в GitHub;
- `reviewed` — источник просмотрен и использован;
- `conflicting` — есть противоречие;
- `incomplete` — источник неполный.

## Правило
Статус источника описывает **физическую сохранность**, а не истинность психологической интерпретации. `SOURCE` не становится `FACT` автоматически, а `FACT` не доказывает мотив без отдельной `HYPOTHESIS`.
