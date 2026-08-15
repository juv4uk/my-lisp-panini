# it (anubandha): Metalinguistic Markers and Control Flow

## English
This document establishes the formal epistemology of the **it** (or *anubandha*) system in Pāṇini's grammar. It strictly separates the traditional source material from computational hypotheses.

## Українська
Цей документ встановлює формальну епістемологію системи **it** (*anubandha*) у граматиці Паніні. Він строго відокремлює традиційне джерельне знання від обчислювальних гіпотез.

## Deutsch
Dieses Dokument begründet die formale Epistemologie des **it**- (*anubandha*)-Systems in Pāṇinis Grammatik. Es trennt strikt das traditionelle Quellenmaterial von rechnergestützten Hypothesen.

---

## [PANINI]

**Source Anchor:** Aṣṭādhyāyī 1.3.2–1.3.9.

`it` (इत्, literally "this [sound]"), also known in the later commentarial tradition as *anubandha*, is a metalinguistic sound attached to elements in the formal grammar (e.g., in the *Dhātupāṭha* or within a *pratyaya*). Crucially, an `it` marker never appears in the final spoken word, but its presence dictates how subsequent operational rules are applied.

### Key Principles

1. **Identification of markers (1.3.2–1.3.8):** 
   - A precise set of rules defines exactly which sounds in which positions are considered `it`.
   - *Example (1.3.2 upadeśe 'janunāsika it):* A nasalized vowel in the original enunciation (upadeśa) is an `it`.
   - *Example (1.3.3 halantyam):* A final consonant (in an upadeśa) is an `it`.

2. **Deletion (1.3.9 tasya lopaḥ):**
   - The operational rule "its elision" universally deletes all `it` sounds. They do not surface in the final output.

3. **Heterogeneity of Effects:**
   - There are dozens of specific `it` sounds, each governing distinct grammatical effects.
   - **Ṇit** (*ṇ*-marker): Blocks *guṇa* and *vṛddhi* strengthening; triggers *samprasāraṇa* (6.1.15).
   - **Ñit** (*ñ*-marker): Causes *vṛddhi* (7.2.115); when on a *dhātu*, allows both active and middle endings (*ubhayapada*, 1.3.72).
   - **pit** (*p*-marker): Indicates grave (*anudātta*) accent (3.1.4); explicitly allows *guṇa*/*vṛddhi* for *sārvadhātuka* affixes.

## [SCHOLARLY INTERPRETATION]

Modern linguistic scholarship (Cardona, Kiparsky, Sharma) views the `it` system as a sophisticated device for categorizing roots and affixes into intersective classes without creating separate lists.

- **Marker vs. Marked:** The tradition strictly distinguishes between the marker (*anubandha*) and the item to which it is attached (*anubandhin*). 
- **Algorithmic Control Flow:** The markers serve as control instructions for the derivation process. They trigger or block specific phonological and morphological operations.
- **Economy (lāghava):** By embedding these instructions directly into the abstract underlying forms, Pāṇini avoids verbose conditional statements in the operational rules.

## [COMPUTATIONAL INTERPRETATION]

Formally, an `it` marker acts as **Metadata**, an **Annotation**, or a **Compiler Directive**.

- **Ephemeral State:** The `it` marker represents data that is crucial during the derivation phase (compile-time) but must be stripped out before the final output generation (runtime). This is analogous to type erasure in generics, or non-emitting macros.
- **Multi-phase Evaluation:** The system requires a distinct lifecycle:
  1. *Lexical Phase:* Identification of markers attached to a token.
  2. *Derivation Phase:* Execution of rules conditional on the presence/absence of these markers.
  3. *Emission Phase:* `tasya lopaḥ` corresponds to the final flattening/emission where annotations are stripped.
- **Property Bags:** An entity with an `it` marker can be modeled as a record or object carrying boolean flags or property bags (e.g., `{ base: "grah", properties: ["Ṇit"] }`).

## [MY-LISP HYPOTHESIS]

How can My Lisp model the `it` system to support Proof-Carrying Derivations?

- **Hypothesis 1 (Symbolic Metadata):** In My Lisp, `it` markers can be implemented as Lisp property lists (plists) or attributes attached to a symbol: `(put 'grah 'it-marker 'ṇ)`. The operational rules check these properties via predicates like `(has-it-p token 'ṇ)`.
- **Hypothesis 2 (Evaluation Lifecycle):** We can implement a specialized derivation engine where `tasya lopaḥ` is not a sequential rule that destroys data prematurely, but rather a final `(emit form)` function that strips all properties to yield a pure string.
- **Hypothesis 3 (Proof Tracing):** In a Proof-Carrying Derivation `(symbol value proof)`, if a rule applies because a token is `Ṇit`, the proof graph must reference the original presence of the `ṇ` marker. If `tasya lopaḥ` truly erased the `ṇ` from memory midway through the derivation, the proof engine would lose the provenance. Thus, `it` markers must persist in the *derivation state* even if they are elided from the *surface form*.
