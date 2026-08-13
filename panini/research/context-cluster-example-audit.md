# Context cluster audit: adhikāra, anuvṛtti, asiddha

Status: `PANINI-CONTEXT-CLUSTER-EXAMPLE-AUDIT`. This compares concrete
evidence already used by the project. It rejects a premature single “context
primitive” and does not modify `panini/machine/`.

## [PANINI]

The three labels address different textual/grammatical questions:

| Mechanism | Evidence-backed question | Concrete project evidence |
| --- | --- | --- |
| adhikāra | Which governing content has a documented span and endpoint? | `bhUte` 3.2.84; `striyAm` 4.1.3; documented endpoints/restrictions |
| anuvṛtti | Which particular prior item is carried into a later sūtra? | inherited items and their source sūtras require commentary-facing evidence |
| asiddha | Which effect is treated as visible for a later rule check? | 8.2.1 `pUrvatrAsidDam` and qualified Tripādī readings |

The terms may interact in a derivation, but this evidence does not establish
that they are one mechanism or that one common scope boundary governs all three.

## [INTERPRETATION]

The current example portfolio shows uneven but useful coverage:

| Example | adhikāra / scope | anuvṛtti | asiddha / visibility |
| --- | --- | --- | --- |
| `Bavati` | 3.1.68 is used inside a broader interpreted rule context; exact inherited conditions remain partial | not yet enumerated per rule | not applicable in the bounded path |
| `dadAti` | same early derivational region; source path remains partial | not yet enumerated per rule | not applicable; the existing conflict harness is not Tripādī |
| `bhAvayati` candidate | 3.1.26 and later derivational stages expose a possible nested/secondary-root question | requires future source trace | not established |
| Tripādī audit | scope concerns a later grammar region | may coexist with scope records | explicit but relation-specific visibility question |

The dynamic-binding implementation is therefore an engineering convenience,
not a faithful proof that anuvṛtti or adhikāra is a runtime stack. Similarly,
the `visibility_relation` schema is deliberately an observer/observed pair,
not a universal inheritance edge.

## [MY-LISP HYPOTHESIS]

### Result: a typed context envelope, not a unified primitive

If a machine fixture needs common transport for contextual evidence, it may use
an envelope with *separate* relation kinds:

```yaml
context_evidence:
  - kind: governing-scope
    source_sutra: "3.2.84"
    carried_item: BUte
    endpoint: "3.2.123"
    provenance: [prov:<id>]
  - kind: textual-inheritance
    source_sutra: "<id>"
    target_sutra: "<id>"
    carried_item: <SLP1 item>
    provenance: [prov:<id>]
  - kind: rule-effect-visibility
    observer_rule: rule:<id>
    observed_rule: rule:<id>
    relation: siddha | asiddha | qualified | unresolved
    provenance: [prov:<id>]
```

This envelope is `machine:` data vocabulary. It does not assert that Pāṇini
has a supercategory called `context`, does not replace the specialised
`visibility_relation` contract, and must not be exposed as a My Lisp primitive.

### Invariants

1. `governing-scope` requires scope/evidence and an endpoint or an explicit
   unknown endpoint; it cannot imply a visibility decision.
2. `textual-inheritance` identifies a carried item and source/target rules; it
   cannot be inferred by lexical execution order.
3. `rule-effect-visibility` identifies observer and observed rule effects; it
   cannot be inferred from a scope span or an inherited word.
4. A fixture may say `not-applicable` for a kind. It must not create empty
   records merely to satisfy a uniform schema.
5. The `bhAvayati` question whether a secondary form proceeds recursively is a
   separate derivational-structure hypothesis, not evidence that any of the
   three kinds above is recursive scope.

### Portfolio consequence

The next complete-or-partial fixtures should add context records only where the
specific example needs them. `Bavati` and `dadAti` must explicitly record
`visibility: not-applicable` for their bounded early paths. A future Tripādī
fixture must include at least one `unresolved` relation. A causative fixture is
a candidate for testing derivational-stage identity, not for proving a general
context model.

## English summary

Adhikāra, anuvṛtti, and asiddha answer different questions: governing span,
carried textual item, and visibility of a rule effect. A typed machine envelope
may hold their evidence, but no unified context primitive is justified yet.

## Українська

Adhikāra, anuvṛtti та asiddha відповідають на різні питання: governing span,
успадкований текстовий елемент і visibility ефекту правила. Типізований
machine envelope може переносити їхній доказ, але єдиний context primitive
поки не обґрунтований.

Нормативно: `Bavati` і `dadAti` не отримують штучний `asiddha`; для їхніх
обмежених ранніх шляхів visibility є `not-applicable`. Tripādī fixture мусить
мати relation-specific provenance й чесний `unresolved`, якщо її бракує.
Adhikāra scope не доводить anuvṛtti, anuvṛtti не доводить visibility, а
visibility не є conflict priority. Усі три лишаються окремими machine relation
kinds до появи корпусу прикладів, що обґрунтує сильніше узагальнення.

## Deutsch

Adhikāra, anuvṛtti und asiddha beantworten unterschiedliche Fragen:
geltender Bereich, übertragener Textbestandteil und Sichtbarkeit eines
Regeleffekts. Ein typisierter Machine-Envelope darf ihre Evidenz tragen, doch
ein einheitliches Context-Primitive ist noch nicht begründet.
