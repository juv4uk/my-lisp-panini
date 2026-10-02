# Code-cost benchmark: A table v3 / B linear 7×14 / C raw UPC-14 (research, independent of SENS)

Question: does a GF(2)-linear 7-bit cell (B) win anything over the hand table (A) or the raw 14-bit code (C) for encode/decode of text?

Protocol (SENS #1987): Cachegrind I refs, `--cache-sim=no`, differential `setup` vs `full`, round-trip parity (`verify`) before any measurement,
per sound = (full − setup)/(R·n), net = lane − copy loop, median of 3 (the count is deterministic). Environment: valgrind 3.27.0, gcc 13.3.0 `-O2`, WSL2.

Run: `python3 gen_data.py --proto <shiva-sutras/prototype> --dict <dict_uk/data/dict/base.lst> --verses <sanskrit_embeddings.jsonl> --out DIR`,
`gcc -O2 -o /tmp/codes codes.c`, `python3 run_codes.py --data DIR --valgrind <path> --out result.tsv` (`--r 20`).

Workloads: 5000 dict_uk lemmas (stride over the 229962 clean distinct lemmas, 61242 sounds incl. spaces, 114191 UTF-8 bytes);
400 Devanagari verses (18542 sounds, 48551 UTF-8 bytes) after a lossy benchmark-only normalisation (ṃ→m, ḥ/avagraha/daṇḍa dropped; the graph has no such sounds).

## Result (I refs per sound, net of the copy loop; identical on both workloads to ±0.1)

| lane | encode | decode | bytes per sound | note |
|---|---|---|---|---|
| A table | 1 | 4 | 1 | cell = table[sound]; 128-entry inverse |
| B linear, 7 parity rows | 74 | 4 | 1 | decode through a prepared 128-entry inverse table (fail-closed) |
| B linear, two split tables | 7 | 4 | 1 | encode = tlo[c&127] ^ thi[c>>7] |
| B linear, decode by SEARCH | 74 | 230–266 | 1 | no prepared inverse table (linear scan of the 55–74 sounds) |
| C raw UPC-14 | 1 | 9 | 2 | decode through a 16384-entry table (16 KiB) |
| C raw UPC-14, binary search | 1 | 66 | 2 | no 16 KiB table |

Reading: B is never faster than A. Encode from a sound id is one table load for A; B needs the sound's 14-bit code first (that load is already C's cost) and then the linear map on top.
Decode through a prepared inverse table is the same 4 I refs for A and B (the map is gone at decode time). C costs 2 bytes and, to decode in 9 I refs, a 16 KiB table.
`-mpopcnt` changes nothing (gcc already emits the parity-flag sequence; results/codes-r20-mpopcnt.tsv).

## What is parity
text → sounds → code → sounds → text is identical for A, B and C (python: `gen_data.py` asserts via `LangText.render`; C: `verify` = zero mismatches over the whole stream and every code outside the image rejected: 54 of 128 cells for A/B, 16310 of 16384 for C).

## What is NOT measured / caveats
- Tokenising text → sounds and rendering sounds → text are shared and not measured (same for every lane); UTF-8 handling not measured.
- Ukrainian-only sounds and signs have no UPC-14 vertex; for B and C they carry a placeholder 14-bit preimage under the same M (B keeps their pinned cell). That is a benchmark device, not a graph claim; it affects bytes/branches not at all, but "C encodes Ukrainian" is NOT shown.
- M is one injective matrix on the 55 present Sanskrit vertices found by hill-climb (seed 1); not shown to be unique or best; B's cells for Sanskrit sounds differ from A's (hence parity is at the text level, not the cell level).
- Instruction counts only: no cache simulation (the 16 KiB table of C is the lane that would cost cache misses), no wall time, no branch mispredicts, one compiler, one host.
- The Sanskrit workload is lossily normalised; 132 of 1372 candidate lines were not encodable even then.
