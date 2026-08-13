# Philosophy control layer v0.1

Status: design contract for `PANINI-PHILOSOPHY-CONTROL-LAYER-DESIGN`.
It governs the admission and labelling of claims used by the project. It is
not a reconstruction of a Pāṇinian mechanism, a rule executor, or permission
to change the My Lisp runtime.

## [PANINI]

The Aṣṭādhyāyī, its associated lexical material, and its commentarial
traditions must not be silently collapsed into a modern software model. A
project record can cite a sūtra, but a machine consequence inferred from that
record remains a distinct claim. Likewise, a useful computational analogy does
not become an ancient category merely because it is convenient.

Therefore this layer makes no claims of the form “Pāṇini executes this control
layer”. Its purpose is methodological: preserve the difference between what a
source says, how it is interpreted, and what My Lisp may test.

## [INTERPRETATION]

The layer is a small, auditable decision procedure over `ProvenanceRecord`
objects from `provenance-type-schema-v0.1.md`. It may check whether the support
and classification required for a proposed use are present. It must not infer
new historical facts, choose a grammatical rule during derivation, or promote
an implementation result to textual evidence.

Two dimensions remain independent:

| Dimension | Question | Examples |
| --- | --- | --- |
| epistemic layer | What kind of claim is this? | `panini`, `interpretation`, `my-lisp-hypothesis` |
| operational gate | What is it permitted to do now? | cite, document, prototype, execute, release |

An admissible hypothesis may be used by a bounded experiment while remaining
inadmissible as a claim about Pāṇini. A verified sūtra citation may support
documentation while still being insufficient to authorize a machine rule.

## [MY-LISP HYPOTHESIS]

### Control decision record

```yaml
id: control:<stable-key>
request: cite | classify | admit-machine-experiment | admit-machine-rule | release
subject: <stable subject ID>
provenance: [prov:<id>]
classification:
  layer: panini | interpretation | my-lisp-hypothesis
  claim_kind: source-text | lexical-record | interpretation | implementation | hypothesis
  confidence: high | medium | low | unresolved
checks:
  provenance: pass | fail | unresolved
  layer-consistency: pass | fail
  anachronism: pass | fail | review-required
  falsifier: present | not-applicable | missing
  foundation-gate: pass | fail | not-applicable
decision: allow | allow-as-hypothesis | block | escalate
reason: <short, inspectable explanation>
review:
  status: draft | reviewed | superseded | rejected
  reviewed_on: YYYY-MM-DD
```

`provenance` is mandatory and points to stable provenance records; the control
record does not duplicate or replace their evidence. `falsifier` is required
for a machine experiment or rule proposal: it names a test, counterexample, or
condition that could disconfirm the operational hypothesis. It is
`not-applicable` only for a narrow citation/classification request.

### Admission policy

1. Classify the proposed statement before discussing machine use.
2. Require a matching provenance record and inspectable locator for every
   citation. A missing locator yields `block` or `escalate`.
3. Run the anachronism check whenever a Pāṇinian term is compared with a modern
   type, tag, compiler, graph, or VM construct. The result must state
   `my-lisp-hypothesis`, not identity, unless direct textual evidence supports
   the narrower statement.
4. A source-text claim may be cited only as source text. It does not by itself
   permit a machine rule.
5. An interpretation may inform a bounded experiment, but its resulting trace
   is implementation evidence, not verification of the interpretation.
6. A machine rule requires a passed foundation gate, explicit operational
   semantics, a falsifier, and a traceable test. Otherwise the decision is
   `block`.
7. Any disputed or unresolved premise must remain visible in the decision
   reason and cannot be upgraded by a later automation step.

### Boundary with derivation

The derivation engine owns such operations as matching a rule, evaluating an
applicability condition, ordering candidates, and recording a state transition.
The control layer may annotate a proposal as admitted, experimental, blocked,
or requiring review. It must never decide that a Pāṇinian sūtra applies solely
from the control record.

```text
ProvenanceRecord ──> control decision ──> allowed scope
                                        │
Derivation IR ──> rule matching ────────┼──> trace event
                                        │
                         no historical inference back from trace
```

This directionality prevents circular proof: a successful program trace may
validate conformance with an implementation contract, but cannot validate a
historical or philological assertion without independent source review.

### Examples

```yaml
id: control:it-metadata-analogy
request: admit-machine-experiment
subject: it
provenance: [prov:sutra:it-definition, prov:hypothesis:it-control-tag-analogy]
classification:
  layer: my-lisp-hypothesis
  claim_kind: hypothesis
  confidence: low
checks:
  provenance: pass
  layer-consistency: pass
  anachronism: pass
  falsifier: present
  foundation-gate: pass
decision: allow-as-hypothesis
reason: "May test an erased-control-marker model; it does not identify it with compiler metadata."
review: { status: draft, reviewed_on: "2026-08-13" }
```

```yaml
id: control:semantic-call-runtime
request: admit-machine-rule
subject: machine:semantic-call
provenance: [prov:machine:semantic-call-contract]
classification:
  layer: my-lisp-hypothesis
  claim_kind: implementation
  confidence: unresolved
checks:
  provenance: unresolved
  layer-consistency: pass
  anachronism: review-required
  falsifier: missing
  foundation-gate: fail
decision: block
reason: "The foundation gate and an executable falsifier are absent."
review: { status: draft, reviewed_on: "2026-08-13" }
```

## English summary

The control layer is an auditable claim-admission gate, not a Pāṇinian rule
engine. It keeps source, interpretation, and My Lisp hypotheses distinct;
requires provenance, anachronism checks, and falsifiers; and prevents a program
trace from becoming historical proof.

## Українська

Філософський control layer — це перевірюваний шлюз допуску тверджень, а не
двигун правил Паніні. Він зберігає відмінність між джерелом, інтерпретацією та
гіпотезою My Lisp; вимагає provenance, перевірки анахронізму й фальсифікатора;
та не дозволяє програмному trace перетворюватися на історичний доказ.

Нормативне правило для проєкту: жодна автоматизація не може підвищити статус
твердження. Лише незалежно перевірене джерело підтримує джерельне твердження,
а лише окремо пройдений foundation gate і відтворюваний тест дозволяють
машинний експеримент або правило. Позитивний результат такого тесту доводить
лише відповідність реалізації її контракту.

## Deutsch

Die philosophische Control-Schicht ist ein prüfbares Zulassungstor für
Behauptungen und keine Pāṇini-Regelmaschine. Sie trennt Quelle,
Interpretation und My-Lisp-Hypothese, verlangt Provenienz,
Anachronismusprüfung und Falsifikator und verhindert, dass ein Programm-Trace
zum historischen Beweis wird.
