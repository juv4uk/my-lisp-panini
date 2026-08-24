# pratyaya · pratyaya · pratyaya

`pratyaya` (suffix/affix) — fundamental category of Pāṇinian grammar.
`pratyaya` (суфікс/афікс) — фундаментальна категорія граматики Паніні.
`pratyaya` (Suffix/Affix) — Grundkategorie der Grammatik Pāṇinis.

## [PANINI]

**Source anchors:** Aṣṭādhyāyī 3.1.1 (*pratyayaḥ*), 3.1.2 (*paraś ca*);
affix section 3.1.1–5.4.159.

A *pratyaya* is any suffix attached to a base (*prakṛti*/*aṅga* — either a
*dhatu* or a *prātipadika*) to produce a derived form. The section opens with
an *adhikāra* pair: 3.1.1 introduces the category; 3.1.2 restricts position —
the affix occurs **after** the base, never before.

Traditional classification:

- **kṛt** — primary suffixes on a *dhatu* forming nominal bases
  (participles, action nouns); application conditions frequently reference a
  semantic *kāraka* role (e.g., suffix *kta* when the meaning is *karman*).
- **taddhita** — secondary suffixes on a *prātipadika* forming further nominal
  bases (patronymics etc.).
- **vikaraṇa** — thematic affixes inserted between *dhatu* and personal
  ending, specific to the root's *gaṇa*.
- **tiṅ / sup** — verbal personal endings and nominal case endings.

An affix addition typically triggers morphophonemic changes (*guṇa*,
*vṛddhi*) in the base; *it*-markers on the affix explicitly block or mandate
these changes. A typical prescribing sūtra states: (a) the base, (b) the
semantic condition (*artha* or *kāraka*), and (c) the affix — derivation is
semantically conditioned, rarely purely morphological.

## [SCHOLARLY INTERPRETATION]

Modern descriptive grammar treats this as a rule-governed word-formation
system where suffix choice is conditioned by both morphological class and
lexical semantics — the *kāraka*-referencing conditions of *kṛt* affixes are
the classical example of semantic conditioning inside an otherwise formal
apparatus. The four-way suffix taxonomy (kṛt/taddhita/vikaraṇa/tiṅ-sup) plus
the adhikāra positioning convention constitute the structural backbone of
the derivational section (3.1–5.4).

## [COMPUTATIONAL INTERPRETATION]

A *pratyaya* prescription is a **guarded transformation rule**: precondition
= (base-class predicate, optional semantic condition), action = attach affix
identifier, side-effect = trigger/block morphophonemic rules via carried
flags. The 3.1.2 positional constraint is a scope declaration; *it*-markers
are control flags that enable or suppress downstream phonological rules.

## [MY-LISP HYPOTHESIS]

We want a suffix registry where each entry carries:
(base-class predicate, semantic-condition predicate, affix id, flag set).
Semantic conditions become predicates over *kāraka*-role annotations in the
derivation state; flag sets drive the block/mandate logic of the
morphophonemic pass. Every affix application cites its sūtra, extending the
proof-carrying derivation chain.
