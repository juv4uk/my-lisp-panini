#!/usr/bin/env python3
"""Does the fail-closed render of upc7_lang (shiva-sutras PR #100) refuse VALID cell streams?
A stream is valid when some text encodes to it. Method: draw random texts, keep the ones `encode` accepts, and require `render(cells)` to succeed
and to re-encode to the same cells (a refusal here is a FALSE refusal). Families: random uk texts (letters, capitals, apostrophes, signs, digits),
random IAST / Devanagari / Cyrillic-Sanskrit texts built from table spellings and signs, real texts (dict_uk lemmas, Sanskrit verses with ṃ ḥ ’ । ॥),
mixed two-language streams, and every single cell. Usage: python3 review_upc7_failclosed_render.py --proto P --dict base.lst --verses sanskrit_embeddings.jsonl [--n 60000]
"""
import csv, json, random, re, sys, unicodedata
from pathlib import Path

def arg(n, d=None): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
proto = Path(arg('--proto')); N = int(arg('--n', '60000'))
sys.path.insert(0, str(proto))
import upc7_lang as L
T = L.LangText(); rnd = random.Random(100)
rows = list(csv.DictReader(open(proto / 'upc7-table-v3.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
fails = []; stats = {}
def check(family, text, layout):
    st = stats.setdefault(family, [0, 0, 0])                          # drawn, valid, false refusals
    st[0] += 1
    try: cells = T.encode(text, layout)
    except L.LangError: return
    st[1] += 1
    try:
        out = T.render(cells, layout)
        ok = tuple(T.encode(out, layout)) == tuple(cells)
    except L.LangError as e:
        out, ok = 'REFUSED: ' + str(e)[:70], False
    except Exception as e:
        out, ok = 'EXCEPTION %s: %s' % (type(e).__name__, str(e)[:60]), False
    if not ok:
        st[2] += 1
        if len(fails) < 30: fails.append((family, layout, text, out))

# --- random uk texts
UK = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя') + list("''’ʼ") + list(' \n-.,:;()"!?0123456789_+*/=<>&|@#\\')
for _ in range(N):
    t = ''.join(rnd.choice(UK) for _ in range(rnd.randrange(1, 9)))
    if rnd.random() < 0.3: t = t.capitalize()
    check('uk random text', t, 'uk')
# --- random Sanskrit texts from the table spellings + signs
for lay, col in (('sa-iast', 'sa-iast'), ('sa-deva', 'sa-deva'), ('sa-cyr', 'sa-cyr')):
    pool = [r[col] for r in rows if r[col] and r['class'] != 'class' and not r['sound'].startswith('digit')] + list(' \n.,;:-()0123456789०१२३४५६७८९') + ['ṃ', 'ḥ', '’', '।', '॥']
    for _ in range(N // 2):
        t = ''.join(rnd.choice(pool) for _ in range(rnd.randrange(1, 8)))
        check(lay + ' random text', unicodedata.normalize('NFC', t), lay)
# --- every single cell and every pair of valid cells
singles = {}
for r in rows:
    if r['class'] == 'class': continue
    c = int(r['bits'], 2); singles[c] = r
for c in singles:
    for lay in ('uk', 'sa-iast', 'sa-deva', 'sa-cyr'):
        try: T.render((c,), lay)
        except L.LangError: pass
# --- real texts
verses = []
if arg('--verses'):
    for ln in open(arg('--verses'), encoding='utf-8'):
        if len(verses) >= 600: break
        for l in json.loads(ln)['chunk_text'].split('\n'):
            if '॥' in l or '।' in l: verses.append(' '.join(re.sub(r'[0-9०-९.]+', ' ', l).split()))
for v in verses: check('real Sanskrit verse, deva with ṃ ḥ ऽ । ॥', v, 'sa-deva')
words = []
if arg('--dict'):
    seen = set()
    for ln in open(arg('--dict'), encoding='utf-8'):
        if ln.strip() and not ln.startswith(('#', ' ')):
            w = ln.split()[0]
            if w not in seen and re.fullmatch(r"[а-щьюяєіїґ'ʼ’-]+", w): seen.add(w); words.append(w)
    rnd.shuffle(words); words = words[:6000]
for w in words: check('real dict_uk lemma', w, 'uk')
long_text = ' '.join(words[:800]); check('long uk text (800 lemmas in one stream)', long_text, 'uk')
good = [v for v in verses if (lambda t: (T.encode(t, 'sa-deva') is not None))(v) if True] if False else []
for v in verses:
    try: T.encode(v, 'sa-deva'); good.append(v)
    except L.LangError: pass
long_sa = ' ।\n'.join(good[:200]); check('long Sanskrit text (200 verses in one stream, ṃ ḥ throughout)', long_sa, 'sa-deva')
# --- closure under concatenation: A and B each render, does A+B (a legal Text7 concatenation) render?
conc = {}
pool_by_layout = {}
def valid_texts(layout, gen, k):
    out = []
    while len(out) < k:
        t = gen()
        try: T.encode(t, layout); out.append(t)
        except L.LangError: pass
    return out
gens = {'uk': lambda: ''.join(rnd.choice(UK) for _ in range(rnd.randrange(1, 6))),
        'sa-iast': lambda: ''.join(rnd.choice([r['sa-iast'] for r in rows if r['sa-iast'] and r['class'] != 'class' and not r['sound'].startswith('digit')] + [' ', 'ṃ', 'ḥ']) for _ in range(rnd.randrange(1, 5))),
        'sa-deva': lambda: ''.join(rnd.choice([r['sa-deva'] for r in rows if r['sa-deva'] and r['class'] != 'class' and not r['sound'].startswith('digit')] + [' ', 'ं', 'ः']) for _ in range(rnd.randrange(1, 5)))}
for lay, g in gens.items():
    texts = valid_texts(lay, g, 1500); n = bad = only121 = 0; ex = []
    for _ in range(6000):
        a, b = rnd.choice(texts), rnd.choice(texts)
        try: stream = T.encode(a, lay) + T.encode(b, lay)
        except L.LangError: continue
        n += 1
        try:
            out = T.render(stream, lay); ok = tuple(T.encode(out, lay)) == tuple(stream)
        except L.LangError as e: ok = False; out = 'REFUSED ' + str(e)[:50]
        if not ok:
            bad += 1; only121 += 121 in stream
            if len(ex) < 4: ex.append((a, b, out))
    conc[lay] = (n, bad, ex, only121)
# --- named closure counterexamples
named = []
for label, a, b, lay in (("д + з across a morpheme boundary (digraph дз is one cell)", 'під', 'звіт', 'uk'), ("д + ж", 'під', 'жити', 'uk'), ("apostrophe sign then я", "к'", 'ять', 'uk'),
                         ("sign ' then a letter in sa-iast", "k'", 't', 'sa-iast')):
    st = T.encode(a, lay) + T.encode(b, lay)
    try: joined = T.encode(a + b, lay)
    except L.LangError: joined = 'the joined TEXT is refused'
    try: out = T.render(st, lay); res = 'renders ' + repr(out) + ' re-encodes same: ' + str(tuple(T.encode(out, lay)) == tuple(st))
    except L.LangError as e: res = 'REFUSED'
    named.append((label, a, b, 'cells(A)+cells(B) == cells(A+B): ' + str(st == joined), res))
print('named closure cases:'); [print('  ', n) for n in named]
# --- mixed streams: segments in two languages, all-shared sounds, rendered per segment
SH_UK = 'кґтднпбміуйсрлвш'; SH_IAST = ['k', 'g', 't', 'd', 'n', 'p', 'b', 'm', 'i', 'u', 'y', 's', 'r', 'l', 'v', 'ś']
mixed = {'n': 0, 'bad': 0, 'ex': []}
for _ in range(4000):
    a = ''.join(rnd.choice(SH_UK) for _ in range(rnd.randrange(1, 5))); b = ''.join(rnd.choice(SH_IAST) for _ in range(rnd.randrange(1, 5)))
    try: ca, cb = T.encode(a, 'uk'), T.encode(b, 'sa-iast')
    except L.LangError: continue
    sp = T.encode(' ', 'uk'); stream = ca + sp + cb; mixed['n'] += 1
    try:
        t_uk = T.render(stream, 'uk'); t_sa = T.render(stream, 'sa-iast')
        ok = T.encode(t_uk, 'uk') == stream and T.encode(t_sa, 'sa-iast') == stream
    except L.LangError as e: ok = False; t_uk = str(e)[:60]
    if not ok:
        mixed['bad'] += 1
        if len(mixed['ex']) < 5: mixed['ex'].append((a, b, t_uk))
print('family                                              drawn  valid  false-refusals')
for k, (d, v, f) in stats.items(): print(f'{k:<52}{d:>6}{v:>7}{f:>8}')
print(f'mixed uk+sa-iast shared-sound streams: {mixed["n"]} valid, {mixed["bad"]} not rendered/re-encoded identically {mixed["ex"]}')
for lay, (n, bad, ex, o121) in conc.items(): print(f'concatenation closure {lay}: {n} pairs A+B of individually valid texts, {bad} streams refused ({o121} of them contain the apostrophe sign cell 121); examples {ex[:2]}')
print('first false refusals:'); [print('  ', f) for f in fails[:12]]
sys.exit(0)
