# Проект: Психология отношений с Крис — индекс пакета

## Назначение
Этот пакет — рабочая база знаний для проекта. Он собран так, чтобы:
- отделять **факты** от **выводов** и **гипотез**;
- хранить не только сюжет, но и **логику анализа**;
- давать будущему чату/проекту устойчивое ядро, а не хаотичный набор реплик.

## Как использовать
1. Сначала читать `01_PROJECT_CORE.md`.
2. Потом читать `02_TIMELINE.md`.
3. Для оценки текущей ситуации — `03_HYPOTHESES_AND_CONFIDENCE.md`.
4. Для практических ходов — `05_COMMUNICATION_PROTOCOL.md` и `06_DECISION_MATRIX.md`.
5. Для обновления проекта после новых событий — `07_UPDATE_PROTOCOL.md`.
6. Для проверки источников — `08_SOURCE_REGISTRY.md`.
7. Для физической полноты миграции — `MIGRATION_STATUS.md`, `MIGRATION_AUDIT_2026-09-15.md` и `sources/chatgpt/PROJECT_FILE_INVENTORY_2026-09-15.md`.

## Список файлов
- `01_PROJECT_CORE.md` — ядро проекта, сущности, роли, границы.
- `02_TIMELINE.md` — хронология по этапам.
- `03_HYPOTHESES_AND_CONFIDENCE.md` — главные версии и их вес.
- `04_SIGNAL_MATRIX.md` — признаки, маркеры, фазы.
- `05_COMMUNICATION_PROTOCOL.md` — как общаться и чего не делать.
- `06_DECISION_MATRIX.md` — что делать при разных сценариях.
- `07_UPDATE_PROTOCOL.md` — как дополнять базу новыми событиями.
- `08_SOURCE_REGISTRY.md` — перечень источников и их физический статус.
- `09_COMBINED_MASTER.md` — главный источник истины проекта.

## Принцип документации
Используются метки:
- **ФАКТ** — прямо сказано/наблюдалось;
- **ВЫВОД** — логическое следствие;
- **ГИПОТЕЗА** — версия без полного доказательства;
- **ОТКРЫТЫЙ ВОПРОС** — что не закрыто;
- **ПРАВИЛО** — практическая инструкция.

## Актуальное расширение
- `10_STRONGEST_FACTS_FOR_KRIS_TO_GVOZDAR.md`
- `11_STRONGEST_FACTS_AGAINST_HIDDEN_WARM_UNION_WITH_EVGENY.md`
- `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md`
- `13_HYPOTHESIS_UPDATE_LOG_MAY.md`
- `kris/2026-06-17_to_2026-08-02_UPDATE.md`
- `sources/chatgpt/2026-09-15_CURRENT_CHAT_ARCHIVE.md` — архив доступного контекста текущего чата.
- `sources/chatgpt/2026-09-15_CHAT_ARCHIVE_DELTA_AFTER_TRANSFER.md` — продолжение после первоначального переноса.
- `sources/chatgpt/02_Хронология_Крис.txt`
- `sources/chatgpt/07_Ключевые_цитаты.txt`
- `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.md`
- `sources/chatgpt/PROJECT_FILE_INVENTORY_2026-09-15.md` — инвентарь 35 файлов текущей поверхности и статус каждого класса.
- `sources/project_snapshot_2026-09-15/Психология_отношений_с_Крис_variant_A.txt`
- `sources/project_snapshot_2026-09-15/Психология_отношений_с_Крис_variant_B.txt`
- `sources/project_snapshot_2026-09-15/Психология_отношений_с_Крис_variant_C.txt`
- `sources/project_snapshot_2026-09-15/Ветка_Ветка_Ветка_Ветка_Флирт_и_доверие.txt`
- `MIGRATION_AUDIT_2026-09-15.md` — evidence-based аудит переноса.
- `MIGRATION_STATUS.md` — текущий физический статус.

## Исправление ошибочного bundle
Файл `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz`, который ранее был ошибочно принят за полный 98456-byte snapshot, фактически имел размер 8138 bytes. После проверки он был удалён из рабочей ветки как вводящий в заблуждение неполный артефакт. История коммита остаётся в Git и позволяет проверить факт ошибки.

## Приоритет при конфликте документов
1. `09_COMBINED_MASTER.md`
2. `00_INDEX.md`
3. более поздний датированный источник/журнал обновления;
4. остальные рабочие документы;
5. гипотезы и интерпретации уступают прямому источнику.

Нельзя повышать `REPORT` или `HYPOTHESIS` до `FACT` только потому, что версия хорошо согласуется с общей картиной.

## Физическая полнота архива
По аудиту 15.09.2026:

**Подтверждено:** текстовый архив текущего чата, delta, отдельный MD таймлайна, хронология, ключевые цитаты и дополнительные читаемые Project-source snapshots.

**Не подтверждено/заблокировано:** полный `messages12.html` exact bytes в GitHub, generated ZIP binary, 17 старых MP4 и exact originals 161 screenshots. Некоторые Project-backed документы доступны для чтения в Project, но их byte-exact GitHub snapshot требует отдельного доказательства.

Аналитическая полнота и физическая миграция — разные вещи. `DONE` не ставить до закрытия hard gates.