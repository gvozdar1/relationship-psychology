# Source integrity ledger

Локальный контрольный срез перед полной миграцией бинарных источников.

| SHA-256 | Размер, байт | Файл |
|---|---:|---|
| `94a9615400ffb361538185609f15fcbb2fce3e1526b5ea4d4f84c6d85a8cf087` | 2890 | `00_INDEX.md` |
| `d9633941f875f6c999543e9095c21c82572a073d23b4204fbcd48cce2427c6b7` | 5713 | `01_PROJECT_CORE.md` |
| `8a4ac5ecc1997b75635a4962fac6103c7ce8fd5b85ae24988e4c2a3a32380cb4` | 5175 | `02_TIMELINE.md` |
| `c1a52feac9925b96df5d0e9faa6e07a15a49f186827d02bd072ab3c3146d9a48` | 5125 | `03_HYPOTHESES_AND_CONFIDENCE.md` |
| `981c0a4b4a84fabfdeababf5375d3e874ed40b0a8d9a41af383a57a688a185e3` | 5226 | `05_COMMUNICATION_PROTOCOL.md` |
| `ddd407c8f85bc1d940571cc2dd8468aeaf2fda10360df5156c98893408e16c28` | 38249 | исходный локальный `09_COMBINED_MASTER.md` до синхронизации |
| `99deec24e438f5db895ce1c0663e598a1ff3196b13fb6867c98da511385305e8` | 6323 | `10_STRONGEST_FACTS_FOR_KRIS_TO_GVOZDAR.md` |
| `5d780c3dc9741817932175f22cc1cef12b99da3f871e8fa55b9cd69b692df12c` | 5406 | `11_STRONGEST_FACTS_AGAINST_HIDDEN_WARM_UNION_WITH_EVGENY.md` |
| `d2d194d9687f461000ea62483717126d9a53703eed752d4fde9dcdd5fcb5ddff` | 5195 | `12_UPDATED_WORKING_HYPOTHESIS_CURRENT.md` |
| `cafd89ec9d89f9328f219822f22bf9dc23eefb7b9ad5a66fea37bf009e1301d6` | 7255 | `13_HYPOTHESIS_UPDATE_LOG_MAY.md` |
| `d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf` | 630716 | `messages12.html` |
| `84e60852857c3e145546ce63fbec920e1124ffca056eac68a87b3e624c5ffcac` | 12773 | `Ветка · Ветка · Флирт и доверие.txt` |
| `d1d685bf9612bad7f18eefbec7a511f6b64fba235555b6aca420a4ff099e2551` | 3311 | `Психология отношений с Крис.txt` |
| `7257e6c3ab58295160bb41cb29ffc18e7f8e5546c4d352ac20ba9ffaaade7bf2` | 2752754 | `1000029050.mp4` |

## Изображения
Полный перечень 161 канонического скриншота, размеры, геометрия, фактический формат и SHA-256: `sources/screenshots/original_manifest.csv`.

## Назначение
Этот файл позволяет отличить:
- смысловую синхронизацию документа;
- точную побайтовую архивацию исходника.

Если GitHub-версия была переработана для актуализации проекта, её SHA естественно отличается от исходного локального baseline. Поэтому baseline хранится отдельно в `archive/baseline/`.

