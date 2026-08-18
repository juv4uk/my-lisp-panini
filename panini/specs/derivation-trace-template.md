# Evidence trace template / Шаблон доказового trace / Evidenz-Trace-Vorlage

## English

### Purpose and boundary

This v0.1 template records a manually reviewable derivation trace. It is not a
VM format, does not prove a complete derivation, and does not turn a sequence
of notes into executable grammar. Each step separates source fact,
interpretation, and our state representation.

### Invariants

- A sūtra reference alone does not prove the operation summary.
- Inherited context must be `explicit`, `inferred`, or `unresolved`; inferred
  context is never presented as literal sūtra text.
- Every transformation is our representation and declares its representation
  status.
- Missing evidence produces `unresolved` or a `blocked` trace. Alternatives
  remain recorded instead of being erased by a final surface form.

## Українська

### Призначення й межа

Цей шаблон v0.1 фіксує ручний trace деривації, який можна перевірити. Це не
формат VM, не доказ повної деривації й не перетворення послідовності нотаток
на виконувану граматику. Кожен крок розділяє факт джерела, інтерпретацію та
наше представлення стану.

### Інваріанти

- Саме посилання на sūtra не доводить operation summary.
- Успадкований контекст мусить бути `explicit`, `inferred` або `unresolved`;
  inferred context не подається як буквальний текст sūtra.
- Кожна transformation є нашим представленням і оголошує свій
  representation status.
- Відсутній доказ породжує `unresolved` або trace `blocked`. Alternatives
  залишаються записаними, а не зникають через фінальну поверхневу форму.

## Deutsch

### Zweck und Grenze

Diese v0.1-Vorlage hält einen manuell prüfbaren Derivationstrace fest. Sie ist
kein VM-Format, beweist keine vollständige Derivation und macht aus einer
Notizfolge keine ausführbare Grammatik. Jeder Schritt trennt Quellenfakt,
Interpretation und unsere Zustandsrepräsentation.

### Invarianten

- Eine sūtra-Referenz allein beweist die Operationszusammenfassung nicht.
- Geerbter Kontext muss `explicit`, `inferred` oder `unresolved` sein;
  inferred Kontext wird nie als wörtlicher sūtra-Text dargestellt.
- Jede Transformation ist unsere Repräsentation und erklärt ihren
  Repräsentationsstatus.
- Fehlende Evidenz führt zu `unresolved` oder einem `blocked`-Trace.
  Alternativen bleiben verzeichnet und werden nicht durch eine Endform gelöscht.

## Shared v0.1 schema / Спільна схема v0.1 / Gemeinsames Schema v0.1

```yaml
trace_id: example-id
status: draft # draft | source-checked | disputed | blocked
goal:
  display_iast: "..."
  canonical_slp1: "..."
initial_terms:
  - term_id: root
    form_slp1: "..."
    asserted_categories:
      - designation: dhAtu
        source: {kind: dhatupatha, reference: "...", evidence_status: source-checked}
steps:
  - ordinal: 1
    operation_summary: "short human-readable assertion"
    input_state: "..." # our state notation, never a Pāṇini quotation
    source:
      kind: sutra # sutra | commentary | traditional-principle | implementation-convenience
      reference: "3.1.68"
      text_ref: "registry/sutras/index.yaml#sutras.3.1.68"
      evidence_status: corpus-checked
    inherited_context:
      - source: "..."
        status: explicit # explicit | inferred | unresolved
        note: "what is inherited and why"
    interpretation:
      claim: "how source is applied to this step"
      status: source-checked # source-checked | interpretation | disputed
    transformation:
      before: "..."
      after: "..."
      representation_status: my-lisp-hypothesis
    alternatives:
      - status: unresolved # rejected | unresolved
        reason: "rule, condition, or missing evidence"
    output_state: "..."
result:
  form_slp1: "..."
  display_iast: "..."
  confidence: partial # source-checked | partial | blocked
open_issues: ["..."]
```

## Pre-publication check / Перевірка перед публікацією / Prüfung vor Veröffentlichung

1. Every sūtra ID appears in the provenance registry.
2. Every form change has SLP1 `before` and `after` values.
3. Every implicit `anuvftti` or `aDikAra` context is labelled `inferred` or
   `unresolved`.
4. Rejected alternatives and conflicts remain in `alternatives`.
5. A final form never substitutes for evidence of its path.

Related: [rule provenance](rule-provenance-schema.md),
[anuvṛtti boundary](../sastra/anuvrtti.md), and
[derivation-example verification](../research/derivation-examples-verification.md).
