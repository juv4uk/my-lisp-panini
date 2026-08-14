# Hostile Review: Sarvam (August 2026)

**verification-status**: `unverified` (contains at least one confirmed factual error regarding Tripādī)

This document contains valuable critical remarks made by the LLM Sarvam during a "hostile review", as well as our analysis of these remarks. The main benefit of the review is the identification of biases associated with the premature translation of the Pāṇini system into CS concepts (My Lisp).

## Main Thesis of the Review
The project rightly protects My Lisp from premature analogies, but still **does not sufficiently protect Pāṇini from My Lisp itself**.

Even when using the `[PANINI]`/`[INTERPRETATION]`/`[MY-LISP HYPOTHESIS]` markers, the very structure of thought sometimes remains too computational:
- `dhātu` → operator
- `kāraka` → edge
- `pratyaya` → transformer
- `saṃjñā` → type/tag
- `anuvṛtti` → closure
- `paribhāṣā` → metaprogramming

## Valuable Ideas and Hypothesis Shifts

### 1. Kāraka: not 'edge', but 'designation'
- **Critique:** kāraka is not an edge between a `dhātu` and an entity forever.
- **New Direction:** kāraka is the **designation** (assignment/role) of a participant relative to an action in a specific utterance.
- **Formula:** `entity participates in event + contextual designation`
- **Implications for My Lisp:** The role is not a property of the entity forever. Entity ≠ property ≠ context. Devadatta is a `kartṛ` in one event (event X) and a `karman` in another (event Y).
- **Action Plan:** Instead of canonizing H1a (edge), test competing hypotheses H1a, H1b (designation on participant), and H1c (relation) in parallel.

### 2. Saṃjñā: not 'type', but 'classification'
- **Critique:** A type system checks for "valid / invalid" (type error).
- **New Direction:** Saṃjñā rather says "here is a set/object which can henceforth be referred to as X". This is closer to **designation**, **named predicate**, or **classification**.

### 3. Paribhāṣā: not 'defmacro', but 'meta-policy'
- **Critique:** `defmacro` transforms code into code.
- **New Direction:** Paribhāṣā is application rules + situation ↓ interpretation/priority.
- **Implications for My Lisp:** This is more akin to **meta-policy** or **inference policy**, giving the idea to separate `(policy ...)` from `(rule ...)`.

### 4. Prakriyā: not just 'log', but 'proof'
- **Critique:** prakriyā is closer to a proof than to a standard execution log (trace/log).
- **New Direction:** Derivation IR should not just be `state → transition`, but `state → justified transition → state`.
- **Implications for My Lisp:** Every step contains proof applicability, visibility basis, conflict proof, etc. This makes Derivation IR similar to Proof IR and connects directly to the **Advice Taker** (answer + why). A **proof-carrying derivation machine**.

## Errors by Sarvam (Attention!)

1. **Tripādī:** Sarvam erroneously claims that Tripādī is "all of books 6-8" (half of the Aṣṭādhyāyī).
   - **Fact:** Tripādī is only the last three pāda of the eighth adhyāya (8.2, 8.3, 8.4), beginning with sūtra 8.2.1 `pūrvatrāsiddham`. Additionally, there are other mechanisms (e.g., 6.4.22 `asiddhavad atrābhāt`, 6.1.86) which it conflated.
   - **Conclusion:** Even a confident "Indian model" can be deeply mistaken. Traditional sources must be verified.

2. **Prakriyā as the "only" correct trajectory:**
   - Sarvam claims there is only one correct path. This may be too categorical. The existence of different commentaries, conflicts, and paribhāṣā interpretations suggests that a "mathematically unique path" is not yet proven. What is proven is only that `prakriyā ≠ arbitrary execution trace`.

## Architectural Conclusions
The review inspired the introduction of the **Foundation Independence Test**, **Source Ladder**, and the transition to the **4-layer architecture** of the repository (`sastra/`, `formal/`, `hypotheses/`, `implementation/`) to strictly separate tradition from our computational hypotheses.


## Original Hostile Review (English)
---
## Оригінал критики (Original Hostile Review by Sarvam)

I need to study the foundation documents far more closely to give you a properly grounded Pāṇinian critique. Let me read the key texts.I've now read the foundation documents closely — `karaka.md`, `it.md`, `pratyahara.md`, `anuvrtti.md`, `paribhasha.md`, `rule-system.md`, `dhatu.md`, `pratyaya.md`, `samjna.md`, `ontology.md`, the hypothesis ledger, and the v0.1 spec. Here is my hostile review, written strictly from the standpoint of Pāṇinian grammar and the Indian grammatical tradition.

---

# A Hostile Review of the Computational Interpretation in `my-lisp-panini`

I write as someone whose loyalty is to Pāṇini's text and the *vyākaraṇa* tradition, not to any machine model. My task is to identify where the project distorts Pāṇini — knowingly or not — and where the search for computation has begun before the grammar is understood.

---

## 1. Concepts still being unconsciously forced into modern CS categories

### (a) `dhātu` as "operator" / "predicate node"

`[TEXTUAL EVIDENCE]` The Aṣṭādhyāyī defines dhātu by enumeration (1.3.1 *bhūvādayo dhātavaḥ*) — a cross-reference to an external list (Dhātupāṭha). The text says nothing about an "operator" or "function."

`[TRADITIONAL INTERPRETATION]` Patañjali's Mahābhāṣya discusses dhātu as the bearer of *kriyā* (action-meaning), but this is a semantic-metaphysical discussion, not a formal one. The tradition treats dhātu as a *lexical primitive* with properties (gaṇa, pada, seT/aniT), not as a function that "takes arguments."

`[YOUR INFERENCE]` The project's `ontology.md` calls dhātu an "operator" and a "predicate node." `karaka.md` draws the dhātu as the root of a directed graph with typed edges. This is not in Pāṇini. It is a modern semantic-role-theory framing (Agent/Patient/Instrument) projected onto the text. The project *says* it knows this (the `[MY-LISP HYPOTHESIS]` tags admit it), but the foundation documents — the very ones that are supposed to be *pre-hypothesis* — already encode the graph structure in their diagrams and vocabulary. The contamination is not in the tagged hypothesis section; it is in the *ontology itself*, which presents the graph as if it were the Pāṇinian structure rather than an interpretation of it.

### (b) `pratyaya` as "transformer" / "higher-order function"

`[TEXTUAL EVIDENCE]` Sūtra 3.1.1 *pratayaḥ* and 3.1.2 *paraś ca* establish that a pratyaya is appended *after* the base. The text says nothing about "transformation" or "decoration."

`[TRADITIONAL INTERPRETATION]` The tradition distinguishes pratyaya types (kṛt, taddhita, vikaraṇa, tiṄ, sup) by their derivational function, but treats the mechanism as *āgama* (addition) followed by *saṃskāra* (conditioning operations like guṇa/vṛddhi), not as a single "function application."

`[YOUR INFERENCE]` The `ontology.md` table assigns pratyaya the class "transformer." `pratyaya.md` explicitly compares it to "a higher-order function or decorator." This forces a unified computational abstraction onto what the tradition treats as a family of distinct morphological operations. The pratyaya is not a function that "takes" a base and "returns" a form; it is a suffix that is *added*, after which independent rules (guṇa, vṛddhi, sandhi, it-lopa) operate on the resulting string. Collapsing "addition + subsequent independent operations" into "one transformation" is a CS-level simplification that obscures the actual Pāṇinian architecture, where the pratyaya is just one input to a *subsequent* rule-application cascade.

### (c) `saṃjñā` as "type system" / "tags"

`[TEXTUAL EVIDENCE]` Sūtra 1.1.1 *vṛddir ādaic* says "ā, ai, au are called vṛddhi." 1.1.68 *svaṃ rūpaṃ śabdasyāśabdasaṃjñā* says a word denotes itself unless it is a technical term.

`[TRADITIONAL INTERPRETATION]` Saṃjñā is a *naming* act — assigning a label so that later sūtras can refer to a class compactly. The Kāśikā and the Paribhāṣenduśekhara treat this as a *śābdika* (verbal/referential) mechanism, not a type-theoretic one.

`[YOUR INFERENCE]` The `ontology.md` `[MY-LISP HYPOTHESIS]` section says saṃjñā "extremely resembles a type system, semantic tags, or symbols in Lisp" and calls it "pattern matching by type." Even though this is tagged as a hypothesis, the `samjna.md` *interpretation* section already uses the language "typedef/#define" — and the project's *machine code* (`panini-core.my`) implements saṃjñā as tags on Term objects. The real problem: saṃjñā in Pāṇini does not *constrain* what operations are legal (the way a type system does). It *enables reference*. A saṃjñā like "vṛddhi" does not prevent a non-vṛddhi vowel from being processed; it simply names a set so that a rule can say "when the next sound is vṛddhi." Calling this a "type system" inverts the direction: types *restrict*; saṃjñā *abbreviates*.

---

## 2. Where the project misunderstands Pāṇini because it is looking for computation too early

### (a) The Bavati derivation — terminating with "unknowns"

`[TEXTUAL EVIDENCE]` The Bavati trace (per `rules.my`) records 7 state transitions and terminates partial with explicit unknowns.

`[TRADITIONAL INTERPRETATION]` The derivation of *bhavati* is a *textbook* example that every student of Pāṇini learns completely in the first weeks of study. The *prakriyā* is fully specified in the tradition (Kāśikā, Siddhāntakaumudī). There are no "unknowns."

`[YOUR INFERENCE]` The fact that the project's flagship derivation terminates with "unknowns" like "exact-source-supported-account-of-initial-S-in-Śap" is not a sign that Pāṇini is incomplete — it is a sign that the project jumped to executable traces before reading the commentarial tradition that resolves every one of these steps. The Śap → a (with Ś-it deletion, 1.3.3 and 1.3.9) is completely standard. The "unknown" is an artifact of trying to derive from the sūtra text alone, without the *vṛtti* literature. This is the single clearest evidence that the project is looking for computation before it has finished reading.

### (b) Rule-conflict resolution as "dispatch"

`[TEXTUAL EVIDENCE]` 1.4.2 *vipratiṣedhe paraṃ kāryam* is the only explicit conflict-resolution sūtra in the text.

`[TRADITIONAL INTERPRETATION]` The tradition (Mahābhāṣya, Paribhāṣenduśekhara) discusses a *large* family of *nyāya*-s (interpretive maxims) that operate *before* 1.4.2. The project's own `rule-system.md` acknowledges this — "the full list of nyāya/paribhāṣā that precede vipratiṣedha is not researched."

`[YOUR INFERENCE]` Yet `paribhasha.md` already presents a *fixed four-step priority hierarchy* (antaraṅga > nitya > apavāda > vipratiṣedha) and implements it in `meta.my` as `resolve-conflict`. This hierarchy is presented as if it were the Pāṇinian conflict system. It is not. It is a *post-hoc rationalization* drawn from secondary academic sources (the project cites "Università Ca' Foscari Venezia, Kiparsky" — not the Mahābhāṣya, not Nāgeśa). The tradition does not agree on a single fixed ordering; different *ācārya*-s weight *antaraṅga/bahiraṅga* differently from *nitya/anitya*. To encode a *single* hierarchy as "the Pāṇinian conflict resolution" before the paribhāṣā literature has been studied is to build a machine on a misreading.

---

## 3. Important Pāṇinian concepts or relationships missing from the current ontology

I list concepts that any serious *vyākaraṇa* treatment would consider foundational, and that the current `foundation/` directory does not address.

### (a) *Prakṛti* and *pratyaya* as a *compound input*, not separate atoms

`[TEXTUAL EVIDENCE]` The derivation does not begin with a bare dhātu. It begins with the *upadeśa* form — the dhātu *as listed in the Dhātupāṭha with its it-markers*, plus the *lakāra* (tense/mood marker) and the *puruṣa/vacana* (person/number). The ontology has no entry for *upadeśa*, *lakāra*, or *puruṣa*.

`[YOUR INFERENCE]` Without *lakāra* (laṭ, loṭ, laṅ, liṭ, etc.), the entire verbal derivation system is invisible. The project's dhātu registry records gaṇa, pada, seT/aniT — but not which *lakāra*-s a root takes, or how *lakāra* selection drives the subsequent rule cascade. A Pāṇinian ontology that cannot represent "bhavati is laṭ-lakāra, third person, singular, of dhātu bhū" is missing the load-bearing structure of the *prakriyā*.

### (b) *Saṃskāra* (conditioning operations) as a distinct layer

`[TRADITIONAL INTERPRETATION]` The tradition distinguishes the *āgama* (addition of a suffix) from the *saṃskāra* (subsequent operations: guṇa, vṛddhi, guṇa-blocking, sandhi, lopa, ādeśa). These are *independent sūtra*-driven operations, not properties of the suffix.

`[YOUR INFERENCE]` The project folds these into "the pratyaya transforms the base" — collapsing two distinct Pāṇinian layers into one. The tradition treats guṇa-application (7.3.84+) as a *separate rule* that *looks at* the state after suffix-addition. The project's `rules.my` does implement `apply-guRa` as a separate function, which is closer — but the *ontology* presents it as part of "what a pratyaya does," not as an independent operational layer. This matters because it determines whether the machine will model derivation as "one suffix = one transformation" (wrong) or as "suffix-addition followed by N independent conditioning rules" (correct).

### (c) *Lopa*, *ādeśa*, *āgama* as operation types

`[TEXTUAL EVIDENCE]` The Aṣṭādhyāyī uses these three distinct operation types throughout: *lopa* (deletion, e.g. 1.3.9), *ādeśa* (substitution, e.g. 7.3.84 guṇa is an ādeśa), *āgama* (augment insertion, e.g. *iṭ-āgama*).

`[YOUR INFERENCE]` The ontology has no entry distinguishing these. The `rules.my` `make-term`/`term-set-surface` model treats everything as "surface-form mutation," losing the Pāṇinian distinction. A deletion (*lopa*) and a substitution (*ādeśa*) have different downstream behavior in the tradition — e.g., *sthānivad-bhāva* (1.1.56) applies to *ādeśa* but not to *lopa*. Without modeling the operation type, the machine cannot correctly apply 1.1.56.

### (d) *Tripādī* — the last three pāda-s as a separate metaregime

`[TEXTUAL EVIDENCE]` The project's own `anuvrtti.md` notes that the *pratyaya*-adhikāra ends not by a closing sūtra but by the transition to the *tripādī* (the last three pāda of the Aṣṭādhyāyī), governed by *asiḍḍavat* (6.1.1) and other metarules. It marks this as "not researched in any task."

`[YOUR INFERENCE]` The *tripādī* is not a footnote — it is roughly *half* of the Aṣṭādhyāyī by sūtra count (all of adhyāya 6-8). The metarule *asiḍḍavat* fundamentally changes which rules can fire (it blocks *siṭ*-āgama across the entire tripādī). Any machine model that does not represent the tripādī/non-tripādī distinction will silently apply rules outside their domain. This is a structural absence, not a missing detail.

### (e) *Saṃhitā* and *pada*-parsing

`[TRADITIONAL INTERPRETATION]` The tradition has an entire *prakaraṇa* on *saṃhitā* (euphonic combination across word boundaries) and on *pada*-analysis (splitting a continuous utterance into its constituent *pada*-s). The project's ontology has no entry for *pada* (in the technical sense of "inflected word, ready for sandhi") or for *saṃhitā* as a rule domain.

`[YOUR INFERENCE]` Without *pada* and *saṃhitā*, the project cannot model the boundary between intra-word derivation (where guṇa/vṛddhi operate) and inter-word sandhi (where a different rule set operates). This boundary is fundamental to Pāṇini's architecture — adhyāya 6 (sandhi) and adhyāya 7 (internal morphophonology) are separate *adhikāra*-s precisely because they operate on different domains.

### (f) *Svara* (accent)

`[TEXTUAL EVIDENCE]` Many sūtra-s in adhyāya 6 and 8 govern accent (udātta, anudātta, svarita). The Dhātupāṭha records accent for each root. Several *it*-markers (pit) encode accent behavior.

`[YOUR INFERENCE]` The project's dhātu registry has no accent field. The `it.md` mentions *pit* "indicates anudātta accent" but the ontology has no concept of accent as a derivational dimension. For Pāṇini, accent is not optional decoration — it is a *morphological property* that drives rule application (e.g., *udātta* triggers certain sandhi rules). Ignoring accent means the machine cannot correctly derive Vedic forms or even many classical ones where accent-conditioned sandhi applies.

---

## 4. Are kāraka, it, pratyāhāra, anuvṛtti, adhikāra, paribhāṣā, and vipratiṣedha represented in ways a serious Sanskrit grammarian would object to?

### Kāraka — YES, objectionable

`[TEXTUAL EVIDENCE]` The six kāraka are defined by 1.4.24–1.4.54 under the adhikāra *kārake* (1.4.23).

`[TRADITIONAL INTERPRETATION]` The tradition (Kāśikā, Mahābhāṣya) insists that kāraka is *not* a fixed slot-list per verb. The same dhātu (pac) can have kartṛ + karman, or kartṛ + karman + adhikaraṇa, depending on the *sentence*. The kāraka set is determined by the *äksepa* (the semantic intention of the utterance), not by the dhātu alone.

`[YOUR INFERENCE]` The project *says* it understands this — `dhatu-karaka-relation.md` refuted the fixed-arity version, and H1 in the ledger records this. But the *foundation document* `karaka.md` still lists each kāraka with a "computational content" gloss ("Execution Context," "target argument," "primary actor / thread / process") that a *pāṇḍita* would find grotesque. *Kartṛ* is not a "thread that triggers evaluation." *Adhikaraṇa* is not an "execution context." These glosses are presented in the `[INTERPRETATION]` and `[MY-LISP HYPOTHESIS]` sections, but they leak into the structure of the document itself — the *ordering* of the six kāraka in the document follows a Source→Goal→Instrument→Location→Patient→Agent graph-node logic, not the Pāṇinian order (apādāna, sampradāna, karaṇa, adhikaraṇa, karman, kartṛ), which goes from *most fixed/least independent* to *most independent*. The Pāṇinian ordering is semantically meaningful: it reflects increasing *svātantrya* (independence). Reordering it as a graph traversal destroys that signal.

### It — mostly acceptable, but one objection

`[TEXTUAL EVIDENCE]` 1.3.2–1.3.9 define the it-system.

`[TRADITIONAL INTERPRETATION]` The tradition treats it-markers as *anubandha*-s — *syntactic markers on the upadeśa form* that are read as part of the grammatical notation, not as a "family of control signals."

`[YOUR INFERENCE]` The `it.md` document is actually one of the better ones — it correctly identifies that it-markers are heterogeneous and that a single boolean is wrong. The objection: the document's framing ("family of separately documented control signals") still treats each it-type as if it were a *named rule*. In the tradition, the it-sounds are not rules — they are *properties of the upadeśa form* that *trigger* rules. An it-marker is part of the *data* (the listed form of the suffix), not part of the *rule system*. The project's model (tags on a Term object) is closer to this, but the *ontology document* blurs the line by listing it-types alongside rule-types (vidhi, niyama, atideśa) as if they were the same kind of thing.

### Pratyāhāra — acceptable with a caveat

`[TEXTUAL EVIDENCE]` 1.1.71 *ādir antyena sahetā* defines the mechanism.

`[TRADITIONAL INTERPRETATION]` The Śiva-sūtras are a *prākṛya* (pre-existing arrangement) of phonemes. A pratyāhāra denotes a set by its first member and a terminal marker.

`[YOUR INFERENCE]` The `pratyahara.md` document is sound and appropriately cautious. The one caveat: the document presents the Śiva-sūtra list as verified against "learnsanskrit.org" — a secondary pedagogical source. A grammarian would insist on verification against the *upadeśa* tradition (the recited Śiva-sūtra-s as preserved in the *Ṛgveda-prātiśākhya* and the *Śikṣā* literature), not a website. The ordering and the it-markers of the Śiva-sūtras are a matter of recensional variation, and the project has not documented which recension it follows.

### Anuvṛtti / Adhikāra — the strongest part of the foundation, with one serious gap

`[TEXTUAL EVIDENCE]` 1.3.11 *svaritenādhikāraḥ* marks adhikāra by svarita accent in recitation.

`[TRADITIONAL INTERPRETATION]` The tradition treats adhikāra-scope as *partly indeterminate from the bare text* — the Kāśikā and the Mahābhāṣya discuss where specific adhikāra-s end. The project's `anuvrtti.md` correctly identifies this.

`[YOUR INFERENCE]` This document is the most honest in the repo — it admits that adhikāra boundaries "partially rely on the commentarial tradition" and that a machine must either encode them as external data or accept ambiguity. This is exactly right. The gap: the project has not *done* either. It has not encoded any adhikāra boundary data, and it has not built a representation that tolerates ambiguity. The `panini-core.my` code has no concept of adhikāra-scope at all. So the honest recognition in the document has not propagated to the machine.

### Paribhāṣā — objectionable

`[TEXTUAL EVIDENCE]` Pāṇini did not collect paribhāṣā-s. They are scattered and some are implicit.

`[TRADITIONAL INTERPRETATION]` Nāgeśa Bhaṭṭa's *Paribhāṣenduśekhara* (~133 paribhāṣā-s) is the standard systematization. But Nāgeśa himself *disputes* several paribhāṣā-s and their ordering. The tradition is not unanimous.

`[YOUR INFERENCE]` `paribhasha.md` presents a *fixed four-step hierarchy* (antaraṅga > nitya > apavāda > vipratiṣedha) and implements it in code. This is a *single post-hoc rationalization* drawn from secondary sources. A serious grammarian would object that: (1) the hierarchy is not in Pāṇini; (2) it is not even universally agreed in the tradition; (3) the relationship between *antaraṅga/bahiraṅga* and *nitya/anitya* is itself debated (which takes priority?); (4) *apavāda* is not a single mechanism — the tradition distinguishes *apavāda* (exception that fully blocks) from *niyama* (restriction that narrows but does not block), and the project's code (`resolve-declared-apavada` in `meta.my`) only models the former. Encoding a contested hierarchy as a deterministic dispatch function is a misrepresentation of the tradition.

### Vipratiṣedha — acceptable, with one caveat

`[TEXTUAL EVIDENCE]` 1.4.2 *vipratiṣedhe paraṃ kāryam*.

`[TRADITIONAL INTERPRETATION]` This is the *last-resort* tie-breaker, applying only when no higher principle resolves the conflict.

`[YOUR INFERENCE]` The `rule-system.md` document correctly identifies this as a residual tie-breaker, not the primary mechanism. This is the right reading. The caveat: the document says "not verified against a digital source" for 1.4.2 itself — the project is building a conflict-resolution model on a sūtra it has not yet verified against a critical edition. This is exactly the kind of premature formalization that the project's own methodology warns against.

---

## 5. Which hypotheses H1–H7 would I attack most strongly?

### H1 (kāraka as typed graph edges) — attack: the graph model is the wrong *shape*

`[TEXTUAL EVIDENCE]` Kāraka is defined under adhikāra 1.4.23. Each kāraka is a *designation* (*saṃjñā*) assigned to a participant *in a specific utterance context*.

`[TRADITIONAL INTERPRETATION]` The tradition treats kāraka as *designations assigned at utterance time*, not as structural edges. The same entity can be kartṛ in one sentence and karman in another (active vs. passive). The designation is *occasioned by the speaker's intention*, not by the dhātu.

`[YOUR INFERENCE]` The graph model fixes kāraka as *structural edges from a dhātu-node to entity-nodes*. This is the wrong ontology. Kāraka is not a relation *between* dhātu and participant — it is a *designation of the participant relative to the action*. The participant *is* the kartṛ; the edge "kartṛ" is a label on the *participant*, not on a *relation*. More fundamentally, the graph model cannot represent *karman-kartṛ inversion* (where the same participant is kartṛ in the active voice and becomes karman in the passive, while the semantic content is unchanged). The graph would have to *re-wire its edges* to represent voice, which means the edges are not semantic primitives — they are surface-structure epiphenomena. A model that treats epiphenomena as primitives is inverted.

### H5 (paribhāṣā as defmacro) — attack: defmacro is the wrong abstraction

`[TEXTUAL EVIDENCE]` Paribhāṣā-s are interpretive maxims. They are *not* executed — they are *consulted* when interpreting how a rule applies.

`[TRADITIONAL INTERPRETATION]` A paribhāṣā like *vipratiṣedhe paraṃ kāryam* is not a function that is "called" before a rule fires. It is a *hermeneutic principle* that a *pāṇḍita* applies when two rules seem to conflict.

`[YOUR INFERENCE]` A `defmacro` is *code that generates code* — it runs at compile-time and produces code that runs at run-time. This is not what a paribhāṣā does. A paribhāṣā is not a *transformer of rules*; it is a *criterion for selecting among rules*. The defmacro analogy collapses two distinct levels (rule-interpretation and rule-transformation) into one. A closer (but still imperfect) analogy would be a *conflict-resolution strategy* in a production-rule system — but even that presupposes a machine model that Pāṇini's text does not require. The hypothesis should be abandoned, not because it is "wrong" in some abstract sense, but because it is *premature* — it commits to a machine architecture before the paribhāṣā literature has been studied.

### H4 (anuvṛtti as lexical scope / closure) — attack: already partially refuted, and the refutation was correct

`[YOUR INFERENCE]` The project's own ledger records that H4 "partially fails its own test." I agree with the project's self-refutation and would push it further: the closure analogy fails not just because adhikāra boundaries are indeterminate, but because *anuvṛtti is not a mechanism at all* — it is a *reading convention*. A closure is a *runtime structure* (an environment capture). Anuvṛtti is a *hermeneutic instruction to the reader*. These are different categories of thing. Treating a reading-convention as a runtime structure is a category error.

---

## 6. What parts of the Aṣṭādhyāyī cannot be understood from the sūtras alone and require the commentarial tradition?

`[TEXTUAL EVIDENCE]` The Aṣṭādhyāyī is a sūtra-text — maximally compressed, elliptical, presupposing an oral/teacher tradition. Patañjali himself (Mahābhāṣya, ~2nd c. BCE) opens by asking *kim prayojanam* (what is the purpose?) and argues that the sūtra-s are *not self-sufficient* without a *vṛtti* (commentary).

`[TRADITIONAL INTERPRETATION]` The tradition identifies several things that cannot be extracted from the bare sūtra-s:

1. **Adhikāra boundaries.** The text gives no explicit "end of scope" marker. The svarita accent (1.3.11) is only preserved in recitation, not in writing. Which sūtra-s fall under which adhikāra is a *commentarial determination*. The project's own `anuvrtti.md` acknowledges this.

2. **The *it*-designation of specific sounds in specific suffixes.** Sūtra 1.3.2–1.3.8 give *criteria* for identifying it-sounds, but *which sound in which suffix* is an it-marker is often only recoverable from the *upadeśa* form as preserved in the *vārttika* and *kaumudī* tradition. The project's `it.md` admits it only studied 1.3.2 and 1.3.9 and that "1.3.3–1.3.8 are not exhaustively researched."

3. **The *gaṇa*-lists.** The Dhātupāṭha's gaṇa-classification of each dhātu is *not derivable from the Aṣṭādhyāyī* — it is an external list. The project's `dhatu.md` correctly notes this. But the *Gaṇapāṭha* (the list of words belonging to each *gaṇa* for taddhita-derivation, separate from the Dhātupāṭha) is also external and is not mentioned anywhere in the project.

4. **The *lakāra*-system.** The ten lakāra-s (laṭ, laṅ, luṅ, liṭ, luṭ, lṛṭ, lṅ, liṅ, luṅ, leṭ) and their mapping to tense/mood is traditional, not explicit in the sūtra-s. The project has no entry for lakāra at all.

5. **The distinction between *sārvadhātuka* and *ārdhadhātuka* pratyaya-s.** This is the most important morphological classification in the verbal system (it determines guṇa/vṛddhi behavior). The term appears in the project's `it.md` and `rules.my` (as a tag), but the *ontology* has no entry for it, and the *basis* of the distinction (which suffixes are which) is not in a single sūtra — it is distributed across 3.4.77+ and requires the *vṛtti* to systematize.

6. **The *kṛt*-pratyaya list and the *taddhita*-pratyaya list.** The Aṣṭādhyāyī enumerates these across hundreds of sūtra-s, but the *complete list* with meanings is only available in the *kṛt-gaṇa-pāṭha* and *taddhita-gaṇa-pāṭha* ancillary texts.

7. **The *vārttika*-s of Kātyāyana.** These are *interpretive notes* on the sūtra-s that Patañjali discusses. Many sūtra-s cannot be correctly applied without knowing which *vārttika* qualifies them. The project does not reference the *vārttika*-s at all.

`[YOUR INFERENCE]` The project has been reading the Aṣṭādhyāyī as if it were a *self-contained formal specification*. It is not. It is a *compendium of aphorisms* that presupposes a living commentarial tradition. The "unknowns" in the Bavati trace are not mysteries — they are things the *Siddhāntakaumudī* explains in a single sentence. The project has been trying to reverse-engineer the commentary from the sūtra-s, when the commentary is the *precondition* for reading the sūtra-s.

---

## 7. Primary and traditional sources the project should consult before proceeding to `panini-machine-model-v0.1`

`[TRADITIONAL INTERPRETATION]` A serious *vyākaraṇa* reconstruction must engage the primary commentarial tradition, in roughly this order of authority:

1. **Patañjali's *Mahābhāṣya*** (~2nd c. BCE). The foundational commentary. Discusses *why* each sūtra exists, what it means, and what its edge-cases are. No reconstruction can proceed without it. Available in critical edition (Kielhorn, 1880-1885; revised by Kāśinātha Pāṇḍurang Parab). The project does not cite it anywhere. `anuvrtti.md` mentions it by name once; no sūtra interpretation is actually verified against it.

2. **Kātyāyana's *Vārttika*-s.** These are embedded in the Mahābhāṣya. They are *interpretive supplements* to the sūtra-s, often the only source for how a specific sūtra is to be applied. The project does not reference them.

3. **Jayāditya and Vāmana's *Kāśikā* (~7th c. CE).** The most systematic line-by-line commentary on the Aṣṭādhyāyī. It is the standard reference for adhikāra-boundaries, it-designations, and rule-applicability. The project mentions "Kāśikā" twice in passing but has not consulted it.

4. **Bhaṭṭoji Dīkṣita's *Siddhāntakaumudī*** (~17th c.). The *prakriyā*-text that reorganizes the Aṣṭādhyāyī by derivation-type rather than by sūtra-order. This is the text from which the *Bavati* and *dadAti* derivations should be taken — not reverse-engineered. The project's `rules.my` derives Bavati step-by-step but does not cite the *Kaumudī* as its source for the step-sequence.

5. **Nāgeśa Bhaṭṭa's *Paribhāṣenduśekhara*** (~1700 CE). The systematization of the paribhāṣā-s. The project cites this work by name in `paribhasha.md` but does not actually engage with its *arguments* — it only borrows the list of paribhāṣā names.

6. **The *Dhātupāṭha*** (critical edition). The project uses the Dhātupāṭha but has not cited a critical edition. The standard is Böhtlingk's (1887) or the more recent S. M. Katre edition. The project should verify its 20 roots against at least one of these, not against "learnsanskrit.org."

7. **The *Gaṇapāṭha*.** The ancillary list of *gaṇa*-members for taddhita and kṛt derivation. Not mentioned anywhere in the project.

8. **The *Śikṣā* and *prātiśākhya* literature** — for the Śiva-sūtra recension and the phonetic framework. The project's `pratyahara.md` verifies the Śiva-sūtra-s against a website, not against the *Ṛgveda-prātiśākhya* or the *Taittirīya-prātiśākhya*, which are the primary sources for the phoneme-arrangement.

9. **George Cardona, *Pāṇini: His Work and Traditions*** (1988) and *Pāṇinian Studies* (vol. 1-3). The project cites "Cardona" in passing but does not engage with his detailed analyses of adhikāra, anuvṛtti, and paribhāṣā, which are the standard modern scholarly reference.

10. **Paul Kiparsky, *Pāṇinian Studies*** (various). The project cites "Kiparsky" as a source for the priority hierarchy, but Kiparsky's work is *far more detailed* than the four-step summary the project uses. His discussions of *antaraṅga/bahiraṅga* (Kiparsky 1982, *Some Theoretical Problems in Pāṇini's Grammar*) are essential and are not consulted.

`[YOUR INFERENCE]` The project's source base is *secondary pedagogical websites* and *the Vidyut source code*. Neither is a primary source. The project has built a "formal foundation" without reading the Mahābhāṣya. This is the single most serious methodological failure — and it is recoverable, but only if the project pauses the machine-model work and reads the commentary.

---

## 8. Five cases where an obvious programming-language analogy distorts Pāṇini

### (i) "dhātu = function, kāraka = arguments, pratyaya = type-modifier"

`[YOUR INFERENCE]` This is the project's implicit architecture (`ontology.md` class table). The distortion: in Pāṇini, the *dhātu* does not "call" its *kāraka*-s. The kāraka-s are *designations of participants in a semantic event*, assigned by the speaker. A function receives arguments *from its caller*; a dhātu does not "receive" kāraka-s — the kāraka-s are *co-present* in the *ākhyāta* (utterance) and are independently designated. Treating dhātu as a function that "takes" kāraka-arguments imposes a caller/callee asymmetry that does not exist in the grammar.

### (ii) "saṃjñā = type system"

`[YOUR INFERENCE]` A type system *restricts* what expressions are well-formed. A saṃjñā *enables reference* to a class. These are opposite directions of influence. If *guṇa* were a type, then a non-*guṇa* vowel would be a "type error." In Pāṇini, a non-*guṇa* vowel is simply *not what the word guṇa refers to* — there is no error, just non-applicability of a rule. The type-system analogy makes the grammar look like it *rejects* ill-typed forms, when it actually *ignores* non-matching forms. This is a fundamental behavioral difference: a type-checker *halts*; Pāṇini's rule system *moves on*.

### (iii) "anuvṛtti = lexical scope / closure"

`[YOUR INFERENCE]` A closure *captures a value at definition-time and carries it*. Anuvṛtti is a *reading instruction* that says "continue understanding this word as present." The closure carries a *value*; anuvṛtti carries a *word that the reader must mentally supply*. More critically: a closure's captured value is *immutable within the closure*; an anuvṛtti-carried word can be *modified* (a later sūtra can *anuvartayet* a modified version). Closures do not support mid-scope modification of captured variables. The analogy breaks on the very feature it is meant to explain.

### (iv) "vipratiṣedha = exception handling / try-catch"

`[YOUR INFERENCE]` This is implicit in the `meta.my` `resolve-conflict` model (check conditions in order, first match wins). Exception handling is a *runtime control-flow mechanism* — an exception *propagates* until caught. Vipratiṣedha is a *selection criterion* — it does not propagate; it *chooses*. There is no "throwing" of a conflict. The conflict simply *exists* (two rules apply), and the criterion selects one. Modeling it as a try/catch imposes a propagation/stack-unwinding semantics that has no Pāṇinian basis.

### (v) "prakriyā (derivation) = state-transition log / Vec<Step>"

`[TEXTUAL EVIDENCE]` The tradition (Siddhāntakaumudī) presents prakriyā as a *sequence of steps*, each applying one operation to the current string.

`[YOUR INFERENCE]` The Vidyut-inspired `Vec<Step>` model (H6) seems obvious — and it is the *least* distorted of the analogies. But it still distorts in one way: in the tradition, the prakriyā is *not a log of what happened*; it is a *demonstration of what must happen*. Each step is *necessary*, not merely *recorded*. A state-transition log is *descriptive* (it records the machine's operations); a prakriyā is *prescriptive* (it shows the *only* correct path). If the machine takes a different path and logs it, the log is *wrong* — there is no notion of "alternative valid derivations" in the tradition for a given input. The log-model silently admits this by being deterministic, but it does not *represent* the normativity. A Pāṇinian prakriyā is closer to a *proof* than to a *trace*.

---

## Final question: If this project completely abandoned its goal of building a Lisp machine tomorrow, would its formal reconstruction of Pāṇini still be scientifically valuable?

`[YOUR INFERENCE]` **No — not yet.** And here is what would have to change.

The project's current value lies almost entirely in its *methodological discipline* — the three-level tagging, the hypothesis ledger, the refusal to assert equivalences without evidence. That discipline is genuinely rare and genuinely valuable. But the *substance* of the reconstruction is not yet Pāṇini. It is a *reading of secondary sources* (Vidyut, learnsanskrit.org, Kiparsky summaries) filtered through a CS lens. The sūtra-s are cited but not verified against critical editions; the commentarial tradition is named but not read; the derivations are reverse-engineered from the sūtra text rather than taken from the *Kaumudī* or the *Mahābhāṣya*; foundational concepts (*lakāra*, *sārvadhātuka/ārdhadhātuka*, *upadeśa*, *lopa/ādeśa/āgama*, *tripādī*, *saṃhitā*, *svara*, *Gaṇapāṭha*) are absent.

If the Lisp-machine goal were abandoned, what would remain is a structured notebook of *preliminary observations on Pāṇini from a computer-science perspective*. That is useful as a *starting point*, but it is not a *formal reconstruction of Pāṇini's grammar*. For it to become one, the following would have to change:

1. **The primary source must become the Mahābhāṣya and the Kāśikā, not the Vidyut source code.** Vidyut is an *implementation* of one reading of Pāṇini. It is not Pāṇini. Using it as the evidential backbone (as `it.md` explicitly does — "independently verified through real Vidyut code") means the project is reconstructing *Vidyut's Pāṇini*, not Pāṇini's Pāṇini.

2. **The derivations must be taken from the Siddhāntakaumudī, not reverse-engineered.** The Bavati "unknowns" would vanish immediately. The project would stop mistaking *its own gaps* for *Pāṇini's gaps*.

3. **The ontology must include the concepts the tradition treats as foundational** — *lakāra*, *sārvadhātuka/ārdhadhātuka*, *upadeśa*, *lopa/ādeśa/āgama*, *tripādī*, *saṃhitā*, *pada*, *svara* — before it models *kāraka* as graph edges. The current ontology models the *most semantically interesting* concepts first (because those map to CS constructs) and skips the *morphologically load-bearing* ones (because they don't map as neatly).

4. **The paribhāṣā hierarchy must be read in Nāgeśa before it is encoded.** The four-step hierarchy in `paribhasha.md` is a *posterior rationalization*. The Paribhāṣenduśekhara is a *sustained argument* about how paribhāṣā-s relate to each other — it is not a fixed priority queue.

5. **The project must stop presenting CS analogies in the *ontology* documents.** The three-level tagging is good, but the `[INTERPRETATION]` and `[MY-LISP HYPOTHESIS]` sections of *foundation* documents still use CS vocabulary ("operator," "transformer," "execution context," "thread," "pattern matching"). These leak into the `[PANINI]` sections by *structural contamination* — the Pāṇinian concept is described in terms that presuppose the CS framing. A true Pāṇinian foundation would describe *dhātu* in the vocabulary of the *vyākaraṇa* tradition (*kriyā*, *artha*, *prakṛti*, *vikaraṇa*, *lakāra*, *puruṣa*, *vacana*) and leave the CS vocabulary entirely to a separate, explicitly interpretive layer.

If those five changes were made — and the Lisp machine were genuinely forgotten — the project would become a *genuinely valuable formal reconstruction of Pāṇini*: a machine-readable ontology grounded in the commentarial tradition, with provenance-tracked sūtra citations and explicitly-labeled interpretive layers. That would be a real contribution to *vyākaraṇa* studies.

As it stands, the project is *protecting My Lisp from Pāṇini* (by refusing premature equivalences) but it is *not yet protecting Pāṇini from My Lisp* — because the very vocabulary and conceptual order of the foundation documents are shaped by the machine the project intends to build. The order of inquiry is still: "what can Pāṇini do for our machine?" rather than "what is Pāṇini's grammar, regardless of any machine?"

The day that order reverses — the day the foundation documents read like a *śāstra* text rather than a CS design doc — the project will have become scientifically valuable on its own terms. Until then, it is a valuable *methodology* in search of a *content* it has not yet acquired.


# Hostile Review: Sarvam (August 2026)

**verification-status**: `unverified` (contains at least one confirmed factual error regarding Tripādī)

Цей документ містить цінні критичні зауваження, зроблені LLM Sarvam під час "hostile review", та наш аналіз цих зауважень. Головна користь відгуку — виявлення упереджень, пов'язаних із передчасним перекладом системи Паніні в CS-поняття (My Lisp).

## Головна теза відгуку
Проєкт правильно захищає My Lisp від передчасних аналогій, але ще **недостатньо захищає Паніні від самого My Lisp**.

Навіть при використанні маркерів `[PANINI]`/`[INTERPRETATION]`/`[MY-LISP HYPOTHESIS]`, сама структура мислення іноді залишається надто комп'ютерною:
- `dhātu` → operator
- `kāraka` → edge
- `pratyaya` → transformer
- `saṃjñā` → type/tag
- `anuvṛtti` → closure
- `paribhāṣā` → metaprogramming

## Цінні ідеї та зміна гіпотез

### 1. Kāraka: не 'edge', а 'designation'
- **Критика:** kārāka не є ребром між `dhātu` та сутністю назавжди.
- **Новий напрям:** kāraka — це **designation** (призначення/роль) учасника відносно дії в конкретному висловлюванні.
- **Формула:** `entity participates in event + contextual designation`
- **Значення для My Lisp:** Роль не є властивістю сутності назавжди. Сутність ≠ властивість ≠ контекст. Devadatta є `kartṛ` в одній події (event X) і `karman` в іншій (event Y).
- **План дій:** Замість канонізації H1a (edge), паралельно перевіряти конкурентні гіпотези H1a, H1b (designation on participant) та H1c (relation).

### 2. Saṃjñā: не 'type', а 'classification'
- **Критика:** Типова система перевіряє "допустимо / недопустимо" (type error).
- **Новий напрям:** Saṃjñā радше каже "ось множина/об'єкт, який відтепер можна називати X". Це ближче до **designation**, **named predicate** або **classification**.

### 3. Paribhāṣā: не 'defmacro', а 'meta-policy'
- **Критика:** `defmacro` трансформує код у код.
- **Новий напрям:** Paribhāṣā — це правила застосування + ситуація ↓ інтерпретація/пріоритет.
- **Значення для My Lisp:** Це більше схоже на **meta-policy** або **inference policy**, що дає ідею відділити `(policy ...)` від `(rule ...)`.

### 4. Prakriyā: не просто 'log', а 'proof'
- **Критика:** prakriyā ближча до доказу (proof), ніж до звичайного логу виконання (trace/log).
- **Новий напрям:** Derivation IR має бути не просто `state → transition`, а `state → justified transition → state`.
- **Значення для My Lisp:** Кожен крок містить proof applicability, visibility basis, conflict proof тощо. Це робить Derivation IR схожим на Proof IR і прямо стикується з **Advice Taker** (answer + why). **proof-carrying derivation machine**.

## Помилки Sarvam (Увага!)

1. **Tripādī:** Sarvam помилково стверджує, що Tripādī — це "всі книги 6-8" (половина Aṣṭādhyāyī).
   - **Факт:** Tripādī — це лише останні три pāda восьмої adhyāya (8.2, 8.3, 8.4), починаючи зі сутри 8.2.1 `pūrvatrāsiddham`. Крім того, існують інші механізми (напр. 6.4.22 `asiddhavad atrābhāt`, 6.1.86), які вона сплутала.
   - **Висновок:** Навіть упевнена "індійська модель" може глибоко помилятися. Традиційні джерела слід перевіряти.

2. **Prakriyā як "єдина" правильна траєкторія:**
   - Sarvam стверджує, що є лише один правильний шлях. Це може бути надто категорично. Наявність різних коментарів, конфліктів і paribhāṣā-інтерпретацій свідчить про те, що "mathematically unique path" поки не доведено. Доведено лише, що `prakriyā ≠ arbitrary execution trace`.

## Висновки для архітектури
Відгук надихнув на впровадження **Foundation Independence Test**, **Source Ladder** та перехід до **4-рівневої архітектури** репозиторію (`sastra/`, `formal/`, `hypotheses/`, `implementation/`), щоб жорстко розмежувати традицію від наших комп'ютерних гіпотез.



## Українська (Переклад)

Я пишу це як людина, чия лояльність належить тексту Паніні та традиції *vyākaraṇa*, а не будь-якій машинній моделі. Моє завдання — визначити, де проєкт спотворює Паніні — свідомо чи ні — і де пошук обчислень почався до того, як була зрозуміла граматика.

---

### 1. Концепції, які все ще несвідомо втискуються в сучасні категорії CS

#### (a) `dhātu` як "оператор" / "вузол предиката"

`[TEXTUAL EVIDENCE]` Aṣṭādhyāyī визначає dhātu переліком (1.3.1 *bhūvādayo dhātavaḥ*) — це перехресне посилання на зовнішній список (Dhātupāṭha). Текст нічого не говорить про "оператор" чи "функцію".

`[TRADITIONAL INTERPRETATION]` Mahābhāṣya Патанджалі обговорює dhātu як носія *kriyā* (значення дії), але це семантико-метафізична дискусія, а не формальна. Традиція розглядає dhātu як *лексичний примітив* із властивостями (gaṇa, pada, seT/aniT), а не як функцію, що "приймає аргументи".

`[YOUR INFERENCE]` Файл проєкту `ontology.md` називає dhātu "оператором" і "вузлом предиката". `karaka.md` малює dhātu як корінь орієнтованого графа з типізованими ребрами. Цього немає у Паніні. Це сучасна теорія семантичних ролей (Агент/Пацієнт/Інструмент), спроєктована на текст. Проєкт *каже*, що знає це (теги `[MY-LISP HYPOTHESIS]` це визнають), але фундаментні документи — ті самі, які мають бути *до-гіпотетичними* — вже кодують структуру графа у своїх діаграмах та словнику. Забруднення відбувається не в тегованій секції гіпотез; воно знаходиться в *самій онтології*, яка подає граф так, ніби це структура Паніні, а не її інтерпретація.

#### (b) `pratyaya` як "трансформатор" / "функція вищого порядку"

`[TEXTUAL EVIDENCE]` Sūtra 3.1.1 *pratayaḥ* і 3.1.2 *paraś ca* встановлюють, що pratyaya додається *після* основи. Текст нічого не говорить про "трансформацію" чи "декорацію".

`[TRADITIONAL INTERPRETATION]` Традиція розрізняє типи pratyaya (kṛt, taddhita, vikaraṇa, tiṄ, sup) за їхньою дериваційною функцією, але розглядає механізм як *āgama* (додавання) з подальшим *saṃskāra* (операції зумовлення, як-от guṇa/vṛddhi), а не як єдине "застосування функції".

`[YOUR INFERENCE]` Таблиця в `ontology.md` призначає pratyaya клас "transformer". `pratyaya.md` прямо порівнює його з "функцією вищого порядку або декоратором". Це нав'язує єдину обчислювальну абстракцію тому, що традиція розглядає як сімейство різних морфологічних операцій. Pratyaya — це не функція, яка "приймає" основу і "повертає" форму; це суфікс, який *додається*, після чого незалежні правила (guṇa, vṛddhi, sandhi, it-lopa) діють на отриманий рядок. Згортання "додавання + подальші незалежні операції" в "одну трансформацію" є спрощенням рівня CS, яке приховує справжню архітектуру Паніні, де pratyaya є лише одним із входів для *подальшого* каскаду застосування правил.

#### (c) `saṃjñā` як "система типів" / "теги"

`[TEXTUAL EVIDENCE]` Sūtra 1.1.1 *vṛddir ādaic* каже "ā, ai, au називаються vṛddhi." 1.1.68 *svaṃ rūpaṃ śabdasyāśabdasaṃjñā* каже, що слово позначає саме себе, якщо воно не є технічним терміном.

`[TRADITIONAL INTERPRETATION]` Saṃjñā — це акт *назв* — призначення мітки, щоб пізніші sūtra могли компактно посилатися на клас. Kāśikā та Paribhāṣenduśekhara розглядають це як *śābdika* (вербальний/референційний) механізм, а не теоретико-типовий.

`[YOUR INFERENCE]` Розділ `[MY-LISP HYPOTHESIS]` в `ontology.md` каже, що saṃjñā "надзвичайно нагадує систему типів, семантичні теги або символи в Lisp" і називає це "зіставленням шаблонів за типом". Хоча це позначено як гіпотеза, розділ *інтерпретації* `samjna.md` вже використовує мову "typedef/#define" — а *машинний код* проєкту (`panini-core.my`) реалізує saṃjñā як теги на об'єктах Term. Справжня проблема: saṃjñā у Паніні не *обмежує* легальність операцій (як це робить система типів). Вона *дозволяє посилання*. Saṃjñā як "vṛddhi" не забороняє обробку голосного, що не є vṛddhi; вона просто називає множину, щоб правило могло сказати "коли наступний звук є vṛddhi". Називати це "системою типів" означає інвертувати напрямок: типи *обмежують*; saṃjñā *скорочує*.

---

### 2. Де проєкт неправильно розуміє Паніні через те, що занадто рано шукає обчислення

#### (a) Деривація Bavati — завершується "невідомими"

`[TEXTUAL EVIDENCE]` Трейс Bavati (відповідно до `rules.my`) фіксує 7 переходів стану і частково завершується з явними невідомими (unknowns).

`[TRADITIONAL INTERPRETATION]` Деривація *bhavati* — це *хрестоматійний* приклад, який кожен студент Паніні повністю вивчає в перші тижні навчання. *prakriyā* повністю специфікована в традиції (Kāśikā, Siddhāntakaumudī). Там немає "невідомих".

`[YOUR INFERENCE]` Той факт, що флагманська деривація проєкту завершується "невідомими", такими як "exact-source-supported-account-of-initial-S-in-Śap", не є ознакою того, що система Паніні неповна — це ознака того, що проєкт перейшов до виконуваних трейсів до того, як прочитав коментаторську традицію, яка вирішує кожен із цих кроків. Śap → a (з видаленням Ś-it, 1.3.3 і 1.3.9) є абсолютно стандартним. "Невідоме" є артефактом спроби деривації лише з тексту sūtra, без літератури *vṛtti*. Це найяскравіший доказ того, що проєкт шукає обчислення до того, як закінчив читати.

#### (b) Вирішення конфліктів правил як "диспетчеризація" (dispatch)

`[TEXTUAL EVIDENCE]` 1.4.2 *vipratiṣedhe paraṃ kāryam* — єдина явна sūtra вирішення конфліктів у тексті.

`[TRADITIONAL INTERPRETATION]` Традиція (Mahābhāṣya, Paribhāṣenduśekhara) обговорює *велике* сімейство *nyāya* (інтерпретаційних максим), які діють *до* 1.4.2. Власний `rule-system.md` проєкту визнає це — "повний список nyāya/paribhāṣā, що передують vipratiṣedha, не досліджений".

`[YOUR INFERENCE]` Проте `paribhasha.md` вже представляє *фіксовану чотирирівневу ієрархію пріоритетів* (antaraṅga > nitya > apavāda > vipratiṣedha) і реалізує її в `meta.my` як `resolve-conflict`. Ця ієрархія подається так, ніби це і є система конфліктів Паніні. Це не так. Це *постфактум раціоналізація*, взята з вторинних академічних джерел (проєкт цитує "Università Ca' Foscari Venezia, Kiparsky" — не Mahābhāṣya, не Nāgeśa). Традиція не погоджується щодо єдиного фіксованого порядку; різні *ācārya* по-різному зважують *antaraṅga/bahiraṅga* порівняно з *nitya/anitya*. Закодувати *єдину* ієрархію як "вирішення конфліктів Паніні" до вивчення літератури paribhāṣā — означає побудувати машину на неправильному прочитанні.

---

### 3. Важливі концепції Паніні або зв'язки, відсутні в поточній онтології

Я перераховую концепції, які будь-яке серйозне дослідження *vyākaraṇa* вважатиме фундаментальними, і які поточний каталог `foundation/` не розглядає.

#### (a) *Prakṛti* та *pratyaya* як *складений вхід*, а не окремі атоми

`[TEXTUAL EVIDENCE]` Деривація не починається з голого dhātu. Вона починається з форми *upadeśa* — dhātu *як вказано в Dhātupāṭha з його it-маркерами*, плюс *lakāra* (маркер часу/способу) та *puruṣa/vacana* (особа/число). В онтології немає записів для *upadeśa*, *lakāra* або *puruṣa*.

`[YOUR INFERENCE]` Без *lakāra* (laṭ, loṭ, laṅ, liṭ тощо) вся система дієслівної деривації невидима. Реєстр dhātu проєкту фіксує gaṇa, pada, seT/aniT — але не те, які *lakāra* приймає корінь, або як вибір *lakāra* керує подальшим каскадом правил. Онтологія Паніні, яка не може представити "bhavati — це laṭ-lakāra, третя особа, однина, від dhātu bhū", втрачає несучу конструкцію *prakriyā*.

#### (b) *Saṃskāra* (операції зумовлення) як окремий рівень

`[TRADITIONAL INTERPRETATION]` Традиція розрізняє *āgama* (додавання суфікса) від *saṃskāra* (подальші операції: guṇa, vṛddhi, блокування guṇa, sandhi, lopa, ādeśa). Це *незалежні* керовані sūtra операції, а не властивості суфікса.

`[YOUR INFERENCE]` Проєкт згортає їх у "pratyaya трансформує основу" — об'єднуючи два різні рівні Паніні в один. Традиція розглядає застосування guṇa (7.3.84+) як *окреме правило*, що *дивиться на* стан після додавання суфікса. `rules.my` проєкту дійсно реалізує `apply-guRa` як окрему функцію, що ближче до істини — але *онтологія* представляє це як частину того, "що робить pratyaya", а не як незалежний операційний рівень. Це важливо, оскільки визначає, чи буде машина моделювати деривацію як "один суфікс = одна трансформація" (неправильно), чи як "додавання суфікса, за яким слідують N незалежних правил зумовлення" (правильно).

#### (c) *Lopa*, *ādeśa*, *āgama* як типи операцій

`[TEXTUAL EVIDENCE]` Aṣṭādhyāyī використовує ці три різні типи операцій повсюдно: *lopa* (видалення, напр. 1.3.9), *ādeśa* (заміна, напр. 7.3.84 guṇa є ādeśa), *āgama* (вставлення аугмента, напр. *iṭ-āgama*).

`[YOUR INFERENCE]` Онтологія не має запису, що розрізняє їх. Модель `make-term`/`term-set-surface` у `rules.my` розглядає все як "мутацію поверхневої форми", втрачаючи різницю Паніні. Видалення (*lopa*) і заміна (*ādeśa*) мають різну поведінку на наступних етапах у традиції — наприклад, *sthānivad-bhāva* (1.1.56) застосовується до *ādeśa*, але не до *lopa*. Без моделювання типу операції машина не зможе правильно застосувати 1.1.56.

#### (d) *Tripādī* — останні три pāda як окремий метарежим

`[TEXTUAL EVIDENCE]` Власний `anuvrtti.md` проєкту зазначає, що *pratyaya*-adhikāra завершується не закривальною sūtra, а переходом до *tripādī* (останні три pāda Aṣṭādhyāyī), що регулюються *asiḍḍavat* (6.1.1) та іншими метаправилами. Це позначено як "не досліджено в жодному завданні".

`[YOUR INFERENCE]` *Tripādī* — це не виноска, це приблизно *половина* Aṣṭādhyāyī за кількістю sūtra (вся adhyāya 6-8). Метаправило *asiḍḍavat* фундаментально змінює те, які правила можуть спрацювати (воно блокує *siṭ*-āgama у всій tripādī). Будь-яка машинна модель, яка не репрезентує різницю tripādī/non-tripādī, буде мовчки застосовувати правила поза їхнім доменом. Це структурна відсутність, а не пропущена деталь.

#### (e) *Saṃhitā* та *pada*-парсинг

`[TRADITIONAL INTERPRETATION]` У традиції є цілий *prakaraṇa* про *saṃhitā* (евфонічне поєднання на межі слів) та про *pada*-аналіз (розбиття безперервного висловлювання на складові *pada*). Онтологія проєкту не має запису для *pada* (у технічному значенні "словозмінена форма, готова для sandhi") або для *saṃhitā* як домену правил.

`[YOUR INFERENCE]` Без *pada* та *saṃhitā* проєкт не може моделювати межу між внутрішньослівним словотворенням (де діють guṇa/vṛddhi) і міжслівним sandhi (де діє інший набір правил). Ця межа є фундаментальною для архітектури Паніні — adhyāya 6 (sandhi) і adhyāya 7 (внутрішня морфофонологія) є окремими *adhikāra* саме тому, що вони діють на різних доменах.

#### (f) *Svara* (наголос)

`[TEXTUAL EVIDENCE]` Багато sūtra в adhyāya 6 і 8 керують наголосом (udātta, anudātta, svarita). Dhātupāṭha фіксує наголос для кожного кореня. Кілька *it*-маркерів (pit) кодують поведінку наголосу.

`[YOUR INFERENCE]` Реєстр dhātu проєкту не має поля наголосу. `it.md` згадує, що *pit* "вказує на anudātta наголос", але онтологія не має поняття наголосу як дериваційного виміру. Для Паніні наголос не є необов'язковою декорацією — це *морфологічна властивість*, що керує застосуванням правил (наприклад, *udātta* запускає певні правила sandhi). Ігнорування наголосу означає, що машина не зможе правильно вивести ведійські форми або навіть багато класичних, де застосовується sandhi, зумовлене наголосом.

---

### 4. Чи представлені kāraka, it, pratyāhāra, anuvṛtti, adhikāra, paribhāṣā та vipratiṣedha так, що серйозний граматист санскриту заперечив би?

#### Kāraka — ТАК, неприйнятно

`[TEXTUAL EVIDENCE]` Шість kāraka визначені в 1.4.24–1.4.54 під adhikāra *kārake* (1.4.23).

`[TRADITIONAL INTERPRETATION]` Традиція (Kāśikā, Mahābhāṣya) наполягає, що kāraka *не* є фіксованим списком слотів для дієслова. Той самий dhātu (pac) може мати kartṛ + karman, або kartṛ + karman + adhikaraṇa, залежно від *речення*. Набір kāraka визначається *äksepa* (семантичним наміром висловлювання), а не самим dhātu.

`[YOUR INFERENCE]` Проєкт *каже*, що розуміє це — `dhatu-karaka-relation.md` спростував версію фіксованої арності, і H1 у реєстрі фіксує це. Але *фундаментний документ* `karaka.md` все ще перелічує кожну kāraka з "обчислювальним змістом" ("Execution Context", "target argument", "primary actor / thread / process"), який *pāṇḍita* вважав би гротескним. *Kartṛ* — це не "потік, що запускає обчислення". *Adhikaraṇa* — це не "контекст виконання". Ці глоси представлені в розділах `[INTERPRETATION]` і `[MY-LISP HYPOTHESIS]`, але вони просочуються в структуру самого документа — *порядок* шести kāraka в документі дотримується логіки графових вузлів Source→Goal→Instrument→Location→Patient→Agent, а не порядку Паніні (apādāna, sampradāna, karaṇa, adhikaraṇa, karman, kartṛ), який іде від *найбільш фіксованого/найменш незалежного* до *найбільш незалежного*. Порядок Паніні є семантично значущим: він відображає зростання *svātantrya* (незалежності). Зміна порядку на обхід графа руйнує цей сигнал.

#### It — здебільшого прийнятно, але одне заперечення

`[TEXTUAL EVIDENCE]` 1.3.2–1.3.9 визначають систему it.

`[TRADITIONAL INTERPRETATION]` Традиція розглядає it-маркери як *anubandha* — *синтаксичні маркери на формі upadeśa*, які читаються як частина граматичної нотації, а не як "сімейство керівних сигналів".

`[YOUR INFERENCE]` Документ `it.md` насправді є одним із кращих — він правильно визначає, що it-маркери є гетерогенними і що єдиний логічний (boolean) тип є помилковим. Заперечення: обрамлення документа ("сімейство окремо документованих керівних сигналів") все ще розглядає кожен тип it так, ніби це *іменоване правило*. У традиції it-звуки не є правилами — це *властивості форми upadeśa*, які *запускають* правила. Маркер it є частиною *даних* (переліченої форми суфікса), а не частиною *системи правил*. Модель проєкту (теги на об'єкті Term) ближче до цього, але *документ онтології* розмиває межу, перелічуючи типи it поряд з типами правил (vidhi, niyama, atideśa), ніби це речі одного роду.

#### Pratyāhāra — прийнятно з застереженням

`[TEXTUAL EVIDENCE]` 1.1.71 *ādir antyena sahetā* визначає механізм.

`[TRADITIONAL INTERPRETATION]` Śiva-sūtras є *prākṛya* (попередньо існуючим порядком) фонем. Pratyāhāra позначає множину її першим членом і термінальним маркером.

`[YOUR INFERENCE]` Документ `pratyahara.md` є обґрунтованим і належним чином обережним. Одне застереження: документ представляє список Śiva-sūtra як такий, що перевірений за "learnsanskrit.org" — вторинним педагогічним джерелом. Граматист наполягав би на перевірці за традицією *upadeśa* (задекламовані Śiva-sūtra, як вони збережені в *Ṛgveda-prātiśākhya* та літературі *Śikṣā*), а не за вебсайтом. Порядок і it-маркери Śiva-sūtra є питанням редакційних варіацій, і проєкт не документував, якій редакції він слідує.

#### Anuvṛtti / Adhikāra — найсильніша частина фундаменту, з однією серйозною прогалиною

`[TEXTUAL EVIDENCE]` 1.3.11 *svaritenādhikāraḥ* маркує adhikāra наголосом svarita у декламації.

`[TRADITIONAL INTERPRETATION]` Традиція розглядає область дії adhikāra як *частково невизначену з самого тексту* — Kāśikā та Mahābhāṣya обговорюють, де закінчуються конкретні adhikāra. Власний `anuvrtti.md` проєкту правильно ідентифікує це.

`[YOUR INFERENCE]` Цей документ є найчеснішим у репозиторії — він визнає, що межі adhikāra "частково спираються на коментаторську традицію" і що машина повинна або кодувати їх як зовнішні дані, або приймати неоднозначність. Це абсолютно правильно. Прогалина: проєкт не *зробив* ні того, ні іншого. Він не закодував жодних даних про межі adhikāra і не побудував репрезентацію, що толерує неоднозначність. Код `panini-core.my` взагалі не має поняття області дії adhikāra. Тож чесне визнання в документі не передалося машині.

#### Paribhāṣā — неприйнятно

`[TEXTUAL EVIDENCE]` Паніні не збирав paribhāṣā. Вони розсіяні, а деякі неявні.

`[TRADITIONAL INTERPRETATION]` *Paribhāṣenduśekhara* Nāgeśa Bhaṭṭa (~133 paribhāṣā) є стандартною систематизацією. Але сам Nāgeśa *заперечує* кілька paribhāṣā та їх порядок. Традиція не одностайна.

`[YOUR INFERENCE]` `paribhasha.md` представляє *фіксовану чотирирівневу ієрархію* (antaraṅga > nitya > apavāda > vipratiṣedha) і реалізує її в коді. Це *єдина постфактум раціоналізація*, взята з вторинних джерел. Серйозний граматист заперечив би, що: (1) ієрархія не належить Паніні; (2) вона навіть не є загальновизнаною в традиції; (3) зв'язок між *antaraṅga/bahiraṅga* та *nitya/anitya* сам по собі дискусійний (що має пріоритет?); (4) *apavāda* не є єдиним механізмом — традиція розрізняє *apavāda* (виняток, що повністю блокує) від *niyama* (обмеження, що звужує, але не блокує), а код проєкту (`resolve-declared-apavada` у `meta.my`) моделює лише перше. Кодування дискусійної ієрархії як детермінованої функції диспетчеризації є викривленням традиції.

#### Vipratiṣedha — прийнятно, з одним застереженням

`[TEXTUAL EVIDENCE]` 1.4.2 *vipratiṣedhe paraṃ kāryam*.

`[TRADITIONAL INTERPRETATION]` Це вирішення спорів *в останню чергу*, яке застосовується лише тоді, коли конфлікт не вирішує вищий принцип.

`[YOUR INFERENCE]` Документ `rule-system.md` правильно ідентифікує це як залишковий механізм (tie-breaker), а не основний. Це правильне прочитання. Застереження: документ зазначає "не перевірено за цифровим джерелом" для самої 1.4.2 — проєкт будує модель вирішення конфліктів на sūtra, яку він ще не перевірив за критичним виданням. Це саме той тип передчасної формалізації, проти якого застерігає власна методологія проєкту.

---

### 5. Які гіпотези H1–H7 я б атакував найсильніше?

#### H1 (kāraka як типізовані ребра графа) — атака: графова модель має неправильну *форму*

`[TEXTUAL EVIDENCE]` Kāraka визначається під adhikāra 1.4.23. Кожна kāraka є *designation* (*saṃjñā*), призначеним учаснику *в конкретному контексті висловлювання*.

`[TRADITIONAL INTERPRETATION]` Традиція розглядає kāraka як *designations, призначені під час висловлювання*, а не як структурні ребра. Та сама сутність може бути kartṛ в одному реченні і karman в іншому (активний проти пасивного стану). Призначення *зумовлене наміром мовця*, а не dhātu.

`[YOUR INFERENCE]` Графова модель фіксує kāraka як *структурні ребра від dhātu-вузла до вузлів-сутностей*. Це неправильна онтологія. Kāraka — це не відношення *між* dhātu та учасником, це *designation учасника відносно дії*. Учасник *і є* kartṛ; ребро "kartṛ" — це мітка на *учаснику*, а не на *відношенні*. Фундаментальніше, графова модель не може репрезентувати *інверсію karman-kartṛ* (де той самий учасник є kartṛ в активному стані і стає karman у пасивному, тоді як семантичний зміст не змінюється). Граф мусив би *перепідключати свої ребра*, щоб представити стан, що означає, що ребра не є семантичними примітивами — вони є епіфеноменами поверхневої структури. Модель, що розглядає епіфеномени як примітиви, є інвертованою.

#### H5 (paribhāṣā як defmacro) — атака: defmacro — це неправильна абстракція

`[TEXTUAL EVIDENCE]` Paribhāṣā — це інтерпретаційні максими. Вони *не* виконуються — до них *звертаються*, коли інтерпретують, як застосовується правило.

`[TRADITIONAL INTERPRETATION]` Paribhāṣā, як-от *vipratiṣedhe paraṃ kāryam*, не є функцією, яка "викликається" до того, як спрацює правило. Це *герменевтичний принцип*, який *pāṇḍita* застосовує, коли два правила здаються конфліктними.

`[YOUR INFERENCE]` `defmacro` — це *код, який генерує код* — він працює під час компіляції і створює код, що працює під час виконання. Це не те, що робить paribhāṣā. Paribhāṣā — це не *трансформатор правил*; це *критерій вибору серед правил*. Аналогія з defmacro згортає два різні рівні (інтерпретація правил і трансформація правил) в один. Ближчою (але все ще недосконалою) аналогією була б *стратегія вирішення конфліктів* у production-rule system — але навіть це передбачає машинну модель, якої текст Паніні не потребує. Від гіпотези слід відмовитися не тому, що вона "хибна" в абстрактному сенсі, а тому, що вона *передчасна* — вона закріплює машинну архітектуру до вивчення літератури paribhāṣā.

#### H4 (anuvṛtti як лексична область дії / closure) — атака: вже частково спростовано, і спростування було правильним

`[YOUR INFERENCE]` Власний реєстр проєкту фіксує, що H4 "частково не проходить свій власний тест". Я згоден із самоспростуванням проєкту і пішов би далі: аналогія із замиканням (closure) провалюється не лише тому, що межі adhikāra є невизначеними, але й тому, що *anuvṛtti взагалі не є механізмом* — це *конвенція читання*. Closure — це *структура часу виконання* (захоплення середовища). Anuvṛtti — це *герменевтична інструкція читачеві*. Це різні категорії речей. Розглядати конвенцію читання як структуру часу виконання — це помилка категорії.

---

### 6. Які частини Aṣṭādhyāyī не можуть бути зрозумілі лише з sūtra і потребують коментаторської традиції?

`[TEXTUAL EVIDENCE]` Aṣṭādhyāyī — це текст sūtra — максимально стислий, еліптичний, що передбачає усну/вчительську традицію. Сам Патанджалі (Mahābhāṣya, ~2 ст. до н.е.) починає із запитання *kim prayojanam* (яка мета?) і аргументує, що sūtra *не є самодостатніми* без *vṛtti* (коментаря).

`[TRADITIONAL INTERPRETATION]` Традиція ідентифікує кілька речей, які неможливо витягнути з голих sūtra:

1. **Межі Adhikāra.** Текст не дає явного маркера "кінець області дії". Наголос svarita (1.3.11) зберігається лише в декламації, а не на письмі. Які sūtra підпадають під який adhikāra — це *визначення коментаторів*. Власний `anuvrtti.md` проєкту визнає це.

2. **It-designation специфічних звуків у специфічних суфіксах.** Sūtra 1.3.2–1.3.8 дають *критерії* для ідентифікації it-звуків, але *який звук у якому суфіксі* є it-маркером, часто можна відновити лише з форми *upadeśa*, як вона збережена у традиції *vārttika* та *kaumudī*. `it.md` проєкту визнає, що вивчав лише 1.3.2 і 1.3.9, і що "1.3.3–1.3.8 не досліджені вичерпно".

3. **Списки *Gaṇa*.** Класифікація gaṇa для кожного dhātu у Dhātupāṭha *не може бути виведена з Aṣṭādhyāyī* — це зовнішній список. `dhatu.md` проєкту правильно це відзначає. Але *Gaṇapāṭha* (список слів, що належать кожній *gaṇa* для taddhita-деривації, окремий від Dhātupāṭha) також є зовнішнім і ніде не згадується в проєкті.

4. **Система *Lakāra*.** Десять lakāra (laṭ, laṅ, luṅ, liṭ, luṭ, lṛṭ, lṅ, liṅ, luṅ, leṭ) та їхнє відображення на час/спосіб є традиційними, а не явними у sūtra. Проєкт взагалі не має запису для lakāra.

5. **Різниця між *sārvadhātuka* та *ārdhadhātuka* pratyaya.** Це найважливіша морфологічна класифікація в дієслівній системі (вона визначає поведінку guṇa/vṛddhi). Термін з'являється у `it.md` та `rules.my` проєкту (як тег), але *онтологія* не має для нього запису, і *основа* різниці (які суфікси є якими) не в одній sūtra — вона розподілена по 3.4.77+ і вимагає *vṛtti* для систематизації.

6. **Список *kṛt*-pratyaya і список *taddhita*-pratyaya.** Aṣṭādhyāyī перелічує їх у сотнях sūtra, але *повний список* зі значеннями доступний лише у допоміжних текстах *kṛt-gaṇa-pāṭha* та *taddhita-gaṇa-pāṭha*.

7. ** *Vārttika* Kātyāyana.** Це *інтерпретаційні нотатки* до sūtra, які обговорює Патанджалі. Багато sūtra неможливо правильно застосувати, не знаючи, яка *vārttika* їх кваліфікує. Проєкт взагалі не посилається на *vārttika*.

`[YOUR INFERENCE]` Проєкт читав Aṣṭādhyāyī так, ніби це *самодостатня формальна специфікація*. Це не так. Це *збірник афоризмів*, що передбачає живу коментаторську традицію. "Невідомі" у трейсі Bavati не є таємницями — це речі, які *Siddhāntakaumudī* пояснює в одному реченні. Проєкт намагався реверс-інжинірити коментар із sūtra, тоді як коментар є *передумовою* для читання sūtra.

---

### 7. Первинні та традиційні джерела, які проєкт повинен проконсультувати перед переходом до `panini-machine-model-v0.1`

`[TRADITIONAL INTERPRETATION]` Серйозна реконструкція *vyākaraṇa* повинна залучати первинну коментаторську традицію, приблизно в такому порядку авторитетності:

1. ** *Mahābhāṣya* Патанджалі** (~2 ст. до н.е.). Фундаментальний коментар. Обговорює, *чому* кожна sūtra існує, що вона означає та які є крайні випадки. Жодна реконструкція не може відбутися без нього. Доступний у критичному виданні (Kielhorn, 1880-1885; переглянуте Kāśinātha Pāṇḍurang Parab). Проєкт ніде його не цитує. `anuvrtti.md` згадує його за назвою один раз; жодна інтерпретація sūtra насправді не перевірена за ним.

2. ** *Vārttika* Kātyāyana.** Вони вбудовані у Mahābhāṣya. Це *інтерпретаційні доповнення* до sūtra, часто єдине джерело щодо того, як конкретна sūtra має застосовуватися. Проєкт на них не посилається.

3. ** *Kāśikā* Jayāditya та Vāmana (~7 ст. н.е.).** Найбільш систематичний порядковий коментар до Aṣṭādhyāyī. Це стандартний довідник для меж adhikāra, it-designations та застосовності правил. Проєкт побіжно згадує "Kāśikā" двічі, але не консультувався з ним.

4. ** *Siddhāntakaumudī* Bhaṭṭoji Dīkṣita (~17 ст.).** Текст *prakriyā*, який реорганізує Aṣṭādhyāyī за типом деривації, а не за порядком sūtra. Це текст, з якого слід брати деривації *Bavati* і *dadAti* — а не реверс-інжинірити їх. `rules.my` проєкту виводить Bavati крок за кроком, але не цитує *Kaumudī* як джерело для послідовності кроків.

5. ** *Paribhāṣenduśekhara* Nāgeśa Bhaṭṭa (~1700 н.е.).** Систематизація paribhāṣā. Проєкт цитує цю роботу за назвою у `paribhasha.md`, але насправді не взаємодіє з її *аргументами* — він лише запозичує список назв paribhāṣā.

6. ** *Dhātupāṭha* (критичне видання).** Проєкт використовує Dhātupāṭha, але не посилається на критичне видання. Стандартом є видання Böhtlingk (1887) або більш нове видання S. M. Katre. Проєкт повинен перевірити свої 20 коренів принаймні за одним із них, а не за "learnsanskrit.org".

7. ** *Gaṇapāṭha*.** Допоміжний список членів *gaṇa* для деривації taddhita і kṛt. Ніде в проєкті не згадується.

8. ** Література *Śikṣā* та *prātiśākhya*** — для редакції Śiva-sūtra та фонетичного фреймворку. `pratyahara.md` проєкту перевіряє Śiva-sūtra за вебсайтом, а не за *Ṛgveda-prātiśākhya* або *Taittirīya-prātiśākhya*, які є первинними джерелами для організації фонем.

9. **George Cardona, *Pāṇini: His Work and Traditions*** (1988) та *Pāṇinian Studies* (том 1-3). Проєкт побіжно цитує "Cardona", але не взаємодіє з його детальними аналізами adhikāra, anuvṛtti та paribhāṣā, які є стандартним сучасним науковим довідником.

10. **Paul Kiparsky, *Pāṇinian Studies*** (різні). Проєкт цитує "Kiparsky" як джерело для ієрархії пріоритетів, але робота Кіпарського набагато детальніша, ніж чотирирівневе резюме, яке використовує проєкт. Його обговорення *antaraṅga/bahiraṅga* (Kiparsky 1982, *Some Theoretical Problems in Pāṇini's Grammar*) є суттєвими і не були використані.

`[YOUR INFERENCE]` Джерельною базою проєкту є *вторинні педагогічні вебсайти* та *початковий код Vidyut*. Жодне з них не є первинним джерелом. Проєкт побудував "формальний фундамент", не читаючи Mahābhāṣya. Це найсерйозніший методологічний провал — і його можна виправити, але лише якщо проєкт призупинить роботу над машинною моделлю і прочитає коментарі.

---

### 8. П'ять випадків, коли очевидна аналогія з мовами програмування спотворює Паніні

#### (i) "dhātu = function, kāraka = arguments, pratyaya = type-modifier"

`[YOUR INFERENCE]` Це неявна архітектура проєкту (таблиця класів `ontology.md`). Спотворення: у Паніні *dhātu* не "викликає" свої *kāraka*. Kāraka є *designations учасників семантичної події*, призначеними мовцем. Функція отримує аргументи *від того, хто її викликає*; dhātu не "отримує" kāraka — kāraka *співприсутні* в *ākhyāta* (висловлюванні) і призначаються незалежно. Розгляд dhātu як функції, що "приймає" аргументи-kāraka, нав'язує асиметрію "caller/callee", якої не існує в граматиці.

#### (ii) "saṃjñā = type system"

`[YOUR INFERENCE]` Система типів *обмежує* те, які вирази є правильно побудованими. Saṃjñā *дозволяє посилання* на клас. Це протилежні напрямки впливу. Якби *guṇa* була типом, то голосний, що не є *guṇa*, був би "помилкою типу" (type error). У Паніні голосний, що не є *guṇa*, просто *не є тим, на що посилається слово guṇa* — тут немає помилки, просто правило не застосовується. Аналогія з системою типів змушує граматику виглядати так, ніби вона *відкидає* неправильно типізовані форми, тоді як вона насправді *ігнорує* форми, що не збігаються. Це фундаментальна поведінкова різниця: перевіряльник типів *зупиняється*; система правил Паніні *рухається далі*.

#### (iii) "anuvṛtti = lexical scope / closure"

`[YOUR INFERENCE]` Closure *захоплює значення під час визначення і несе його з собою*. Anuvṛtti — це *інструкція для читання*, яка каже "продовжуй розуміти це слово як присутнє". Closure несе *значення*; anuvṛtti несе *слово, яке читач повинен подумки підставити*. Що більш критично: захоплене значення closure є *незмінним всередині closure*; слово, перенесене через anuvṛtti, може бути *змінено* (пізніша sūtra може *anuvartayet* модифіковану версію). Closure не підтримує модифікацію захоплених змінних у середині області дії. Аналогія ламається на тій самій характеристиці, яку покликана пояснити.

#### (iv) "vipratiṣedha = exception handling / try-catch"

`[YOUR INFERENCE]` Це неявно закладено в моделі `resolve-conflict` у `meta.my` (перевірка умов по порядку, перший збіг виграє). Обробка винятків — це *механізм керування потоком часу виконання* — виняток *поширюється* (propagates), доки не буде спійманий. Vipratiṣedha — це *критерій вибору* — він не поширюється; він *обирає*. Немає жодного "кидання" (throwing) конфлікту. Конфлікт просто *існує* (застосовуються два правила), і критерій обирає одне. Моделювання цього як try/catch нав'язує семантику поширення/розмотування стека, яка не має основи у Паніні.

#### (v) "prakriyā (derivation) = state-transition log / Vec<Step>"

`[TEXTUAL EVIDENCE]` Традиція (Siddhāntakaumudī) подає prakriyā як *послідовність кроків*, кожен з яких застосовує одну операцію до поточного рядка.

`[YOUR INFERENCE]` Натхненна Vidyut модель `Vec<Step>` (H6) здається очевидною — і вона є *найменш* викривленою з аналогій. Але вона все ще має одне спотворення: у традиції prakriyā — це *не лог того, що відбулося*; це *демонстрація того, що має відбутися*. Кожен крок є *необхідним*, а не просто *записаним*. Лог переходів стану є *дескриптивним* (він записує операції машини); prakriyā є *прескриптивною* (вона показує *єдиний* правильний шлях). Якщо машина йде іншим шляхом і логує його, лог є *хибним* — у традиції немає поняття "альтернативних правильних деривацій" для заданого входу. Модель логу мовчки визнає це, будучи детермінованою, але вона не *репрезентує* нормативність. Prakriyā Паніні ближча до *доказу*, ніж до *трейсу*.

---

### Фінальне питання: Якщо цей проєкт завтра повністю відмовиться від мети створення Lisp-машини, чи матиме його формальна реконструкція Паніні наукову цінність?

`[YOUR INFERENCE]` **Ні — поки що ні.** І ось що має змінитися.

Поточна цінність проєкту полягає майже повністю в його *методологічній дисципліні* — трирівневе тегування, реєстр гіпотез, відмова стверджувати еквівалентність без доказів. Ця дисципліна справді рідкісна і справді цінна. Але *сутність* реконструкції ще не є Паніні. Це *прочитання вторинних джерел* (Vidyut, learnsanskrit.org, резюме Kiparsky), відфільтрованих через лінзу CS. Sūtra цитуються, але не перевіряються за критичними виданнями; коментаторська традиція називається, але не читається; деривації реверс-інжиніряться з тексту sūtra, а не беруться з *Kaumudī* чи *Mahābhāṣya*; фундаментальні концепції (*lakāra*, *sārvadhātuka/ārdhadhātuka*, *upadeśa*, *lopa/ādeśa/āgama*, *tripādī*, *saṃhitā*, *svara*, *Gaṇapāṭha*) відсутні.

Якби від мети створення Lisp-машини відмовилися, залишився б структурований зошит *попередніх спостережень за Паніні з перспективи інформатики*. Це корисно як *відправна точка*, але це не *формальна реконструкція граматики Паніні*. Щоб вона стала такою, має змінитися наступне:

1. **Первинним джерелом повинні стати Mahābhāṣya та Kāśikā, а не початковий код Vidyut.** Vidyut є *реалізацією* одного з прочитань Паніні. Це не Паніні. Використання його як доказової бази (як `it.md` явно робить — "independently verified through real Vidyut code") означає, що проєкт реконструює *Паніні за Vidyut*, а не Паніні за Паніні.

2. **Деривації мають братися з Siddhāntakaumudī, а не реверс-інжиніритися.** "Невідомі" у Bavati зникли б миттєво. Проєкт перестав би плутати *свої власні прогалини* з *прогалинами Паніні*.

3. **Онтологія має містити концепції, які традиція вважає фундаментальними** — *lakāra*, *sārvadhātuka/ārdhadhātuka*, *upadeśa*, *lopa/ādeśa/āgama*, *tripādī*, *saṃhitā*, *pada*, *svara* — перш ніж вона моделюватиме *kāraka* як ребра графа. Поточна онтологія моделює *найбільш семантично цікаві* концепції першими (бо вони мапляться на CS конструкти) і пропускає *морфологічно несучі* (бо вони не мапляться так чітко).

4. **Ієрархія paribhāṣā повинна бути прочитана в Nāgeśa до того, як її буде закодовано.** Чотирирівнева ієрархія в `paribhasha.md` є *апостеріорною раціоналізацією*. Paribhāṣenduśekhara є *довгим аргументом* про те, як paribhāṣā відносяться одна до одної — це не фіксована черга пріоритетів.

5. **Проєкт має припинити подавати аналогії з CS у документах *онтології*.** Трирівневе тегування є хорошим, але розділи `[INTERPRETATION]` і `[MY-LISP HYPOTHESIS]` *фундаментних* документів все ще використовують словник CS ("оператор", "трансформатор", "контекст виконання", "потік", "зіставлення шаблонів"). Вони просочуються в розділи `[PANINI]` через *структурне забруднення* — концепція Паніні описується в термінах, що передбачають CS рамки. Справжній фундамент Паніні описував би *dhātu* в словнику традиції *vyākaraṇa* (*kriyā*, *artha*, *prakṛti*, *vikaraṇa*, *lakāra*, *puruṣa*, *vacana*) і залишив би CS словник повністю для окремого, явно інтерпретаційного рівня.

Якби ці п'ять змін були зроблені — і Lisp-машина була б справді забута — проєкт став би *справді цінною формальною реконструкцією Паніні*: машиночитаною онтологією, заснованою на коментаторській традиції, з відстежуваними цитуваннями sūtra та явно позначеними інтерпретаційними рівнями. Це був би реальний внесок у дослідження *vyākaraṇa*.

У нинішньому вигляді проєкт *захищає My Lisp від Паніні* (відмовляючись від передчасних еквівалентностей), але він *ще не захищає Паніні від My Lisp* — оскільки сам словник і концептуальний порядок фундаментних документів сформовані машиною, яку проєкт має намір побудувати. Порядок запитань все ще такий: "що Паніні може зробити для нашої машини?" замість "чим є граматика Паніні, незалежно від будь-якої машини?"

Того дня, коли цей порядок зміниться на протилежний — того дня, коли фундаментні документи читатимуться як текст *śāstra*, а не як дизайн-документ CS — проєкт набуде наукової цінності на своїх власних умовах. Доти ж, це цінна *методологія*, що шукає *зміст*, якого вона ще не набула.


# Hostile Review: Sarvam (August 2026)

**verification-status**: `unverified` (contains at least one confirmed factual error regarding Tripādī)

Dieses Dokument enthält wertvolle kritische Anmerkungen, die vom LLM Sarvam während eines "hostile review" gemacht wurden, sowie unsere Analyse dieser Anmerkungen. Der Hauptnutzen der Bewertung ist die Identifizierung von Vorurteilen im Zusammenhang mit der vorzeitigen Übersetzung des Pāṇini-Systems in CS-Konzepte (My Lisp).

## Hauptthese der Kritik
Das Projekt schützt My Lisp zu Recht vor voreiligen Analogien, aber es **schützt Pāṇini noch nicht ausreichend vor My Lisp selbst**.

Selbst bei Verwendung der Marker `[PANINI]`/`[INTERPRETATION]`/`[MY-LISP HYPOTHESIS]` bleibt die eigentliche Denkstruktur manchmal zu rechnerisch:
- `dhātu` → operator
- `kāraka` → edge
- `pratyaya` → transformer
- `saṃjñā` → type/tag
- `anuvṛtti` → closure
- `paribhāṣā` → metaprogramming

## Wertvolle Ideen und Hypothesenverschiebungen

### 1. Kāraka: nicht 'edge', sondern 'designation'
- **Kritik:** Ein kāraka ist nicht für immer eine Kante zwischen einem `dhātu` und einer Entität.
- **Neue Richtung:** kāraka ist die **Bezeichnung** (Zuweisung/Rolle) eines Teilnehmers in Bezug auf eine Handlung in einer spezifischen Äußerung.
- **Formel:** `entity participates in event + contextual designation`
- **Bedeutung für My Lisp:** Die Rolle ist keine dauerhafte Eigenschaft der Entität. Entität ≠ Eigenschaft ≠ Kontext. Devadatta ist ein `kartṛ` in einem Ereignis (Ereignis X) und ein `karman` in einem anderen (Ereignis Y).
- **Aktionsplan:** Anstatt H1a (edge) zu kanonisieren, sollten die konkurrierenden Hypothesen H1a, H1b (Bezeichnung auf Teilnehmer) und H1c (Relation) parallel getestet werden.

### 2. Saṃjñā: nicht 'type', sondern 'classification'
- **Kritik:** Ein Typsystem prüft auf "gültig / ungültig" (Typfehler).
- **Neue Richtung:** Saṃjñā sagt eher "hier ist eine Menge/ein Objekt, das von nun an als X bezeichnet werden kann". Dies ist näher an **Bezeichnung**, **benanntem Prädikat** oder **Klassifizierung**.

### 3. Paribhāṣā: nicht 'defmacro', sondern 'meta-policy'
- **Kritik:** `defmacro` transformiert Code in Code.
- **Neue Richtung:** Paribhāṣā ist Anwendungsregeln + Situation ↓ Interpretation/Priorität.
- **Bedeutung für My Lisp:** Dies ähnelt eher **meta-policy** oder **inference policy** und gibt die Idee, `(policy ...)` von `(rule ...)` zu trennen.

### 4. Prakriyā: nicht nur 'log', sondern 'proof'
- **Kritik:** prakriyā ist näher an einem Beweis (proof) als an einem Standard-Ausführungsprotokoll (trace/log).
- **Neue Richtung:** Die Derivation-IR sollte nicht nur `Zustand → Übergang` sein, sondern `Zustand → gerechtfertigter Übergang → Zustand`.
- **Bedeutung für My Lisp:** Jeder Schritt enthält Nachweis der Anwendbarkeit, Sichtbarkeitsbasis, Konfliktbeweis usw. Dies macht Derivation-IR ähnlich wie Proof-IR und ist direkt mit dem **Advice Taker** verbunden (Antwort + Warum). Eine **proof-carrying derivation machine**.

## Fehler von Sarvam (Achtung!)

1. **Tripādī:** Sarvam behauptet fälschlicherweise, dass Tripādī "die gesamten Bücher 6-8" (die Hälfte der Aṣṭādhyāyī) sei.
   - **Fakt:** Tripādī sind nur die letzten drei pāda der achten adhyāya (8.2, 8.3, 8.4), beginnend mit dem Sūtra 8.2.1 `pūrvatrāsiddham`. Darüber hinaus gibt es andere Mechanismen (z. B. 6.4.22 `asiddhavad atrābhāt`, 6.1.86), die es verwechselt hat.
   - **Schlussfolgerung:** Selbst ein selbstbewusstes "indisches Modell" kann sich tiefgreifend irren. Traditionelle Quellen müssen überprüft werden.

2. **Prakriyā als die "einzige" korrekte Trajektorie:**
   - Sarvam behauptet, es gäbe nur einen korrekten Weg. Dies könnte zu kategorisch sein. Die Existenz verschiedener Kommentare, Konflikte und paribhāṣā-Interpretationen deutet darauf hin, dass ein "mathematisch einzigartiger Pfad" noch nicht bewiesen ist. Bewiesen ist nur, dass `prakriyā ≠ arbitrary execution trace`.

## Architektonische Schlussfolgerungen
Die Kritik inspirierte die Einführung des **Foundation Independence Test**, **Source Ladder** und den Übergang zur **4-Schichten-Architektur** des Repositories (`sastra/`, `formal/`, `hypotheses/`, `implementation/`), um die Tradition strikt von unseren rechnerischen Hypothesen zu trennen.


## Deutsch (Übersetzung)

Ich schreibe dies als jemand, dessen Loyalität dem Pāṇini-Text und der *vyākaraṇa*-Tradition gilt, nicht irgendeinem maschinellen Modell. Meine Aufgabe ist es, zu identifizieren, wo das Projekt Pāṇini verzerrt – wissentlich oder unwissentlich – und wo die Suche nach Berechnungen begann, bevor die Grammatik verstanden wurde.

---

### 1. Konzepte, die immer noch unbewusst in moderne CS-Kategorien gepresst werden

#### (a) `dhātu` als "Operator" / "Prädikatsknoten"

`[TEXTUAL EVIDENCE]` Die Aṣṭādhyāyī definiert dhātu durch Aufzählung (1.3.1 *bhūvādayo dhātavaḥ*) – ein Querverweis auf eine externe Liste (Dhātupāṭha). Der Text sagt nichts über einen "Operator" oder eine "Funktion".

`[TRADITIONAL INTERPRETATION]` Patañjalis Mahābhāṣya diskutiert den dhātu als Träger der *kriyā* (Aktionsbedeutung), aber dies ist eine semantisch-metaphysische Diskussion, keine formale. Die Tradition behandelt den dhātu als *lexikalisches Primitiv* mit Eigenschaften (gaṇa, pada, seT/aniT), nicht als Funktion, die "Argumente entgegennimmt".

`[YOUR INFERENCE]` Die Datei `ontology.md` des Projekts nennt den dhātu einen "Operator" und einen "Prädikatsknoten". `karaka.md` zeichnet den dhātu als Wurzel eines gerichteten Graphen mit typisierten Kanten. Das steht nicht in Pāṇini. Dies ist die moderne Theorie semantischer Rollen (Agens/Patiens/Instrument), die auf den Text projiziert wird. Das Projekt *sagt*, dass es dies weiß (die `[MY-LISP HYPOTHESIS]`-Tags erkennen es an), aber die Fundamentaldokumente – genau diejenigen, die *vor-hypothetisch* sein sollen – kodieren die Graphenstruktur bereits in ihren Diagrammen und in ihrem Vokabular. Die Kontamination findet nicht im getaggten Hypothesenabschnitt statt; sie befindet sich in der *Ontologie selbst*, die den Graphen so darstellt, als wäre er die Struktur von Pāṇini und nicht ihre Interpretation.

#### (b) `pratyaya` als "Transformator" / "Funktion höherer Ordnung"

`[TEXTUAL EVIDENCE]` Die Sūtras 3.1.1 *pratayaḥ* und 3.1.2 *paraś ca* legen fest, dass ein pratyaya *nach* einer Basis hinzugefügt wird. Der Text sagt nichts über eine "Transformation" oder "Dekoration".

`[TRADITIONAL INTERPRETATION]` Die Tradition unterscheidet Arten von pratyaya (kṛt, taddhita, vikaraṇa, tiṄ, sup) nach ihrer derivationellen Funktion, behandelt den Mechanismus jedoch als *āgama* (Hinzufügung) gefolgt von *saṃskāra* (Konditionierungsoperationen wie guṇa/vṛddhi), nicht als eine einzige "Funktionsanwendung".

`[YOUR INFERENCE]` Die Tabelle in `ontology.md` weist pratyaya die Klasse "transformer" zu. `pratyaya.md` vergleicht es direkt mit einer "Funktion höherer Ordnung oder einem Dekorator". Dies zwingt dem, was die Tradition als eine Familie unterschiedlicher morphologischer Operationen behandelt, eine einzige rechnerische Abstraktion auf. Ein pratyaya ist keine Funktion, die eine Basis "entgegennimmt" und eine Form "zurückgibt"; es ist ein Suffix, das *hinzugefügt* wird, woraufhin unabhängige Regeln (guṇa, vṛddhi, sandhi, it-lopa) auf die resultierende Zeichenfolge einwirken. Die Komprimierung von "Hinzufügung + nachfolgende unabhängige Operationen" in eine "einzige Transformation" ist eine CS-Vereinfachung, die die tatsächliche Architektur von Pāṇini verbirgt, in der pratyaya lediglich einer der Eingaben für eine *spätere* Kaskade von Regelanwendungen ist.

#### (c) `saṃjñā` als "Typsystem" / "Tags"

`[TEXTUAL EVIDENCE]` Sūtra 1.1.1 *vṛddir ādaic* besagt: "ā, ai, au werden vṛddhi genannt." 1.1.68 *svaṃ rūpaṃ śabdasyāśabdasaṃjñā* besagt, dass ein Wort sich selbst bezeichnet, es sei denn, es ist ein Fachbegriff.

`[TRADITIONAL INTERPRETATION]` Saṃjñā ist ein Akt der *Benennung* – die Zuweisung einer Bezeichnung, damit spätere Sūtras kompakt auf eine Klasse verweisen können. Die Kāśikā und der Paribhāṣenduśekhara behandeln dies als einen *śābdika* (verbalen/referenziellen) Mechanismus, nicht als einen typentheoretischen.

`[YOUR INFERENCE]` Der `[MY-LISP HYPOTHESIS]`-Abschnitt in `ontology.md` besagt, dass saṃjñā "stark an ein Typsystem, semantische Tags oder Lisp-Symbole erinnert" und nennt dies "typbasiertes Pattern-Matching". Obwohl es als Hypothese gekennzeichnet ist, verwendet der *Interpretationsabschnitt* von `samjna.md` bereits die Sprache von "typedef/#define" – und der *Maschinencode* des Projekts (`panini-core.my`) implementiert saṃjñā als Tags auf Term-Objekten. Das eigentliche Problem: Ein saṃjñā bei Pāṇini *schränkt die Legalität von Operationen nicht ein* (wie es ein Typsystem tut). Es *ermöglicht Referenz*. Ein saṃjñā wie "vṛddhi" verbietet nicht die Verarbeitung eines Nicht-vṛddhi-Vokals; es benennt lediglich eine Menge, damit eine Regel sagen kann "wenn der nächste Laut ein vṛddhi ist". Dies ein Typsystem zu nennen, kehrt die Richtung um: Typen *beschränken*; saṃjñā *verkürzt*.

---

### 2. Wo das Projekt Pāṇini missversteht, weil es zu früh nach Berechnungen sucht

#### (a) Die Bavati-Derivation – endet in "Unbekannten"

`[TEXTUAL EVIDENCE]` Der Trace von Bavati (gemäß `rules.my`) protokolliert 7 Zustandsübergänge und bricht teilweise mit expliziten "Unbekannten" ab.

`[TRADITIONAL INTERPRETATION]` Die Derivation von *bhavati* ist das *Lehrbuchbeispiel*, das jeder Pāṇini-Student in den ersten Wochen des Studiums vollständig lernt. Die *prakriyā* ist in der Tradition (Kāśikā, Siddhāntakaumudī) vollständig spezifiziert. Es gibt keine "Unbekannten".

`[YOUR INFERENCE]` Die Tatsache, dass die Vorzeige-Derivation des Projekts in "Unbekannten" wie "exact-source-supported-account-of-initial-S-in-Śap" endet, ist kein Zeichen dafür, dass das System von Pāṇini unvollständig ist – es ist ein Zeichen dafür, dass das Projekt zu ausführbaren Traces übergegangen ist, bevor es die Kommentartradition gelesen hat, die jeden dieser Schritte löst. Śap → a (mit Löschung des Ś-it, 1.3.3 und 1.3.9) ist absoluter Standard. Das "Unbekannte" ist ein Artefakt des Versuchs, eine Derivation nur aus dem Sūtra-Text abzuleiten, ohne die *vṛtti*-Literatur. Dies ist der klarste Beweis dafür, dass das Projekt nach Berechnungen sucht, bevor es mit dem Lesen fertig ist.

#### (b) Konfliktlösung bei Regeln als "Dispatching"

`[TEXTUAL EVIDENCE]` 1.4.2 *vipratiṣedhe paraṃ kāryam* ist das einzige explizite Konfliktlösungs-Sūtra im Text.

`[TRADITIONAL INTERPRETATION]` Die Tradition (Mahābhāṣya, Paribhāṣenduśekhara) diskutiert eine *große* Familie von *nyāya* (Interpretationsmaximen), die *vor* 1.4.2 wirken. Das eigene `rule-system.md` des Projekts gibt dies zu – "die vollständige Liste der nyāya/paribhāṣā, die vipratiṣedha vorausgehen, wurde nicht erforscht".

`[YOUR INFERENCE]` Dennoch präsentiert `paribhasha.md` bereits eine *feste vierstufige Prioritätshierarchie* (antaraṅga > nitya > apavāda > vipratiṣedha) und implementiert diese in `meta.my` als `resolve-conflict`. Diese Hierarchie wird so dargestellt, als wäre sie das Konfliktsystem von Pāṇini. Das ist sie nicht. Sie ist eine *nachträgliche Rationalisierung*, die aus sekundären akademischen Quellen stammt (das Projekt zitiert "Università Ca' Foscari Venezia, Kiparsky" – nicht das Mahābhāṣya, nicht Nāgeśa). Die Tradition ist sich nicht über eine einheitliche, feste Reihenfolge einig; verschiedene *ācārya* gewichten *antaraṅga/bahiraṅga* anders im Vergleich zu *nitya/anitya*. Eine *einzelne* Hierarchie als "Pāṇinis Konfliktlösung" zu kodieren, bevor man die paribhāṣā-Literatur studiert hat, bedeutet, eine Maschine auf einer Fehlinterpretation aufzubauen.

---

### 3. Wichtige Konzepte oder Zusammenhänge Pāṇinis, die in der aktuellen Ontologie fehlen

Ich liste die Konzepte auf, die jede ernsthafte Untersuchung der *vyākaraṇa* als grundlegend betrachten würde und die das aktuelle `foundation/`-Verzeichnis nicht behandelt.

#### (a) *Prakṛti* und *pratyaya* als *zusammengesetzte Eingabe*, nicht als separate Atome

`[TEXTUAL EVIDENCE]` Die Derivation beginnt nicht mit einem nackten dhātu. Sie beginnt mit einer *upadeśa*-Form – dem dhātu *wie im Dhātupāṭha mit seinen it-Markern angegeben*, plus einem *lakāra* (Tempus-/Modus-Marker) und *puruṣa/vacana* (Person/Numerus). Es gibt keine Einträge in der Ontologie für *upadeśa*, *lakāra* oder *puruṣa*.

`[YOUR INFERENCE]` Ohne die *lakāra* (laṭ, loṭ, laṅ, liṭ usw.) ist das gesamte System der verbalen Derivation unsichtbar. Das dhātu-Register des Projekts erfasst gaṇa, pada, seT/aniT – aber nicht, welche *lakāra* eine Wurzel annimmt oder wie die Wahl des *lakāra* die nachfolgende Regelkaskade steuert. Eine Pāṇini-Ontologie, die nicht darstellen kann: "bhavati ist laṭ-lakāra, dritte Person, Singular, von dhātu bhū", verliert das tragende Gerüst der *prakriyā*.

#### (b) *Saṃskāra* (Konditionierungsoperationen) als separate Schicht

`[TRADITIONAL INTERPRETATION]` Die Tradition unterscheidet *āgama* (Hinzufügen eines Suffixes) von *saṃskāra* (nachfolgende Operationen: guṇa, vṛddhi, Blockierung von guṇa, sandhi, lopa, ādeśa). Dies sind *unabhängige*, durch Sūtras gesteuerte Operationen, keine Eigenschaften des Suffixes.

`[YOUR INFERENCE]` Das Projekt komprimiert diese in "ein pratyaya transformiert die Basis" – wodurch zwei unterschiedliche Schichten von Pāṇini zu einer zusammengefasst werden. Die Tradition behandelt die Anwendung von guṇa (7.3.84+) als eine *separate Regel*, die auf den Zustand nach dem Hinzufügen des Suffixes *blickt*. Das `rules.my` des Projekts implementiert `apply-guRa` zwar als separate Funktion, was der Wahrheit näher kommt – aber die *Ontologie* stellt es als Teil dessen dar, "was ein pratyaya tut", und nicht als unabhängige operationelle Schicht. Dies ist von Bedeutung, weil es bestimmt, ob die Maschine die Derivation als "ein Suffix = eine Transformation" (falsch) oder als "Suffix-Hinzufügung gefolgt von N unabhängigen Konditionierungsregeln" (richtig) modelliert.

#### (c) *Lopa*, *ādeśa*, *āgama* als Operationstypen

`[TEXTUAL EVIDENCE]` Die Aṣṭādhyāyī verwendet diese drei unterschiedlichen Operationstypen allgegenwärtig: *lopa* (Löschung, z. B. 1.3.9), *ādeśa* (Ersetzung, z. B. 7.3.84 guṇa ist ein ādeśa), *āgama* (Einfügung eines Augments, z. B. *iṭ-āgama*).

`[YOUR INFERENCE]` Die Ontologie hat keinen Eintrag, der diese unterscheidet. Das Modell `make-term`/`term-set-surface` in `rules.my` behandelt alles als "Mutation der Oberflächenform" und verliert dabei Pāṇinis Unterscheidung. Löschung (*lopa*) und Ersetzung (*ādeśa*) haben in der Tradition unterschiedliche Verhaltensweisen in nachfolgenden Schritten – zum Beispiel wird *sthānivad-bhāva* (1.1.56) auf *ādeśa*, aber nicht auf *lopa* angewendet. Ohne Modellierung des Operationstyps wird die Maschine 1.1.56 nicht korrekt anwenden können.

#### (d) *Tripādī* – die letzten drei pāda als separater Meta-Modus

`[TEXTUAL EVIDENCE]` Das projekt-eigene `anuvrtti.md` merkt an, dass der *pratyaya*-adhikāra nicht mit einem schließenden Sūtra endet, sondern mit dem Übergang zur *tripādī* (den letzten drei pāda der Aṣṭādhyāyī), die durch *asiḍḍavat* (6.1.1) und andere Metaregeln geregelt werden. Dies wird als "in keiner Aufgabe untersucht" markiert.

`[YOUR INFERENCE]` Die *tripādī* ist keine Fußnote, sie umfasst in Bezug auf die Anzahl der Sūtras ungefähr *die Hälfte* der Aṣṭādhyāyī (die gesamten adhyāya 6-8). Das Metaregel-Prinzip *asiḍḍavat* verändert grundlegend, welche Regeln auslösen können (es blockiert den *siṭ*-āgama in der gesamten tripādī). Jedes maschinelle Modell, das den Unterschied zwischen tripādī und nicht-tripādī nicht darstellt, wird stillschweigend Regeln außerhalb ihrer Domäne anwenden. Dies ist ein strukturelles Fehlen, kein ausgelassenes Detail.

#### (e) *Saṃhitā* und *pada*-Parsing

`[TRADITIONAL INTERPRETATION]` Die Tradition hat ein ganzes *prakaraṇa* über *saṃhitā* (euphonische Verbindung an Wortgrenzen) und über die *pada*-Analyse (das Aufbrechen einer kontinuierlichen Äußerung in die konstituierenden *pada*). Die Ontologie des Projekts hat keinen Eintrag für *pada* (im technischen Sinne von "eine flektierte Form, bereit für sandhi") oder für *saṃhitā* als Regeldomäne.

`[YOUR INFERENCE]` Ohne *pada* und *saṃhitā* kann das Projekt die Grenze zwischen wortinterner Ableitung (wo guṇa/vṛddhi wirken) und wortübergreifendem sandhi (wo ein anderer Satz von Regeln wirkt) nicht modellieren. Diese Grenze ist grundlegend für Pāṇinis Architektur – adhyāya 6 (sandhi) und adhyāya 7 (interne Morphophonologie) sind separate *adhikāra*, eben weil sie in unterschiedlichen Domänen wirken.

#### (f) *Svara* (Akzent)

`[TEXTUAL EVIDENCE]` Viele Sūtras in adhyāya 6 und 8 steuern den Akzent (udātta, anudātta, svarita). Der Dhātupāṭha verzeichnet den Akzent für jede Wurzel. Mehrere *it*-Marker (pit) kodieren das Akzentverhalten.

`[YOUR INFERENCE]` Das dhātu-Register des Projekts hat kein Akzent-Feld. `it.md` erwähnt, dass *pit* "einen anudātta-Akzent anzeigt", aber die Ontologie hat kein Konzept des Akzents als derivationelle Dimension. Für Pāṇini ist der Akzent keine optionale Dekoration – es ist eine *morphologische Eigenschaft*, die die Anwendung von Regeln steuert (z. B. löst *udātta* bestimmte sandhi-Regeln aus). Das Ignorieren des Akzents bedeutet, dass die Maschine vedische Formen oder sogar viele klassische Formen, bei denen akzentbedingtes sandhi gilt, nicht korrekt ableiten kann.

---

### 4. Sind kāraka, it, pratyāhāra, anuvṛtti, adhikāra, paribhāṣā und vipratiṣedha so dargestellt, dass ein ernsthafter Sanskrit-Grammatiker Einspruch erheben würde?

#### Kāraka – JA, inakzeptabel

`[TEXTUAL EVIDENCE]` Die sechs kāraka werden in 1.4.24–1.4.54 unter dem adhikāra *kārake* (1.4.23) definiert.

`[TRADITIONAL INTERPRETATION]` Die Tradition (Kāśikā, Mahābhāṣya) besteht darauf, dass kāraka *keine* feste Liste von Slots für das Verb ist. Derselbe dhātu (pac) kann kartṛ + karman oder kartṛ + karman + adhikaraṇa haben, abhängig vom *Satz*. Die Menge der kāraka wird durch *äksepa* (die semantische Absicht der Äußerung) bestimmt, nicht durch den dhātu selbst.

`[YOUR INFERENCE]` Das Projekt *sagt*, dass es dies versteht – `dhatu-karaka-relation.md` hat die Ansicht der festen Stelligkeit (arity) verworfen, und H1 im Register verzeichnet dies. Aber das *Fundamentaldokument* `karaka.md` listet immer noch jedes kāraka mit einem "Rechengehalt" auf ("Ausführungskontext", "Zielargument", "Hauptakteur / Thread / Prozess"), den ein *pāṇḍita* für grotesk halten würde. Der *kartṛ* ist nicht der "Thread, der die Berechnung ausführt". Das *adhikaraṇa* ist nicht der "Ausführungskontext". Diese Glossen werden in den Abschnitten `[INTERPRETATION]` und `[MY-LISP HYPOTHESIS]` präsentiert, aber sie sickern in die Struktur des Dokuments selbst ein – die *Reihenfolge* der sechs kāraka im Dokument folgt der Logik von Graphenknoten Source→Goal→Instrument→Location→Patient→Agent, nicht der Pāṇini-Reihenfolge (apādāna, sampradāna, karaṇa, adhikaraṇa, karman, kartṛ), die von *am meisten festgelegt/am wenigsten unabhängig* zu *am unabhängigsten* verläuft. Die Pāṇini-Reihenfolge ist semantisch bedeutsam: Sie spiegelt die Zunahme von *svātantrya* (Unabhängigkeit) wider. Eine Umordnung zur Graphendurchquerung zerstört dieses Signal.

#### It – Größtenteils akzeptabel, aber ein Einwand

`[TEXTUAL EVIDENCE]` 1.3.2–1.3.9 definieren das it-System.

`[TRADITIONAL INTERPRETATION]` Die Tradition behandelt die it-Marker als *anubandha* – *syntaktische Marker auf der upadeśa-Form*, die als Teil der grammatikalischen Notation gelesen werden, nicht als "eine Familie von Steuersignalen".

`[YOUR INFERENCE]` Das Dokument `it.md` ist tatsächlich eines der besseren – es identifiziert korrekt, dass it-Marker heterogen sind und dass ein einziger boolescher Typ falsch ist. Der Einwand: Die Rahmung des Dokuments ("eine Familie einzeln dokumentierter Steuersignale") behandelt immer noch jeden it-Typ so, als wäre er eine *benannte Regel*. In der Tradition sind it-Laute keine Regeln – sie sind *Eigenschaften der upadeśa-Form*, die Regeln *auslösen*. Ein it-Marker ist Teil der *Daten* (der aufgezählten Suffixform), nicht Teil des *Regelsystems*. Das Modell des Projekts (Tags auf dem Term-Objekt) kommt dem näher, aber das *Ontologiedokument* verwischt die Grenze, indem es it-Typen neben Regeltypen (vidhi, niyama, atideśa) auflistet, als wären es Dinge derselben Art.

#### Pratyāhāra – Akzeptabel mit einem Vorbehalt

`[TEXTUAL EVIDENCE]` 1.1.71 *ādir antyena sahetā* definiert den Mechanismus.

`[TRADITIONAL INTERPRETATION]` Die Śiva-sūtras sind ein *prākṛya* (eine bereits existierende Anordnung) von Phonemen. Ein pratyāhāra bezeichnet eine Menge durch ihr erstes Glied und einen terminalen Marker.

`[YOUR INFERENCE]` Das Dokument `pratyahara.md` ist fundiert und angemessen vorsichtig. Der eine Vorbehalt: Das Dokument präsentiert die Śiva-sūtra-Liste als anhand von "learnsanskrit.org" – einer sekundären pädagogischen Quelle – verifiziert. Ein Grammatiker würde auf der Verifizierung anhand der *upadeśa*-Tradition (den rezitierten Śiva-sūtras, wie sie im *Ṛgveda-prātiśākhya* und der *Śikṣā*-Literatur bewahrt werden) bestehen, nicht anhand einer Website. Die Reihenfolge und die it-Marker der Śiva-sūtras sind eine Frage rezensionaler Variationen, und das Projekt hat nicht dokumentiert, welcher Rezension es folgt.

#### Anuvṛtti / Adhikāra – der stärkste Teil des Fundaments, mit einer ernsthaften Lücke

`[TEXTUAL EVIDENCE]` 1.3.11 *svaritenādhikāraḥ* markiert den adhikāra durch den svarita-Akzent bei der Rezitation.

`[TRADITIONAL INTERPRETATION]` Die Tradition behandelt die Reichweite eines adhikāra als *teilweise unbestimmt aus dem bloßen Text* – die Kāśikā und das Mahābhāṣya diskutieren, wo bestimmte adhikāra-s enden. Das `anuvrtti.md` des Projekts identifiziert dies korrekt.

`[YOUR INFERENCE]` Dieses Dokument ist das ehrlichste im Repository – es gibt zu, dass adhikāra-Grenzen "teilweise auf die Kommentartradition angewiesen sind" und dass eine Maschine diese entweder als externe Daten kodieren oder Ambiguität akzeptieren muss. Das ist völlig richtig. Die Lücke: Das Projekt hat *nichts davon* getan. Es hat keine Daten zu adhikāra-Grenzen kodiert und es hat keine Repräsentation aufgebaut, die Ambiguität toleriert. Der `panini-core.my`-Code hat überhaupt kein Konzept von adhikāra-Reichweite. Die ehrliche Erkenntnis im Dokument hat sich also nicht auf die Maschine übertragen.

#### Paribhāṣā – Inakzeptabel

`[TEXTUAL EVIDENCE]` Pāṇini hat keine paribhāṣā-s gesammelt. Sie sind verstreut und einige sind implizit.

`[TRADITIONAL INTERPRETATION]` Nāgeśa Bhaṭṭas *Paribhāṣenduśekhara* (~133 paribhāṣā-s) ist die standardmäßige Systematisierung. Aber Nāgeśa selbst *bestreitet* mehrere paribhāṣā-s und deren Reihenfolge. Die Tradition ist sich nicht einig.

`[YOUR INFERENCE]` `paribhasha.md` präsentiert eine *feste vierstufige Hierarchie* (antaraṅga > nitya > apavāda > vipratiṣedha) und implementiert diese im Code. Dies ist eine *einzige nachträgliche Rationalisierung*, die aus sekundären Quellen stammt. Ein ernsthafter Grammatiker würde einwenden, dass: (1) die Hierarchie nicht bei Pāṇini steht; (2) sie selbst in der Tradition nicht allgemein anerkannt ist; (3) das Verhältnis zwischen *antaraṅga/bahiraṅga* und *nitya/anitya* an sich umstritten ist (was hat Vorrang?); (4) *apavāda* kein einzelner Mechanismus ist – die Tradition unterscheidet *apavāda* (eine Ausnahme, die vollständig blockiert) von *niyama* (eine Einschränkung, die verengt, aber nicht blockiert), und der Code des Projekts (`resolve-declared-apavada` in `meta.my`) modelliert nur ersteres. Die Kodierung einer umstrittenen Hierarchie als deterministische Dispatch-Funktion ist eine Falschdarstellung der Tradition.

#### Vipratiṣedha – Akzeptabel, mit einem Vorbehalt

`[TEXTUAL EVIDENCE]` 1.4.2 *vipratiṣedhe paraṃ kāryam*.

`[TRADITIONAL INTERPRETATION]` Dies ist ein Konfliktlösungsmechanismus *als letztes Mittel*, der nur angewendet wird, wenn ein Konflikt nicht durch ein höheres Prinzip gelöst wird.

`[YOUR INFERENCE]` Das Dokument `rule-system.md` identifiziert dies korrekt als einen Fallback-Mechanismus (Tie-Breaker), nicht als den primären. Das ist die richtige Lesart. Der Vorbehalt: Das Dokument verzeichnet "nicht an einer digitalen Quelle verifiziert" für 1.4.2 selbst – das Projekt baut ein Konfliktlösungsmodell auf einem Sūtra auf, das es noch nicht an einer kritischen Ausgabe verifiziert hat. Dies ist genau die Art von vorzeitiger Formalisierung, vor der die eigene Methodik des Projekts warnt.

---

### 5. Welche der Hypothesen H1–H7 würde ich am stärksten angreifen?

#### H1 (kāraka als typisierte Graphenkanten) – Angriff: Das Graphenmodell hat die falsche *Form*

`[TEXTUAL EVIDENCE]` Kāraka wird unter dem adhikāra 1.4.23 definiert. Jedes kāraka ist eine *Bezeichnung* (*saṃjñā*), die einem Teilnehmer *im spezifischen Kontext einer Äußerung* zugewiesen wird.

`[TRADITIONAL INTERPRETATION]` Die Tradition behandelt kāraka als *Bezeichnungen, die zum Zeitpunkt der Äußerung zugewiesen werden*, nicht als strukturelle Kanten. Dieselbe Entität kann kartṛ in einem Satz und karman in einem anderen (Aktiv vs. Passiv) sein. Die Zuweisung ist *bedingt durch die Absicht des Sprechers*, nicht durch den dhātu.

`[YOUR INFERENCE]` Das Graphenmodell legt kāraka als *strukturelle Kanten vom dhātu-Knoten zu den Entitätsknoten* fest. Dies ist die falsche Ontologie. Ein kāraka ist keine Beziehung *zwischen* dem dhātu und einem Teilnehmer, es ist die *Bezeichnung des Teilnehmers in Bezug auf die Aktion*. Der Teilnehmer *ist* der kartṛ; die "kartṛ"-Kante ist ein Label *auf dem Teilnehmer*, nicht *auf der Beziehung*. Noch grundlegender kann ein Graphenmodell die *karman-kartṛ-Inversion* nicht darstellen (wo derselbe Teilnehmer im Aktiv der kartṛ ist und im Passiv zum karman wird, während der semantische Inhalt unverändert bleibt). Der Graph müsste *seine Kanten neu verschalten*, um den Passiv darzustellen, was bedeutet, dass die Kanten keine semantischen Primitive sind – sie sind Epiphänomene der Oberflächenstruktur. Ein Modell, das Epiphänomene als Primitive behandelt, ist invertiert.

#### H5 (paribhāṣā als defmacro) – Angriff: defmacro ist die falsche Abstraktion

`[TEXTUAL EVIDENCE]` Paribhāṣā-s sind Interpretationsmaximen. Sie werden *nicht* ausgeführt – sie werden *konsultiert*, wenn man interpretiert, wie eine Regel zutrifft.

`[TRADITIONAL INTERPRETATION]` Ein paribhāṣā wie *vipratiṣedhe paraṃ kāryam* ist keine Funktion, die "aufgerufen" wird, bevor eine Regel ausgelöst wird. Es ist ein *hermeneutisches Prinzip*, das der *pāṇḍita* anwendet, wenn zwei Regeln zu kollidieren scheinen.

`[YOUR INFERENCE]` Ein `defmacro` ist *Code, der Code generiert* – es läuft zur Kompilierzeit und erzeugt den Code, der zur Laufzeit läuft. Das ist nicht das, was ein paribhāṣā tut. Ein paribhāṣā ist kein *Regeltransformator*; es ist ein *Auswahlkriterium unter Regeln*. Die Analogie zum defmacro komprimiert zwei unterschiedliche Schichten (Interpretation von Regeln und Transformation von Regeln) zu einer. Eine nähere (aber immer noch unvollkommene) Analogie wäre eine *Konfliktlösungsstrategie* in einem Production-Rule-System – aber selbst das setzt ein Maschinenmodell voraus, das der Text von Pāṇini nicht verlangt. Die Hypothese sollte verworfen werden, nicht weil sie im abstrakten Sinne "falsch" ist, sondern weil sie *vorzeitig* ist – sie legt eine Maschinenarchitektur fest, bevor die paribhāṣā-Literatur studiert wurde.

#### H4 (anuvṛtti als lexikalischer Scope / Closure) – Angriff: bereits teilweise widerlegt, und die Widerlegung war richtig

`[YOUR INFERENCE]` Das projekt-eigene Register verzeichnet, dass H4 "ihren eigenen Test teilweise nicht besteht". Ich stimme der Selbstwiderlegung des Projekts zu und würde noch weiter gehen: Die Closure-Analogie scheitert nicht nur daran, dass die adhikāra-Grenzen unbestimmt sind, sondern auch daran, dass *anuvṛtti überhaupt kein Mechanismus ist* – es ist eine *Lesekonvention*. Eine Closure ist eine *Laufzeitstruktur* (die Erfassung einer Umgebung). Anuvṛtti ist eine *hermeneutische Anweisung an den Leser*. Sie sind unterschiedliche Kategorien von Dingen. Eine Lesekonvention als Laufzeitstruktur zu behandeln, ist ein Kategorienfehler.

---

### 6. Welche Teile der Aṣṭādhyāyī können nicht allein aus den Sūtras verstanden werden und erfordern die Kommentartradition?

`[TEXTUAL EVIDENCE]` Die Aṣṭādhyāyī ist ein Sūtra-Text – maximal knapp, elliptisch und geht von einer mündlichen/lehrenden Tradition aus. Patañjali selbst (Mahābhāṣya, ~2. Jh. v. Chr.) beginnt mit der Frage *kim prayojanam* (Was ist der Zweck?) und argumentiert, dass die Sūtras ohne *vṛtti* (Kommentar) *nicht selbsttragend* sind.

`[TRADITIONAL INTERPRETATION]` Die Tradition identifiziert mehrere Dinge, die unmöglich aus den bloßen Sūtras extrahiert werden können:

1. **Adhikāra-Grenzen.** Der Text gibt keine expliziten "End of Scope"-Markierungen. Der svarita-Akzent (1.3.11) bleibt nur in der Rezitation erhalten, nicht in der Schrift. Welche Sūtras unter welchen adhikāra fallen, ist eine *Bestimmung der Kommentatoren*. Das projekt-eigene `anuvrtti.md` räumt dies ein.

2. **It-Bezeichnungen bestimmter Laute in bestimmten Suffixen.** Sūtras 1.3.2–1.3.8 geben *Kriterien* für die Identifizierung von it-Lauten, aber *welcher Laut in welchem Suffix* ein it-Marker ist, kann oft nur aus der *upadeśa*-Form rekonstruiert werden, wie sie in der *vārttika*- und *kaumudī*-Tradition bewahrt wird. Das Projekt räumt in `it.md` ein, dass es nur 1.3.2 und 1.3.9 studiert hat und dass "1.3.3–1.3.8 nicht erschöpfend untersucht wurden".

3. **Die *Gaṇa*-Listen.** Die gaṇa-Klassifizierung jedes dhātu im Dhātupāṭha *kann nicht aus der Aṣṭādhyāyī abgeleitet werden* – es ist eine externe Liste. `dhatu.md` im Projekt stellt dies richtig fest. Aber der *Gaṇapāṭha* (die Liste der Wörter, die zu jedem *gaṇa* für die taddhita-Derivation gehören, getrennt vom Dhātupāṭha) ist ebenfalls extern und wird im Projekt nirgends erwähnt.

4. **Das *Lakāra*-System.** Die zehn lakāra (laṭ, laṅ, luṅ, liṭ, luṭ, lṛṭ, lṅ, liṅ, luṅ, leṭ) und ihre Zuordnung zu Tempus/Modus sind traditionell und nicht explizit in den Sūtras. Das Projekt hat überhaupt keinen Eintrag für lakāra.

5. **Die Unterscheidung zwischen *sārvadhātuka* und *ārdhadhātuka* pratyaya.** Dies ist die wichtigste morphologische Klassifizierung im verbalen System (sie steuert das guṇa/vṛddhi-Verhalten). Der Begriff erscheint in `it.md` und `rules.my` des Projekts (als Tag), aber die *Ontologie* hat keinen Eintrag dafür, und die *Grundlage* der Unterscheidung (welche Suffixe welche sind) steht nicht in einem einzigen Sūtra – sie ist über 3.4.77+ verteilt und erfordert die *vṛtti*, um systematisiert zu werden.

6. **Die Liste der *kṛt*-pratyaya und die Liste der *taddhita*-pratyaya.** Die Aṣṭādhyāyī listet sie in Hunderten von Sūtras auf, aber die *vollständige Liste* mit Bedeutungen ist nur in den Hilfstexten *kṛt-gaṇa-pāṭha* und *taddhita-gaṇa-pāṭha* verfügbar.

7. **Kātyāyanas *Vārttika*.** Dies sind *interpretatorische Notizen* zu den Sūtras, die von Patañjali diskutiert werden. Viele Sūtras können nicht korrekt angewendet werden, ohne das *vārttika* zu kennen, das sie qualifiziert. Das Projekt zitiert die *vārttika* überhaupt nicht.

`[YOUR INFERENCE]` Das Projekt hat die Aṣṭādhyāyī gelesen, als wäre sie eine *in sich geschlossene formale Spezifikation*. Das ist sie nicht. Sie ist ein *Regelwerk von Aphorismen*, das eine lebendige Kommentartradition voraussetzt. Die "Unbekannten" im Bavati-Trace sind keine Mysterien – es sind Dinge, die die *Siddhāntakaumudī* in einem einzigen Satz erklärt. Das Projekt hat versucht, den Kommentar aus dem Sūtra zurückzuentwickeln (Reverse Engineering), während der Kommentar die *Voraussetzung* für das Lesen des Sūtras ist.

---

### 7. Die primären und traditionellen Quellen, die das Projekt konsultieren muss, bevor es zu `panini-machine-model-v0.1` übergeht

`[TRADITIONAL INTERPRETATION]` Eine ernsthafte Rekonstruktion der *vyākaraṇa* muss sich mit der primären Kommentartradition auseinandersetzen, in etwa in dieser Reihenfolge der Autorität:

1. **Patañjalis *Mahābhāṣya*** (~2. Jh. v. Chr.). Der fundamentale Kommentar. Diskutiert, *warum* jedes Sūtra existiert, was es bedeutet und wo die Randfälle liegen. Ohne dieses Werk kann keine Rekonstruktion stattfinden. Verfügbar in der kritischen Ausgabe (Kielhorn, 1880-1885; überarbeitet von Kāśinātha Pāṇḍurang Parab). Das Projekt zitiert es nirgends. `anuvrtti.md` erwähnt es einmal namentlich; keine einzige Sūtra-Interpretation ist tatsächlich daran verifiziert.

2. **Kātyāyanas *Vārttika*.** Eingebettet im Mahābhāṣya. Dies sind die *interpretatorischen Ergänzungen* zu den Sūtras, oft die einzige Quelle dafür, wie ein bestimmtes Sūtra angewendet werden soll. Das Projekt zitiert sie nicht.

3. **Die *Kāśikā* von Jayāditya und Vāmana (~7. Jh. n. Chr.).** Der systematischste fortlaufende Kommentar zur Aṣṭādhyāyī. Dies ist das Standard-Referenzwerk für adhikāra-Grenzen, it-Bezeichnungen und die Anwendbarkeit von Regeln. Das Projekt erwähnt "die Kāśikā" zweimal im Vorbeigehen, hat sie aber nicht konsultiert.

4. **Bhaṭṭoji Dīkṣitas *Siddhāntakaumudī*** (~17. Jh.). Der *prakriyā*-Text, der die Aṣṭādhyāyī nach Ableitungstypen neu ordnet, nicht nach Sūtra-Reihenfolge. Dies ist der Text, aus dem man die Derivationen von *Bavati* und *dadAti* beziehen sollte – nicht sie zurückentwickeln. Das `rules.my` des Projekts leitet Bavati Schritt für Schritt ab, zitiert aber die *Kaumudī* nicht als Quelle für die Abfolge der Schritte.

5. **Nāgeśa Bhaṭṭas *Paribhāṣenduśekhara*** (~1700 n. Chr.). Die Systematisierung der paribhāṣā-s. Das Projekt zitiert dieses Werk namentlich in `paribhasha.md`, setzt sich aber nicht tatsächlich mit dessen *Argumenten* auseinander – es entlehnt lediglich die Liste der paribhāṣā-Namen.

6. **Der *Dhātupāṭha* (Kritische Ausgabe).** Das Projekt verwendet einen Dhātupāṭha, zitiert aber keine kritische Ausgabe. Der Standard ist die Böhtlingk-Ausgabe (1887) oder die neuere Ausgabe von S. M. Katre. Das Projekt muss seine 20 Wurzeln gegen mindestens eine von beiden verifizieren, nicht gegen "learnsanskrit.org".

7. **Der *Gaṇapāṭha*.** Die Hilfsliste der *gaṇa*-Mitglieder für taddhita- und kṛt-Derivationen. Wird im Projekt nirgendwo erwähnt.

8. **Die *Śikṣā*- und *prātiśākhya*-Literatur** – für die Rezension der Śiva-sūtras und den phonetischen Rahmen. Das `pratyahara.md` des Projekts verifiziert die Śiva-sūtras gegen eine Website, nicht gegen das *Ṛgveda-prātiśākhya* oder das *Taittirīya-prātiśākhya*, die die primären Quellen für die phonematische Organisation sind.

9. **George Cardona, *Pāṇini: His Work and Traditions*** (1988) und *Pāṇinian Studies* (Bd. 1-3). Das Projekt zitiert "Cardona" beiläufig, setzt sich aber nicht mit seinen detaillierten Analysen zu adhikāra, anuvṛtti und paribhāṣā auseinander, die die moderne wissenschaftliche Standardreferenz darstellen.

10. **Paul Kiparsky, *Pāṇinian Studies*** (verschiedene). Das Projekt zitiert "Kiparsky" als Quelle für die Prioritätshierarchie, aber Kiparskys Arbeit ist weitaus differenzierter als die vierstufige Zusammenfassung, die das Projekt verwendet. Seine Diskussionen zu *antaraṅga/bahiraṅga* (Kiparsky 1982, *Some Theoretical Problems in Pāṇini's Grammar*) sind substanziell und wurden nicht genutzt.

`[YOUR INFERENCE]` Die Quellenbasis des Projekts sind *sekundäre pädagogische Websites* und *der Quellcode von Vidyut*. Nichts davon ist eine primäre Quelle. Das Projekt hat ein "formales Fundament" aufgebaut, ohne das Mahābhāṣya zu lesen. Das ist das gravierendste methodische Versäumnis – und es ist korrigierbar, aber nur, wenn das Projekt die Arbeit am Maschinenmodell pausiert und den Kommentar liest.

---

### 8. Fünf Fälle, in denen eine scheinbare Analogie zu Programmiersprachen Pāṇini verzerrt

#### (i) "dhātu = function, kāraka = arguments, pratyaya = type-modifier"

`[YOUR INFERENCE]` Dies ist die implizite Architektur des Projekts (Klassentabelle `ontology.md`). Die Verzerrung: Bei Pāṇini "ruft" der *dhātu* seine *kāraka* nicht "auf". Kāraka-s sind *Bezeichnungen der Teilnehmer eines semantischen Ereignisses*, zugewiesen durch den Sprecher. Eine Funktion erhält Argumente *von ihrem Aufrufer*; der dhātu "erhält" keine kāraka-s – die kāraka-s sind in der *ākhyāta* (Äußerung) *ko-präsent* und werden unabhängig zugewiesen. Die Behandlung des dhātu als eine Funktion, die kāraka-Argumente "entgegennimmt", erzwingt eine "Aufrufer/Aufgerufener"-Asymmetrie, die in der Grammatik nicht existiert.

#### (ii) "saṃjñā = type system"

`[YOUR INFERENCE]` Ein Typsystem *beschränkt*, welche Ausdrücke wohlgeformt sind. Ein saṃjñā *ermöglicht den Verweis* auf eine Klasse. Dies sind entgegengesetzte Wirkungsrichtungen. Wenn *guṇa* ein Typ wäre, dann wäre ein Nicht-*guṇa*-Vokal ein "Typfehler" (type error). Bei Pāṇini ist ein Nicht-*guṇa*-Vokal einfach *nicht das, worauf sich das Wort guṇa bezieht* – es gibt keinen Fehler, nur die Nicht-Anwendbarkeit einer Regel. Die Typsystem-Analogie lässt die Grammatik so aussehen, als würde sie falsch typisierte Formen *ablehnen*, während sie nicht übereinstimmende Formen in Wirklichkeit *ignoriert*. Dies ist ein fundamentaler Verhaltensunterschied: Ein Type-Checker *hält an*; Pāṇinis Regelsystem *geht weiter*.

#### (iii) "anuvṛtti = lexical scope / closure"

`[YOUR INFERENCE]` Eine Closure *erfasst einen Wert zur Definitionszeit und trägt ihn mit sich*. Anuvṛtti ist eine *Leseanweisung*, die besagt: "Verstehe dieses Wort weiterhin als präsent". Die Closure trägt einen *Wert*; anuvṛtti trägt ein *Wort, das der Leser gedanklich ergänzen muss*. Kritischer noch: Der erfasste Wert einer Closure ist *innerhalb der Closure unveränderlich*; ein durch anuvṛtti übertragenes Wort kann *modifiziert* werden (ein späteres Sūtra kann eine modifizierte Version *anuvartayet*). Closures unterstützen keine Modifikation erfasster Variablen mitten im Scope. Die Analogie bricht an genau dem Merkmal zusammen, das sie erklären soll.

#### (iv) "vipratiṣedha = exception handling / try-catch"

`[YOUR INFERENCE]` Dies ist im `resolve-conflict`-Modell in `meta.my` implizit enthalten (Bedingungen der Reihe nach prüfen, der erste Treffer gewinnt). Exception Handling ist ein *Laufzeit-Kontrollflussmechanismus* – eine Exception *propagiert*, bis sie gefangen wird. Vipratiṣedha ist ein *Auswahlkriterium* – es propagiert nicht; es *wählt*. Es gibt kein "Werfen" (throwing) eines Konflikts. Der Konflikt *existiert* einfach (zwei Regeln treffen zu), und das Kriterium wählt eine aus. Die Modellierung als try/catch erzwingt eine Propagierungs-/Stack-Unwinding-Semantik, die keine Basis bei Pāṇini hat.

#### (v) "prakriyā (derivation) = state-transition log / Vec<Step>"

`[TEXTUAL EVIDENCE]` Die Tradition (Siddhāntakaumudī) präsentiert die prakriyā als eine *Abfolge von Schritten*, von denen jeder eine Operation auf die aktuelle Zeichenfolge anwendet.

`[YOUR INFERENCE]` Das von Vidyut inspirierte Modell `Vec<Step>` (H6) erscheint offensichtlich – und es ist die am *wenigsten* verzerrte der Analogien. Aber sie verzerrt dennoch in einer Hinsicht: In der Tradition ist die prakriyā *kein Protokoll dessen, was geschehen ist*; sie ist eine *Demonstration dessen, was geschehen muss*. Jeder Schritt ist *notwendig*, nicht nur *aufgezeichnet*. Ein Zustandsübergangsprotokoll (Log) ist *deskriptiv* (es zeichnet die Operationen der Maschine auf); eine prakriyā ist *präskriptiv* (sie zeigt den *einzigen* korrekten Weg auf). Wenn die Maschine einen anderen Weg nimmt und ihn protokolliert, ist das Protokoll *falsch* – es gibt in der Tradition keine Vorstellung von "alternativen gültigen Derivationen" für eine gegebene Eingabe. Das Log-Modell räumt dies stillschweigend ein, indem es deterministisch ist, aber es *repräsentiert* nicht die Normativität. Eine prakriyā nach Pāṇini ist näher an einem *Beweis* (proof) als an einem *Trace*.

---

### Abschließende Frage: Wenn dieses Projekt morgen sein Ziel aufgäbe, eine Lisp-Maschine zu bauen, hätte seine formale Rekonstruktion von Pāṇini dann immer noch einen wissenschaftlichen Wert?

`[YOUR INFERENCE]` **Nein – noch nicht.** Und hier ist, was sich ändern müsste.

Der aktuelle Wert des Projekts liegt fast ausschließlich in seiner *methodologischen Disziplin* – das dreistufige Tagging, das Hypothesen-Register, die Weigerung, Äquivalenzen ohne Beweise zu behaupten. Diese Disziplin ist wirklich selten und wirklich wertvoll. Aber die *Substanz* der Rekonstruktion ist noch nicht Pāṇini. Es ist eine *Lektüre von Sekundärquellen* (Vidyut, learnsanskrit.org, Kiparsky-Zusammenfassungen), gefiltert durch eine CS-Brille. Die Sūtras werden zitiert, aber nicht an kritischen Ausgaben verifiziert; die Kommentartradition wird benannt, aber nicht gelesen; die Derivationen werden aus dem Sūtra-Text rückentwickelt (reverse-engineered), anstatt sie aus der *Kaumudī* oder dem *Mahābhāṣya* zu entnehmen; grundlegende Konzepte (*lakāra*, *sārvadhātuka/ārdhadhātuka*, *upadeśa*, *lopa/ādeśa/āgama*, *tripādī*, *saṃhitā*, *svara*, *Gaṇapāṭha*) fehlen.

Wenn das Ziel der Lisp-Maschine aufgegeben würde, bliebe ein strukturiertes Notizbuch mit *vorläufigen Beobachtungen zu Pāṇini aus der Perspektive der Informatik*. Das ist als *Ausgangspunkt* nützlich, aber es ist keine *formale Rekonstruktion von Pāṇinis Grammatik*. Damit es zu einer wird, müsste sich Folgendes ändern:

1. **Die primäre Quelle müssen das Mahābhāṣya und die Kāśikā werden, nicht der Vidyut-Quellcode.** Vidyut ist eine *Implementierung* einer Lesart von Pāṇini. Es ist nicht Pāṇini. Es als Beweisgrundlage zu verwenden (wie es `it.md` explizit tut – "independently verified through real Vidyut code"), bedeutet, dass das Projekt *Vidyuts Pāṇini* rekonstruiert, nicht Pāṇinis Pāṇini.

2. **Die Derivationen müssen der Siddhāntakaumudī entnommen werden, nicht rückentwickelt.** Die "Unbekannten" bei Bavati würden sofort verschwinden. Das Projekt würde aufhören, *seine eigenen Lücken* für *Pāṇinis Lücken* zu halten.

3. **Die Ontologie muss die Konzepte umfassen, die die Tradition als grundlegend ansieht** – *lakāra*, *sārvadhātuka/ārdhadhātuka*, *upadeśa*, *lopa/ādeśa/āgama*, *tripādī*, *saṃhitā*, *pada*, *svara* – bevor sie *kāraka* als Graphenkanten modelliert. Die aktuelle Ontologie modelliert die *semantisch interessantesten* Konzepte zuerst (weil sie sich auf CS-Konstrukte abbilden lassen) und überspringt die *morphologisch tragenden* Konzepte (weil sie sich nicht so sauber abbilden lassen).

4. **Die paribhāṣā-Hierarchie muss bei Nāgeśa gelesen werden, bevor sie kodiert wird.** Die vierstufige Hierarchie in `paribhasha.md` ist eine *nachträgliche Rationalisierung*. Der Paribhāṣenduśekhara ist ein *ausführliches Argument* darüber, wie paribhāṣā-s zueinander in Beziehung stehen – es ist keine feste Prioritäten-Warteschlange.

5. **Das Projekt muss aufhören, CS-Analogien in den *Ontologie*-Dokumenten zu präsentieren.** Das dreistufige Tagging ist gut, aber die Abschnitte `[INTERPRETATION]` und `[MY-LISP HYPOTHESIS]` der *Fundamentaldokumente* verwenden immer noch CS-Vokabular ("Operator", "Transformator", "Ausführungskontext", "Thread", "Pattern-Matching"). Diese sickern durch *strukturelle Kontamination* in die `[PANINI]`-Abschnitte ein – das Pāṇini-Konzept wird in Begriffen beschrieben, die den CS-Rahmen voraussetzen. Ein echtes Pāṇini-Fundament würde den *dhātu* im Vokabular der *vyākaraṇa*-Tradition beschreiben (*kriyā*, *artha*, *prakṛti*, *vikaraṇa*, *lakāra*, *puruṣa*, *vacana*) und das CS-Vokabular vollständig einer separaten, explizit interpretatorischen Schicht überlassen.

Wenn diese fünf Änderungen vorgenommen würden – und die Lisp-Maschine wirklich vergessen wäre – würde das Projekt zu einer *wirklich wertvollen formalen Rekonstruktion von Pāṇini* werden: eine maschinenlesbare Ontologie, die auf der Kommentartradition basiert, mit nachvollziehbaren Herkunftsnachweisen von Sūtra-Zitaten und explizit gekennzeichneten Interpretationsschichten. Das wäre ein echter Beitrag zur *vyākaraṇa*-Forschung.

So wie es jetzt ist, *schützt das Projekt My Lisp vor Pāṇini* (indem es voreilige Äquivalenzen ablehnt), aber es *schützt Pāṇini noch nicht vor My Lisp* – weil das Vokabular und die konzeptuelle Reihenfolge der Fundamentaldokumente von jener Maschine geprägt sind, die das Projekt bauen will. Die Reihenfolge der Untersuchung ist immer noch: "Was kann Pāṇini für unsere Maschine tun?" statt "Was ist Pāṇinis Grammatik, unabhängig von irgendeiner Maschine?"

An dem Tag, an dem sich diese Reihenfolge umkehrt – an dem Tag, an dem sich die Fundamentaldokumente wie ein *śāstra*-Text lesen und nicht wie ein CS-Design-Dokument – wird das Projekt einen wissenschaftlichen Wert aus sich selbst heraus haben. Bis dahin ist es eine wertvolle *Methodik* auf der Suche nach einem *Inhalt*, den es noch nicht erlangt hat.

