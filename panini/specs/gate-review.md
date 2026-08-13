# Gate review: чи `panini/machine/` дочекався стабілізації v0.1?

Статус: завершено (`PANINI-MACHINE-GATE-REVIEW`).

`AGENTS.md` §13 і §24–25 явно ставлять milestone-гейт: жодної
реалізації (parser, VM, міст до My Lisp) до стабілізації
`panini-foundation-v0.1` (онтологія, реєстри dhātu/kāraka, кілька
повністю простежених прикладів). `panini/machine/` (694 рядки Lisp:
`panini-core.my`, `rules.my`, `compiler.my`, `siva-sutras.my`,
`meta.my`, `tests.my`) з'явився паралельно з рештою `foundation/`-
роботи, а не після неї. Ця задача не видаляє й не відкочує код —
лише чесно оцінює, чи гейт справді дотриманий.

## Хронологія (за mtime файлів)

```
03:04  dhatu.md, terminology.md
03:06  anuvrtti.md
03:24  pratyaya.md
05:00  ontology.md
05:20  karaka.md
05:30  pratyahara.md
06:05  paribhasha.md
07:10  it.md
07:11  rule-system.md
07:19  samjna.md
```

`panini/machine/*.my` не має окремого mtime-сліду в цій перевірці (не
знято окремо), але з git-логу видно: комміт `caa12ef` ("Add Rule
Engine v0.1 with Term, Prakriya, it-samjna, guRa, sandhi") датований
раніше за фінальні `it.md`/`rule-system.md`/`samjna.md` (07:10–07:19)
і за мою власну `PANINI-SUTRA-CITATION-VERIFICATION` (виконана вже
після цього перегляду). **Висновок: `panini/machine/` писався до того,
як `foundation/` дійсно стабілізувався й був звірений проти реального
джерела sūtra.** Формально гейт §24–25 не витриманий — реалізація
почалась паралельно з дослідженням, а не після його завершення.

## Що саме постраждало від передчасності

### 1. `make-action-graph` — саме та наївна модель, яку `AGENTS.md` §8 попереджав не приймати

```lisp
(defun make-action-graph (action-id dhatu kartf-entity karman-entity)
  (list action-id
        (cons 'dhAtu dhatu)
        (cons 'kartf kartf-entity)
        (cons 'karman karman-entity)))
```

Фіксована арність — рівно `kartf` + `karman`, без `karaRa`/
`sampradAna`/`apAdAna`/`aDikaraRa`. Це буквально той "ACTION з
фіксованими named slots per dhātu", який
[`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md)
(написано **раніше** за `machine/`, у цьому ж репозиторії) прямо
назвав спрощенням, яке сам текст Паніні не підтримує (`pac` з/без
`aDikaraRa` залежно від речення, не dhātu). Код `machine/` не посилається
на цей висновок і не документує це як свідоме архітектурне рішення —
просто реалізує спрощення мовчки. Якби гейт був дотриманий (спершу
дочекатись `PANINI-DHATU-KARAKA-RELATION`, вже виконаної на момент
написання коду — і справді, `dhatu-karaka-relation.md` вже існував!),
цей конкретний недолік можна було б уникнути свідомим рішенням, а не
випадковим повторенням уже знайденої й задокументованої помилки.

### 2. Дублювання реєстру dhātu — два джерела істини

`panini-core.my` містить **власний, inline, 6-корінний** список dhātu
(`BU`, `eD`, `dA`, `kf`, `gam`, `sTA`), окремий від
[`panini/registry/dhatu/`](../registry/dhatu) (20 файлів, YAML,
уже звірених у `PANINI-DHATU-REGISTRY-20`/`PANINI-TERMINOLOGY-GLOSSARY`).
Жодного механізму синхронізації між ними немає. Це класичний ризик
"двох джерел істини" — саме той тип проблеми, який `PANINI-TASKS-MY-RECONCILE`
(окрема задача) вже знайшов на рівні task-реєстрів; тут той самий
патерн повторюється на рівні даних.

### 3. Код не запущений

`TESTING.md` прямо каже: "Once the My Lisp VM is bootstrapped, you can
run the test suite" — умовний спосіб, не факт. Немає доказу, що
`panini-core.my`/`rules.my`/`tests.my` реально виконувались у My Lisp
інтерпретаторі й давали заявлений результат (`Bavati` з `BU + Sap +
tip`). Водночас `panini-foundation-v0.1.md` §10 (до мого виправлення
в `PANINI-V01-SPEC-METHODOLOGY-REVIEW`) стверджував "`it` = Compiler
Metadata ✅ Підтверджено і реалізовано" — "реалізовано" для коду, який
ще жодного разу не запускався, це передчасне твердження.

## Що зроблено правильно, попри передчасність

- **SLP1-дисципліна дотримана** — усі ідентифікатори в коді строго
  SLP1, як і вимагає `AGENTS.md` §2.
- **Архітектура `rules.my` (Term, Prakriya, it-samjna, guRa, sandhi)**
  явно перегукується з висновками `PANINI-VIDYUT-AUDIT`
  ([`vidyut-analysis.md`](../research/vidyut-analysis.md)) — журнал
  кроків деривації, а не єдина функція. Це саме той "reuse the idea,
  not the code" підхід, який аудит Vidyut рекомендував.
- Кожен `foundation/*.md` файл (окрім `terminology.md`, глосарію)
  використовує обов'язковий трирівневий формат `[PANINI]/
  [INTERPRETATION]/[MY-LISP HYPOTHESIS]` — методологічна дисципліна
  §21 формально дотримана на рівні документації, навіть коли гейт §24
  порушено на рівні реалізації.

## Висновок

Гейт **процедурно порушено**: `panini/machine/` писався до завершення
й перевірки `foundation/`, не після. Наслідок не катастрофічний —
знайдено 2 конкретні технічні проблеми (наївна `kartf`+`karman`-
модель, дубльований реєстр dhātu), а не системний провал — але обидві
проблеми були б імовірно уникнуті, якби послідовність `AGENTS.md`
§13/§24 витримувалась буквально: `dhatu-karaka-relation.md` уже містив
попередження, яке `machine/`-код проігнорував просто тому, що писався
паралельно, а не після нього.

**Рекомендація для наступної роботи над `panini-machine-model-v0.1`
(не виконується в цій задачі — лише фіксується):** звести
`panini-core.my`'s dhatu-registry до реального читання
`registry/dhatu/*.yaml` замість дублювання, і замінити фіксовану
арність `make-action-graph` на змінний список kāraka-пар, що
відповідає висновку `dhatu-karaka-relation.md`.

## Джерела

- Git-лог цього репозиторію (`git log --format='%h %ad %s'`),
  timestamps `foundation/*.md`.
- [`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md),
  [`research/vidyut-analysis.md`](../research/vidyut-analysis.md) —
  порівняння з уже задокументованими висновками.
- `panini/machine/panini-core.my`, `panini/machine/TESTING.md` —
  прочитано напряму.
