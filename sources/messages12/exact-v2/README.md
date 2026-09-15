# messages12.html exact-v2

Статус: **lossless-reconstructable / VERIFIED BY GIT BLOB IDENTITY**.

Этот каталог содержит новый точный архив исходного `messages12.html`, созданный после обнаружения, что старый multipart-набор в `sources/messages12/b64/` физически не содержит `part03`.

## Исходник
- `messages12.html`: 630716 байт
- SHA-256 исходного HTML: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`

## Новый XZ
- объединённый XZ: 54856 байт
- SHA-256 XZ: `b3ad5c8bd5ea53ebb494ab6b1dbe7e7b1a32df91684d19418a8f4ebdf9d1fa45`

## Части
Последовательно объединить:
- `messages12.html.xz.part00` — 12000 байт; SHA-256 `5add20fcaaf60505192f212a47bd7624327ef35c94251f5500f7ea99b5b854d6`; Git blob `fac1b5417e485c2b0b9f66e683391f56ea308916`
- `messages12.html.xz.part01` — 12000; SHA-256 `71714a30bbc6bf0b0199fe747aa08e1123b1056cf97f218f26f29f09cfc9e6f0`; Git blob `02b46bf326166a042897e356a7bad3d84c894467`
- `messages12.html.xz.part02` — 12000; SHA-256 `28592ad44b27f8924fb90ba25998b72ee70e0a01208690a93f126ea4381b1ecc`; Git blob `efeb4d3ba0c1af75c1458607467042bf5e881a57`
- `messages12.html.xz.part03` — 12000; SHA-256 `39c1f03f6ab1d536ce1c18f13b9169ae3ea3cdcdbb588b3091732a3343a680d5`; Git blob `70ddc7a4d11830edda9088d8b7f5e3730b3849e4`
- `messages12.html.xz.part04` — 6856; SHA-256 `737d717a020cdfa14a659dcaf534cf322ebe646a8b12fe19f66a87e6240ea245`; Git blob `709e3fd2c24205f8acb29d3272e08caba73cff91`

GitHub API после записи подтвердил ожидаемые Git blob SHA для всех пяти частей и размеры частей в дереве репозитория.

## Реконструкция
```bash
cat messages12.html.xz.part00 \
    messages12.html.xz.part01 \
    messages12.html.xz.part02 \
    messages12.html.xz.part03 \
    messages12.html.xz.part04 > messages12.html.xz

sha256sum messages12.html.xz
xz -dc messages12.html.xz > messages12.html
sha256sum messages12.html
```

Ожидаемые результаты:
- XZ: `b3ad5c8bd5ea53ebb494ab6b1dbe7e7b1a32df91684d19418a8f4ebdf9d1fa45`
- HTML: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`

## Приоритет
Для точной реконструкции использовать **этот `exact-v2` набор**, а не старый неполный набор `sources/messages12/b64/`.
