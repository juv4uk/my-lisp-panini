# Testing the Panini Machine Model

This document outlines the testing strategy for `panini-machine-model-v0.1`. Since our engine is designed to run on the custom **My Lisp** VM, we provide a native test suite written directly in Lisp.

## Test Suite Location
The tests are located in [`panini/machine/tests.my`](file:///c:/GitHub/my-lisp-panini/panini/machine/tests.my).

## How to Run Tests
Once the My Lisp VM is bootstrapped, you can run the test suite by loading the environment and executing `(run-tests)`. 

A typical REPL session will look like this:
```lisp
> (load "panini/machine/compiler.my")
> (load "panini/machine/meta.my")
> (load "panini/machine/rules.my")
> (load "panini/machine/tests.my")
> (run-tests)
```

## Test Structure
The test suite utilizes a simple `assert-equal` function to validate state transitions.

### 1. Unit Tests (Phonology/Morphology)
We test individual helper functions to ensure rules like *Guṇa* and *Sandhi* operate correctly on phonemes:
- `test-eco-sandhi`: Validates Rule 6.1.78 (e/o/ai/au + vowel -> ay/av/āy/āv)
- `test-guna`: Validates Rule 1.1.2 mapping (i -> e, u -> o, ṛ -> ar)

### 2. Integration Tests (Derivation Traces)
These tests validate the **Inference Engine** by executing a full derivation (Prakriyā) and verifying the final string output.
- `test-bavati-derivation`: Checks if `BU + Sap + tip` successfully compiles into `Bavati` using the dynamic rule resolution and context inheritance.
- `test-dadati-derivation`: (Upcoming) Will verify conflict resolution where Class 3 reduplication (*Ślu*) correctly blocks the general *Śap* vikarana via *apavāda* (exception).

## Adding New Tests
When a new Paninian rule is added to the DSL (via `def-panini-rule`), you should:
1. Add a unit test if it involves a new phonological operation.
2. Add a full derivation trace (Integration Test) for a word that exercises the new rule.
