# paribhāṣā: The Meta-Rules of Pāṇini's Grammar

## English
This document establishes the formal epistemology of the **paribhāṣā** system in Pāṇini's grammar — the traditional apparatus of "rules about rules" governing how object-level rules are read, interpreted, and applied, including its conflict-resolution hierarchy and the principle of extended identity (*sthānivad-bhāva*). It strictly separates the traditional source material from computational hypotheses.

## Українська
Цей документ встановлює формальну епістемологію системи **paribhāṣā** у граматиці Паніні — традиційного апарату "правил про правила", що визначає, як тлумачити та застосовувати об'єктні правила, включно з ієрархією вирішення конфліктів та принципом розширеної ідентичності (*sthānivad-bhāva*). Він строго відокремлює традиційне джерельне знання від обчислювальних гіпотез.

## Deutsch
Dieses Dokument begründet die formale Epistemologie des **paribhāṣā**-Systems in Pāṇinis Grammatik — des traditionellen Apparats von "Regeln über Regeln", der festlegt, wie objektstufige Regeln gelesen, interpretiert und angewendet werden, einschließlich der Konfliktlösungshierarchie und des Prinzips der erweiterten Identität (*sthānivad-bhāva*). Es trennt strikt das traditionelle Quellenmaterial von rechnergestützten Hypothesen.

---

## [PANINI]

**Source Anchor:** Aṣṭādhyāyī 1.4.2 (vipratiṣedhe paraṃ kāryam), 1.1.56 (sthānivad ādeśo 'nalvidhau), 1.1.68 (svaṃ rūpaṃ śabdasyāśabdasaṃjñā); traditional systematization in the *Paribhāṣenduśekhara* of Nāgeśabhaṭṭa.

In the Aṣṭādhyāyī, `paribhāṣā` refers to a "rule about rules." Unlike object-level rules (`vidhi-sūtra`) that directly describe operations on the language (replacing sounds, adding suffixes), a `paribhāṣā` describes **how to read, interpret, and apply** those object-level rules. Pāṇini embeds some of these meta-rules directly within the Aṣṭādhyāyī; others are implicit conventions deduced from his practice and later systematized by commentators — most notably in the *Paribhāṣenduśekhara* by Nāgeśabhaṭṭa.

### Types of Paribhāṣā

A common traditional classification identifies four functional types of meta-rules:
1. **saṃjñā-paribhāṣā**: Rules defining how technical terms operate (e.g., how to interpret a term when it appears in a sūtra).
2. **vidhi-paribhāṣā**: Rules governing the conditions under which operational rules are applied.
3. **niyama-paribhāṣā**: Rules that restrict the application of other rules.
4. **adhikāra-paribhāṣā**: Rules defining the scope or domain of influence for a section of the grammar.

*(Note: This four-way functional classification of paribhāṣās is distinct from the classification of sūtras themselves into vidhi (operation), niyama (restriction), atideśa (extension), and paribhāṣā (meta-rule) — the latter classifies sūtra *types*, the former classifies what a paribhāṣā *does*.)*

### Key Principles of Conflict Resolution

When two rules are simultaneously applicable to the same linguistic context, a conflict (`vipratiṣedha`) arises. The tradition establishes a strict hierarchy to resolve such conflicts, applied in the following order:

1. **antaraṅga > bahiraṅga**: An "internal" rule (*antaraṅga*) prevails over an "external" rule (*bahiraṅga*). An internal rule relies on conditions closer to the core or more immediate; an external rule depends on a wider, outer context.
2. **nitya > anitya**: A "constant"/"obligatory" rule (*nitya*) prevails over a "non-constant" one (*anitya*). A rule is *nitya* if its conditions would still be met even if the competing rule were applied first.
3. **apavāda > utsarga**: An exception (*apavāda*, a rule with a narrow, specific scope) always overrules a general rule (*utsarga*), regardless of their physical order in the text.
4. **vipratiṣedhe paraṃ kāryam (1.4.2)**: "In case of a conflict [between rules of equal force], the operation [enjoined by the rule] which comes later [in the Aṣṭādhyāyī] is to be performed." This is the ultimate fallback, applied **only** when the conflicting rules are *tulyabala* (of equal strength) — i.e. when none of the three preceding principles resolve the tie.

### The Principle of Extended Identity (sthānivad-bhāva)

Another critical paribhāṣā is **1.1.56 sthānivad ādeśo 'nalvidhau**: "A substitute (*ādeśa*) behaves like the original (*sthānin*), except concerning rules based on a specific sound (*al-vidhi*)." This ensures continuity in the derivation: when one element replaces another, subsequent rules still recognize the grammatical properties of the original element, preserving the derivational context — but the *analvidhau* exception means this inheritance is explicitly **not** unconditional; rules keyed to the specific phonetic shape of the substitute do not look through to the original.

### Relation to saṃjñā (cross-reference)

`saṃjñā-paribhāṣā` governs how a technical term, once established, is to be read wherever it recurs — this is the same mechanism documented from the saṃjñā side in `panini/sastra/samjna.md` (notably sūtra 1.1.68, cited there as the rule protecting a technical term from being read as an ordinary word). The two documents describe the same phenomenon from complementary angles: `samjna.md` from the side of the definition, this document from the side of the meta-rule that governs its reuse.

## [SCHOLARLY INTERPRETATION]

Modern Indological and linguistic scholarship treats `paribhāṣā` as the primary evidence that the Aṣṭādhyāyī is a self-describing, two-level system rather than a flat list of instructions.

- **Kielhorn's edition of the *Paribhāṣenduśekhara*** (F. Kielhorn, late 19th century) remains the standard reference point for the traditional paribhāṣā corpus in Western Indology; it establishes that the paribhāṣās were never fully enumerated by Pāṇini himself but were extracted and systematized by later grammarians from his actual rule-application practice — meaning some paribhāṣās are themselves interpretive reconstructions, not sūtra text.
- **Cardona** (in his survey work on Pāṇini) discusses `vipratiṣedha` and the antaraṅga/bahiraṅga and apavāda/utsarga principles as the grammar's own account of rule ordering, and notes that commentators disagree in specific cases about which principle should be invoked first — the hierarchy is traditionally agreed upon in the abstract, but its application to a given derivation is sometimes itself a matter of scholarly dispute.
- **Paul Kiparsky's "Elsewhere Condition"** (proposed in generative phonology, 1973) is widely credited by Kiparsky himself as directly inspired by the Pāṇinian `apavāda > utsarga` principle — a specific rule blocks a general one wherever both could apply. This is a documented case of a Pāṇinian paribhāṣā being explicitly imported into modern linguistic theory as a claimed language universal, not merely compared to it after the fact.
- Scholarship is divided on whether the four-principle conflict hierarchy given above is a strict, context-free priority ordering or whether its principles interact in more context-sensitive ways in specific derivations — the traditional commentarial literature (Kāśikā, Mahābhāṣya) records disputed applications, which is itself scholarly evidence that the hierarchy is not always mechanically decidable from the sūtra text alone.

## [COMPUTATIONAL INTERPRETATION]

Formally, the paribhāṣā system corresponds to a **meta-level control layer** that governs how a base rule set is interpreted and dispatched, rather than to any rule in the base set itself.

- **Rule-selection / conflict resolution:** When multiple object-level rules match the same state, a dedicated resolution procedure — not the rules themselves — decides which one fires. This is structurally the same problem production-rule systems (e.g. the Rete-algorithm family: OPS5, CLIPS) address with an explicit "conflict resolution strategy" (specificity, recency, refraction), independently of the domain rules being matched.
- **Specificity ordering:** The `apavāda > utsarga` principle — a narrower rule overrides a broader one regardless of textual order — is structurally analogous to most-specific-rule-wins resolution found in object-oriented method dispatch, CSS specificity, and default-logic systems, where a more specific applicable clause pre-empts a general default.
- **Total ordering as tie-breaker:** The `vipratiṣedhe paraṃ kāryam` fallback requires a stable total order over the rule set (textual position in the Aṣṭādhyāyī) to break ties that specificity and other criteria leave unresolved — comparable to using declaration order as the last-resort disambiguator in a rule engine once semantic priority criteria are exhausted.
- **Conditional property inheritance:** `sthānivad-bhāva`'s substitute-inherits-properties-of-original mechanism, with its explicit *analvidhau* carve-out, resembles a type system's inheritance-with-override: a derived entity inherits the properties of what it replaces except along the specific axis where an overriding, narrower rule applies.
- **Meta-rules as a separate evaluation pass:** Because `saṃjñā-paribhāṣā` governs how a technical term is expanded wherever it recurs (cf. `samjna.md`'s [COMPUTATIONAL INTERPRETATION] on binding/macro-expansion), and `vidhi`/`niyama`/`adhikāra`-paribhāṣā govern the *conditions* under which base rules apply, the system as a whole separates a "what the rules mean" evaluation pass from a "which rule actually fires" evaluation pass — two passes that operate on different objects (terms vs. whole rules) but both sit above the object-rule layer.

## [MY-LISP HYPOTHESIS]

These are explicit, unverified hypotheses about how the paribhāṣā mechanism might map onto the my-lisp `(symbol value proof)` architecture. They are not settled facts, and per this repo's Foundation Independence Test, none of them may be read back into the `[PANINI]` layer above. A more detailed, earlier-drafted set of candidate formalizations already exists at `panini/hypotheses/paribhasha-machine-model.md` (H1–H4); the hypotheses below restate and organize that material rather than duplicating it in full — see that file for the candidate `resolve-conflict` pseudocode and the sūtra-ID comparison sketch.

- **Hypothesis 1 (Meta-rule dispatch layer, separate from object rules):** The engine could implement paribhāṣās as a distinct dispatch/meta layer sitting above a declarative table of object rules, rather than as rules in the same table — see `paribhasha-machine-model.md` H1 for a `defmacro`-flavored sketch of this split. Open question: whether this two-layer separation is itself forced by the source material, or a convenience the architecture is choosing to impose.
- **Hypothesis 2 (Conflict hierarchy as an ordered predicate chain):** The four-principle hierarchy (antaraṅga>bahiraṅga, nitya>anitya, apavāda>utsarga, vipratiṣedhe paraṃ kāryam) could be encoded as an ordered chain of predicates in a `resolve-conflict` procedure, tried in strict priority order with the sūtra-position comparison as final fallback — see `paribhasha-machine-model.md` H2–H3 for a candidate implementation and the `later-in-ashtadhyayi?` comparison it depends on. This assumes the hierarchy is context-free and strictly ordered, which §[SCHOLARLY INTERPRETATION] above flags as disputed in specific derivations — if that dispute reflects a real context-sensitivity in the source system rather than commentarial disagreement about a fixed rule, a flat ordered-predicate-chain model would be an oversimplification, not just an implementation detail to fix later.
- **Hypothesis 3 (sthānivad-bhāva as filtered proof-continuity, not blanket copying):** In a Proof-Carrying Derivation, when an *ādeśa* replaces a *sthānin* under 1.1.56, the new derivation-state node's proof graph might inherit references to the properties/proofs attached to the replaced node — but only for the subset of properties not excluded by the *analvidhau* clause. This must be modeled as filtered, partial inheritance keyed to rule type (al-vidhi vs. non-al-vidhi), not as unconditional copy-forward of the prior node's proof.
- **Hypothesis 4 (Stable total order as a structural precondition, not an afterthought):** If Hypothesis 2's fallback tie-breaker is adopted, every object rule in the registry must carry a stable, comparable identifier (its full numeric Aṣṭādhyāyī ID) from the moment it is entered into the system — this is a precondition for the vipratiṣedha fallback to be implementable at all, not an incidental data-quality nice-to-have.
