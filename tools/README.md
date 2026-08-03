# Archive tools

`verify_archive.py` проверяет физическую целостность источников и не занимается психологической интерпретацией.

## Базовая проверка репозитория
```bash
python tools/verify_archive.py
```
Проверяется:
- lossless-реконструкция `messages12.html` из четырёх XZ/base64 частей;
- размер и SHA-256 XZ и восстановленного HTML;
- наличие ровно 161 уникальной строки в manifest скриншотов.

## Проверка локальных оригиналов скриншотов
```bash
python tools/verify_archive.py --local-screenshots /path/to/original/screenshots
```
Скрипт сверит канонические имена и SHA-256 с `sources/screenshots/original_manifest.csv`.

## Реконструкция произвольного base64-пакета
```bash
python tools/verify_archive.py \
  --reconstruct-b64 sources/screenshots/bundles/b64/PACKAGE \
  --output /tmp/package.zip
```
После реконструкции скрипт печатает размер и SHA-256. Сравнивать их нужно с контрольными значениями конкретного пакета.

## Принцип
`manifest` подтверждает, что источник инвентаризирован. `migrated` ставится только когда полное содержимое реально хранится в GitHub напрямую либо может быть побайтово восстановлено из проверяемых частей.
