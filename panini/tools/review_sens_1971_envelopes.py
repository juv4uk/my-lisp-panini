#!/usr/bin/env python3
"""Independent encoder/decoder for the two raw-wire envelopes of SENS #1971, from the description only.

Spec read (not the coordinator's script research-1971-unique-decoding.py):
  A = Width3 + escape (docs/research/1962-framing-separation.md): per word a 3-bit header
      000..110 = width 1..7 (header = width-1), then the payload;
      111 = extended: Elias-gamma(width-7) follows, then the payload (width >= 8).
      Worked example from the doc: tokens [10][0001][01] -> 001 10 | 011 0001 | 001 01 = 00110011000100101.
  B = gamma-only (issue #1971: "length-prefix/gamma-only"): Elias-gamma(width), then the payload.
      ASSUMPTION: B is exactly that (no other header); the issue gives no more detail.
Elias-gamma(n>=1): (bitlength(n)-1) zeros, then n in binary.  gamma(1)='1', gamma(2)='010', gamma(4)='00100'.

Checks (exhaustive): round trip, injectivity, and zero-padding to a whole byte after the last word.
"""
import itertools, sys

def gamma(n):
    b = format(n, 'b')
    return '0' * (len(b) - 1) + b

def enc_word_A(w):
    n = len(w)
    return (format(n - 1, '03b') + w) if n <= 7 else ('111' + gamma(n - 7) + w)
def enc_word_B(w):
    return gamma(len(w)) + w
ENC = {'A': enc_word_A, 'B': enc_word_B}

class Incomplete(Exception):
    pass

def read_gamma(s, i):
    z = 0
    while True:
        if i >= len(s): raise Incomplete()
        if s[i] == '1': break
        z += 1; i += 1
    if i + z + 1 > len(s): raise Incomplete()
    return int(s[i:i + z + 1], 2), i + z + 1

def read_word(env, s, i):
    if env == 'A':
        if i + 3 > len(s): raise Incomplete()
        h = int(s[i:i + 3], 2); i += 3
        if h < 7: n = h + 1
        else:
            g, i = read_gamma(s, i); n = g + 7
    else:
        n, i = read_gamma(s, i)
    if i + n > len(s): raise Incomplete()
    return s[i:i + n], i + n

def decode(env, s, lenient=False):
    """Greedy decoder. lenient: an incomplete trailing fragment is ignored; strict: it is an error."""
    out, i = [], 0
    while i < len(s):
        try:
            w, i2 = read_word(env, s, i)
        except Incomplete:
            if lenient: return out
            raise
        out.append(w); i = i2
    return out

def encode(env, words):
    return ''.join(ENC[env](w) for w in words)

def pad(s):
    return s + '0' * (-len(s) % 8)

def words_upto(n):
    return [''.join(b) for k in range(1, n + 1) for b in itertools.product('01', repeat=k)]

def sequences(words, maxlen):
    for k in range(1, maxlen + 1):
        yield from itertools.product(words, repeat=k)

def main():
    W = words_upto(4)
    seqs = list(sequences(W, 3))
    print('words (<=4 bits): %d; sequences (1..3 words): %d' % (len(W), len(seqs)))
    # sanity: the worked example in the doc
    assert encode('A', ['10', '0001', '01']) == '00110011000100101', encode('A', ['10', '0001', '01'])
    for env in 'AB':
        streams = {}
        rt_bad = 0
        for q in seqs:
            s = encode(env, q)
            if decode(env, s) != list(q): rt_bad += 1
            streams.setdefault(s, []).append(q)
        inj_coll = sum(len(v) - 1 for v in streams.values() if len(v) > 1)
        # padding: whole-byte zero padding after the last word
        padded = {}
        misread = misread_strict_err = 0
        for q in seqs:
            ps = pad(encode(env, q))
            padded.setdefault(ps, []).append(q)
            try:
                got = decode(env, ps, lenient=True)
            except Incomplete:
                got = None
            if got != list(q): misread += 1
            try:
                decode(env, ps, lenient=False)
            except Incomplete:
                misread_strict_err += 1
        shared = [v for v in padded.values() if len(v) > 1]
        pairs = sum(len(v) * (len(v) - 1) // 2 for v in shared)
        print('\nENVELOPE %s' % env)
        print('  round-trip failures (unpadded):                   %d' % rt_bad)
        print('  injectivity collisions (unpadded streams):        %d' % inj_coll)
        print('  padded streams shared by >1 sequence:             %d streams, %d unordered pairs, %d sequences involved' % (len(shared), pairs, sum(len(v) for v in shared)))
        print('  sequences whose padded stream decodes (lenient) to a DIFFERENT sequence: %d of %d' % (misread, len(seqs)))
        print('  sequences whose padded stream is an ERROR for a strict decoder:          %d of %d' % (misread_strict_err, len(seqs)))
    # wider words (escape range for A): single words and pairs, round trip + injectivity
    for env in 'AB':
        wide = words_upto(10)
        bad = sum(1 for w in wide if decode(env, encode(env, [w])) != [w])
        pr = list(itertools.product(words_upto(5), repeat=2)) + [(w, 'x') for w in []]
        bad2 = sum(1 for q in pr if decode(env, encode(env, list(q))) != list(q))
        print('\nENVELOPE %s wide check: single words up to 10 bits (%d): %d failures; pairs of words up to 5 bits (%d): %d failures' % (env, len(wide), bad, len(pr), bad2))

if __name__ == '__main__':
    main()
