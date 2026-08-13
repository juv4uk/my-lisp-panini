# Tripādī visibility relation v0.1

Status: foundation-level schema for
`PANINI-TRIPADI-VISIBILITY-RELATION-SCHEMA`. It operationalizes the bounded
conclusion of `research/tripadi-rule-exception-audit.md`; it authorizes no
parser, evaluator, scheduler, or registry change.

## [PANINI]

`pUrvatrAsidDam` (8.2.1) is a textual anchor for an `asiddha` mechanism in the
Tripādī. This specification does not claim that its fields, direction, or
enumerated values occur as such in the Aṣṭādhyāyī. In particular, it does not
reduce `asiddha` to deletion of an earlier operation or to a universal numeric
execution order.

## [INTERPRETATION]

The project audit records that commentarial presentations constrain a simple
reading: same-`prakaraRa` relations and other exceptions may matter. A machine
model therefore needs to ask a visibility question for an ordered pair of rule
applications, independently of candidate selection.

Visibility answers: “which prior effect may this check see?” Conflict policy
answers: “which simultaneously applicable candidate is selected?” Neither
question entails the other.

## [MY-LISP HYPOTHESIS]

### Record shape

```yaml
id: visibility:<stable-key>
observer:
  rule: rule:<stable-id>
  phase: applicability | operation | postcondition
observed:
  rule: rule:<stable-id>
  transition: evt:<ordinal>|transition:<stable-id>|null
scope:
  kind: tripadi | same-prakarana | cross-section | explicit-exception | unknown
  id: <stable scope ID>|null
relation: siddha | asiddha | qualified | unresolved
direction: observer-cannot-see-observed | observer-can-see-observed | conditional | unknown
conditions: [condition:<stable-id>]
provenance: [prov:<stable-id>]
evidence_status: verified | needs-check | disputed | derived
machine_policy: allow | restrict | block
notes: <non-normative explanation>
```

`observer.rule` and `observed.rule` must be distinct stable IDs. `transition`
identifies a concrete prior effect when one is known; `null` is permitted only
for a relation stated at rule-pair level. `scope.kind: same-prakarana` requires
`scope.id`; a prose label is insufficient.

### Invariants

1. `relation: asiddha` requires
   `direction: observer-cannot-see-observed`. It does **not** erase the stored
   state or the append-only trace.
2. `relation: siddha` requires
   `direction: observer-can-see-observed`.
3. `qualified` requires at least one explicit condition and cannot use
   `machine_policy: allow` without an implementation-policy provenance record.
4. `unresolved` requires `machine_policy: block`; numeric sūtra order is not a
   permitted default that upgrades it to `siddha` or `asiddha`.
5. A record with `basis` only in commentary or project policy must keep its
   provenance layer visible. It cannot be serialized as direct sūtra text.
6. A scheduler may consume an `allow` or `restrict` record only after the
   foundation gate for its referenced machine rule has passed. Until then this
   schema is data-only.
7. Visibility evidence and conflict evidence have different IDs. A
   `conflict-resolved` trace event cannot satisfy the provenance requirement
   for a visibility relation.

### Decision procedure for a future scheduler

```text
find(observer-rule, observed-rule, phase, scope)
  -> no record or unresolved: emit visibility-unresolved; block/partial
  -> asiddha: expose a view without the observed effect; retain full trace
  -> siddha: expose the prior effect
  -> qualified: evaluate declared conditions, then emit the selected view

only afterwards: evaluate candidate conflict policy, if candidates conflict
```

The “view” is a machine-local projection for a particular check. It must have
a stable trace reference and must not overwrite the derivation state.

### Minimal fixtures

```yaml
# A generic Tripādī relation, deliberately not executable.
id: visibility:tripadi:example-unresolved
observer: { rule: "rule:sutra:8.3.example", phase: applicability }
observed: { rule: "rule:sutra:8.2.example", transition: null }
scope: { kind: tripadi, id: "scope:tripadi" }
relation: unresolved
direction: unknown
conditions: []
provenance: [prov:commentary:tripadi-boundary]
evidence_status: needs-check
machine_policy: block
```

```yaml
# A same-prakaraṇa case must name its boundary and must not inherit a generic
# Tripādī result automatically.
id: visibility:same-prakarana:example
observer: { rule: "rule:sutra:8.3.example-b", phase: applicability }
observed: { rule: "rule:sutra:8.3.example-a", transition: "evt:12" }
scope: { kind: same-prakarana, id: "scope:prakaranam:example" }
relation: qualified
direction: conditional
conditions: [condition:scope-membership]
provenance: [prov:interpretation:same-prakarana-visibility]
evidence_status: needs-check
machine_policy: block
```

### Acceptance gates

1. A validator rejects an `asiddha` record without the required direction.
2. A validator rejects `same-prakarana` without `scope.id`.
3. An executable prototype includes one `unresolved` fixture that ends as
   `partial` or `blocked`, never silently as success.
4. An executable prototype separately emits a visibility event and a conflict
   event when both questions arise.
5. Machine integration requires a reviewed source/interpretation audit for
   each relation family it implements.

## English summary

`VisibilityRelation` records what a particular rule check may see of an
earlier rule effect. It is provenance-bearing, directional, conditional when
necessary, and deliberately separate from conflict priority. Unknown
relations block completion rather than falling back to numeric order.

## Українська

`VisibilityRelation` фіксує, який ефект попереднього правила може бачити
конкретна перевірка іншого правила. Це provenance-зв’язок із напрямком та,
коли потрібно, умовами; він навмисно відокремлений від пріоритету конфлікту.
Невідома relation блокує завершення derivation, а не підміняється числовим
порядком sūtra.

Нормативно: `asiddha` обмежує видимість для заданого check, але не знищує
історію станів і не видаляє trace. `same-prakaraRa` не є автоматичною
підставою для жодного результату: він потребує окремої ідентифікованої межі,
джерела та policy record. Лише після визначення visibility scheduler може
окремо розглядати конфлікт кандидатів.

## Deutsch

`VisibilityRelation` hält fest, welchen Effekt einer früheren Regel eine
bestimmte Regelprüfung sehen darf. Die Relation ist provenienzgebunden,
gerichtet und bei Bedarf bedingt; sie ist absichtlich von Konfliktpriorität
getrennt. Unbekannte Relationen blockieren den Abschluss einer Derivation,
statt auf numerische Sūtra-Reihenfolge zurückzufallen.
