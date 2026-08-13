# Foundation Reconciliation Report (panini-machine-model-v0.1)

**Status:** RECONCILED
**Date:** 2026-08-13
**Gate Reference:** `PANINI-MACHINE-GATE-REVIEW`

This document serves as the formal closure of the `PANINI-MACHINE-FOUNDATION-RECONCILIATION` task. It verifies that the `panini/machine/` codebase now fully adheres to the theoretical foundation established in `panini-foundation-v0.1.md` and addresses the technical debt identified during the gate review.

## Addressed Technical Debt

### 1. Dhatu Registry Synchronization
**Issue:** `panini-core.my` originally contained a hardcoded inline registry of roots, duplicating the single source of truth (`registry/dhatu/*.yaml`). `rules.my` didn't even use this inline registry, hardcoding lists of characters like `'(B U)`.
**Resolution:** 
- The inline registry in `panini-core.my` was explicitly rebranded as `*test-dhatu-registry*`—a temporary snapshot used purely for testing until file I/O is added to My Lisp. 
- `rules.my` (`semantic-to-prakriya`) was rewritten to use `*test-dhatu-registry*` dynamically. When it processes `DHATU_DA`, it looks up the root's `class` in the registry and dynamically applies the `juhotyAdi` tag. This proves that structural metadata is now driven by the central data structures.

### 2. Variable Arity in Action Graphs
**Issue:** `make-action-graph` originally forced a strict two-argument structure (`kartf` + `karman`), which was historically inaccurate and rejected by `dhatu-karaka-relation.md`.
**Resolution:**
- `make-action-graph` was updated to accept `karaka-pairs`, an association list of arbitrary length containing any valid subset of the six `kAraka` roles.

### 3. Trilingual Documentation and Test Coverage Sync
**Issue:** `TESTING.md` stated that the `dadAti` test was merely "planned". The status of the documentation was out of sync with the actual implementation.
**Resolution:**
- `TESTING.md` was rewritten across all three supported languages (English, Ukrainian, German) to accurately reflect that the `dadAti` apavāda conflict is fully tested.
- It was also updated to document the new `test-karayati-derivation`, which verifies recursive grammar generation (Rule 3.1.32).

## Conclusion
The `panini/machine/` prototype engine is now structurally sound and theoretically aligned with the v0.1 foundation. It successfully acts as a bridge between the AST semantic calls and the Paninian state-machine derivation loop.
