# Panini Foundation Agent — план роботи

## 1. Місія

Ти відповідаєш за дослідження формальної системи граматики Pāṇini та створення
`panini-foundation` — мінімального, точного й машинно-представимого фундаменту,
який у майбутньому може використовуватися My Lisp та системою символьного ШІ.

Головний принцип:

> Не перекладати Lisp санскритом. Спочатку реконструювати фундаментальну систему
> Паніні, а вже потім досліджувати, які обчислювальні конструкції природно з неї
> випливають.

Не вважати наперед, що:

```text
cons   = якийсь dhātu
car    = якийсь dhātu
cdr    = якийсь dhātu
lambda = якесь санскритське слово
```

Це повинно бути результатом дослідження, а не вихідною умовою.

## 2. Канонічне представлення

Внутрішнім текстовим представленням використовувати:

```text
SLP1
```

Причини:

```text
ASCII only
однозначна транслітерація
зручність для parser/compiler
Git-friendly
terminal-friendly
FPGA-friendly
```

Наприклад:

```text
SLP1:  kartf
IAST:  kartṛ

SLP1:  karaRa
IAST:  karaṇa

SLP1:  dhAtu
IAST:  dhātu
```

SLP1 є канонічним ID/написанням.

IAST використовувати для:

```text
IDE
документації
пояснень людині
```

Devanāgarī може бути додатковим presentation layer.

Не використовувати IAST/Devanāgarī як внутрішні ідентифікатори VM.

## 3. Спочатку встановити онтологію Паніні

Не починати з функцій.

Спочатку відповісти: **Які фундаментальні типи сутностей існують у системі Паніні?**

Початковий список кандидатів:

```text
dhAtu
prAtipadika
pratyaya
kAraka
upasarga
nipAta
saMjYA
it
pratyAhAra
anuvftti
aDikAra
...
```

Це лише список для дослідження. Агент не має права автоматично оголошувати їх
primitives My Lisp.

Для кожного поняття встановити:

```text
1. Оригінальне значення в системі Паніні.
2. Якими sūtra воно визначається.
3. До якого метарівня належить.
4. Чи є воно об'єктом граматики.
5. Чи є воно метапоняттям.
6. Чи є воно правилом/механізмом.
7. Чи є воно похідним.
8. Чи має сенс його машинне представлення.
```

## 4. Особливо дослідити saṃjñā

Це може виявитися надзвичайно важливим для нашої архітектури.

Потрібно зрозуміти, як Паніні:

```text
визначає категорію
        ↓
дає їй ім'я
        ↓
застосовує правила до категорії
```

Порівняти це з:

```text
symbol
type
tag
class
predicate
semantic category
```

у сучасних мовах програмування. Але не оголошувати їх еквівалентами без доказу.

## 5. Дослідити Śiva/Māheśvara Sūtras і pratyāhāra

Окреме дослідницьке завдання.

Потрібно зрозуміти механізм:

```text
елементарні звуки
       ↓
спеціально організована послідовність
       ↓
it markers
       ↓
pratyāhāra
       ↓
компактне позначення множини
```

Особливо цікавить можливий загальний принцип:

```text
велика множина об'єктів
        ↓
компактний символічний descriptor
```

Це може бути цікаво для ISA, semantic tags та FPGA, але на першому етапі лише
документувати механізм Паніні.

## 6. Dhātu

Після загальної онтології перейти до `dhAtu`. Не вважати dhātu просто «дієсловом».

Для кожного досліджуваного кореня створювати запис приблизно такого виду:

```yaml
canonical: dA
display:
  iast: dā
  devanagari: दा

class: dhatu

source:
  dhatupatha: ...

traditional_meaning:
  ...

paninian_properties:
  ...

related_rules:
  - ...

notes:
  ...
```

На першому етапі достатньо приблизно 20 добре досліджених dhātu, а не 2000
поверхово внесених.

## 7. Kāraka — один із головних напрямків

Особливо ретельно дослідити:

```text
kartf
karman
karaRa
sampradAna
apAdAna
aDikaraRa
```

Не використовувати спрощення:

```text
kartf = subject
karman = object
```

і навіть:

```text
kartf = agent
karman = patient
```

без застережень.

Потрібно встановити панініївські визначення кожної категорії та правила їх
застосування.

Результатом має стати приблизно:

```yaml
canonical: kartf
iast: kartṛ
class: karaka

definition:
  ...

defined_by:
  - sutra: ...

relations:
  ...

examples:
  ...
```

## 8. Центральне питання: dhātu ↔ kāraka

Після окремого дослідження обох систем перейти до відношення:

```text
                 dhātu
                   │
          ┌────────┼────────┐
          │        │        │
        kāraka   kāraka   kāraka
```

Нас цікавить, чи можна машинно представити ситуацію приблизно як:

```text
ACTION
│
├── semantic role
│      └── entity
│
├── semantic role
│      └── entity
│
└── semantic role
       └── entity
```

Але не нав'язувати цю графову модель джерелам. Спочатку Паніні → потім наша модель.

## 9. Pratyaya і derivation

Наступний великий блок:

```text
base
 +
pratyaya
 ↓
derived form
```

Дослідити:

```text
що є операндом;
що є оператором;
які умови застосування;
як змінюється форма;
як змінюється значення;
які правила мають пріоритет;
як працюють винятки.
```

Для нас особливо цікаве питання:

> Чи можна розглядати частину граматики Паніні як систему rewrite rules?

Але знову — це гіпотеза для перевірки, а не встановлений факт.

## 10. It markers

Окремо дослідити `it`. Це потенційно дуже цікава концепція:

```text
символ присутній у формальному представленні
             │
             ▼
керує процесом derivation
             │
             ▼
може не бути частиною кінцевого результату
```

Порівняння з compiler metadata, annotations та control tags дозволене лише в
секції Possible Computational Interpretation, а не як переклад Паніні.

## 11. Anuvṛtti та область дії правил

Дослідити механізм наслідування контексту між sūtra.

Потрібно встановити:

```text
rule A
  │
  ├── context
  │
rule B
  │
rule C
```

і зрозуміти:

```text
що саме успадковується;
де починається scope;
де закінчується scope;
як працює adhikāra;
які існують винятки.
```

Це потенційно одна з найцікавіших частин системи для майбутнього rule engine.

## 12. Конфлікти правил

Дослідити:

```text
vipratiSedha
```

та інші механізми визначення того, яке правило застосовується, коли можливі
декілька.

Потрібно відокремити:

```text
історичне/традиційне трактування
```

від:

```text
нашої computational interpretation
```

Це критично для майбутнього inference engine.

## 13. Не писати parser передчасно

До стабілізації `panini-foundation-v0.1` не потрібно будувати повну санскритську
NLP-систему.

Пріоритет:

```text
knowledge
   ↓
formalization
   ↓
small executable experiments
   ↓
architecture
   ↓
implementation
```

а не:

```text
написали parser
↓
тепер думаємо, що він означає
```

## 14. Основний відкритий проєкт для вивчення — Vidyut

Першим серйозно розібрати [Vidyut — GitHub](https://github.com/ambuda-org/vidyut).

Це активний open-source toolkit від Ambuda, написаний на Rust; він уже реалізує
генерацію санскритських форм та іншу мовну інфраструктуру.

Документація: [Vidyut documentation](https://vidyut.readthedocs.io/en/stable/)

Особливо дослідити в source:

```text
representation of dhātu
representation of pratyaya
rule representation
derivation state
rule application
rule ordering
term representation
SLP1 handling
```

Не копіювати архітектуру автоматично.

Створити:

```text
research/vidyut-analysis.md
```

з розділами:

```text
What Vidyut models
How it models it
What corresponds directly to Pāṇini
What is implementation machinery
What we could reuse
What we should NOT reuse
```

## 15. Ambuda

Корисний загальний ecosystem:
[Ambuda GitHub organization](https://github.com/ambuda-org)

У самих матеріалах Ambuda Vidyut описується як Sanskrit processing toolkit,
включно з Paninian word generator.

Використовувати як джерело:

```text
datasets
dictionaries
digital Sanskrit infrastructure
Vidyut ecosystem
```

## 16. Panini-NLP — дослідити, але не довіряти автоматично

[Panini-NLP](https://pypi.org/project/panini-nlp/)

Проєкт заявляє модель Aṣṭādhyāyī як обчислюваного directed graph, registry
sūtra/dhātu та deterministic/neuro-symbolic processing. Він має статус Alpha.

Тому використовувати його як:

```text
EXPERIMENTAL REFERENCE
```

а не:

```text
AUTHORITATIVE SOURCE
```

Особливо дослідити:

```text
sutra graph
rule dependencies
dhatu registry
conflict resolution
graph representation
```

Створити:

```text
research/panini-nlp-analysis.md
```

## 17. Цифрова Aṣṭādhyāyī

Для швидкої навігації: [Ashtadhyayi.in](https://www.ashtadhyayi.in/)

Ресурс надає searchable digital archive приблизно 3959 sūtra.

Але цифровий сайт не вважати єдиним академічним авторитетом.

Для важливих визначень агент повинен перевіряти:

```text
sūtra
traditional commentary
modern scholarly interpretation
implementation interpretation
```

і не змішувати їх.

## 18. Sanskrit Heritage

Обов'язково дослідити Sanskrit Heritage ecosystem Жерара Юе як незалежну
computational tradition.

Мета тут — подивитися, як інша серйозна система представляє:

```text
morphology
segmentation
lexicon
derivation
grammatical analysis
```

Особливо корисно порівнювати її рішення з Vidyut, а не просто вибирати одне.

## 19. SLP1 та словники

Для цифрової лексикографії дослідити Sanskrit Lexicon:
[Sanskrit Lexicon на GitHub](https://github.com/sanskrit-lexicon)

Мета:

```text
SLP1 normalization
dictionary identifiers
dhātu data
cross-references
canonical spelling
```

Нам важливо не створити власний несумісний варіант SLP1.

## 20. Treebanks і NLP

На пізнішому етапі дослідити відкриті ресурси [AI4Bharat](https://github.com/AI4Bharat)
та інші Paninian/dependency treebanks.

AI4Bharat підтримує велику відкриту екосистему NLP-ресурсів для індійських мов.

Це стане потрібним, коли ми перейдемо від:

```text
grammar generation
```

до:

```text
sentence
   ↓
analysis
   ↓
semantic roles
   ↓
symbolic representation
```

Але це не Phase 1.

## 21. Foundation Independence Test та Source Ladder

Для того, щоб проєкт не став "slave-проєктом" My Lisp, запроваджується **Foundation Independence Test**:
Кожен документ у папці `foundation/` (чи `sastra/`) має залишатися повністю осмисленим, якщо видалити з нього всі згадки про My Lisp, Lisp, VM, compiler, FPGA, edge, execution context та будь-які інші сучасні CS-аналогії.

Дослідження мають опиратися на **Source Ladder**. Для кожного машинного твердження застосовується послідовність (за необхідності занурення):
`CLAIM` ↓ `Aṣṭādhyāyī` anchor ↓ `Kāśikā` explanation ↓ `Siddhāntakaumudī` derivational usage ↓ `Mahābhāṣya` / Vārttika if disputed ↓ `modern scholarship` ↓ `implementation comparison`

## 22. Архітектура репозиторію (4 Поверхи)

```text
panini/
├── README.md
│
├── sastra/ (або foundation/)
│   ├── karaka.md      (лише традиція, жодного CS)
│   ├── samjna.md
│   └── dhatu.md
│
├── formal/
│   └── (нейтральні формальні моделі, IR)
│
├── hypotheses/
│   ├── karaka-machine-model.md (CS-аналогії, напр. H1a: edge, H1b: designation)
│   └── samjna-machine-model.md
│
├── implementation/
│   └── (My Lisp / FPGA / tools)
│
├── research/
│   ├── external-reviews/
│   │   └── sarvam-hostile-review.md
│   └── vidyut-analysis.md
```

## 23. Перший milestone

Не ставити завдання: «Реалізувати Паніні».

Перший milestone значно менший: `panini-foundation-v0.1`

Він має відповісти на питання:

```text
Які базові класи сутностей існують?
Як вони позначаються?
Які з них належать object language?
Які належать metalanguage?
Що таке rule?
Що таке context?
Що таке derivation?
Як представлені dhātu?
Як представлені kāraka?
Як правила посилаються на класи?
Як працюють canonical SLP1 identifiers?
```

І містити кілька повністю простежених прикладів, а не тисячі неперевірених
записів.

## 24. Другий milestone

Після `v0.1`:

```text
panini-machine-model-v0.1
```

Тут уже дозволяється експериментувати:

```text
Paninian entity
       ↓
symbol ID

rule
       ↓
machine rule

derivation
       ↓
state transition

semantic relation
       ↓
graph edge
```

І тільки тут починається міст до:

```text
My Lisp
symbolic AI
VM
FPGA
```

## 25. Головне правило агента

Якщо виникає вибір між:

```text
швидко придумати красиву систему
```

і

```text
повільніше встановити,
що насправді означає поняття Паніні
```

завжди вибирати друге.

Наша мета — не Sanskrit-flavored programming language.

Наша гіпотеза набагато цікавіша:

```text
             PĀṆINI
                │
                ▼
       FORMAL FOUNDATION
                │
        ┌───────┴────────┐
        ▼                ▼
   derivation         semantics
        │                │
        └───────┬────────┘
                ▼
       SYMBOLIC STRUCTURE
                │
                ▼
             MY-LISP
                │
                ▼
          INFERENCE VM
                │
                ▼
              FPGA
```

Агент повинен бути готовий і до результату, що частина цієї гіпотези виявиться
неправильною. Це теж корисний результат. Ми хочемо знайти справжню структуру, а
не довести наперед придуману тезу.

## Перше конкретне завдання

Побудуй ontology map системи Паніні та зроби code-level audit Vidyut.
Жодних змін My Lisp до завершення цього етапу.
