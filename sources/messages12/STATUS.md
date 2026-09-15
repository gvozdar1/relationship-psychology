# STATUS: exact-byte-github-preservation-blocked-by-transfer-gate

## Проверено 15.09.2026
Legacy-набор `b64/` неполон:
- `part01` — присутствует;
- `part02` — присутствует;
- `part03` — **отсутствует**;
- `part04` — присутствует.

Следовательно старый multipart **не является lossless-reconstructable**.

## Исходный `messages12.html`
Во время аудита Project source удалось materialize/прочитать:
- размер: **630716 bytes**;
- строк: **27380**;
- SHA-256 materialized source: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

Это подтверждает исходный файл в рабочей среде, но само по себе не доказывает запись exact bytes в GitHub.

## Ошибка предыдущего bundle
Ранее было ошибочно указано, что exact bytes находятся в `sources/chatgpt/current_chat_materializable_files_2026-09-15.tar.xz` размером 98456 bytes.

Фактический GitHub blob имел размер **8138 bytes**. После обнаружения несоответствия неполный tar.xz был удалён из рабочей ветки коммитом:
`881ee0ab064227da690d60c6c28bbe89075b5bf3`.

## Почему перенос exact HTML сейчас не закрыт
GitHub connector в этом сеансе принимает текстовое `content`/base64, но не local materialized file reference. Binary/file bridge через container/Python во время аудита возвращал инфраструктурную ошибку. Ручная реконструкция 27380 строк не считается безопасной заменой byte-exact переносу исходника.

## Текущий статус
- исходный `messages12.html`: **LOCAL SOURCE VERIFIED DURING AUDIT**;
- exact-byte preservation in GitHub: **BLOCKED_BY_TOOL_TRANSFER_GATE / NOT CONFIRMED**;
- legacy multipart: **INCOMPLETE / OBSOLETE AS COMPLETION EVIDENCE**.

Старые части не удалять: это исторический артефакт миграции, но не каноническое доказательство полной сохранности.