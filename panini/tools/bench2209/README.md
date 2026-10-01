# Independent harness for SENS #2209 (D34-DISPATCH-1)
Written from issue #2209 only. Build `gcc -O2 -o /tmp/dispatch dispatch.c` (`-DCOUNT` for counters); parity `./dispatch U mixed 0 verify`
(also P, D; 6 selectors x 64 trees x 3 start nodes). Measure `python3 run_dispatch.py --n 200000` (valgrind cachegrind --cache-sim=no --branch-sim=yes,
median of 3, per call = (full - setup) / N minus the empty lane). Environment: valgrind 3.27.0, gcc 16.1.0 -O2, WSL2.
Absolute I refs are not comparable across compilers/hosts; compare lane order and sign of differences.
