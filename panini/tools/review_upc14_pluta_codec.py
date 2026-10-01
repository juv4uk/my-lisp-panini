#!/usr/bin/env python3
"""Independent check of the pluta spelling in upc14v2_script (shiva PR #67), written from the PR text only.

Expectations come from the description + the Kasika corpus fact quoted there (bho3i = Devanagari bhO3i):
  pluta = LONG form + the digit 3 (a -> a-macron 3, i -> i-macron 3, u -> u-macron 3, r-vocalic -> long r-vocalic 3,
  l-vocalic (no long) -> l-vocalic 3, e o ai au -> e3 o3 ai3 au3); the strict decoder accepts only the long form + 3,
  short form + 3 (a3) only with strict=False.
Usage: python3 panini/tools/review_upc14_pluta_codec.py --graph /path/to/prototype
"""
import sys, itertools, random, unicodedata

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]
    sys.path.insert(0, gd)
    import upc14v2 as g, upc14v2_script as sc
    S = g.SOUNDS
    # base vowels by IAST key (stage-2 keys)
    LONG_IAST = {'a': 'ā', 'i': 'ī', 'u': 'ū', 'ṛ': 'ṝ', 'ḷ': 'ḷ', 'e': 'e', 'o': 'o', 'ai': 'ai', 'au': 'au'}
    DEV = {'a': 'आ', 'i': 'ई', 'u': 'ऊ', 'ṛ': 'ॠ', 'ḷ': 'ऌ', 'e': 'ए', 'o': 'ओ', 'ai': 'ऐ', 'au': 'औ'}
    def pluta(base, nasal=0):
        w = g.unpack(S[base])
        return g.Vertex(w.place, nasal, w.aperture, 2, w.voice, w.asp).code
    res = {'checked': 0, 'fail': []}
    def check(name, ok, detail=''):
        res['checked'] += 1
        if not ok: res['fail'].append((name, detail))
    for base in LONG_IAST:
        for nasal in (0, 1):
            c = pluta(base, nasal)
            tag = '%s%s' % (base, '~' if nasal else '')
            ia, de, cy = sc.to_iast(c), sc.to_devanagari(c), sc.to_cyrillic(c)
            if not nasal:
                check('iast spelling ' + tag, ia == LONG_IAST[base] + '3', ia)
                check('deva spelling ' + tag, de == DEV[base] + '३', de)
            else:
                nfd = unicodedata.normalize('NFD', ia)
                check('iast nasal = long form + U+0303 + 3 (NFD view) ' + tag, nfd == unicodedata.normalize('NFD', LONG_IAST[base]) + '\u0303' + '3', repr(nfd))
                try:
                    both = sc.decode_text(ia, 'iast', strict=True) == sc.decode_text(nfd, 'iast', strict=True)
                except Exception as e:
                    both = False
                check('decoder accepts NFC and NFD of ' + tag, both, repr(ia))
            for sname, fn_to, fn_from in (('iast', sc.to_iast, sc.code_from_iast), ('deva', sc.to_devanagari, sc.code_from_devanagari), ('cyr', sc.to_cyrillic, sc.code_from_cyrillic)):
                s = fn_to(c)
                try:
                    back = fn_from(s)
                except Exception as e:
                    back = 'ERR:%s' % type(e).__name__
                check('round-trip %s %s' % (sname, tag), back == c, '%r -> %r' % (s, back))
            for sname in ('iast', 'devanagari', 'cyrillic'):
                s = {'iast': ia, 'devanagari': de, 'cyrillic': cy}[sname]
                try:
                    seq = sc.decode_text(s, sname, strict=True)
                except Exception as e:
                    seq = 'ERR:%s' % type(e).__name__
                check('strict decode_text %s %s' % (sname, tag), seq == (c,), repr(seq))
    # short form + 3: strict must reject, non-strict accept and give the same code as the long form
    for short, long_ in (('a3', 'ā3'), ('i3', 'ī3'), ('u3', 'ū3'), ('ṛ3', 'ṝ3')):
        try:
            sc.decode_text(short, 'iast', strict=True); strict_rejects = False
        except Exception:
            strict_rejects = True
        try:
            lax = sc.decode_text(short, 'iast', strict=False)
            ref = sc.decode_text(long_, 'iast', strict=True)
            lax_ok = lax == ref
        except Exception as e:
            lax_ok = False
        check('strict rejects %s' % short, strict_rejects)
        check('non-strict %s == %s' % (short, long_), lax_ok)
    # corpus word: bho3i (IAST) and its Devanagari spelling decode to the same codes
    try:
        a = sc.decode_text('bho3i', 'iast', strict=True); b = sc.decode_text('भो३इ', 'devanagari', strict=True)
        check('bho3i iast == deva', a == b and len(a) == 3, '%r vs %r' % (a, b))
    except Exception as e:
        check('bho3i decode', False, type(e).__name__ + str(e)[:60])
    # round-trip every pair/triple of {42 sounds + all pluta vowels} through every script
    alph = [S[k] for k in S] + [pluta(b, n) for b in LONG_IAST for n in (0, 1)]
    for script in ('iast', 'devanagari', 'cyrillic'):
        bad = 0
        pairs = list(itertools.product(alph, repeat=2))
        for q in pairs:
            try:
                if sc.decode_text(sc.encode_text(q, script), script, strict=True) != tuple(q): bad += 1
            except Exception:
                bad += 1
        random.seed(67)
        trip = [tuple(random.choice(alph) for _ in range(3)) for _ in range(20000)]
        bad3 = 0
        for q in trip:
            try:
                if sc.decode_text(sc.encode_text(q, script), script, strict=True) != q: bad3 += 1
            except Exception:
                bad3 += 1
        check('pairs %s (%d)' % (script, len(pairs)), bad == 0, '%d failures' % bad)
        check('random triples %s (20000, seed 67)' % script, bad3 == 0, '%d failures' % bad3)
    print('checks run: %d, failures: %d' % (res['checked'], len(res['fail'])))
    for f in res['fail'][:40]: print('  FAIL', f)

if __name__ == '__main__':
    main()
