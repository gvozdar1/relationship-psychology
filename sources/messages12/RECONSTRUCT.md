# Reconstruction

`messages12.html.gz` является lossless gzip-копией исходного `messages12.html`.

Контроль исходника:
- размер HTML: 630716 байт
- SHA-256 HTML: `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`

Контроль gzip:
- размер gzip: 69384 байта
- SHA-256 gzip: `43c4f65680ce4623b53aae3d99a53a587dbe7e35d68c47d4461339100cb97a90`

Восстановление:
```bash
gzip -dc messages12.html.gz > messages12.html
sha256sum messages12.html
```
