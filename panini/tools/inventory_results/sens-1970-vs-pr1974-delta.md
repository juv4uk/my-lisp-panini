# SENS #1970: cross-check of my heuristic first pass against draft PR #1974 (2c330985), 2026-10-01

Run: `inventory_function8.py` on `git archive` of the PR head (410 occurrences / 107 files; 372 / 105 paths without PR #1974's own docs); #1974 inventory TSV (46 curated rows, 37 local paths + 10 `cml:` cross-repo rows).
Read-only. Heuristic labels (hand-check of 30 rows: 19 of 22 classified rows acceptable = 86%; unknown 38%).

| Delta | Count | Notes |
|---|---|---|
| Paths in BOTH inventories | 28 | of #1974's 37 local paths; class agrees on 9, disagrees on 4, my label unknown on 15 |
| (a) only in my scan (non-docs) | 65 paths | actionable beyond tests/unknown: 5 CI workflows (core1-*, sid8-issue-lifecycle-guard, kernel-abi-transport-boundary), lib/macro.lisp, contracts/core4-predicate-answer-boundary.lisp, eval/{lower,builtins,closures,profile_mechanisms_generated,special_forms/core}.rs, semantic_registry.rs, scripts/generate-rust-profile-mechanism-routes.lisp, examples/ci_bench.rs; plus knowledge/semantic-lineage-core-v1.lisp (axiom text) |
| (b) only in #1974 | 9 local paths + 10 `cml:` rows | local: contracts/core-profile-contract.lisp, lib/surface/semantic-registry.lisp, lib/core.lisp, lib/core4.lisp, lib/generated/function-table.lisp, docs/generated/function-table.md, scripts/verify-repo.lisp, workflows/surface-drift-check.yml, knowledge/repo-tooling-inventory.lisp. My patterns missed them: their assumptions are phrased as `function-identity-space`, table rows, drift checks, not as Sens8/{8}/256. The cml: rows are outside my scan |
| (c) class disagreement on shared paths | 4 | canon.rs PRIMITIVE_TABLE[256]: mine runtime-dispatch, theirs profiling/index (backend-only-safe); scripts/check_semantic_registry.py: mine runtime-dispatch (my error), theirs semantic-guard; benchmarks/function_table.py: mine profiling, theirs test-only; workflows ci.yml, sid8-only-ontology.yml: mine semantic-guard, theirs CI/ratchet |

The paths named as candidate gaps (syntax.rs:80/:95, parser.rs:459-460, eval/canon.rs:115, scripts/check_semantic_registry.py:11) are ALREADY in #1974 (syntax.rs split into Call(Sens8) parser/AST and FASL TAG_BINARY; canon.rs split into PRIMITIVE_TABLE and SID_ROUTES). Real deltas: workflows/kernel-abi-transport-boundary.yml, lib/macro.lisp:1 and knowledge/semantic-lineage-core-v1.lisp:179 (axiom statements; #1974 uses knowledge/guard-reference.lisp for the axiom text).
Not checked: the 15 shared paths where my label is unknown; the cml: repo; whether #1974's blocker flags are right.
