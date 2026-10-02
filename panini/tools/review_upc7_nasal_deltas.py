#!/usr/bin/env python3
"""Why the GF(2)-linear 7-bit map has 5 nasal deltas (SENS #2359): classify the xor masks of e_nasal over the 59 Sanskrit vertices.
The graph's nasal DERIVATION edge (voiced unaspirated stop -> nasal; vowel -> nasal vowel) is the constant xor 0x0080; the other masks
(0x81, 0x82, 0x83) come from applying the NORMALISING e_nasal ((c | 0x82) & ~1: set voice, clear asp) to k/kh/gh/... and 0x0000 is the
idempotent pair (already nasal).   Usage: python3 review_upc7_nasal_deltas.py --graph /path/to/prototype
"""
import sys
from collections import Counter

def main():
    sys.path.insert(0, sys.argv[sys.argv.index('--graph') + 1])
    import upc14v2 as g
    S = g.SOUNDS; V = dict(S)
    for k, b in (('ā', 'a'), ('ī', 'i'), ('ū', 'u'), ('ṝ', 'ṛ')): V[k] = g.e_long(S[b])
    for b in ['a', 'i', 'u', 'ṛ', 'ḷ', 'e', 'o', 'ai', 'au', 'ā', 'ī', 'ū', 'ṝ']:
        w = g.unpack(V[b]); V[b + '~'] = g.Vertex(w.place, 1, w.aperture, w.length, w.voice, w.asp).code
    lab = {c: l for l, c in V.items()}; cs = set(V.values())
    rows = []
    for c in sorted(cs):
        try: d = g.e_nasal(c)
        except Exception: continue
        if d in cs: rows.append((lab[c], lab[d], c ^ d, g.unpack(c).aperture >= 3))
    print('nasal pairs inside the 59-vertex set: %d' % len(rows))
    for (m, v), n in sorted(Counter((hex(m), 'vowel' if v else 'stop') for _, _, m, v in rows).items()): print('  mask %-5s %-5s %d' % (m, v, n))
    print('derivation nasal edges (child <- parent):', [(c, p) for c, p, e in g.DERIVATION if e == 'nasal'])
    d80 = [(a, b) for a, b, m, _ in rows if m == 0x80]
    print('pairs with the single mask 0x0080: %d (5 stop derivation edges + %d vowel nasalisations)' % (len(d80), len(d80) - 5))

if __name__ == '__main__':
    main()
