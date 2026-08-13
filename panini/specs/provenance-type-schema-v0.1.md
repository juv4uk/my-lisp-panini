# Provenance type schema v0.1

Status: design contract for `PANINI-PROVENANCE-TYPE-SCHEMA-V0-1`. It extends,
but does not replace, `rule-provenance-schema.md` and the citation registry.
No runtime or registry migration is authorized by this document.

## [PANINI]

Pāṇini, a Dhātupāṭha record, later commentary, and a project inference are not
the same kind of assertion. The distinction is methodological: the schema is
not a Pāṇinian category, and its fields must never be represented as if they
were words of the Aṣṭādhyāyī.

## [INTERPRETATION]

The existing repository already separates sūtra text records, citation-check
status, commentary, traditional principles, implementation convenience, and
My Lisp hypotheses. The missing common contract is a machine-readable unit
that can point from any claim to its support without silently upgrading an
interpretation into a primary-text fact.

## [MY-LISP HYPOTHESIS]

### Canonical record

```yaml
id: prov:<namespace>:<stable-key>
claim_kind: source-text | lexical-record | interpretation | implementation | hypothesis
layer: panini | interpretation | my-lisp-hypothesis
subject:
  kind: sutra | dhatu | karaka | rule-field | derivation-step | semantic-id
  id: <canonical-SLP1-or-stable-source-ID>
assertion: <short, falsifiable claim>
evidence:
  - kind: sutra | dhatupatha | commentary | implementation | test | manual-review
    ref: <stable local path or external edition reference>
    locator: <sutra ID, record key, revision, line, or test name>
    status: verified | needs-check | disputed | derived
    checked_on: YYYY-MM-DD
derivation:
  method: direct | interpreted | implemented | inferred
  depends_on: [prov:<id>]
status: active | superseded | rejected
supersedes: []
notes: <non-normative explanation>
```

### Invariants

1. `id` is stable and never recycled; correction creates a new record linked
   through `supersedes`.
2. `subject.id` uses canonical SLP1 for Panini vocabulary. Internal IDs such as
   `DHATU_DA` belong in an implementation claim and must map explicitly to
   `dA`; they cannot replace it.
3. `layer`, `claim_kind`, and every `evidence.kind` must agree. A commentary
   cannot be the sole evidence for a `source-text` claim.
4. `verified` means the cited locator was checked, not that every derived
   machine behaviour is historically established.
5. `derived` evidence must name its upstream records in `depends_on`.
6. A disputed claim is retained with alternatives; it is never overwritten by
   an arbitrary single value.

### Examples

```yaml
id: prov:sutra:1.4.2-text
claim_kind: source-text
layer: panini
subject: { kind: sutra, id: "1.4.2" }
assertion: "Citation identifies vipratiSeDa paraM kAryam."
evidence:
  - { kind: sutra, ref: registry/sutras/index.yaml, locator: "1.4.2",
      status: verified, checked_on: "2026-08-13" }
derivation: { method: direct, depends_on: [] }
status: active
supersedes: []

id: prov:machine:dadati-apavada-choice
claim_kind: implementation
layer: my-lisp-hypothesis
subject: { kind: rule-field, id: "machine:2.4.75:utsarga" }
assertion: "The machine selects 2.4.75 over 2.4.72 through apavada-of?."
evidence:
  - { kind: implementation, ref: panini/machine/meta.my,
      locator: "apavada-of?", status: needs-check, checked_on: "2026-08-13" }
derivation:
  { method: implemented, depends_on: [prov:sutra:1.4.2-text] }
status: active
supersedes: []
```

The second record intentionally does **not** claim that the executable trace
has passed or that the complete priority hierarchy follows from 1.4.2.

## English summary

`ProvenanceRecord` is a proposal for one typed, stable record shape across
source claims, interpretations, implementation details, and hypotheses. It
preserves SLP1 identity, supports corrections and disputes, and makes every
machine-relevant claim point to independently inspectable evidence.

## Українська

`ProvenanceRecord` — пропозиція єдиної типізованої стабільної форми запису для
джерельних тверджень, інтерпретацій, деталей реалізації та гіпотез. Вона
зберігає SLP1-ідентичність, підтримує виправлення й суперечки та змушує кожне
машинно значуще твердження посилатися на незалежно перевірний доказ.

Ключове правило: schema не підміняє реєстри і не легітимізує P5 або machine
runtime. Це контракт для наступної міграції, яку треба окремо затвердити й
перевірити.

## Deutsch

`ProvenanceRecord` ist ein Vorschlag für eine einheitliche typisierte, stabile
Datensatzform für Quellenbehauptungen, Interpretationen, Implementierungs-
details und Hypothesen. Sie bewahrt die SLP1-Identität, unterstützt Korrekturen
und Streitfälle und verweist für jede maschinenrelevante Behauptung auf
unabhängig prüfbare Evidenz.

Die Schema ersetzt keine Register und legitimiert weder P5 noch eine
Machine-Runtime. Sie ist ein Vertrag für eine später ausdrücklich genehmigte
und geprüfte Migration.
