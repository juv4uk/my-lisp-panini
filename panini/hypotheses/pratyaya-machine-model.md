# Machine Models for pratyaya

## Hypothesis: Pratyaya Derivation as a Rewrite System

This document outlines the provisional machine representation of **pratyaya** (affixation) within the My Lisp/VM ecosystem. It addresses the question posed in `AGENTS.md` regarding whether Pāṇinian grammar can be modeled as a system of rewrite rules.

### H1: Semantically Conditioned Rewrite Rules

The formal structure of derivation (base + rule → new base) maps cleanly to a state-transition or string-rewriting model. Implementations like Vidyut successfully model affixation as a sequence of discrete `Step`s that mutate a `Term` state.

However, a pure context-free string rewrite system is insufficient. 
In classical formal languages, a rewrite rule `A → B` triggers based solely on the syntactic pattern of the string. In the Aṣṭādhyāyī, the application of a `pratyaya` (especially `kṛt` affixes) systematically references **semantics**. 

For example, `dhātoḥ karmaṇi kta` dictates that `kta` is applied when the semantic role is *karman* (object). Therefore, the machine model cannot just read the AST/string; the transition state must include a semantic context or intent environment. 

```lisp
;; Pseudo-code for a semantically conditioned rule dispatch
(defapply-rule rule-kta (base semantic-context)
  (if (and (is-dhatu? base) 
           (eq (get-role semantic-context) 'karman))
      (apply-affix base 'kta)
      nil))
```

### H2: The Affix as a Metadata Carrier (Operator)

In the machine model, a `pratyaya` is not just a string to be concatenated (`"gam" + "ta"`). It acts as an operator carrying execution metadata, specifically its `it` markers.

When a `pratyaya` is attached to a base, it brings configuration tags (e.g., `kit`, `ṇit`) that the engine reads during subsequent passes to determine whether to trigger or block morphophonemic routines like `guṇa` or `vṛddhi`.

```lisp
;; A pratyaya object in the VM
{
  :id 'kta
  :surface-form "ta"
  :it-markers '(kit)  ;; blocks guṇa/vṛddhi
  :type 'krt
}
```

### Open Questions for Implementation
1. **The Effect of `it` Markers**: We need an exhaustive matrix of how every `it` marker on a `pratyaya` affects the base (mapped to `PANINI-IT-MARKERS`).
2. **Conflict Resolution**: How does the engine resolve competition when multiple `pratyaya` rules are applicable for the exact same semantic intent? (Ties into `PANINI-RULE-CONFLICTS-VIPRATISEDHA` and the `resolve-conflict` hierarchy).
3. **Pure Morphology**: Are there instances in the Aṣṭādhyāyī where a `pratyaya` application is entirely devoid of semantic conditioning (referencing only the morphological shape of the base)? If so, the "semantic conditioning" hypothesis might only apply to certain subsets (like `kṛt` and `taddhita`) rather than being a universal requirement for the rule engine.
