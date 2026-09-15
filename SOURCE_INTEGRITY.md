# Source integrity ledger

Контрольный реестр исходных и восстановимых источников проекта.

| SHA-256 | Размер, байт | Файл / объект | GitHub-статус |
|---|---:|---|---|
| `94a9615400ffb361538185609f15fcbb2fce3e1526b5ea4d4f84c6d85a8cf087` | 2890 | исходный `00_INDEX.md` | baseline/reference |
| `d9633941f875f6c999543e9095c21c82572a073d23b4204fbcd48cce2427c6b7` | 5713 | `01_PROJECT_CORE.md` | archived/reference |
| `8a4ac5ecc1997b75635a4962fac6103c7ce8fd5b85ae24988e4c2a3a32380cb4` | 5175 | исходный `02_TIMELINE.md` | baseline/reference |
| `c1a52feac9925b96df5d0e9faa6e07a15a49f186827d02bd072ab3c3146d9a48` | 5125 | исходный `03_HYPOTHESES_AND_CONFIDENCE.md` | baseline/reference |
| `981c0a4b4a84fabfdeababf5375d3e874ed40b0a8d9a41af383a57a688a185e3` | 5226 | `05_COMMUNICATION_PROTOCOL.md` | archived/reference |
| `ddd407c8f85bc1d940571cc2dd8468aeaf2fda10360df5156c98893408e16c28` | 38249 | исходный локальный `09_COMBINED_MASTER.md` до синхронизации | exact baseline archived in parts |
| `99deec24e438f5db895ce1c0663e598a1ff3196b13fb6867c98da511385305e8` | 6323 | `10_STRONGEST_FACTS_FOR_KRIS_TO_GVOZDAR.md` | archived |
| `5d780c3dc9741817932175f22cc1cef12b99da3f871e8fa55b9cd69b692df12c` | 5406 | `11_STRONGEST_FACTS_AGAINST_HIDDEN_WARM_UNION_WITH_EVGENY.md` | archived |
| `d2d194d9687f461000ea62483717126d9a53703eed752d4fde9dcdd5fcb5ddff` | 5195 | baseline `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` | archived |
| `cafd89ec9d89f9328f219822f22bf9dc23eefb7b9ad5a66fea37bf009e1301d6` | 7255 | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` | archived |
| `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf` | 630716 | исходный `messages12.html` | **lossless reconstructable via `sources/messages12/exact-v2/`** |
| `b3ad5c8bd5ea53ebb494ab6b1dbe7e7b1a32df91684d19418a8f4ebdf9d1fa45` | 54856 | объединённый `messages12.html.xz` exact-v2 | **reconstructable from 5 verified Git blobs** |
| `692d0093bf05864162dfe76bff3a5c0d17d371bb93adb3529d4608443aab7987` | 4530 | `26_TIMELINE_MARCH_APRIL_2026.zip` | **byte-exact Git blob verified** |
| `84e60852857c3e145546ce63fbec920e1124ffca056eac68a87b3e624c5ffcac` | 12773 | `Ветка · Ветка · Флирт и доверие.txt` | migrated text/source |
| `d1d685bf9612bad7f18eefbec7a511f6b64fba235555b6aca420a4ff099e2551` | 3311 | один Project-source вариант `Психология отношений с Крис.txt` | migrated/source snapshot |
| `7257e6c3ab58295160bb41cb29ffc18e7f8e5546c4d352ac20ba9ffaaade7bf2` | 2752754 | `1000029050.mp4` | **RAW BINARY HARD GATE** |

## `messages12.html` exact-v2 Git objects
| Part | Размер | SHA-256 части | Git blob SHA |
|---|---:|---|---|
| part00 | 12000 | `5add20fcaaf60505192f212a47bd7624327ef35c94251f5500f7ea99b5b854d6` | `fac1b5417e485c2b0b9f66e683391f56ea308916` |
| part01 | 12000 | `71714a30bbc6bf0b0199fe747aa08e1123b1056cf97f218f26f29f09cfc9e6f0` | `02b46bf326166a042897e356a7bad3d84c894467` |
| part02 | 12000 | `28592ad44b27f8924fb90ba25998b72ee70e0a01208690a93f126ea4381b1ecc` | `efeb4d3ba0c1af75c1458607467042bf5e881a57` |
| part03 | 12000 | `39c1f03f6ab1d536ce1c18f13b9169ae3ea3cdcdbb588b3091732a3343a680d5` | `70ddc7a4d11830edda9088d8b7f5e3730b3849e4` |
| part04 | 6856 | `737d717a020cdfa14a659dcaf534cf322ebe646a8b12fe19f66a87e6240ea245` | `709e3fd2c24205f8acb29d3272e08caba73cff91` |

GitHub recursive tree от 15.09.2026 подтвердил указанные размеры и blob SHA.

## Generated timeline ZIP
Git blob SHA для `sources/chatgpt/26_TIMELINE_MARCH_APRIL_2026.zip`:
`e7d709ffe876eee831c8d5cb81a479015cb4073f`

Recursive tree подтвердил размер **4530 bytes** и этот blob SHA.

## Изображения
Полный перечень **161** канонического скриншота, размеры, геометрия, фактический формат и SHA-256: `sources/screenshots/original_manifest.csv`.

Важно: manifest подтверждает inventory и контрольные данные, но exact raw originals сейчас не доступны файловой поверхности и потому **не считаются physically migrated**.

## Видео
17 старых MP4 отображаются как uploads, однако их backing raw bytes больше не выдаются Files surface. Проверено materialize + альтернативной Library-copy на representative файле. Это hard gate, а не завершённая миграция.

## Назначение
Этот ledger различает:
- смысловую синхронизацию;
- текстовую архивацию;
- точную побайтовую архивацию;
- lossless-реконструируемую архивацию;
- manifest-only evidence;
- hard gate из-за отсутствующих raw bytes.

Если GitHub-версия рабочего документа была переработана для актуализации проекта, её SHA естественно отличается от исходного baseline. Baseline хранится отдельно в `archive/baseline/`.