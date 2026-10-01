# Independent harness for SENS #1988 (selector family: flat / root+suffix / cached / hybrid)

Written from issues #1987/#1988 only. Build: `gcc -O2 -o /tmp/selbench selbench.c`;
counters: `gcc -O2 -DCOUNT ...`. Measure: `python3 run_bench.py --n 100000 --out result.tsv`
(valgrind --tool=cachegrind --cache-sim=no; per-call I refs = (full - setup) / N, minus the null-strategy loop).
Parity: `./selbench A 8 random 0 verify` (exhaustive, suffix <= 8) before any timing.
Environment of the stored result: valgrind 3.27.0, gcc 16.1.0 -O2, 4 cores (WSL2); absolute I refs are not comparable to other CPUs.
Not measured: wall time, allocation bytes, working set, calloc of the 16 MB cache table (zero pages, not instructions).
