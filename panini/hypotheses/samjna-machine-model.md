# Machine Models for saṃjñā

## Hypothesis: saṃjñā as a Lexical Tag or Typedef

This document explores computational analogies for the **saṃjñā** system in Pāṇini's grammar. These are explicitly marked as *hypotheses* for machine representation, not historical claims about Pāṇini's intent.

### H1: The `typedef` or `#define` Macro Analogy

In many modern computational implementations (and observed by researchers like Cardona), the `saṃjñā` layer of the grammar functions analogously to a `typedef` in C, or a macro `#define`.

**The Mechanism:**
- A base entity or set of entities (e.g., the sounds `ā`, `ai`, `au`) exists.
- A `saṃjñā` rule binds a specific identifier (e.g., `vṛddhi`) to this set.
- Subsequent operational rules (`vidhi`) use the identifier `vṛddhi` as a compact reference.

**Computational Strengths of this Model:**
- **Compression:** It reduces the length of operational rules, similar to how macros reduce code repetition.
- **Indirection:** Changing the definition of a `saṃjñā` automatically updates all rules that depend on it, without rewriting the operational rules.

### H2: The Semantic Tag or Interface Analogy

While `vṛddhi` and `guṇa` behave like simple aliases for sets of characters (like an enum or an array of chars), other `saṃjñā`s act more like semantic tags or interfaces.

For instance, `ghu` (assigned to roots `dā` and `dhā`, with exceptions) or `sarvanāma` (pronominals) do not just alias characters, but group disparate lexical items that share a common morphological behavior. 

**The Mechanism:**
- In an AST or a semantic graph, `saṃjñā` acts as a tag applied to a node.
- `Root("dā") -> implements -> Tag("ghu")`
- Operational rules pattern-match on these tags during derivation: `if node.hasTag("ghu") then apply_rule()`.

### H3: Scope and Override (The 1.4.1 Conflict)

Pāṇini's rule 1.4.1 (*ākāḍārād ekā saṃjñā*) limits the application to a single `saṃjñā` when multiple might apply in a specific domain (like *kāraka*).

**The Mechanism:**
- This is functionally equivalent to conflict resolution in class inheritance (e.g., method resolution order) or CSS specificity.
- When two mutually exclusive semantic tags (e.g., *apādāna* and *karman*) can be assigned to the same graph node, the engine must consult a priority table (dictated by rule ordering or specificity) to assign only one active `saṃjñā`.

### Conclusion for My Lisp / VM

The `saṃjñā` mechanism is not a single construct in modern CS terms, but spans several:
1. Alias / Macro (for simple sets like `vṛddhi`).
2. Semantic Tag / Trait / Interface (for behavioral classes like `ghu`).
3. State Label / Role (for syntactic positions like *kāraka*).

When implementing the `panini-foundation` in Lisp or FPGA, the IR should likely represent `saṃjñā` as a general *tagging* mechanism on the derivation state, where rules act as conditional triggers watching for specific tags.
