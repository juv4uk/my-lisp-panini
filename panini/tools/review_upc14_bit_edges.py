#!/usr/bin/env python3
"""Independent check of the claim of shiva-sutras PR #72: every typed edge of the UPC-14 sound graph is ONE bit
operation on the 14-bit code. Written from the PR description only (NOT prototype/upc14v2_bitops.py).

Layout (header of upc14v2.py): bit13 meta | 12..8 place | 7 nasal | 6..4 aperture | 3..2 length | 1 voice | 0 asp.
Claimed bit forms:  asp = c ^ 1;  voice = c ^ 2;  nasal = (c | 0x82) & ~1;  shift = place << 1 (bits 8..12);
                    lift(n) = c + 16*n;  join(atoms) = c | (atoms << 8);  long = c + 4.
Usage: python3 review_upc14_bit_edges.py --graph /path/to/prototype
"""
import sys

def main():
    sys.path.insert(0, sys.argv[sys.argv.index('--graph') + 1])
    import upc14v2 as g
    FULL = (1 << 14) - 1
    def valid(c):
        try: g.unpack(c); return True
        except Exception: return False
    V = [c for c in range(1 << 14) if valid(c)]
    print('codes 0..%d: vertices (unpack ok) %d; non-vertices %d' % (FULL, len(V), (1 << 14) - len(V)))
    def call(f, *a):
        try: return ('ok', f(*a))
        except Exception as e: return ('err', type(e).__name__)
    forms = {
        'asp':   (lambda c: g.e_asp(c),   lambda c: c ^ 1),
        'voice': (lambda c: g.e_voice(c), lambda c: c ^ 2),
        'nasal': (lambda c: g.e_nasal(c), lambda c: (c | 0x82) & ~1),
        'shift': (lambda c: g.e_shift(c), lambda c: (c & ~0x1F00) | (((c & 0x1F00) << 1) & 0x1F00) if (c & 0x1F00) << 1 <= 0x1F00 else None),
        'long':  (lambda c: g.e_long(c),  lambda c: c + 4),
    }
    for n in (1, 2, 3):
        forms['lift%d' % n] = ((lambda n: lambda c: g.e_lift(c, n))(n), (lambda n: lambda c: c + 16 * n)(n))
    for atoms in (1, 2, 4, 8, 16, 5, 9, 17):
        forms['join%d' % atoms] = ((lambda a: lambda c: g.e_join(c, a))(atoms), (lambda a: lambda c: c | (a << 8))(atoms))
    print('\nON ALL VERTICES (e_* result vs my bit form; only calls that return a value; an exception is counted separately)')
    print('%-8s %6s %6s %8s %s' % ('edge', 'equal', 'DIFF', 'raised', 'first differences (code -> e_*, bit form)'))
    for name, (f, bf) in forms.items():
        eq = df = er = 0; ex = []
        for c in V:
            r = call(f, c)
            if r[0] == 'err': er += 1; continue
            b = bf(c)
            if b is None: continue
            if r[1] == b: eq += 1
            else:
                df += 1
                if len(ex) < 3: ex.append((format(c, '014b'), format(r[1], '014b'), format(b, '014b') if b is not None else None))
        print('%-8s %6d %6d %8d %s' % (name, eq, df, er, ex))
    print('\nNON-VERTEX acceptance (does e_* return a value for a code that is not a vertex?)')
    NV = [c for c in range(1 << 14) if c not in set(V)]
    for name in ('asp', 'voice', 'nasal', 'shift', 'long', 'lift1', 'join1'):
        f = forms[name][0]
        acc = sum(1 for c in NV if call(f, c)[0] == 'ok')
        print('  e_%-6s returns a value for %d of %d non-vertices' % (name, acc, len(NV)))
    print('\nDERIVATION instances (%d): constant xor mask per edge type' % len(g.DERIVATION))
    S = g.SOUNDS; masks = {}
    for child, parent, edge in g.DERIVATION:
        if parent not in S or child not in S: continue
        masks.setdefault(edge, set()).add(S[child] ^ S[parent])
    for edge, m in sorted(masks.items()): print('  %-12s xor masks seen: %s' % (edge, sorted(format(x, '#06x') for x in m)))

if __name__ == '__main__':
    main()
