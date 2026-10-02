#!/usr/bin/env python3
"""Attack on the 53 cells shared by the Sanskrit and the Ukrainian layouts of UPC-7 v3 (16 letters, 10 digits, 27 ASCII signs).
Subject: shiva-sutras upc7_lang (read only). Expectations come from upc7-table-v3.tsv and from the rule "refuse, never approximate".
(1) homoglyphs and normalisation; (2) cross-layout rendering of the 16 letters; (3) collisions of shared cells with syntax/apostrophes.
Usage: python3 review_upc7_shared53_attack.py --proto <shiva-sutras/prototype>     (prints PASS/DEFECT lines; counterexamples are printed)
"""
import csv, itertools, random, string, sys, unicodedata
from pathlib import Path

proto = Path(sys.argv[sys.argv.index('--proto') + 1])
sys.path.insert(0, str(proto))
import upc7_lang as L
T = L.LangText()
rows = list(csv.DictReader(open(proto / 'upc7-table-v3.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
nfc = lambda s: unicodedata.normalize('NFC', s); nfd = lambda s: unicodedata.normalize('NFD', s)
defects = []
def report(name, ok, detail=''):
    print(('PASS   ' if ok else 'DEFECT ') + name + (' | ' + detail if detail else ''))
    if not ok: defects.append(name)
def enc(t, lay):
    try: return ('ok', T.encode(t, lay))
    except L.LangError as e: return ('refused', str(e)[:80])
def show(t): return repr(t) + ' ' + ' '.join('U+%04X' % ord(c) for c in t if ord(c) > 127 or unicodedata.combining(c))

# ---------------------------------------------------------------- (1) homoglyphs
LAT = string.ascii_lowercase; CYR = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяъыэёѕ'
accepted = [c for c in LAT if enc(c, 'uk')[0] == 'ok']
report('uk layout refuses every single Latin letter a-z', not accepted, f'accepted: {accepted}')
accepted = [c for c in CYR if enc(c, 'sa-iast')[0] == 'ok']
report('sa-iast refuses every single Cyrillic letter', not accepted, f'accepted: {accepted}')
accepted = [c for c in CYR if enc(c, 'sa-deva')[0] == 'ok']
report('sa-deva refuses every single Cyrillic letter', not accepted, f'accepted: {accepted}')
accepted = [c for c in LAT if enc(c, 'sa-cyr')[0] == 'ok']
report('sa-cyr refuses every single Latin letter', not accepted, f'accepted: {accepted}')
H = {'k': 'к', 'p': 'п', 'c': 'с', 'o': 'о', 'a': 'а', 'i': 'і', 'y': 'у', 's': 'ѕ', 'x': 'х', 'e': 'е'}   # Latin -> look-alike Cyrillic
bad = []
for lat, cyr in H.items():
    for left, right in (('к', 'т'), ('т', 'і')):
        mixed_uk = left + lat + right; mixed_sa = 'k' + cyr + 't'
        if enc(mixed_uk, 'uk')[0] == 'ok': bad.append(('uk', show(mixed_uk)))
        if enc(mixed_sa, 'sa-iast')[0] == 'ok': bad.append(('sa-iast', show(mixed_sa)))
report('a Latin homoglyph inside a Ukrainian word / a Cyrillic homoglyph inside an IAST word is refused', not bad, str(bad[:4]))
other = ['ο', 'ν', 'ι', 'α', 'ｋ', 'ı', 'ł', 'ⅰ', 'ӏ']
bad = [(lay, show(c)) for c in other for lay in ('uk', 'sa-iast', 'sa-deva', 'sa-cyr') if enc(c, lay)[0] == 'ok']
report('Greek / fullwidth / dotless / Roman-numeral look-alikes are refused in all layouts', not bad, str(bad[:6]))

# ---------------------------------------------------------------- normalisation
def norm_check(layout, col):
    bad = []; n = 0
    for r in rows:
        s = r[col]
        if not s or r['class'] in ('sign',) or r['sound'].startswith('digit') or r['sound'] in ('capital', 'class'): continue
        n += 1
        variants = {s, nfc(s), nfd(s)}
        marks = [c for c in nfd(s) if unicodedata.combining(c)]
        if len(marks) >= 2:                                           # every ordering of the combining marks on the base
            base = [c for c in nfd(s) if not unicodedata.combining(c)]
            for perm in itertools.permutations(marks):
                cand = ''.join(base[:1]) + ''.join(perm) + ''.join(base[1:])
                if nfd(cand) == nfd(s): variants.add(cand)          # same combining class marks are NOT canonically equivalent: skip them
        results = {v: enc(v, layout) for v in variants}
        cells = {res[1] for res in results.values() if res[0] == 'ok'}
        refused = [show(v) for v, res in results.items() if res[0] == 'refused']
        if len(cells) > 1 or (cells and refused):
            bad.append((r['sound'], len(cells), refused[:2]))
    return n, bad
for layout, col in (('sa-iast', 'sa-iast'), ('sa-cyr', 'sa-cyr'), ('sa-deva', 'sa-deva')):
    n, bad = norm_check(layout, col)
    report(f'{layout}: NFC / NFD / any mark order of each of {n} sound spellings give the same cells (or are all refused)', not bad, str(bad[:5]))
for name, a, b in (('й', 'й', 'й'), ('ї', 'ї', 'ї'), ('ё-less: й in a word', 'кій', 'кі' + 'й')):
    ra, rb = enc(a, 'uk'), enc(b, 'uk')
    report(f'uk: {name} precomposed == decomposed', ra == rb, f'{ra} vs {rb}')
for label, a, b in (('ṃ U+1E43 vs m+U+0323', 'ṃ', 'ṃ'), ('ṃ vs ṁ (U+1E41, the common alternative)', 'ṃ', 'ṁ'), ('ś vs s+U+0301', 'ś', 'ś'),
                    ('ṛ vs ṙ', 'ṛ', 'ṙ'), ('ṅ vs ń', 'ṅ', 'ń'), ('ḥ vs h+U+0323', 'ḥ', 'ḥ')):
    ra, rb = enc(a, 'sa-iast'), enc(b, 'sa-iast')
    print(f'       info  sa-iast {label}: {ra[0]} / {rb[0]}  same={ra == rb}')
digits_other = ['٣', '۳', '３', '²', '①', '৩', '௩', '๓']
bad = [(lay, show(c)) for c in digits_other for lay in ('uk', 'sa-iast', 'sa-deva', 'sa-cyr') if enc(c, lay)[0] == 'ok']
report('Arabic-Indic / fullwidth / superscript / circled / other-script digits are refused everywhere', not bad, str(bad[:5]))
bad = [(lay, t) for lay, t in (('sa-deva', 'क7'), ('sa-deva', '7'), ('uk', 'к७'), ('sa-iast', 'k७'), ('sa-cyr', 'к७')) if enc(t, lay)[0] == 'ok']
report('Devanagari digit refused outside sa-deva and ASCII digit refused inside sa-deva (also next to a letter)', not bad, str(bad))
c_acute = enc('ш́', 'uk'); print('       info  uk: ш + U+0301 (sa-cyr spelling of ś) ->', c_acute[0], c_acute[1] if c_acute[0] == 'refused' else '')
r1 = enc('ш́', 'sa-cyr'); r2 = enc('ш', 'sa-cyr'); print('       info  sa-cyr: ш + U+0301 ->', r1[0], r1[1] if r1[0] == 'ok' else r1[1], '| plain ш ->', r2[0], r2[1] if r2[0] != 'ok' else '')
bad = [t for t in ('а́', 'ш́а', 'ќ') if enc(t, 'sa-cyr')[0] == 'ok' and enc(t, 'sa-cyr') == enc(t, 'uk')]
for t in ('а́', 'и́', 'у́'):                   # a Ukrainian stress on a vowel written in the sa-cyr layout
    print(f'       info  stress {show(t)}: uk {enc(t, "uk")[0]}, sa-cyr {enc(t, "sa-cyr")[0]}')

# ---------------------------------------------------------------- (2) cross-render of the 16 letters
SH = {'к': 'k', 'ґ': 'g', 'т': 't', 'д': 'd', 'н': 'n', 'п': 'p', 'б': 'b', 'м': 'm', 'і': 'i', 'у': 'u', 'й': 'y', 'с': 's', 'р': 'r', 'л': 'l', 'в': 'v', 'ш': 'ś'}
col = {r['sound']: r for r in rows}
bad = []
for u, s in SH.items():
    cu = enc(u, 'uk')[1]
    for lay, c in (('sa-iast', 'sa-iast'), ('sa-deva', 'sa-deva'), ('sa-cyr', 'sa-cyr')):
        try: out = T.render(cu, lay)
        except L.LangError as e: bad.append((u, lay, 'render refused')); continue
        back = enc(out, lay)
        if back != ('ok', cu): bad.append((u, lay, out, back))
        if lay == 'sa-iast' and out != s: bad.append((u, lay, 'expected', s, 'got', out))
        if T.render(back[1], 'uk') != u if back[0] == 'ok' else True: bad.append((u, lay, 'does not return to', u))
report('16 letters: uk -> cell -> iast/deva/cyr -> same cell -> uk gives the same letter, iast glyph as in the table', not bad, str(bad[:5]))
rnd = random.Random(53); words = []
letters = list(SH)
for ln in range(1, 6):
    for _ in range(1500): words.append(''.join(rnd.choice(letters) for _ in range(ln)))
bad = []; textdiff = []; refused = 0
for w in words:
    r = enc(w, 'uk')
    if r[0] != 'ok': refused += 1; continue
    for lay in ('sa-iast', 'sa-deva', 'sa-cyr'):
        try: out = T.render(r[1], lay); back = enc(out, lay)
        except L.LangError as e: bad.append((w, lay, 'render/encode: ' + str(e)[:40])); continue
        if back != ('ok', r[1]): bad.append((w, lay, out, back[0]))
        elif T.render(back[1], 'uk') != w: textdiff.append((w, T.render(back[1], 'uk')))
report('7500 random words of the 16 shared letters: uk -> iast/deva/cyr -> same CELLS', not bad, f'{len(bad)} cell failures {bad[:4]}; refused by uk orthography {refused}')
print(f'       info  text (not cell) differences after the round trip: {len(textdiff)} of {len(words)*3}; all contain й+vowel merged by the orthography: {all("й" in w for w, _ in textdiff)}; samples {textdiff[:4]}')
# the wrong-sound question: shared cells vs the distinctions Sanskrit makes
pairs = [('ś/ṣ', 'विष', 'sa-deva', 'uk'), ('ś/ṣ', 'विश', 'sa-deva', 'uk'), ('r/ṛ', 'कृत', 'sa-deva', 'uk'), ('r/ṛ', 'कर', 'sa-deva', 'uk')]
for label, t, a, b in pairs:
    r = enc(t, a)
    try: print(f'       info  {label}: {t!r} ({a}) -> {b}:', repr(T.render(r[1], b)) if r[0] == 'ok' else r)
    except L.LangError as e: print(f'       info  {label}: {t!r} ({a}) -> {b}: REFUSED ({str(e)[:60]})')
bad = []
for lay, t in (('sa-iast', 'viṣa'), ('sa-iast', 'kṛta'), ('sa-iast', 'tantra'), ('sa-iast', 'śiva'), ('sa-iast', 'vaśa')):
    r = enc(t, lay)
    if r[0] == 'ok':
        try: out = T.render(r[1], 'uk'); bad.append((t, '->', out))
        except L.LangError: pass
print('       info  Sanskrit words that DO render in the Ukrainian layout (a sound outside the shared set would have been refused):', bad)
mism = []
for t in ('śiva', 'veśa', 'vaśa', 'viṣa', 'veṣa', 'kṛta', 'ṛṣi'):
    r = enc(t, 'sa-iast')
    if r[0] != 'ok': print('       info  not encodable:', t, r[1]); continue
    try: mism.append((t, T.render(r[1], 'uk')))
    except L.LangError as e: mism.append((t, 'REFUSED'))
print('       info  Sanskrit -> uk:', mism)

# ---------------------------------------------------------------- (3) syntax and apostrophes
for t in ("п'ять", 'п’ять', 'пʼять', 'п`ять', "'кіт'", "кіт'", "'", "м'я"):
    r = enc(t, 'uk'); print(f'       info  uk {t!r}: {r[0]}', r[1] if r[0] == 'ok' else r[1])
a1, a2, a3, a4 = (enc(x, 'uk') for x in ("п'ять", 'п’ять', 'пʼять', 'п`ять'))
report("uk: the three apostrophe spellings ' ’ ʼ give the same cells", a1 == a2 == a3, f'{a1[1]} / {a2[1]} / {a3[1]}')
report("uk: backtick is NOT an apostrophe (a sign cell + a new word), by policy after PR #100", a4[0] != 'ok' or a4[1] != a1[1], f'{a4}')
print('       info  uk apostrophe renders back as:', T.render(a1[1], 'uk'), '(’ and ʼ inputs become the ASCII apostrophe)')
r = enc("к'т", 'uk')
try: out = T.render(r[1], 'uk'); back = enc(out, 'uk'); report("uk: ASCII ' between two consonant letters is the sign cell and round-trips", r[0] == 'ok' and back == r and 121 in r[1], f"к'т {r[1]} -> {out!r} -> {back[1]}")
except L.LangError as e: report("uk: к'т renders", False, str(e)[:80])
r2 = enc("k't", 'sa-iast')
report("sa-iast: ASCII ' inside a word is refused (the avagraha is written ’)", r2[0] == 'refused', str(r2))
av_iast, ap_iast = enc('so’ham', 'sa-iast'), enc("so'ham", 'sa-iast')
report("sa-iast: so’ham (U+2019) is accepted and so'ham (ASCII ') is refused, so one identity", av_iast[0] == 'ok' and ap_iast[0] == 'refused', f"so’ham {av_iast[0]} / so'ham {ap_iast}")
report('sa-iast: "||" (two ASCII pipes) is not silently the double daṇḍa, and "|" is not the daṇḍa', enc('||', 'sa-iast') != enc('॥', 'sa-iast') and enc('|', 'sa-iast') != enc('।', 'sa-iast'), f"{enc('||', 'sa-iast')[1]} vs {enc('॥', 'sa-iast')[1]}")
shared_signs = [s for s, c in L.SIGN_CELL.items()]
bad = []
for s in shared_signs:
    for lay, left, right in (('uk', 'к', 'т'), ('sa-iast', 'k', 't'), ('sa-deva', 'क', 'त'), ('sa-cyr', 'к', 'т')):
        t = left + s + right; r = enc(t, lay)
        if r[0] != 'ok':
            if s == "'" and lay != 'uk': continue                    # by policy: ASCII ' inside a Sanskrit word is refused (avagraha = U+2019)
            bad.append((lay, repr(s), r[1])); continue
        try: back = T.render(r[1], lay)
        except L.LangError as e: bad.append((lay, repr(s), 'render ' + str(e)[:40])); continue
        if enc(back, lay) != r: bad.append((lay, repr(s), 'round trip', repr(back)))
report(f'each of the {len(shared_signs)} ASCII signs between two letters round-trips in all four layouts', not bad, str(bad[:6]))
cells_signs = {s: enc(s, lay)[1] for s in shared_signs for lay in ('uk',)}
same = all(enc(s, lay) == enc(s, 'uk') for s in shared_signs for lay in ('sa-iast', 'sa-deva', 'sa-cyr'))
report('each ASCII sign has the identical cell in all four layouts', same)
print(f'\n{len(defects)} defects: {defects}')
sys.exit(0)
