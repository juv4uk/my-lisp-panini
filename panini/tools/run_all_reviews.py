#!/usr/bin/env python3
"""Run every independent review/oracle of the UPC-14/UPC-7 lab against ONE shiva-sutras checkout and print a table: command, exit code, seconds, last lines.
Usage: python3 run_all_reviews.py --proto <shiva-sutras/prototype> --dict <dict_uk base.lst> --verses <sanskrit_embeddings.jsonl> [--log DIR] [--jobs 4]
A non-zero exit or a line starting with DEFECT/FAIL is reported as such; 'exit 0' alone means the script finished, read its last lines for what it checked."""
import concurrent.futures as cf, subprocess, sys, time
from pathlib import Path

def arg(n, d=None): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
P, D, V = arg('--proto'), arg('--dict'), arg('--verses'); LOG = Path(arg('--log', '.')); JOBS = int(arg('--jobs', '4'))
H = Path(__file__).resolve().parent
CMDS = [
    ('second_impl_pratyahara_savarna', ['--graph', P]),
    ('review_upc14_consonant_sandhi', ['--graph', P]),
    ('review_upc14_natva', ['--graph', P]),
    ('review_upc14_pluta_codec', ['--graph', P]),
    ('review_uk_orthography', ['--graph', P, '--lst', D]),
    ('review_upc7_affine_shift', ['--graph', P]),
    ('review_upc7_gf2_linear', ['--graph', P]),
    ('review_upc7_nasal_deltas', ['--graph', P]),
    ('review_upc7_digits', ['--proto', P]),
    ('review_upc7_shared53_attack', ['--proto', P]),
    ('review_upc7_failclosed_render', ['--proto', P, '--dict', D, '--verses', V, '--n', '20000']),
    ('review_upc7_punct7_attack', ['--proto', P]),
    ('review_d7_relabel_attack', ['--proto', P]),
]
def run(item):
    name, args = item; t = time.time()
    r = subprocess.run([sys.executable, str(H / (name + '.py'))] + args, capture_output=True, text=True, timeout=3000)
    out = r.stdout + r.stderr; (LOG / (name + '.log')).write_text(out, encoding='utf-8')
    lines = [l for l in out.strip().split('\n') if l.strip()]
    flag = [l for l in lines if l.startswith(('DEFECT', 'FAIL'))]
    return name, r.returncode, time.time() - t, flag, lines[-2:]
LOG.mkdir(parents=True, exist_ok=True)
with cf.ThreadPoolExecutor(JOBS) as ex:
    for name, rc, sec, flag, tail in ex.map(run, CMDS):
        print(f'{name:<34} exit {rc}  {sec:6.1f}s  defect/fail lines: {len(flag)}')
        for l in flag[:3]: print('     ' + l[:200])
        for l in tail: print('   | ' + l[:200])
