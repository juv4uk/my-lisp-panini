#!/usr/bin/env python3
"""Read-only audit (#17): sutra numbers cited in machine/ and tests/ vs registry/sutras.lisp.

No dependencies. Usage: python3 panini/tools/audit_sutra_refs.py [--md]
Does not modify anything. The registry (:slp1) is the oracle; code names are
IAST/ASCII prose, so both sides are reduced to a lossy skeleton before comparing.
"""
import glob, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
NUM = re.compile(r'(?<![\d.])(\d\.\d\.\d{1,3})(?![\d.])')

def load_registry():
    reg = {}
    pat = re.compile(r'"(\d\.\d\.\d+)"\s+\(hash\b.*?:slp1\s+"([^"]*)"')
    for line in open(os.path.join(ROOT, 'registry', 'sutras.lisp'), encoding='utf-8'):
        m = pat.search(line)
        if m:
            reg[m.group(1)] = m.group(2)
    return reg

DIGRAPHS = [('kh', 'K'), ('gh', 'G'), ('ch', 'C'), ('jh', 'J'), ('ṭh', 'W'), ('ḍh', 'Q'),
            ('th', 'T'), ('dh', 'D'), ('ph', 'P'), ('bh', 'B')]
IAST = [('ai', 'E'), ('au', 'O'), ('ā', 'A'), ('ī', 'I'), ('ū', 'U'), ('ṝ', 'F'), ('ṛ', 'f'),
        ('ḷ', 'x'), ('ṅ', 'N'), ('ñ', 'Y'), ('ṭ', 'w'), ('ḍ', 'q'), ('ṇ', 'R'), ('ś', 'S'),
        ('ṣ', 'z'), ('ṃ', 'M'), ('ḥ', 'H')]

def skeleton(s, slp1=False):
    """Lossy comparison key. IAST is first turned into SLP1 (digraphs before singles),
    then case and vowel length are dropped and non-letters removed."""
    if not slp1:
        s = s.replace('Ś', 'ś').replace('Ṣ', 'ṣ')
        for a, b in DIGRAPHS:
            s = s.replace(a, b)
        for a, b in IAST:
            s = s.replace(a, b)
    s = re.sub(r"[^A-Za-z]", '', s).lower()
    return s.replace('aa', 'a').replace('ii', 'i').replace('uu', 'u')

def name_after(text, end):
    rest = text[end:]
    if re.match(r'\s*[)+,/]', rest) or not rest.strip():
        return ''
    rest = re.sub(r'^\s*[:\-–—]?\s*', '', rest)
    return re.split(r'\s+[—–]|\s*[(;)]|\s{2,}', rest)[0].strip(' :,.')

def main():
    reg = load_registry()
    files = sorted(glob.glob(os.path.join(ROOT, 'machine', '*.lisp')) +
                   glob.glob(os.path.join(ROOT, 'tests', '*.lisp')))
    rows = []
    for f in files:
        lines = open(f, encoding='utf-8').read().split('\n')
        for i, line in enumerate(lines, 1):
            for m in NUM.finditer(line):
                num = m.group(1)
                if not re.match(r'[1-8]\.\d\.\d+$', num):
                    continue
                window = line + ' ' + (lines[i] if i < len(lines) else '')
                rows.append((os.path.relpath(f, ROOT) + ':%d' % i, num,
                             name_after(line, m.end()), reg.get(num), window))
    out = ['| file:line | number | text after number in code | name in registry (SLP1) | verdict |', '|---|---|---|---|---|']
    counts = {}
    orphans, unmatched = [], []
    for loc, num, name, r, window in rows:
        if r is None:
            verdict = 'ORPHAN (number not in registry)'; orphans.append(loc + ' ' + num)
        else:
            rs = skeleton(r, True)
            cs = skeleton(name)
            found = rs and (rs in skeleton(window) or rs in skeleton(window, True)
                            or (len(cs) >= 3 and (cs in rs or rs in cs)))
            if found:
                verdict = 'match (registry name found on this/next line)'
            else:
                verdict = 'NO MATCHING NAME ON LINE'; unmatched.append((loc, num, name, r))
        counts[verdict.split(' (')[0]] = counts.get(verdict.split(' (')[0], 0) + 1
        out.append('| %s | %s | %s | %s | %s |' % (loc, num, name.replace('|', '/') or '-', r or '-', verdict))
    print('\n'.join(out))
    print('\nrefs=%d %s' % (len(rows), counts))
    print('Orphans:', orphans or 'none')
    print('Unmatched (triage manually: a wrong name is NOT the only cause; English glosses and string data land here):')
    for m in unmatched: print('  ', m[0], m[1], '| code:', repr(m[2])[:60], '| registry:', m[3])

if __name__ == '__main__':
    main()
