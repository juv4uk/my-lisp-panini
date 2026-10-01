#!/usr/bin/env python3
"""First-pass, read-only inventory of 'function identity is exactly 8 bits' assumptions (SENS #1970).

Heuristic: precise patterns (NOT the generic number 256) + path-based classification into the issue's classes.
Output: TSV (path, line, pattern, class, bucket, snippet) and a summary. It never modifies the scanned repo.
The class/bucket are HEURISTIC labels to be confirmed by a human; precision is measured on a hand-checked sample.

Usage: python3 inventory_function8.py /path/to/sens [--tsv out.tsv] [--sample N --seed S]
"""
import os, re, sys, random
from collections import Counter

PATTERNS = [
    ('type-name',    re.compile(r'\b(Function8|Sid8|SID8|Sens8)\b')),
    ('bitstring-8',  re.compile(r'\[01\]\{8\}|\[0-9a-fA-F\]\{2\}|\{8\}')),
    ('len-eq-8',     re.compile(r'\.len\(\)\s*[!=]=\s*8\b|\blen\s*[!=]=\s*8\b|len\([^)]*\)\s*[!=]=\s*8\b')),
    ('array-256',    re.compile(r'\[\s*(?:u8|[A-Za-z_][A-Za-z0-9_<>]*)\s*;\s*256\s*\]|\bFUNCTION_TABLE_SIZE\b|\b256-entry\b|\b256 entries\b')),
    ('phrase-8bit',  re.compile(r'exactly 8 bits|exactly eight bits|all functions are (?:exactly )?(?:8|eight)|8-bit function|function identity is (?:exactly )?8', re.I)),
]
EXT = ('.rs', '.lisp', '.md', '.yml', '.yaml', '.toml', '.py', '.sh')
SKIP = ('/target/', '/.git/', '/node_modules/', '/HEAD/', '/vendor/', '/third_party/', '/external/')

def classify(path, pat, line):
    p = path.lower()
    if p.endswith('.md') or '/docs/' in p or 'changelog' in p: return 'docs/history', 'historical-only'
    if '/tests/' in p or '/test_' in p or p.endswith('_test.rs') or '/benches/' in p and False: return 'test-only', 'can-remain-as-compatibility'
    if 'bench' in p or 'profil' in p: return 'profiling/index optimization', 'backend-only-safe'
    if 'fasl' in p or 'wire' in p or 'binary_framing' in p or 'framing' in p: return 'FASL/wire compatibility', 'must-change-before-variable-width'
    if 'generated' in p or p.endswith('_table.rs') or 'table' in os.path.basename(p): return 'generated table', 'can-remain-as-compatibility'
    if '/parser' in p or '/ast' in p or 'lexer' in p or 'reader' in p or p.endswith('/syntax.rs'): return 'parser/AST shape', 'must-change-before-variable-width'
    if '/eval' in p or '/runtime' in p or 'dispatch' in p or '/vm' in p or 'semantic_registry' in p: return 'runtime dispatch mechanism', 'can-remain-as-compatibility'
    if '.github' in p or p.endswith('.yml') or p.endswith('.yaml'): return 'semantic-guard', 'unknown'   # CI guards / ratchets
    if pat == 'phrase-8bit': return 'semantic-guard', 'unknown'
    return 'unknown', 'unknown'

def scan(root):
    rows = []
    for dp, dn, fn in os.walk(root):
        full = dp + '/'
        if any(s in full for s in SKIP): dn[:] = []; continue
        for f in fn:
            if not f.endswith(EXT): continue
            path = os.path.join(dp, f)
            try: text = open(path, encoding='utf-8', errors='ignore').read().split('\n')
            except Exception: continue
            for i, line in enumerate(text, 1):
                for name, rx in PATTERNS:
                    if rx.search(line):
                        c, b = classify(path.replace(root, ''), name, line)
                        rows.append((path.replace(root, '').lstrip('/'), i, name, c, b, line.strip()[:140]))
                        break
    return rows

def main():
    root = os.path.abspath(sys.argv[1])
    rows = scan(root)
    out = sys.argv[sys.argv.index('--tsv') + 1] if '--tsv' in sys.argv else None
    if out:
        with open(out, 'w', encoding='utf-8') as f:
            f.write('path\tline\tpattern\tclass\tbucket\tsnippet\n')
            for r in rows: f.write('\t'.join(str(x).replace('\t', ' ') for x in r) + '\n')
    print('occurrences: %d in %d files' % (len(rows), len({r[0] for r in rows})))
    print('by class :', dict(Counter(r[3] for r in rows).most_common()))
    print('by bucket:', dict(Counter(r[4] for r in rows).most_common()))
    print('by pattern:', dict(Counter(r[2] for r in rows).most_common()))
    if '--sample' in sys.argv:
        n = int(sys.argv[sys.argv.index('--sample') + 1]); seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
        random.seed(seed)
        for r in random.sample(rows, min(n, len(rows))): print('%-60s %5d  %-12s | %-28s | %s' % (r[0][-60:], r[1], r[2], r[3], r[5][:90]))

if __name__ == '__main__':
    main()
