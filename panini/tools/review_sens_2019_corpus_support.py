#!/usr/bin/env python3
"""SENS #2019 (C): which bija3 seeds does each node of the typed Lisp I / Lisp 1.5 corpus (#1962: nodes.tsv, edges.tsv) reach?
Independent reachability check over the corpus GRAPH as published (not an execution of the programs): edges source->target in
the era subgraph (era or 'both'). Reports seed support per era, binding forms (lambda, label) reached, nodes reaching no seed,
and era-stability of the nodes present in both eras.
Usage: python3 review_sens_2019_corpus_support.py nodes.tsv edges.tsv
"""
import csv, sys
from collections import defaultdict

SEEDS = ['nil', 'quote', 'atom', 'eq', 'cons', 'car', 'cdr', 'cond']; BIND = ['lambda', 'label']

def main():
    N = list(csv.DictReader(open(sys.argv[1], encoding='utf-8'), delimiter='\t'))
    E = list(csv.DictReader(open(sys.argv[2], encoding='utf-8'), delimiter='\t'))
    ids = {n['id']: n for n in N}
    print('endpoints missing from the node list:', sorted(({e['source'] for e in E} | {e['target'] for e in E}) - set(ids)))
    def sub(era):
        nodes = {i for i, n in ids.items() if n['era'] in (era, 'both')}
        adj = defaultdict(set)
        for e in E:
            if e['era'] in (era, 'both') and e['source'] in nodes and e['target'] in nodes: adj[e['source']].add(e['target'])
        reach = {}
        for n in nodes:
            seen, st = set(), [n]
            while st:
                x = st.pop()
                for y in adj[x]:
                    if y not in seen: seen.add(y); st.append(y)
            reach[n] = seen
        return nodes, reach
    R = {}
    for era in ('lisp1', 'lisp15'):
        nodes, reach = sub(era); R[era] = reach
        nonseed = [n for n in nodes if n not in SEEDS + BIND]
        used = {s for n in nodes for s in reach[n] if s in SEEDS}
        print('\n%s: %d nodes (%d non-seed); seeds reached: %s; unreached: %s' % (era, len(nodes), len(nonseed), sorted(used), sorted(set(SEEDS) - used)))
        print('  nodes that reach lambda/label:', sorted(n for n in nodes if reach[n] & set(BIND)))
        print('  non-seed nodes that reach NO seed:', [n for n in nonseed if not reach[n] & set(SEEDS)])
        print('  nodes that reach only seeds (no lambda/label): %d of %d non-seed' % (sum(1 for n in nonseed if not reach[n] & set(BIND)), len(nonseed)))
    both = [n for n in ids if ids[n]['era'] == 'both']
    diff = [(n, sorted(R['lisp1'][n] & set(SEEDS)), sorted(R['lisp15'][n] & set(SEEDS))) for n in both if (R['lisp1'][n] & set(SEEDS)) != (R['lisp15'][n] & set(SEEDS))]
    print('\nnodes present in both eras with different seed support:', diff)
    for a, b in (('eval_lisp1', 'eval_lisp15'), ('apply_lisp1', 'apply_lisp15'), ('assoc_lisp1', 'assoc_lisp15')):
        if a in R['lisp1'] and b in R['lisp15']:
            print('%s %s | %s %s' % (a, sorted(R['lisp1'][a] & set(SEEDS)), b, sorted(R['lisp15'][b] & set(SEEDS))))

if __name__ == '__main__':
    main()
