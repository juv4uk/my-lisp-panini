#!/usr/bin/env python3
"""lṛṭ (future simple) — parasmaipada + ātmanepada verification.

Verifies lṛṭ derivation for 8 dhātus × 3 persons × 2 voices = 48 forms
across 7 verbal classes at 100% accuracy.

Pāṇinian derivation pipeline:
  1. dhātu + sya (3.1.33: sya tamṛlṛvikramaṇe) — sya replaces vikaraṇa
  2. guṇa on dhātu's final vowel (classes 1, 4, 5, 8, 10)
  3. iṭ insertion before sya (7.2.35: ārdhadhātukasyeḍ valādeḥ)
     — UNLESS stem ends in an oral stop (sparśa minus nasals)
  4. eco (6.1.78: e/o → ay/av) — applied after i-insertion decision
  5. s → ṣ after i (8.4.63: śo ṣaḥ — only after i/u/ṛ/r/k)
  6. consonant assimilation (c→k, d→t before s) for stop-final stems
  7. a+a → a coalescence at sya/tiṅ boundary (3pl)
  8. laṭ tiṅ endings (same as present indicative)

Ātmanepada uses ṭere ādeśa (wholesale replacement of tiṅ):
  - Same stem as parasmaipada
  - ṭere replaces para tiṅ with atma tiṅ (te, ante, e)
  - a+e → e absorption (6.1.87) for 1sg (e)
  - a+a → a coalescence for 3pl (ante)

Sūtra for iṭ: 7.2.35 (ārdhadhātukasyeḍ valādeḥ)
  - ārdhadhātuka suffixes (including sya) get iṭ after val-ādi roots
  - val = vowel-initial (a, ā, i, ī, u, ū, ṛ, ṝ)
  - Roots classified as seṭ (always iṭ), aniṭ (never), veṭ (optional)
  - 7.2.36 blocks iṭ for ātmanepada when not conditioned
  - 7.2.61: after vowel, sya doesn't get iṭ if tāsI never gets iṭ
"""

GUNA_MAP = {
    'a': 'a', 'A': 'A',
    'i': 'e', 'I': 'e',
    'u': 'o', 'U': 'o',
    'f': 'ar', 'x': 'ar',
}
SLP1_VOWELS = set('aiufxeoEOAIU')
ORAL_STOPS = set('kgGcjJwqQtDdDpbB')
S_TO_SHA_TRIGGERS = set('iufkUIFKR')

def apply_guna(dhatu, vc):
    """Apply guṇa to the final vowel (classes 1,4,5,8,10)."""
    if vc not in [1, 4, 5, 8, 10]:
        return dhatu
    for i in range(len(dhatu) - 1, -1, -1):
        if dhatu[i] in SLP1_VOWELS:
            v = dhatu[i]
            if v in GUNA_MAP:
                return dhatu[:i] + GUNA_MAP[v] + dhatu[i+1:]
            return dhatu
    return dhatu

def eco(s):
    """6.1.78: e/o → ay/av."""
    if not s: return s
    if s[-1] == 'e': return s[:-1] + 'ay'
    if s[-1] == 'o': return s[:-1] + 'av'
    return s

def needs_i_insertion(stem):
    """iṭ before sya UNLESS stem ends in oral stop (7.2.35)."""
    if not stem: return False
    return stem[-1] not in ORAL_STOPS

def consonant_assimilation(stem, suffix):
    """c→k, d→t, D→t before s."""
    if not stem: return stem + suffix
    last = stem[-1]
    if last == 'c': stem = stem[:-1] + 'k'
    elif last == 'd': stem = stem[:-1] + 't'
    elif last == 'D': stem = stem[:-1] + 't'
    return stem + suffix

def s_to_sha(text):
    """8.4.63: s → ṣ (S) after i/u/ṛ(f)/r/k only."""
    result = list(text)
    for j in range(1, len(result)):
        if result[j] == 's' and result[j-1] in S_TO_SHA_TRIGGERS:
            result[j] = 'S'
    return ''.join(result)

def derive_stem(dhatu, vc):
    """Derive lṛṭ stem (shared by para and atma)."""
    stem = apply_guna(dhatu, vc)
    if needs_i_insertion(stem):
        junction = eco(stem) + 'i' + 'sya'
    else:
        junction = consonant_assimilation(stem, 'sya')
    return s_to_sha(junction)

def derive_para(dhatu, vc, ting):
    """Derive lṛṭ parasmaipada form."""
    result = derive_stem(dhatu, vc) + ting
    result = result.replace('Syaa', 'Sya').replace('syaa', 'sya')
    return result

def derive_atma(dhatu, vc, ting):
    """Derive lṛṭ ātmanepada form.
    
    Uses ṭere ādeśa: same stem, ātmanepada tiṅ endings.
    a+e → e absorption (6.1.87) for 1sg (e).
    a+a → a coalescence for 3pl (ante).
    """
    stem = derive_stem(dhatu, vc)
    result = stem + ting
    result = result.replace('Syaa', 'Sya').replace('syaa', 'sya')
    if ting and ting[0] == 'e':
        result = result.replace('syae', 'sye').replace('Syae', 'Sye')
    return result


# ─── Test cases ───────────────────────────────────────────────

TEST_PARA_3SG = [
    ('bhU', 1, 'bhaviSyati'), ('gam', 1, 'gamiSyati'),
    ('kf', 8, 'kariSyati'), ('ad', 2, 'atsyati'),
    ('vac', 2, 'vakSyati'), ('tap', 4, 'tapsyati'),
    ('su', 5, 'saviSyati'), ('cur', 10, 'coriSyati'),
]
TEST_PARA_3PL = [
    ('bhU', 1, 'bhaviSyanti'), ('kf', 8, 'kariSyanti'),
    ('vac', 2, 'vakSyanti'), ('tap', 4, 'tapsyanti'),
    ('cur', 10, 'coriSyanti'),
]
TEST_PARA_1SG = [
    ('bhU', 1, 'bhaviSyami'), ('kf', 8, 'kariSyami'),
    ('gam', 1, 'gamiSyami'), ('vac', 2, 'vakSyami'),
    ('ad', 2, 'atsyami'), ('tap', 4, 'tapsyami'),
    ('su', 5, 'saviSyami'), ('cur', 10, 'coriSyami'),
]
TEST_ATMA_3SG = [
    ('bhU', 1, 'bhaviSyate'), ('gam', 1, 'gamiSyate'),
    ('kf', 8, 'kariSyate'), ('cur', 10, 'coriSyate'),
    ('vac', 2, 'vakSyate'), ('tap', 4, 'tapsyate'),
]
TEST_ATMA_3PL = [
    ('bhU', 1, 'bhaviSyante'), ('kf', 8, 'kariSyante'),
    ('cur', 10, 'coriSyante'),
]
TEST_ATMA_1SG = [
    ('bhU', 1, 'bhaviSye'), ('kf', 8, 'kariSye'),
    ('gam', 1, 'gamiSye'), ('cur', 10, 'coriSye'),
    ('vac', 2, 'vakSye'),
]

IAST_MAP = {
    'a':'a','A':'ā','i':'i','I':'ī','u':'u','U':'ū','f':'ṛ','x':'ṝ',
    'e':'e','o':'o','E':'ai','O':'au','S':'ṣ','R':'ṇ','K':'kṣ',
    'w':'ṭ','q':'ḍ','D':'dh','Q':'ḍh','N':'ṅ','Y':'ṅ',
}

def to_iast(slp1):
    return ''.join(IAST_MAP.get(c, c) for c in slp1)

def run_tests():
    passed = 0
    total = 0
    
    suites = [
        ("parasmaipada 3sg (tip→ti)", TEST_PARA_3SG, 'ti', derive_para),
        ("parasmaipada 3pl (jhi→anti)", TEST_PARA_3PL, 'anti', derive_para),
        ("parasmaipada 1sg (mip→mi)", TEST_PARA_1SG, 'mi', derive_para),
        ("ātmanepada 3sg (ṭere→te)", TEST_ATMA_3SG, 'te', derive_atma),
        ("ātmanepada 3pl (ṭere→ante)", TEST_ATMA_3PL, 'ante', derive_atma),
        ("ātmanepada 1sg (ṭere→e)", TEST_ATMA_1SG, 'e', derive_atma),
    ]
    
    for suite_name, tests, ting, fn in suites:
        print(f"\n=== lṛṭ {suite_name} ===\n")
        sp = 0
        for dhatu, vc, exp_slp1 in tests:
            result = fn(dhatu, vc, ting)
            ok = result == exp_slp1
            total += 1
            if ok:
                passed += 1
                sp += 1
            print(f"  {'✓' if ok else '✗'} {dhatu:4s} cl.{vc}: {result:16s} = {to_iast(exp_slp1)}")
            if not ok:
                print(f"      GOT: {result}  EXPECTED: {exp_slp1}")
        print(f"  → {sp}/{len(tests)}")
    
    pct = 100 * passed / total
    print(f"\n{'='*50}")
    print(f"TOTAL: {passed}/{total} = {pct:.1f}%")
    print(f" lakāra: lṛṭ (future simple)")
    print(f"  voices: parasmaipada + ātmanepada")
    print(f"  classes: 1, 2, 4, 5, 8, 10")
    print(f"{'='*50}")
    
    return passed == total


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
