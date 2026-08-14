# Machine Models for anuvṛtti and adhikāra

## Hypothesis: anuvṛtti as Lexical Scope / Context Binding

This document outlines the provisional machine representation of **anuvṛtti** and **adhikāra** (contextual continuation) within the My Lisp/VM ecosystem. It treats these mechanisms as explicit data structures rather than implicit reading rules.

### H1: The Insufficiency of AST Inheritance

Modern computer science models often map hierarchical contexts to Abstract Syntax Trees (ASTs). In an AST, a child node inherits properties from its parent because the block boundaries are explicitly defined by syntax (brackets, indentation).

In the Aṣṭādhyāyī, the text is a linear sequence of rules. An `adhikāra` structurally resembles **lexical scoping**, but without explicit closing brackets. The boundaries are deduced by the interpreter (commentator) based on grammatical sense or phonetic markers lost to writing, rather than syntactic structure.

Therefore, any machine model cannot simply parse the text into a tree based on tokens. The `adhikāra` boundaries must be injected as a separate, independently verified metadata layer.

### H2: Explicit State Injection vs. Rule Modification

There are two primary ways to model `anuvṛtti` in a rule engine:

**Approach A (Rule Expansion):**
Pre-process the rule database. If rule B inherits context from rule A, rewrite rule B in memory to explicitly include A's conditions.
*Advantage*: Evaluation is stateless and extremely fast. Each rule is self-contained.
*Disadvantage*: Loss of provenance. If a rule fails, it's hard to trace whether the failure was due to its own condition or an inherited condition.

**Approach B (Dynamic Environment):**
The engine maintains a `ContextEnvironment`. When an `adhikāra` rule triggers, it pushes a context onto the environment stack. Subsequent rules evaluate against both their own conditions *and* the current stack.
*Advantage*: Mirrors the Paninian reading process closely. Traceability is perfect.
*Disadvantage*: State management complexity. 

```lisp
;; Pseudo-code for Approach B
(def evaluate-rule (rule state context-stack)
  (let ((effective-rule (merge-context rule context-stack)))
    (if (matches? effective-rule state)
        (apply-rule effective-rule state)
        nil)))
```

Current inclination leans towards Approach B for `panini-machine-model-v0.1`, as it preserves the original rule structure and enables better explanation tracking.

### Open Questions for Implementation
1. **Scope Termination**: How do we encode the end of an `adhikāra`? Since the text lacks `end-adhikāra` markers, do we add explicit `(end-scope 1.4.23)` instructions in our formal rule registry, or do we rely on the next `adhikāra` to pop the stack?
2. **Conflicting Scopes**: When the domains of two different `adhikāra`s intersect (e.g., a high-level general `adhikāra` and a nested specific one), how does the interpreter resolve priority?
3. **The tripādī Boundary**: The grammar shifts into a fundamentally different meta-regime for the last three chapters (`tripādī`), governed by rules like `asiddhavat` (rules are considered "as if suspended" to earlier rules). This boundary is a massive shift in scope and state management not yet modeled.
