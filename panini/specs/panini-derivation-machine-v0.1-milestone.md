# Panini Derivation Machine v0.1 — milestone

Status: normative project milestone. It supersedes any near-term plan to
integrate Pāṇinian vocabulary or mechanisms into My Lisp before the required
derivation evidence exists.

## [PANINI]

The project must let the formal structure of the grammatical system constrain
its own machine model. `dhAtu`, `saMjYA`, `kAraka`, anuvṛtti, adhikāra and
asiddha are research objects; this milestone does not declare any of them My
Lisp primitives, graph edges, types, or VM instructions.

## [INTERPRETATION]

Recent contracts motivate an especially careful distinction: an immutable
derivation history can be retained while a particular rule check receives a
limited view of prior effects. This is a machine interpretation to test against
examples, not an assertion that the project has reconstructed all of Tripādī.

## [MY-LISP HYPOTHESIS]

### Goal

`Panini Derivation Machine 0.1` must be **reproducible, immutable and
explainable**. It is a bounded evidence milestone, not a universal scheduler,
Sanskrit NLP system, or My Lisp language feature.

### Example portfolio

Select three to five well-documented derivations with increasing and distinct
demands. Every selected example must traverse:

```text
source
  → terms
  → designations
  → immutable state_0
  → candidate rules
  → visibility
  → conflict resolution (if any)
  → operation
  → state_n
  → surface result
  → complete evidence trace
```

Each transition answers, with stable references:

1. What changed?
2. Which rule or interpreted rule was used?
3. Why was it applicable in this state and scope?
4. Which earlier effects could it see, and why?
5. Which alternatives existed, if any, and why were they not selected?
6. Which operation produced the next immutable state?
7. Which source, interpretation, policy, or machine hypothesis supports every
   decision?
8. What remains unknown, disputed, partial, or blocked?

### Mandatory epistemic boundaries

| Distinction | Required treatment |
| --- | --- |
| term identity / source form / surface form | distinct IR fields or explicitly named relation |
| designation / metadata | designation requires provenance; metadata is namespaced machine data |
| semantic referent / display name | neither is implicit in a string or SLP1 identifier |
| visibility / conflict | separate records and trace events |
| Pāṇini / interpretation / My Lisp hypothesis | explicit layer on every nontrivial claim |

An independent entity or referent record is an open research question. It is
added only when an example demonstrates a need not handled by term identity,
forms, designation, relation, and display fields.

### Unknown first

`unresolved`, `disputed`, `partial`, and `blocked` are valid outcomes. An
example with unknown rule applicability, visibility, precedence, or source
support must stop at the appropriate result; it must not use unstated numeric,
implementation, or “common sense” fallback. A successful result is permitted
only when the trace’s declared acceptance gates pass.

### Deferred decisions

Until the example portfolio is complete, the project must not:

- add a universal scheduler;
- equate kāraka with a graph edge or a modern semantic role;
- equate saṃjñā with a type, tag, or class;
- infer that adhikāra, anuvṛtti, and asiddha form one general context primitive;
- optimize representation for My Lisp, C, CUDA, FPGA, or a VM;
- change My Lisp parser/evaluator semantics from Panini research.

The appropriate question for every proposed abstraction is: “is this a
property established for the Pāṇinian system, or a convenience of our machine
model?” The latter must be namespaced as `machine:` and linked to explicit
provenance.

### Exit criteria

1. Three to five examples have independently reviewable source paths and
   explicit epistemic layers.
2. At least one example records a genuine conflict; at least one records
   contextual visibility or an honest `unresolved` visibility result.
3. Each example serializes immutable states and append-only evidence events.
4. Each transition is answerable by the eight questions above.
5. No result marked `complete` relies on an undocumented fallback.
6. A synthesis report identifies which abstractions are evidenced, merely
   implementation conveniences, or still unknown.

Only after this milestone may a separate review ask whether any demonstrated
abstraction belongs in My Lisp.

## English summary

The next milestone is a small portfolio of end-to-end, source-traceable,
immutable and explainable derivations. It deliberately defers My Lisp
integration, universal scheduling, and premature ontology decisions.

## Українська

Наступний milestone — невеликий портфель end-to-end, джерельно простежених,
immutable та explainable деривацій. Він навмисно відкладає інтеграцію з My
Lisp, універсальний scheduler і передчасні онтологічні рішення.

Нормативно: формальна модель має проявитися через реальні приклади. `asiddha`
розглядається як перевірювана гіпотеза про контекстну видимість immutable
історії, а не як дозвіл переписувати минулий state. `unknown`, `unresolved`,
`partial`, `blocked` і `disputed` є повноправними результатами. Якщо для
переходу бракує source, застосовності, visibility чи precedence, derivation не
має вигадувати fallback.

Лише після 3–5 повністю пояснених прикладів дозволено окремо запитати, чи
якась виявлена абстракція заслуговує бути частиною My Lisp. До того `dhAtu`,
`saMjYA`, `kAraka`, anuvṛtti, adhikāra та asiddha не є його primitives.

## Deutsch

Der nächste Meilenstein ist ein kleines Portfolio durchgängiger,
quellennachvollziehbarer, unveränderlicher und erklärbarer Derivationen. Er
verschiebt die My-Lisp-Integration, universelles Scheduling und voreilige
ontologische Entscheidungen bewusst.
