#!/usr/bin/env python3
"""Attack on the seven non-ASCII punctuation cells of UPC-7 v3 (« » — – “ ” …, shiva-sutras PR #105).
Checks: each glyph encodes to its table cell in all 4 layouts and round-trips (alone, between letters, inside quotes, next to digits/capital/apostrophe);
no collision with any other cell (h r l, digits, capital/stress, signs); cells are reserved (not assigned) in the PINNED table; look-alikes and
unplaced characters are refused, not merged; NFC/NFKC behaviour; real-prose round trip. Usage: python3 review_upc7_punct7_attack.py --proto <prototype> [--prose FILE ...]
"""
import csv, re, sys, unicodedata
from pathlib import Path

def arg(n, d=None): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
proto = Path(arg('--proto')); sys.path.insert(0, str(proto))
import upc7_lang as L
T = L.LangText()
rows = list(csv.DictReader(open(proto / 'upc7-table-v3.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
pinned = {int(r['bits'], 2): r for r in csv.DictReader(open(proto / 'upc7-table.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)}
defects = []
def report(name, ok, detail=''):
    print(('PASS   ' if ok else 'DEFECT ') + name + (' | ' + detail if detail else ''))
    if not ok: defects.append(name)
def enc(t, lay):
    try: return ('ok', T.encode(t, lay))
    except L.LangError as e: return ('refused', str(e)[:70])
LAYS = ('uk', 'sa-iast', 'sa-deva', 'sa-cyr')
P = dict(L.PUNCT_CELL); print('placed:', {g: (c, hex(c)) for g, c in P.items()})

# table: v3 rows, uniqueness, pinned-safety
cells = [int(r['bits'], 2) for r in rows]
report(f'v3 table: {len(rows)} rows, every cell used once', len(set(cells)) == len(cells))
col = {r['sound']: r for r in rows}
tab = {g: [r for r in rows if r['uk'] == g or r['sa-iast'] == g] for g in P}
report('each glyph has a v3 table row at the cell upc7_lang uses', all(len(tab[g]) == 1 and int(tab[g][0]['bits'], 2) == P[g] for g in P), str({g: [r['sound'] for r in tab[g]] for g in P}))
report('each of the 7 cells is RESERVED (not assigned) in the PINNED table (no migration)', all(pinned[c]['status'] == 'reserved' for c in P.values()), str({g: pinned[c]['status'] for g, c in P.items()}))
other = {int(r['bits'], 2): r['sound'] for r in rows if r['uk'] not in P and r['sa-iast'] not in P}
report('no collision with any other v3 cell (h r l, digits, capital/stress, signs, letters)', not (set(P.values()) & set(other)), str([(g, other[c]) for g, c in P.items() if c in other]))
for name in ('h', 'r', 'l', 'capital'):
    print(f'       info  {name}: cell {int(col[name]["bits"], 2)} ({hex(int(col[name]["bits"], 2))}); punctuation cells {sorted(P.values())}')
digit = {int(r['bits'], 2) for r in rows if r['sound'].startswith('digit')}
report('no punctuation cell is a digit cell', not (digit & set(P.values())))
sub = {c for c in range(128) if True}
d0 = L.DIGIT_CELL['0']; gens = [L.DIGIT_CELL[str(1 << i)] ^ d0 for i in range(4)]
span = {d0 ^ (gens[0] if m & 1 else 0) ^ (gens[1] if m & 2 else 0) ^ (gens[2] if m & 4 else 0) ^ (gens[3] if m & 8 else 0) for m in range(16)}
print('       info  punctuation cells that lie in the 16-cell affine subspace of the digits (digit values 10..15):', {g: hex(c) for g, c in P.items() if c in span})
print('       info  class prefixes (top 2 bits) of the 7 cells:', {g: format(c, '07b')[:2] for g, c in P.items()}, '(shiva: class-prefix reading does not hold for these)')

# encode / round trip
bad = []
for g, c in P.items():
    for lay in LAYS:
        r = enc(g, lay)
        if r != ('ok', (c,)): bad.append((g, lay, r)); continue
        if T.render((c,), lay) != g: bad.append((g, lay, 'render'))
report('each glyph: encode == (cell,) and render == glyph in all 4 layouts', not bad, str(bad[:4]))
letters = {'uk': ('к', 'т'), 'sa-iast': ('k', 't'), 'sa-deva': ('क', 'त'), 'sa-cyr': ('к', 'т')}
bad = []
for g, c in P.items():
    for lay, (a, b) in letters.items():
        dg = '७' if lay == 'sa-deva' else '7'
        for t in (a + g + b, g + a, a + g, g + g, dg + g + dg, ' ' + g + ' ', g * 3):
            r = enc(t, lay)
            if r[0] != 'ok': bad.append((lay, t, r[1])); continue
            try:
                out = T.render(r[1], lay)
                if enc(out, lay) != r: bad.append((lay, t, 'round trip ' + out))
            except L.LangError as e: bad.append((lay, t, 'render ' + str(e)[:40]))
report('glyph between/next to letters, digits, spaces, repeated: encode + render + re-encode identical (4 layouts x 7 glyphs x 7 contexts)', not bad, f'{len(bad)} failures {bad[:4]}')
# uk specifics: capital after « , apostrophe inside quotes, ellipsis after a word
cases = ['«Привіт»', '«п\'ять» — це «п’ять»', 'Київ…', '“Кіт”', '–кіт–', '«Ґанок»', '«м\'ясо»…', 'Він сказав: «Так».', '«»', '——', '…']
bad = []
for t in cases:
    r = enc(t, 'uk')
    if r[0] != 'ok': bad.append((t, r[1])); continue
    out = T.render(r[1], 'uk')
    if enc(out, 'uk') != r: bad.append((t, 'round trip', out))
    elif out.lower() != unicodedata.normalize('NFC', t).lower().replace('’', "'") and out != t: print(f'       info  uk text normalised on render: {t!r} -> {out!r}')
report('uk sample sentences with « » — – “ ” … round-trip (capitals, apostrophes inside quotes)', not bad, str(bad[:4]))

# refusals: look-alikes and unplaced characters
unplaced = ['‘', '’', '„', '‚', '‹', '›', '§', '№', '$', '%', '[', ']', '^', '{', '}', '~', '‐', '‑', '‒', '―', '−', '⁄', '″', '′', '‟', '〝', '〞', '‥', '⋯', '・', '•', '¬', '«»'.replace('«', '').replace('»', '')]
unplaced = [u for u in unplaced if u]
acc = {}
for u in unplaced:
    for lay in LAYS:
        r = enc('к' + u + 'т' if lay in ('uk', 'sa-cyr') else ('k' if lay == 'sa-iast' else 'क') + u + ('t' if lay == 'sa-iast' else 'त'), lay)
        if r[0] == 'ok': acc.setdefault(u, []).append((lay, r[1]))
print('       info  characters that were ACCEPTED between letters although not placed:', {u: v[:1] for u, v in acc.items()})
expected_refuse = [u for u in unplaced if u not in ("’",)]       # ’ is the apostrophe in uk and the avagraha in Sanskrit by policy
real = {u: v for u, v in acc.items() if u in expected_refuse}
report('look-alikes (‘ „ ‚ ‹ › ‐ ‑ ‒ ― − ⁄ ′ ″ ‟ ‥ ⋯ •) and the unplaced § № $ % [ ] ^ { } ~ are REFUSED, not merged', not real, str({u: v[:1] for u, v in real.items()}))
for u, w in (("’", 'к’т'),):
    print(f'       info  ’ between letters: uk {enc(w, "uk")}, sa-iast {enc("k’t", "sa-iast")}')
merge = []
for a, b in (('...', '…'), ('--', '—'), ('-', '–'), ('<<', '«'), ('>>', '»'), ('"', '“'), ('"', '”'), ('---', '—')):
    ra, rb = enc('к' + a + 'т', 'uk'), enc('к' + b + 'т', 'uk')
    if ra == rb: merge.append((a, b))
    print(f'       info  uk {a!r} -> {ra[1] if ra[0]=="ok" else ra}  vs  {b!r} -> {rb[1] if rb[0]=="ok" else rb}')
report('ASCII stand-ins (... -- --- << >> ") are NOT silently the placed glyphs (different cells)', not merge, str(merge))
nfkc_ok = [g for g in P if unicodedata.normalize('NFKC', g) != g]
print('       info  glyphs that NFKC would change (a pipeline using NFKC would merge them):', [(g, unicodedata.normalize('NFKC', g)) for g in nfkc_ok])
report('NFC input of every glyph is unchanged (no decomposition hazard)', all(unicodedata.normalize('NFC', g) == g and unicodedata.normalize('NFD', g) == g for g in P))

# the middle dot is NOT a placed glyph: in the Sanskrit decoders it is the designed boundary separator (upc14v2_script.SEPARATOR, ISO 15919), no cell
r1, r2 = enc('k·t', 'sa-iast'), enc('kt', 'sa-iast')
print(f'       info  sa-iast k·t == kt (the separator leaves no cell; k·h vs kh differ only in the sound sequence): {r1 == r2}; uk: {enc("к·т", "uk")[0]}')
# real prose
files = [Path(p) for p in sys.argv[sys.argv.index('--prose') + 1:] if not p.startswith('--')] if '--prose' in sys.argv else []
if files:
    tot = ok = fals = 0; samples = []
    for f in files:
        for line in f.read_text(encoding='utf-8', errors='replace').split('\n'):
            for seg in re.split(r'(?<=[.!?])\s+', line):
                seg = seg.strip()
                if not any(g in seg for g in P) or len(seg) > 200: continue
                tot += 1; r = enc(seg, 'uk')
                if r[0] != 'ok': continue
                ok += 1
                try:
                    out = T.render(r[1], 'uk')
                    if enc(out, 'uk') != r: fals += 1; samples.append(seg[:60])
                except L.LangError: fals += 1; samples.append(seg[:60])
    print(f'       info  prose segments containing a placed glyph: {tot}; fully encodable in uk: {ok}; false refusals/round-trip failures among them: {fals} {samples[:3]}')
print(f'\n{len(defects)} defects: {defects}')
