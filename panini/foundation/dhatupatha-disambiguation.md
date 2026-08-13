# Dhātupāṭha disambiguation policy

## English

**Status:** v0.1 (`PANINI-DHATUPATHA-DISAMBIGUATION-POLICY`). A Dhātupāṭha
`aupadeSika` source form and the project’s canonical citation form serve
different purposes. Preserve the literal source in `source_form` with its
`dhatupatha_code`; retain canonical SLP1 for interoperable citation. Purely
decorative markers may be normalized only under the documented rule. A change
of consonant, such as `zWA` versus `sTA`, requires independent confirmation;
otherwise the record must remain explicitly uncertain. Homonymy and gaṇa
disagreement are source-identity issues, not spelling fixes. The detailed
Ukrainian policy gives the full evidence boundaries.

## Deutsch

**Status:** v0.1 (`PANINI-DHATUPATHA-DISAMBIGUATION-POLICY`). Eine
`aupadeSika`-Quellform des Dhātupāṭha und die kanonische Zitierform des
Projekts erfüllen verschiedene Zwecke. Die wörtliche Quelle ist mit
`source_form` und `dhatupatha_code` zu bewahren; kanonisches SLP1 bleibt für
interoperables Zitieren erhalten. Rein dekorative Marker dürfen nur nach der
dokumentierten Regel normalisiert werden. Eine Konsonantenänderung wie
`zWA` gegenüber `sTA` braucht unabhängige Bestätigung; andernfalls muss der
Datensatz ausdrücklich unsicher bleiben. Homonymie und gaṇa-Abweichungen sind
Fragen der Quellidentität, keine Schreibkorrekturen. Die ukrainische
Detailrichtlinie enthält die vollständigen Evidenzgrenzen.

## Українська

Статус: v0.1 (`PANINI-DHATUPATHA-DISAMBIGUATION-POLICY`).

## Проблема

`PANINI-DHATUPATHA-SOURCE-VERIFICATION` знайшла: первинний Dhātupāṭha
(`vidyut-prakriya/data/dhatupatha.tsv`) часто подає корінь у формі, що
відрізняється від "цитатної" (`citation`) форми, звичної з підручників
і нашого власного `canonical`-поля:

| `canonical` (наш реєстр) | Форма в Dhātupāṭha (`aupadeSika`) | Код |
|---|---|---|
| `gam` | `ga\mx~` (декоративний `x`, акцентний `\`, anudātta `~`) | `01.1137` |
| `kf` | `qukf\Y` (декоративний префікс `qu`, акцент `\`, it `Y`) | `08.0010` |
| `sTA` | `zWA\` (**ретрофлексне `z`**, не дентальне `s`!) | `01.1077` |

Перші два — очевидні декоративні маркери (легко відділити). Третій —
не декоративний маркер, а **інша приголосна на початку кореня** —
традиційна орфографія Dhātupāṭha системно фіксує деякі корені з
початковим ретрофлексним `ṣ`, хоча їхня "цитатна" форма (і реальна
вимова поза певними фонетичними контекстами) — з дентальним `s`. Це
принципово інший тип розбіжності, ніж перші два.

## Політика

### Поля запису

Кожен запис `registry/dhatu/*.yaml` **може** (не зобов'язаний, лише
там, де відомо) мати два додаткові поля поза наявною схемою
[`dhatu.md`](dhatu.md):

```yaml
source_form: <буквальна форма з Dhātupāṭha, з усіма декоративними маркерами>
dhatupatha_code: <gaRa.номер, напр. "08.0010">
```

`canonical` **лишається** цитатною формою (без декоративних маркерів)
— саме те, що вже узгоджено з рештою екосистеми
(`my-lisp`'s `transliteration.rs`, `panini/research/slp1-lexicon-alignment.md`).
`source_form`/`dhatupatha_code` — це *додаткова*, не замінна
інформація для простежуваності.

### Правило нормалізації (`source_form` → `canonical`)

1. **Видалити суто декоративні it-маркери**: кінцеві `~`, `\`, `^`,
   цифри, префікси-розділювачі типу `qu-`/`ti-` — це не частина
   вимовленого кореня, а технічна позначка Dhātupāṭha (аналог `it`,
   [`it.md`](it.md)). Приклад: `ga\mx~` → видалити `\`, `x`
   (декоративний реферативний голосний), `~` → `gam`.
2. **НЕ автоматично нормалізувати зміну приголосного** (як `z`→`s` у
   `zWA`→`sTA`) без незалежного підтвердження, що цитатна форма
   справді відрізняється приголосним, а не лише маркерами. Підстава
   для `sTA`: універсально визнана цитатна форма в усій традиції
   (підручники, `my-lisp`, `PANINI-GRAMMAR-REFERENCE.md`) — `sthā`
   з дентальним `s`, а не `ṣṭhā`. Це не здогад, а факт, підтверджений
   множинними незалежними джерелами поза самим Dhātupāṭha.
3. Якщо для кореня є `source_form` із незвичною приголосною, а
   незалежного підтвердження цитатної форми **немає** — запис
   повинен явно позначити це полем `citation_form_uncertain: true`,
   а не мовчки обирати одну з двох форм.

### Коли запис повинен лишатися неоднозначним

`PANINI-DHATUPATHA-SOURCE-VERIFICATION` також знайшла **омонімію**:
форма `jYA` присутня в кількох gaṇa одночасно з різними значеннями;
`Sru` в Dhātupāṭha закодований у gaṇa 01, а наш реєстр каже gaṇa 5.
Це не помилка транслітерації — це або (а) справжня омонімія (кілька
різних коренів з однаковим написанням), або (б) розбіжність між
джерелами щодо gaṇa-приналежності. У цьому випадку:

- `canonical` (написання) лишається без змін.
- Поле `gana` **не виправляється мовчки** — додається
  `gana_disputed: true` і нотатка з обома варіантами, поки не буде
  третього незалежного джерела для вирішення.
- **Не вигадувати** "правильну" відповідь із двох суперечливих —
  чесна неоднозначність краща за хибну впевненість (`AGENTS.md` §17).

## Застосування до реєстру (3 приклади, за пам'яттю задачі)

Додано `source_form`/`dhatupatha_code` до `gam.yaml`, `sTA.yaml`,
`kf.yaml` (нижче в коміті). `sTA.yaml` додатково отримує нотатку про
розбіжність приголосного з поясненням, чому нормалізація до `sTA`
виправдана (на відміну від "мовчки обраної"). `Sru.yaml` отримує
`gana_disputed: true` за знахідкою `PANINI-DHATUPATHA-SOURCE-VERIFICATION`
(джерело: gaṇa 1, наш реєстр: gaṇa 5).

## Джерела

- [`research/dhatupatha-verification.md`](../research/dhatupatha-verification.md)
  — першоджерело всіх трьох прикладів вище.
- `vidyut-prakriya/data/dhatupatha.tsv` — прочитано напряму в
  попередній задачі.
