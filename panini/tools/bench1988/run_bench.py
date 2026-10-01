#!/usr/bin/env python3
"""Drive selbench under valgrind --tool=cachegrind --cache-sim=no; write a TSV of I refs per phase.

I refs per call  = (full - setup) / N          (minus the null-strategy loop overhead, reported separately)
prepare I refs   = setup - tree
Usage: python3 run_bench.py [--n 100000] [--out result.tsv] [--bin ./selbench] [--depths 0,1,2,4,8,16]
"""
import subprocess, sys, re, os

def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

BIN = arg('--bin', '/tmp/selbench'); N = int(arg('--n', '100000')); OUT = arg('--out', 'bench1988.tsv')
DEPTHS = [int(x) for x in arg('--depths', '0,1,2,4,8,16').split(',')]

def irefs(strategy, k, wl, mode):
    cmd = ['valgrind', '--tool=cachegrind', '--cache-sim=no', '--cachegrind-out-file=/dev/null', BIN, strategy, str(k), wl, str(N), mode]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    m = re.search(r'I\s+refs:\s+([\d,]+)', r.stderr)
    if not m: raise RuntimeError(r.stderr[-300:])
    return int(m.group(1).replace(',', ''))

def main():
    rows = []
    for k in DEPTHS:
        for wl in ('random', 'repeat'):
            base = {}
            for S in 'NABCD':
                tree = irefs(S, k, wl, 'tree'); setup = irefs(S, k, wl, 'setup'); full = irefs(S, k, wl, 'full')
                base[S] = (tree, setup, full)
            loop = (base['N'][2] - base['N'][1]) / N
            for S in 'ABCD':
                tree, setup, full = base[S]
                per_call = (full - setup) / N
                rows.append((k, wl, S, tree, setup, full, setup - tree, per_call, per_call - loop))
                print(k, wl, S, 'prepare', setup - tree, 'per_call', round(per_call, 1), 'net', round(per_call - loop, 1), flush=True)
    with open(OUT, 'w') as f:
        f.write('k\tworkload\tstrategy\tI_tree\tI_setup\tI_full\tI_prepare\tI_per_call\tI_per_call_net_of_loop\tN=%d\n' % N)
        for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')

if __name__ == '__main__':
    main()
