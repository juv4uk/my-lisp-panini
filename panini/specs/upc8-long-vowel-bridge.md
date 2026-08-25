# UPC-8 long-vowel bridge (spec only, no code)

**Status:** SPEC v0.1, 2026-08-25. Answers the gap `research/upc8-crosscheck.md`
(2026-08-18) found and deliberately left open: 7 of our 20 canonical
`registry/dhatu/*.yaml` spellings contain a long vowel and none encode
directly via `shiva-sutras/prototype/upc8.py`'s `encode_sanskrit()`.

**Scope, explicit:** this document specifies a decomposition rule and
applies it by hand to the 7 affected roots as worked examples. It does
**not** modify `upc8.py` (a different repo — shiva-sutras owns that
authority) and does **not** modify `registry/dhatu/*.yaml` (our own
canonical spellings are correct as written; the gap is in how a
consumer would *bridge* them to UPC-8, not an error in the spellings
themselves). No code in this repo changes as a result of this spec.

## Why a symbol-by-symbol string mapping can't work

`upc8.py`'s own canonical 42-sound table (`CODE_OF_SOUND`) indexes
short vowels (`a`, `i`, `u`, `f`, `x`, `e`, `o`) and consonants directly
by their SLP1 letter. Long vowels are not in that table at all — they
live in a separate `SANSKRIT_EXTENDED` table (codes `0x2A`-`0x2E`),
addressed by an ASCII placeholder spelling (`"a:"`, `"i:"`, `"u:"`,
`"R:"`, `"L:"`) that has no relationship to the SLP1 letter our own
registry uses (`A`, `I`, `U`, `F`, `X`) for the same sound. Since
2026-08-25, `upc8.py` also exposes `encode_sanskrit_iast_token()`,
which accepts genuine Unicode IAST (`'ā'`, `'ī'`, `'ū'`, `'ṝ'`, `'ḹ'`)
for exactly these five extended codes — that is the bridge target this
spec uses, not the older ASCII placeholder path (kept in `upc8.py`
only for its own pre-existing callers).

Standard SLP1 (the Huet convention our own `AGENTS.md`/`terminology.md`
already commit to) marks vowel length by case: lowercase = short,
uppercase = long, for exactly five letter pairs. Uppercase on a
*consonant* letter means something else entirely (a different phoneme
— `B`=bh vs `b`=b, not "long b"). A decomposition rule must therefore
treat vowel-length case-marking and consonant-identity case-marking as
two unrelated facts about the same alphabet, never conflate them.

## The decomposition rule

Given any canonical SLP1 string (one of our `registry/dhatu/*.yaml`
`canonical` fields, or any other SLP1 string built from the same
alphabet), scan it left to right, one SLP1 token at a time (every
token in this alphabet is exactly one character — no digraphs, by
design, same as `upc8.py`'s own canonical layer). For each token:

1. **If the token is one of `A`, `I`, `U`, `F`, `X`** (the five
   long-vowel letters): it decomposes to `(base, is_long=True)`, where
   `base` is the lowercase short-vowel counterpart (`A`→`a`, `I`→`i`,
   `U`→`u`, `F`→`f`, `X`→`x`).
2. **Otherwise**, the token decomposes to `(token, is_long=False)`
   unchanged — this covers every short vowel and every consonant,
   long or not being irrelevant to a consonant's identity.

```text
LONG_VOWEL_BASE = { "A": "a", "I": "i", "U": "u", "F": "f", "X": "x" }

def decompose(slp1_string):
    return [
        (LONG_VOWEL_BASE[ch], True) if ch in LONG_VOWEL_BASE else (ch, False)
        for ch in slp1_string
    ]
```

(Pseudocode for the spec's own clarity — not a claim that this repo
runs Python or that this is real code to add anywhere.)

## Encoding a decomposed token (for a future consumer)

Once decomposed, each `(base, is_long)` pair maps onto `upc8.py`'s
real API (as of the `encode_sanskrit_slp1_token`/
`encode_sanskrit_iast_token` split, 2026-08-25):

- `is_long=False` → `encode_sanskrit_slp1_token(base)` — `base` is
  already a valid canonical SLP1 token (short vowel or consonant),
  encodes directly, no translation needed.
- `is_long=True` → look up `base` in a second small table mapping the
  five short bases to their real IAST long-vowel spelling
  (`{"a":"ā", "i":"ī", "u":"ū", "f":"ṝ", "x":"ḹ"}`), then call
  `encode_sanskrit_iast_token()` on *that* — this is the piece that
  did not exist before 2026-08-25 (before that, only the ASCII
  placeholder `"a:"`-style spelling could reach these five codes at
  all, and it doesn't derive from our own SLP1 letters).

## Worked examples: all 7 affected roots

| Root | IAST | Decomposition | Encoding calls (in order) |
|---|---|---|---|
| `BAz` | bhāṣ | B, (a,long), z | `encode_sanskrit_slp1_token('B')`, `encode_sanskrit_iast_token('ā')`, `encode_sanskrit_slp1_token('z')` |
| `BI` | bhī | B, (i,long) | `encode_sanskrit_slp1_token('B')`, `encode_sanskrit_iast_token('ī')` |
| `BU` | bhū | B, (u,long) | `encode_sanskrit_slp1_token('B')`, `encode_sanskrit_iast_token('ū')` |
| `dA` | dā | d, (a,long) | `encode_sanskrit_slp1_token('d')`, `encode_sanskrit_iast_token('ā')` |
| `jYA` | jñā | j, Y, (a,long) | `encode_sanskrit_slp1_token('j')`, `encode_sanskrit_slp1_token('Y')`, `encode_sanskrit_iast_token('ā')` |
| `nI` | nī | n, (i,long) | `encode_sanskrit_slp1_token('n')`, `encode_sanskrit_iast_token('ī')` |
| `sTA` | sthā | s, T, (a,long) | `encode_sanskrit_slp1_token('s')`, `encode_sanskrit_slp1_token('T')`, `encode_sanskrit_iast_token('ā')` |

None of the 7 roots involve `F`/`X` (long vocalic r/l) — the rule
still names them (row above) for completeness, since a future 8th root
could.

## Verification of the worked examples

Every `encode_sanskrit_slp1_token`/`encode_sanskrit_iast_token` call
above was checked against the live `shiva-sutras/prototype/upc8.py`
(commit `ff37b4d`, the commit that introduced these two functions) —
none raise `KeyError`, confirming the rule actually bridges all 7
roots, not just on paper:

```text
BAz -> B=0x14(bh) ā=0x2A z=0x28(ṣ)
BI  -> B=0x14(bh) ī=0x2B
BU  -> B=0x14(bh) ū=0x2C
dA  -> d=0x1c ā=0x2A
jYA -> j=0x18 Y=0x0e(ñ) ā=0x2A
nI  -> n=0x12 ī=0x2B
sTA -> s=0x29 T=0x21(th) ā=0x2A
```

(Every value above is the actual output of running `encode_sanskrit_slp1_token`/
`encode_sanskrit_iast_token` against the live `upc8.py`, not hand-computed —
an earlier hand-computed draft of this table had three wrong hex values,
caught only by actually running the code before publishing this spec.)

## What this spec does not claim

- Not a claim that `s`/`z`/`S` etc. codes above are re-derived here —
  they are exactly `upc8.py`'s own existing canonical codes, unchanged,
  already confirmed correct by `upc8-crosscheck.md`'s Result 1.
- Not an integration — no code in either repo calls this rule. If a
  real consumer is ever built, it belongs to whichever repo owns that
  integration surface, following `upc8-crosscheck.md`'s own boundary
  note: this repo does not implement UPC-8.
- Not a claim that every possible SLP1 string in existence is covered
  — only the alphabet actually used in `registry/dhatu/*.yaml`
  (short/long vowel pairs + the 37 consonant letters already confirmed
  by the crosscheck). A string using a symbol outside that alphabet is
  out of this spec's scope.

## Sources

- `research/upc8-crosscheck.md` (2026-08-18) — the gap this spec closes.
- `github.com/juv4uk/shiva-sutras`, `prototype/upc8.py` commit `ff37b4d`
  (`encode_sanskrit_slp1_token`/`encode_sanskrit_iast_token` added) and
  `dae641c` (ś/ṣ swap fix in a different prototype file, unrelated to
  this bridge but same repo/session) — read directly, functions called
  directly to verify the worked examples, not assumed from a description.
- `registry/dhatu/{BAz,BI,BU,dA,jYA,nI,sTA}.yaml` — canonical spellings,
  read directly for this spec, matching `upc8-crosscheck.md`'s citation.
