#!/usr/bin/env python3
"""liṅ (optative) verification — self-contained script."""

vowels = set('aiufxoEORAeIU')
ik_vowels = set('iIuUfFxX')

vikarana = {
    1: (['z','a','p'], ['z','p']),
    2: ([], []),
    4: (['z','y','a'], ['z']),
    5: (['z','n','u'], ['z']),
    6: (['z','a'], ['z']),
    7: (['z','n','A'], ['z','A']),
    8: (['u'], []),
    9: (['z','n','A'], ['z','A']),
    10:(['R','i','c'], ['R','c']),
}

# Optative parasmaipada endings (after s-lopa + ī→e by guṇa)
# These are for a-final aṅga (classes 1, 4, 6, 10)
# sīt → īt → et, sīyātam → eyātam, sīyus → eyus, etc.
lin_ting_para = {
    'tip': ['e','t'],          # 3sg: et
    'tas': ['e','y','A','t','a','m'],  # 3du: eyātam
    'jhi': ['e','y','u','s'],  # 3pl: eyus
    'sip': ['e','s'],          # 2sg: es (→eḥ by visarga)
    'thas': ['e','s','t','A','m'],  # 2du: estām
    'tha': ['e','s','t','a'],  # 2pl: esta
    'mip': ['e','y','a','m'],  # 1sg: eyam
    'vas': ['e','v','a'],      # 1du: eva
    'mas': ['e','m','a'],      # 1pl: ema
}

# For Śnu/Śu classes (5, 8): aṅga ends in u, NOT a
# The optative uses DIFFERENT endings: yāt, yātām, yus, etc.
# (The "sī" marker doesn't get guṇa→e because the eco interaction is different)
# Actually: u + sī → (s lopa) u + ī → guṇa on ī → u + e → no eco (u is not e/o)
# But actual form is sunuyāt, not sunuet. So the ending must be yāt not et.
# This means: for non-a-final aṅga, the optative marker stays as "ī" → "y" (yaṇ)?
# ī → y by yaṇ (1.1.48: ūkalyaṇ?) No, yaṇ is for IK + vowel → yaṇ.
# Actually: u + ī → u + y (ī→y by yaṇ? No, yaṇ replaces the vowel, not adds)
# Let me just use pre-computed endings for class 5/8
lin_ting_snu = {
    'tip': ['y','A','t'],      # 3sg: yāt
    'tas': ['y','A','t','A','m'],  # 3du: yātām
    'jhi': ['y','u','s'],      # 3pl: yus
    'sip': ['y','A','s'],      # 2sg: yās (→yāḥ)
    'thas': ['y','A','s','t','A','m'],  # 2du: yāstām
    'tha': ['y','A','s','t','a'],  # 2pl: yāsta
    'mip': ['y','A','m'],      # 1sg: yām
    'vas': ['y','A','v','a'],  # 1du: yāva
    'mas': ['y','A','m','a','h','i'],  # 1pl: yāmahi
}

def remove_it(sounds, markers):
    return [s for s in sounds if s not in markers]

def is_vowel(s):
    return s in vowels

def is_ik_vowel(s):
    return s in ik_vowels

def guna(s):
    m = {'i':'e','I':'e','u':'o','U':'o','f':'ar','F':'ar','x':'al','X':'al'}
    return m.get(s, s)

def apply_guna_last_ik(sounds):
    result = list(sounds)
    for i in range(len(result)-1, -1, -1):
        if is_ik_vowel(result[i]):
            g = guna(result[i])
            result = result[:i] + list(g) + result[i+1:]
            break
    return result

def apply_guna_all(sounds):
    result = []
    for s in sounds:
        if is_ik_vowel(s):
            result.extend(list(guna(s)))
        else:
            result.append(s)
    return result

def eco(sounds):
    result = []
    i = 0
    while i < len(sounds):
        s = sounds[i]
        if s in ('e','o') and i+1 < len(sounds) and is_vowel(sounds[i+1]):
            if s == 'e':
                result.extend(['a','y'])
            else:
                result.extend(['a','v'])
            i += 1
        else:
            result.append(s)
            i += 1
    return result

def savarna(sounds):
    pairs = {('a','a'):('A',1), ('a','A'):('A',1), ('A','a'):('A',1), ('A','A'):('A',1),
             ('i','i'):('I',1), ('i','I'):('I',1), ('I','i'):('I',1), ('I','I'):('I',1),
             ('u','u'):('U',1), ('u','U'):('U',1), ('U','u'):('U',1), ('U','U'):('U',1),
             ('e','e'):('e',1), ('o','o'):('o',1)}
    result = []
    i = 0
    while i < len(sounds):
        if i+1 < len(sounds) and (sounds[i],sounds[i+1]) in pairs:
            result.append(pairs[(sounds[i],sounds[i+1])][0])
            i += 2
        else:
            result.append(sounds[i])
            i += 1
    return result

def devoice(sounds):
    v2vl = {'g':'k','G':'K','j':'c','J':'C','d':'t','D':'T','b':'p','B':'P','q':'w','Q':'W'}
    aghosha = set('kKpPcCwWtT')
    result = []
    for i, s in enumerate(sounds):
        if s in v2vl and i+1 < len(sounds) and sounds[i+1] in aghosha:
            result.append(v2vl[s])
        else:
            result.append(s)
    return result

def derive_lin(dhatu, class_num, ting_label):
    """liṅ (optative) derivation.
    
    Architecture: 
    - aṅga = dhātu (+ Ṇic for class 10), with guṇa, WITHOUT vikaraṇa
    - optative ending = sī-derived (et, eyātam for a-final; yāt, yātām for u-final)
    - eco applies between guṇa'd dhātu vowel and optative vowel
    """
    vik_raw, vik_it = vikarana[class_num]
    vik_clean = remove_it(vik_raw, vik_it)
    
    has_tit = class_num in (1,5,7,8,9,10)
    is_nic = class_num == 10
    is_snu = class_num in (5,8)
    
    # Build aṅga: dhātu + vikaraṇa (but for optative, we need the STEM without the final -a vikaraṇa)
    # For class 1: aṅga = dhātu (NO Śap) → guṇa → bho → eco(with optative vowel) → bhav
    # For class 10: aṅga = dhātu + Ṇic(i) → guṇa ALL → cor+e → eco → coray
    # For class 4: aṅga = dhātu + Śya(ya) → no guṇa → pazy(a) → but we drop the final 'a'
    # For class 6: aṅga = dhātu → no guṇa → pac
    
    if is_nic:
        # Class 10: dhātu + i (Ṇic), guṇa ALL, keep vikaraṇa material (i)
        anga = dhatu + vik_clean  # cur + i
        anga = apply_guna_all(anga)  # cor + e
    elif has_tit and not is_snu:
        # Class 1: dhātu only (no Śap), guṇa last IK vowel
        anga = list(dhatu)
        anga = apply_guna_last_ik(anga)  # bhU → bho
    elif is_snu:
        # Class 5, 8: dhātu + vikaraṇa (nu/u), guṇa last IK vowel
        anga = dhatu + vik_clean  # su + nu = sunu
        anga = apply_guna_last_ik(anga)  # suno (u→o)
    else:
        # Class 4: dhātu + Śya(ya), no guṇa (class 4 has no ṭit)
        anga = dhatu + vik_clean  # paz + ya = pazy(a)
        # Class 6: dhātu only, no guṇa
        if class_num == 6:
            anga = list(dhatu)  # pac (no vikaraṇa in optative)
        elif class_num == 2:
            anga = list(dhatu)
        elif class_num == 4:
            # Class 4: Śya→ya, but the final 'a' in ya is NOT part of the optative stem
            # paz + ya → pazy(a) → drop final 'a' → pazy + et = pazyet ✓
            anga = dhatu + vik_clean  # paz + ya = p a z y a
            # Drop the final 'a' (it's the laṭ vikaraṇa vowel, not needed in optative)
            if anga and anga[-1] == 'a':
                anga = anga[:-1]  # p a z y
    
    # Get optative ending
    if is_snu:
        # For Śnu/Śu classes: need to handle u-final aṅga
        # guṇa'd: suno (o from u→o). eco: o + ī(vowel) → av + ī → sunavīt → ī→e → sunavet?
        # But actual is sunuyāt! So for Śnu classes, the optative uses yā-type, not e-type.
        # This means: no guṇa on dhātu vowel for Śnu in optative? Or different ending set?
        # 
        # Actually: sunuyāt = sunu + yāt. The 'u' stays (no guṇa), and 'yāt' is the ending.
        # So for Śnu: NO guṇa on dhātu vowel, use yā-type endings.
        anga = dhatu + vik_clean  # su + nu = sunu (NO guṇa!)
        ting = list(lin_ting_snu[ting_label])
    else:
        ting = list(lin_ting_para[ting_label])
    
    # Combine: aṅga + optative ending
    combined = anga + ting
    
    # For a-final aṅga: the last 'a' merges with 'e' of ending: a+e → ?
    # Actually, the vikaraṇa 'a' is NOT included (we dropped it).
    # So for class 1: bho + et → eco: o+e → av+e → bhavet
    # For class 6: pac + et = pacet (no sandhi)
    
    # Sandhi pipeline
    combined = eco(combined)
    combined = savarna(combined)
    combined = devoice(combined)
    
    return combined

# === Verify ===
print("=== liṅ (optative) verification ===\n")

lin_tests = [
    # (dhātu, class, tiṅ, expected)
    (['b','h','U'], 1, 'tip', 'bhavet'),       # bhū cl1: bhavet
    (['p','a','c'], 6, 'tip', 'pacet'),         # pac cl6: pacet
    (['c','u','r'], 10, 'tip', 'corayet'),       # cur cl10: corayet
    (['p','a','z'], 4, 'tip', 'pazyet'),         # paz cl4: paśyet
    (['n','I'], 1, 'tip', 'nayet'),              # nī cl1: nayet (ī→e→ay before e)
    (['k','f','S'], 6, 'tip', 'kfSet'),          # krṣ cl6: karṣet? → kfSet
    # 3pl
    (['b','h','U'], 1, 'jhi', 'bhaveyus'),      # bhav + eyus
    (['p','a','c'], 6, 'jhi', 'paceyus'),        # pac + eyus
    (['c','u','r'], 10, 'jhi', 'corayeyus'),    # coray + eyus
    # 1sg
    (['b','h','U'], 1, 'mip', 'bhaveyam'),      # bhav + eyam
    (['p','a','c'], 6, 'mip', 'paceyam'),        # pac + eyam
    (['c','u','r'], 10, 'mip', 'corayeyam'),    # coray + eyam
    # Class 5 (Śnu)
    (['s','u'], 5, 'tip', 'sunuyAt'),            # su cl5: sunuyāt (yā-type)
    (['s','u'], 5, 'jhi', 'sunuyus'),            # su cl5: sunuyus
    (['s','u'], 5, 'mip', 'sunuyAm'),            # su cl5: sunuyām
]

p = 0
for dhatu, cls, ting, expected in lin_tests:
    result = derive_lin(dhatu, cls, ting)
    got = ''.join(result)
    match = "✓" if got == expected else "✗"
    if got == expected:
        p += 1
    person = {'tip':'3sg', 'jhi':'3pl', 'mip':'1sg'}[ting]
    print(f"  {''.join(dhatu):6s} cl{cls:2d} {person:4s} expect={expected:12s} got={got:12s} {match}")

print(f"\nliṅ: {p}/{len(lin_tests)} ({100*p/len(lin_tests):.0f}%)")
