# AUD-0008 — экспорт текущего чата в JSON

**Дата:** 15.09.2026  
**Репозиторий:** `gvozdar1/relationship-psychology`  
**Режим проверки:** AI Psychiatry (`never-stop`, `evidence-gate`, `context-balance`, `blocker-validator`, `completion-evidence`).

## Цель

Сохранить текущий пользовательский чат в GitHub в удобном машиночитаемом формате, не выдавая сжатые реконструкции за дословную первичку.

## Реализация

Создан каталог:

`archive/chat_exports/2026/09/15/current-chat/`

Состав:

- `archive/chat_exports/2026/09/15/current-chat/user-visible-transcript.json` — индекс, сообщения 1–23;
- `archive/chat_exports/2026/09/15/current-chat/parts/part-001.json` — 1–6;
- `archive/chat_exports/2026/09/15/current-chat/parts/part-002.json` — 7–12;
- `archive/chat_exports/2026/09/15/current-chat/parts/part-003.json` — 13–16;
- `archive/chat_exports/2026/09/15/current-chat/parts/part-004.json` — 17–23;
- `archive/chat_exports/2026/09/15/current-chat/coverage-manifest.json` — карта более ранней сжатой части чата на существующие `SRC-*` документы;
- `README.md` — правила использования.

## Evidence matrix

| Требование | Доказательство | Статус |
|---|---|---|
| Целевой репозиторий правильный | GitHub metadata: `gvozdar1/relationship-psychology`, default branch `main`, write/admin permission | VERIFIED |
| Пользовательские и ассистентские сообщения текущего доступного окна сохранены | `archive/chat_exports/2026/09/15/current-chat/parts/part-001.json` … `archive/chat_exports/2026/09/15/current-chat/parts/part-004.json` | VERIFIED |
| Последовательность сообщений сохранена | `seq` 1–23 без разрыва; индекс задаёт ranges 1–6, 7–12, 13–16, 17–23 | VERIFIED |
| Большой пользовательский блок 29.05 не сокращён как в старом `SRC-0009` | `archive/chat_exports/2026/09/15/current-chat/parts/part-003.json`, message 13 хранит исходный pasted-текст из текущего окна | VERIFIED |
| Технические сообщения текущего чата тоже не потеряны | part-002 и part-004 содержат вопросы о новой ветке, ZIP, GitHub и AI Psychiatry | VERIFIED |
| Скрытые/system/developer/tool данные не смешаны с пользовательским чатом | README + schema excludes these roles | VERIFIED |
| UI-обвязка ответов сохранена побайтово | writing-block/citation widgets могут быть нормализованы или опущены; смысловой текст сообщений сохранён | NOT REQUIRED FOR CONTENT EXPORT / NOT BYTE-EXACT |
| Более ранняя часть большого чата не исчезает из проекта | `archive/chat_exports/2026/09/15/current-chat/coverage-manifest.json` связывает её с `SRC-0009`–`SRC-0022` и существующими audit/update files | VERIFIED AS SOURCE MAP |
| Более ранняя часть большого чата доступна дословно сообщение-за-сообщением | runtime не предоставляет сырой до-компрессионный поток | NOT CONFIRMED / HARD PLATFORM LIMIT |

## Важная коррекция прежнего аудита

`AUD-0004 COMPLETE / VERIFIED` означает тематическое покрытие доступного материала, а не доказательство побайтовой полноты всего исторического пользовательского transcript.

Новый JSON-экспорт устраняет этот дефект для **текущего доступного user-visible окна** на уровне содержания сообщений: каждое видимое сообщение хранится отдельной записью с ролью и порядковым номером. UI-специфические citation/rendering wrappers не считаются частью содержательного экспорта и могут быть нормализованы.

## Итог

**IMPLEMENTED + VERIFIED для содержания всего user-visible transcript, который реально доступен этому запуску.**

Более ранний до-компрессионный сырой transcript не выдумывается задним числом. Вместо этого в репозитории сохранена доказательная карта на уже существующие источники. Если когда-либо появится нативный полный экспорт исходной ветки, его следует добавить как raw-source и повторить побайтовую сверку; до этого текущая структура является максимально полной без фальсификации данных.


Поправка метаданных 24.10.2026: прежний конфликтующий AUD-0006 заменён на AUD-0008. AUD-0006 закреплён за построчным аудитом; оценки полноты выше описывают исторический запуск, не новую сверку 24.10.
