# Machine Models for Foundation Ontology

## Hypothesis: Ontology as the Lisp Type System / AST

This document outlines the provisional machine representation of the foundational ontological entities of the Aṣṭādhyāyī within the My Lisp/VM ecosystem. We must take care never to blindly map ancient terms to modern CS constructs without verifying the structural equivalence.

### H1: `dhātu` and `prātipadika` as Base Objects (Primitive Entities)

In a symbolic AI graph, the `dhātu` and `prātipadika` represent the core, typed object instances or primitive nodes. 
- A `dhātu` acts as the core *predicate* or *action node* in a semantic graph.
- A `prātipadika` acts as the core *entity* or *argument node*.

```lisp
;; Machine type representations
(deftype dhatu (id meaning gana))
(deftype pratipadika (id meaning gender))
```

### H2: `pratyaya` as Higher-Order Functions / Decorators

Since a `pratyaya` (affix) is applied to a base and transforms it into a new legal form (often carrying its own semantic shift, like moving from "cook" to "one who cooks"), it behaves conceptually like a higher-order function, decorator, or state transformer.

A pure AST approach might treat it merely as a child node `(Suffix 'kta')`, but a dynamic inference approach treats it as an operator that encapsulates state logic and applies it to the base.

```lisp
;; Conceptualizing a pratyaya as an operator
(def pratyaya-kta (base)
  (transform-state base ...))
```

### H3: `kāraka` as Semantic Edges (Graph Theory)

A `kāraka` defines the relationship between the `dhātu` and a participating entity. It is the most direct analogue to a **labeled directed edge** in a Knowledge Graph or an Abstract Semantic Graph (ASG).
The mapping is structural: `[Entity/prātipadika] --(kāraka-edge)--> [Action/dhātu]`.

```lisp
;; A triple representation in the knowledge graph
(assert-relation 'kartr 'devadatta 'pac)
```

### H4: `saṃjñā` as Type Traits / Tags

`saṃjñā` terms act precisely like type tags or interfaces. When a rule applies to `tiṅ`, it is executing a pattern match on all objects bearing the `tiṅ` tag. This translates directly to Lisp symbols used as metadata tags on data structures, enabling polymorphic rule dispatch.

### H5: Sūtra Types as Evaluation Regimes

If the rule engine categorizes its operations, the sūtra types map to different operational behaviors:
- `vidhi`: Standard mutation/rewrite operations.
- `niyama`: Constraint solvers or filter functions.
- `atideśa`: Metamorphic casts or alias assignments (e.g., treating type X as type Y for the duration of a scope).
- `paribhāṣā`: Core engine dispatch logic (e.g., Lisp macros or engine-level conflict resolvers).
