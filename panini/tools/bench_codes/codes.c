/* Code-cost benchmark: A hand table v3 (cell = sound), B linear 7x14 GF(2) map, C raw UPC-14 (2 bytes per sound).
 * Input: the .bin from gen_data.py. Usage: ./codes LANE FILE R OP PHASE
 *   LANE  N baseline | A | B (rows encode, inverse-table decode) | T (split-table encode, inverse-table decode)
 *         | S (rows encode, decode by SEARCH over the sound set) | C (table encode, 16384-entry direct decode) | Q (table encode, binary-search decode)
 *   OP enc|dec   PHASE setup|full|verify   (full = setup + R passes of OP; per symbol = (full-setup)/(R*n))
 * decode is fail-closed: a code outside the image sets `bad`, which the program prints and which verify mode asserts. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static uint32_t S, n;
static uint8_t acell[256], *stream, *dec8, *out8, inv128[128];
static uint16_t code14[256], row[7], *out16, tlo[128], thi[128], sorted_code[256], sorted_sid[256];
static uint8_t cellb[256], *inv16k;                       /* inv16k: 16384 bytes, 0xFF = not a code */
static uint8_t g_bad;
#define BARRIER() __asm__ volatile("" ::: "memory")

static void load(const char *f) {
    FILE *fp = fopen(f, "rb"); if (!fp) { perror(f); exit(2); }
    if (fread(&S, 4, 1, fp) != 1 || S > 255) exit(2);
    if (fread(acell, 1, S, fp) != S || fread(code14, 2, S, fp) != S || fread(row, 2, 7, fp) != 7 || fread(&n, 4, 1, fp) != 1) exit(2);
    stream = malloc(n); dec8 = malloc(n); out8 = malloc(n); out16 = malloc(2 * (size_t)n);
    if (fread(stream, 1, n, fp) != n) exit(2);
    fclose(fp);
}
static inline unsigned rowsmap(unsigned c) {               /* the linear map as 7 parity bits */
    unsigned r = 0;
    for (int k = 0; k < 7; k++) r |= (unsigned)__builtin_parity(c & row[k]) << k;
    return r;
}
static int cmp(const void *a, const void *b) { return (int)*(const uint16_t *)a - (int)*(const uint16_t *)b; }
static void prepare(char lane) {                           /* everything a lane builds BEFORE the measured loop */
    memset(inv128, 0xFF, 128);
    for (uint32_t s = 0; s < S; s++) cellb[s] = rowsmap(code14[s]);
    if (lane == 'A') for (uint32_t s = 0; s < S; s++) inv128[acell[s]] = s;
    else for (uint32_t s = 0; s < S; s++) inv128[cellb[s]] = s;
    for (int k = 0; k < 128; k++) {                         /* split tables of the linear map: M*(hi<<7 | lo) = thi[hi] ^ tlo[lo] */
        unsigned lo = 0, hi = 0;
        for (int j = 0; j < 7; j++) { lo |= (unsigned)__builtin_parity((unsigned)k & row[j]) << j; hi |= (unsigned)__builtin_parity(((unsigned)k << 7) & row[j]) << j; }
        tlo[k] = lo; thi[k] = hi;
    }
    inv16k = malloc(16384); memset(inv16k, 0xFF, 16384);
    for (uint32_t s = 0; s < S; s++) inv16k[code14[s]] = s;
    uint32_t idx[256]; for (uint32_t s = 0; s < S; s++) idx[s] = ((uint32_t)code14[s] << 8) | s;
    for (uint32_t i = 0; i < S; i++) for (uint32_t j = i + 1; j < S; j++) if (idx[j] < idx[i]) { uint32_t t = idx[i]; idx[i] = idx[j]; idx[j] = t; }
    for (uint32_t i = 0; i < S; i++) { sorted_code[i] = idx[i] >> 8; sorted_sid[i] = idx[i] & 255; }
    (void)cmp;
}
static void enc_pass(char lane) {
    switch (lane) {
    case 'N': for (uint32_t i = 0; i < n; i++) out8[i] = stream[i]; break;
    case 'A': for (uint32_t i = 0; i < n; i++) out8[i] = acell[stream[i]]; break;
    case 'B': case 'S': for (uint32_t i = 0; i < n; i++) out8[i] = rowsmap(code14[stream[i]]); break;
    case 'T': for (uint32_t i = 0; i < n; i++) { unsigned c = code14[stream[i]]; out8[i] = tlo[c & 127] ^ thi[c >> 7]; } break;
    case 'C': case 'Q': for (uint32_t i = 0; i < n; i++) out16[i] = code14[stream[i]]; break;
    }
}
static void dec_pass(char lane) {
    uint8_t bad = 0;
    switch (lane) {
    case 'N': for (uint32_t i = 0; i < n; i++) dec8[i] = out8[i]; break;
    case 'A': case 'B': case 'T': for (uint32_t i = 0; i < n; i++) { uint8_t v = inv128[out8[i]]; bad |= v == 0xFF; dec8[i] = v; } break;
    case 'S': for (uint32_t i = 0; i < n; i++) {             /* search the sound set for the preimage vertex: no prepared inverse table */
            unsigned want = out8[i], k = 0; while (k < S && cellb[k] != want) k++;
            bad |= k == S; dec8[i] = k; } break;
    case 'C': for (uint32_t i = 0; i < n; i++) { uint8_t v = inv16k[out16[i] & 16383]; bad |= (v == 0xFF) | (out16[i] > 16383); dec8[i] = v; } break;
    case 'Q': for (uint32_t i = 0; i < n; i++) {
            unsigned lo = 0, hi = S, want = out16[i];
            while (lo < hi) { unsigned m = (lo + hi) >> 1; if (sorted_code[m] < want) lo = m + 1; else hi = m; }
            int ok = lo < S && sorted_code[lo] == want; bad |= !ok; dec8[i] = ok ? sorted_sid[lo] : 0xFF; } break;
    }
    g_bad |= bad;
}
int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: LANE FILE R enc|dec setup|full|verify\n"); return 2; }
    char lane = argv[1][0]; unsigned R = atoi(argv[3]); int isdec = argv[4][0] == 'd'; char ph = argv[5][0];
    load(argv[2]); prepare(lane);
    enc_pass(lane);                                         /* one encode in every phase: dec needs its input; enc setup keeps the buffers live */
    if (ph == 'f') for (unsigned r = 0; r < R; r++) { if (isdec) dec_pass(lane); else enc_pass(lane); BARRIER(); }
    if (isdec) dec_pass(lane);                              /* one decode in every phase: the checksum below reads dec8 */
    unsigned long sum = 0;
    for (uint32_t i = 0; i < n; i++) sum += (lane == 'C' || lane == 'Q') ? out16[i] : out8[i];
    for (uint32_t i = 0; i < n; i++) sum += dec8[i];
    if (ph == 'v') {                                        /* parity: round trip over the text, and fail-closed on every code outside the image */
        if (lane == 'N') { puts("verify N skipped"); return 0; }
        dec_pass(lane); unsigned long wrong = 0; for (uint32_t i = 0; i < n; i++) wrong += dec8[i] != stream[i];
        unsigned reject = 0, expect = 0;
        if (lane == 'C' || lane == 'Q') {
            for (unsigned c = 0; c < 16384; c++) { out16[0] = c; g_bad = 0; uint32_t sv = n; n = 1; dec_pass(lane); n = sv; reject += g_bad; int in = 0; for (uint32_t s = 0; s < S; s++) in |= code14[s] == c; expect += !in; }
        } else {
            for (unsigned c = 0; c < 128; c++) { out8[0] = c; g_bad = 0; uint32_t sv = n; n = 1; dec_pass(lane); n = sv; reject += g_bad; int in = 0; for (uint32_t s = 0; s < S; s++) in |= (lane == 'A' ? acell[s] : cellb[s]) == c; expect += !in; }
        }
        printf("verify %c: n=%u round-trip mismatches=%lu  fail-closed rejected=%u expected=%u  %s\n", lane, n, wrong, reject, expect, (wrong == 0 && reject == expect) ? "OK" : "FAIL");
        return !(wrong == 0 && reject == expect);
    }
    printf("sum %lu bad %u\n", sum, g_bad);
    return 0;
}
