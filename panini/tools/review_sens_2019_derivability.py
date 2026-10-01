#!/usr/bin/env python3
"""Bounded executable derivability of the bija3 seeds (SENS #2019): independent implementation, finite evidence only.

EXACT ASSUMPTIONS (model M):
 1. Values: atoms NIL, T, A, B (variant M2: only NIL, T), pairs (x . y), and ERR (partial operations return ERR).
 2. Seeds (8): '()' = the constant NIL; QUOTE = may introduce any atom constant among T, A, B;
    ATOM(x)=T if x is an atom else NIL; EQ(x,y)=T/NIL on two ATOMS, ERR otherwise (McCarthy 1960: eq is defined on atoms);
    CONS(x,y)=(x . y); CAR/CDR of a non-pair (incl. NIL) = ERR;
    COND is the ternary ITE(p,a,b): p == NIL -> b, any other p -> a.
 3. STRICT branch: ITE (and every operation) returns ERR if any argument is ERR.  LAZY branch: ITE returns the selected
    branch even if the other one is ERR (the only observable effect of laziness in a pure value model without
    non-termination); every other operation stays strict.
 4. Derivable(t, B): there is a term over variables x,y,z (arity of t) and the constants/operations of basis B (t not in B)
    whose value vector equals t's on a finite TEST SET of inputs, within term size N.  Test inputs: unary 8 values, binary
    8x8, ternary p in {NIL,T} x a,b in {A,B,(A.B),NIL}.
    This is BOUNDED evidence (finite inputs, bounded size, no lambda): a 'found' is a witness on the test set (to be re-checked),
    a 'not found' means 'not within size N / term cap', NOT underivable.
Usage: python3 review_sens_2019_derivability.py [--size 7] [--cap 60000] [--atoms 4|2]
"""
import sys, itertools

ERR = 'ERR'
def isatom(x): return isinstance(x, str) and x != ERR
def car(x): return x[0] if isinstance(x, tuple) else ERR
def cdr(x): return x[1] if isinstance(x, tuple) else ERR
def cons(x, y): return ERR if ERR in (x, y) else (x, y)
def atom(x): return ERR if x == ERR else ('T' if isatom(x) else 'NIL')
def eq(x, y): return ('T' if x == y else 'NIL') if isatom(x) and isatom(y) else ERR
def ite_strict(p, a, b): return ERR if ERR in (p, a, b) else (b if p == 'NIL' else a)
def ite_lazy(p, a, b): return ERR if p == ERR else (b if p == 'NIL' else a)

SEEDS = ['()', 'QUOTE', 'ATOM', 'EQ', 'CONS', 'CAR', 'CDR', 'COND']
ARITY = {'ATOM': 1, 'CAR': 1, 'CDR': 1, 'EQ': 2, 'CONS': 2, 'COND': 3}
U = ['NIL', 'T', 'A', 'B', ('A', 'B'), ('A', 'NIL'), (('A', 'B'), 'NIL'), ('NIL', 'NIL')]

def points(k):
    if k == 1: return [(u,) for u in U]
    if k == 2: return list(itertools.product(U, repeat=2))
    return [(p, a, b) for p in ('NIL', 'T') for a in ('A', 'B', ('A', 'B'), 'NIL') for b in ('A', 'B', ('A', 'B'), 'NIL')]

def target_fn(name, lazy):
    return {'ATOM': atom, 'CAR': car, 'CDR': cdr, 'EQ': eq, 'CONS': cons, 'COND': ite_lazy if lazy else ite_strict}[name]

def derivable(target, basis, lazy, size, cap, atoms):
    """target is a function seed (arity 1..3) not in basis; returns (expr, nterms) or (None, nterms)."""
    k = ARITY[target]; pts = points(k)
    goal = tuple(target_fn(target, lazy)(*p) for p in pts)
    ops = []
    if 'ATOM' in basis: ops.append(('ATOM', 1, atom))
    if 'CAR' in basis: ops.append(('CAR', 1, car))
    if 'CDR' in basis: ops.append(('CDR', 1, cdr))
    if 'EQ' in basis: ops.append(('EQ', 2, eq))
    if 'CONS' in basis: ops.append(('CONS', 2, cons))
    if 'COND' in basis: ops.append(('COND', 3, ite_lazy if lazy else ite_strict))
    seen = {}; by_size = {}
    def add(vec, expr, s):
        if vec in seen: return
        seen[vec] = expr; by_size.setdefault(s, []).append((vec, expr))
    for i, v in enumerate('xyz'[:k]): add(tuple(p[i] for p in pts), v, 1)
    if '()' in basis: add(tuple('NIL' for _ in pts), 'NIL', 1)
    if 'QUOTE' in basis:
        for c in (['T', 'A', 'B'] if atoms == 4 else ['T']): add(tuple(c for _ in pts), "'" + c, 1)
    if goal in seen: return seen[goal], len(seen)
    for s in range(2, size + 1):
        for name, ar, f in ops:
            if ar == 1:
                for vec, e in by_size.get(s - 1, []):
                    add(tuple(f(a) for a in vec), '%s(%s)' % (name, e), s)
            elif ar == 2:
                for s1 in range(1, s - 1):
                    s2 = s - 1 - s1
                    for v1, e1 in by_size.get(s1, []):
                        for v2, e2 in by_size.get(s2, []):
                            add(tuple(f(a, b) for a, b in zip(v1, v2)), '%s(%s,%s)' % (name, e1, e2), s)
                            if len(seen) > cap: return None, len(seen)
            else:
                for s1 in range(1, s - 2):
                    for s2 in range(1, s - 1 - s1):
                        s3 = s - 1 - s1 - s2
                        for v1, e1 in by_size.get(s1, []):
                            for v2, e2 in by_size.get(s2, []):
                                for v3, e3 in by_size.get(s3, []):
                                    add(tuple(f(a, b, c) for a, b, c in zip(v1, v2, v3)), '%s(%s,%s,%s)' % (name, e1, e2, e3), s)
                                    if len(seen) > cap: return None, len(seen)
            if goal in seen: return seen[goal], len(seen)
            if len(seen) > cap: return None, len(seen)
    return (seen.get(goal), len(seen))

def main():
    size = int(sys.argv[sys.argv.index('--size') + 1]) if '--size' in sys.argv else 7
    cap = int(sys.argv[sys.argv.index('--cap') + 1]) if '--cap' in sys.argv else 60000
    atoms = int(sys.argv[sys.argv.index('--atoms') + 1]) if '--atoms' in sys.argv else 4
    print('model: atoms=%d, size<=%d, term cap %d' % (atoms, size, cap))
    funcs = list(ARITY)
    for lazy in (False, True):
        print('\n=== %s branch ===' % ('LAZY COND' if lazy else 'STRICT COND'))
        print('each function seed from ALL the other seeds:')
        for t in funcs:
            B = set(SEEDS) - {t}
            e, n = derivable(t, B, lazy, size, cap, atoms)
            print('  %-5s %s  (%d terms)' % (t, ('DERIVED  ' + e) if e else 'not found', n))
        # generating subsets: B generates every seed if each seed outside B is derivable from B
        cache = {}
        def der(t, B):
            key = (t, frozenset(B))
            if key not in cache:
                if t in ('()', 'QUOTE'):
                    # constants: '()' derivable iff a closed term has value NIL: needs QUOTE (quote NIL excluded: QUOTE introduces T,A,B only)
                    # or a constant source; we test closed terms via derivable on a 0-ary pseudo-target below
                    cache[key] = const_derivable(t, B, lazy, atoms, size, cap)
                else:
                    cache[key] = derivable(t, B, lazy, size, cap, atoms)[0] is not None
            return cache[key]
        gen = []
        for r in range(1, 9):
            for B in itertools.combinations(SEEDS, r):
                if all(t in B or der(t, B) for t in SEEDS): gen.append(set(B))
        minimal = [g for g in gen if not any(h < g for h in gen)]
        print('generating subsets (all 8 seeds obtained): %d; MINIMAL ones (%d): %s' % (len(gen), len(minimal), [sorted(m) for m in minimal]))

def const_derivable(t, B, lazy, atoms, size, cap):
    """'()' and QUOTE are closed constants: derivable from B iff a closed term over B yields NIL (resp. every atom in T,A,B)."""
    vals = set()
    if '()' in B: vals.add('NIL')
    if 'QUOTE' in B: vals |= ({'T', 'A', 'B'} if atoms == 4 else {'T'})
    changed = True; rounds = 0
    ops1 = {'ATOM': atom, 'CAR': car, 'CDR': cdr}
    while changed and rounds < size:
        changed = False; rounds += 1
        new = set(vals)
        for n, f in ops1.items():
            if n in B:
                for v in vals:
                    r = f(v)
                    if r != ERR and r not in new: new.add(r)
        if 'CONS' in B:
            for a in list(vals)[:30]:
                for b in list(vals)[:30]:
                    r = cons(a, b)
                    if r not in new and len(new) < 200: new.add(r)
        if 'EQ' in B:
            for a in vals:
                for b in vals:
                    r = eq(a, b)
                    if r != ERR: new.add(r)
        if 'COND' in B:
            for p in list(vals)[:20]:
                for a in list(vals)[:20]:
                    for b in list(vals)[:20]:
                        r = (ite_lazy if lazy else ite_strict)(p, a, b)
                        if r != ERR: new.add(r)
        if new != vals: vals = new; changed = True
    return ('NIL' in vals) if t == '()' else {'T', 'A', 'B'}.issuperset(set()) and (({'T', 'A', 'B'} if atoms == 4 else {'T'}) <= {v for v in vals if isatom(v)})

if __name__ == '__main__':
    main()
