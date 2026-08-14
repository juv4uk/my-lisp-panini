# Machine Models for prātipadika

## Hypothesis: The Provenance-Aware Type System

This document outlines the provisional machine representation of `prātipadika` (nominal stems) within the My Lisp/VM ecosystem.

### H1: Not Just a Syntax Tree Node

In standard compilers, a noun is simply a leaf node in an AST `(Noun "tree")`. In the Paninian system, `prātipadika` is a formal state that a string of characters achieves either fundamentally (by having meaning but not being a root or affix, per 1.2.45) or through derivation (by appending specific suffixes like `kṛt` or forming a compound, per 1.2.46).

Therefore, equating `prātipadika` to a generic `Symbol`, `String`, or `Entity` class is a lossy abstraction. 

### H2: Representing Provenance

If a future engine needs this category, it should be stored as a typed designation within the derivation state, preserving its source rule (provenance). 

```lisp
;; My-Lisp Hypothesis: A struct with provenance
(defstruct pratipadika
  base-form       ;; e.g., "rAma"
  provenance)     ;; The rule that granted this status (e.g., 1.2.45 or 1.2.46)

;; Example of creating a derived pratipadika (krdanta)
(defn apply-krt (dhatu suffix)
  (let [derived-form (concat (apply-sandhi dhatu suffix))]
    (make-pratipadika :base-form derived-form :provenance "1.2.46")))
```

Alternatively, using a semantic tagging system:

```yaml
term_id: example-derived-form
designation: prAtipadika
designation_source: "1.2.46"
evidence_status: corpus-checked
```

### H3: The Filter for Suffixes
The primary mechanical purpose of the `prātipadika` tag in the inference engine is to act as a gatekeeper. Sūtra 4.1.1 (*ṅyāpprātipadikāt*) dictates that the specific case suffixes (`sup`) and feminine affixes can *only* be attached to items bearing this designation. 

In a machine model, this behaves exactly like a type signature on a function:

```lisp
;; The sup-affix applier expects an object of type 'pratipadika'
(defn apply-sup-case (p :type pratipadika, case-id)
  ...)
```

Any attempt to attach a nominal suffix to a raw `dhātu` or a meaningless string would fail the type-check because the object lacks the `prātipadika` trait/provenance tag.
