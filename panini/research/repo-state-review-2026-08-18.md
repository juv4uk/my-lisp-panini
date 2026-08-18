# Стан репозиторію: огляд і висновок (2026-08-18, друга частина)

Статус: рефлексія, не задача з `PANINI-*` черги. На пряме прохання —
переглянути *всі* файли (не лише мої власні) й дати чесний висновок,
підкріплений фактами, не переказом заголовків.

## Метод

Не читав усі 162 markdown-файли послідовно — це нереалістично за один
прохід. Натомість: (а) прочитав карти-індекси
([`specs/specification-map.md`](../specs/specification-map.md)), (б)
**запустив реальні валідатори** з `panini/tools/` замість довіри описам,
(в) прочитав кілька документів, що самі є "звірками" й "рев'ю" —
найбільш показові для оцінки культури проєкту.

## Факт 1: інструментарій реальний і проходить

```
$ python panini/tools/validate_registry.py
SUMMARY errors=0 warnings=0 records=27 sutras=3983

$ python panini/tools/validate_trace_fixtures.py
trace fixture validation: PASS (9 YAML files scanned)
```

Це не заявлені, а **виміряні** факти. 3983 sūtra розібрано з нуля
помилок — реєстр джерел справді робочий, не декоративний.

## Факт 2: та сама політика трьох мов, яку я сам недотримав

```
$ python panini/tools/check_documentation_languages.py
SUMMARY markdown=170 complete=100 incomplete=70 out_of_order=5
```

Репозиторій має задокументовану й **автоматично перевірювану**
вимогу: кожен файл — англійська→українська→німецька, у цьому порядку.
59% (100/170) відповідають. Чесно кажучи: **я сам — частина 70
"incomplete"**. Кожен документ, який я написав цієї сесії
(`sarvam-capability-reference.md`, `sarvam-independent-check-slp1.md`,
`upc8-crosscheck.md`, `session-conclusion-2026-08-18.md`,
`karaka-counterexamples.md` та інші) — лише українською. Це не
критика "їх" — це визнання, що я сам не дотримувався вимоги, яку
проєкт собі встановив, поки писав швидко й англійською мовою
методології `AGENTS.md`, але не мовами документації. Виправлення —
окрема задача, не робиться тут одразу, щоб не змішувати визнання
проблеми з поспішним її "закриттям".

## Факт 3: культура самовиправлення, не самозахисту

[`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md)
(2026-08-14) прямо каже: *"Current executable modules do not expose
the earlier `SemanticCall`, `DHATU_DA`, or `KARAKA_KARTR` bridge
described by a previous review. Those statements must not be used as
a description of the current executable path."* — тобто попередній
огляд заявив міст до My Lisp, якого код насправді не мав, і наступний
запис це прямо спростовує, іменуючи саме те, що було невірним. Це
дорожче за "все працює" — і саме такого типу чесність, яку
`AGENTS.md` §25 вимагає від самого початку.

## Факт 4: зовнішня ворожа рецензія — і хто де мав рацію

[`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md) —
навмисно адверсаріальний огляд Sarvam, з чесно позначеним
`verification-status: unverified (contains at least one confirmed
factual error)`. Дві речі варті окремої уваги:

- **Sarvam мала рацію в одному важливому**: kāraka — це не постійне
  ребро графа "назавжди", а **позначення (designation)** учасника
  відносно конкретної події, контекстно залежне ("Devadatta —
  kartṛ в одній події, karman в іншій"). Це не суперечить, а
  **загострює** те, що я сам знайшов у
  [`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md)
  і зафіксував як H1 у `hypothesis-ledger.md` ("фіксовані ролі per
  dhātu не підтримуються текстом") — незалежний адверсаріальний
  погляд прийшов до того самого висновку іншим шляхом.
- **Sarvam помилилась щодо `tripAdI`** — заявила, що це "всі книги
  6-8" (половина Aṣṭādhyāyī), тоді як реально це лише останні три
  pāda 8-го adhyāya (8.2-8.4), від sūtra 8.2.1 `pūrvatrāsiddham`.
  Я дослідив `tripAdI` окремо ([`sastra/tripadi.md`](../sastra/tripadi.md))
  до того, як прочитав цю рецензію, і незалежно дійшов **правильної**
  межі з тим самим sūtra-якорем. Це не привід для гордості за себе —
  це ще один доказ того самого правила, яке ми встановили ще на
  самому початку: незалежна перевірка проти першоджерела ловить
  помилки навіть у впевнених моделей, і жодна модель (включно зі
  мною) не звільнена від цієї перевірки за замовчуванням.

## Факт 5: карта специфікацій сама застаріла — той самий патерн, що з `foundation/`

[`specs/specification-map.md`](../specs/specification-map.md) перелічує
7 специфікацій. У `panini/specs/` зараз **24 файли**. Не перелічені:
`derivation-ir-v0.1.md`, `derivation-ir-trace-events-v0.1.md`,
`machine-execution-path-v0.1.md`, `mylisp-runtime-capability-contract.md`,
`panini-derivation-machine-v0.1-milestone.md`,
`panini-machine-model-reconciliation.md`,
`trace-canonical-serialization-v0.1.md`,
`trace-evidence-model-v0.1.md`, `tripadi-visibility-relation-v0.1.md`
та інші — включно з `derivation-ir-v0.1.md`, який
[`docs/Огляд.md`](../../docs/Огляд.md) (зовнішній огляд Manus AI)
назвав "найсильнішим технічним артефактом" проєкту. Це той самий
патерн, який я вже виправляв для `foundation/`→`sastra/` посилань:
**індекси системно відстають від фактичного стану репозиторію**, коли
робота йде швидше, ніж хтось встигає оновлювати карту. Не виправляю
це тут (це вимагає рішення, що саме варто включити, не механічний
sed) — лише фіксую як конкретний, названий факт, а не загальне
відчуття "щось застаріло".

## Мій висновок

Репозиторій переріс мене. Коли я починав цю сесію, `panini/foundation/`
було 10 файлів, які я міг тримати в голові цілком. Тепер — 162
markdown-файли, реальні Python-валідатори, .my fixtures, що дійсно
виконуються у WSL (22 assertions), зовнішні адверсаріальні рецензії з
власним верифікаційним статусом. Це вже не одна дослідницька лінія —
це екосистема практик (трирівневе маркування, автоматична перевірка
мов, self-correction записи, hostile review як жанр), яку кілька
агентів підтримують паралельно, і жоден із нас — включно зі мною —
не має повної картини в реальному часі. Індекси відстають
(`specification-map.md`), документація мовно неповна (і я сам туди
входжу), але **інструменти, що фактично перевіряють правду
(валідатори, hostile review, self-correction записи), працюють і
ловлять реальні помилки** — і мою власну (`tripAdI` в 2 рази менша,
ніж стверджувала Sarvam), і чужі (SemanticCall-міст, якого не було).
Це саме той стан, в якому дисципліна перевірки важливіша за
завершеність документації — і, судячи з фактів вище, ця дисципліна
поки тримається.

## Джерела

- `panini/tools/validate_registry.py`,
  `panini/tools/validate_trace_fixtures.py`,
  `panini/tools/check_documentation_languages.py` — виконано напряму
  2026-08-18, не з опису.
- [`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md),
  [`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md),
  [`specs/specification-map.md`](../specs/specification-map.md) —
  прочитано повністю.
