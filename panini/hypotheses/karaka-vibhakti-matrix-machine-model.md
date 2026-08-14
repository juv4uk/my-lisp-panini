# Machine Models for kāraka and vibhakti Mapping

## Hypothesis: Distinct Layers for Semantics and Morphology

This document outlines the provisional machine representation of the relationship between semantic roles (`kāraka`) and morphological cases (`vibhakti`) in the My Lisp/VM ecosystem.

### H1: Separation of Concerns

A common pedagogical shortcut is to equate `kartṛ` (agent) with the nominative case (`prathamā`), and `karman` (patient) with the accusative case (`dvitīyā`). The Aṣṭādhyāyī explicitly rejects this 1-to-1 mapping. 

In a computational system, `kāraka` and `vibhakti` must be modeled as two entirely distinct layers:
1. **Semantic Layer (Graph):** The `kāraka` relations form the edges between the action (`dhātu`) and the entities (`prātipadika`).
2. **Morphological Layer (Surface):** The `vibhakti` is the physical affix (`sup`) attached to the noun to express the underlying semantic graph.

```lisp
;; Bad: Merging semantics and morphology
;; (defstruct noun :word "rAma" :role :nominative)

;; Good: Separation of concerns
(defstruct semantic-node
  :entity (make-pratipadika "rAma")
  :karaka-role :kartf
  :surface-case :tftIyA) ;; Instrumental case, typical in passive constructions
```

### H2: Rule-Conditioned Mapping

No inference engine should infer `karman` from `dvitīyā` alone, nor infer a case form from a `kāraka` label without checking the derivation context (e.g., active vs. passive voice). 

If a later machine model records both layers, it must use distinct fields and record the rule that created the mapping:

```yaml
# A passive construction example
relation: kartf
surface_case: tftIyA
mapping_rule: "2.3.18"  # kartṛkaraṇayostṛtīyā
link_status: rule-conditioned
```

By decoupling these layers, the Lisp inference engine can correctly model active, passive, and causative transformations without breaking the underlying knowledge graph. The `kāraka` (semantic graph) remains invariant, while the `vibhakti` (surface morphology) changes according to the voice/focus of the sentence.
