# Blocked raw files — 2026-09-15

Этот файл фиксирует **только физически не закрытые части миграции после полного evidence-audit**. Документы, `messages12.html` и generated ZIP больше не являются блокерами.

## 1. Старые MP4, raw bytes недоступны Files surface

Нужна повторная загрузка/доступный raw source для:

| # | Файл | Размер, bytes |
|---:|---|---:|
| 1 | `video (2).mp4` | 1437918 |
| 2 | `video (3).mp4` | 2977147 |
| 3 | `video (4).mp4` | 1788026 |
| 4 | `1775173257172.mp4` | 6033784 |
| 5 | `1775173257210.mp4` | 2487952 |
| 6 | `video (5).mp4` | 565275 |
| 7 | `1775173223574.mp4` | 8017053 |
| 8 | `1775177812987.mp4` | 8122236 |
| 9 | `1775177813015.mp4` | 1793450 |
| 10 | `1775177813030.mp4` | 3630642 |
| 11 | `1775177813054.mp4` | 3852023 |
| 12 | `1775177813068.mp4` | 1329135 |
| 13 | `1775177812388.mp4` | 4251938 |
| 14 | `1775177812520.mp4` | 4459235 |
| 15 | `1775177812561.mp4` | 3490992 |
| 16 | `1775177812582.mp4` | 5187035 |
| 17 | `1775177812610.mp4` | 2593480 |

Проверка первых пяти через materialize дала одинаковое:
`The requested Library file does not have a downloadable backing file yet.`

Независимая попытка перенести representative `video (2).mp4` через Library-copy завершилась `source_file_not_found / exact exported file unavailable or expired`.

Это валидирует hard gate для старого upload-класса: raw backing bytes отсутствуют в доступном источнике.

## 2. Historical `1000029050.mp4`

Ранее зарегистрировано:
- размер: **2752754 bytes**;
- SHA-256: `7257e6c3ab58295160bb41cb29ffc18e7f8e5546c4d352ac20ba9ffaaade7bf2`.

В текущей Files surface raw binary отсутствует и в GitHub физически не подтверждён.

## 3. Скриншоты

В `sources/screenshots/original_manifest.csv` зарегистрированы **161** канонических screenshot originals.

В GitHub физически подтверждены:
- manifest;
- документация;
- часть производных/оптимизированных данных.

Полный набор exact raw original image bytes не доступен текущей Files surface. Manifest/preview/bundle metadata не заменяют original bytes.

Для закрытия hard gate нужен исходный архив этих 161 изображений либо повторно доступные raw originals.

## Решённые пункты
### `messages12.html`
Закрыт через `sources/messages12/exact-v2/`: пять проверенных бинарных частей XZ позволяют lossless восстановить исходный HTML с SHA-256 `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf`.

### `26_TIMELINE_MARCH_APRIL_2026.zip`
Закрыт byte-exact. GitHub tree подтверждает путь `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.zip`, размер **4530 bytes**, Git blob `e7d709ffe876eee831c8d5cb81a479015cb4073f`.

### Ошибочный tar.xz snapshot
Усечённый 8138-byte artifact удалён из рабочей ветки. Он не нужен для завершённости, поскольку доступные Project text sources перенесены отдельно, `messages12` закрыт exact-v2, а оставшиеся raw-media блокеры перечислены выше.

## Completion condition
Полный буквальный статус `DONE` по всем media допустим после появления и записи:
1. 17 old-upload MP4;
2. `1000029050.mp4`;
3. 161 original screenshot raw files.

До этого корректный статус: **all independent accessible work verified; raw-media hard gates remain**.