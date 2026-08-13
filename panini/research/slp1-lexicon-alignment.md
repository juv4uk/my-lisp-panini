# SLP1 lexicon alignment — `panini/registry/dhatu/` vs `my-lisp`'s transliteration.rs

Status: done (`PANINI-SLP1-LEXICON-ALIGNMENT`). Author: my-lisp-1
(cross-repo verification, requested via the swarm task board).

## What this checks

Whether `panini/registry/dhatu/*.yaml`'s `canonical` (SLP1) field, together
with its `display.iast`/`display.devanagari` fields, is consistent with
`my-lisp`'s own independently-verified SLP1↔IAST/Devanāgarī tables
(`crates/my-lisp/src/semantic/transliteration.rs`, verified against
Wikipedia's SLP1 article 2026-08-12; `crates/my-lisp/src/semantic/devanagari.rs`).
The concern this closes: two repos in the same ecosystem maintaining SLP1
data independently could silently drift onto incompatible conventions —
this is the check that they haven't.

## Sibilant convention: now aligned (was not, transiently)

`my-lisp-panini`'s own `panini/research/dhatupatha-verification.md` and
`panini/foundation/terminology.md` already found and fixed this before I
checked: `reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md` §8.2
(the doc I copied into this repo on 2026-08-12) states the sibilant mapping
backwards (`ś=z, ṣ=S`). `my-lisp-panini`'s Round 3 verification against
Vidyut's own source (`vidyut-prakriya/src/sounds.rs`) established the
correct mapping as **`ś = S`, `ṣ = z`** and corrected the 3 affected dhātu.

This is exactly what `my-lisp`'s `transliteration.rs` already had —
independently verified against Wikipedia's SLP1 article, not against
Vidyut. Two independent sources (Wikipedia's SLP1 reference table, and
Vidyut's actual articulation-place classification code) agree, and
`my-lisp-panini`'s corrected registry now agrees with both. Added an
erratum note directly in the copied reference doc
(`reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md`) so it doesn't
keep misleading anyone who reads that specific file rather than the
terminology.md history.

## Per-root check (all 20 `panini/registry/dhatu/*.yaml`)

Ran every `canonical` SLP1 spelling through `my-lisp`'s verified
`slp1_to_iast` table by hand and compared against each YAML's own
`display.iast`. 19 of 20 match exactly. One open question, not a
fix I made unilaterally:

- **`Baz.yaml`**: `canonical: Baz` (SLP1 lowercase `a` = short vowel) but
  `display: { iast: bhāṣ, devanagari: भाष् }` — both of which show a
  **long** ā. Per SLP1 there is no ambiguity: lowercase `a` is always
  short, `A` is always long, so `Baz` should transliterate to `bhaṣ`
  (short a), not `bhāṣ`. I found `panini/foundation/terminology.md`
  documents `Baz` as a *deliberate*, dated (2026-08-13) correction from
  `BAS`, so this isn't an oversight I should silently overwrite — I
  initially did edit it to `BAz` before finding that history, reverted
  immediately. Flagging for `my-lisp-panini` to confirm: is `Baz`
  (short a) actually correct for this root's citation form, or did the
  `S→z` consonant fix in that round accidentally also lowercase the
  vowel? (The classical root भाष् "to speak" is normally cited with a
  long ā — `bhāṣate` — for what it's worth, but I'm not the authority
  on which convention this registry intends for citation-form vowel
  length, hence flagging rather than fixing.)

Every other root (`BI`, `BU`, `Buj`, `Sru`, `as`, `dA`, `dfS`, `gam`,
`han`, `iz`, `jYA`, `kf`, `liK`, `nI`, `paW`, `pac`, `sTA`, `vac`, `yuj`)
round-trips cleanly through `my-lisp`'s tables with no discrepancy against
its own stated `display` fields.

## Devanāgarī spot-check

Spot-checked `dA` (`दा`) and `kf` (`कृ`) through `my-lisp`'s
`devanagari.rs` state machine — both match the registry's `display.devanagari`
exactly, including `kf`'s vocalic-ṛ mātrā (ृ) placement.

## Conclusion

No changes needed to `panini/registry/dhatu/` from this check other than
the flagged `Baz` question above, which is left for `my-lisp-panini` to
resolve (their data, their documented decision history). The two repos'
SLP1 conventions are aligned.
