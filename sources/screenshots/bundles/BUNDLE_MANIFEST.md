# Optimized screenshot bundle manifest

Оптимизированный слой содержит 161 WebP-копию канонических скриншотов. Это производные копии для просмотра, не замена оригиналам.

| Bundle | Файлы | Размер ZIP | SHA-256 | Migration status |
|---|---:|---:|---|---|
| `screenshots_part_01_1000028787-1000028985.zip` | 25 | 427006 | `b2cee56e92d32a2cfb0b2a1a7ad65a99830a3aabbc7c1f3b1cc4c4c0528e5f95` | pending |
| `screenshots_part_02_1000028986-1000029010.zip` | 25 | 409754 | `1a0420349a560e47ccec9ef625db3b0c86f166509f17f8252a1320ec96763f9e` | pending |
| `screenshots_part_03_1000029014-1000029147.zip` | 25 | 456067 | `76a08e46c10c4251719bb8810f6229d0f96ce900bc1ef900a0294e19855ba580` | pending |
| `screenshots_part_04_1000029148-1000029173.zip` | 25 | 483027 | `b656e36c80a1d300b42a11864e9624577e19b83dc48d60922d1857945f9a6d99` | pending |
| `screenshots_part_05_1000029174-1000029304.zip` | 25 | 513929 | `3d5d74366b4353134be873b1daa8980b75186b63b192794e6ca23cb2f74ab8d0` | pending |
| `screenshots_part_06_1000029305-1000029387.zip` | 25 | 478889 | `b2c8fba3db30891f0063f2defdfcded1f2c6a507e9f28fe3251d474b5c9d994d` | pending |
| `screenshots_part_07_1000029405-1000029437.zip` | 11 | 179828 | `87145dedcdb850c2ea59935c7c42a5a6bc5109e883b3382b5bf40d50b4774fff` | partial, canonical v2 parts 00–04 uploaded |

## Total optimized payload
- 161 WebP files before ZIP grouping;
- approximately 2.93 MB of optimized WebP content before ZIP packaging;
- source originals remain governed by `../original_manifest.csv`.

## Rule
A bundle changes to `migrated-lossless-reconstructable` only after every canonical base64 part is present and the reconstructed ZIP matches both expected byte size and SHA-256.
