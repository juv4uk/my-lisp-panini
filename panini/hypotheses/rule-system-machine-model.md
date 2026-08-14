# Machine Models for the Rule System and Conflicts

## Hypothesis: Conflict Resolution as Inference Engine Dispatch

This document outlines the provisional machine representation of rule conflicts (`utsarga-apavāda` and `vipratiṣedha`) within the My Lisp/VM ecosystem.

### H1: Static vs. Dynamic Conflict Resolution

When multiple rules can apply to the same AST node, a rule engine must decide which to execute. There are two fundamental architectural approaches to this:

1. **Static Imperative Dispatch (The Vidyut Approach)**:
   In a standard procedural implementation like Vidyut, the resolution logic is hardcoded into the execution flow. The program explicitly calls the `apavāda` function first; if it returns null, it calls the `utsarga` function. The `vipratiṣedha` principle is never "calculated" at runtime; the programmer has already manually ordered the function calls to respect the correct priority.
   *Advantage*: Extremely fast, highly predictable.
   *Disadvantage*: The grammar's logical structure is lost inside imperative code. The system cannot "explain" why it chose a rule based on Paninian principles, only that the code was written that way.

2. **Dynamic Inference Engine (The Symbolic AI Approach)**:
   In a true symbolic rule engine (the goal for My Lisp), the engine queries a rule database. The query returns a *set* of applicable rules. The engine then passes this set through a priority filter:
   - Filter 1 (Domain Check): Does Rule A's condition completely subsume Rule B's condition? If yes, keep B (`apavāda`).
   - Filter 2 (Paribhāṣā Check): Is Rule A `nitya` and Rule B `anitya`? If yes, keep A.
   - Filter 3 (Fallback): Compare the internal numeric IDs (sūtra numbers) of the remaining rules. Keep the highest number (`vipratiṣedha` 1.4.2).

### H2: The Computational Cost of Domain Checking

Filter 1 (determining if Rule B is an `apavāda` to Rule A dynamically) is computationally equivalent to proving that Set B is a strict subset of Set A. 
In a purely formal rule system, calculating subset relations dynamically at runtime for every rule evaluation is computationally prohibitive. 

Therefore, a hybrid machine model is most likely:
The subset relations (`utsarga-apavāda` links) are calculated *at compile time* and stored as explicit pointers in the rule registry.

```lisp
;; Machine representation of a rule with pre-computed conflict metadata
{
  :id 7.3.84
  :type 'vidhi
  :overrides '(7.3.82 7.3.83) ;; Pre-computed apavāda links
  :action (fn [node] ...)
}
```

When the engine executes, it simply checks the `:overrides` list of the applicable rules. If a tie remains, it executes a simple integer comparison on the `:id` field to resolve `vipratiṣedha`.

### Open Questions for Implementation
1. **The Paribhāṣā Matrix**: We need a complete, strictly ordered array of the interpretative filters (`antaraṅga`, `bahiraṅga`, `nitya`, `anitya`). This acts as the middleware between the subset check and the final ID check.
2. **Runtime Flexibility**: Does the user ever need to disable the `vipratiṣedha` fallback to see all possible derivations (e.g., in a debug mode)? The engine architecture should probably allow the conflict-resolution pipeline to be swapped or introspected.
