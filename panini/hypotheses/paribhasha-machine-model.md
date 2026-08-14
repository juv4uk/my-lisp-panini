# Machine Models for Paribhāṣā

## Hypothesis: Paribhāṣā as Meta-Level Rule Dispatch

This document explores computational analogies for the **paribhāṣā** system in Pāṇini's grammar. These are explicitly marked as *hypotheses* for machine representation within the My Lisp/VM ecosystem, not claims about Pāṇini's historical intent.

### H1: Paribhāṣā as `defmacro`

A key insight for the inference engine is that paribhāṣās are **not** object-level rules. They do not add suffixes or mutate phonemes. Instead, they determine the **conditions of application** for other rules.

In Lisp terminology, they function analogously to a `defmacro` layer or a meta-circular evaluator. In a rule engine architecture, paribhāṣās act as **meta-functions** that wrap the dispatch mechanism. 

```text
                 Rule Engine
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
  [Object Rules]            [Meta Rules / paribhāṣā]
  (vidhi-sūtra)             (resolve-conflict logic)
  - rule-7-3-84             - antaraṅga?
  - rule-6-1-78             - nitya?
  - rule-3-1-68             - apavada-of?
                            - later-in-ashtadhyayi?
```

This implies a two-layered architecture:
1. **Layer 1**: Declarative object rules (e.g., a-lists in `rules.my`).
2. **Layer 2**: Meta-logic dispatching (paribhāṣā implemented in `meta.my`).

### H2: The `resolve-conflict` Dispatch Algorithm

When the inference engine finds two or more rules applicable to a single state (a conflict), it does not apply them directly. Instead, it delegates to a `resolve-conflict` routine, which is a programmatic implementation of the paribhāṣā hierarchy.

```lisp
;; [MY-LISP HYPOTHESIS]
;;
;; resolve-conflict: Implementation of the paribhāṣā priority hierarchy.
;; Accepts two competing rules and the current derivation state (prakriyā).
;; Returns the single rule that should be applied.
;;
(def resolve-conflict
  (lambda (rule-a rule-b prakriya)
    (cond
      ;; P3: antaraṅga > bahiraṅga
      ((antaraMga? rule-a prakriya) rule-a)
      ((antaraMga? rule-b prakriya) rule-b)
      
      ;; P4: nitya > anitya
      ((and (nitya? rule-a prakriya) (not (nitya? rule-b prakriya))) rule-a)
      ((and (nitya? rule-b prakriya) (not (nitya? rule-a prakriya))) rule-b)
      
      ;; P2: apavāda > utsarga
      ((apavada-of? rule-a rule-b) rule-a)
      ((apavada-of? rule-b rule-a) rule-b)
      
      ;; P1: vipratiṣedhe paraṃ kāryam (1.4.2) — DEFAULT FALLBACK
      ((later-in-ashtadhyayi? rule-a rule-b) rule-a)
      (t rule-b))))
```

### H3: Determining "Later in the Text"

The default resolution mechanism (1.4.2) requires knowing which rule comes "later" in the grammar.
In a machine model, every rule in the registry must possess a numeric ID, such as `"7.3.84"`. 
The `later-in-ashtadhyayi?` function would parse these IDs into tuples `(adhyāya, pāda, sūtra)` and perform a lexicographical comparison.

```lisp
;; Returns t if rule-a comes later in the Aṣṭādhyāyī than rule-b
(def later-in-ashtadhyayi?
  (lambda (rule-a rule-b)
    (sutra-gt? (rule-id rule-a) (rule-id rule-b))))
```

### H4: Sūtra Types as State Modifiers

If the `panini-machine-model-v0.1` models sūtra types with distinct tags:
- `vidhi` (operational) and `atideśa` (extension) represent different *execution effects* (mutating state vs. expanding rule applicability).
- `niyama` (restriction) acts as an applicability *modifier* for a `vidhi`, rather than an independent action type. 

### Implementation Roadmap for Paribhāṣā
1. Implement `resolve-conflict` in `panini/machine/meta.my`.
2. Ensure all rules in `rules.my` have their full numeric Aṣṭādhyāyī IDs.
3. Use a complex derivation like `dadāti` (which inherently features rule conflicts) as the integration test for the paribhāṣā hierarchy.
