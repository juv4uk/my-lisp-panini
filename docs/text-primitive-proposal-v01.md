# Text Primitive Proposal v0.1

Status: DRAFT — pending COMPILER STEWARD review (vyasa)
Motivation: fpga-lisp@6c2e024 benchmark (recursive text traversal = bottleneck)
Author: sakshi · 2026-08-24

## Context

check-stale-refs.my (20 invocations) takes 13.65s vs empty my-lisp 0.06s.
Bottleneck: recursive string traversal and construction in the checker.
Python equivalent: 0.89s total.

Root cause: my-lisp lacks efficient string primitives. All text processing
uses recursive car/cdr traversal over character lists, allocating new lists
at every step.

## Proposed primitives

### 1. string-slice

```my-lisp
(string-slice str start end)
```

Returns substring from `start` to `end` (exclusive). Zero-copy if
implementation uses offset+length into original buffer.

Rationale: eliminates recursive char-by-char traversal for common cases
(line extraction, token splitting, prefix/suffix checks).

### 2. *argv*

```my-lisp
*argv*    ; => list of strings from command line
```

Binds command-line arguments as a list of strings at program start.
Already partially exists in CLI mode (`--version`, file argument handling
in `tests/cli.rs`) but not exposed as a my-lisp binding.

## Non-goals (v0.1)

- No regex engine
- No mutable strings (immutability preserved)
- No Unicode normalization (host-side responsibility)

## Expected impact

check-stale-refs.my bottleneck is O(n²) recursive traversal over ~200-line
files. With string-slice, common patterns become O(1) slicing instead of
O(n) list reconstruction. Estimated improvement: significant reduction in
wall time for text-heavy tools, bringing closer to Python baseline.

## Implementation notes

- `string-slice`: likely a thin wrapper over Rust's `str::get(start..end)`
  with bounds checking → named error on out-of-range.
- `*argv*`: bind once during environment initialization from
  `std::env::args().skip(1)` collected into my-lisp list of strings.
