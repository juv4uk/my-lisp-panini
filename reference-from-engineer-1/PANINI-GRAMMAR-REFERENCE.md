# Pāṇini Grammar Reference
## A working reference for the Sanskrit semantic migration (SANSKRIT-P1..P9)

> **Erratum (added 2026-08-13, PANINI-SLP1-LEXICON-ALIGNMENT / cross-referenced
> against `my-lisp-panini`'s `panini/research/dhatupatha-verification.md` and
> `panini/foundation/terminology.md#знайдені-й-виправлені-розбіжності`):**
> §8.2 below states the sibilant convention as `ś=z, ṣ=S`. This is backwards.
> Verified against `vidyut-prakriya/src/sounds.rs` (articulation-place
> classification, the most authoritative source checked) and independently
> matching `my-lisp`'s own `crates/my-lisp/src/semantic/transliteration.rs`
> (verified 2026-08-12 against Wikipedia's SLP1 article): the correct mapping
> is **`ś = S`, `ṣ = z`**. `my-lisp-panini` already found and corrected this
> (3 dhātu were briefly mis-transliterated under the wrong rule before being
> caught and reverted). This copy is left otherwise unedited — treat §8.2's
> sibilant line as superseded by this note, not as a live claim.

Author: engineer-1
Date: 2026-08-12
Audience: my-lisp-1 (Sanskrit phases), cml (IR/backend), swarm at large.
Status: reference document — root/word senses listed here are *working* senses
and must be confirmed against an authoritative lexicographic source
(Monier-Williams, Apte, or the on-line Sanskrit Lexicon) before being filed as
semantic atoms, per the SANSKRIT-P2/SS34 ethos ("verify against an
authoritative source, not memory").

---

## 1. What the Aṣṭādhyāyī is

The *Aṣṭādhyāyī* ("Eight Chapters") is Pāṇini's generative grammar of
Classical Sanskrit, composed ~4th century BCE. It is the earliest known
generative/formal grammar in any language and an explicit design ancestor of
Backus–Naur form.

- 8 *adhyāya*s, each divided into 4 *pāda*s → 32 *pāda*s.
- ≈4,000 *sūtra*s (rule aphorisms), traditionally counted as 3,959.
- Rules are ordered: later rules apply after earlier ones (the "elsewhere"
  / specificity ordering principle — *utsarga-apavāda* = general-rule then
  exception).

Rule kinds (relevant because SANSKRIT-P1-DESIGN-DECISIONS asks whether
semantic machinery is "language semantics or implementation"; Pāṇini mixes
both and separates them by *rule kind*):

| Kind          | Sanskrit  | Meaning / example                              |
|---------------|-----------|------------------------------------------------|
| technical term| *saṃjñā*  | defines a term used by the system              |
| heading       | *adhikāra*| opens a rule domain that governs until closed  |
| continuation  | *anuvṛtti*| a term "continues" down a series of rules      |
| operational   | *vidhi*   | does something (replace, delete, affix, …)     |
| restriction   | *niyama*  | limits another rule                            |
| extension     | *atideśa* | "treat X as Y"                                 |
| meta-rule     | *paribhāṣā*| interpretive maxim (e.g. "a rule takes effect as soon as its cause is given") |

**Relevance**: the migration's own layered design (tokenizer → parser → atom
resolver → semantic AST → IR) mirrors the Pāṇinian separation between
phonological sandhi, morphological derivation, and semantic role assignment.

---

## 2. Sound inventory and the Śivasūtras

The *Śivasūtras* (also *Śivasūtrāṇi*, the 14 mnemonic lines ending in a
marker consonant) arrange the phonemes in a tight order so that a *pratyāhāra*
(abbreviation "X from first sound up to marker") names a class:

```
a i u ṛ ḷ e o ai au h y v r l ñ       (ac = vowels in this range)
ṇ   ṅ ṇ n m  …                         (etc.)
```

Examples:
- `aC` = vowels (all simple vowels/diphthongs in order).
- `haL` = all consonants (h + ḻ list).
- `yaN` = y v r l (semivowels).
- `jhaL` = all stops+fricatives (a common trigger class for sandhi).

Implication for P1-TRANSLITERATION: the SLP1 scheme is built to preserve this
contrast set exactly (see §8). A transliteration library that loses any of
these 3-way consonant distinctions (dental/retroflex/palatal) cannot express
Pāṇinian rules.

## 3. Morphology

### 3.1 Nominal inflections — the 7 *vibhakti*s (+ vocative)

| Case            | Sanskrit term | Pāṇinian use                          |
|-----------------|---------------|---------------------------------------|
| Nominative      | *prathamā*    | subject / predicate of a sentence     |
| Accusative      | *dvitīyā*     | karman (direct object)                |
| Instrumental    | *tṛtīyā*      | karaṇa (instrument); also kartṛ        |
| Dative          | *caturthī*    | sampradāna (recipient)                |
| Ablative        | *pañcamī*     | apādāna (source)                      |
| Genitive        | *ṣaṣṭhī*      | possession; not a kāraka              |
| Locative        | *saptamī*     | adhikaraṇa (locus)                    |
| Vocative        | *sambodhana*  | address                               |

Numbers: *ekavacana* (sg), *dvivacana* (dual), *bahuvacana* (pl).
Genders: *puṃliṅga* (m), *strīliṅga* (f), *napuṃsakaliṅga* (n).

### 3.2 Verbal morphology — root → stem → inflected form

- *dhātu* = the bare root (e.g. `kf` kṛ "do").
- *vikaraṇa* = the class marker inserted between root and ending; the 10
  *gaṇa*s are distinguished precisely by this marker:
  1. *bhvādi*    (√bhū)    class 1, `-a-`        (gam → gacch-a-ti)
  2. *adādi*     (√ad)     class 2, no marker   (ad → at-ti)
  3. *juhotyādi* (√hu)     class 3, reduplication (juhu → ju-ho-ti)
  4. *divādi*    (√div)    class 4, `-ya-`       (nṛt → nṛty-a-ti)
  5. *svādi*     (√su)     class 5, `-nu-`       (su → su-no-ti)
  6. *tudādi*    (√tud)    class 6, `-a-`        (tud → tud-a-ti)
  7. *rudhādi*   (√rudh)   class 7, nasal infix  (rudh → ru-ṇ-dh-…)
  8. *tanādi*    (√tan)    class 8, `-o-`        (tan → tan-o-ti)
  9. *kryādi*    (√krī)    class 9, `-nā-`       (krī → krī-ṇā-ti)
  10. *curādi*   (√cur)    class 10, `-aya-`     (cur → cōray-a-ti)
- *pada* classes: *parasmaipada* (active "for another") and *ātmanepada*
  (middle "for oneself").
- Tenses/moods *(lakāra)*: present, imperfect, perfect, aorist, future,
  conditional, imperative, optative, subjunctive(+benefactive per some).

The P3-DHATU-CORE task's 12 roots and their *working* gaṇa assignments:

| SLP1  | Deva         | Root  | Gaṇa    | Working sense (confirm per source) |
|-------|--------------|-------|---------|------------------------------------|
| kf    | कृ           | kṛ    | 8 (tan)| do, make, act on                    |
| gam   | गम्          | gam   | 1 (bhv)| go, move, reach                     |
| dA    | दा           | dā    | 3 (juh)| give, grant                         |
| grah  | ग्रह्        | grah  | 9 (kry)| seize, grasp, take                  |
| jYA   | ज्ञा         | jñā   | 9 (kry)| know, perceive                      |
| dfS   | दृश्         | dṛś   | 1 (bhv)| see, view                           |
| Sru   | श्रु         | śru   | 5 (svā)| hear, listen                        |
| vac   | वच्         | vac   | 2 (ad) | speak, say                          |
| liK   | लिख्         | likh  | 6 (tud)| write, scratch                      |
| paW   | पठ्          | paṭh  | 1 (bhv)| read, recite                        |
| sTA   | स्था         | sthā  | 1 (bhv)| stand, stay                         |
| BU    | भू           | bhū   | 1 (bhv)| become, be                          |

> The migrators' own examples already match this model: `(dA :kartf server
> :karman packet :sampradAna client)` = dā + kartṛ + karman + sampradāna,
> i.e. "the server gives the packet to the client."

## 4. The six *kāraka*s — semantic roles

Pāṇini's key insight: *kāraka* = a *semantic* role assigned to a participant
*by* the action of the verb; cases (vibhakti) are then *derived from* the
kāraka. This is exactly the SANSKRIT-P5 requirement ("AST carries semantic
IDs, not raw strings").

The defining sūtras (Pāṇini 1.4):

| Kāraka       | SLP1 in tasks | Defining sūtra (working gloss)                 |
|--------------|---------------|------------------------------------------------|
| apādāna      | apAdAna       | P.1.4.24 *dhruvam apāye 'pādānam* — the fixed point from which departure takes place |
| sampradāna   | sampradAna    | P.1.4.32 *karmaṇā yam abhipraiti sa sampradānam* — the one the agent intends to be reached by the object |
| karaṇa       | karaRa        | P.1.4.42 *sādhakatamaṁ karaṇam* — the most effective means (instrument) |
| adhikaraṇa   | aDikaraRa     | P.1.4.45 *ādhāro 'dhikaraṇam* — the locus, the support/substratum |
| karman       | karman        | P.1.4.49 *kartur īpsitatamaṁ karma* — what the agent most wishes to attain |
| kartṛ        | kartf         | P.1.4.54 *svatantraḥ kartā* — the independent agent |

Note the derivation order in the sūtras (apādāna → sampradāna → karaṇa →
adhikaraṇa → karman → kartṛ): Pāṇini *defines the more restricted roles
first*, and kartṛ (the independent one) last, as the default when nothing
else applies. A semantic role-assignment algorithm can apply the same
specificity ordering.

### 4.1 kāraka vs. case — the crucial distinction

- kāraka = semantic role (level of the semantic AST, SANSKRIT-P5).
- vibhakti = surface case ending (level of morphology / string).
- The mapping kāraka→vibhakti is regular but not 1:1 (kartṛ → nominative, but
  an instrumental *kartṛ* is possible in passive constructions; the genitive
  is explicitly *not* a kāraka, P.1.4.1-2 style boundary).

This distinction is why P4's example `(dA :kartf … :karman … :sampradAna …)`
is the right level of abstraction: the AST should carry *kāraka* labels, and
the transliteration layer only ever concerns itself with strings (P1).

## 5. *upasarga* — preverbs

22 traditional *upasargas* (Pāṇini P.1.4.59-60, *upasargāḥ kriyāyoge*):

```
pra  parā  apa  sam  ni  nis  vi  ā  upa  abhi  ati  adhi  api  anu  prati
su   dur  (and:  ūṛ, ... some lists differ in count)
```

Each modifies the meaning of a dhātu (e.g. `gam` go + `ā` → *ā-gacch* come
near; `kf` do + `pari` → "make around", "attend"). For the atom registry
(P2) an upasarga should be its own atom kind with its own semantic ID,
because root+upasarga composition is productive and must be lowerable
compositionally, not as a flat string.

## 6. *sandhi* — phoneme-joining rules

Pāṇini's phonological layer is explicit and complete enough to be the model
for a deterministic transducer. Core classes:

- **Vowel sandhi**: `a`/`ā` + `i`/`ī` → `e`; `a` + `u`/`ū` → `o`;
  `a` + `ṛ` → `ar`; `a` + `e` → `ai`; `a` + `o` → `au`; long-vowel
  simplification; guṇa/vṛddhi strength (a, ā); deletion of final `a` before
  a vowel, etc.
- **Visarga sandhi**: `ḥ` → `s`/`r`/`o` before certain sounds (e.g. before a
  voiceless stop `ḥ` becomes `s` with sibilant assimilation `kḥ`→`kṣ`).
- **Consonant sandhi**: internal (word-internal, *abhyantara*) vs. external
  (word-boundary, *bahiraṅga*) — the external rules are exactly what a
  tokenizer must *undo* to recover the base word forms.
- Voice/aspiration assimilation: `t` + `bh` → `ddh` (e.g. *tat* + *bhavati*
  → *tad bhavati*, then *taddhavati*).

Relevance to P1: the round-trip property required (SLP1→IAST→SLP1 canonical)
is only testable if the test corpus is *sandhi-aware*; an authoritative
lexicographic source gives the *pada* (unjoined) form, so the library should
be tested on pada-level entries first and on joined text only after a sandhi
splitter exists (out of scope for P1 but worth noting in the test plan).

## 7. Compounds (*samāsa*)

Useful as the analog for the migration's "old builtins lower to semantic IDs
via aliases" idea (P6): compounds are *compositional* units parsed into
parts, and their semantics = function of parts + class:

| Class             | Relation                                      |
|-------------------|-----------------------------------------------|
| tatpuruṣa         | dependent-determinative (X of Y)              |
| karmadhāraya      | appositional ("X which is Y")                 |
| dvandva           | coordination ("X and Y")                      |
| bahuvrīhi         | exocentric ("possessing X", an adjective)     |
| avyayībhāva       | indeclinable                                  |
| dvigu             | numeral bahuvrīhi ("counting X")              |

## 8. Transliteration maps (for P1)

Three notations the tasks use interchangeably; the library must cover all
three with a lossless round-trip (IAST ↔ SLP1 minimal; Devanāgarī ↔ SLP1 for
the atom registry display layer).

### 8.1 Vowels

| Deva | IAST | SLP1 |  | Deva | IAST | SLP1 |
|------|------|------|--|------|------|------|
| अ    | a    | a    |  | आ    | ā    | A    |
| इ    | i    | i    |  | ई    | ī    | I    |
| उ    | u    | u    |  | ऊ    | ū    | U    |
| ऋ    | ṛ    | f    |  | ॠ    | ṝ    | F    |
| ऌ    | ḷ    | x    |  | ॡ    | ḹ    | X    |
| ए    | e    | e    |  | ऐ    | ai   | E    |
| ओ    | o    | o    |  | औ    | au   | O    |
| अं   | ṃ (anusvāra) | M |  | अः  | ḥ (visarga) | H |

### 8.2 Consonants (stops — the contrast the tasks must never collapse)

| Class      | voiceless | voiceless asp. | voiced | voiced asp. | nasal |
|------------|-----------|----------------|--------|-------------|-------|
| velar      | k  K      | kh  K        | g  G   | gh  G      | ṅ  N |
| palatal    | c  c      | ch  C        | j  j   | jh  J      | ñ  Y |
| retroflex  | ṭ  w      | ṭh  W       | ḍ  q   | ḍh  Q      | ṇ  R |
| dental     | t  t      | th  T        | d  d   | dh  D      | n  n |
| labial     | p  p      | ph  P        | b  b   | bh  B      | m  m |

(SLP1 glyphs for sibilants: ś=z, ṣ=S, s=s; semivowels y v r l; aspirate h=h.
— *glyphs shown are the working convention; verify against the my-lisp SLP1
module's own table before wiring the library.*)

### 8.3 Round-trip test set (P1 acceptance candidates)

- vocalic ṛ: `kf` कृ kṛ; `f` ऋ ṛ; `fma` ऋम ṛma
- retroflex: `paW` पठ् paṭh; `dfS` दृश् dṛś; `WA` ठा ṭhā
- palatals: `jYA` ज्ञा jñā; `Sru` श्रु śru; `cC` च्छ cch
- aspirates: `liK` लिख् likh; `gR` घृ ghṛ; `BU` भू bhū
- anusvāra/visarga: `AM` अं aṃ; `kaH` कः kaḥ
- long vowels: `dA` दा dā; `sTA` स्था sthā; `nI` नी nī
- everything combined: `saMskftam` संस्कृतम् saṃskṛtam

## 9. Mapping to the SANSKRIT-P1..P9 tasks

| Task | Pāṇini layer it consumes |
|------|--------------------------|
| P1-TRANSLITERATION | §8 tables + §2 sound inventory (lossless contrast set) |
| P1-DESIGN-DECISIONS | §1 rule-kinds analogy (semantics vs. implementation) |
| P2-ATOM-REGISTRY | §3.2 dhātu list, §5 upasarga list, §8 orthography fields (slp1/iast/deva) |
| P3-DHATU-CORE | §3.2 gaṇa table + working senses (verify per source) |
| P4-KARAKA-LAYER | §4 six kārakas + §4.1 role-vs-case distinction |
| P5-AST-SEMANTIC-IDS | §4 kāraka labels as AST nodes; §7 composition model |
| P6-COMPAT-ALIASES | §7 compounds-as-composition analogy (old English builtin → semantic ID) |
| P9-FPGA-OPCODE-BOUNDARY | §8 note: SLP1/IAST/Deva must *never* reach the ISA; only semantic IDs → opcodes |

## 10. Sources to verify against (per the "not memory" rule)

- Monier-Williams *Sanskrit–English Dictionary* (MW).
- Apte *Practical Sanskrit–English Dictionary*.
- Online Sanskrit Lexicon / Cologne Digital Sanskrit Lexicon (U. Cologne).
- Pāṇini Aṣṭādhyāyī critical text; Kāśikāvṛtti commentary for kāraka sūtras
  (P.1.4.24–54).
- Any Pāṇinian sūtra number cited here (P.1.4.n) must be double-checked
  against the critical edition before use in the language contract.
