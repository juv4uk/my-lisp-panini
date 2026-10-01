#!/usr/bin/env python3
"""Independent Ukrainian orthography <-> sound tokens oracle (shiva-sutras PR #77), written from the rule TABLE in
docs/upc7-language-table-2026-10-02.md section 3 (NOT from uk_orth.py), and run over the dict_uk lemma list.

Rules as read (section 3):  я ю є after a consonant = consonant + ь + а у е;  я ю є at a word start or after a vowel = й + а у е;
ї = й + і;  щ = ш + ч;  ь, ьо, йо are softness / ь+о / й+о;  an apostrophe before я ю є ї after a consonant = consonant + й + vowel
(re-inserted on rendering);  дз дж ц ч are one token each.  Tokens are Ukrainian letters (one per sound), as in uk_orth.to_tokens.
Case: lowercased.  Anything else (digits, hyphen, Latin, other punctuation) is REFUSED.

Usage: python3 review_uk_orthography.py --graph /path/to/shiva-sutras/prototype --lst /path/to/dict_uk/data/dict/base.lst [--limit N]
"""
import sys, collections

CONS = set('бвгґджзйклмнпрстфхцчш')
VOW = set('аеиіоу')
IOT = {'я': 'а', 'ю': 'у', 'є': 'е'}
BACK = {'а': 'я', 'у': 'ю', 'е': 'є'}
APOS = set("'’ʼ`")

class Refuse(Exception):
    pass

def my_tokens(word):
    w = word.lower()
    out = []; i = 0
    while i < len(w):
        c = w[i]
        prev = out[-1] if out else None
        if c in APOS:
            # an apostrophe is only meaningful before я ю є ї after a consonant
            if i + 1 < len(w) and w[i + 1] in 'яюєї' and prev in CONS | {'дз', 'дж', 'ц', 'ч', 'ш'}:
                i += 1; out.append('\0')            # marker: iotation without softness
                continue
            raise Refuse('apostrophe in %r' % word)
        if c == 'д' and i + 1 < len(w) and w[i + 1] in 'зж':
            out.append('д' + w[i + 1]); i += 2; continue
        if c in IOT:
            if out and out[-1] == '\0':
                out.pop(); out.extend(['й', IOT[c]])
            elif prev is not None and (prev in CONS or prev in ('дз', 'дж')) and prev != 'й':
                out.extend(['ь', IOT[c]])
            else:
                out.extend(['й', IOT[c]])
            i += 1; continue
        if c == 'ї':
            if out and out[-1] == '\0': out.pop()
            out.extend(['й', 'і']); i += 1; continue
        if c == 'щ': out.extend(['ш', 'ч']); i += 1; continue
        if c == 'ь' or c in CONS or c in VOW:
            out.append(c); i += 1; continue
        raise Refuse('char %r in %r' % (c, word))
    if '\0' in out: raise Refuse('dangling apostrophe')
    return out

def my_orth(tokens):
    out = []; i = 0; n = len(tokens)
    CONSTOK = CONS | {'дз', 'дж'}
    while i < n:
        t = tokens[i]; prev = tokens[i - 1] if i else None; nxt = tokens[i + 1] if i + 1 < n else None
        if t == 'ь' and nxt in BACK and prev in CONSTOK and prev != 'й':
            out.append(BACK[nxt]); i += 2; continue
        if t == 'й' and nxt in BACK:
            out.append(("'" if prev in CONSTOK and prev != 'й' else '') + BACK[nxt]); i += 2; continue
        if t == 'й' and nxt == 'і':
            out.append(("'" if prev in CONSTOK and prev != 'й' else '') + 'ї'); i += 2; continue
        if t == 'ш' and nxt == 'ч':
            out.append('щ'); i += 2; continue
        out.append(t); i += 1
    return ''.join(out)

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]; lst = sys.argv[sys.argv.index('--lst') + 1]
    limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None
    sys.path.insert(0, gd)
    import uk_orth as U
    lemmas = []
    for line in open(lst, encoding='utf-8'):
        s = line.strip()
        if not s or s.startswith('#'): continue
        lemmas.append(s.split()[0])
    if limit: lemmas = lemmas[:limit]
    norm = lambda s: s.replace('’', "'").replace('ʼ', "'").replace('`', "'")
    stats = collections.Counter(); diff_class = []; tok_diff = []; both = 0
    for w in lemmas:
        wl = w.lower()
        try: mt = my_tokens(w); mo = my_orth(mt); mine = 'exact' if norm(mo) == norm(wl) else 'differs'
        except Refuse: mt = None; mine = 'refused'
        try: tt = U.to_tokens(w); theirs = 'exact' if norm(U.to_orth(tt)) == norm(wl) else 'differs'
        except Exception: tt = None; theirs = 'refused'
        stats[(mine, theirs)] += 1
        if mine != theirs and len(diff_class) < 25: diff_class.append((w, mine, theirs))
        if mt is not None and tt is not None:
            both += 1
            if [t for t in mt] != [t for t in tt] and len(tok_diff) < 25: tok_diff.append((w, mt, tt))
    print('lemmas: %d' % len(lemmas))
    for k, v in sorted(stats.items(), key=lambda x: -x[1]): print('  mine=%-8s theirs=%-8s %d' % (k[0], k[1], v))
    print('classification differences (mine vs theirs), first %d:' % len(diff_class))
    for d in diff_class: print('  ', d)
    print('token sequences compared where both produce tokens: %d; different: shown %d' % (both, len(tok_diff)))
    for d in tok_diff: print('  ', d)

if __name__ == '__main__':
    main()
