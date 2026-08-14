# Vidyut Source Code Audit

*Target: Ambuda's `vidyut-prakriya` Rust crate.*

Vidyut is an active open-source Sanskrit processing toolkit built in Rust by Ambuda. This audit focuses on `vidyut-prakriya`, the specific crate responsible for generating Sanskrit words according to Paninian rules. The goal is to evaluate its architecture, identify what maps directly to Panini, and determine what we can reuse or should discard for `my-lisp`.

## What Vidyut Models
Vidyut aims to be a complete morphophonological generator for Sanskrit. It models:
- The base terms (`dhātu`, `prātipadika`, `pratyaya`).
- The derivation state (a linear array of terms).
- A large subset of the `Aṣṭādhyāyī` rules, implemented as imperative transformations.
- The traditional rule application domains (`Tripādī`, `Aṅgādhikāra`).
- Conflict resolution using ad-hoc procedural ordering.

## How it Models It
Vidyut uses a strictly procedural, linear data structure written in Rust.

1. **Derivation State (`Prakriya`)**:
   The derivation is not a tree or a graph; it is a flat `Vec<Term>`, representing a linear string of components (e.g., `[Upasarga, Dhatu, Vikarana, Tin]`). 
   It stores metadata like semantic conditions (`artha`), configuration flags, and a history of applied rules (`Vec<Step>`).

2. **Term Representation (`Term`)**:
   A `Term` represents a single morpheme. It contains:
   - `u` (Aupadeshika): The underlying theoretical form with `it` markers (e.g., `qukf\Y`).
   - `text`: The current surface form (e.g., `kar`).
   - `tags`: A bitset (`EnumSet<Tag>`) representing assigned `saṃjñā`s (e.g., `Tag::Ardhadhatuka`, `Tag::Dhatu`).
   - `morph`: A Rust enum distinguishing `Dhatu`, `Krt`, `Tin`, `Sup`, etc.

3. **Rule Representation & Application (`Rule` and Functions)**:
   Rules are represented merely as enum labels (e.g., `Rule::Ashtadhyayi("7.1.5")`).
   They are applied via hardcoded Rust logic inside sequence functions like `run_main_rules`.
   Example:
   ```rust
   if base.is_abhyasta() {
       // juhvati
       p.run_at("7.1.4", i, |t| t.set_adi("at"));
   }
   ```
   If the condition is met, the string is mutated in place. Rule ordering is achieved strictly by the order in which these Rust functions are called, simulating Panini's rule priority manually.

4. **`dhātu` and `pratyaya`**:
   Roots and suffixes are bootstrapped from traditional lists (`Dhatupatha`), parsed into strings, and mutated.

## What Corresponds Directly to Pāṇini
- **`u` vs `text` distinction**: Directly maps to `upadeśa` vs `sthānin/ādeśa`.
- **`Tag` enum**: Directly models `saṃjñā` (designations like `Aṅga`, `Bha`, `Pada`, `Sārvadhātuka`).
- **`Rule` IDs**: Maintain 1:1 traceability back to the `Aṣṭādhyāyī`.

## What is Implementation Machinery (Not Pāṇini)
- **Procedural Sequence Control**: Pāṇini's rules operate concurrently in a conflict-driven resolution network (`vipratiṣedha`, `apavāda`). Vidyut uses linear, imperative Rust function calls (`run_before_stritva(); try_iw_agama(); dvitva::run();`) which artificially forces sequential evaluation.
- **Flat Array (`Vec<Term>`)**: Pāṇini's derivation often requires a hierarchical or semantic graph understanding of relations (e.g., for `kāraka` roles). The flat array is a simplistic string-builder pattern.
- **Rule Definitions**: Rules are embedded inside `if/else` Rust blocks rather than existing as independent, queryable axioms.

## What We Could Reuse
- **Data Sets**: The pre-parsed `Dhatupatha` lists, `Gana` classifications, and mappings of `it` markers (e.g., knowing that `qukf\Y` is `Bhvadi` and has `qu` and `\Y` as `it`s).
- **SLP1 String manipulation edge-cases**: Useful reference for tricky sandhi implementations.
- **Traceability logic**: The idea of recording a `History` of applied rules to produce a proof of derivation (`Step`).

## What We Should NOT Reuse
- **Procedural Rule Engine**: For `my-lisp` and Symbolic AI, rules must be independent data structures (axioms) evaluated by an Inference VM, not hardcoded `if/else` Rust macros.
- **Flat State (`Vec<Term>`)**: We need a semantic directed graph where `dhātu` connects to `kāraka` via explicit roles, not just a string builder array.
- **State Mutation (`set_adi("at")`)**: Rather than mutating strings in place, our derivation should ideally be a purely functional trace (a graph transition sequence) suitable for logical verification or backwards-inference.
