# Identity and referent audit from derivation examples

Status: `PANINI-IDENTITY-REFERENT-EXAMPLE-AUDIT`. This audit examines the
current `Bavati` and `dadAti` example paths. It does not add an entity model or
assert that Pāṇini supplies a modern semantic-referent layer for every term.

## [PANINI]

The current evidence concerns roots, affixes, designations, substitutions and
derived forms. It supports keeping a lexical form distinct from an assigned
technical designation. It does not, in these examples, establish an
independently tracked worldly referent for a root or for an inflected word.

`saMjYA` research already shows why a designation cannot be collapsed into an
intrinsic type: its applicability, scope, and possible interaction with other
designations are evidence-bearing questions. That conclusion does not require
an entity/referent object.

## [INTERPRETATION]

The existing Derivation IR distinction is sufficient for the observed
morphological work:

| Concern | Example | Current representation |
| --- | --- | --- |
| term identity | the root occurrence retained through a trace | `term:<stable-id>` |
| source form | `BU`, `dA`, `Sap`, `tip` | `source_form` in canonical SLP1 |
| current form | `Bo`, `Bav`, `da`, `ti` | `surface_form` in canonical SLP1 |
| technical designation | `dhAtu`, `pratyaya`, `abhyAsa` when supported | provenance-bearing `designations` or relation |
| machine bookkeeping | fixture gaṇa field, parser flag, local tag | namespaced `metadata` |
| human presentation | bhū, dadāti, भवति | display-only observation |

The sentence glosses “he is” and “he gives” are useful teaching aids, but they
are not stable referent identifiers. They vary with translation, discourse,
and analysis and cannot silently become machine entities.

## [MY-LISP HYPOTHESIS]

### Result: no referent node for the current portfolio

For the Bhavati and dadAti paths, a new `entity:<id>` record is **not
admitted**. Every required distinction is already represented by term identity,
forms, evidence-bound designation, relation, metadata namespace, and display
artifact. Adding a referent node would merely encode the English gloss as if it
were a source-established machine object.

```text
term:root-BU
  source_form: BU
  surface_form: Bav
  designations: [dhAtu, ... only with provenance]
  display: bhū / bhavati / भवति (outside canonical state)

≠ entity:being
≠ string:"he is"
≠ designation:dhAtu
```

### Admission trigger for a future referent

An entity/referent relation may be proposed only when a documented example
requires identity across two or more term occurrences that cannot be expressed
as:

1. a term-preservation or substitution relation;
2. a designation assignment with scope and provenance;
3. a syntactic/derivational relation; or
4. a display or translation artifact.

The proposal must name the relation (`denotes`, `participant-in`,
`corefers-with`, or another narrow predicate), its evidence layer, scope, and a
counterexample. `entity:<id>` is machine namespace until such a record passes
review.

### Consequences for Lisp design

The safe near-term Lisp abstraction is a neutral identity-bearing record plus
immutable form transitions and designation evidence. It must not expose
`referent` as mandatory on every term, infer it from an SLP1 symbol, or derive
it from an English gloss. A future semantic-role example may require entities,
but that belongs to a separate kāraka/semantic boundary audit.

## English summary

The current Bhavati and dadāti derivations require distinct identities, forms,
designations, metadata and displays, but no independent referent node. Adding
one now would mistake a translation gloss for a source-established entity.

## Українська

Поточні деривації `Bavati` і `dadAti` потребують окремих identity, forms,
designations, metadata та display, але не незалежного referent node. Додавати
його зараз означало б прийняти перекладацький gloss за джерельно встановлену
сутність.

Нормативно: `entity:<id>` не входить до мінімального Derivation Machine 0.1.
Він може з’явитися лише тоді, коли конкретний документований приклад потребує
тотожності між кількома occurrences, яку не виражають term relation,
designation, derivational relation або display artifact. Тоді це буде
`machine:` relation з вузьким predicate, provenance, scope і counterexample.

## Deutsch

Die gegenwärtigen Bhavati- und dadāti-Derivationen benötigen getrennte
Identitäten, Formen, Designationen, Metadaten und Anzeigen, jedoch keinen
eigenständigen Referent-Knoten. Ihn jetzt hinzuzufügen würde eine
Übersetzungsglosse mit einer quellenbelegten Entität verwechseln.
