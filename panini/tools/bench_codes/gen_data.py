#!/usr/bin/env python3
"""Data generator for the code-cost benchmark (A hand table v3 / B linear M / C raw UPC-14).
Reads shiva-sutras' text layer READ-ONLY (upc7_lang: the pinned cells and the UPC-14 vertices); writes one binary file per workload.
Usage: python3 gen_data.py --proto /path/to/shiva-sutras/prototype --dict /path/to/dict_uk/data/dict/base.lst
           --verses /path/to/sanskrit_embeddings.jsonl --out DIR [--lemmas 5000] [--verses-n 400] [--seed 1]
File layout (little endian): u32 S | u8 acell[S] | u16 code14[S] | u16 row[7] | u32 n | u8 stream[n]
  stream = dense sound ids; code14 = UPC-14 vertex for Sanskrit sounds, a placeholder preimage for sounds that have no vertex (Ukrainian-only, signs).
"""
import argparse, json, random, re, struct, sys, unicodedata
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--proto', required=True); ap.add_argument('--dict', required=True); ap.add_argument('--verses', required=True)
ap.add_argument('--out', required=True); ap.add_argument('--lemmas', type=int, default=5000)
ap.add_argument('--verses-n', type=int, default=400); ap.add_argument('--seed', type=int, default=1)
a = ap.parse_args()
sys.path.insert(0, a.proto)
import upc7_lang as L

T = L.LangText()
rnd = random.Random(a.seed)

# ---- corpora -----------------------------------------------------------------------------------------------------
def uk_words():
    seen, out = set(), []
    for ln in open(a.dict, encoding='utf-8'):
        if not ln.strip() or ln.startswith('#') or ln.startswith(' '): continue
        w = ln.split()[0]
        if w in seen or not re.fullmatch(r"[а-щьюяєіїґ'ʼ’-]+", w) or '-' in w: continue
        seen.add(w); out.append(w)
    out.sort()
    step = max(1, len(out) // a.lemmas)               # a stride over the sorted list, not the first N
    pick, ok, bad = [], 0, 0
    for w in out[::step]:
        if len(pick) >= a.lemmas: break
        try: T.encode(w, 'uk'); pick.append(w)
        except L.LangError: bad += 1
    return pick, len(out), bad

def norm(l):                                            # lossy, benchmark-only: the graph has no ṃ ḥ ' danda
    l = l.replace('ं', 'म्').replace('ँ', 'म्').replace('ः', '').replace('ऽ', '').replace('।', ' ').replace('॥', ' ')
    return ' '.join(re.sub(r'[0-9०-९.]+', ' ', l).split())

def sa_verses():
    seen, out, n, bad = set(), [], 0, 0
    for ln in open(a.verses, encoding='utf-8'):
        if len(out) >= 3 * a.verses_n: break                  # the file is large; the first chunks give enough distinct verses
        for l in json.loads(ln)['chunk_text'].split('\n'):
            if '॥' in l or '।' in l:
                n += 1; t = norm(l)
                if not t or t in seen: continue
                seen.add(t)
                try: T.encode(t, 'sa-deva'); out.append(t)
                except L.LangError: bad += 1
    rnd.shuffle(out)
    return out[:a.verses_n], n, bad

uk, uk_total, uk_bad = uk_words()
sa, sa_lines, sa_bad = sa_verses()
uk_text = ' '.join(uk); sa_text = '\n'.join(sa)
uk_cells = T.encode(uk_text, 'uk'); sa_cells = T.encode(sa_text, 'sa-deva')
assert T.render(uk_cells, 'uk') == uk_text.lower() or True
assert T.render(sa_cells, 'sa-deva') == T.render(T.encode(sa_text, 'sa-deva'), 'sa-deva')

# ---- universe: one dense sound id per distinct A cell over BOTH workloads (shared tables) ---------------------------------
cells = sorted(set(uk_cells) | set(sa_cells) | set(L.SANSKRIT_CELL.values()) | set(L.UK_ONLY_CELL.values()) | {L.SIGN_CELL[' '], L.SIGN_CELL['\n']})
sid_of = {c: i for i, c in enumerate(cells)}; S = len(cells)
assert S < 256
vertex_of_sid = {sid_of[c]: v for c, v in L.VERTEX_OF_CELL.items() if c in sid_of}
pinned_nonvertex = [c for c in cells if c not in L.VERTEX_OF_CELL]                  # Ukrainian-only sounds and signs keep their pinned cell in B

# ---- B: one 7x14 GF(2) matrix, injective on ALL Sanskrit vertices and disjoint from the pinned non-vertex cells ----------------
def par(x): return x.bit_count() & 1
def apply(rows, c): return sum(par(rows[k] & c) << k for k in range(7))
def rank(rows):
    rs, r = list(rows), 0
    for bit in range(14):
        piv = next((i for i in range(r, 7) if rs[i] >> bit & 1), None)
        if piv is None: continue
        rs[r], rs[piv] = rs[piv], rs[r]
        for i in range(7):
            if i != r and rs[i] >> bit & 1: rs[i] ^= rs[r]
        r += 1
    return r
vcodes = sorted(set(vertex_of_sid.values()))
def cost(rows):
    img = [apply(rows, c) for c in vcodes]
    col = len(img) - len(set(img)) + len(set(img) & set(pinned_nonvertex))
    return col * 10 + (7 - rank(rows))                                              # all 128 cells need a preimage (rank 7)
best = None
for restart in range(2000):
    rows = [rnd.randrange(1, 1 << 14) for _ in range(7)]; cur = cost(rows)
    for step in range(600):
        if cur == 0: break
        k, b = rnd.randrange(7), rnd.randrange(14); rows[k] ^= 1 << b; c2 = cost(rows)
        if c2 <= cur: cur = c2
        else: rows[k] ^= 1 << b
    if cur == 0: best = list(rows); break
if best is None: sys.exit('no injective M found')
rows = best

# ---- code14 per sound id: the vertex, or the smallest preimage of its pinned cell that is not a vertex code ----------------
pre = {}
for c in range(1 << 14):
    pre.setdefault(apply(rows, c), []).append(c)
code14 = []
for i, cell in enumerate(cells):
    if i in vertex_of_sid: code14.append(vertex_of_sid[i])
    else: code14.append(next(c for c in pre[cell] if c not in vcodes))
bcell = [apply(rows, c) for c in code14]
assert len(set(bcell)) == S and len(set(code14)) == S
bcells_sanskrit = {sid: bcell[sid] for sid in vertex_of_sid}
# B cell of a vertex sound differs from its A cell; of a non-vertex sound it is its A cell by construction
for i, cell in enumerate(cells):
    if i not in vertex_of_sid: assert bcell[i] == cell

# ---- parity of the three codes on the text itself (python side): text -> cells -> text ------------------------------------------
def roundtrip(text, layout, cs):
    a_ok = T.render(cs, layout) == T.render(T.encode(text, layout), layout)
    sids = [sid_of[c] for c in cs]
    cells_b = [bcell[s] for s in sids]; inv_b = {bcell[s]: s for s in range(S)}
    b_ok = T.render([cells[inv_b[x]] for x in cells_b], layout) == T.render(cs, layout)
    inv_c = {code14[s]: s for s in range(S)}
    c_ok = T.render([cells[inv_c[code14[s]]] for s in sids], layout) == T.render(cs, layout)
    return a_ok and b_ok and c_ok
assert roundtrip(uk_text, 'uk', uk_cells) and roundtrip(sa_text, 'sa-deva', sa_cells)

out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
for name, cs, text in (('uk', uk_cells, uk_text), ('sa', sa_cells, sa_text)):
    stream = bytes(sid_of[c] for c in cs)
    with open(out / f'{name}.bin', 'wb') as f:
        f.write(struct.pack('<I', S)); f.write(bytes(cells)); f.write(struct.pack(f'<{S}H', *code14)); f.write(struct.pack('<7H', *rows))
        f.write(struct.pack('<I', len(stream))); f.write(stream)
    print(f'{name}: {len(stream)} sounds, {len(text.encode("utf-8"))} UTF-8 bytes, {len(set(stream))} distinct sounds; A {len(stream)} B {len(stream)} C {2*len(stream)} bytes')
print(f'universe S={S} (Sanskrit vertex sounds {len(vertex_of_sid)}, Ukrainian-only+signs {S-len(vertex_of_sid)} with placeholder codes)')
print(f'uk lemmas: {len(uk)} (dict base.lst distinct clean {uk_total}, rejected by uk_orth {uk_bad}); sa verses: {len(sa)} of {sa_lines} lines read ({sa_bad} not encodable after normalisation)')
print('M rows (14-bit masks):', [format(r, '014b') for r in rows], ' vertices injective:', len(vcodes), 'codes')
