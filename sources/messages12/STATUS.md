# STATUS: migrated-lossless-reconstructable-exact-v2

## Проверено 15.09.2026
Старый legacy-набор `b64/` неполон: в нём отсутствует `part03`. Он остаётся историческим артефактом и **не используется** как доказательство полной сохранности.

## Канонический exact-v2 архив
Создан новый набор:
`sources/messages12/exact-v2/`

Он содержит пять последовательных бинарных частей XZ:
- `messages12.html.xz.part00` — 12000 байт;
- `messages12.html.xz.part01` — 12000;
- `messages12.html.xz.part02` — 12000;
- `messages12.html.xz.part03` — 12000;
- `messages12.html.xz.part04` — 6856.

Итого XZ: **54856 байт**.

GitHub API после записи подтвердил ожидаемые Git blob SHA каждой части и их размеры в дереве репозитория.

## Контрольные суммы
Исходный `messages12.html`:
- размер: **630716 байт**;
- строк при аудите: **27380**;
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Новый XZ:
- размер: **54856 байт**;
- SHA-256: `b3ad5c8bd5ea53ebb494ab6b1dbe7e7b1a32df91684d19418a8f4ebdf9d1fa45`.

Подробные SHA частей и команды реконструкции: `exact-v2/README.md`.

## Ошибка предыдущего bundle
Ранее ошибочно считалось, что exact bytes находятся в `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz` размером 98456 байт. Фактический GitHub blob имел размер **8138 байт**. Неполный tar.xz был удалён из рабочей ветки коммитом `881ee0ab064227da690d60c6c28bbe89075b5bf3`.

## Текущий статус
- исходный `messages12.html`: **SOURCE VERIFIED**;
- exact-byte preservation in GitHub: **VERIFIED / LOSSLESS-RECONSTRUCTABLE через exact-v2**;
- legacy multipart: **INCOMPLETE / OBSOLETE AS COMPLETION EVIDENCE**.
