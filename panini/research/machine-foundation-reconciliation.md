# Machine / foundation reconciliation

## English

### Purpose and boundary

This read-only reconciliation compares the committed Panini-machine model with
the completed `panini-foundation-v0.1` materials. It does not change machine
code, My Lisp, or the status of a historical claim.

### Findings on 2026-08-13

1. `rules.my` now contains a semantic bridge with `make-semantic-call`,
   `semantic-to-prakriya`, and `DHATU_DA` / `KARAKA_KARTR` identifiers.
2. The bridge is labelled as compatible with My Lisp `karaka.rs`, but the My
   Lisp migration materials state that parser transformation and evaluator
   semantics are P5 work and require the foundation gate review.
3. The bridge uses the three-part shorthand `(def name (parameters) ...)`.
   Independent WSL execution established that the current My Lisp runtime
   accepts two-part `(def name expression)` and rejects this shorthand.
4. `tests.my` still begins with a checkout-specific Windows loader path, so
   the new dadAti and kArayati assertions are not executable evidence in WSL.

### Reconciliation result

The model is a useful **machine-design experiment**, but it cannot currently
be described as either an executable My Lisp integration or an approved
representation of Pāṇini. It must be documented as `[MY-LISP HYPOTHESIS]`
until both independent gates pass:

- `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW`; and
- `PANINI-MACHINE-TEST-EXECUTION-COMPAT`.

### Required next handoff

The machine maintainer should either isolate the bridge as a non-executed
design fixture or, after the two gates, implement it against My Lisp's
confirmed parser/evaluator surface. The verification owner must then record a
real WSL/Guix command that loads the suite and reaches both derivation tests.
The durable dependent task is
`PANINI-MACHINE-SEMANTIC-BRIDGE-GATE-CORRECTION`.

## Українська

### Мета й межа

Це read-only звірка committed Panini-machine з завершеними матеріалами
`panini-foundation-v0.1`. Вона не змінює machine-код, My Lisp або статус
історичного твердження.

### Знахідки станом на 2026-08-13

1. У `rules.my` тепер є semantic bridge: `make-semantic-call`,
   `semantic-to-prakriya` та ідентифікатори `DHATU_DA` / `KARAKA_KARTR`.
2. Bridge позначено як сумісний з My Lisp `karaka.rs`, але матеріали міграції
   My Lisp відносять parser transform і evaluator semantics до P5, що потребує
   foundation gate review.
3. Bridge використовує тричастинний shorthand `(def name (parameters) ...)`.
   Незалежне виконання у WSL встановило: поточний My Lisp приймає двочастинний
   `(def name expression)` і відхиляє цей shorthand.
4. `tests.my` все ще починається з Windows loader path конкретного checkout,
   тому нові dadAti та kArayati assertions не є executable evidence у WSL.

### Результат звірки

Модель корисна як **експеримент машинного дизайну**, але нині її не можна
описувати ані як виконувану інтеграцію My Lisp, ані як затверджене представлення
Паніні. До проходження обох незалежних gate вона має бути позначена
`[MY-LISP HYPOTHESIS]`:

- `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW`; і
- `PANINI-MACHINE-TEST-EXECUTION-COMPAT`.

### Наступний handoff

Власник machine має або ізолювати bridge як невиконуваний design fixture, або
після двох gate реалізувати його за підтвердженою parser/evaluator-поверхнею
My Lisp. Власник верифікації після того фіксує реальну WSL/Guix команду, що
завантажує suite та доходить до обох derivation tests. Створена durable задача:
`PANINI-MACHINE-SEMANTIC-BRIDGE-GATE-CORRECTION`.

## Deutsch

### Zweck und Grenze

Dieser Read-only-Abgleich vergleicht das commitete Panini-Machine-Modell mit
`panini-foundation-v0.1`. Er ändert weder Machine-Code noch My Lisp oder den
Status einer historischen Behauptung.

### Befunde vom 2026-08-13

1. `rules.my` enthält nun `make-semantic-call`, `semantic-to-prakriya` sowie
   `DHATU_DA` / `KARAKA_KARTR`.
2. Die Bridge wird als kompatibel mit My Lisp `karaka.rs` bezeichnet; die
   My-Lisp-Migration ordnet Parser-Transformation und Evaluator-Semantik jedoch
   P5 nach dem Foundation-Gate zu.
3. Die Bridge nutzt `(def name (parameters) ...)`, obwohl das aktuelle My Lisp
   nur `(def name expression)` akzeptiert.
4. `tests.my` nutzt weiterhin einen checkout-spezifischen Windows-Laderpfad;
   daher sind dadAti- und kArayati-Assertions in WSL kein ausführbarer Beleg.

### Ergebnis

Das Modell ist ein nützliches **Machine-Design-Experiment**, derzeit aber
weder eine ausführbare My-Lisp-Integration noch eine bestätigte Pāṇini-
Repräsentation. Bis beide Gates bestanden sind, gehört es unter
`[MY-LISP HYPOTHESIS]`: `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW` und
`PANINI-MACHINE-TEST-EXECUTION-COMPAT`.

### Nächster Handoff

Der Machine-Verantwortliche soll die Bridge entweder als nicht ausführbare
Design-Fixture isolieren oder sie nach beiden Gates gegen die bestätigte
My-Lisp-Parser/Evaluator-Oberfläche implementieren. Danach muss eine echte
WSL/Guix-Ausführung beide Derivationstests erreichen. Die abhängige Aufgabe
heißt `PANINI-MACHINE-SEMANTIC-BRIDGE-GATE-CORRECTION`.
