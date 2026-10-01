/* Independent harness for SENS #2209 (D34-DISPATCH-1), written from the issue text only
 * (NOT from benchmarks/d34-dispatch/ of PR #2219).
 *
 * Six selectors on ONE value tree: 101 CAR, 110 CDR (D3), 1010 CAAR, 1011 CADR, 1100 CDAR, 1101 CDDR (D4).
 * Lanes:
 *   U  u8-flat-ready     identity = an 8-bit slot; ONE flat table row lookup -> recipe (ops outer->inner), then execute
 *   P  d3d4-prefix-ready identity = exact word (3 or 4 bits); root 101/110 + one suffix bit (0 = inner CAR, 1 = inner CDR,
 *                        the inner op is applied FIRST); NO descendant row, NO table lookup
 *   D  direct-specialized compile-time chain of car/cdr per selector (lower bound; a switch on the selector index)
 *   N  empty lane        same loop, same index/tree generation, sums the inputs only (subtract it)
 * usage: dispatch <lane U|P|D|N> <workload rep:<idx0..5>|mixed> <N calls> <mode tree|setup|full|verify>
 * -DCOUNT prints semantic counters (table lookups, bits consumed, generator applications) to stdout.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#ifdef COUNT
static unsigned long c_lookup, c_bits, c_gen;
#define CNT(x) (x)++
#else
#define CNT(x) ((void)0)
#endif

#define NTREE 64
#define TNODES 15                       /* full binary tree of depth 3 per root: nodes 1..15, heap numbered, leaves 8..15 */
static uint32_t CARV[NTREE * 16 + 16], CDRV[NTREE * 16 + 16];
static inline uint32_t car1(uint32_t x) { return CARV[x]; }
static inline uint32_t cdr1(uint32_t x) { return CDRV[x]; }
static void build_trees(void) {
    for (uint32_t t = 0; t < NTREE; t++) {
        uint32_t b = t * 16;
        for (uint32_t i = 1; i <= 7; i++) { CARV[b + i] = b + 2 * i; CDRV[b + i] = b + 2 * i + 1; }
        for (uint32_t i = 8; i <= 15; i++) { CARV[b + i] = b + i; CDRV[b + i] = b + i; }
    }
}
static uint32_t root_of(uint32_t t) { return t * 16 + 1; }

/* the six selectors: word length, word bits, op list outer->inner (0 = CAR, 1 = CDR) */
static const uint8_t WLEN[6]  = {3, 3, 4, 4, 4, 4};
static const uint8_t WBITS[6] = {5, 6, 10, 11, 12, 13};        /* 101 110 1010 1011 1100 1101 */
static const uint8_t SLOT[6]  = {0x05, 0x06, 0x0A, 0x0B, 0x0C, 0x0D};   /* the 8-bit slot of each selector */

/* reference: classical name semantics, last letter applied first */
static uint32_t ref_exec(int idx, uint32_t x) {
    uint32_t w = WBITS[idx]; int len = WLEN[idx];
    int root = (w >> (len - 3)) & 7;                       /* 101 -> CAR, 110 -> CDR */
    int rootcdr = (root == 6);
    for (int i = len - 4; i >= 0; i--) x = ((w >> i) & 1) ? CDRV[x] : CARV[x];     /* suffix bits, innermost = last */
    return rootcdr ? CDRV[x] : CARV[x];
}

/* ---- lane U: one flat row lookup -> recipe -> execute ----------------------------------------------------- */
typedef struct { uint8_t n; uint8_t ops[2]; } Recipe;           /* ops outer->inner */
static Recipe TBL[256];
static void prepare_U(void) {
    memset(TBL, 0, sizeof TBL);
    for (int i = 0; i < 6; i++) {
        uint32_t w = WBITS[i]; int len = WLEN[i];
        Recipe r; r.n = (uint8_t)(len - 2);
        r.ops[0] = ((w >> (len - 3)) & 7) == 6;          /* root */
        r.ops[1] = len == 4 ? (w & 1) : 0;
        TBL[SLOT[i]] = r;
    }
}
static uint32_t exec_U(uint8_t slot, uint32_t x) {
    CNT(c_lookup);
    const Recipe *r = &TBL[slot];
    for (int i = r->n - 1; i >= 0; i--) { CNT(c_gen); x = r->ops[i] ? cdr1(x) : car1(x); }
    return x;
}

/* ---- lane P: exact word -> recipe from the prefix law (no descendant row) -------------------------------- */
static uint32_t exec_P(uint16_t word, uint32_t x) {          /* word = (len << 8) | bits */
    uint32_t len = word >> 8, bits = word & 0xFF;
    CNT(c_bits); CNT(c_bits); CNT(c_bits);                   /* 3 root bits */
    uint32_t rootcdr = ((bits >> (len - 3)) & 7) == 6;       /* root 101 CAR / 110 CDR */
    if (len == 4) { CNT(c_bits); CNT(c_gen); x = (bits & 1) ? cdr1(x) : car1(x); }   /* suffix bit: inner op first */
    CNT(c_gen);
    return rootcdr ? cdr1(x) : car1(x);
}

/* ---- lane D: direct specialised chains (switch on the selector index = compile-time known call site) ------- */
static uint32_t exec_D(int idx, uint32_t x) {
    switch (idx) {
        case 0: return car1(x);
        case 1: return cdr1(x);
        case 2: return car1(car1(x));
        case 3: return car1(cdr1(x));
        case 4: return cdr1(car1(x));
        default: return cdr1(cdr1(x));
    }
}

static uint64_t rng = 88172645463325252ull;
static uint32_t rnd(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return (uint32_t)(rng >> 11); }

static uint16_t WORD16[6];
static uint32_t run_lane(char lane, int idx, uint32_t x) {
    switch (lane) {
        case 'U': return exec_U(SLOT[idx], x);
        case 'P': return exec_P(WORD16[idx], x);
        case 'D': return exec_D(idx, x);
        default:  return (uint32_t)idx + x;
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: dispatch U|P|D|N rep:<0..5>|mixed N tree|setup|full|verify\n"); return 2; }
    char lane = argv[1][0]; const char *wl = argv[2]; long N = atol(argv[3]); const char *mode = argv[4];
    build_trees();
    for (int i = 0; i < 6; i++) WORD16[i] = (uint16_t)((WLEN[i] << 8) | WBITS[i]);
    if (!strcmp(mode, "tree")) { printf("trees ready\n"); return 0; }
    if (lane == 'U') prepare_U();
    if (!strcmp(mode, "setup")) { printf("setup done\n"); return 0; }
    if (!strcmp(mode, "verify")) {
        long bad = 0, n = 0;
        for (int i = 0; i < 6; i++) for (uint32_t t = 0; t < NTREE; t++) for (uint32_t k = 1; k <= 3; k++) {
            uint32_t x = t * 16 + k;                          /* a start node deep enough for 2 ops: nodes 1..3 */
            if (run_lane(lane, i, x) != ref_exec(i, x)) bad++;
            n++;
        }
        printf("VERIFY lane %c calls %ld mismatches %ld\n", lane, n, bad); return bad != 0;
    }
    int mixed = !strcmp(wl, "mixed"); int fixed_idx = mixed ? 0 : atoi(wl + 4);
    uint64_t sum = 0;
    for (long i = 0; i < N; i++) {
        uint32_t r = rnd();
        int idx = mixed ? (int)(r % 6) : fixed_idx;
        uint32_t t = mixed ? (r >> 4) % NTREE : 3;
        uint32_t x = t * 16 + 1;
        sum += run_lane(lane, idx, x);
    }
    printf("checksum %llu\n", (unsigned long long)sum);
#ifdef COUNT
    printf("COUNTERS lane=%c wl=%s N=%ld lookup=%.3f bits=%.3f gen=%.3f\n", lane, wl, N, (double)c_lookup / N, (double)c_bits / N, (double)c_gen / N);
#endif
    return 0;
}
