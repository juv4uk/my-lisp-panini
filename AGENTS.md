# Panini Foundation Agent — план роботи

## 0. Session start — приєднання до рою

Перед будь-якою роботою підняти власний `swarm-node` і приєднатись:

```bash
wsl -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp && \
  ./target/debug/swarm-node --port 9106 --node-id my-lisp-panini-1 \
  --project my-lisp-panini --data-dir ~/.swarm-node/my-lisp-panini-1 \
  --connect 127.0.0.1:9101 --connect 100.113.68.50:9101 &'
```

Journal переживає перезапуск процесу (перевірено на практиці — після
падіння WSL 2026-08-18 вузол відновив 2179 подій із диска), але сам
процес **не** переживає перезавантаження машини — після ребута
потрібно підняти його заново й повторити `join`:

```
(join (capabilities (sanskrit dhatu karaka slp1 grammar-research)) (roles (voter)))
```

Далі — `(next-best-action (from "my-lisp-panini-1"))` для пропозиції
задачі, `(claim-task ...)`/`(complete-task ... (generation N))` для
роботи з чергою `PANINI-*`. Якщо після реконекту виявляться "завислі"
claim з попередньої сесії, під якими немає реального контексту в
поточній розмові — чесніше `(release-task ...)`, ніж вигадувати
завершення роботи, якої не пам'ятаєш.

## 1. Місія

Ти відповідаєш за дослідження формальної системи граматики Pāṇini та побудову
**executable epistemology Паніні**.

Машина повинна працювати зі знанням, походженням знання і його виведенням:
`(symbol value proof)`.

Головний принцип:
> Не перекладати Lisp санскритом і не «реалізовувати Паніні». Спочатку реконструювати фундаментальну систему
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

## 13. Не писати parser передчасно (Ніякого Panini NLP)

До стабілізації `panini-foundation-v0.1` заборонено будувати повну санскритську
NLP-систему або оптимізувати систему на здатність аналізувати довільний санскритський текст.

Пріоритет:

```text
knowledge
   ↓
formalization
   ↓
small executable experiments (one full derivation)
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

## 21. Правило «Ніякої семантики без provenance»

Заборонено вводити семантику (наприклад, графи, ролі, функції) без доведення її походження з системи Паніні.
Кожен термін, кожна сутність у `foundation/` має бути задокументована за такою 4-шаровою структурою:

```text
[PANINI]
джерело + sūtra + традиційне трактування

[SCHOLARLY INTERPRETATION]
що стверджує сучасна наука

[COMPUTATIONAL INTERPRETATION]
як це можна формалізувати

[MY-LISP HYPOTHESIS]
що ми хочемо з цього зробити
```

Жодна сутність з четвертого шару (гіпотези) не повинна автоматично проникати назад у перший шар.

Для того, щоб проєкт не став "slave-проєктом" My Lisp, запроваджується **Foundation Independence Test**:
Кожен документ у папці `foundation/` (чи `sastra/`) має залишатися повністю осмисленим, якщо видалити з нього всі згадки про My Lisp, Lisp, VM, compiler, FPGA, edge, execution context та будь-які інші сучасні CS-аналогії.

Дослідження мають опиратися на **Source Ladder**. Для кожного машинного твердження застосовується послідовність (за необхідності занурення):
`CLAIM` ↓ `Aṣṭādhyāyī` anchor ↓ `Kāśikā` explanation ↓ `Siddhāntakaumudī` derivational usage ↓ `Mahābhāṣya` / Vārttika if disputed ↓ `modern scholarship` ↓ `implementation comparison`

## 21a. Proof-Carrying Derivation

Центральною ідеєю системи є Proof-Carrying Derivation.
Замість `input → engine → result` ми робимо:

```text
input
 ↓
state₀
 ↓ rule X
state₁
 ↓ rule Y
...
result
+ proof graph
```

Результат без історії його отримання вважається неповним. Наступним практичним кроком має бути **одна повна канонічна derivation**, яка від початку до кінця генерує такий proof.

## 21b. Cross-Repo Epistemic Dependencies

Існує строга межа відповідальності між `my-lisp-panini` та репозиторієм `shiva-sutras`.
`shiva-sutras` є **upstream research authority** для Śiva-sūtras, pratyāhāra, структури маркерів, канонічного порядку та їх математичної/епістемічної основи.

Правила взаємодії з `shiva-sutras`:
1. **Односторонній імпорт**: `my-lisp-panini` не має права заново встановлювати чи "покращувати" фундаментальні факти про Śiva-sūtras. Він може лише споживати явно позначені результати з upstream.
2. **Cross-Repo Provenance**: Заборонено копіювати твердження без походження. Кожен імпорт має вказувати репозиторій, конкретний claim, його статус (напр., `proved-in-model`, `UNRESOLVED`) та SHA комміту. На практиці такі блоки записуються inline, у документі, що споживає claim (напр. у `sastra/pratyahara.md`), поруч із твердженням, яке вони обґрунтовують — окремого централізованого реєстру `panini/coordination/dependencies.yaml` наразі не існує (перевірено 2026-08-18; директорія `panini/coordination/` відсутня). Якщо централізований реєстр колись буде створений, ця секція має бути оновлена, щоб вказувати на нього.
   ```yaml
   dependency:
     repository: juv4uk/shiva-sutras
     claim: shiva.marker-minimum-14
     status_at_import: proved-in-model
     revision: <commit-sha>
   ```
   Імпортовані ID (стабільні upstream-експорти, див. `shiva-sutras/docs/claims-export.yaml`): `SS-CANON-001`, `SS-PRATYAHARA-001`, `SS-MARKERS-001..003`, `SS-ORDER-001`, `SS-CORPUS-001`, `SS-EPISTEMIC-001..002`.
3. **Обмеження гіпотез**: Невирішений статус (UNRESOLVED) в upstream не означає, що твердження хибне, але його не можна використовувати як foundation. На ньому можна будувати лише експериментальні гіпотези (`[EXPERIMENTAL HYPOTHESIS]`).
4. **Заборона на диктування**: `my-lisp-panini` може ставити upstream-агенту лише дослідницькі питання. Заборонено давати завдання, які диктують бажаний результат (наприклад, "знайди докази, що pratyāhāra — це ISA encoding"). Upstream-результати потрібно поважати.

## 22. Архітектура репозиторію (4 Поверхи)

Історична примітка: директорія `foundation/` була перейменована на
`sastra/`; `formal/` як окрема директорія так і не була створена —
формальні IR-специфікації живуть у `specs/` (напр.
`derivation-ir-v0.1.md`). Дерево нижче відображає фактичний стан на
2026-08-18, не оригінальний ескіз:

```text
panini/
├── README.md
│
├── sastra/
│   ├── karaka.md      (лише традиція, жодного CS)
│   ├── samjna.md
│   └── dhatu.md
│
├── specs/
│   └── (нейтральні формальні моделі, IR — напр. derivation-ir-v0.1.md)
│
├── hypotheses/
│   ├── karaka-machine-model.md (CS-аналогії, напр. H1a: edge, H1b: designation)
│   └── samjna-machine-model.md
│
├── machine/
│   └── (виконуваний My Lisp bridge-код)
│
├── implementation/
│   └── (My Lisp / FPGA / tools)
│
├── registry/
│   └── dhatu/ (машинно-читані SLP1-записи)
│
├── examples/derivations/
│   └── (простежені приклади з provenance)
│
├── tests/
│   └── (fixtures, conformance-звіти)
│
├── tools/
│   └── (реальні Python-валідатори: validate_registry.py, тощо)
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

І містити кілька повністю простежених прикладів (зокрема **одну повністю доказову derivation**), а не тисячі неперевірених
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
```

І тільки тут починається міст до:

```text
My Lisp
symbolic AI
VM
FPGA
```

**Увага:** Концепції на зразок Graph Rewriting (або `semantic relation -> graph edge`) повинні розглядатися виключно як `[MY-LISP HYPOTHESIS]`, а не як встановлена базова онтологія. Слід також розглядати Term Rewriting, Constraint Propagation чи Contextual Transformations.

## 25. Нові пріоритети та головне правило агента

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

## Перше конкретне завдання та Пріоритети

Припини розширення machine model. Заверши epistemically clean Panini foundation згідно з цими пріоритетами:

```text
1. saMjYA
2. anuvftti + aDikAra
3. it
4. pratyAhAra
5. paribhASA / conflict mechanisms
6. dhAtu + pratyaya
7. ONE canonical derivation (повністю доказова)
8. Proof-Carrying Derivation IR
9. machine model v0.1
10. тільки потім general inference engine
```

Жодних змін My Lisp до завершення foundation milestone. Кожен термін повинен мати provenance, рівень абстракції, sūtra/source, traditional interpretation та окремо computational hypothesis.

## 26. Максима координації

> **Не копіюй знання між репозиторіями — посилайся на нього. Не копіюй гіпотезу як факт — імпортуй її статус. Не проси upstream підтвердити downstream-дизайн.**
>
> ## 27. Swarm Contract v0.1 & Агентні ролі
>
> `my-lisp-panini` функціонує в системі як **Knowledge Compiler**.
> 
> У системі існують 4 універсальні ролі для агентів:
> - **RESEARCHER**: висуває та перевіряє claims (напр., визначає онтологію).
> - **BUILDER**: створює формальне представлення або імплементацію.
> - **VERIFIER**: здійснює hostile review, перевіряє provenance або conformance.
> - **COORDINATOR**: (tauricode) планує задачі та агрегує їх.
> 
> **Головне правило рою**: Агент не володіє задачею, репозиторій володіє знанням. Агенти приходять, читають стан, виконують одну операцію, пишуть trace і йдуть. `.my` є lingua franca екосистеми (папка `ecosystem/`).

## 28. Canonical Internally, Permissive Externally

Агенти не зобов'язані мислити або генерувати нативні s-expressions на перших етапах. Ми підтримуємо 3 рівні взаємодії:
- **Level 0**: Агент мислить у YAML/JSON/Markdown та використовує `swarm` CLI-утиліти (adapters) для реєстрації задач, клеймів та хендофів. Для швидкого старту використовуй `agent-cheatsheet.my`.
- **Level 1**: Агент розуміє базовий `.my` (lists, symbols, strings) як data-only формат для координації (ніякого `eval`, closures чи макросів).
- **Level 2**: Agent-native. Агент використовує `my-lisp` reasoning engine (query, explain, reason) для автоматичної валідації та побудови доказів.

Зараз система перебуває у Phase 1: файли координації мають бути strictly data-only S-expressions.
