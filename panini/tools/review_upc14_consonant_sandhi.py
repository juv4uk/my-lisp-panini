#!/usr/bin/env python3
"""Independent oracle for pada-final stop sandhi (8.2.39, 8.4.40, 8.4.41, 8.4.60, 8.4.45, 8.4.55, 8.4.62, 8.4.63),
written from the sutra texts and the rule ORDER stated in upc14v2_sandhi's module docstring (NOT from its code).
Sound classes are computed from the Siva-sutra path (my pratyahara oracle) and the five vargas; substitution is the
'nearest' sound of the target set (1.1.50), here: same row of the target varga.
Compared with upc14v2_sandhi.final_stop(left, right, after): final left, right, and the list of sutras that fired.

Usage: python3 review_upc14_consonant_sandhi.py --graph /path/to/shiva-sutras/prototype
"""
import os, sys, itertools, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
# IAST rows of the five vargas: unvoiced, unvoiced+asp, voiced, voiced+asp, nasal
VARGA = [['k', 'kh', 'g', 'gh', 'ṅ'], ['c', 'ch', 'j', 'jh', 'ñ'], ['ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ'],
         ['t', 'th', 'd', 'dh', 'n'], ['p', 'ph', 'b', 'bh', 'm']]
LOC = {s: (v, r) for v, row in enumerate(VARGA) for r, s in enumerate(row)}
CU, TU, TTU = set(VARGA[1]), set(VARGA[3]), set(VARGA[2])      # c-varga, t-varga, ṭ-varga (names as in the sutras: cu, tu, ṭu)

def sets_from_path(oracle):
    """jhal, jaś, khar, car, yar, jhay, aṭ, nasals as IAST sets, computed by the independent pratyahara oracle."""
    P = lambda st, mk: {oracle.SLP1_TO_IAST[x] for x in oracle.pratyahara(st, 1, mk, 1)}
    return {'jhal': P('J', 'l'), 'jaś': P('j', 'S'), 'khar': P('K', 'r'), 'car': P('c', 'r'), 'yar': P('y', 'r'),
            'jhay': P('J', 'y'), 'aṭ': P('a', 'w'), 'ñam': P('Y', 'm') | {'ṅ'}}

def nearest_row(x, target_varga):
    """1.1.50: same row in the target varga (stops only)."""
    _, r = LOC[x]
    return VARGA[target_varga][r]

def final_stop_oracle(left, right, after, C):
    """A step is recorded only when the sound actually changes (a rule that fires on a sound already in the
    target set is a no-op)."""
    steps = []
    L, R = left, right
    def setL(sutra, new):
        nonlocal L
        if new != L: steps.append(sutra)
        L = new
    def setR(sutra, new):
        nonlocal R
        if new != R: steps.append(sutra)
        R = new
    if L in C['jhal']:                                   # 8.2.39 jhalam jaso 'nte
        setL('8.2.39', VARGA[LOC[L][0]][2])
    if L in TU and (R in CU or R == 'ś'):                 # 8.4.40 stoh ścunā ścuh
        setL('8.4.40', nearest_row(L, 1))
    elif L in TU and (R in TTU or R == 'ṣ'):              # 8.4.41 ṣṭunā ṣṭuḥ
        setL('8.4.41', nearest_row(L, 2))
    if L in TU and R == 'l':                              # 8.4.60 torli
        setL('8.4.60', 'l')
    if L in C['yar'] and R in C['ñam']:                   # 8.4.45 yaro 'nunasike 'nunasiko va
        setL('8.4.45', VARGA[LOC[L][0]][4])
    elif L in C['jhal'] and R in C['khar']:               # 8.4.55 khari ca
        setL('8.4.55', VARGA[LOC[L][0]][0])
    if L in C['jhay'] and R == 'h':                       # 8.4.62 jhayo ho 'nyatarasyam
        setR('8.4.62', VARGA[LOC[L][0]][3])
    if L in C['jhay'] and R == 'ś' and after in C['aṭ']:  # 8.4.63 śaś cho 'ṭi
        setR('8.4.63', 'ch')
    return L, R, steps

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]
    spec = importlib.util.spec_from_file_location('o', os.path.join(HERE, 'second_impl_pratyahara_savarna.py'))
    o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)
    C = sets_from_path(o)
    sys.path.insert(0, gd)
    import upc14v2_sandhi as sd
    lefts = [s for row in VARGA for s in row if s not in ('ṅ', 'ñ', 'ṇ', 'n', 'm')]
    rights = list(o.IAST_TO_SLP1.keys())
    total = eq = df = err = 0; shown = 0; byrule = {}
    for l in lefts:
        for r in rights:
            for after in ('a', 'k'):
                if r != 'ś' and after == 'k': continue
                total += 1
                try:
                    got = sd.final_stop(l, r, after)
                    gl, gr, gt = got.left, got.right, [s.sutra for s in got.trace]
                except Exception as e:
                    err += 1; continue
                ml, mr, mt = final_stop_oracle(l, r, after, C)
                if (gl, gr, gt) == (ml, mr, mt): eq += 1
                else:
                    df += 1
                    key = tuple(sorted(set(gt) ^ set(mt)))
                    byrule[key] = byrule.get(key, 0) + 1
                    if shown < 25:
                        shown += 1; print('DIFF %s + %s (after %s): graph (%s,%s,%s) mine (%s,%s,%s)' % (l, r, after, gl, gr, gt, ml, mr, mt))
    print('\nfinal_stop: compared %d, equal %d, DIFFERENT %d, graph raised %d' % (total, eq, df, err))
    print('differences by symmetric difference of sutras:', byrule)

if __name__ == '__main__':
    main()
