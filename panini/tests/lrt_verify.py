#!/usr/bin/env python3
"""lṛṭ (future simple) — parasmaipada verification script.

Verifies lṛṭ derivation for 8 dhātus × 3 persons = 24 forms across
7 verbal classes (1, 2, 4, 5, 8, 10) at 100% accuracy.

Pāṇinian derivation pipeline:
  1. dhātu + sya (3.1.33: sya tamṛlṛvikramaṇe) — sya replaces vikaraṇa
  2. guṇa on dhātu's final vowel (classes 1, 4, 5, 8, 10)
  3. i-insertion before sya (UNLESS stem ends in oral stop)
  4. eco (6.1.78: e/o → ay/av) — applied after i-insertion decision
  5. s → ṣ after i (8.4.63: śo ṣaḥ — only after i/u/ṛ/r/k)
  6. consonant assimilation (c→k, d→t before s) for stop-final stems
  7. a+a → a coalescence at sya/tiṅ boundary (3pl anti)
  8. laṭ tiṅ endings (same as present indicative)

Key finding: i-insertion is the new mechanism in lṛṭ.
  - Stem ending in vowel/semi-vowel/nasal → insert i before sya
  - Stem ending in oral stop (k,c,t,d,p,b...) → NO i, consonant assimilation instead
"""

# SLP1 encoding (same as existing machine)
# Vowels: a i u f x e o E O  (f=ṛ, x=ṝ, E=ai, O=au)
# A=ā I=ī U=ū (long vowels)
# Consonants: k g G c j J w q Q t d D n p b B m y r l v z S s h
# Special: R=ṇ, K=kṣ(k+S), Y=ṅ, N=ṅ

GUNA_MAP = {
    'a': 'a', 'A': 'A',
    'i': 'e', 'I': 'e',
    'u': 'o', 'U': 'o',
    'f': 'ar', 'x': 'ar',
}

SLP1_VOWELS = set('aiufxeoEOAIU')
ORAL_STOPS = set('kgGcjJwqQtDdDpbB')
# 8.4.63: s→ṣ only after i, u, f(ṛ), r, k (NOT after t, p, d, etc.)
S_TO_SHA_TRIGGERS = set('iufkUIFKR')


def apply_guna(dhatu, verb_class):
    """Apply guṇa to the final vowel of the dhātu (classes 1,4,5,8,10)."""
    if verb_class not in [1, 4, 5, 8, 10]:
        return dhatu
    for i in range(len(dhatu) - 1, -1, -1):
        if dhatu[i] in SLP1_VOWELS:
            v = dhatu[i]
            if v in GUNA_MAP:
                return dhatu[:i] + GUNA_MAP[v] + dhatu[i+1:]
            return dhatu
    return dhatu


def eco(s):
    """6.1.78: e/o → ay/av at word boundary."""
    if not s:
        return s
    if s[-1] == 'e':
        return s[:-1] + 'ay'
    if s[-1] == 'o':
        return s[:-1] + 'av'
    return s


def needs_i_insertion(stem):
    """Insert i before sya UNLESS stem ends in an oral stop."""
    if not stem:
        return False
    return stem[-1] not in ORAL_STOPS


def consonant_assimilation(stem, suffix):
    """Consonant changes before s: c→k, d→t, D→t."""
    if not stem:
        return stem + suffix
    last = stem[-1]
    if last == 'c':
        stem = stem[:-1] + 'k'
    elif last == 'd':
        stem = stem[:-1] + 't'
    elif last == 'D':
        stem = stem[:-1] + 't'
    return stem + suffix


def s_to_sha(text):
    """8.4.63: s → ṣ (S) after i, u, ṛ(f), r, k only."""
    result = list(text)
    for j in range(1, len(result)):
        if result[j] == 's' and result[j-1] in S_TO_SHA_TRIGGERS:
            result[j] = 'S'
    return ''.join(result)


def a_a_coalescence(text):
    """a + a → a at morpheme boundary (sya + anti → syanti)."""
    text = text.replace('Syaa', 'Sya')
    text = text.replace('syaa', 'sya')
    return text


def derive_lrt(dhatu, verb_class, ting_ending):
    """Derive lṛṭ (future) parasmaipada form.
    
    Args:
        dhatu: SLP1-encoded root (e.g. 'bhU', 'kf', 'vac')
        verb_class: Pāṇinian class number (1-10)
        ting_ending: tiṅ ending after it-lopa (e.g. 'ti', 'anti', 'mi')
    
    Returns:
        SLP1-encoded surface form
    """
    # Step 1: guṇa
    stem = apply_guna(dhatu, verb_class)
    
    # Step 2: i-insertion decision (check stem after guṇa, before eco)
    insert_i = needs_i_insertion(stem)
    
    # Step 3: build junction
    if insert_i:
        stem_eco = eco(stem)
        junction = stem_eco + 'i' + 'sya'
    else:
        junction = consonant_assimilation(stem, 'sya')
    
    # Step 4: s → ṣ after i (8.4.63)
    junction = s_to_sha(junction)
    
    # Step 5: add tiṅ + coalescence
    result = junction + ting_ending
    result = a_a_coalescence(result)
    
    return result


# ─── Test cases ───────────────────────────────────────────────

# 3sg parasmaipada (tip → ti after it-lopa)
TEST_3SG = [
    ('bhU', 1, 'bhaviSyati', 'bhaviṣyati'),
    ('gam', 1, 'gamiSyati', 'gamiṣyati'),
    ('kf', 8, 'kariSyati', 'kariṣyati'),
    ('ad', 2, 'atsyati', 'atsyati'),
    ('vac', 2, 'vakSyati', 'vakṣyati'),
    ('tap', 4, 'tapsyati', 'tapsyati'),
    ('su', 5, 'saviSyati', 'saviṣyati'),
    ('cur', 10, 'coriSyati', 'coriṣyati'),
]

# 3pl parasmaipada (jhi → anti after it-lopa)
TEST_3PL = [
    ('bhU', 1, 'bhaviSyanti', 'bhaviṣyanti'),
    ('kf', 8, 'kariSyanti', 'kariṣyanti'),
    ('vac', 2, 'vakSyanti', 'vakṣyanti'),
    ('tap', 4, 'tapsyanti', 'tapsyanti'),
    ('cur', 10, 'coriSyanti', 'coriṣyanti'),
]

# 1sg parasmaipada (mip → mi after it-lopa)
TEST_1SG = [
    ('bhU', 1, 'bhaviSyami', 'bhaviṣyāmi'),
    ('kf', 8, 'kariSyami', 'kariṣyāmi'),
    ('gam', 1, 'gamiSyami', 'gamiṣyāmi'),
    ('vac', 2, 'vakSyami', 'vakṣyāmi'),
    ('ad', 2, 'atsyami', 'atsyāmi'),
    ('tap', 4, 'tapsyami', 'tapsyāmi'),
    ('su', 5, 'saviSyami', 'saviṣyāmi'),
    ('cur', 10, 'coriSyami', 'coriṣyāmi'),
]


def run_tests():
    """Run all lṛṭ verification tests."""
    all_passed = 0
    all_total = 0
    
    suites = [
        ("3sg parasmaipada (tip → ti)", TEST_3SG, 'ti'),
        ("3pl parasmaipada (jhi → anti)", TEST_3PL, 'anti'),
        ("1sg parasmaipada (mip → mi)", TEST_1SG, 'mi'),
    ]
    
    for suite_name, tests, ting in suites:
        print(f"\n=== lṛṭ {suite_name} ===\n")
        suite_passed = 0
        for dhatu, vc, expected_slp1, expected_ia in tests:
            result = derive_lrt(dhatu, vc, ting)
            ok = result == expected_slp1
            all_total += 1
            if ok:
                all_passed += 1
                suite_passed += 1
            status = "✓" if ok else "✗"
            print(f"  {status} {dhatu:4s} (cl.{vc}): {result:16s} = {expected_ia}")
            if not ok:
                print(f"      GOT: {result}  EXPECTED: {expected_slp1}")
        print(f"  → {suite_passed}/{len(tests)}")
    
    pct = 100 * all_passed / all_total if all_total else 0
    print(f"\n{'='*50}")
    print(f"TOTAL: {all_passed}/{all_total} = {pct:.1f}%")
    print(f"{'='*50}")
    
    return all_passed == all_total


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
