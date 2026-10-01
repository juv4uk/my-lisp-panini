#!/usr/bin/env python3
"""Independent encoder/decoder of the four tail-length frames of SENS #2189, from the issue text only
(issues #2189, #2188, PR #2195 description; NOT scripts/research-2189-tail-length.py).

Packed payload (#2188/#2195): words are exact-width bit strings Bits<1..8>, appended MSB-first in program order,
payload_bytes = ceil(payload_bits / 8), tail bits are zero padding (canonical: non-zero tail padding rejected).
Frames (my reading; the issue gives no byte layouts, so these are ASSUMPTIONS stated here):
  A  varint(payload_bits) + payload bytes                        (explicit total payload bit length)
  B  varint(word_count) + word widths (3 bits each = width-1, zero-padded to a byte) + payload bytes
  C  varint(container_len) + valid_bits_in_last_byte (1..8; 0 only for the empty payload) + payload bytes
  D  payload bits + one '1' stop bit, zero-padded to a byte; the last byte must be non-zero   (no length field)
Decoders are STRICT: they accept exactly the canonical encodings (extra bytes, non-zero padding, non-minimal varint,
truncation -> reject).  Words in the test: all bit strings of 1..4 bits (30), sequences of 0..3 words (27931).
"""
import itertools, sys
from collections import defaultdict

class Reject(Exception):
    pass

# ---------- bit helpers
def bits_to_bytes(bits):
    bits += '0' * (-len(bits) % 8)
    return bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))
def bytes_to_bits(bs):
    return ''.join(format(b, '08b') for b in bs)
def varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F; n >>= 7
        out.append(b | (0x80 if n else 0))
        if not n: return bytes(out)
def read_varint(bs, i):
    n = shift = 0; start = i
    while True:
        if i >= len(bs): raise Reject('truncated varint')
        b = bs[i]; i += 1
        n |= (b & 0x7F) << shift; shift += 7
        if not b & 0x80: break
    if varint(n) != bs[start:i]: raise Reject('non-canonical varint')
    return n, i

def payload_of(words):
    return ''.join(words)
def check_tail(payload_bits, bs):
    """payload bytes must be exactly ceil(n/8) with zero tail padding"""
    n = len(payload_bits)
    if len(bs) != -(-n // 8): raise Reject('payload length mismatch')
    return payload_bits

# ---------- A
def enc_A(words):
    p = payload_of(words); return varint(len(p)) + bits_to_bytes(p)
def dec_A(bs):
    n, i = read_varint(bs, 0)
    body = bs[i:]
    if len(body) != -(-n // 8): raise Reject('A: payload length')
    bits = bytes_to_bits(body)
    if bits[n:].strip('0'): raise Reject('A: non-zero padding')
    return bits[:n]

# ---------- B (returns the full word sequence)
def enc_B(words):
    w = ''.join(format(len(x) - 1, '03b') for x in words)
    return varint(len(words)) + bits_to_bytes(w) + bits_to_bytes(payload_of(words))
def dec_B(bs):
    c, i = read_varint(bs, 0)
    wbytes = -(-(3 * c) // 8)
    if len(bs) < i + wbytes: raise Reject('B: truncated widths')
    wbits = bytes_to_bits(bs[i:i + wbytes])
    if wbits[3 * c:].strip('0'): raise Reject('B: non-zero width padding')
    widths = [int(wbits[3 * j:3 * j + 3], 2) + 1 for j in range(c)]
    i += wbytes
    n = sum(widths)
    body = bs[i:]
    if len(body) != -(-n // 8): raise Reject('B: payload length')
    bits = bytes_to_bits(body)
    if bits[n:].strip('0'): raise Reject('B: non-zero padding')
    out, p = [], 0
    for w in widths: out.append(bits[p:p + w]); p += w
    return out

# ---------- C
def enc_C(words):
    p = payload_of(words); n = len(p)
    if n == 0: return varint(0) + bytes([0])
    L = -(-n // 8); v = n - 8 * (L - 1)
    return varint(L) + bytes([v]) + bits_to_bytes(p)
def dec_C(bs):
    L, i = read_varint(bs, 0)
    if i >= len(bs): raise Reject('C: missing valid-bit count')
    v = bs[i]; i += 1
    body = bs[i:]
    if L == 0:
        if v != 0 or body: raise Reject('C: empty payload malformed')
        return ''
    if not 1 <= v <= 8: raise Reject('C: valid count')
    if len(body) != L: raise Reject('C: container length')
    n = 8 * (L - 1) + v
    bits = bytes_to_bits(body)
    if bits[n:].strip('0'): raise Reject('C: non-zero padding')
    return bits[:n]

# ---------- D (no length field)
def enc_D(words):
    return bits_to_bytes(payload_of(words) + '1')
def dec_D(bs):
    if not bs or bs[-1] == 0: raise Reject('D: empty or zero last byte')
    bits = bytes_to_bits(bs)
    k = bits.rfind('1')
    return bits[:k]

FR = {'A': (enc_A, dec_A), 'B': (enc_B, dec_B), 'C': (enc_C, dec_C), 'D': (enc_D, dec_D)}

def sequences(maxwords, maxwidth):
    words = [''.join(b) for k in range(1, maxwidth + 1) for b in itertools.product('01', repeat=k)]
    yield ()
    for n in range(1, maxwords + 1):
        yield from itertools.product(words, repeat=n)

def main():
    seqs = list(sequences(3, 4))
    print('sequences (0..3 words of 1..4 bits): %d' % len(seqs))
    for name in 'ABCD':
        enc, dec = FR[name]
        rt = tr_acc = zero_acc = pad_acc = 0
        frames = defaultdict(list)
        for q in seqs:
            f = enc(list(q)); frames[f].append(q)
            got = dec(f)
            exp = list(q) if name == 'B' else payload_of(q)
            if got != exp: rt += 1
            # truncation: every proper byte prefix must be rejected
            for cut in range(len(f)):
                try: dec(f[:cut]); tr_acc += 1
                except Reject: pass
            # appended zero byte(s)
            for extra in (1, 2):
                try: dec(f + bytes(extra)); zero_acc += 1
                except Reject: pass
            # non-zero padding: set one padding bit (if the frame has tail padding)
            p = payload_of(q)
            n = len(p) + (1 if name == 'D' else 0)
            pad = -n % 8
            if pad and name != 'D':
                b = bytearray(f); b[-1] |= 1
                try:
                    r = dec(bytes(b))
                    if r == (list(q) if name == 'B' else p): pad_acc += 1
                except Reject: pass
        shared = [v for v in frames.values() if len(v) > 1]
        seqs_in_shared = sum(len(v) for v in shared)
        print('\nFRAME %s' % name)
        print('  round-trip failures (%s):                         %d' % ('full sequence' if name == 'B' else 'payload bits', rt))
        print('  truncated (proper byte prefixes) ACCEPTED:       %d' % tr_acc)
        print('  appended zero byte(s) ACCEPTED (1 and 2 bytes):  %d' % zero_acc)
        print('  non-zero tail padding ACCEPTED as the same value: %d' % pad_acc)
        print('  distinct frames: %d; frames shared by >1 sequence (no widths given to the decoder): %d; sequences in them: %d' % (len(frames), len(shared), seqs_in_shared))
    # accounting on the issue's example
    ex = ['1', '01', '101', '011', '1100']
    p = payload_of(ex)
    print('\nACCOUNTING for 1 | 01 | 101 | 011 | 1100  (payload %d bits, payload bytes %d, tail unused bits %d)' % (len(p), -(-len(p) // 8), -len(p) % 8))
    for name in 'ABCD':
        f = FR[name][0](ex)
        pay_bytes = -(-len(p) // 8) if name != 'D' else -(-(len(p) + 1) // 8)
        print('  %s: total wire bytes %d (framing bytes %d), utilization %.3f' % (name, len(f), len(f) - pay_bytes, len(p) / (8 * len(f))))

if __name__ == '__main__':
    main()
