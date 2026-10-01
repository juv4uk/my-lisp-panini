/* Independent harness for SENS #1988 / #1987: selector family executed as
 *   A flat table of rows | B interpret the suffix on every call | C decoded-path cache | D hybrid.
 * Written from the issue text only (not from benchmarks/semantic-tree-exec/ of PR #1992).
 *
 * Word = root(3 bits: 101 CAR, 110 CDR) + suffix of k bits (0 = CAR, 1 = CDR), stored outer->inner,
 * applied inner->outer: word 1011 = CAR . CDR = car(cdr(x)).
 *
 * usage: selbench <strategy A|B|C|D|N> <k> <workload random|repeat> <N calls> <mode tree|setup|full|verify>
 *   mode tree   : build the data tree only
 *   mode setup  : tree + strategy preparation
 *   mode full   : tree + preparation + N calls          (I refs per call = (full - setup) / N)
 *   mode verify : exhaustive parity of the strategy against a reference walker for suffix length <= min(k,8)
 * strategy N is the null strategy: generates the same words and sums them (loop overhead to subtract).
 * Build with -DCOUNT for the semantic-tree counters (printed to stdout); I refs are measured WITHOUT -DCOUNT.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#ifdef COUNT
static unsigned long c_root, c_bits, c_gen, c_edges, c_reg, c_resid, c_hit, c_miss, c_alloc;
#define CNT(x) (x)++
#else
#define CNT(x) ((void)0)
#endif

/* ---- data: a full binary tree of cons cells; leaves carry their own address ----------------------------- */
static uint32_t *CARV, *CDRV;
static uint32_t NCELL;
static uint32_t car1(uint32_t x) { CNT(c_edges); return CARV[x]; }
static uint32_t cdr1(uint32_t x) { CNT(c_edges); return CDRV[x]; }

/* cells 1..2^(D+1)-1 heap-numbered: children of i are 2i (car) and 2i+1 (cdr); leaves are cells >= 2^D */
static void build_tree(int depth) {
    NCELL = (1u << (depth + 1));
    CARV = malloc(NCELL * 4); CDRV = malloc(NCELL * 4);
    for (uint32_t i = 1; i < (1u << depth); i++) { CARV[i] = 2 * i; CDRV[i] = 2 * i + 1; }
    for (uint32_t i = (1u << depth); i < NCELL; i++) { CARV[i] = i; CDRV[i] = i; }  /* leaves: never descended in valid paths */
}

typedef struct { uint32_t root; uint32_t len; uint32_t bits; } Word;   /* bits: suffix, MSB first (outer first) */

/* reference: walk the letters of the classical name (last letter first) */
static uint32_t ref_exec(Word w, uint32_t x) {
    for (int i = (int)w.len - 1; i >= 0; i--) x = ((w.bits >> (w.len - 1 - i)) & 1) ? CDRV[x] : CARV[x];
    return w.root ? CDRV[x] : CARV[x];
}

/* ---- strategy B: interpret the suffix on every call ------------------------------------------------------ */
static uint32_t exec_B(Word w, uint32_t x) {
    CNT(c_root);
    for (int i = (int)w.len - 1; i >= 0; i--) {
        CNT(c_bits); CNT(c_gen);
        x = ((w.bits >> (w.len - 1 - i)) & 1) ? cdr1(x) : car1(x);
    }
    CNT(c_gen);
    return w.root ? cdr1(x) : car1(x);
}

/* ---- strategy A: flat table of rows, one per suffix string (a legacy-style "one definition per name") ---- */
typedef struct Row { uint32_t (*fn)(uint32_t); struct Row *next; } Row;  /* T[b s'] = F(b) . T[s'] ; T[eps] = identity */
static Row **TBL;                      /* TBL[(1<<len)|bits] */
static uint32_t F_car(uint32_t x) { return car1(x); }
static uint32_t F_cdr(uint32_t x) { return cdr1(x); }
static uint32_t apply_row(const Row *r, uint32_t x) {          /* nested call per letter, as nested legacy definitions */
    if (!r) return x;
    uint32_t inner = apply_row(r->next, x);
    CNT(c_gen);
    return r->fn(inner);
}
static void prepare_A(int k) {
    TBL = calloc((size_t)1 << (k + 1), sizeof(Row *));
    TBL[1] = NULL;                                      /* epsilon */
    for (int L = 1; L <= k; L++)
        for (uint32_t bits = 0; bits < (1u << L); bits++) {
            Row *r = malloc(sizeof(Row)); CNT(c_alloc);
            r->fn = (bits >> (L - 1)) & 1 ? F_cdr : F_car;                 /* first (outer) bit */
            r->next = TBL[(1u << (L - 1)) | (bits & ((1u << (L - 1)) - 1))];   /* rest */
            TBL[(1u << L) | bits] = r;
        }
}
static uint32_t exec_A(Word w, uint32_t x) {
    CNT(c_reg); CNT(c_root);
    const Row *r = TBL[(1u << w.len) | w.bits];
    x = apply_row(r, x);
    CNT(c_gen);
    return w.root ? cdr1(x) : car1(x);
}

/* ---- strategy C: cache of decoded paths (decode on miss, then walk the decoded op array) --------------- */
typedef struct { uint64_t key; uint8_t used; uint8_t len; uint8_t ops[24]; } Ent;   /* ops outer->inner incl. root */
static Ent *CACHE; static uint32_t CAP;
static uint64_t keyof(Word w) { return ((uint64_t)w.root << 40) | ((uint64_t)w.len << 32) | w.bits; }
static void prepare_C(int k) { (void)k; CAP = 1u << 19; CACHE = calloc(CAP, sizeof(Ent)); }
static uint32_t exec_C(Word w, uint32_t x) {
    uint64_t key = keyof(w);
    uint32_t h = (uint32_t)((key * 0x9E3779B97F4A7C15ull) >> 45) & (CAP - 1);
    CNT(c_reg);
    while (CACHE[h].used && CACHE[h].key != key) h = (h + 1) & (CAP - 1);
    Ent *e = &CACHE[h];
    if (!e->used) {                                      /* miss: decode once */
        CNT(c_miss); CNT(c_alloc);
        e->used = 1; e->key = key; e->len = (uint8_t)(w.len + 1);
        e->ops[0] = (uint8_t)w.root;
        for (uint32_t i = 0; i < w.len; i++) { CNT(c_bits); e->ops[i + 1] = (uint8_t)((w.bits >> (w.len - 1 - i)) & 1); }
    } else CNT(c_hit);
    CNT(c_root);
    for (int i = e->len - 1; i >= 0; i--) { CNT(c_gen); x = e->ops[i] ? cdr1(x) : car1(x); }
    return x;
}

/* ---- strategy D: hybrid, flat rows for suffix length <= 2, interpreter beyond ---------------------------- */
static void prepare_D(int k) { (void)k; prepare_A(2); }
static uint32_t exec_D(Word w, uint32_t x) {
    if (w.len <= 2) { CNT(c_reg); return exec_A(w, x); }
    CNT(c_resid);
    return exec_B(w, x);
}

/* ---- driver ---------------------------------------------------------------------------------------------- */
static uint64_t rng = 88172645463325252ull;
static uint32_t rnd(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return (uint32_t)(rng >> 11); }

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: selbench A|B|C|D|N k random|repeat N tree|setup|full|verify\n"); return 2; }
    char S = argv[1][0]; int k = atoi(argv[2]); int randomwl = argv[3][0] == 'r' && argv[3][1] == 'a';
    long N = atol(argv[4]); const char *mode = argv[5];
    build_tree(k + 1 > 16 ? k + 1 : k + 1);
    if (!strcmp(mode, "tree")) { printf("tree cells %u\n", NCELL); return 0; }
    switch (S) { case 'A': prepare_A(k); break; case 'C': prepare_C(k); break; case 'D': prepare_D(k); break; default: break; }
    uint32_t (*ex)(Word, uint32_t) = S == 'A' ? exec_A : S == 'B' ? exec_B : S == 'C' ? exec_C : S == 'D' ? exec_D : NULL;
    if (!strcmp(mode, "setup")) { printf("setup done\n"); return 0; }
    if (!strcmp(mode, "verify")) {
        long bad = 0, n = 0; int kk = k < 8 ? k : 8;
        for (uint32_t root = 0; root < 2; root++)
            for (int L = 0; L <= kk; L++)
                for (uint32_t bits = 0; bits < (1u << L); bits++) {
                    Word w = { root, (uint32_t)L, bits };
                    for (uint32_t x = 1; x < 4; x++)
                        if (ex(w, x) != ref_exec(w, x)) bad++;
                    if (ex(w, 1) != ref_exec(w, 1)) bad++;
                    n++;
                }
        printf("VERIFY words %ld mismatches %ld\n", n, bad); return bad != 0;
    }
    Word fixed = { 0, (uint32_t)k, 0 };
    if (!randomwl) { fixed.root = rnd() & 1; fixed.bits = rnd() & ((k >= 32) ? ~0u : ((1u << k) - 1u)); }
    uint64_t sum = 0;
    for (long i = 0; i < N; i++) {
        Word w = fixed;
        if (randomwl) { w.root = rnd() & 1; w.bits = rnd() & ((1u << k) - 1u); }
        sum += ex ? ex(w, 1) : (uint64_t)(w.bits + w.root);
    }
    printf("checksum %llu\n", (unsigned long long)sum);
#ifdef COUNT
    printf("COUNTERS strategy=%c k=%d wl=%s N=%ld root=%lu bits=%lu gen=%lu edges=%lu reg=%lu resid=%lu hit=%lu miss=%lu alloc=%lu\n",
           S, k, argv[3], N, c_root, c_bits, c_gen, c_edges, c_reg, c_resid, c_hit, c_miss, c_alloc);
#endif
    return 0;
}
