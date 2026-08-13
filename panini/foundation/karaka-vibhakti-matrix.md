# Kāraka and vibhakti: an evidence-bounded matrix

## English

This is a matrix of relations, not equivalences: `kAraka` analyzes an action
relation, whereas `vibhakti` is a case-form category. Definitions occur under
`kArake` (1.4.23); cited assignments occur separately in 2.3. Thus no
universal conversion such as `kartf = nominative` follows. The matrix records
only stated, provenance-bounded assignments; its local-index citations are not
upgraded into external verification by this document.

## Українська

Це матриця відношень, а не еквівалентностей: `kAraka` аналізує відношення в
дії, тоді як `vibhakti` є категорією відмінкової форми. Означення містяться
під `kArake` (1.4.23), а наведені призначення — окремо в 2.3. Тому з неї не
випливає універсальна конверсія на кшталт `kartf = nominative`. Матриця
фіксує лише явно задані призначення з обмеженим provenance; local-index
цитати не стають зовнішньо верифікованими лише через цей документ.

## Deutsch

Dies ist eine Relationsmatrix, keine Äquivalenztabelle: `kAraka` analysiert
eine Handlungsrelation, `vibhakti` ist dagegen eine Kasusformkategorie. Die
Definitionen stehen unter `kArake` (1.4.23), die angeführten Zuweisungen
getrennt in 2.3. Daher folgt keine universelle Umrechnung wie
`kartf = nominative`. Die Matrix hält nur explizit genannte, durch Provenienz
begrenzte Zuweisungen fest; local-index-Zitate werden durch dieses Dokument
nicht zu extern verifizierten Zitaten.

Status: research note (`PANINI-KARAKA-CASE-MAPPING-MATRIX`).

This is deliberately a **matrix of relations**, not a table of equivalences.
`kAraka` labels a relation in the analysis of an action; `vibhakti` is a
case-form category. The sūtras below state case assignments under their own
conditions. They do not license a universal conversion such as
`kartf = nominative` or `karman = accusative`.

## [PANINI]

The definitions of the six core kāraka categories occur under the heading
`kArake` (1.4.23). The case-assignment rules cited below occur separately in
2.3. The split is material: a kāraka definition and a case rule are different
claims and must be represented as different source records.

| kāraka | defining source | explicit vibhakti rule in the local corpus | limited result |
|---|---|---|---|
| `karman` | 1.4.49 (and its extensions) | 2.3.2 `karmaRi dvitIyA` | accusative is explicitly assigned in the stated `karman` context |
| `sampradAna` | 1.4.32 | 2.3.13 `caturTI sampradAne` | dative is explicitly assigned in the stated context |
| `kartf` | 1.4.54 | 2.3.18 `kartfkaraRayostftIyA` | instrumental is explicitly assigned for `kartf` in this rule's context; this is already enough to refute a universal nominative equation |
| `karaRa` | 1.4.42 | 2.3.18 `kartfkaraRayostftIyA` | instrumental is explicitly assigned in the stated context |
| `apAdAna` | 1.4.24 and extensions such as 1.4.25 | 2.3.28 `apAdAne paYcamI` | ablative is explicitly assigned in the stated context |
| `aDikaraRa` | 1.4.45 | 2.3.36 `saptamyaDikaraRe ca` | locative is explicitly assigned in the stated context |

Sūtra 2.3.46 (`prAtipadikArTaliNgaparimARavacanamAtre praTamA`) is recorded
here as a separate first-case rule. It must not be silently rewritten as a
definition of `kartf` or as a general kāraka-to-case rule.

The 2.3 citations are present in the committed local `registry/sutras/index.yaml`.
They are marked `local-index` in the citation provenance registry pending a
recorded external text check; this note does not upgrade that status.

## [INTERPRETATION]

The common pedagogical active/passive contrast is useful only when presented
as an interpretation layer:

| construction sketch | stable observation | prohibited shortcut |
|---|---|---|
| active `pac` clause | a participant classified as `karman` can appear with the accusative rule 2.3.2 | “accusative *is* karman” |
| passive `pac` clause | the same semantic participant need not retain the same surface case as in the active clause | “case alone recovers kāraka” |
| causative | more than one action-related participant can require a distinction such as causee/instigator in traditional analysis | “every doer is simply `kartf`” |
| fear predicate such as `BI` | 1.4.25 extends `apAdAna` to a fear-causing participant | “ablative is only physical source/separation” |

These sketches are guardrails for analysis, not fully derived sentence
paradigms. A complete derivation must provide its terms, applicable rules,
anuvṛtti/adhikāra context, rule order, and source state.

## [MY-LISP HYPOTHESIS]

If a later machine model records both layers, it should use distinct fields:

```yaml
relation: karman                 # Paninian analysis, with source ID
surface_case: dvitIyA            # morphology, with its own source ID
link_status: rule-conditioned    # never an identity assertion
```

No inference engine should infer `karman` from `dvitIyA` alone, nor infer a
case form from a kāraka label without selecting the relevant construction and
rules. This is a design constraint, not an assertion about Pāṇini.

## Sources and follow-up

- [Kāraka foundation](karaka.md) — category definitions and cautions.
- [dhātu ↔ kāraka examples](../examples/derivations/dhatu-karaka-relation.md)
  — the `BI`/`apAdAna` extension and `dA`/`sampradAna` examples.
- `registry/sutras/index.yaml` — local text fields for 2.3.2, 2.3.13,
  2.3.18, 2.3.28, 2.3.36, and 2.3.46.
- `registry/sutras/citation-provenance.yaml` — required source-status layer.

The next required work is a source-checked active/passive/causative trace;
until then, do not treat the construction sketches as an executable grammar.
