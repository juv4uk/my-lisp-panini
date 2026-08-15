# anuvṛtti / adhikāra: Context Inheritance and Scope

## English
This document establishes the formal epistemology of the **anuvṛtti** (continuation) and **adhikāra** (governing domain) systems in Pāṇini's grammar. It strictly separates the traditional source material from computational hypotheses.

## Українська
Цей документ встановлює формальну епістемологію систем **anuvṛtti** (успадкування контексту) та **adhikāra** (область дії) у граматиці Паніні. Він строго відокремлює традиційне джерельне знання від обчислювальних гіпотез.

## Deutsch
Dieses Dokument begründet die formale Epistemologie der **anuvṛtti**- (Fortsetzung) und **adhikāra**- (Geltungsbereich) Systeme in Pāṇinis Grammatik. Es trennt strikt das traditionelle Quellenmaterial von rechnergestützten Hypothesen.

---

## [PANINI]

**Source Anchor:** Aṣṭādhyāyī 1.3.11 (svaritenādhikāraḥ), 1.4.23 (kārake), 3.1.1 (pratyayaḥ).

In the Pāṇinian system, a rule (sūtra) is rarely complete on its own. It inherits missing words or conditions from preceding rules.

### Key Principles

1. **anuvṛtti (Continuation/Ellipsis):** 
   - A word or phrase stated in one sūtra does *not* need to be repeated in subsequent sūtras if it continues to apply. 
   - It is a method of reading the text where each sūtra is interpreted alongside a carried-over context from preceding rules, until that context is explicitly canceled, blocked, or replaced.

2. **adhikāra (Governing Domain):** 
   - A formally marked, long-acting variety of `anuvṛtti`. A word or phrase "governs" (`adhikriyate`) an entire block of sūtras up to the end of a section.
   - **Sūtra 1.3.11 (svaritenādhikāraḥ):** States that an `adhikāra` is indicated (in oral recitation) by the *svarita* pitch accent. This proves the text consciously distinguished between short-term `anuvṛtti` and long-term `adhikāra` domains.

3. **Examples of Scope:**
   - **Short Scope (`kārake`, 1.4.23):** Opens the section on semantic roles. It governs about 33 sūtras (1.4.24–1.4.55).
   - **Long Scope (`pratyayaḥ`, 3.1.1):** Opens the section on affixes. Its scope extends across three entire chapters (up to 5.4.160), governing thousands of rules, and contains its own nested `adhikāra`s (like `kṛt` and `taddhita`).

4. **Termination of Scope:**
   - The text does not contain explicit "closing" markers (like a closing bracket).
   - An `adhikāra` applies until a subsequent `adhikāra` rule of the same level overrides it.
   - The exact boundaries are sometimes deduced via *maṇḍūkapluti* (frog-leap, where a rule jumps over intermediate rules) or established by the commentarial tradition (Kāśikā, Mahābhāṣya).

## [SCHOLARLY INTERPRETATION]

Modern linguistic and Indological scholarship (e.g., Joshi and Roodbergen, Kiparsky) views `anuvṛtti` as a highly sophisticated form of text compression (lāghava).

- **Mechanical vs. Semantic:** There is an ongoing debate about whether `anuvṛtti` flows strictly mechanically (everything flows down until blocked) or if semantic compatibility dictates what flows (a word only flows if the subsequent rule semantically expects it).
- **Network of Rules:** Kiparsky argues that Pāṇini's rules are not just a linear list but a network, where `adhikāra` headers act as super-nodes that distribute properties to child nodes.
- **Cancelation (nivṛtti):** The mechanism by which a flowing word stops flowing when an incompatible word of the same grammatical category appears.

## [COMPUTATIONAL INTERPRETATION]

Formally, `anuvṛtti` and `adhikāra` can be modeled as **Execution Contexts**, **Lexical Scoping**, or **Stateful Inheritance**.

- **Context Inheritance:** Instead of evaluating a rule in isolation `evaluate(Rule_N, Token)`, the system evaluates it within a state `evaluate(Rule_N, Token, Context_State)`. 
- **Lexical Scoping:** `adhikāra` functions similarly to lexical scoping blocks in programming (`{ ... }` or `with ...`). Variables declared at the start of the block are implicitly available to all statements within the block.
- **Stack Frames:** An `adhikāra` pushes a frame onto an environment stack. Nested `adhikāra`s push new frames. When the domain ends, the frame is popped. The computational challenge is detecting the "pop" condition without explicit closing syntax.

## [MY-LISP HYPOTHESIS]

How can My Lisp model this context-inheritance system natively to support Proof-Carrying Derivations?

- **Hypothesis 1 (Dynamic Environment/`with-adhikara`):** My Lisp could introduce a native `(with-adhikara (pratyaya) ...)` macro. All rules defined within this macro implicitly receive `pratyaya` in their pattern-matching condition. This maps the flat list of sūtras into a deeply nested tree.
- **Hypothesis 2 (State Machine of Contexts):** Instead of nesting, the inference engine maintains an `active-context` object. As the engine steps through rules `R1 -> R2 -> R3`, it mutates this `active-context`. 
- **Hypothesis 3 (Proof Propagation):** In a Proof-Carrying Derivation, if rule 3.1.2 applies to a token because it's in the `pratyaya` domain, the proof graph must explicitly show: `Applied Rule 3.1.2 (inherited context: 3.1.1 pratyaya)`. The origin of the context must be part of the trace.
