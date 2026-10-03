#!/usr/bin/env python3
"""Independent check of shiva-sutras PR #91 (upc7_sound.py: UPC-7 cell + language profile -> IPA projection) against its stated source
docs/sanskrit-ukrainian-sounds-2026-10-02.tsv. Expectations are read from that TSV (brackets [..] of ipa_sanskrit / ipa_ukrainian, the
confidence column), not from the module's own tables.
Usage: python3 review_upc7_sound_projection.py --proto <prototype of the #91 checkout> --tsv <docs/sanskrit-ukrainian-sounds-2026-10-02.tsv>
"""
import csv, re, sys, unicodedata
from pathlib import Path

def arg(n, d=None): return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
sys.path.insert(0, arg('--proto'))
import upc7_sound as S
from upc7_layouts import UPC7Text, ASSIGNED
nfc = lambda s: unicodedata.normalize('NFC', s)
rows = list(csv.DictReader(open(arg('--tsv'), encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
CONF = {'висока': 'high', 'середня': 'medium', 'низька': 'low'}
def ipas(cell): return {nfc(x) for x in re.findall(r'\[([^\]]+)\]', cell)}
issues = []
def flag(kind, msg):
    issues.append((kind, msg)); print(f'  {kind:<22}{msg}')

# TSV: sound(s) -> expected IPA sets and confidence, per profile
src = {'sa': {}, 'uk': {}}
for r in rows:
    names = [n.strip() for n in re.split(r'[ ,]+', r['sound'].split('(')[0]) if n.strip()] if r['sound'] not in ('ь (пом\'якшення)',) else []
    for n in names:
        src['sa'][nfc(n)] = (ipas(r['ipa_sanskrit']), r['confidence']); src['uk'][nfc(n)] = (ipas(r['ipa_ukrainian']), r['confidence'])
print('(1) every IPA symbol of the module against the TSV')
for prof, table in (('sa', S._SA_IPA), ('uk', S._UK_IPA)):
    for spelling, (pref, cands, conf) in table.items():
        key = nfc(spelling)
        if key not in src[prof]:
            # uk Cyrillic letters are listed as separate TSV rows only for а е о и х; others live inside the Sanskrit row (k, g, t d n ...)
            owner = {'к': 'k', 'ґ': 'g', 'т': 't', 'д': 'd', 'н': 'n', 'п': 'p', 'б': 'b', 'м': 'm', 'й': 'y', 'с': 's', 'р': 'r', 'л': 'l', 'в': 'v', 'і': 'i', 'у': 'u', 'г': 'h', 'ш': 'ś', 'ж': 'ж', 'з': 'ж', 'ц': 'ж', 'ф': 'ж', 'дз': 'ж', 'ч': 'c', 'дж': 'j'}.get(spelling)
            if owner is None or owner not in src[prof]:
                flag('NO SOURCE ROW', f'{prof} {spelling!r}: preferred {pref!r}, candidates {cands}, confidence {conf} — the TSV has no row for it'); continue
            key = owner
        ref, tconf = src[prof][key]
        syms = ([pref] if pref else []) + list(cands)
        if prof == 'uk' and key == 'ж': ref = {'ʒ', 'z', 't͡s', 'f', 'd͡z'}
        if prof == 'sa' and key in ('kh', 'gh'): pass
        miss = [nfc(s) for s in syms if nfc(s) not in {nfc(x) for x in ref}]
        if miss and not (prof == 'sa' and key in ('ṛ', 'ḷ')):
            flag('IPA NOT IN SOURCE', f'{prof} {spelling!r}: {miss} not among the TSV brackets {sorted(ref)} (row {key!r})')
        want = [CONF[w] for w in re.findall(r'(висока|середня|низька)', tconf)]
        if conf not in want and want and pref:
            flag('CONFIDENCE VS TSV', f'{prof} {spelling!r}: module says {conf!r} for the IPA symbol, TSV says {tconf!r}')
# aspirates: the TSV row says "high for the class, medium for the IPA"
asp = [(s, S._SA_IPA[s][2]) for s in ('kh', 'gh', 'ṭh', 'ḍh', 'th', 'dh', 'ph', 'bh') if s in S._SA_IPA]
print('     aspirates (TSV: high for the class, medium for the IPA symbol):', asp)
for s in ('ṝ', 'ḹ'):
    flag('NO SOURCE ROW', f'sa {s!r}: in the module ({S._SA_IPA[s]}) but the TSV has rows for ṛ and ḷ only (long forms by analogy)') if s in S._SA_IPA else None

print('\n(2) statuses against the facts')
codec = UPC7Text()
for prof in ('sa', 'uk'):
    tab = S.sound_table(prof); by = {}
    for p in tab: by.setdefault(p.status, []).append(p)
    print(f'  profile {prof}:', {k: len(v) for k, v in sorted(by.items())})
    reserved = [c for c in range(128) if codec.cells[c].status != ASSIGNED]
    bad = [c for c in reserved if tab[c].status != 'unassigned']
    print(f'    pinned reserved cells: {len(reserved)}; not marked unassigned: {bad}')
    if bad or len(reserved) != 21: flag('STATUS', f'{prof}: reserved cells {len(reserved)}, wrongly marked {bad}')
    sa_only = [p for p in tab if p.status == 'unsupported']
    print('    unsupported:', len(sa_only), [p.identity.split('.')[-1] for p in sa_only][:60])
    # every assigned phonological cell must have a status that matches its layout spelling
    for p in tab:
        sp = codec.layout('uk' if prof == 'uk' else 'sa-iast').code_to_spelling.get(p.code)
        if p.status in ('resolved', 'unresolved') and sp is None: flag('STATUS', f'{prof} cell {p.bits} {p.identity}: {p.status} without a spelling in the layout')
        if p.status == 'unsupported' and sp is not None: flag('STATUS', f'{prof} cell {p.bits} {p.identity}: unsupported although the layout spells it {sp!r}')
        if p.status == 'resolved' and p.ipa is None: flag('STATUS', f'{prof} {p.identity}: resolved with ipa None')
        if p.status == 'unresolved' and p.ipa is not None: flag('STATUS', f'{prof} {p.identity}: unresolved with ipa {p.ipa}')
    unres = [(p.spelling, p.ipa_candidates) for p in tab if p.status == 'unresolved']
    print('    unresolved:', unres)
    kinds = {}
    for p in tab: kinds.setdefault(p.kind, []).append(p.status)
    print('    kind -> statuses:', {k: sorted(set(v)) for k, v in kinds.items()})
    for p in tab:
        if p.kind == 'non-sound' and p.status != 'non-sound': flag('STATUS', f'{prof} {p.identity} kind non-sound but status {p.status}')
        if p.kind == 'phonological' and codec.cells[p.code].status == ASSIGNED and p.status in ('non-sound', 'unassigned'): flag('STATUS', f'{prof} {p.identity}: phonological but {p.status}')

print('\n(3) shared cells: different IPA by profile, same cell')
pair = [('ś', 'ш'), ('r', 'р'), ('l', 'л'), ('v', 'в'), ('h', 'г'), ('c', 'ч'), ('j', 'дж'), ('s', 'с'), ('t', 'т'), ('k', 'к'), ('y', 'й'), ('i', 'і'), ('u', 'у'), ('ṅ', None), ('a', 'а')]
for sa_s, uk_s in pair:
    cs = [c for c in range(128) if codec.layout('sa-iast').code_to_spelling.get(c) == sa_s]
    cu = [c for c in range(128) if uk_s and codec.layout('uk').code_to_spelling.get(c) == uk_s]
    if not cs: print(f'  {sa_s}: no sa-iast cell'); continue
    c = cs[0]; a = S.project_sound(c, 'sa'); b = S.project_sound(c, 'uk')
    same_cell = c in cu
    print(f'  cell {c:3d} sa {sa_s!r:>5} -> {a.status:<10} {str(a.ipa or a.ipa_candidates):<18}| uk {b.spelling!r:>5} -> {b.status:<10} {str(b.ipa or b.ipa_candidates):<18} shared cell with {uk_s!r}: {same_cell}')
    if uk_s and not same_cell: print(f'      note: {uk_s!r} is NOT on the cell of {sa_s!r} in the pinned layout (uk cell(s) {cu})')
print(f'\n{len(issues)} issues flagged')
