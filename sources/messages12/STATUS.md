# STATUS: migrated-lossless-reconstructable

`messages12.html` полностью сохранён в рабочей ветке в lossless-реконструируемой форме.

## Хранилище
Четыре последовательные base64-части XZ-архива:
- `b64/messages12.html.xz.b64.part01`
- `b64/messages12.html.xz.b64.part02`
- `b64/messages12.html.xz.b64.part03`
- `b64/messages12.html.xz.b64.part04`

## Контроль частей
- part01: 18000 байт текста, SHA-256 `17ff16778bb8575a315f56640c3462c7db88801f8ace35170860231172277f50`
- part02: 18000, SHA-256 `ab31bb958689f532c91e1b4b32080af1bfb11642392112d1e83c6883b99033ef`
- part03: 18000, SHA-256 `070b2d14e9ce06101e94f7760466a3c8780ccf91ea27294e6a654ffdc8c5ff8d`
- part04: 14204, SHA-256 `3c3ce96f95a321d85740cb0eb37b84eb063cae15f067e913a937ca7ec3c857dd`

## Реконструкция
```bash
cat b64/messages12.html.xz.b64.part01 \
    b64/messages12.html.xz.b64.part02 \
    b64/messages12.html.xz.b64.part03 \
    b64/messages12.html.xz.b64.part04 \
  | base64 -d > messages12.html.xz
xz -dc messages12.html.xz > messages12.html
sha256sum messages12.html
```

Ожидаемые контрольные данные:
- XZ: 51152 байта, SHA-256 `7a362a7cd5fd08e1420516e68a842a6ddbe44c804d736aaacec8407f42571de2`
- восстановленный HTML: 630716 байт, SHA-256 `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`

Статус `migrated` означает именно сохранение полного содержимого, а не одного manifest-файла.
