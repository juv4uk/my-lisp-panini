# dhātu · dhātu · dhātu

`dhātu` (verbal root) — fundamental category of Pāṇinian grammar.
`dhātu` (дієслівний корінь) — фундаментальна категорія граматики Паніні.
`dhātu` (Verbalwurzel) — Grundkategorie der Grammatik Pāṇinis.

## [PANINI]

**Source anchor:** Aṣṭādhyāyī 1.3.1 (*bhūvādayo dhātavaḥ*).

A *dhātu* is not derived by the Aṣṭādhyāyī; it is assumed from an external,
given list — the *Dhātupāṭha*, a catalogue of roughly 2,000 roots divided
into ten classes (*gaṇa*). Sūtra 1.3.1 simply states that the items beginning
with *bhū* [in the Dhātupāṭha] are called *dhātu*.

Traditional structure recorded with each root:

- **gaṇa (class 1–10)** — determines which thematic affix (*vikaraṇa*) is
  inserted between root and personal ending; a purely morphological
  classification, independent of meaning.
- **it-markers (anubandha)** — metalinguistic markers in the Dhātupāṭha entry
  indicating behaviour such as *seṭ/aniṭ* status or voice; deleted before the
  root enters derivation.
- **pada** — *parasmaipada*, *ātmanepada*, or *ubhayapada*.
- **Semantic paraphrase** — a brief gloss traditional in the Dhātupāṭha
  tradition (Kṣīrasvāmin and others).

The *dhātu* is also the derivational source of a large portion of nominal
vocabulary through *kṛt* affixes (participles, action nouns).

## [SCHOLARLY INTERPRETATION]

Modern descriptive grammar reads the Dhātupāṭha as a lexical root inventory:
the *gaṇa* classes group roots by their morphological behaviour (which
*vikaraṇa* they take), not by semantics — roots of similar meaning may sit in
different classes. The root-plus-affixation model parallels the root/stem
distinction of general morphology, but Pāṇini's system is stricter: every
derived form must be traceable to a listed root through stated rules, and the
*it*-marker mechanism provides an explicit, deletable carrier of lexical
exceptions inside the lexicon itself.

## [COMPUTATIONAL INTERPRETATION]

Formally, the Dhātupāṭha is an **external lexicon table**: each entry carries
a root identifier, a class attribute (*gaṇa*), and a set of boolean/enum
flags corresponding to *it*-markers. Derivation composes three inputs:
root entry + selected *vikaraṇa* (dispatched by class) + ending set
(*tiṅ*). Marker deletion is a preprocessing pass that strips flag carriers
before any operational rule sees the root.

## [MY-LISP HYPOTHESIS]

We want the Dhātupāṭha as a data table in my-lisp (a root registry), where:

- each entry carries `gaṇa` and *seṭ/aniṭ*/*pada* flags as structured fields;
- *it*-deletion becomes an explicit preprocessing pass over the state;
- *gaṇa* → *vikaraṇa* selection is ordinary rule dispatch;
- every use of a root in a derivation cites its registry entry, feeding the
  proof-carrying derivation chain.
