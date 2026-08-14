# Universal Dependencies ↔ kāraka mapping boundary

Status: research boundary for `PANINI-UD-KARAKA-MAPPING-BOUNDARY`.

## English — reference translation

### Decision

Universal Dependencies (UD) labels and Pāṇinian kāraka designations are not
interchangeable identifiers. This project does not define a conversion table
such as `kartf = nsubj` or `karman = obj`. A graph representation is likewise
not evidence that a kāraka is a modern graph edge.

### Why the boundary exists

Kāraka is studied here from its Paninian definitions, applicability conditions,
and derivational role. UD is a contemporary annotation framework for syntactic
dependency relations. Similar English glosses, similar tree shapes, or a shared
need for relation labels are insufficient evidence of equivalence.

### Three separate layers

```text
[PANINI]          canonical kāraka ID, sūtra/source, and documented conditions
[UD ANNOTATION]   original UD relation and its dataset/documentation provenance
[HYPOTHESIS]      a directional, scoped comparison between the two records
```

Neither source layer is rewritten by a hypothesis. In particular, an admitted
`[HYPOTHESIS]` never changes `panini:kartf` into `ud:nsubj`, and never turns a
UD annotation into proof of a Paninian analysis.

### Minimum record for a future comparison

```yaml
id: hypothesis:ud-karaka:0001
panini_record: panini:kartf
ud_record: ud:nsubj
relation: comparable-under-stated-conditions
direction: non-equivalence-preserving
evidence:
  - source: ...
scope: ...
counterexamples: []
status: experimental
confidence: low
```

The permitted relation vocabulary is deliberately cautious: `comparable`,
`overlaps`, `not-comparable`, or `unresolved`. `equivalent` is not an available
initial value.

### Admission gate

No mapping investigation starts from label names. It requires a small aligned
portfolio of actual Sanskrit examples, each retaining its Paninian sources,
UD dataset provenance, segmentation/tokenization assumptions, and documented
counterexamples. Results that remain ambiguous are published as `unresolved`.

## Українська — нормативна

### Рішення

Universal Dependencies (UD) labels і панініївські kāraka designations не є
взаємозамінними ідентифікаторами. Проєкт не визначає таблицю конверсії на кшталт
`kartf = nsubj` або `karman = obj`. Так само graph representation не є доказом,
що kāraka є сучасним graph edge.

### Навіщо потрібна межа

Тут kāraka досліджується через панініївські визначення, умови застосовності й
роль у деривації. UD є сучасною annotation framework для syntactic dependency
relations. Подібні англійські gloss, подібна форма дерева чи спільна потреба в
relation labels не є достатніми доказами еквівалентності.

### Три окремі рівні

```text
[PANINI]          canonical kāraka ID, sūtra/source і документовані умови
[UD ANNOTATION]   оригінальне UD relation та provenance dataset/documentation
[HYPOTHESIS]      напрямлене, обмежене порівняння двох записів
```

Жоден source layer не переписується гіпотезою. Зокрема, прийнята
`[HYPOTHESIS]` не перетворює `panini:kartf` на `ud:nsubj` і не робить UD
annotation доказом панініївського аналізу.

### Мінімальний запис майбутнього порівняння

```yaml
id: hypothesis:ud-karaka:0001
panini_record: panini:kartf
ud_record: ud:nsubj
relation: comparable-under-stated-conditions
direction: non-equivalence-preserving
evidence:
  - source: ...
scope: ...
counterexamples: []
status: experimental
confidence: low
```

Допустима лексика relation навмисно обережна: `comparable`, `overlaps`,
`not-comparable` або `unresolved`. `equivalent` не є початковим значенням.

### Admission gate

Жодне mapping-дослідження не починається з назв labels. Потрібен малий aligned
portfolio реальних санскритських прикладів: кожен зберігає свої Panini sources,
UD dataset provenance, segmentation/tokenization assumptions і documented
counterexamples. Неоднозначні результати публікуються як `unresolved`.

## Deutsch — Referenzübersetzung

### Entscheidung

Universal-Dependencies-Labels und paninische kāraka-Designations sind keine
austauschbaren Kennungen. Dieses Projekt definiert keine Konversionstabelle wie
`kartf = nsubj` oder `karman = obj`. Eine Graphdarstellung beweist ebenso wenig,
dass ein kāraka eine moderne Graphkante ist.

### Grund der Grenze

Kāraka wird hier aus paninischen Definitionen, Anwendbarkeitsbedingungen und
derivationaler Rolle untersucht. UD ist ein modernes Annotation Framework für
syntaktische Dependency Relations. Ähnliche englische Glosses, Baumformen oder
Relation Labels genügen nicht als Äquivalenzbeweis.

### Drei getrennte Ebenen

```text
[PANINI]          canonical kāraka ID, Sūtra/Quelle und dokumentierte Bedingungen
[UD ANNOTATION]   originale UD-Relation und Dataset-/Dokumentations-Provenance
[HYPOTHESIS]      gerichteter, begrenzter Vergleich der beiden Einträge
```

Eine Hypothese schreibt keine Source-Ebene um: `panini:kartf` wird nicht zu
`ud:nsubj`, und eine UD-Annotation wird nicht zum Beweis einer paninischen
Analyse. Künftige Vergleiche benötigen reale ausgerichtete Sanskrit-Beispiele,
behalten Quellen, Segmentierungsannahmen und Gegenbeispiele und verwenden nur
`comparable`, `overlaps`, `not-comparable` oder `unresolved` — niemals
anfänglich `equivalent`.
