#!/usr/bin/env python3
"""Independent question (coordinator, 2026-10-02): does an INJECTIVE GF(2)-linear 7x14 map M exist on the Sanskrit vertices such that the
'shift' edge (place << 1, bits 8..12 of the 14-bit code) becomes ONE AFFINE map T(x) = A x + b on the 7-bit images (all shift pairs inside
the vertex set)?  From the graph definition only (upc14v2 e_shift / e_*), not from upc7_linear_ext.py.

Theory used: S (place<<1 on the code) is linear on GF(2)^14 (identity off the place bits, a nilpotent shift on the 5 place bits).
 - LINEAR T exists iff ker M is S-invariant on the span of the shift pairs; AFFINE T additionally allows a constant b.
 - Existence/frequency are measured: (a) N uniformly random M: how many are injective, how many are injective AND affine-consistent;
   (b) hill-climbs to injective M (independent seeds): fraction affine-consistent; (c) a joint hill-climb that minimises
   collisions + affine inconsistency.
Usage: python3 review_upc7_affine_shift.py --graph /path/to/prototype [--n 200000] [--seeds 300]
"""
import sys, random

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]
    N = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 200000
    SEEDS = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 300
    sys.path.insert(0, gd)
    import upc14v2 as g
    S = g.SOUNDS
    V = dict(S)
    for k, b in (('ā', 'a'), ('ī', 'i'), ('ū', 'u'), ('ṝ', 'ṛ')): V[k] = g.e_long(S[b])
    for b in ['a', 'i', 'u', 'ṛ', 'ḷ', 'e', 'o', 'ai', 'au', 'ā', 'ī', 'ū', 'ṝ']:
        w = g.unpack(V[b]); V[b + '~'] = g.Vertex(w.place, 1, w.aperture, w.length, w.voice, w.asp).code
    codes = sorted(set(V.values())); cs = set(codes)
    def safe(f, c):
        try: return f(c)
        except Exception: return None
    pairs = [(c, safe(g.e_shift, c)) for c in codes if safe(g.e_shift, c) in cs]
    print('vertices %d; shift pairs inside the set: %d' % (len(codes), len(pairs)))
    # S is linear on the codes: check on the pairs
    PL = 0x1F00
    assert all(((c & ~PL) | ((c & PL) << 1 & PL)) == d for c, d in pairs), 'shift is not the linear place<<1'
    def apply(rows, c): return sum(((bin(r & c).count('1') & 1) << i) for i, r in enumerate(rows))
    def collisions(rows):
        seen = {}; n = 0
        for c in codes:
            v = apply(rows, c); n += seen.get(v, 0); seen[v] = seen.get(v, 0) + 1
        return n
    def affine_defect(rows, linear=False):
        """number of output bits j for which no (A[j], b[j]) satisfies all pairs (0 = an affine T exists)"""
        U = [(apply(rows, c), apply(rows, d)) for c, d in pairs]
        bad = 0
        for j in range(7):
            # equations: sum_k A[j][k] u_k + b = v_j ; unknowns 8 bits; Gaussian elimination over GF(2)
            eqs = [((u << 1) | (0 if linear else 1), (v >> j) & 1) for u, v in U]     # row bits: u (7 bits) and the constant column (absent for a LINEAR T)
            basis = []
            ok = True
            for r, rhs in eqs:
                for br, brhs in basis:
                    if r ^ br < r: r ^= br; rhs ^= brhs
                if r == 0:
                    if rhs: ok = False; break
                else: basis.append((r, rhs)); basis.sort(reverse=True)
            if not ok: bad += 1
        return bad
    rnd = random.Random(1)
    inj = both = 0
    for _ in range(N):
        rows = [rnd.randrange(1, 1 << 14) for _ in range(7)]
        if collisions(rows) == 0:
            inj += 1
            if affine_defect(rows) == 0: both += 1
    print('(a) %d uniformly random 7x14 matrices: injective %d; injective AND affine-T-consistent %d' % (N, inj, both))
    # (b) hill-climb to injective M (collisions only), fraction affine-consistent
    found = cons = 0; defects = []
    for sd in range(SEEDS):
        r = random.Random(1000 + sd); rows = [r.randrange(1, 1 << 14) for _ in range(7)]; best = collisions(rows)
        for it in range(20000):
            if best == 0: break
            i = r.randrange(7); old = rows[i]; rows[i] = old ^ (1 << r.randrange(14)) if r.random() < 0.8 else r.randrange(1, 1 << 14)
            c = collisions(rows)
            if c <= best: best = c
            else: rows[i] = old
        if best == 0:
            found += 1; d = affine_defect(rows); defects.append(d)
            if d == 0: cons += 1
    print('(b) %d independent hill-climbs to an injective M: reached %d; of those affine-consistent: %d; defect histogram %s' % (SEEDS, found, cons, {k: defects.count(k) for k in sorted(set(defects))}))
    # (c) joint hill-climb: minimise collisions*10 + affine defect
    sol = None
    for sd in range(60):
        r = random.Random(5000 + sd); rows = [r.randrange(1, 1 << 14) for _ in range(7)]
        cost = lambda rw: 10 * collisions(rw) + affine_defect(rw)
        best = cost(rows)
        for it in range(40000):
            if best == 0: break
            i = r.randrange(7); old = rows[i]; rows[i] = old ^ (1 << r.randrange(14)) if r.random() < 0.8 else r.randrange(1, 1 << 14)
            c = cost(rows)
            if c <= best: best = c
            else: rows[i] = old
        if best == 0: sol = (sd, it, rows); break
    # (d) same joint search for a LINEAR T (b = 0)
    soll = None
    for sd in range(60):
        r = random.Random(9000 + sd); rows = [r.randrange(1, 1 << 14) for _ in range(7)]
        costl = lambda rw: 10 * collisions(rw) + affine_defect(rw, True)
        best = costl(rows)
        for it in range(40000):
            if best == 0: break
            i = r.randrange(7); old = rows[i]; rows[i] = old ^ (1 << r.randrange(14)) if r.random() < 0.8 else r.randrange(1, 1 << 14)
            c = costl(rows)
            if c <= best: best = c
            else: rows[i] = old
        if best == 0: soll = (sd, it); break
    print('(d) joint search for a LINEAR T (b = 0): %s' % (('found (seed %d, %d steps)' % soll) if soll else 'none found in 60 seeds x 40000 steps'))
    if sol:
        sd, it, rows = sol
        U = sorted({(apply(rows, c), apply(rows, d)) for c, d in pairs})
        print('(c) joint search: injective + affine-consistent M found (seed %d, %d steps): rows %s' % (sd, it, [format(x, '014b') for x in rows]))
        # recover T = (A, b)
        print('    pairs images (u -> v):', [(format(u, '07b'), format(v, '07b')) for u, v in U][:6], '...')
    else:
        print('(c) joint search: none found in 60 seeds x 40000 steps')

if __name__ == '__main__':
    main()
