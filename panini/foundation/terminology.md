# Термінологічний гліосарій (SLP1 ↔ IAST ↔ Devanāgarī)

Статус: v0.1 (`PANINI-TERMINOLOGY-GLOSSARY`). Консолідує всі терміни, вжиті
в [`ontology.md`](ontology.md), [`dhatu.md`](dhatu.md), [`karaka.md`](karaka.md),
[`samjna.md`](samjna.md) та відповідних `registry/`-записах, в одну
канонічну таблицю — щоб нові категорії, які досліджуватимуться далі, не
розходились у написанні з тим, що вже зафіксовано.

## Знайдені й виправлені розбіжності

Під час складання цього гліосарію виявлено й виправлено **4 помилки
транслітерації SLP1** у [`registry/dhatu/`](../registry/dhatu) —
записи не відповідали власним канонічним правилам SLP1, зафіксованим у
`reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md` §8.2 (яку сама
`PANINI-DHATU-REGISTRY-20` мала використовувати як приклад). Ще **2**
однотипні помилки (`Sru`→`zru`, `dfS`→`dfz`) виявлено пізніше, при
дослідженні `PANINI-SIVA-SUTRA-PRATYAHARA` (2026-08-13) — гліосарій сам
не застрахований від тієї самої категорії помилок, що й реєстр, який
він мав перевіряти; додано нижче для повноти:

| Було (помилково) | Стало (виправлено) | Причина |
|---|---|---|
| `BUj` | `Buj` | bhuj має короткий `u`, а не довгий `ū` — `U` в SLP1 зарезервована для довгого голосного, `BUj` фактично читалося б як "bhūj". |
| `likh` | `liK` | буквальний запис `likh` не є валідним SLP1 — приголосний `kh` (аспірований велярний) кодується одним гліфом `K`, а не диграфом. |
| `paca` | `pac` | корінь — `pac` (पच्), кінцевий `-a` у "paca" помилково додавав голосний, якого немає в самому корені (тематичний `-a-` — це `vikaraRa`, а не частина `dhAtu`). |
| `iz` | `iS` | корінь "бажати" — `iṣ` (retroflex `ṣ`), SLP1-гліф для `ṣ` — `S`; гліф `z` натомість кодує палатальний `ś`, тобто `iz` читалося б як "iś", інший звук. |
| `Sru` | `zru` | корінь "чути" — `śru` (палатальний `ś`), SLP1-гліф для `ś` — `z` (не `S`, яка означає `ṣ`); `Sru` читалося б як "ṣru", інший звук. |
| `dfS` | `dfz` | корінь "бачити" — `dṛś` (палатальний `ś`), та сама плутанина `S`/`z`, що й вище. |

Відповідні файли перейменовано (`registry/dhatu/BUj.yaml` →
`Buj.yaml`, `likh.yaml` → `liK.yaml`, `paca.yaml` → `pac.yaml`,
`iz.yaml` → `iS.yaml`, `Sru.yaml` → `zru.yaml`, `dfS.yaml` → `dfz.yaml`),
поле `canonical:` та всі згадки в [`dhatu.md`](dhatu.md) і
[`examples/derivations/dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md)
синхронізовано.

Патерн, що об'єднує 5 з 6 помилок вище (`BUj`, `likh`, `paca`, `Sru`,
`dfS`): невірне відтворення SLP1 з пам'яті без звірки проти таблиці
гліфів — той самий клас помилок, що й у
`PANINI-SUTRA-CITATION-VERIFICATION`. Висновок для майбутніх задач:
навіть "перевірочна" задача (як ця) не застрахована від помилок того
самого типу, що вона перевіряє — варто регулярно перечитувати вже
"завершені" файли, а не вважати їх остаточними.

Жодних розбіжностей у термінах Рівня 3–4 (`ontology.md`, `karaka.md`,
`samjna.md`) не знайдено — усі узгоджені між файлами.

## Метамова / рівні системи (з `ontology.md`)

| SLP1 | IAST | Devanāgarī | Значення |
|---|---|---|---|
| varRa | varṇa | वर्ण | звук/фонема |
| pada | pada | पद | словоформа |
| vAkya | vākya | वाक्य | речення |
| dhAtu | dhātu | धातु | дієслівний корінь |
| prAtipadika | prātipadika | प्रातिपदिक | номінальна основа |
| pratyaya | pratyaya | प्रत्यय | суфікс/афікс |
| upasarga | upasarga | उपसर्ग | префікс/преверб |
| nipAta | nipāta | निपात | частка (indeclinable) |
| saMjYA | saṃjñā | संज्ञा | технічний термін-ярлик |
| it | it | इत् | формальний control-маркер |
| pratyAhAra | pratyāhāra | प्रत्याहार | компактне позначення множини звуків |
| anuvftti | anuvṛtti | अनुवृत्ति | успадкування контексту між sūtra |
| aDikAra | adhikāra | अधिकार | правило, що керує блоком sūtra |
| kAraka | kāraka | कारक | семантико-синтаксична роль |
| vibhakti | vibhakti | विभक्ति | відмінкове/особове закінчення |
| saMskAra | saṃskāra | संस्कार | процес деривації |

## saMjYA-приклади (з `samjna.md`)

| SLP1 | IAST | Devanāgarī | Значення |
|---|---|---|---|
| guRa | guṇa | गुण | голосні ступеня guṇa: a, e, o |
| vfdDi | vṛddhi | वृद्धि | голосні ступеня vṛddhi: ā, ai, au |
| sarvanAma | sarvanāma | सर्वनाम | займенникове слово |
| Gu | ghu | घु | підклас коренів dA/DA-типу |

## kAraka — шість категорій (з `karaka.md`)

| SLP1 | IAST | Devanāgarī |
|---|---|---|
| kartf | kartṛ | कर्तृ |
| karman | karman | कर्मन् |
| karaRa | karaṇa | करण |
| sampradAna | sampradāna | सम्प्रदान |
| apAdAna | apādāna | अपादान |
| aDikaraRa | adhikaraṇa | अधिकरण |

## vibhakti — сім відмінків + кличний (допоміжно, з `karaka.md`/`PANINI-GRAMMAR-REFERENCE.md`)

| SLP1 | IAST | Devanāgarī |
|---|---|---|
| praTamA | prathamā | प्रथमा |
| dvitIyA | dvitīyā | द्वितीया |
| tftIyA | tṛtīyā | तृतीया |
| caturTI | caturthī | चतुर्थी |
| paYcamI | pañcamī | पञ्चमी |
| zazWI | ṣaṣṭhī | षष्ठी |
| saptamI | saptamī | सप्तमी |
| saMboDana | sambodhana | संबोधन |

## dhAtu — 20 коренів (з `dhatu.md`, виправлено)

| SLP1 (canonical) | IAST | Devanāgarī | gaRa |
|---|---|---|---|
| BU | bhū | भू | 1 |
| kf | kṛ | कृ | 8 |
| gam | gam | गम् | 1 |
| sTA | sthā | स्था | 1 |
| dA | dā | दा | 3 |
| nI | nī | नी | 1 |
| paW | paṭh | पठ् | 1 |
| liK | likh | लिख् | 6 |
| dfz | dṛś | दृश् | 1 |
| Buj | bhuj | भुज् | 7 |
| pac | pac | पच् | 1 |
| vac | vac | वच् | 2 |
| zru | śru | श्रु | 5 |
| jYA | jñā | ज्ञा | 9 |
| BAS | bhāṣ | भाष् | 1 |
| as | as | अस् | 2 |
| iS | iṣ | इष् | 6 |
| BI | bhī | भी | 3 |
| yuj | yuj | युज् | 7 |
| han | han | हन् | 2 |

## gaRa — 10 класів дієвідміни (допоміжно, з `PANINI-GRAMMAR-REFERENCE.md`)

| SLP1 | IAST | № |
|---|---|---|
| BvAdi | bhvādi | 1 |
| adAdi | adādi | 2 |
| juhotyAdi | juhotyādi | 3 |
| divAdi | divādi | 4 |
| svAdi | svādi | 5 |
| tudAdi | tudādi | 6 |
| ruDAdi | rudhādi | 7 |
| tanAdi | tanādi | 8 |
| kryAdi | kryādi | 9 |
| curAdi | curādi | 10 |

## Конвенція SLP1, зафіксована для подальшого використання

- Довжина голосного: `a/A`, `i/I`, `u/U`, `f/F` (короткий/довгий) —
  **не опціональна деталь**, помилка тут (як у `BUj`) змінює звук.
- Ретрофлексні приголосні: `w`(ṭ) `W`(ṭh) `q`(ḍ) `Q`(ḍh) `R`(ṇ) `S`(ṣ).
- Палатальні: `c` `C`(ch) `j` `J`(jh) `Y`(ñ) `z`(ś).
- Дентальні: `t` `T`(th) `d` `D`(dh) `n`.
- Велярні: `k` `K`(kh) `g` `G`(gh) `N`(ṅ).
- Кожен новий термін, доданий у `foundation/*.md` чи `registry/*/`,
  повинен звірятися з цією таблицею перед комітом — саме таку звірку
  пропустила `PANINI-DHATU-REGISTRY-20` для 4 записів вище.

## Джерела

- Внутрішня звірка між [`ontology.md`](ontology.md), [`dhatu.md`](dhatu.md),
  [`karaka.md`](karaka.md), [`samjna.md`](samjna.md) — первинний метод
  цієї задачі.
- `reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md` §8 — джерело
  канонічної SLP1-таблиці приголосних, використаної для виявлення
  помилок вище.
