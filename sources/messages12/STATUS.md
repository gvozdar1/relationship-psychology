# STATUS: preserved-via-2026-09-15-exact-byte-bundle

## Corrected audit finding
Ранее этот файл утверждал, что `messages12.html` полностью сохранён через четыре последовательные base64-части XZ-архива.

Проверка дерева GitHub 15.09.2026 показала:
- `b64/messages12.html.xz.b64.part01` — присутствует;
- `b64/messages12.html.xz.b64.part02` — присутствует;
- `b64/messages12.html.xz.b64.part03` — **отсутствует**;
- `b64/messages12.html.xz.b64.part04` — присутствует.

Следовательно legacy-набор `b64/` **не является lossless-reconstructable** и не должен использоваться как доказательство полной миграции.

## Новый подтверждённый источник байтов
Исходный `messages12.html` был заново materialized из текущего Project source и проверен:
- размер: **630716 bytes**;
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Exact bytes этого HTML теперь находятся внутри:
`sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz`

SHA-256 tar.xz:
`fe2dcaf73ed8b9d797fca38c3db18c5f8d116576a3637e0d9138170fa8b98c68`

Внутри архива путь:
`project_files/messages12.html`

Также внутри есть `MANIFEST.json` с размером и SHA-256 каждого вложенного файла.

## Статус
- exact content `messages12.html`: **PRESERVED / VERIFIED VIA NEW BUNDLE**;
- старый четырёхчастный `sources/messages12/b64/` архив: **INCOMPLETE / OBSOLETE AS COMPLETION EVIDENCE**.

Не удалять старые части: они остаются историческим артефактом миграции, но не являются каноническим доказательством полной сохранности.
