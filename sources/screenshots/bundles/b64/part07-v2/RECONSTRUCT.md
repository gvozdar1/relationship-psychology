# Reconstruct optimized screenshot bundle 07

Канонический исходный ZIP:
- `screenshots_part_07_1000029405-1000029437.zip`
- 11 WebP-файлов
- 179828 байт
- SHA-256 `87145dedcdb850c2ea59935c7c42a5a6bc5109e883b3382b5bf40d50b4774fff`

## Проверка частей
После загрузки всех 14 частей:
```bash
sha256sum -c SHA256SUMS.expected.txt
```

## Реконструкция
```bash
cat part00.b64 part01.b64 part02.b64 part03.b64 part04.b64 \
    part05.b64 part06.b64 part07.b64 part08.b64 part09.b64 \
    part10.b64 part11.b64 part12.b64 part13.b64 \
  | base64 -d > screenshots_part_07_1000029405-1000029437.zip

stat -c '%s' screenshots_part_07_1000029405-1000029437.zip
sha256sum screenshots_part_07_1000029405-1000029437.zip
unzip -t screenshots_part_07_1000029405-1000029437.zip
```

Ожидается размер `179828` и SHA-256 `87145dedcdb850c2ea59935c7c42a5a6bc5109e883b3382b5bf40d50b4774fff`.

## Текущий статус
Пока не загружены все 14 частей, пакет имеет статус `partial` и не считается мигрированным.
