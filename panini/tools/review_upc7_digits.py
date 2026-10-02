#!/usr/bin/env python3
"""Independent check of the decimal-digit cells in the candidate UPC-7 table v3 (shiva-sutras#93), written from the TSV definition only.
Checks: (1) the 10 digit rows and their cells; no collision between any two rows; (2) spelling: round trip in the 4 layouts with a codec of my own
built from the TSV columns, and the same strings through upc7_lang (the subject), incl. refusal of the other layout's glyphs; (3) the affine law
cell(a)^cell(b)^cell(c)^cell(a^b^c)=0 for all a,b,c in 0..9 with a^b^c<10; (4) digit is not Number: cells are not ordered like values;
(5) placement census: which free cells existed, how many contiguous runs, how many affine embeddings, how many have single-bit generators.
Usage: python3 review_upc7_digits.py --proto /path/to/shiva-sutras/prototype
"""
import csv, itertools, random, sys
from pathlib import Path

proto = Path(sys.argv[sys.argv.index('--proto') + 1])
rows = list(csv.DictReader(open(proto / 'upc7-table-v3.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
pinned = list(csv.DictReader(open(proto / 'upc7-table.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
ok = True
def check(name, cond, detail=''):
    global ok; ok &= bool(cond); print(('OK   ' if cond else 'FAIL ') + name + (' ' + detail if detail else ''))

cell = lambda r: int(r['bits'], 2)
check('v3: every cell is used by at most one row', len({cell(r) for r in rows}) == len(rows), f'{len(rows)} rows')
dig = {int(r['sound'][6:]): cell(r) for r in rows if r['sound'].startswith('digit-')}
check('ten digit rows 0..9', sorted(dig) == list(range(10)), str([dig[d] for d in range(10)]))
others = {cell(r) for r in rows if not r['sound'].startswith('digit-')}
check('digit cells collide with no other v3 row', not (set(dig.values()) & others))
pin = {cell(r): r for r in pinned}
for d in range(10):
    p = pin[dig[d]]
    print(f'     digit {d} -> cell {dig[d]:#04x}: pinned table says status={p["status"]} name={p["name"]!r} spellings(iast/deva/uk)=({p["sa-iast"]!r},{p["sa-deva"]!r},{p["uk"]!r})')
taken = [d for d in dig if pin[dig[d]]['status'] == 'assigned']
print('     digits whose cell is ASSIGNED (not reserved) in the pinned table:', [(d, hex(dig[d]), pin[dig[d]]['sa-iast']) for d in taken])
check('9 of 10 digit cells are reserved in the pinned table; digit 7 sits on the pinned cell of h (v3 moved h to 0x21)', taken == [7] and pin[dig[7]]['sa-iast'] == 'h' and [r for r in rows if r['sound'] == 'h'][0]['bits'] == '0100001')

# spelling: my own codec from the TSV, then the subject
cols = {'sa-iast': 'sa-iast', 'sa-deva': 'sa-deva', 'sa-cyr': 'sa-cyr', 'uk': 'uk'}
glyph_owner = {}
for lay, col in cols.items():
    owners = {}
    for r in rows:
        if r[col]: owners.setdefault(r[col], []).append(r['sound'])
    for d in range(10):
        g = [r[col] for r in rows if r['sound'] == f'digit-{d}'][0]
        check(f'{lay}: glyph {g!r} of digit {d} names only that cell in the table', owners[g] == [f'digit-{d}'])
        glyph_owner[(lay, g)] = d

sys.path.insert(0, str(proto))
import upc7_lang as L
T = L.LangText(); rnd = random.Random(7)
samples = [str(i) for i in range(100)] + [''.join(rnd.choice('0123456789') for _ in range(rnd.randrange(1, 25))) for _ in range(300)]
deva = '०१२३४५६७८९'
bad = 0
for lay in ('uk', 'sa-iast', 'sa-deva', 'sa-cyr'):
    for s in samples:
        txt = ''.join(deva[int(c)] for c in s) if lay == 'sa-deva' else s
        want = tuple(dig[int(c)] for c in s)
        try:
            got = T.encode(txt, lay); back = T.render(got, lay)
        except L.LangError as e:
            bad += 1; print('  refused', lay, repr(txt), e); continue
        if got != want or back != txt: bad += 1; print('  mismatch', lay, repr(txt), got, want, repr(back))
check('round trip text->cells->text, 4 layouts x 400 strings, cells equal the TSV cells', bad == 0, f'{bad} failures')
mix = {'uk': 'к7т', 'sa-iast': 'k7t', 'sa-deva': 'क७त'}
for lay, t in mix.items():
    try: check(f'{lay}: digit between letters round-trips', T.render(T.encode(t, lay), lay) == t)
    except L.LangError as e: check(f'{lay}: digit between letters round-trips', False, str(e))
for lay, t in (('sa-deva', '7'), ('uk', '७'), ('sa-iast', '७'), ('sa-cyr', '७')):
    try: T.encode(t, lay); check(f'{lay} refuses the foreign digit glyph {t!r}', False)
    except L.LangError: check(f'{lay} refuses the foreign digit glyph {t!r}', True)

# affine law
base = dig[0]; gen = [dig[1 << i] ^ base for i in range(4)]
tested = fails = 0
for a, b, c in itertools.product(range(10), repeat=3):
    x = a ^ b ^ c
    if x < 10:
        tested += 1; fails += (dig[a] ^ dig[b] ^ dig[c] ^ dig[x]) != 0
check('affine law cell(a)^cell(b)^cell(c)^cell(a^b^c)=0', fails == 0, f'{tested} triples, base={base:#04x} generators={[hex(g) for g in gen]}')
check('generators are independent (rank 4)', len({g1 ^ g2 for g1 in (0, gen[0]) for g2 in (0, gen[1])} | {0}) >= 4 and len({sum(0 for _ in ()) or 0}) >= 1 and
      len({ (gen[0] if m & 1 else 0) ^ (gen[1] if m & 2 else 0) ^ (gen[2] if m & 4 else 0) ^ (gen[3] if m & 8 else 0) for m in range(16)}) == 16)
sub = {base ^ (gen[0] if m & 1 else 0) ^ (gen[1] if m & 2 else 0) ^ (gen[2] if m & 4 else 0) ^ (gen[3] if m & 8 else 0): m for m in range(16)}
print('     the 16-cell affine subspace: cells of digit values 10..15 =', {m: hex(c) for c, m in sub.items() if m >= 10}, 'used by v3 rows:', sorted(sub_c for sub_c, m in sub.items() if m >= 10 and sub_c in others))

# digit is not Number
order = sorted(range(10), key=lambda d: dig[d])
check('cell order is NOT value order (so a cell comparison is not a number comparison)', order != list(range(10)), 'order by cell: ' + str(order))
check('cell difference is not value difference', any((dig[b] - dig[a]) != (b - a) for a in range(10) for b in range(a + 1, 10)))

# placement census over the cells free BEFORE the digits (v3 without digit rows)
used = {cell(r) for r in rows if not r['sound'].startswith('digit-')}
free = sorted(set(range(128)) - used)
runs, cur = [], []
for c in free:
    if cur and c == cur[-1] + 1: cur.append(c)
    else:
        if cur: runs.append(cur)
        cur = [c]
if cur: runs.append(cur)
print('     free cells before the digits:', len(free), free)
print('     longest contiguous free run:', max(map(len, runs)), ' runs:', [(r[0], len(r)) for r in runs])
vowel_cells = {cell(r) for r in rows if r['class'] == 'vowel'}
print('     vowel-class cells occupy', hex(min(vowel_cells)), '..', hex(max(vowel_cells)))
def census(fcells, label):
    fs, n_distinct = set(fcells), set()
    for b0 in fcells:
        cand = [f ^ b0 for f in fcells if f != b0]
        for g0 in cand:
            for g1 in cand:
                if g1 == g0: continue
                for g2 in cand:
                    if g2 in (g0, g1) or g2 == g0 ^ g1: continue
                    for g3 in cand:
                        cs = [b0 ^ (g0 if d & 1 else 0) ^ (g1 if d & 2 else 0) ^ (g2 if d & 4 else 0) ^ (g3 if d & 8 else 0) for d in range(10)]
                        if len(set(cs)) == 10 and all(c in fs for c in cs): n_distinct.add(tuple(cs))
    print(f'     {label}: affine placements d -> cell (ordered generators, distinct maps):', len(n_distinct),
          ' with all four generators single-bit:', sum(all(bin(g).count("1") == 1 for g in (c[1] ^ c[0], c[2] ^ c[0], c[4] ^ c[0], c[8] ^ c[0])) for c in n_distinct))
    return n_distinct
census([c for c in free if c not in vowel_cells], 'free non-vowel cells')
ordinal = [b for b in free if all(b + k in set(free) for k in range(10))]
check('an ORDINAL placement (10 consecutive free cells) exists in the free cells (expected: no)', not ordinal, 'longest run 7 (0x19..0x1f)')
sys.exit(0 if ok else 1)
