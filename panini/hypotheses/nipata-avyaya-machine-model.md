# Machine Models for nipāta and avyaya

## Hypothesis: The Non-Productive Lexicon and Contextual Tagging

This document outlines the provisional machine representation of undeclinables (`avyaya`) and particles (`nipāta`/`upasarga`) within the My Lisp/VM ecosystem.

### H1: The Non-Productive Core vs. The Productive Core
In the Lisp ecosystem, `dhātu` (roots) and `prātipadika` (stems) represent the *productive* core of the language. They act as base nodes that accept `pratyaya` (affixes) to generate an infinite number of derived forms. 

By contrast, `nipāta` and `avyaya` are a closed, *non-productive* lexical class. They are emitted into the final syntax tree "as-is". 

A machine model must not flatten all semantic tokens into a single generic `Token` or `Word` class, as that erases this fundamental architectural boundary.

```lisp
;; Good: Distinguishing productive from non-productive bases
(deftype dhatu ...)
(deftype pratipadika ...)
(deftype avyaya ...)       ;; Represents an immutable terminal node

;; Bad: Flattening everything
;; (deftype token (value)) 
```

### H2: Context-Dependent Tagging (`nipāta` vs `upasarga`)

The fact that the same list of words (`prādi` list: *pra*, *apa*, *sam*, etc.) receives the designation `nipāta` when used alone, but `upasarga` when bound to a verb, is a profound architectural hint.

It suggests that in the Knowledge Graph or AST, these items are **not** strictly typed at birth. Instead, their type (`saṃjñā`) is a **contextual property** assigned during parsing or graph assembly. 

```lisp
;; A word from the prAdi list
(def pra-token (make-lexical-item :value 'pra))

;; During AST construction, the engine applies contextual tags
(defn assign-role (token context-node)
  (if (is-verb? context-node)
      (add-tag token :upasarga)
      (add-tag token :nipAta)))
```

This implies a dynamic, tag-based type system rather than rigid OOP-style inheritance, perfectly aligning with symbolic AI paradigms.
