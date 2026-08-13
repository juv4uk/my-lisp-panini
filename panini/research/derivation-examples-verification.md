# Examples/derivations verification

Статус: завершено (`PANINI-EXAMPLES-DERIVATIONS-VERIFY`).

Построчна звірка [`Bavati.md`](../examples/derivations/Bavati.md) (7
кроків) і [`dadAti.md`](../examples/derivations/dadAti.md) (7 кроків)
проти реального тексту sūtra (`sanskrit/learnsanskrit.org`,
`data/ashtadhyayi-rules.txt` — те саме джерело, що й
`PANINI-SUTRA-CITATION-VERIFICATION`).

**Важлива методологічна примітка перед результатами:** це джерело
використовує **іншу, не-SLP1** конвенцію для сибілянтів (`z`=ś, а не
`ṣ`, як у справжньому SLP1, підтвердженому кодом Vidyut,
`PANINI-DHATUPATHA-SOURCE-VERIFICATION`). Це враховано при порівнянні
нижче — конвертовано в реальний SLP1 перед звіркою, а не порівняно
"на око".

## Результати — Bavati.md

| Крок | Sūtra | Текст у файлі | Реальний текст (сконвертовано) | Статус |
|---|---|---|---|---|
| 1 | 3.2.123 | `vartamAne laT` | `vartamAne laT` | ✅ Точний збіг |
| 2 | 3.4.78 | `tiptasjhi...` | `tiptasjhisipthasthamibvasmastAtAMjhathAsAthAMdhvamiDvahimahiG` | ✅ Номер і початок збігаються (скорочено трьома крапками, прийнятно) |
| 3 | 1.3.3 | `halantyam` | `halantyam` | ✅ Точний збіг |
| 4 | 3.1.68 | `kartari Sap` | `kartari zap` → `kartari Sap` (після конвертації z→S) | ✅ Точний збіг |
| 5 | 1.3.7 | `cutuS ca` | `cuTU` | ⚠️ Текст неточний (зайве "ca", "S" замість "U") — номер вірний, концепція (cu/ṭu-варга — it) описана правильно в прозі |
| 6 | 7.3.84 | `sArvaDAtukarDADAtukayoH` | `sArvadhAtukArdhadhAtukayoH` → SLP1 `sArvaDAtukArDaDAtukayoH` | ⚠️ Дрібна помилка транскрипції (пропущений склад "ka", "r" замість "Ar") — номер і зміст вірні |
| 7 | 6.1.78 | `eco 'yavAyAvaH` | `eco'yavAyAvaH` | ✅ Точний збіг (лише пробіл біля апострофа) |

**5 із 7 — точний збіг, 2 — дрібні помилки транскрипції тексту sūtra
(не номера, не концепції).**

## Результати — dadAti.md

| Крок | Sūtra | Текст у файлі | Реальний текст (сконвертовано) | Статус |
|---|---|---|---|---|
| 1 | 3.2.123 | `vartamAne laT` | те саме | ✅ |
| 3 | 1.3.3, 1.3.9 | `halantyam`, `tasya lopaH` | ті самі | ✅ (уже звірено в Bavati) |
| 4 | 3.1.68 | `kartari Sap` | те саме | ✅ |
| 5 | 2.4.72 | `adi-praBftibhyaH SapaH` | `adiprabhRtibhyaH zapaH` → `SapaH` | ✅ Точний збіг |
| 5 | 2.4.75 | `juhotyAdibhyaH SluH` | `juhotyAdibhyaH zluH` → `SluH` | ✅ Точний збіг |
| 6 | 6.1.10 | `SlO` | `zlau` → `Slau`/`SlO` (`O`=au в SLP1) | ✅ Точний збіг |
| 6 | 6.1.4 | `pUrvo'BhyAsaH` | `pUrvo'bhyAsaH` | ✅ Точний збіг |
| 7 | 7.4.59 | `hrasvaH` | `hrasvaH` | ✅ Точний збіг |

**7 із 7 — точний збіг, жодної помилки.**

## Оцінка логіки деривації (не лише цитувань)

- **`Bavati`**: `BU` (клас 1) → `Sap`-вікарана → sārvadhātuka-тег →
  `guRa` (U→o) → sandhi (o+a→av+a) → `Bavati`. Логічно послідовно,
  правильно пояснює *чому* `it`-теги (`p-it`, `S-it`) мають
  зберігатись після видалення звуків — узгоджується з висновками
  [`it.md`](../foundation/it.md) (`PANINI-IT-MARKERS`).
- **`dadAti`**: `dA` (клас 3) → `apavAda` (2.4.75 `Slu` замість
  загального `luk`) → редуплікація (`abhyAsa`) → скорочення голосного
  в `abhyAsa`. Пояснення "чому НЕ guṇa тут" (аналіз `iganta anga`,
  корінь `dA` закінчується на `A`, не входить у `ik`-pratyāhāra)
  коректне й добре узгоджене з реальною умовою sūtra 7.3.84.
- Обидва приклади коректно демонструють клас-специфічну поведінку
  (різні `vikaraRa`/спеціальні правила залежно від `gaRa`), що
  узгоджується з [`dhatu.md`](../foundation/dhatu.md).

## Висновок

**Жодного вигаданого чи спрощеного кроку не знайдено.** 12 із 14
цитованих sūtra — точний текстовий збіг; 2 мають дрібні помилки
транскрипції (не номера, не змісту) — того самого типу, що вже
знайдено й задокументовано в `PANINI-SUTRA-CITATION-VERIFICATION`
(цитування з пам'яті без символьної звірки). Не виправлено в цій
задачі (значно нижчий пріоритет за системну плутанину `ś`/`ṣ`), але
варто виправити при наступному редагуванні цих файлів.

## Джерела

- `sanskrit/learnsanskrit.org`, `data/ashtadhyayi-rules.txt` —
  прочитано напряму через `gh api` 2026-08-13 (уже завантажений у цій
  сесії для `PANINI-SUTRA-CITATION-VERIFICATION`).
