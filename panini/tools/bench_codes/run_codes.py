#!/usr/bin/env python3
"""Cachegrind driver for codes.c (protocol of SENS #1987): I refs, --cache-sim=no, differential setup vs full, parity (verify) before any measurement.
per symbol = (full - setup) / (R * n);  net = lane - N (the empty copy lane);  median of 3 runs (the count is deterministic; the median is kept for the protocol).
Usage: python3 run_codes.py --data DIR [--bin /tmp/codes] [--r 20] [--valgrind PATH] [--out result.tsv]
"""
import re, statistics, struct, subprocess, sys
from pathlib import Path

def arg(n, d): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
DATA, BIN, R, OUT = Path(arg('--data', '.')), arg('--bin', '/tmp/codes'), int(arg('--r', '20')), arg('--out', 'codes.tsv')
VG = arg('--valgrind', 'valgrind')
LANES = 'NABTSCQ'
DESC = {'N': 'copy loop (baseline, subtracted)', 'A': 'A table: cell = table[sound]; dec 128-entry inverse', 'B': 'B linear M: 7 parity rows; dec 128-entry inverse (fail-closed)',
        'T': 'B linear M via two 128-entry split tables; dec as B', 'S': 'B linear M rows; dec = SEARCH over the sound set (no inverse table)',
        'C': 'C raw UPC-14, 2 bytes; dec 16384-entry direct table', 'Q': 'C raw UPC-14, 2 bytes; dec binary search over the sorted codes'}

def ir(lane, wl, op, ph):
    cmd = [VG, '--tool=cachegrind', '--cache-sim=no', '--cachegrind-out-file=/dev/null', BIN, lane, str(DATA / (wl + '.bin')), str(R), op, ph]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=1200).stderr
    return int(re.search(r'I\s+refs:\s+([\d,]+)', r).group(1).replace(',', ''))
def med(*a): return statistics.median(ir(*a) for _ in range(3))

def main():
    for wl in ('uk', 'sa'):                                          # parity first
        for l in LANES[1:]:
            r = subprocess.run([BIN, l, str(DATA / (wl + '.bin')), '1', 'enc', 'verify'], capture_output=True, text=True)
            print(r.stdout.strip()); assert r.returncode == 0, 'parity failed'
    rows = []
    for wl in ('uk', 'sa'):
        with open(DATA / (wl + '.bin'), 'rb') as f:
            S = struct.unpack('<I', f.read(4))[0]; f.seek(4 + S + 2 * S + 14); n = struct.unpack('<I', f.read(4))[0]
        for op in ('enc', 'dec'):
            res = {l: (med(l, wl, op, 'setup'), med(l, wl, op, 'full')) for l in LANES}
            loop = (res['N'][1] - res['N'][0]) / (R * n)
            for l in LANES:
                se, fu = res[l]; per = (fu - se) / (R * n)
                rows.append((wl, op, l, n, se, per, per - loop, DESC[l])); print(wl, op, l, 'setup %d' % se, 'I/sound %.2f net %.2f' % (per, per - loop), flush=True)
    with open(OUT, 'w') as f:
        f.write('workload\top\tlane\tn_sounds\tI_setup\tI_per_sound\tI_net_of_copy\tlane_description\tR=%d\n' % R)
        for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')

if __name__ == '__main__':
    main()
