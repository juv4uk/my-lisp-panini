# Machine Models for Terminology

## Hypothesis: SLP1 as Canonical Identifiers

This document outlines the provisional machine representation of terminology within the My Lisp/VM ecosystem.

### H1: Canonical Text Encodings
In a computational environment, processing Sanskrit strings requires a strict, bijective, and 1-byte-per-character ASCII encoding to guarantee performance and simplicity (avoiding Unicode normalization hell, surrogate pairs, and multi-byte parsing in the core engine). 

**SLP1** (Sanskrit Library Phonetic Basic) is chosen as the canonical machine representation for all identifiers, strings, and symbols in the inference engine.

```lisp
;; Good: A symbol in SLP1
(def dhatu-pac 'pac)

;; Bad: A symbol in Unicode (Devanagari)
;; (def dhatu-pac 'पच्)
```

### H2: The Presentation Layer
IAST and Devanāgarī representations are strictly relegated to the **presentation layer** (UI, logging, debugging outputs, documentation). The core engine operates exclusively on SLP1.

```lisp
;; The machine converts to display formats only at the boundary
(defn display-dhatu (dhatu-id)
  (let [slp1-str (symbol-name dhatu-id)]
    (println "IAST:" (slp1-to-iast slp1-str))
    (println "Devanagari:" (slp1-to-devanagari slp1-str))))
```

### H3: The Dangers of String Typographical Errors
Because SLP1 uses case-sensitivity to distinguish phonemes (e.g., `s` is dental *s*, `S` is palatal *ś*, `z` is retroflex *ṣ*), hardcoding strings everywhere is dangerous.

The terminology tables should be loaded at engine boot time and compiled into a set of global constants or a keyword registry to prevent runtime typographical errors.

```lisp
;; Compiling the terminology into Lisp keywords
:varRa
:pada
:vAkya
:dhAtu
```
Any mismatch (e.g., typing `:varNa` with a capital N instead of `:varRa`) will fail fast at compile time rather than causing subtle derivation failures at runtime.
