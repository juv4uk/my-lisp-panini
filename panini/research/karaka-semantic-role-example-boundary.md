# Kāraka and semantic-role boundary from examples

Status: `PANINI-KARAKA-SEMANTIC-ROLE-EXAMPLE-BOUNDARY`. This audit constrains
future machine representation. It does not choose an AST container or claim
that a modern semantic-role graph is Pāṇini’s own ontology.

## [PANINI]

The kāraka material applies general criteria within the `kArake` domain rather
than publishing a fixed valency table for every dhātu. The existing worked
examples demonstrate two different paths:

1. `dA` in a giving situation supports `kartf`, `karman`, and `sampradAna`
   through the situation and the general criteria.
2. `BI` with a fear source involves `apAdAna` through a rule-specific extension
   beyond the basic physical-separation criterion.

Counterexamples add essential constraints: passive voice separates `kartf`
from grammatical subject; causation distinguishes a causing participant from
a simple physical-doer gloss; and `karman` cannot be equated universally with
an affected “patient”. No cited evidence makes kāraka a predeclared list of
slots attached intrinsically to a dhātu.

## [INTERPRETATION]

A modern record such as `predicate → role → participant` is useful as a
question-shaped representation: it can preserve *which criterion classified
which participant for which described situation*. It becomes misleading if it
silently means any of the following:

- every dhātu owns a fixed role frame;
- each role is a single-valued map key;
- a kāraka is identical to a dependency edge;
- `kartf`, `karman`, `karaRa`, etc. are English agent/patient labels;
- the roles exhaust all semantic relations in an utterance.

The current simple `SemanticCall` profile is therefore a bounded implementation
profile for simple examples, not a Paninian semantic model.

## [MY-LISP HYPOTHESIS]

### Minimum admissible machine record

For a documented simple situation, the smallest neutral representation is a
provenance-bearing classification claim:

```yaml
participant_classification:
  situation: situation:<stable-id>
  participant: term:<stable-id>|entity:<machine-id>
  designation: kartf | karman | karaRa | sampradAna | apAdAna | aDikaraRa
  basis:
    kind: general-criterion | rule-specific-extension | machine-fixture
    ref: "1.4.<n>"|machine:<id>
  conditions: [condition:<stable-id>]
  provenance: [prov:<stable-id>]
  status: asserted | disputed | unresolved
```

`situation` is an analysis scope, not automatically a worldly event object.
`participant` may remain a derivational term for grammar-focused examples. An
`entity:<machine-id>` is optional and subject to the separate referent admission
rule; an English gloss cannot create it implicitly.

### Boundaries demonstrated by the portfolio

| Case | What is safe to record | What must remain open |
| --- | --- | --- |
| simple giving `dA` | three independent classification claims in one scoped situation | fixed valency of `dA` |
| `pac` with/without location | optional `aDikaraRa` claim when participant is present | mandatory location slot |
| fear `BI` | `apAdAna` claim with rule-specific provenance | generic Source equivalence |
| passive | `kartf` classification independently of surface subject | subject = actor rule |
| causative | multiple scoped claims and an explicit `unsupported`/nested-event boundary | one flat `agent` slot |

### Implementation gate

1. A simple map/record may validate a *single simple situation* only when its
   profile says so and each binding has provenance.
2. Duplicate roles, causation, nesting, alternative analyses, or unclear
   participant identity must return `unsupported`, `partial`, or `unresolved`;
   they must not overwrite a map entry.
3. A graph representation is permitted only as `machine:` analysis data with
   explicit node/edge semantics. It cannot be named “the Paninian graph”.
4. My Lisp integration remains gated by the Derivation Machine v0.1 portfolio;
   this audit authorizes no parser syntax or evaluator feature.

## English summary

Kāraka is best represented provisionally as evidence-bound participant
classification in a scoped situation. The examples reject fixed dhātu frames,
universal graph edges, and direct agent/patient translations.

## Українська

Kāraka наразі найкраще представляти як evidence-bound класифікацію учасника в
обмеженій ситуації. Приклади відкидають фіксовані frames для dhātu,
універсальні graph edges і прямі переклади `agent/patient`.

Нормативно: простий `SemanticCall` допустимий лише як явно обмежений profile
для однієї простої ситуації. Він не встановлює валентність dhātu і не є
моделлю Паніні. Каузатив, duplicate role, nested event, альтернативний аналіз
чи невідомий participant повертають `unsupported`, `partial` або `unresolved`.
Усі modern nodes/edges мають namespace `machine:` і власний provenance.

## Deutsch

Kāraka wird vorläufig am besten als evidenzgebundene Klassifikation eines
Teilnehmers in einer abgegrenzten Situation dargestellt. Die Beispiele
verwerfen feste Dhātu-Frames, universelle Graphkanten und direkte
Agent/Patient-Übersetzungen.
