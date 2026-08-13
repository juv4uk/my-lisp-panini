# Derivation machine explanation boundary v0.1

Status: `proposed`. Contract for `PANINI-MACHINE-EXPLANATION-BOUNDARY`.
Створено: 2026-08-13, my-lisp-panini-1.

## Purpose

Цей контракт фіксує, **що саме derivation machine може пояснити** (і що
зобов'язана пояснити), і **що знаходиться поза її межею пояснення**. Він не
змінює rule engine і не додає нові стани чи примітиви: він закріплює вже
наявні межі (`philosophy-control-layer-v0.1.md`,
`trace-evidence-model-v0.1.md`, `derivation-ir-trace-events-v0.1.md`,
`trace-canonical-serialization-v0.1.md`) як один явний, перевірюваний contract.

## English

A machine explanation is a **falsifiable statement whose support the machine
can exhibit**. Every such statement is either a state fact, a transition fact,
a decision fact, or a provenance link — never an unsupported assertion about
historical intent. Anything the machine cannot exhibit support for is outside
the boundary and must be labelled `interpretation` or `needs-check`, not
presented as derived output.

## [PANINI]

Машина не пояснює, чому правило історично правильне чи що мало на увазі
Pāṇini. Такі твердження належать джерельним записам і коментаторським
традиціям. Межа пояснення — це межа machine-level виводу, а не межа знання
про Аṣṭādhyāyī.

## [INTERPRETATION]

### Що всередині межі (machine-explainable)

1. **State facts.** Стан — це terms + relations + schema. Пояснення = навести
   canonical bytes і digest (`state:sha256:<hex>`), які незалежно
   відтворюються. Це вже визначено в `trace-canonical-serialization-v0.1.md`.
2. **Transition facts.** Зміна `before → after` під дією правила, з
   canonical rule id та хоча б одним `provenance`. Пояснення = назвати
   операцію й правило; цього достатньо, щоб крок був перевірюваний.
3. **Decision facts.** Чому кандидат обрано або відхилено: policy/reason у
   `explanation`, все відомі кандидати в `conflict`. Пояснення = policy
   застосування (наприклад, declared apavāda), а не історична перевага.
4. **Provenance links.** Кожен крок посилається на `ProvRecord`; ніколи не
   дублює джерельний текст. Пояснення = стабільне посилання.
5. **Verification labels.** Кожен крок несе `verified | needs-check |
   disputed | derived`. Це частина пояснення: воно явно каже, що саме
   перевірено, а що лише виведено.

### Що поза межею (not machine-explainable)

1. **Історичний намір.** «Правило застосовне тому, що Pāṇini мав на увазі X».
2. **Повнота традиції.** «Це повна деривація слова в традиції» — без
   повного portfolio доказів і згод.
3. **Перенесення статусу.** Машинний вивід (навіть з `verified`) не стає
   панінійським фактом без окремого джерельного запису.
4. **Схвалення runtime.** Будь-яке твердження про те, що my-lisp runtime
   «реалізує» механізм Паніні, — поза межею; дозволене лише
   `my-lisp-hypothesis` з операційним гейтом.

### Предикати

- `explains? (claim)`: машина може показати підтримку (state bytes+digest,
  rule id, provenance, verification). Інакше — `outside-boundary`.
- `well-labelled? (claim)`: кожне поза-межове твердження має label
  `interpretation` або `needs-check`; жодне не позначено як `derived`.
- `trace-consistent? (trace)`: кожен `transition` має `before`/`after`/`rule`/
  `provenance`; кожен `conflict` має всі кандидати; кожен стан має digest.
  Це перевіряється валідатором (`validate_trace_fixtures.py`).

### Застосування до наявних артефактів

- `tests.my::test-trace-canonical-serialization` пояснює digest як state fact —
  всередині межі (перевірюється `(sha256-hex ...)`).
- `tests.my::test-dadati-declared-conflict` пояснює, чому обрано 2.4.75:
  policy = declared apavāda, provenance = machine fixture. Твердження про
  історичну достатність залишається `needs-check` — поза межею, але явно
  позначене.
- Трасування `state-observed` / `trace-terminated` з `outcome` у
  `canonical-empty-state-v0.1.yaml` — state/termination facts, у межах.

## [MY-LISP HYPOTHESIS]

Для My Lisp contract є один висновок: **explanation — це не текст, а набір
посилань**. Пояснення має бути: (1) falsifiable, (2) exhibitable (машина
може показати всі складові), (3) типізоване за рівнем (`state`/`transition`/
`decision`/`provenance`/`verification`). Це не визначає новий runtime-API.
Якщо колись з'явиться `explain` примітив, він мусить повертати посилання, а
не природномовний текст.

## Acceptance criteria

1. Новий або змінений trace не називає machine policy панінійським фактом
   без окремого джерельного запису.
2. Кожен `transition` у fixtures має `before`, `after`, `rule`, `provenance`;
   кожен стан має digest або явний `fixture-sexpr-not-hashed`.
3. Валідатор не потребує змін для цього контракту (усі правила вже існують).
4. Принаймні один тест показує `needs-check` як чесний поза-межевий ярлик.

## Related

- specs/philosophy-control-layer-v0.1.md (epistemic layer vs operational gate)
- specs/trace-evidence-model-v0.1.md (event invariants)
- specs/derivation-ir-trace-events-v0.1.md (envelope)
- specs/trace-canonical-serialization-v0.1.md (state bytes/digest)
- research/machine-foundation-reconciliation.md (three-level boundary)
- research/derivation-machine-evidence-gate-review.md (status vocabulary)
