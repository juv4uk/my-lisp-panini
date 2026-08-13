# dhAtu

Статус: чернетка v0.1 (`PANINI-DHATU-REGISTRY-20`).

## [PANINI]

`dhAtu` — дієслівний корінь. Ключове застереження з `AGENTS.md`: **не
вважати dhātu просто «дієсловом»**. Точніше:

- Список dhātu подається окремим традиційним текстом — **Dhātupāṭha**
  (~2000 коренів, згрупованих у 10 `gaRa`, класів дієвідміни), а не
  виводиться правилами самої Aṣṭādhyāyī. Aṣṭādhyāyī оперує dhātu як
  зовнішнім, заданим списком (sūtra 1.3.1 `bhUvAdayo dhAtavaH` —
  буквально "[корені], що починаються з `bhU`, [є] dhātu" — це
  визначення-посилання на список, не змістовне визначення).
- `dhAtu` — вихідна точка деривації дієслівних форм: до нього
  приєднуються `vikaraRa` (тематичний суфікс класу), особові
  закінчення (`tiN`), а через `kft`-pratyaya — і номінальні похідні
  (дієприкметники, іменники дії тощо). Тобто dhātu породжує не лише
  дієслова, а й велику частину номінальної лексики.
- `dhAtu` як формальна одиниця в Dhātupāṭha часто несе `it`-маркери
  (напр. позначення перехідності/неперехідності, `seT`/`aniT` —
  чи вставляється `i` перед деякими pratyaya), які видаляються перед
  реальним використанням — сам dhātu в Dhātupāṭha вже є прикладом
  формального запису з metalanguage-шаром (`it`), описаним у
  [`ontology.md`](ontology.md).
- `gaRa` (клас, 1–10) визначає, як саме dhātu поводиться при приєднанні
  `vikaraRa` — це не властивість значення кореня, а суто морфологічна
  класифікація.

## [INTERPRETATION]

Сучасні джерела (традиційні коментарі до Dhātupāṭha, а також
комп'ютерні реалізації типу Vidyut) типово додають до кожного dhātu:
`gaRa`, `pada` (parasmaipada/ātmanepada/ubhayapada — який набір
особових закінчень використовується), `seT`/`aniT`-статус, і
традиційне значення мовою коментаря (санскрит/гінді/англійська
парафраза). Це вже інтерпретаційний шар — Dhātupāṭha сам по собі
переважно списочний, значення часто дається одним словом і потребує
традиційного коментаря (Maitreyī, Kṣīrasvāmin та ін.) для повного
розуміння.

## [MY-LISP HYPOTHESIS]

Не сформульовано. dhātu тут реєструється як мовна одиниця першого
порядку (Рівень 2, `ontology.md`) — жодного припущення про
відповідність `cons`/`car`/`cdr` чи будь-якій обчислювальній
конструкції.

## Формат запису

```yaml
canonical: <SLP1>
display:
  iast: <IAST>
  devanagari: <देवनागरी>
class: dhatu
gana: <1-10>
pada: <parasmaipada|atmanepada|ubhayapada>
set_anit: <seT|aniT|unknown>
source:
  dhatupatha: <gaRa номер, порядковий номер якщо відомий>
traditional_meaning: <коротка парафраза>
notes: <застереження щодо неоднозначності/варіантів>
```

## Реєстр (20 коренів)

Добірка навмисно охоплює різні `gaRa`, щоб не створювати враження, ніби
всі dhātu поводяться однаково.

```yaml
canonical: BU
display: { iast: bhū, devanagari: भू }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaRa 1), перший корінь списку" }
traditional_meaning: "бути, ставати, існувати"
notes: >
  Канонічний "перший" dhātu — sūtra 1.3.1 називає весь клас dhātu саме
  через нього ("bhU-вādayaḥ"). Класичний приклад для навчальних текстів.
```

```yaml
canonical: kf
display: { iast: kṛ, devanagari: कृ }
class: dhatu
gana: 8
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "tanAdi (gaRa 8)" }
traditional_meaning: "робити"
notes: >
  Один з найуживаніших коренів; irregular/суплетивна поведінка в ряді
  форм (напр. imperfect kftavat- vs. поточна основа karo-/kuru-) —
  потребує окремої перевірки при переході до derivation.md.
```

```yaml
canonical: gam
display: { iast: gam, devanagari: गम् }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "йти"
notes: "Носовий елемент випадає в ряді похідних форм (напр. gata, не gamta)."
```

```yaml
canonical: sTA
display: { iast: sthā, devanagari: स्था }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "стояти"
notes: "Корінь на довгий голосний — інша поведінка при guRa/vfdDi ніж у приголосних коренів."
```

```yaml
canonical: dA
display: { iast: dā, devanagari: दा }
class: dhatu
gana: 3
pada: ubhayapada
set_anit: aniT
source: { dhatupatha: "juhotyAdi (gaRa 3)" }
traditional_meaning: "давати"
notes: "Клас 3 (reduplicating class) — основа dadA-ti, окремий тип vikaraRa."
```

```yaml
canonical: nI
display: { iast: nī, devanagari: नी }
class: dhatu
gana: 1
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "вести"
notes: "Частий приклад у kAraka-розділах (хто кого куди веде)."
```

```yaml
canonical: paW
display: { iast: paṭh, devanagari: पठ् }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "читати (вголос)"
notes: "Регулярний корінь, зручний як baseline-приклад без суплетивізму."
```

```yaml
canonical: liK
display: { iast: likh, devanagari: लिख् }
class: dhatu
gana: 6
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "tudAdi (gaRa 6)" }
traditional_meaning: "писати"
notes: "gaRa 6 — vikaraRa a з наголосом на ньому, а не на корені."
```

```yaml
canonical: dfS
display: { iast: dṛś, devanagari: दृश् }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "бачити"
notes: >
  Сильно суплетивний у різних часах/способах (paS-, dadfS- тощо) —
  класичний приклад того, що "один dhātu" ≠ "один регулярний патерн
  форм". SLP1: канонічно "dfS" (не "dfz") — виправлено двічі 2026-08-13
  (`PANINI-DHATUPATHA-SOURCE-VERIFICATION`): спершу помилково змінено
  на "dfz" за хибним твердженням `PANINI-GRAMMAR-REFERENCE.md`
  ("ś=z, ṣ=S"), потім відкочено назад після звірки проти реального
  коду Vidyut (`sounds.rs`, класифікація місць артикуляції: `S`
  групується з палатальними `i/c/y` = ś, `z` групується з
  ретрофлексними `f/w/r` = ṣ) — правильно: `ś=S`, `ṣ=z`.
```

```yaml
canonical: Buj
display: { iast: bhuj, devanagari: भुज् }
class: dhatu
gana: 7
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "rudhAdi (gaRa 7)" }
traditional_meaning: "їсти; насолоджуватися (залежно від pada)"
notes: >
  Значення систематично залежить від parasmaipada/ātmanepada вибору —
  важливий приклад того, що `pada`-вибір не суто морфологічний, а й
  семантичний сигнал (пор. sūtra розділу про ātmanepada, 1.3.12 і далі).
```

```yaml
canonical: pac
display: { iast: pac, devanagari: पच् }
class: dhatu
gana: 1
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "варити, готувати їжу"
notes: >
  Стандартний приклад у більшості підручників для ілюстрації kAraka
  (напр. "pacati" — хто варить, що варить, чим варить).
```

```yaml
canonical: vac
display: { iast: vac, devanagari: वच् }
class: dhatu
gana: 2
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "adAdi (gaRa 2)" }
traditional_meaning: "говорити"
notes: "gaRa 2 — атематичний клас, без голосного vikaraRa між коренем і закінченням."
```

```yaml
canonical: Sru
display: { iast: śru, devanagari: श्रु }
class: dhatu
gana: 5
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "svAdi (gaRa 5)" }
traditional_meaning: "чути"
notes: "gaRa 5 — vikaraRa nu/no, окремий морфологічний патерн."
```

```yaml
canonical: jYA
display: { iast: jñā, devanagari: ज्ञा }
class: dhatu
gana: 9
pada: ubhayapada
set_anit: aniT
source: { dhatupatha: "kryAdi (gaRa 9)" }
traditional_meaning: "знати"
notes: "gaRa 9 — vikaraRa nA/nI, ще один окремий клас відмінювання."
```

```yaml
canonical: Baz
display: { iast: bhāṣ, devanagari: भाष् }
class: dhatu
gana: 1
pada: atmanepada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaRa 1)" }
traditional_meaning: "говорити"
notes: >
  Виключно ātmanepada — приклад коренів, що не мають ubhayapada-варіанту.
  SLP1 виправлено з "BAS" на "Baz" 2026-08-13
  (`PANINI-DHATUPATHA-SOURCE-VERIFICATION`) — ṣ (retroflex) кодується
  `z`, не `S` (яка означає ś, palatal); первісний запис "BAS" мовчки
  наслідував хибну конвенцію `PANINI-GRAMMAR-REFERENCE.md`.
```

```yaml
canonical: as
display: { iast: as, devanagari: अस् }
class: dhatu
gana: 2
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "adAdi (gaRa 2)" }
traditional_meaning: "бути (дієслово-зв'язка)"
notes: >
  Один з найнерегулярніших коренів (суплетивна форма bhū в ряді часів);
  критично важливий для копулятивних конструкцій, отже і для майбутнього
  дослідження kAraka в реченнях без явного "дієслова дії".
```

```yaml
canonical: iz
display: { iast: iṣ, devanagari: इष् }
class: dhatu
gana: 6
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "tudAdi (gaRa 6)" }
traditional_meaning: "бажати, прагнути"
notes: >
  Семантично цікавий для kAraka-дослідження: apAdAna/sampradAna
  поведінка при дієсловах бажання нетривіальна. SLP1: канонічно "iz"
  (не "iS") — виправлено двічі 2026-08-13
  (`PANINI-DHATUPATHA-SOURCE-VERIFICATION`): спершу помилково змінено
  з "iz" на "iS" у `PANINI-TERMINOLOGY-GLOSSARY` за хибним
  твердженням `PANINI-GRAMMAR-REFERENCE.md`, потім відкочено назад
  після звірки проти реального коду Vidyut (`sounds.rs`) — правильно:
  `ṣ=z`, `ś=S`.
```

```yaml
canonical: BI
display: { iast: bhī, devanagari: भी }
class: dhatu
gana: 3
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "juhotyAdi (gaRa 3)" }
traditional_meaning: "боятися"
notes: >
  Класичний приклад для apAdAna kAraka ("боятися ЧОГОСЬ" — джерело
  страху виражається аблативом) — прямий місток до
  `PANINI-DHATU-KARAKA-RELATION`.
```

```yaml
canonical: yuj
display: { iast: yuj, devanagari: युज् }
class: dhatu
gana: 7
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "rudhAdi (gaRa 7)" }
traditional_meaning: "з'єднувати, запрягати"
notes: >
  Історично важливий для лінгвістичної термінології (від нього —
  "yoga"), гарний приклад інфіксного vikaraRa класу 7 (n перед
  останньою приголосною корня).
```

```yaml
canonical: han
display: { iast: han, devanagari: हन् }
class: dhatu
gana: 2
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "adAdi (gaRa 2)" }
traditional_meaning: "вбивати, вражати"
notes: >
  Сильно нерегулярний атематичний корінь (значні звукові зміни
  основи залежно від закінчення) — хороший stress-test для майбутньої
  derivation-моделі, а не лише "простий" приклад.
```

## Відкриті питання

- Чи потрібен окремий `it`-запис для кожного dhātu з Dhātupāṭha (де
  реально фіксуються `seT`/`aniT` та подібні маркери), чи досить
  зберігати вже "очищене" значення поля `set_anit`, як зроблено вище?
  Пов'язано з `PANINI-IT-MARKERS`.
- `gaRa`-класифікація стосується виключно морфології дієвідміни — чи
  варто взагалі зберігати її в `panini-foundation`, чи це вже деталь
  рівня `PANINI-PRATYAYA-DERIVATION` (яка саме `vikaraRa` приєднується)?
  Залишено відкритим для наступної задачі.
- 20 коренів вище навмисно різноманітні за `gaRa`/`pada`/регулярністю,
  але це **не статистична вибірка** з 2000 коренів Dhātupāṭha — при
  розширенні реєстру варто явно позначати, за яким принципом додаються
  нові записи.

## Джерела

- Traditional Dhātupāṭha (10 gaṇa), перехресна перевірка потрібна проти
  принаймні одного цифрового видання і одного традиційного коментаря —
  правило 17 `AGENTS.md` (не покладатися на єдине джерело).
- [Sanskrit Heritage](https://sanskrit.inria.fr/) dhātu-таблиці — для
  порівняння з `PANINI-HERITAGE-AUDIT`.
- Vidyut dhātu-дані — для порівняння з `PANINI-VIDYUT-AUDIT`.
