#!/usr/bin/env python3
"""Independent check of upc14v2.pratyahara_named(name) (shiva PR #68), against my own 43-name oracle.

Usage: python3 panini/tools/review_upc14_named_api.py --graph /path/to/shiva-sutras/prototype
Expects every one of my 43 named pratyaharas (second_impl NAMED) to give the same sound stream through
pratyahara_named(name), and unknown/malformed names (bhas-with-sibilant, '', 'xyz', 'an3') to fail closed.
"""
import sys, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('o', os.path.join(HERE, 'second_impl_pratyahara_savarna.py'))
o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]
    sys.path.insert(0, gd)
    import upc14v2 as g
    lab = {c: l for l, c in g.SOUNDS.items()}
    vowels = {'a', 'i', 'u', 'f', 'x', 'e', 'o', 'E', 'O'}
    ok = bad = 0
    for k, (st, mk, nth, so) in o.NAMED.items():
        s, m = o.SLP1_TO_IAST[st], o.SLP1_TO_IAST[mk]
        name = 'aṇ2' if k == 'aR2' else ((s + m) if st in vowels else (s + 'a' + m))
        try:
            got = [lab[c] for c in g.pratyahara_named(name)]
        except Exception as e:
            print('ERR', name, type(e).__name__, e); bad += 1; continue
        exp = [o.SLP1_TO_IAST[x] for x in o.pratyahara(st, so, mk, nth)]
        if got == exp: ok += 1
        else: bad += 1; print('DIFF', name, got, exp)
    print('named: equal %d, different/err %d, of %d' % (ok, bad, len(o.NAMED)))
    for n in ['bhaś', 'xyz', '', 'aṇ3']:
        try:
            g.pratyahara_named(n); print('ACCEPTED (should fail closed):', repr(n))
        except Exception as e:
            print('rejected', repr(n), type(e).__name__)

if __name__ == '__main__':
    main()
