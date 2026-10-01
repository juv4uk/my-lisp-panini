#!/usr/bin/env python3
"""Independent check of SENS PR #1976 / issue #1975 (root + suffix selector execution).

Written ONLY from the PR/issue description (not from its code):
  root 101 = CAR, root 110 = CDR; suffix bit 0 = compose inner CAR, 1 = compose inner CDR.
  Stored outer-to-inner: word 1011 = CAR . CDR, applied to data inner-to-outer (report text).
Second view (the oracle): the classical name view, c<L1><L2>...<Lk>r, letters a=car d=cdr,
the LAST letter applied first. Both views are exercised on ALL words up to a bounded length.

Data model: nil, atoms, pairs. car/cdr of a non-pair (including nil) is a domain ERROR, as observed in
the SENS binary ("car expects a non-empty list").

Usage: python3 panini/tools/review_sens_1975_selector_words.py [--maxsuffix 12] [--sens /path/to/sens]
"""
import sys, itertools, subprocess, tempfile, os

NIL = ()
class DomainError(Exception):
    pass

def car(x):
    if isinstance(x, tuple) and len(x) == 2:
        return x[0]
    raise DomainError('car')
def cdr(x):
    if isinstance(x, tuple) and len(x) == 2:
        return x[1]
    raise DomainError('cdr')

ROOT = {'101': car, '110': cdr}
SUFFIX = {'0': car, '1': cdr}

def exec_word(word, x):
    """Root + suffix executor from the spec: ops outer-to-inner, applied inner-to-outer."""
    root, suffix = word[:3], word[3:]
    if root not in ROOT or any(b not in SUFFIX for b in suffix):
        raise ValueError('malformed word %r' % word)
    ops = [ROOT[root]] + [SUFFIX[b] for b in suffix]
    for op in reversed(ops):
        x = op(x)
    return x

def word_to_name(word):
    letters = ''.join('a' if b == '0' else 'd' for b in word[3:])
    first = 'a' if word[:3] == '101' else 'd'
    return 'c' + first + letters + 'r'

def exec_name(name, x):
    """Classical view: c L1 ... Lk r, last letter applied first."""
    assert name[0] == 'c' and name[-1] == 'r'
    for ch in reversed(name[1:-1]):
        x = car(x) if ch == 'a' else cdr(x)
    return x

def address_tree(depth, path=''):
    """Full binary tree whose leaves are labelled with their address; an asymmetric order test."""
    if depth == 0:
        return 'L' + path
    return (address_tree(depth - 1, path + 'a'), address_tree(depth - 1, path + 'd'))

def run(x, f):
    try:
        return ('ok', f(x))
    except DomainError as e:
        return ('err', str(e))

def all_words(maxsuffix):
    for root in ('101', '110'):
        for n in range(maxsuffix + 1):
            for bits in itertools.product('01', repeat=n):
                yield root + ''.join(bits)

def main():
    maxs = int(sys.argv[sys.argv.index('--maxsuffix') + 1]) if '--maxsuffix' in sys.argv else 12
    words = list(all_words(maxs))
    # trees: deep address tree (order test), shallow trees (error parity), atoms and nil
    deep = address_tree(maxs + 1)
    shallow = [address_tree(d) for d in range(0, 6)] + [NIL, 'x', (NIL, NIL), ('a', NIL), (('a', 'b'), ('c', NIL))]
    bad_order = bad_err = 0
    for w in words:
        nm = word_to_name(w)
        # order/identity on the deep tree
        a = run(deep, lambda t: exec_word(w, t)); b = run(deep, lambda t: exec_name(nm, t))
        if a != b: bad_order += 1
        # error parity on shallow trees
        for t in shallow:
            if run(t, lambda t: exec_word(w, t)) != run(t, lambda t: exec_name(nm, t)):
                bad_err += 1
    # decoding: a root-only word is its own operation; every word has exactly one (root, suffix) split
    print('words checked: %d (roots 101,110; suffix length 0..%d)' % (len(words), maxs))
    print('order/identity mismatches on the address tree: %d' % bad_order)
    print('domain-error parity mismatches on %d shallow trees: %d' % (len(shallow), bad_err))
    # negative: malformed words must be rejected, never decoded to something
    neg = ['', '1', '10', '100', '111', '000', '1012', '1a1', '0101', '10', '11']
    rejected = 0
    for w in neg:
        try:
            exec_word(w, deep)
        except ValueError:
            rejected += 1
    print('malformed words rejected: %d of %d' % (rejected, len(neg)))
    # distinctness: different words give different address results (no hidden aliasing), on the deep tree
    seen = {}
    coll = 0
    for w in words:
        r = run(deep, lambda t: exec_word(w, t))
        if r[0] == 'ok':
            if r[1] in seen and seen[r[1]] != w: coll += 1
            seen[r[1]] = w
    print('distinct words with the same result on the address tree (collisions): %d' % coll)
    if '--sens' in sys.argv:
        sens = sys.argv[sys.argv.index('--sens') + 1]
        # live parity with names the binary defines (the binary may be older than the PR's lib/core.lisp)
        data = "'((1 2 3) (4 5) 6 7 8)"
        lisp_tree = (  (1, (2, (3, NIL))), ((4, (5, NIL)), (6, (7, (8, NIL)))) )
        names = [word_to_name(w) for w in words if len(w) <= 5]
        defined, diffs = [], []
        for nm in sorted(set(names)):
            with tempfile.NamedTemporaryFile('w', suffix='.lisp', delete=False) as f:
                f.write("(%s %s)\n" % (nm, data))
            out = subprocess.run([sens, f.name], capture_output=True, text=True, timeout=30)
            os.unlink(f.name)
            txt = (out.stdout + out.stderr).strip()
            if 'unknown symbol' in txt:
                continue
            defined.append(nm)
            w = [w for w in words if word_to_name(w) == nm][0]
            exp = run(lisp_tree, lambda t: exec_word(w, t))
            diffs.append((nm, w, exp, txt.splitlines()[0][:60]))
        print('names defined in this sens binary: %d of %d (<=5 bits)' % (len(defined), len(set(names))))
        for d in diffs: print('   ', d)

if __name__ == '__main__':
    main()
