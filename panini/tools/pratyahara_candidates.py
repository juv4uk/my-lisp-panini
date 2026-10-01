#!/usr/bin/env python3
"""Candidate cases for pratyahara-exhaustive v0.2 (#18). Read-only w.r.t. v0.1.

Expected values are derived ONLY from (a) the 14 sutras in pratyahara-exhaustive-v0.1.yaml
and (b) the occurrence rules in shiva-sutras ksetra/astadhyayi/occurrence-resolution.yaml
(quoted in the candidates file). The shiva-sutras graph (upc14v2) is used only for the
comparison step, never to produce an expected value.

Usage: python3 panini/tools/pratyahara_candidates.py [--graph /home/agents/work/shiva-upc7/prototype]
"""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, '..', 'tests', 'pratyahara-exhaustive-v0.1.yaml')

def sutras():
    txt = open(FIXTURE, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'\{ ordinal: (\d+), sounds: \[(.*?)\], marker: (\S+) \}', txt):
        out.append(([x.strip() for x in m.group(2).split(',')], m.group(3)))
    assert len(out) == 14
    return out

def path():
    nodes = []  # (label, is_marker, sutra_ordinal)
    for i, (snd, mk) in enumerate(sutras(), 1):
        nodes += [(s, False, i) for s in snd] + [(mk, True, i)]
    return nodes

# (id, notation, start_sound, start_sutra, end_marker, marker_occurrence, provenance)
CASES = [
    ('in-vowels-semivowels-2nd-N', 'iR', 'i', 1, 'R', 2, 'occurrence-resolution: rule_iR = always the second R (sutra 6)'),
    ('aN-first', 'aR(1)', 'a', 1, 'R', 1, 'occurrence-resolution: rule_aR = up to the first R (sutra 1)'),
    ('aN-second', 'aR(2)', 'a', 1, 'R', 2, 'occurrence-resolution: exception stated in yaml for 8.3.32; see notes in candidates file'),
    ('has-first-h', 'haS', 'h', 5, 'S', 1, 'occurrence-resolution: usage_first_h lists a w, aS, haS, iR'),
    ('jhas', 'JaS', 'J', 8, 'S', 1, 'no ambiguity: single J, first marker S after it'),
    ('as', 'aS', 'a', 1, 'S', 1, 'occurrence-resolution: usage_first_h lists aS'),
    ('sal-second-h', 'Sal', 'S', 13, 'l', 1, 'occurrence-resolution: usage_second_h lists Sal, val, ral, Jal'),
    ('jhal-second-h', 'Jal', 'J', 8, 'l', 1, 'occurrence-resolution: usage_second_h lists Jal'),
    ('val-second-h', 'val', 'v', 5, 'l', 1, 'occurrence-resolution: usage_second_h lists val'),
    ('ral-second-h', 'ral', 'r', 5, 'l', 1, 'occurrence-resolution: usage_second_h lists ral'),
]

def expected(start, start_sutra, marker, occ):
    nodes = path()
    i = next(k for k, n in enumerate(nodes) if n[0] == start and not n[1] and n[2] == start_sutra)
    seen = 0
    stream = []
    for label, is_marker, _ in nodes[i:]:
        if is_marker:
            if label == marker:
                seen += 1
                if seen == occ:
                    return stream
        else:
            stream.append(label)
    raise ValueError('no marker')

def graph_stream(gdir, start, marker, occ):
    sys.path.insert(0, gdir)
    sys.path.insert(0, HERE)
    import upc14v2 as g
    from second_impl_pratyahara_savarna import SLP1_TO_IAST, IAST_TO_SLP1
    iast = 'ṇ' in g.SOUNDS   # stage-2 graph keys are IAST; earlier they were SLP1
    to_g = (lambda x: SLP1_TO_IAST[x]) if iast else (lambda x: x)
    from_g = (lambda x: IAST_TO_SLP1[x]) if iast else (lambda x: x)
    return [from_g(g.LABELS_BY_CODE[c]) for c in g.pratyahara(g.SOUNDS[to_g(start)], to_g(marker), occ)]

def main():
    gdir = None
    if '--graph' in sys.argv:
        gdir = sys.argv[sys.argv.index('--graph') + 1]
    for cid, nota, st, sts, mk, occ, prov in CASES:
        exp = expected(st, sts, mk, occ)
        line = '%-26s %-6s %s' % (cid, nota, ' '.join(exp))
        if gdir:
            gr = graph_stream(gdir, st, mk, occ)
            line += '\n    graph: ' + ('SAME' if gr == exp else 'DIFF ' + ' '.join(gr))
        print(line)

if __name__ == '__main__':
    main()
