# Machine Models for it-markers (anubandha)

## Hypothesis: The `it` System as Structured Execution Metadata

This document outlines the provisional machine representation of **it** markers within the My Lisp/VM ecosystem. It clarifies why equating `it` with simplistic "control tags" or "compiler metadata" is an inadequate hypothesis if taken too loosely.

### H1: The Heterogeneity of Metadata

A naive computational model might represent an `it` marker as a simple boolean flag or a single generic metadata class (e.g., `is_it: bool`). 

However, the Aṣṭādhyāyī defines dozens of distinct `it` markers (e.g., `Kit`, `Git`, `Ṇit`, `cit`, `Ñit`, `pit`), each of which triggers or blocks entirely different routines in the inference engine. Therefore, `it` is not a single type of metadata; it is a **family of distinct control signals**, each with its own semantic effect.

```lisp
;; Naive (Incorrect) Model
{ :surface "a" :is-it true }

;; Paninian Machine Model
{
  :surface "a"
  :it-markers '(Nit cit) ;; Specific signals carrying specific execution rules
}
```

### H2: The Lifecycle of an `it` Marker

The lifecycle of an `it` marker in the machine model closely resembles compiler directives that are consumed during intermediate representation (IR) processing and stripped from the final binary.

1. **Injection (upadeśa)**: The marker exists in the canonical registry (e.g., the `dhātu` registry or the `pratyaya` definition).
2. **Evaluation**: When a rule applies, the engine checks the presence of specific `it` tags on the operands to decide control flow (e.g., branching to a `vṛddhi` routine if `Ñit` is present, or skipping it if `Ṇit` is present).
3. **Elision (tasya lopaḥ)**: A universal garbage-collection or cleanup routine (implementing 1.3.9) strips the `it` markers from the surface form so they do not accidentally bleed into the final string output. 

```lisp
;; Pseudo-code for the lopa routine
(def tasya-lopah (term)
  (let ((clean-form (remove-it-characters (surface-form term))))
    (update-term term :surface clean-form)))
```

### H3: Default vs. Exception Mechanics

The `it` system often encodes default-override mechanics. For instance, all `sārvadhātuka` affixes implicitly block `guṇa`/`vṛddhi` (acting as if they were `Ṇit`), *unless* they possess a `pit` marker (which overrides the default and allows the strengthening).

In a machine model, this requires the rule engine to calculate an "effective" `it` state for a given term, rather than just reading its explicit tags.

```lisp
;; Pseudo-code for effective tag resolution
(def has-effective-Nit? (affix)
  (if (is-sarvadhatuka? affix)
      (not (has-tag? affix 'pit)) ;; Implicitly Ṇit if not pit
      (has-tag? affix 'Nit)))     ;; Otherwise explicitly check for Ṇit
```

### Open Questions for Implementation
1. **The `it` Identification Algorithm**: Sūtras 1.3.2 through 1.3.8 provide the algorithmic criteria for determining which letters in a string are `it` markers (e.g., "final consonants", "initial palatals in affixes"). Does the machine model parse raw strings (like `"ṣvuñ"`) and dynamically identify the `it` characters, or do we hardcode the `it` markers into the registry as structured arrays (e.g., `surface: "vu", it: [ṣ, ñ]`)? Relying on pre-parsed arrays is vastly simpler and less error-prone.
2. **Tag Provenance**: If we pre-parse the tags in the registry, we must ensure we retain a link to the original sūtra that justifies *why* that tag was assigned (provenance tracking).
