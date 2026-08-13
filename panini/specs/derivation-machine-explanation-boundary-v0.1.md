# Derivation Machine explanation boundary v0.1

Status: `proposed`. Contract for `PANINI-MACHINE-EXPLANATION-BOUNDARY`.

## English — reference translation

### Purpose

This contract says what the derivation machine can explain, what it is required
to explain, and what remains outside its explanation boundary. It changes
neither the rule engine nor the state model; it makes the existing evidence,
trace, and philosophy boundaries testable together.

A machine explanation is a **falsifiable claim whose support the machine can
exhibit**. It is a state fact, transition fact, decision fact, provenance link,
or verification label — never an unsupported assertion about historical intent.
Claims without exhibited support are labelled `interpretation` or `needs-check`.

### [PANINI]

The machine does not explain why a rule is historically correct or what Pāṇini
intended. Such claims belong to source records and commentarial traditions. The
boundary limits machine-level output; it does not limit knowledge of the
Aṣṭādhyāyī.

### [INTERPRETATION]

Inside the boundary are reproducible state bytes and digests; a `before → rule
→ operation → after` transition with provenance; candidate selection or
rejection policy; stable provenance links; and `verified`, `needs-check`,
`disputed`, or `derived` labels. Outside are historical intent, claims of a
complete traditional derivation, promotion of machine output to a Paninian fact,
and claims that a My Lisp runtime implements Panini.

`explains?` requires exhibited support. `well-labelled?` requires every
outside-boundary claim to be marked `interpretation` or `needs-check` rather
than `derived`. `trace-consistent?` requires transition endpoints, rule,
provenance, all conflict candidates, and a digest or explicitly unhashed
fixture state; `validate_trace_fixtures.py` checks these structural invariants.

### [MY-LISP HYPOTHESIS]

The limited hypothesis is that explanation is a typed bundle of references,
not prose: state, transition, decision, provenance, and verification. This
does not define a runtime API. If an `explain` primitive is ever proposed, it
must return inspectable references rather than natural-language authority.

### Acceptance criteria

1. A trace never calls a machine policy a Paninian fact without a separate
   source record.
2. Every fixture transition supplies `before`, `after`, `rule`, and
   `provenance`; every state supplies a digest or explicit unhashed status.
3. At least one fixture demonstrates `needs-check` as an honest outcome.
4. The current validator requires no speculative scheduler or runtime feature.

## Українська — нормативна

### Призначення

Цей контракт визначає, що саме derivation machine може й зобов'язана пояснити,
а що лишається поза її межею пояснення. Він не змінює rule engine чи модель
стану; натомість робить уже наявні межі evidence, trace і philosophy спільно
перевірюваними.

Машинне пояснення — це **фальсифіковане твердження, підтримку якого машина може
показати**. Воно є фактом стану, переходу, рішення, provenance-посиланням або
verification-ярликом, але не непідтвердженим твердженням про історичний намір.
Твердження без показаної підтримки маркуються `interpretation` або
`needs-check`.

### [PANINI]

Машина не пояснює, чому правило історично правильне або що мав на увазі Pāṇini.
Такі твердження належать джерельним записам і коментаторським традиціям. Межа
обмежує machine-level вивід, а не знання про Aṣṭādhyāyī.

### [INTERPRETATION]

У межі входять: відтворювані bytes і digest стану; перехід `before → rule →
operation → after` з provenance; policy вибору або відхилення кандидатів;
стабільні provenance-посилання; ярлики `verified`, `needs-check`, `disputed`
та `derived`. Поза межею лишаються історичний намір, твердження про повну
традиційну деривацію, перетворення машинного виводу на факт Паніні та твердження,
що runtime My Lisp реалізує Паніні.

`explains?` вимагає показаної підтримки. `well-labelled?` вимагає, щоб кожне
поза-межове твердження мало `interpretation` або `needs-check`, а не `derived`.
`trace-consistent?` вимагає endpoints переходу, rule, provenance, усіх
кандидатів конфлікту й digest або явно не-хешований fixture-стан;
`validate_trace_fixtures.py` перевіряє ці структурні інваріанти.

### [MY-LISP HYPOTHESIS]

Обмежена гіпотеза: пояснення — це типізований набір посилань, а не проза:
state, transition, decision, provenance і verification. Це не визначає runtime
API. Якщо колись запропонують primitive `explain`, він має повертати оглядові
посилання, а не природномовний авторитет.

### Критерії прийняття

1. Trace не називає machine policy фактом Паніні без окремого джерельного
   запису.
2. Кожен fixture-перехід має `before`, `after`, `rule` і `provenance`; кожен
   стан має digest або явно не-хешований статус.
3. Принаймні один fixture показує `needs-check` як чесний результат.
4. Поточний валідатор не потребує спекулятивного scheduler чи runtime-feature.

## Deutsch — Referenzübersetzung

### Zweck

Dieser Vertrag legt fest, was die Derivationsmaschine erklären kann und muss
und was außerhalb ihrer Erklärungsgrenze bleibt. Er ändert weder Rule Engine
noch Zustandsmodell, sondern macht die vorhandenen Grenzen für Evidence, Trace
und Philosophie gemeinsam prüfbar.

Eine maschinelle Erklärung ist eine **falsifizierbare Behauptung, deren Stütze
die Maschine vorzeigen kann**. Sie ist Zustands-, Übergangs- oder
Entscheidungsfakt, Provenance-Verweis oder Verification-Label, niemals eine
unbelegte Aussage über historische Absicht. Behauptungen ohne vorzeigbare
Stütze werden `interpretation` oder `needs-check` markiert.

### [PANINI]

Die Maschine erklärt weder die historische Richtigkeit einer Regel noch die
Absicht Pāṇinis. Das gehört zu Quellen und Kommentierungstraditionen. Die
Grenze beschränkt maschinellen Output, nicht das Wissen über die Aṣṭādhyāyī.

### [INTERPRETATION]

Innerhalb der Grenze liegen reproduzierbare Zustandsbytes und Digests, ein
Übergang `before → rule → operation → after` mit Provenance, Kandidatenpolitik,
stabile Provenance-Verweise und die Labels `verified`, `needs-check`,
`disputed`, `derived`. Außerhalb liegen historische Absicht, Vollständigkeit
traditioneller Derivation, die Erhebung maschinellen Outputs zu Panini-Fakten
und Behauptungen, eine My-Lisp-Runtime implementiere Panini.

`explains?` verlangt gezeigte Stütze; `well-labelled?` verlangt
`interpretation` oder `needs-check` für jede äußere Behauptung;
`trace-consistent?` verlangt Übergangsenden, Regel, Provenance, alle
Konfliktkandidaten und Digest oder explizit ungehashten Fixture-Zustand.

### [MY-LISP HYPOTHESIS] und Abnahme

Die begrenzte Hypothese lautet: Erklärung ist ein typisiertes Bündel von
Verweisen, nicht Prosa. Ein mögliches `explain` würde überprüfbare Verweise
zurückgeben. Kein Trace darf Maschinenpolitik ohne Quelle als Panini-Fakt
ausgeben; jeder Fixture-Übergang benötigt vollständige Referenzen; mindestens
ein Fixture zeigt ehrlich `needs-check`; der Validator verlangt keinen
spekulativen Scheduler oder Runtime-Mechanismus.

## Related

- `specs/philosophy-control-layer-v0.1.md`
- `specs/trace-evidence-model-v0.1.md`
- `specs/derivation-ir-trace-events-v0.1.md`
- `specs/trace-canonical-serialization-v0.1.md`
- `research/machine-foundation-reconciliation.md`
- `research/derivation-machine-evidence-gate-review.md`
