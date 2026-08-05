Для lossless-архива используется `messages12.html.xz`: это побайтово восстанавливаемая копия исходного UTF-8 HTML.

Контроль:
- исходный HTML: 630716 байт, SHA-256 `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`
- XZ-архив: SHA-256 `7a362a7cd5fd08e1420516e68a842a6ddbe44c804d736aaacec8407f42571de2`

Восстановление: `xz -dc messages12.html.xz > messages12.html`.
