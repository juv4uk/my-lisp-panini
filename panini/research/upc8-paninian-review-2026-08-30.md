# UPC-8 paninian/linguistic review — verdict on canonical claims (2026-08-30)

Status: PANINIAN REVIEW v0.1, 2026-08-30. Second-pass follow-up to
`research/upc8-crosscheck.md` (2026-08-18) and
`specs/upc8-long-vowel-bridge.md` (2026-08-25). This pass re-verifies
the review previously done by `shiva-sutras-1` (Claude Code) in
`shiva-sutras/docs/claude-review-upc8-manus-proposals-2026-08-18.md`
against the *live* `shiva-sutras/prototype/upc8.py` — from the panini
side, i.e. against our own SLP1 registry and the traditional
pratyāhāra/Śiva-sūtra definitions this repo is authoritative for.

Scope: the four linguistic/paninian claims that matter for whether
UPC-8's Sanskrit layer is trustworthy:
1. the base 42-sound canon is a true bijection onto the Śiva-sūtras;
2. the pratyāhāra engine respects the it-marker rule (the P0 bug claim);
3. SLP1 long-vowel encoding gap (7/20 dhatu roots);
4. remaining unresolved edges in the Sanskrit extended layer.

Method: read `shiva-sutras/prototype/upc8.py` directly; ran
`test_upc8.py` directly; cross-checked the traditional marker rule
against the canon itself. No changes to any repo — this is a read-only
review verdict.

===============================================================================

## 1. Base 42-sound canon — CONFIRMED (bijective with Śiva-sūtra sequence)

- `_assign_codes()` asserts exactly **42 unique codes**; `CANON_POSITIONS`
  is **43 positions** because `h` appears twice (sūtra 5 and sūtra 14)
  and aliases to one code (`0x09`, sūtra 5 wins).
- The 43-position → 42-code bijection is exactly what the traditional
  canon requires: 42 distinct sounds, with `h`'s repetition in sūtra 14
  being the one genuine duplicate (it is the same phoneme, not a
  different one — correct to alias).
- This matches our own `registry/dhatu/*.yaml` SLP1 alphabet as already
  confirmed in `upc8-crosscheck.md` Result 1, and it matches the
  `ś=S`, `ṣ=z` convention established across three independent codebases
  (Vidyut, my-lisp, shiva-sutras).

Verdict: **CONFIRMED**. No linguistic defect in the base allocation.

## 2. it-marker / pratyāhāra rule (the P0 bug) — CONFIRMED FIXED, verified live

`claude-review...md` had already `PROVED` (via its own source reading +
Manus AI + Sarvam cold witness) that `pratyahara()` dropped a listed
sound whenever its SLP1 letter equalled a query's marker letter, instead
of excluding only the marker occurrence. The fix landed in commit
`55d60a6`.

This pass re-ran the live suite:

```
[PASS] Pratyahara 'hal' -> 33 consonants (h deduplicated, l included)
[PASS] All 6 marker/sound spelling-collision families resolved correctly (l/y/r/m/Y/v)
[PASS] Pratyahara 'ac' -> 9 vowels
[PASS] Pratyahara 'ik' -> 4
[PASS] Pratyahara 'Sar' -> 3
[PASS] Pratyahara 'yaR' -> 4
Results: 28 passed, 0 failed, 28 total
```

The characteristic bug symptom is gone: `hal` now resolves to **33** (was
buggy 32), i.e. the real `l` of sūtra 6 is correctly retained while the
marker-`l` of sūtra 14 is excluded. All 6 collision families
(`l/y/r/m/Y/v`) have a regression test that passes.

This matches the traditional rule precisely: exclude **only the marker
occurrence** of the anubandha letter, keep the phoneme-`l` that closes
the pratyāhāra as a full member (`hal` includes `l`). The engine now
behaves per grammar, not per spelling accident.

Verdict: **CONFIRMED FIXED**. No remaining pratyāhāra marker-collision
defect. This also validates the sole engine claim `claude-review` flagged
as the one that actually mattered.

## 3. SLP1 long-vowel gap (7/20 dhatu roots) — CLOSED by existing bridge spec

`upc8-crosscheck.md` (2026-08-18) found 7/20 roots
(`BAz, BI, BU, dA, jYA, nI, sTA`) do not encode directly via
`encode_sanskrit()` with our own SLP1 spelling because long vowels live
in the extended table (`0x2A`-`0x2E`), not the base 42.

`specs/upc8-long-vowel-bridge.md` (2026-08-25) already closed this as a
spec (no code): a decomposition rule `(base, is_long)` over the five
SLP1 long-vowel letters, bridged to `encode_sanskrit_iast_token()` with
real IAST `ā/ī/ū/ṝ/ḹ`. Its worked examples were verified against live
`upc8.py` commit `ff37b4d` (all 7 encode without `KeyError`).

This pass confirms the classification is linguistically sound: SLP1's
uppercase-on-vowel = length and its uppercase-on-consonant = a different
phoneme are two unrelated facts about the same alphabet, and the bridge
rule correctly treats them as orthogonal (never conflating eg `A`=long
a with `B`=bh). The 7 roots are all short-`a/i/u` length cases; the rule
also names `F`/`X` (long vocalic r/l) for a future 8th root.

Verdict: **CLOSED (by existing spec, verified)**. No new gap.

## 4. Remaining unresolved edges — UNRESOLVED (documented, low severity)

Two entries in `SANSKRIT_EXTENDED` carry `"unresolved"` IPA/aliasing and
`"not in canon"` provenance: `0x2F` (PH-SKT-M, anusvāra `~`) and `0x30`
(PH-SKT-H, visarga `H`). Both are real Sanskrit phonemes but are **not**
Śiva-sūtra members, so their placement in the extended layer is an
engineering decision, not a canon claim. Their `"unresolved"` tag is
honest and correct as-is.

Note also that `SLP1_TO_IAST`'s `f→ṛ`, `x→ḷ` mapping is conventional
(short vocalic r/l), consistent with our own established SLP1 convention.

Verdict: **UNRESOLVED, correctly labeled, not a canon defect** — flagged
for completeness only.

===============================================================================

## Summary

| Claim | Verdict | Evidence |
|---|---|---|
| Base 42-sound canon bijective over Śiva-sūtras | CONFIRMED | `_assign_codes()` assert, 43→42, h alias |
| it-marker rule in pratyāhāra (P0) | CONFIRMED FIXED (live 28/28, hal→33) | `test_upc8.py`, run directly |
| SLP1 long-vowel gap, 7/20 roots | CLOSED by `upc8-long-vowel-bridge.md`, verified | bridge spec worked examples |
| anusvāra/visarga extended entries | UNRESOLVED, correctly tagged | `SANSKRIT_EXTENDED` |
| `ś=S`, `ṣ=z` convention | CONFIRMED (3rd+ independent) | crosscheck Result 1 |

PANINIAN_REVIEW_CALLS = 0 Sarvam — none needed; every claim here is
checked by direct source reading against the Śiva-sūtra canon and our own
SLP1 registry, not by LLM translation.

## What this doc does NOT claim

- No change to `upc8.py` (shiva-sutras authority) or to our own
  `registry/dhatu/*.yaml` — read-only verdict.
- No verdict on UPC-8's Ukrainian/English layers, FPGA economics, or the
  P1/P2 architectural proposals (versioned profiles, hardware headers) —
  those remain uncommitted/drafts per `claude-review` §4/§5, out of scope
  for paninian review.

## Sources

- `shiva-sutras/prototype/upc8.py` and `prototype/test_upc8.py` — read
  and run directly (28/28), 2026-08-30; fix commit `55d60a6`.
- `shiva-sutras/docs/claude-review-upc8-manus-proposals-2026-08-18.md` —
  the prior review this pass confirms.
- `panini/research/upc8-crosscheck.md` (2026-08-18) and
  `panini/specs/upc8-long-vowel-bridge.md` (2026-08-25) — our own
  sibling findings, this doc's baseline.
- `panini/registry/dhatu/*.yaml` — the 20 canonical SLP1 spellings.
