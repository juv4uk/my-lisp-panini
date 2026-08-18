# Śiva Sūtras та Pratyāhāra · Śiva Sūtras and Pratyāhāra · Śiva Sūtras und Pratyāhāra

## Epistemic Dependencies (imported from `juv4uk/shiva-sutras`)

> Канон 14 сутр і механіка pratyāhāra імпортуються з upstream; наведений нижче список у SLP1 — спожите подання, а не повторне встановлення фактів. Джерело: `panini/coordination/dependencies.yaml`; upstream-реєстр: `shiva-sutras/docs/claims-export.yaml`.

| Imported claim | status_at_import | min_status | revision |
| :--- | :--- | :--- | :--- |
| `SS-CANON-001` | `resolved` | `supported` | `a8391c4` |
| `SS-PRATYAHARA-001` | `supported` | `supported` | `a8391c4` |

**Boundary**: При виявленні розбіжності між цим файлом та upstream-каноном — авторитетним є `SS-CANON-001`; розбіжність фіксується як `[REVALIDATE]`.

---

## English
This document establishes the formal epistemology of the **pratyāhāra** system (compact phonetic sets) and the **Śiva Sūtras**. It separates the textual basis from computational interpretations.

## Українська
Цей документ встановлюється формальну епістемологію системи **pratyāhāra** (компактні множини звуків) та **Śiva Sūtras**. Він відокремлює текстуальну базу від обчислювальних інтерпретацій.

## Deutsch
Dieses Dokument begründet die formale Epistemologie des **pratyāhāra**-Systems (kompakte phonetische Mengen) und der **Śiva Sūtras**. Es trennt die textliche Grundlage von rechnergestützten Interpretationen.

---

## [PANINI]

**Source Anchor:** Śiva Sūtras 1–14, Aṣṭādhyāyī 1.1.71 (ādir antyena sahetā).

Pāṇini begins his grammar with the **Śiva Sūtras** (māheśvara sūtra), which enumerate phonemes in a strictly defined sequence.

### The Canonical Sūtras (`SS-CANON-001`)
The full list in SLP1 notation (bracketed letters are the `it`-markers at the end of each line, not part of the sound set themselves):
```text
 1. a i u [ṇ]
 2. ṛ ḷ [k]
 3. e o [ṅ]
 4. ai au [c]
 5. h y v r [ṭ]
 6. l [ṇ]
 7. ñ m ṅ ṇ n [m]
 8. jh bh [ñ]
 9. gh ḍh dh [ṣ]
10. j b g ḍ d [ś]
11. kh ph ch ṭh th c ṭ t [v]
12. k p [y]
13. ś ṣ s [r]
14. h [l]
```

*(Verified 2026-08-18 against `juv4uk/shiva-sutras`, `ksetra/canon/siva-sutras.yaml`, commit `0f6110d` — byte-level diff of all 14 `text_iast` lines against this table found exactly one discrepancy: line 1's it-marker was capitalized (`Ṇ`) here versus lowercase `ṇ` upstream — fixed per this file's own `[REVALIDATE]` boundary rule, upstream wins. All 13 other lines matched exactly. `PANINI-RECONCILE-SHIVA-SUTRAS-DEPENDENCY`.)*

### The Pratyāhāra Mechanism (`SS-PRATYAHARA-001`)
- **Sūtra 1.1.71 (ādir antyena sahetā):** "The initial [letter] along with the final `it` [forms a designation]".
- The mechanism: The initial letter of any line, combined with the `it`-marker of *any* subsequent line, designates the set of all sounds between them, inclusive (but excluding the `it`-markers themselves).
- **Example:** `ac` (from `a` in line 1 to the `it`-marker `c` in line 4) denotes the set of all vowels: `{a, i, u, ṛ, ḷ, e, o, ai, au}`. `hal` (from `h` in line 5 to the `it`-marker `l` in line 14) denotes all consonants.

## [SCHOLARLY INTERPRETATION]

Modern linguistic scholarship (e.g., Staal, Kiparsky, Petersen) views the Śiva Sūtras as one of the greatest achievements of early phonological feature geometry.

- **Non-traditional Ordering:** Pāṇini intentionally broke the traditional, strictly phonetic Sanskrit alphabet ordering (*varṇasamāmnāya*) to optimize for operational rules. The sequence is arranged so that sounds undergoing similar grammatical operations are grouped together.
- **Maximal Brevity (lāghava):** The arrangement minimizes the number of rules required in the Aṣṭādhyāyī. It is a sorting algorithm designed for maximum descriptive economy.
- **Formal System:** It behaves like a formal algebra. The `pratyāhāra` is a substring extraction operator.
- **Caveat on "optimality" (`SS-ORDER-001`, imported 2026-08-18, `status_at_import: PROVED / FALSIFIED (as uniqueness hypothesis)`, revision `a8391c4`):** the continuity requirement alone (C1P — no it-marker letter needs to appear in more than one contiguous block) does **not** force a unique canonical ordering; `shiva-sutras` found >10,000 valid topologies satisfying C1P for the 42-class model. "Maximal brevity" above is a scholarly characterization of *why* this particular order was likely chosen, not a claim that it's the *only* order satisfying the formal constraint — the two are different claims and must not be conflated. What upstream *has* proved (`SS-MARKERS-001`/`002`/`003`) is narrower: this order achieves the global minimum marker count (`M_min = 14`), only one other structural class ties it, and only this one ("Class B") permits collision-free addressing.

## [COMPUTATIONAL INTERPRETATION]

Formally, a `pratyāhāra` acts as **Set Comprehension**, an **Interval Definition**, or a **Computed Constant**.

- **Substring Extraction:** It is a function `P(start_char, end_marker)` that returns a subset of an ordered array.
- **Immutability:** The Śiva Sūtras are immutable. Therefore, all possible `pratyāhāra` sets can be computed at compile-time as constant sets or hash maps for O(1) membership checking.
- **Equivalence to Regular Expressions:** A `pratyāhāra` like `ac` is computationally equivalent to a character class in a regular expression `[aiuṛḷeoaiau]`.

## [MY-LISP HYPOTHESIS]

How can My Lisp model `pratyāhāra` in a way that respects upstream constraints and supports Proof-Carrying Derivations?

- **Upstream Dependencies:** The `shiva-sutras` repository has proven mathematically that the marker structure is optimal (`SS-MARKERS-001`, `SS-MARKERS-002`) and that "Class B" is unique for collision-free addressing (`SS-MARKERS-003`).
- **Hypothesis 1 (Bitset / ISA Encoding):** Because the addressing is optimal and collision-free, My Lisp can encode the Śiva Sūtras natively as a Bitset or an Instruction Set Architecture (ISA) mask. A phoneme is a binary vector, and checking `ac` membership is a bitwise `AND` operation, resulting in extremely fast execution on an FPGA.
- **Hypothesis 2 (Proof-Carrying Type System):** When a token is checked against `ac`, the evaluation might use the precomputed bitset for speed. However, the resulting proof graph `(symbol value proof)` must trace the `true` evaluation back to the definition `ādir antyena sahetā` and the specific subset `a i u Ṇ ... c`. The phonological check must be tied to the foundational layer, not just an opaque bitwise result.
