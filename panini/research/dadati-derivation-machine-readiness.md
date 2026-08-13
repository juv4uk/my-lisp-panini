# dadāti: Derivation Machine v0.1 readiness audit

Status: `PANINI-DERIVATION-MACHINE-EXAMPLE-02-DADATI-CONFLICT`. This is a
source-and-machine boundary audit for a future end-to-end fixture. It does not
execute the My Lisp model or certify a complete historical derivation.

## [PANINI]

The registered root `dA` is a gaṇa-3 (`juhotyAdi`) dhātu. The existing example
uses 3.2.123, 3.4.78, 3.1.68, 2.4.75, 6.1.10, 6.1.4, and 7.4.59. The textual
identity of 2.4.72 (`adiprabhRtibhyaH SapaH`) and 2.4.75
(`juhotyAdibhyaH SluH`) is independently available in the digital
Aṣṭādhyāyī index and commentary-facing sources.

The source presentation for 2.4.72 includes `luk` through anuvṛtti and
describes it for the `adAdi` class. It must not be rewritten as a direct rule
for the `juhotyAdi` root `dA`. Rule 2.4.75 is the relevant explicit `Slu`
rule for the latter class. This audit does not decide every traditional account
of their mutual relation.

## [INTERPRETATION]

The project’s existing machine fixture represents 2.4.72 and 2.4.75 as two
applicable machine candidates and declares 2.4.75 an exception of 2.4.72. That
is a useful **counterfactual conflict harness**: it proves that the IR can
separate candidates, a declared policy, and a transition. It is not yet a
source-complete account that both rules are applicable to `dA` under the same
Pāṇinian conditions.

This distinction corrects a risky wording in the teaching example, which says
2.4.72 “usually” deletes `Sap` for class 2 and then treats it as the general
alternative for class 3. The first part belongs to the `adAdi` reading; the
second needs a separate interpretive justification rather than an automatic
`apavAda > utsarga` claim.

## [MY-LISP HYPOTHESIS]

### Two complementary fixtures, not one conflated proof

| Fixture | Purpose | Permitted result |
| --- | --- | --- |
| `dadati-apavada-conflict-v0.1.yaml` | test a declared machine relation between two candidates | `partial` |
| `dadati-source-path-v0.1` (future) | model the source-backed `dA` path through 2.4.75, reduplication and hrasva | `partial` until every bridge is checked |

The first must retain the word `machine` in rule IDs, provenance, and decision
reason. The second must not manufacture a conflict event merely because the
IR supports one.

### Conservative source-path outline

```text
dA + laT → dA + tip → dA + Sap + ti
  → dA + Slu + ti (2.4.75, source-path candidate)
  → reduplication relation / abhyAsa candidate (6.1.10, 6.1.4)
  → da + dA + ti (7.4.59 candidate)
  → dadAti (surface observation)
```

This outline is not a complete trace. In particular, the transition from the
displayed `da + dA + ti` representation to `dadAti` needs a typed,
source-accounted operation rather than concatenation by presentation.

### Required unknowns and gates

```yaml
result: { status: partial }
unknowns:
  - complete-source-account-of-the-2.4.72-to-2.4.75-conflict-relation-for-dA
  - provenance-backed-Slu-to-reduplication-precondition
  - typed-state-operation-from-abhyasa-representation-to-surface-dadAti
  - portable-execution-and-provenance-trace-of-the-existing-machine-harness
```

1. The conflict fixture must remain `partial` and label 2.4.72/2.4.75 as
   `machine:` candidates unless a separate source review establishes their
   co-applicability for this case.
2. The source-path fixture needs immutable before/after states, explicit
   applicability checks, selected decisions, and a trace termination event.
3. `Slu`, reduplication and abhyāsa must be distinct records/relations; no
   display string may carry their unproven semantics implicitly.
4. No Tripādī visibility relation belongs to this early path unless a concrete
   rule pair and scope require it. The example must say `not-applicable`, not
   invent `asiddha`.
5. A final `dadAti` form is a `trace-observation` until transition evidence is
   sufficient; it is not retrospective proof of candidate priority.

### Why this advances the milestone

`dadAti` gives the portfolio both a useful *positive* machine conflict case
and a source-side boundary that blocks overclaiming. It exercises the question
“which alternatives exist and why did one win?” while preserving the stronger
answer “we do not yet know whether this exact source path is complete.”

Sources: [2.4.72 with anuvṛtti and commentarial explanation](https://ashtadhyayi.com/sutraani/2/4/72),
[2.4.72 in SanskritDictionary](https://sanskritdictionary.com/panini/2-4-72),
and [the Learn Sanskrit treatment of 2.4.72/2.4.75](https://www.learnsanskrit.org/static/pdf/vyakarana.pdf).

## English summary

The existing dadāti fixture is valid as a partial machine conflict harness, but
not as proof that 2.4.72 and 2.4.75 are source-co-applicable to `dA`. A
separate source path must preserve this unknown and avoid invented visibility.

## Українська

Наявний fixture `dadAti` є коректним як `partial` machine conflict harness,
але не як доказ того, що 2.4.72 і 2.4.75 джерельно одночасно застосовні до
`dA`. Окремий source path має зберегти цю невідомість і не вигадувати
visibility relation.

Нормативно: 2.4.72 з `luk` через anuvṛtti документується для `adAdi`, а
2.4.75 є явним `Slu`-правилом для `juhotyAdi`. Тому попередній машинний
`apavAda` trace цінний як експеримент структури конфлікту, але не може бути
переписаний як історичний доказ. Фінальна форма `dadAti` лишається
`trace-observation`, доки кожен перехід, включно з abhyAsa та surface
операцією, не має окремого provenance.

## Deutsch

Das vorhandene `dadAti`-Fixture ist als `partial` Machine-Konflikt-Harness
gültig, jedoch kein Beweis dafür, dass 2.4.72 und 2.4.75 quellenbasiert
gleichzeitig auf `dA` anwendbar sind. Ein getrennter Quellenpfad muss diese
Ungewissheit erhalten und darf keine Visibility-Relation erfinden.
