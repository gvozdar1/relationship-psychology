# `messages12.html` — lossless archive

Исходный файл проекта:
- имя: `messages12.html`
- размер: **630716 байт**
- кодировка: UTF-8
- SHA-256: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`

## Канонический способ хранения
Исходный HTML сжат без потерь в XZ, затем XZ закодирован в base64 и разделён на четыре последовательные части:

1. `b64/messages12.html.xz.b64.part01`
2. `b64/messages12.html.xz.b64.part02`
3. `b64/messages12.html.xz.b64.part03`
4. `b64/messages12.html.xz.b64.part04`

Склейка четырёх частей, base64-декодирование и XZ-распаковка восстанавливают исходный `messages12.html` побайтово.

Контроль XZ:
- размер: **51152 байта**
- SHA-256: `7a362a7cd5fd08e1420516e68a842a6ddbe44c804d736aaacec8407f42571de2`

Подробная команда восстановления находится в `RECONSTRUCT.md`. Статус источника: `migrated-lossless-reconstructable`.
