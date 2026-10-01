#!/usr/bin/env python3
"""Independent oracle for natva (8.4.1 + 8.4.2 + 8.4.37) inside one pada, from the Kasika texts
(KASIKA-8.4.1/8.4.2.yaml read), compared with upc14v2_sandhi.natva.
Rule as read:  n -> ṇ after r or ṣ (8.4.1; by the vartika also after ṛ, ṝ, Kasika 8.4.1 'ṛvarṇāc ca'), in the same pada,
even if only sounds of  aṭ (vowels, h y v r), ku (k kh g gh ṅ), pu (p ph b bh m)  (and ā, ṅ, anusvara)  intervene (8.4.2);
a pada-final n does not change (8.4.37, 'vṛkṣān'); with complete_pada=False a final n is not final yet.
Not modelled: 8.4.3+ compound exceptions, the vartika 'n only before vowel/n/m/y/v' (the Kasika text read does not state it),
anusvara/num, several n in one word (the words enumerated here have at most one n).
Usage: python3 review_upc14_natva.py --graph /path/to/prototype [--maxlen 4]
"""
import sys, itertools

ATT = {'a', 'i', 'u', 'ṛ', 'ḷ', 'e', 'o', 'ai', 'au', 'h', 'y', 'v', 'r'}      # aṭ
KU = {'k', 'kh', 'g', 'gh', 'ṅ'}
PU = {'p', 'ph', 'b', 'bh', 'm'}
TRIG = {'r', 'ṣ', 'ṛ'}
ALPHA = ['r', 'ṣ', 'ṛ', 'a', 'i', 'u', 'e', 'k', 'g', 'ṅ', 'p', 'm', 'h', 'y', 'v', 'c', 'ṭ', 't', 's', 'ś', 'n', 'l']

def natva_oracle(word, complete_pada=True):
    out = list(word)
    for j, s in enumerate(word):
        if s != 'n': continue
        if complete_pada and j == len(word) - 1: continue          # 8.4.37
        # nearest earlier sound that is not an allowed intervener must be a trigger; allowed interveners may sit between
        k = j - 1
        while k >= 0 and word[k] in (ATT | KU | PU) and word[k] not in TRIG:
            k -= 1
        if k >= 0 and word[k] in TRIG: out[j] = 'ṇ'
    return tuple(out)

def main():
    gd = sys.argv[sys.argv.index('--graph') + 1]
    maxlen = int(sys.argv[sys.argv.index('--maxlen') + 1]) if '--maxlen' in sys.argv else 4
    sys.path.insert(0, gd)
    import upc14v2_sandhi as sd
    total = diff = err = 0; kinds = {}; shown = 0
    for L in range(1, maxlen + 1):
        for w in itertools.product(ALPHA, repeat=L):
            if w.count('n') > 1: continue
            for cp in (True, False):
                total += 1
                try: got = tuple(sd.natva(list(w), complete_pada=cp))
                except Exception as e: err += 1; continue
                exp = natva_oracle(w, cp)
                if got != exp:
                    diff += 1
                    j = [i for i, s in enumerate(w) if s == 'n'][0] if 'n' in w else -1
                    nxt = w[j + 1] if 0 <= j < len(w) - 1 else '<end>'
                    key = ('graph ṇ, mine n' if 'ṇ' in got[j:j+1] else 'graph n, mine ṇ', 'next=' + ('vowel' if nxt in ATT else nxt))
                    kinds[key] = kinds.get(key, 0) + 1
                    if shown < 12: shown += 1; print('DIFF', ''.join(w), 'complete=%s' % cp, 'graph', ''.join(got), 'mine', ''.join(exp))
    print('\nnatva: words compared %d, DIFFERENT %d, graph raised %d' % (total, diff, err))
    for k, v in sorted(kinds.items(), key=lambda x: -x[1])[:10]: print('  ', k, v)

if __name__ == '__main__':
    main()
