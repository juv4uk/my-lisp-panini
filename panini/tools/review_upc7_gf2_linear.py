#!/usr/bin/env python3
"""Independent check of the claim of shiva-sutras PR #84: a GF(2)-linear 7-bit cell map exists on the Sanskrit vertices
where asp, voice, long are each ONE xor delta. Written from the PR description only (not from its code).

Observation tested here: for ANY GF(2)-linear map L (7x14 matrix), L(c ^ m) = L(c) ^ L(m), so an edge that is a constant xor mask
m on the 14-bit codes is automatically ONE constant delta L(m) in the image. The nontrivial content of the claim is therefore only
INJECTIVITY of L on the vertex set (equivalently: a 7-dim subspace ker L avoiding all pairwise xors of the vertex codes).
This script (1) builds the vertex set (42 sounds + long ā ī ū ṝ + nasal forms of the 9 simple vowels and 4 long vowels = 59),
(2) checks which edges are constant xor masks on this set, (3) searches L by hill-climbing on collision count, (4) verifies the
deltas in the image.   Usage: python3 review_upc7_gf2_linear.py --graph /path/to/prototype [--seed 3] [--steps 200000]
"""
import sys, random, itertools

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]
    seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 3
    steps = int(sys.argv[sys.argv.index('--steps') + 1]) if '--steps' in sys.argv else 200000
    sys.path.insert(0, gd)
    import upc14v2 as g
    S = g.SOUNDS
    V = {k: c for k, c in S.items()}
    for k, b in (('ā', 'a'), ('ī', 'i'), ('ū', 'u'), ('ṝ', 'ṛ')): V[k] = g.e_long(S[b])
    base = ['a', 'i', 'u', 'ṛ', 'ḷ', 'e', 'o', 'ai', 'au', 'ā', 'ī', 'ū', 'ṝ']
    for b in base:
        w = g.unpack(V[b]); V[b + '~'] = g.Vertex(w.place, 1, w.aperture, w.length, w.voice, w.asp).code
    codes = sorted(set(V.values()))
    print('vertices: %d named, %d distinct codes' % (len(V), len(codes)))
    cs = set(codes)
    def mask_set(f):
        return {c ^ f(c) for c in codes if safe(f, c) is not None and safe(f, c) in cs}
    def safe(f, c):
        try: return f(c)
        except Exception: return None
    for name, f in (('asp', g.e_asp), ('voice', g.e_voice), ('long', g.e_long), ('nasal', g.e_nasal)):
        ms = {c ^ safe(f, c) for c in codes if safe(f, c) in cs}
        print('  edge %-5s: pairs inside the set %d; distinct xor masks on the 14-bit codes: %s' % (name, sum(1 for c in codes if safe(f, c) in cs), sorted(format(m, '#06x') for m in ms)))
    # linear map = 7 row masks over 14 bits; L(c) = 7 parity bits
    def apply(rows, c): return sum(((bin(r & c).count('1') & 1) << i) for i, r in enumerate(rows))
    def collisions(rows):
        seen = {}; n = 0
        for c in codes:
            v = apply(rows, c)
            n += seen.get(v, 0); seen[v] = seen.get(v, 0) + 1
        return n
    rnd = random.Random(seed)
    rows = [rnd.randrange(1, 1 << 14) for _ in range(7)]; best = collisions(rows)
    for it in range(steps):
        if best == 0: break
        i = rnd.randrange(7); old = rows[i]
        rows[i] = old ^ (1 << rnd.randrange(14)) if rnd.random() < 0.8 else rnd.randrange(1, 1 << 14)
        c = collisions(rows)
        if c <= best: best = c
        else: rows[i] = old
    print('hill-climb: collision count %d after %d steps (0 = injective)' % (best, it))
    if best == 0:
        print('rows (bit masks over the 14-bit code):', [format(r, '014b') for r in rows])
        for name, f in (('asp', g.e_asp), ('voice', g.e_voice), ('long', g.e_long), ('nasal', g.e_nasal)):
            d = {apply(rows, c) ^ apply(rows, safe(f, c)) for c in codes if safe(f, c) in cs}
            print('  image deltas of %-5s: %d distinct %s' % (name, len(d), sorted(format(x, '07b') for x in d)))

if __name__ == '__main__':
    main()
