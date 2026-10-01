#!/usr/bin/env python3
"""Independent second implementation of pratyahara and savarna (consumer side).

Inputs ONLY: the 14 Siva-sutras in panini/tests/pratyahara-exhaustive-v0.1.yaml
(siva_sutras block) and the savarna classes read from Kasika 1.1.9 (cited below).
No code from upc14v2 is used for the oracle; upc14v2 is imported only by --graph
for the comparison step.

Usage:
  python3 panini/tools/second_impl_pratyahara_savarna.py [--graph /path/to/shiva-sutras/prototype] [--json]
"""
import os, re, sys, itertools, json

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, '..', 'tests', 'pratyahara-exhaustive-v0.1.yaml')

def sutras():
    txt = open(FIXTURE, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'\{ ordinal: (\d+), sounds: \[(.*?)\], marker: (\S+) \}', txt):
        out.append(([x.strip() for x in m.group(2).split(',')], m.group(3)))
    assert len(out) == 14
    return out

# path = recitation order; each node: (label, is_marker, sutra_no)
PATH = []
for i, (snd, mk) in enumerate(sutras(), 1):
    PATH += [(s, False, i) for s in snd] + [(mk, True, i)]
SOUNDS = []
for l, mk, _ in PATH:
    if not mk and l not in SOUNDS:
        SOUNDS.append(l)
assert len(SOUNDS) == 42


# SLP1 -> IAST (lowercase, with diacritics) for the 42 sounds. upc14v2 changed its keys from SLP1 to
# IAST (stage 2). The oracle stays SLP1 (my-lisp-panini contract, AGENTS section 2); this adapter is
# applied only at the boundary, and compare() auto-detects which spelling the graph uses.
SLP1_TO_IAST = {
    'a': 'a', 'i': 'i', 'u': 'u', 'f': 'ṛ', 'x': 'ḷ', 'e': 'e', 'o': 'o', 'E': 'ai', 'O': 'au',
    'h': 'h', 'y': 'y', 'v': 'v', 'r': 'r', 'l': 'l', 'Y': 'ñ', 'm': 'm', 'N': 'ṅ', 'R': 'ṇ', 'n': 'n',
    'j': 'j', 'J': 'jh', 'b': 'b', 'B': 'bh', 'g': 'g', 'G': 'gh', 'k': 'k', 'K': 'kh', 'c': 'c', 'C': 'ch',
    'w': 'ṭ', 'W': 'ṭh', 'q': 'ḍ', 'Q': 'ḍh', 't': 't', 'T': 'th', 'd': 'd', 'D': 'dh', 'p': 'p', 'P': 'ph',
    'S': 'ś', 'z': 'ṣ', 's': 's',
}
IAST_TO_SLP1 = {v: k for k, v in SLP1_TO_IAST.items()}
assert len(SLP1_TO_IAST) == 42 and len(IAST_TO_SLP1) == 42

def start_positions(label):
    return [i for i, (l, mk, _) in enumerate(PATH) if l == label and not mk]

def pratyahara(start, start_occ, marker, nth):
    """1.1.71: start sound .. nth marker named `marker` after it; markers excluded.
    Returns the stream (with repeats) or None if there is no such marker."""
    pos = start_positions(start)
    if start_occ > len(pos):
        return None
    i = pos[start_occ - 1]
    seen, out = 0, []
    for l, mk, _ in PATH[i:]:
        if mk:
            if l == marker:
                seen += 1
                if seen == nth:
                    return out
        else:
            out.append(l)
    return None

# Named pratyahara (SLP1, start, marker, nth, start occurrence), from the tradition's list.
# Occurrence policy (occurrence-resolution.yaml, read as EXPERIMENTAL import): aR first R,
# iR second R; first h for aw/aS/hS/iR/hl; second h only when h is not the start (Sl, vl, rl, Jl, ...)
NAMED = {
 'aR': ('a', 'R', 1, 1), 'aR2': ('a', 'R', 2, 1), 'ak': ('a', 'k', 1, 1), 'ac': ('a', 'c', 1, 1),
 'aw': ('a', 'w', 1, 1), 'am': ('a', 'm', 1, 1), 'aS': ('a', 'S', 1, 1), 'al': ('a', 'l', 1, 1),
 'ik': ('i', 'k', 1, 1), 'ic': ('i', 'c', 1, 1), 'iR': ('i', 'R', 2, 1), 'uk': ('u', 'k', 1, 1),
 'eN': ('e', 'N', 1, 1), 'ec': ('e', 'c', 1, 1), 'Ec': ('E', 'c', 1, 1), 'yY': ('y', 'Y', 1, 1),
 'yR': ('y', 'R', 1, 1), 'ym': ('y', 'm', 1, 1), 'yy': ('y', 'y', 1, 1), 'yr': ('y', 'r', 1, 1),
 'vS': ('v', 'S', 1, 1), 'vl': ('v', 'l', 1, 1), 'rl': ('r', 'l', 1, 1), 'my': ('m', 'y', 1, 1),
 'Ym': ('Y', 'm', 1, 1), 'JS': ('J', 'S', 1, 1), 'Jz': ('J', 'S', 1, 1), 'Jy': ('J', 'y', 1, 1),
 'Jr': ('J', 'r', 1, 1), 'Jl': ('J', 'l', 1, 1), 'BS': ('B', 'S', 1, 1), 'jS': ('j', 'S', 1, 1),
 'bS': ('b', 'S', 1, 1), 'Ky': ('K', 'y', 1, 1), 'Kr': ('K', 'r', 1, 1), 'Cv': ('C', 'v', 1, 1),
 'cy': ('c', 'y', 1, 1), 'cr': ('c', 'r', 1, 1), 'Sr': ('S', 'r', 1, 1), 'Sl': ('S', 'l', 1, 1),
 'hS': ('h', 'S', 1, 1), 'hl': ('h', 'l', 1, 1),
}
# 'Jz' (jhaS-ṣ typo guard): there is no marker z after J except the sutra-9 marker z, so 'Jz' means J..z
NAMED['Jz'] = ('J', 'z', 1, 1)

# Savarna classes from Kasika 1.1.9 (KASIKA-1.1.9.yaml; kAshikAvRRitti.txt 375-403):
# vargyo vargyeNa savarNaH; repho'zmaNAM savarNA na santi; ya/va/la are classes of their own;
# vowels a i u f (x) have classes; vartika: f and x are savarNa (txt 400-403).
VARGAS = [['k', 'K', 'g', 'G', 'N'], ['c', 'C', 'j', 'J', 'Y'], ['w', 'W', 'q', 'Q', 'R'],
          ['t', 'T', 'd', 'D', 'n'], ['p', 'P', 'b', 'B', 'm']]

def savarna_oracle(a, b, vartika=False):
    """True / False / None (not decided by the source read)."""
    if a == b:
        return True
    for v in VARGAS:
        if a in v and b in v:
            return True
    if {a, b} == {'f', 'x'}:
        return True if vartika else False
    if {a, b} in ({'e', 'E'}, {'o', 'O'}):
        return None   # Kasika 1.1.9 gives each sandhyakshara its own 12 forms; e~ai / o~au is not stated
    return False


# ---- savarna over length/nasal variants (Kasika 1.1.9, kAshikAvRRitti.txt 387-390) ----
# a i u f: 18 varieties each = 3 lengths (short, long, pluta) x 3 accents x 2 nasality -> ONE class each.
# x (l-vocalic): 12 varieties, NO long (txt 389) -> lengths {short, pluta}.
# e o E O: 12 varieties each, NO short -> lengths {long, pluta}. Accents are not in the code (ignored).
VARIANT_LENGTHS = {'a': (0, 1, 2), 'i': (0, 1, 2), 'u': (0, 1, 2), 'f': (0, 1, 2), 'x': (0, 2),
                   'e': (1, 2), 'o': (1, 2), 'E': (1, 2), 'O': (1, 2)}

def variants():
    """[(base, length, nasal)] for every vowel variant the source names (accents ignored)."""
    return [(b, ln, nz) for b, lns in VARIANT_LENGTHS.items() for ln in lns for nz in (0, 1)]

def savarna_variant(x, y, vartika=False):
    """Class = base sound (length and nasality never separate savarna; txt 387-390); f~x only by the vartika;
    e~E and o~O undecided (None). Different bases: False."""
    (bx, _, _), (by, _, _) = x, y
    if bx == by:
        return True
    if {bx, by} == {'f', 'x'}:
        return True if vartika else False
    if {bx, by} in ({'e', 'E'}, {'o', 'O'}):
        return None
    return False

def compare_variants(graph_dir):
    sys.path.insert(0, graph_dir)
    import upc14v2 as g
    iast = 'ṇ' in g.SOUNDS
    from_g = (lambda x: IAST_TO_SLP1[x]) if iast else (lambda x: x)
    S = {from_g(l): c for l, c in g.SOUNDS.items()}
    def code(v):
        b, ln, nz = v
        w = g.unpack(S[b])
        return g.Vertex(w.place, nz, w.aperture, ln, w.voice, w.asp).code
    vs = variants()
    out = {'n': len(vs), 'pairs': 0, 'diff': [], 'none': 0, 'status_missing': not hasattr(g, 'savarna_status')}
    for x, y in itertools.combinations(vs, 2):
        for vt in (False, True):
            exp = savarna_variant(x, y, vt)
            try:
                got = bool(g.savarna(code(x), code(y), vartika=vt))
            except Exception as e:
                got = 'ERR:' + type(e).__name__
            out['pairs'] += 1
            if exp is None:
                out['none'] += 1
            elif exp != got:
                out['diff'].append((x, y, vt, exp, got))
            if hasattr(g, 'savarna_status'):
                st = g.savarna_status(code(x), code(y), vartika=vt)
                if st != exp:
                    out['diff'].append((x, y, vt, exp, 'status=' + repr(st)))
    return out

def compare(graph_dir):
    sys.path.insert(0, graph_dir)
    import upc14v2 as g
    S = g.SOUNDS
    iast = 'ṇ' in S            # stage-2 graph keys are IAST; before that they were SLP1
    to_g = (lambda x: SLP1_TO_IAST[x]) if iast else (lambda x: x)
    from_g = (lambda x: IAST_TO_SLP1[x]) if iast else (lambda x: x)
    lab = {c: from_g(l) for c, l in g.LABELS_BY_CODE.items()}
    S = {from_g(l): c for l, c in S.items()}      # keyed by the oracle's SLP1 labels
    print('graph spelling:', 'IAST' if iast else 'SLP1')
    res = {'pratyahara_all': [], 'pratyahara_named': [], 'savarna': []}
    # --- every (start, start_occ, marker, nth) combination that exists in the path
    markers = sorted({l for l, mk, _ in PATH if mk})
    for start in SOUNDS:
        for so in range(1, len(start_positions(start)) + 1):
            for mk in markers:
                for nth in (1, 2):
                    exp = pratyahara(start, so, mk, nth)
                    try:
                        got = [lab[c] for c in g.pratyahara(S[start], to_g(mk), nth, start_occurrence=so)]
                    except Exception as e:
                        got = 'ERR:' + type(e).__name__
                    if exp is None and (got == 'ERR:GraphError' or (isinstance(got, str) and got.startswith('ERR'))):
                        continue
                    res['pratyahara_all'].append((start, so, mk, nth, exp, got, exp == got))
    for name, (st, mk, nth, so) in NAMED.items():
        exp = pratyahara(st, so, mk, nth)
        try:
            got = [lab[c] for c in g.pratyahara(S[st], to_g(mk), nth, start_occurrence=so)]
        except Exception as e:
            got = 'ERR:' + type(e).__name__
        res['pratyahara_named'].append((name, exp, got, exp == got))
    for a, b in itertools.combinations(SOUNDS, 2):
        for vt in (False, True):
            exp = savarna_oracle(a, b, vt)
            got = bool(g.savarna(S[a], S[b], vartika=vt))
            res['savarna'].append((a, b, vt, exp, got, (exp is None) or exp == got))
    return res

def main():
    if '--graph' not in sys.argv:
        print('oracle only: %d sounds, %d path nodes' % (len(SOUNDS), len(PATH)))
        for k, v in NAMED.items():
            print(k, ''.join(pratyahara(*[v[0], v[3], v[1], v[2]]) or ['?']))
        return
    gd = sys.argv[sys.argv.index('--graph') + 1]
    if '--variants' in sys.argv:
        v = compare_variants(gd)
        print('variants: %d sounds, %d pair-comparisons (x vartika on/off), undecided-by-source %d, DIFFERENT %d' % (v['n'], v['pairs'], v['none'], len(v['diff'])))
        for d in v['diff'][:40]: print('  DIFF', d)
        return
    r = compare(gd)
    pa = r['pratyahara_all']; pn = r['pratyahara_named']; sv = r['savarna']
    print('pratyahara all combos: %d, equal %d, DIFFERENT %d' % (len(pa), sum(x[6] for x in pa), sum(not x[6] for x in pa)))
    for x in pa:
        if not x[6]: print('  DIFF', x[:4], 'oracle', x[4], 'graph', x[5])
    print('pratyahara named: %d, equal %d, DIFFERENT %d' % (len(pn), sum(x[3] for x in pn), sum(not x[3] for x in pn)))
    for x in pn:
        if not x[3]: print('  DIFF', x[0], 'oracle', x[1], 'graph', x[2])
    for vt in (False, True):
        rows = [x for x in sv if x[2] == vt]
        und = [x for x in rows if x[3] is None]
        bad = [x for x in rows if x[3] is not None and x[3] != x[4]]
        print('savarna vartika=%s: pairs %d, undecided-by-source %d, DIFFERENT %d' % (vt, len(rows), len(und), len(bad)))
        for x in bad: print('  DIFF', x[0], x[1], 'oracle', x[3], 'graph', x[4])
        for x in und: print('  UNDECIDED', x[0], x[1], 'graph', x[4])

if __name__ == '__main__':
    main()
