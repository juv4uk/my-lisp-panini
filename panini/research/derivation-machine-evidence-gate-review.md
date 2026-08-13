# Derivation Machine v0.1: evidence-gate review

Status: `partial`. This review tests whether the written milestone gates can
currently prevent an unjustified `complete` claim. It does not upgrade any
fixture or derivation.

## English

The project has strong qualitative gates: source/machine separation,
first-class unknowns, explicit provenance, conflict/visibility requirements,
and a ban on undocumented fallbacks. The new trace-fixture validator enforces
a useful structural subset. But the gates are not yet a complete executable
acceptance contract: the trace envelope uses `trace_status: complete`, while
the Derivation IR result uses `status: success`; current fixtures use the
latter shape and neither publishes content-addressed state bytes. No validator
can yet decide the full milestone exit criteria.

## Українська

### [PANINI]

Цей review не є твердженням про Паніні. `evidence gate`, `complete`, `success`
і acceptance validator належать до machine/engineering рівня.

### [INTERPRETATION]

Письмові межі вже сильні: джерело відокремлено від machine, `unknown` не
маскується fallback-ом, provenance обов'язковий, а milestone вимагає реального
conflict та visibility або чесного `unresolved`. Новий validator перевіряє
structural підмножину: DAG подій, існування state, selected decision перед
transition, provenance і termination/result status.

Виявлено один blocker до автоматичного acceptance:

| Contract | Статуси успіху | Поточний наслідок |
| --- | --- | --- |
| Trace-event envelope | `complete | partial | omitted | invalid` | `complete` є trace-level словом |
| Derivation IR result | `success | partial | blocked | invalid` | `success` є result-level словом |
| Milestone exit criterion | «No result marked `complete`» | змішує обидва vocabulary |

Це не просто стилістика: validator не повинен сам вирішувати, чи `complete`
означає trace completeness, result success, чи виконання портфельного
milestone. Поки версіонований mapping не зафіксовано, automated gate може
лише відхиляти структурні помилки, але не видавати повний acceptance verdict.

Другий blocker — canonical state bytes і digest vectors ще не визначено;
поточні fixtures навмисно `fixture-sexpr-not-hashed`. Третій — портфель досі
не має трьох-п'яти independently reviewable end-to-end source paths.

### [MY-LISP HYPOTHESIS]

Для My Lisp тут є лише методологічний висновок: статус виконання повинен бути
типізованим за рівнем (`trace`, `result`, `milestone`) і мати provenance.
Не можна робити один boolean `complete` для факту, доказу, виконання та
портфельної готовності. Це не визначає runtime API чи primitive My Lisp.

## Рішення

Milestone лишається `partial`. Перед будь-яким automated `complete` потрібні:

1. окремий versioned status mapping або перейменування одного vocabulary;
2. canonical serialization contract і test vectors;
3. machine-checkable portfolio manifest із посиланнями на 3–5 traces;
4. окремі evidence records для genuine conflict і visibility/unresolved;
5. review, який показує вісім відповідей `why?` для кожного transition.

## Post-fix status / Стан після фіксів / Stand nach den Fixes

**2026-08-14 (my-lisp-panini-1).** Reviewed against current master after the
trace-format and derivation work. Blocker status:

| Blocker | Стан | Де закрито |
| --- | --- | --- |
| 1. status mapping (trace vs result) | закрито | `specs/trace-canonical-serialization-v0.1.md` (trace_status vs result.status, versioned) |
| 2. canonical serialization + test vectors | закрито | `specs/trace-canonical-serialization-v0.1.md` + vectors A/B + `canonical-empty-state-v0.1.yaml` |
| 3. portfolio manifest (3–5 traces) | закрито | `tests/trace-fixtures/portfolio-manifest-v0.1.yaml` (6 reviewable fixtures, gate result partial) |
| 4. evidence records: conflict + visibility | закрито | `dadati-apavada-conflict-v0.1.yaml`, `tripadi-unresolved-visibility-v0.1.yaml` |
| 5. why?-review (8 відповідей на transition) | відкрито | наступний крок, окрема review |

`python3 panini/tests/test_trace_fixture_validator.py` → trace fixture validator
negative fixtures: PASS. Усі fixtures лишаються `partial` (крім canonical-empty
state-vector), тож automated `complete`-verdict досі заборонений; milestone
залишається `partial`, але всі п'ять документованих блокерів, крім why?-review,
мають закриваючі артефакти.

## Deutsch

Die qualitativen Gates sind stark, aber noch kein vollständiger ausführbarer
Acceptance-Contract. Insbesondere verwendet der Trace-Umschlag `complete`,
das Derivation-IR-Ergebnis jedoch `success`, während das Milestone-Dokument
beide Vokabulare vermischt. Zusätzlich fehlen canonical state bytes und drei
bis fünf vollständig überprüfbare End-to-End-Pfade. Daher bleibt der
Milestone `partial`; ein Validator darf derzeit nur Strukturfehler ablehnen,
aber keinen vollständigen Acceptance-Verdict erteilen.
