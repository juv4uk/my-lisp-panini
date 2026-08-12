# Kāraka Reference
## The six semantic roles of the Sanskrit sentence, for the semantic resolver

Author: engineer-1
Date: 2026-08-12
Audience: my-lisp-1 (SANSKRIT-P4 semantic AST, SANSKRIT-P5 semantic IDs),
cml (IR/backend), swarm at large.
Status: reference document — the sūtra numbers below were re-verified on
2026-08-12 against the Aṣṭādhyāyī (P.1.4.24, P.1.4.32, P.1.4.42, P.1.4.45,
P.1.4.49, P.1.4.54) per the SANSKRIT-P2 ethos ("verify against an
authoritative source, not memory"). Example translations are working glosses
for the migration, not the full Pāṇinian canon.

---

## 1. What a *kāraka* is

A *kāraka* is a **semantic role** that a participant plays *with respect to
the action of the verb*. The *vibhakti* (surface case ending) is *derived
from* the kāraka, never the other way around:

```
kāraka (semantic role)  →  vibhakti (surface case ending)
        ↑                                    ↑
   semantic AST (P5)              morphological string (P1)
```

This is exactly why SANSKRIT-P5 requires the AST to carry semantic IDs, not
raw strings: the same kāraka surfaces in different cases under passivization,
nominalization, and different declensions, while the *role* stays constant.

The fixed kāraka IDs used by the migration (matching the migrators' own
example `(dA :kartf server :karman packet :sampradAna client)`):

| SLP1 atom  | IAST     | Deva       | English gloss |
|------------|----------|------------|---------------|
| kartf      | kartṛ    | कर्तृ      | agent         |
| karman     | karman   | कर्मन्     | object        |
| karaRa     | karaṇa   | करण        | instrument    |
| sampradAna | sampradāna | सम्प्रदान | recipient     |
| apAdAna    | apādāna  | अपादान    | source        |
| aDikaraRa  | adhikaraṇa | अधिकरण  | locus         |

## 2. The six kārakas and their defining sūtras

Pāṇini defines the roles in a deliberate order — the *most restricted* first,
the *independent* kartṛ last as the default (P.1.4.54 *svatantraḥ kartā*).
A role-assignment algorithm should apply the same specificity ordering.

| # | Kāraka (SLP1 / IAST) | Defining sūtra (gloss) | Default vibhakti | Example (SLP1 · Deva · IAST) |
|---|----------------------|------------------------|------------------|------------------------------|
| 1 | apAdAna / apādāna    | P.1.4.24 *dhruvam apāye 'pādānam* — the fixed point from which departure takes place | pañcamī (abl.) | vfkzAt parRam patati · वृक्षात् पर्णम् पतति · vṛkṣāt parṇam patati "the leaf falls *from the tree*" |
| 2 | sampradAna / sampradāna | P.1.4.32 *karmaṇā yam abhipraiti sa sampradānam* — the one the agent intends to be reached by the object | caturthī (dat.) | guruH SizyAya pustakaM dadAti · गुरुः शिष्याय पुस्तकम् ददाति · guruḥ śiṣyāya pustakam dadāti "the teacher gives a book *to the student*" |
| 3 | karaRa / karaṇa      | P.1.4.42 *sādhakatamaṁ karaṇam* — the most effective means | tṛtīyā (instr.) | rAmaH kuWAreRa vfkzaM Cinatti · रामः कुठारेण वृक्षम् छिनत्ति · rāmaḥ kuṭhāreṇa vṛkṣam chinatti "Rāma cuts the tree *with an axe*" |
| 4 | aDikaraRa / adhikaraṇa | P.1.4.45 *ādhāro 'dhikaraṇam* — the locus, the substratum where the action takes place | saptamī (loc.) | pakzI SAKAyAm Aste · पक्षी शाखायाम् आस्ते · pakṣī śākhāyām āste "the bird sits *on the branch*" |
| 5 | karman / karman      | P.1.4.49 *kartur īpsitatamaṁ karma* — what the agent most wishes to attain | dvitīyā (acc.) | bAlaH pustakaM pawati · बालः पुस्तकम् पठति · bālaḥ pustakam paṭhati "the boy reads *the book*" |
| 6 | kartf / kartṛ        | P.1.4.54 *svatantraḥ kartā* — the independent agent (the default role) | prathamā (nom.) | rAmaH vadati · रामः वदति · rāmaḥ vadati "Rāma speaks" |

Devanagari conjuncts in the table (पर्णम्, शिष्याय, कुठारेण, वृक्षम्,
शाखायाम्, पुस्तकम्, पठति) are *pada-level* forms; the SLP1 column is the
canonical representation the transliteration layer must round-trip
(P1 canonical = SLP1).

## 3. kāraka → vibhakti (surface case endings)

For a masculine `-a` stem (paradigm: `rAma` / राम / rāma):

| Vibhakti | Sanskrit | SLP1 ending | Full SLP1 | Deva | IAST |
|----------|----------|-------------|-----------|------|------|
| prathamā (nom.) | प्रथमा | -aH | rAmaH | रामः | rāmaḥ |
| dvitīyā (acc.)  | द्वितीया | -am | rAmaM | रामम् | rāmam |
| tṛtīyā (instr.) | तृतीया | -ena | rAmeRa | रामेण | rāmeṇa |
| caturthī (dat.) | चतुर्थी | -Aya | rAmAya | रामाय | rāmāya |
| pañcamī (abl.)  | पञ्चमी | -At | rAmAt | रामात् | rāmāt |
| ṣaṣṭhī (gen.)   | षष्ठी | -asya | rAmasya | रामस्य | rāmasya |
| saptamī (loc.)  | सप्तमी | -e | rAme | रामे | rāme |

## 4. Override rules (where the default mapping is not used)

The kāraka→vibhakti mapping above is *regular but not 1:1*. The resolver must
know the overrides, because they are exactly the cases where the surface case
alone would mislead a naive parser:

1. **Passive (karmaṇi prayoga)**: the karman of the active sentence becomes
   the *nominative* subject; the kartṛ surfaces in the *instrumental*.
   `bAlena pustakaM pawyate` · बालेन पुस्तकम् पठ्यते · bālena pustakam paṭhyate
   "the book is read by the boy" — `bAlena` is an instrumental *kartṛ*, not a
   karaṇa.
2. **Genitive is never a kāraka** (the ṣaṣṭhī is a relation of possession,
   outside the kāraka system). A genitive nominal should be lowered to a
   possessive/attributive node, never to a kāraka slot.
3. **Double accusatives** occur with causatives and verbs of double-object
   type; only the *īpsitatama* (most desired) object is the primary karman,
   the secondary object is *karuṇa-virodhin* etc. For the migration, treat the
   primary karman per P.1.4.49 and attach the secondary one as a `:karman2`
   slot (to be confirmed against a corpus before use).
4. **kartṛ in the instrumental** is legal only in passives (rule 1) and with
   gerundives (see §5); it is never karaṇa.

## 5. Passive and *kṛt* (nominal) constructions

| Construction | Surface pattern | Role assignment |
|--------------|-----------------|-----------------|
| Active (kartari prayoga) | kartṛ = nom., karman = acc. | straightforward per §2 |
| Passive (karmaṇi prayoga) | karman = nom., kartṛ = instr. | swap roles, verb agrees with karman |
| *ktvā* absolutive ("having done") | kartṛ shared with main clause | karman (if any) stays in acc. |
| *tum* infinitive ("to do") | kartṛ in instr. or gen. (with *alam*) | keep kāraka labels, surface differs |
| gerundive *tavya/anīya* ("to be done") | karman = nom., kartṛ = instr./gen. | same swap as passive |

Net effect for the resolver: the **semantic labels never change** when the
voice changes — only the vibhakti and the agreement target do. This is the
property the SANSKRIT-P5 semantic IDs preserve.

## 6. Decision procedure for the semantic resolver

Pseudo-procedure (per finite verb + its nominal participants):

```
1. Locate the finite verb; resolve its dhātu sense to a semantic ID (P2/P3).
   The verb's frame declares its valence slots (e.g. dA = kartf, karman,
   sampradAna).
2. Collect the sentence's nominal participants (dependents of the verb).
3. For each participant, test the candidate roles in Pāṇini's order:
     apAdAna → sampradAna → karaRa → aDikaraRa → karman → kartf
   (most restricted first, kartf last as the default).
   A participant matches a role when it satisfies that role's sūtra
   definition against the verb's semantics, not just its surface case.
4. Surface-case clue is only a *filter* (use the inverse of §3/§4), never a
   proof: an instrumental can be karaRa, a passive kartf, or a kṛt-agent.
5. If a participant satisfies nothing else, assign kartf (P.1.4.54 default).
6. Assign exactly one kāraka per participant. A genitive nominal is not a
   kāraka (rule 2): emit a possessive node instead.
7. Emit the semantic AST node (P4/P5):
   (VERB <dhātu-id> (:kartf ...) (:karman ...) (:sampradAna ...) ...)
   — labels are the SLP1 atoms of §1, never the raw surface strings.
```

Precedence note: the sūtra order is a *search* order, not a priority for
conflict resolution — Pāṇini's roles are defined so that at most one
applies; when a participant matches several definitions, the most specific
one (earliest in the sūtra order) wins, exactly as in P.1.4.1-2
(*kārakādhikāra*).

---

### Cross-references

- PANINI-GRAMMAR-REFERENCE.md — sound inventory, gaṇa table, upasargas,
  sandhi, vibhakti overview (§3.1), and the kāraka table (§4).
- Used by: SANSKRIT-P1 (transliteration of the role atoms), SANSKRIT-P4
  (semantic AST), SANSKRIT-P5 (semantic IDs), SANSKRIT-P9 (opcode-boundary
  review of the atom representation).
