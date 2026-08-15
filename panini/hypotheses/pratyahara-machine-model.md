# Machine Models for pratyāhāra

## Epistemic Dependencies (imported from `juv4uk/shiva-sutras`)

> Розділ hypotheses — шар `[MY-LISP HYPOTHESIS]`/`[COMPUTATIONAL INTERPRETATION]`. Фундаментальні факти про Śiva-sūtras, механіку pratyāhāra та математичні властивості моделі імпортуються з upstream і **не** встановлюються тут. Джерело: `panini/coordination/dependencies.yaml`; upstream-реєстр: `shiva-sutras/docs/claims-export.yaml`.

| Imported claim | status_at_import | min_status | revision | Використання тут |
| :--- | :--- | :--- | :--- | :--- |
| `SS-CANON-001` | `resolved` | `supported` | `a8391c4` | Канон 14 сутр у SLP1 (база для bitset) |
| `SS-PRATYAHARA-001` | `supported` | `supported` | `a8391c4` | Механіка `start + it_marker = set` (H1) |
| `SS-MARKERS-001` (M_min=14) | `proved-in-model` | `supported` | `a8391c4` | Обмеження: 14 маркерів, канонічний порядок досягає оптимуму |
| `SS-MARKERS-002` | `proved-in-model` | `supported` | `a8391c4` | Рівно 2 оптимальні класи |
| `SS-MARKERS-003` | `proved-in-model` | `supported` | `a8391c4` | Class B унікальний для безколізійної адресації — основа ISA-аналогії (H2) |
| `SS-ORDER-001` | `proved` (`falsified` як гіпотеза унікальності) | `supported` | `a8391c4` | Забороняє аргумент «порядок унікальний через C1P» |

**Boundary**: `[MY-LISP HYPOTHESIS]` (bitset/ISA/compile-time constant) — локальна інженерна інтерпретація; не є фактом про Паніні. `M_min = 14` доведено лише для 42-класової моделі upstream, не як історичний задум.

---

## Hypothesis: `pratyāhāra` as a Bitset / Computed Constant

This document outlines the provisional machine representation of **pratyāhāra** (compact phoneme sets) within the My Lisp/VM ecosystem. It addresses how the Śiva Sūtras are implemented as a computational data structure.

### H1: The Independence of Mechanism and Implementation

The Aṣṭādhyāyī (1.1.71) defines the *algorithm* for generating a `pratyāhāra`: `start_char` + `it_marker` = `set_of_sounds`. 
Because the Śiva Sūtras are a finite, closed list of 43 phonemes (plus 14 `it` markers), the resulting sets are entirely static. 

In a machine model (especially for an Inference VM or FPGA), it is highly inefficient to dynamically traverse a string or array at runtime every time a rule asks "is `x` in `ac`?". 

Therefore, while the Paninian *mechanism* is algorithmic, the optimal *machine implementation* is to compute these sets at compile-time and represent them as constants—specifically, **bitsets** or hardware registers.

```lisp
;; My-Lisp Hypothesis: Compile-time generation
(def-pratyahara ac '(a i u f x e o E O))

;; Under the hood, this compiles to a 64-bit integer mask
;; where bits 0-8 are set.
;; Checking if a phoneme is in 'ac' becomes a single bitwise AND.
(if (bitwise-and (phoneme-mask next-char) MASK_AC)
    (apply-sandhi)
    ...)
```

### H2: The Śiva Sūtras as an ISA (Instruction Set Architecture)

The Śiva Sūtras are ingeniously ordered so that naturally co-occurring classes of sounds (vowels, semivowels, nasals, stops by voicing/aspiration, sibilants) form contiguous blocks. 
This ordering allows almost any phonological rule in the grammar to reference exactly the needed subset of sounds using just two characters (e.g., `ac`, `hal`, `jhal`, `yaṇ`).

In a hardware (FPGA) context, this sequence maps perfectly to a bit-vector. The Śiva Sūtras can be viewed as the foundational **Instruction Set Architecture (ISA) mapping** for the phonetic processor.

### Open Questions for Implementation
1. **The `h` Anomaly**: The phoneme `h` appears twice in the Śiva Sūtras (in line 5 `h y v r [ṭ]` and line 14 `h [l]`). How does the bitset model handle this duplication? Do we assign `h` two different bits, or does the compiler map both logical positions to the same physical bit?
2. **Dynamic Generation vs. Hardcoded Registry**: Should the Lisp engine include a function `(generate-pratyahara "ac")` that reads a string representation of the Śiva Sūtras and generates the list, or should we just hardcode the 41 traditionally recognized `pratyāhāra` sets as constants in the VM registry? (Hardcoding is faster, but dynamic generation proves the algorithm works).
