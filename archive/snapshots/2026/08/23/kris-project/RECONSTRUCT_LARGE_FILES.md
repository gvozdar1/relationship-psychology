# Восстановление крупных файлов

Части являются последовательными фрагментами исходного бинарного файла. Для восстановления используется обычный `cat`; декодирование base64 не требуется.

## `1000029050.mp4.parts`

```bash
cat archive/kris-project-2026-08-23/primary/video/1000029050.mp4.parts/part-*.bin > 1000029050.mp4.parts
sha256sum 1000029050.mp4.parts
```

- Размер: 2752754 байт
- SHA-256: `7257e6c3ab58295160bb41cb29ffc18e7f8e5546c4d352ac20ba9ffaaade7bf2`
- Статус: `video`

## `1000030230.mp4.parts`

```bash
cat archive/kris-project-2026-08-23/primary/evidence/2026-06-27/1000030230.mp4.parts/part-*.bin > 1000030230.mp4.parts
sha256sum 1000030230.mp4.parts
```

- Размер: 629895 байт
- SHA-256: `ab34334f8191f7cba0397c6c0bd2da9c2e0d96c871ccedb423481f03682cb69f`
- Статус: `video`

## `1000030186.mp4.parts`

```bash
cat archive/kris-project-2026-08-23/primary/evidence/unclassified/1000030186.mp4.parts/part-*.bin > 1000030186.mp4.parts
sha256sum 1000030186.mp4.parts
```

- Размер: 1137278 байт
- SHA-256: `b6ee04f67241a630413cba4c23b1c5ba5a380847b307f894d7d64f5452b6ac9e`
- Статус: `unclassified-video`

## `KRIS_2026-06-27_EVIDENCE.zip.parts`

```bash
cat archive/kris-project-2026-08-23/primary/evidence/KRIS_2026-06-27_EVIDENCE.zip.parts/part-*.bin > KRIS_2026-06-27_EVIDENCE.zip.parts
sha256sum KRIS_2026-06-27_EVIDENCE.zip.parts
```

- Размер: 3212981 байт
- SHA-256: `8e4d2f11b442629604a79f2342e92b8b7d0906f822ae53e1dc961fdbce1681fe`
- Статус: `source-container`

