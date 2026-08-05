# Reconstruction

Канонический архив `messages12.html` хранится как четыре base64-части lossless XZ-файла.

## Восстановление
```bash
cat b64/messages12.html.xz.b64.part01 \
    b64/messages12.html.xz.b64.part02 \
    b64/messages12.html.xz.b64.part03 \
    b64/messages12.html.xz.b64.part04 \
  | base64 -d > messages12.html.xz

xz -dc messages12.html.xz > messages12.html
sha256sum messages12.html.xz messages12.html
```

## Ожидаемые значения
- `messages12.html.xz`: 51152 байта, SHA-256 `7a362a7cd5fd08e1420516e68a842a6ddbe44c804d736aaacec8407f42571de2`
- `messages12.html`: 630716 байт, SHA-256 `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`

Если обе контрольные суммы совпадают, восстановленный HTML побайтово соответствует исходнику проекта.
