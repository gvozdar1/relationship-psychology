# STATUS: exact-byte-github-preservation-not-confirmed

## Проверено 15.09.2026
Legacy-набор `b64/` неполон:
- `part01` — присутствует;
- `part02` — присутствует;
- `part03` — **отсутствует**;
- `part04` — присутствует.

Следовательно старый multipart **не является lossless-reconstructable**.

## Исходный `messages12.html`
Во время аудита Project source удалось materialize локально:
- размер: **630716 bytes**;
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Это подтверждает исходный файл в рабочей среде, но не его физическую запись в GitHub.

## Ошибка предыдущего статуса
Ранее было указано, что exact bytes находятся в
`sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz`
размером 98456 bytes.

Фактический GitHub blob по этому пути имеет размер **8138 bytes** и SHA `b09281144681b90372fa3bbf91ca89180baf2ba3`.
Поэтому он не может считаться доказательством заявленного полного snapshot.

## Текущий статус
- исходный `messages12.html`: **LOCAL SOURCE VERIFIED DURING AUDIT**;
- exact-byte preservation in GitHub: **NOT CONFIRMED**;
- legacy multipart: **INCOMPLETE / OBSOLETE AS COMPLETION EVIDENCE**.

Не удалять старые части: они остаются историческим артефактом миграции.