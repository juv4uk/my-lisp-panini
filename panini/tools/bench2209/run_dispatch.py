#!/usr/bin/env python3
"""Cachegrind driver for dispatch.c (SENS #2209): I refs and branches per call, minus the empty lane; median of 3.
per call = (full - setup) / N;  net = lane - empty lane;  prepare = setup - tree.
Usage: python3 run_dispatch.py [--n 200000] [--bin /tmp/dispatch] [--out result.tsv]
"""
import subprocess, re, sys, statistics

def arg(n, d): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
BIN, N, OUT = arg('--bin', '/tmp/dispatch'), int(arg('--n', '200000')), arg('--out', 'dispatch2209.tsv')

def run(lane, wl, mode):
    cmd = ['valgrind', '--tool=cachegrind', '--cache-sim=no', '--branch-sim=yes', '--cachegrind-out-file=/dev/null', BIN, lane, wl, str(N), mode]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600).stderr
    i = int(re.search(r'I\s+refs:\s+([\d,]+)', r).group(1).replace(',', ''))
    b = re.search(r'Branches:\s+([\d,]+)', r); m = re.search(r'Mispredicts:\s+([\d,]+)', r)
    return i, int(b.group(1).replace(',', '')), int(m.group(1).replace(',', ''))

def med(lane, wl, mode):
    xs = [run(lane, wl, mode) for _ in range(3)]
    return tuple(statistics.median(x[k] for x in xs) for k in range(3))

def main():
    wls = ['rep:%d' % i for i in range(6)] + ['mixed']
    rows = []
    for wl in wls:
        res = {}
        for L in 'NUPD':
            tr, se, fu = med(L, wl, 'tree'), med(L, wl, 'setup'), med(L, wl, 'full')
            res[L] = (tr, se, fu)
        loop = [(res['N'][2][k] - res['N'][1][k]) / N for k in range(3)]
        for L in 'UPD':
            tr, se, fu = res[L]
            per = [(fu[k] - se[k]) / N for k in range(3)]
            net = [per[k] - loop[k] for k in range(3)]
            rows.append((wl, L, se[0] - tr[0], per[0], net[0], per[1], net[1], per[2], net[2]))
            print(wl, L, 'prepare_Ir %d' % (se[0] - tr[0]), 'I/call %.2f net %.2f | branches/call %.2f net %.2f | mispred/call %.3f net %.3f' % (per[0], net[0], per[1], net[1], per[2], net[2]), flush=True)
    with open(OUT, 'w') as f:
        f.write('workload\tlane\tI_prepare\tI_per_call\tI_net\tbranches_per_call\tbranches_net\tmispred_per_call\tmispred_net\tN=%d\n' % N)
        for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')

if __name__ == '__main__':
    main()
