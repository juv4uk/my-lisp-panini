#!/usr/bin/env python3
"""D7 adversarial check (SENS #2415, #2366 style): which cell-level laws of the UPC-7 v3 table survive a relabelling of the 128 cells?
Laws measured on the table itself: asp / voice (varga stop pairs), long / nasal (vowel pairs), digit affine law (0..9), class = top 2 bits.
Experiments: E1 uniform random permutation of the 128 cells; E2 random invertible GF(2)-affine map; E3 a structured, NON-affine group G that moves
whole runs (varga places, non-varga rows, vowel rows) and fixes the digit row. Usage: python3 review_d7_relabel_attack.py --proto <shiva-sutras/prototype> [--n 2000]
"""
import csv, itertools, math, random, sys, unicodedata
from pathlib import Path

proto = Path(sys.argv[sys.argv.index('--proto') + 1]); N = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 2000
rows = list(csv.DictReader(open(proto / 'upc7-table-v3.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
nfc = lambda t: unicodedata.normalize('NFC', t)
cell = {nfc(r['sound']): int(r['bits'], 2) for r in rows}; cls = {int(r['bits'], 2): r['class'] for r in rows}
places = ['k', 'c', 'ṭ', 't', 'p']
asp = [(p, p + 'h') for p in ('k', 'c', 'ṭ', 't', 'p')] + [(v, v + 'h') for v in ('g', 'j', 'ḍ', 'd', 'b')]
voice = [(a, b) for a, b in zip(['k', 'kh', 'c', 'ch', 'ṭ', 'ṭh', 't', 'th', 'p', 'ph'], ['g', 'gh', 'j', 'jh', 'ḍ', 'ḍh', 'd', 'dh', 'b', 'bh'])]
long_ = [('a', 'ā'), ('i', 'ī'), ('u', 'ū'), ('ṛ', 'ṝ'), ('ã', 'ā̃'), ('ĩ', 'ī̃'), ('ũ', 'ū̃'), ('ṛ̃', 'ṝ̃')]
nasal = [('a', 'ã'), ('ā', 'ā̃'), ('i', 'ĩ'), ('ī', 'ī̃'), ('u', 'ũ'), ('ū', 'ū̃'), ('ṛ', 'ṛ̃'), ('ṝ', 'ṝ̃'), ('ḷ', 'ḷ̃'), ('e', 'ẽ'), ('ai', 'aĩ'), ('o', 'õ'), ('au', 'aũ')]
digits = {d: cell[f'digit-{d}'] for d in range(10)}
for pairs in (asp, voice, long_, nasal):
    for a, b in pairs: assert nfc(a) in cell and nfc(b) in cell, (a, b)

def laws(m):
    """m: old cell -> new cell. Returns {law: (constant additive delta?, constant xor delta?, same value as before?)} and the two global laws."""
    out = {}
    for name, pairs in (('asp', asp), ('voice', voice), ('long', long_), ('nasal', nasal)):
        add = {(m[cell[nfc(b)]] - m[cell[nfc(a)]]) % 128 for a, b in pairs}; xr = {m[cell[nfc(b)]] ^ m[cell[nfc(a)]] for a, b in pairs}
        old = {(cell[nfc(b)] - cell[nfc(a)]) % 128 for a, b in pairs}
        out[name] = (len(add) == 1, len(xr) == 1, add == old)
    c = [m[digits[d]] for d in range(10)]
    out['digit-affine'] = all(c[a] ^ c[b] ^ c[cc] ^ c[a ^ b ^ cc] == 0 for a in range(10) for b in range(10) for cc in range(10) if a ^ b ^ cc < 10)
    byp = {}
    for old_cell, k in cls.items(): byp.setdefault(m[old_cell] >> 5, set()).add(k)
    pre = {}
    for p, ks in byp.items():
        for k in ks: pre.setdefault(k, set()).add(p)
    out['class-prefix'] = all(len(v) == 1 for v in byp.values()) and all(len(v) == 1 for v in pre.values())      # top 2 bits <-> class, both ways
    return out

def is_affine(m):
    return all(m[a] ^ m[b] ^ m[c] ^ m[a ^ b ^ c] == 0 for a, b, c in ((random.randrange(128), random.randrange(128), random.randrange(128)) for _ in range(300)))

def summarize(title, perms):
    cnt = {}; tot = 0; aff = 0
    for m in perms:
        tot += 1; aff += is_affine(m)
        for k, v in laws(m).items():
            if isinstance(v, tuple):
                for i, lab in enumerate(('const+', 'const^', 'same+')): cnt[f'{k}:{lab}'] = cnt.get(f'{k}:{lab}', 0) + v[i]
            else: cnt[k] = cnt.get(k, 0) + v
    print(f'{title}: {tot} relabellings, affine {aff}')
    print('   ' + '  '.join(f'{k}={v}' for k, v in cnt.items()))

rnd = random.Random(2415); random.seed(2415)
ident = {c: c for c in range(128)}
print('identity (the table itself):', {k: v for k, v in laws(ident).items()})

def uniform():
    p = list(range(128)); rnd.shuffle(p); return dict(enumerate(p))
def affine_map():
    while True:
        A = [rnd.randrange(1, 128) for _ in range(7)]; b = rnd.randrange(128)
        def f(x): return sum((bin(A[i] & x).count('1') & 1) << i for i in range(7)) ^ b
        img = [f(x) for x in range(128)]
        if len(set(img)) == 128: return dict(enumerate(img))
# structured group G: permute whole runs, fix everything that is not a run of the law
def structured():
    m = dict(ident)
    sv = list(range(5)); rnd.shuffle(sv)                                  # varga places (runs of 5 cells 0..24)
    for p in range(5):
        for j in range(5): m[p * 5 + j] = sv[p] * 5 + j
    rows_nv = [r for r in range(8, 14)]           # non-varga rows 0x20..0x37 (digit row 14 = 0x38..0x3b stays)
    sn = rows_nv[:]; rnd.shuffle(sn)
    for r, s in zip(rows_nv, sn):
        for j in range(4): m[r * 4 + j] = s * 4 + j
    rows_v = list(range(16, 24)); sw = rows_v[:]; rnd.shuffle(sw)         # vowel rows 0x40..0x5f
    for r, s in zip(rows_v, sw):
        for j in range(4): m[r * 4 + j] = s * 4 + j
    assert len(set(m.values())) == 128
    return m
summarize('E1 uniform random permutation of 128 cells', (uniform() for _ in range(N)))
summarize('E2 random invertible GF(2)-affine relabelling', (affine_map() for _ in range(N)))
summarize('E3 structured relabelling (runs permuted as units; digit row, signs fixed)', (structured() for _ in range(N)))
size = math.factorial(5) * math.factorial(6) * math.factorial(8)
moved = sum(1 for _ in range(N) if structured()[0] != 0)
print(f'|G| = 5! * 6! * 8! = {size} relabellings (place order of the 5 varga series, 6 non-varga rows, 8 vowel rows); a random one moves the cell of k in {moved}/{N} samples')
m = structured()
print('example: k->', m[cell[nfc('k')]], ' t->', m[cell['t']], ' a->', m[cell['a']], ' (before: ', cell[nfc('k')], cell['t'], cell['a'], ')')
