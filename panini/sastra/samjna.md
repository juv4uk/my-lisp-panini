# saMjYA · saṃjñā: Technical Terms in Pāṇini's Grammar

## English
This document establishes the formal epistemology of the **saṃjñā** system in Pāṇini's grammar. It strictly separates the traditional source material from computational hypotheses.

## Українська
Цей документ встановлює формальну епістемологію системи **saṃjñā** у граматиці Паніні. Він строго відокремлює традиційне джерельне знання від обчислювальних гіпотез.

## Deutsch
Dieses Dokument begründet die formale Epistemologie des **saṃjñā**-Systems in Pāṇinis Grammatik. Es trennt strikt das traditionelle Quellenmaterial von rechnergestützten Hypothesen.

---

## [PANINI]

**Source Anchor:** Aṣṭādhyāyī 1.1.68, 1.4.1–1.4.110.

In the Pāṇinian system, a `saṃjñā` is a technical designation (name or label) assigned to a specific grammatical entity, class of entities, or operation.

### Key Principles

1. **Definition by Equation (saṃjñā-sūtra):** A term is assigned to a class without operational verbs. 
   - *Example (1.1.1 vṛddhir ādaic):* The phonemes `ā`, `ai`, `au` are designated by the term `vṛddhi`.
   - *Example (1.1.2 adeṅ guṇaḥ):* The phonemes `a`, `e`, `o` are designated by the term `guṇa`.

2. **Non-operational Nature:** A saṃjñā-sūtra itself does not trigger any grammatical derivation or transformation. It only establishes the binding between a name (`saṃjñā`) and its referent (`saṃjñin`).

3. **Protection from Literal Interpretation:** 
   - **Sūtra 1.1.68 (svaṃ rūpaṃ śabdasyāśabdasaṃjñā):** "A word's own form [denotes itself], except when it is a non-verbal saṃjñā."
   - This ensures that when a technical term is used in subsequent rules, it refers to its defined class, not its phonetic shape or everyday lexical meaning.

4. **Scoping and Conflict Resolution (adhikāra):**
   - **Sūtra 1.4.1 (ākāḍārād ekā saṃjñā):** "Up to [the word] *kāḍāra* [in rule 2.2.38], only one designation [applies]."
   - When multiple terms in this section apply simultaneously to the same entity, only one takes effect (governed by specific conflict rules, usually the later rule). This section notably includes the definitions of all `kāraka` roles.

## [SCHOLARLY INTERPRETATION]

Modern linguistic and Indological scholarship (e.g., Cardona, Kiparsky) views `saṃjñā` as the cornerstone of Pāṇini's metalinguistic architecture. 

- **Artificial vs. Meaningful Terms:** Pāṇini uses both highly artificial, algebraic terms (like `ṭi`, `ghu`, `bha`) and terms drawn from conventional Sanskrit (like `kāraka`, `samāsa`, `sarvanāman`). However, rule 1.1.68 ensures that even conventional words, when established as saṃjñās, function purely as technical class labels.
- **Economy (lāghava):** The primary motivation for the saṃjñā system is brevity. By assigning a short label to a large set or complex condition, subsequent operational rules (vidhi-sūtras) can be stated with extreme conciseness.
- **Taxonomy:** The `ākāḍārād ekā saṃjñā` block (1.4.1–2.2.38) creates a strict taxonomy where certain grammatical properties are mutually exclusive.

## [COMPUTATIONAL INTERPRETATION]

Formally, a saṃjñā-sūtra acts as a **Type Definition**, **Macro**, or **Binding**. 

- **Environment Binding:** In an abstract computational model, applying a saṃjñā-sūtra modifies the global or local environment by introducing a new symbol that evaluates to a specific set of entities or structural conditions.
- **Evaluation Strategy:** When the engine encounters a rule containing a saṃjñā, it must expand or evaluate that symbol against the environment rather than treating it as a literal string token (mirroring rule 1.1.68).
- **Mutual Exclusion (Tags/Enums):** The `ākāḍārād` block behaves like a strongly typed Enum or a set of mutually exclusive tags. An entity can hold various properties, but within this specific domain, assigning a new tag overwrites or preempts others based on priority rules.

## [MY-LISP HYPOTHESIS]

Could the `saṃjñā` mechanism be the direct equivalent of `(define ...)` or variable binding in a Lisp-like environment?

- **Hypothesis 1 (Symbolic Tagging):** We can implement `saṃjñā` as semantic tags attached to the derivation state. When a token enters the system, a set of saṃjñā-sūtras runs as pattern-matching predicates, tagging the token (e.g., `[TAG: ghu]`).
- **Hypothesis 2 (Proof-Carrying Context):** In our `(symbol value proof)` architecture, when a token is identified as `guṇa`, the proof graph must trace back not just to the operational rule, but to the specific `saṃjñā-sūtra` (1.1.2) that authorized this classification.
- **Hypothesis 3 (Conflict Engine):** The `ākāḍārād ekā saṃjñā` block suggests that our My Lisp inference engine needs a dedicated subsystem for resolving tag conflicts, rather than just sequential execution.
