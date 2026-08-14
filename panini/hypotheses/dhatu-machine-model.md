# Machine Models for dhātu

## Hypothesis: The Dhātu Registry

This document defines the computational representation of a **dhātu** in the My Lisp/VM ecosystem. It is an explicitly provisional machine model, separate from historical claims.

### H1: The Dhātu as a First-Class Language Unit

In our inference engine, a `dhātu` is a first-class lexical atom. There is no assumption that it directly corresponds to a `cons`, `car`, or `cdr`. It acts as a data record injected into the rule engine.

### H2: The Registry Schema

The computational registry records canonical SLP1, source identity, properties, and evidence status before any derivation takes place. 

```yaml
canonical: <SLP1>
display:
  iast: <IAST>
  devanagari: <देवनागरी>
class: dhatu
gana: <1-10>
pada: <parasmaipada|atmanepada|ubhayapada>
set_anit: <seT|aniT|unknown>
source:
  dhatupatha: <gaṇa name/number, sequence number if known>
traditional_meaning: <short paraphrase>
notes: <caveats, variants, computational notes>
```

### Initial Baseline Registry (20 Roots)

This selection spans different `gaṇa` and behaviors to ensure the derivation engine is tested against variety, not just regular roots.

```yaml
canonical: BU
display: { iast: bhū, devanagari: भू }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaṇa 1), first root" }
traditional_meaning: "to be, become"
notes: "The canonical 'first' dhātu. Sūtra 1.3.1 refers to the entire class via 'bhūvādayaḥ'."

---
canonical: kf
display: { iast: kṛ, devanagari: कृ }
class: dhatu
gana: 8
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "tanAdi (gaṇa 8)" }
traditional_meaning: "to do, make"
notes: "Highly frequent; irregular/suppletive behavior in many forms (e.g., karo-/kuru-)."

---
canonical: gam
display: { iast: gam, devanagari: गम् }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to go"
notes: "The nasal drops in several derivatives (e.g., gata, not gamta)."

---
canonical: sTA
display: { iast: sthā, devanagari: स्था }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to stand"
notes: "Ends in a long vowel, exhibiting different guṇa/vṛddhi behavior compared to consonants."

---
canonical: dA
display: { iast: dā, devanagari: दा }
class: dhatu
gana: 3
pada: ubhayapada
set_anit: aniT
source: { dhatupatha: "juhotyAdi (gaṇa 3)" }
traditional_meaning: "to give"
notes: "Class 3 (reduplicating class) — base is dadā-ti."

---
canonical: nI
display: { iast: nī, devanagari: नी }
class: dhatu
gana: 1
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to lead"
notes: "Common example for ditransitive/complex kāraka relations."

---
canonical: paW
display: { iast: paṭh, devanagari: पठ् }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to read, recite"
notes: "Regular root, good baseline test case."

---
canonical: liK
display: { iast: likh, devanagari: लिख् }
class: dhatu
gana: 6
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "tudAdi (gaṇa 6)" }
traditional_meaning: "to write"
notes: "Class 6 — takes vikaraṇa 'a' with accent on the affix."

---
canonical: dfS
display: { iast: dṛś, devanagari: दृश् }
class: dhatu
gana: 1
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to see"
notes: "Suppletive in several tenses/moods (e.g., paśyati vs dadarśa)."

---
canonical: Buj
display: { iast: bhuj, devanagari: भुज् }
class: dhatu
gana: 7
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "rudhAdi (gaṇa 7)" }
traditional_meaning: "to eat; to enjoy"
notes: "Meaning systematically depends on the parasmaipada/ātmanepada choice."

---
canonical: pac
display: { iast: pac, devanagari: पच् }
class: dhatu
gana: 1
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to cook"
notes: "Standard pedagogical example for kāraka roles."

---
canonical: vac
display: { iast: vac, devanagari: वच् }
class: dhatu
gana: 2
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "adAdi (gaṇa 2)" }
traditional_meaning: "to speak"
notes: "Athematic class (no vowel vikaraṇa)."

---
canonical: Sru
display: { iast: śru, devanagari: श्रु }
class: dhatu
gana: 5
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "svAdi (gaṇa 5)" }
traditional_meaning: "to hear"
notes: "Class 5 takes the vikaraṇa 'nu/no'."

---
canonical: jYA
display: { iast: jñā, devanagari: ज्ञा }
class: dhatu
gana: 9
pada: ubhayapada
set_anit: aniT
source: { dhatupatha: "kryAdi (gaṇa 9)" }
traditional_meaning: "to know"
notes: "Class 9 takes the vikaraṇa 'nā/nī'."

---
canonical: BAz
display: { iast: bhāṣ, devanagari: भाष् }
class: dhatu
gana: 1
pada: atmanepada
set_anit: seT
source: { dhatupatha: "bhvAdi (gaṇa 1)" }
traditional_meaning: "to speak"
notes: "Exclusively ātmanepada."

---
canonical: as
display: { iast: as, devanagari: अस् }
class: dhatu
gana: 2
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "adAdi (gaṇa 2)" }
traditional_meaning: "to be (copula)"
notes: "Highly irregular, suppletive with 'bhū'. Critical for copular constructions."

---
canonical: iz
display: { iast: iṣ, devanagari: इष् }
class: dhatu
gana: 6
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "tudAdi (gaṇa 6)" }
traditional_meaning: "to desire, seek"
notes: "Complex kāraka behavior for verbs of desiring."

---
canonical: BI
display: { iast: bhī, devanagari: भी }
class: dhatu
gana: 3
pada: parasmaipada
set_anit: seT
source: { dhatupatha: "juhotyAdi (gaṇa 3)" }
traditional_meaning: "to fear"
notes: "Classic example for apādāna kāraka (source of fear)."

---
canonical: yuj
display: { iast: yuj, devanagari: युज् }
class: dhatu
gana: 7
pada: ubhayapada
set_anit: seT
source: { dhatupatha: "rudhAdi (gaṇa 7)" }
traditional_meaning: "to join, yoke"
notes: "Takes an infix nasal vikaraṇa."

---
canonical: han
display: { iast: han, devanagari: हन् }
class: dhatu
gana: 2
pada: parasmaipada
set_anit: aniT
source: { dhatupatha: "adAdi (gaṇa 2)" }
traditional_meaning: "to kill, strike"
notes: "Highly irregular athematic root. Excellent stress-test for the derivation model."
```

### Open Questions for the Implementation
1. **Raw vs. Processed `it` Markers**: Does the machine registry need to store the raw Dhātupāṭha form with all its *it* markers, or is it sufficient to store the post-processed `set_anit` and `pada` flags as currently modeled? (Ties into `PANINI-IT-MARKERS`).
2. **Role of `gaṇa`**: Is the *gaṇa* purely a morphological implementation detail for `PANINI-PRATYAYA-DERIVATION` (determining which *vikaraṇa* to load), or does it have deeper semantic/systemic implications for the foundation layer?
