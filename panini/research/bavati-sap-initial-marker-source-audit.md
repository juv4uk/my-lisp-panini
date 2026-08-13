# Bhavati: initial Ś of Śap source audit

Status: `PANINI-BAVATI-SAP-INITIAL-MARKER-SOURCE-AUDIT`. This resolves one
identified source blocker in the Bhavati readiness audit. It does not by itself
make the full Bhavati derivation complete or authorize a runtime change.

## [PANINI]

The initial `S` of the affix `Sap` is not established by 1.3.7 `cuTU`.
The relevant rule is 1.3.8 `laSakvatadDite`: with its inherited conditions,
an initial `l`, `S`, or velar of a non-taddhita affix receives `it`-saṃjñā.
The commentary-facing page explicitly gives `kartari Sap` as an example of
the initial `S` case. Under 1.3.9 `tasya lopaH`, the marked sound undergoes
lopa; the terminal `p` has its own `halantyam` (1.3.3) path.

Rule 3.4.113 `tiNSitsArvaDAtukam` supplies the relevant designation:
tiṅ affixes and `Sit` affixes are `sArvaDAtuka`. Its presented commentary
examples include `bhavati`. Rule 7.3.84 then concerns guṇa of an `iganta`
aṅga before a `sArvaDAtuka` or `ArDaDAtuka` affix; the cited commentary
presents `bhavati` among its examples.

This establishes a source path for the three distinct statements; it does not
say that any of the project record field names occur in the source text.

## [INTERPRETATION]

The prior teaching text conflated two matters:

1. it attributed initial `S` of `Sap` to 1.3.7, although the appropriate
   source path is 1.3.8; and
2. it described the residual surface `a` as if it itself “inherited a tag”.

A more faithful project reading is that the *affix occurrence* has an
evidence-backed `Sit`/`sArvaDAtuka` designation while its `it` sounds are
removed from the represented surface. The designation is neither the literal
surface `a` nor a claim that an `it` letter equals compiler metadata.

## [MY-LISP HYPOTHESIS]

### Corrected bounded record

```yaml
term: term:vikarana-Sap
source_form: Sap
surface_form: a
designations:
  - id: it
    basis: "1.3.8"
    target: initial-S
    provenance: [prov:sutra:1.3.8-text]
  - id: it
    basis: "1.3.3"
    target: final-p
    provenance: [prov:sutra:1.3.3-text]
  - id: sArvaDAtuka
    basis: "3.4.113"
    target: affix-occurrence
    provenance: [prov:sutra:3.4.113-text]
transitions:
  - { rule: "1.3.9", operation: remove-marked-sound, target: initial-S }
  - { rule: "1.3.9", operation: remove-marked-sound, target: final-p }
```

`designations` above are a project evidence representation. It must not be
implemented as an unscoped Boolean attached only to the display string `a`.
The same term identity retains `source_form: Sap` while its current form is
`a`; an immutable state transition records that difference.

### Consequences for Bhavati readiness

| Earlier unknown | Status after this audit |
| --- | --- |
| source account of initial `S` in `Sap` | resolved for the cited source path: 1.3.8 |
| `sArvaDAtuka` bridge | resolved as a designation path: 3.4.113 |
| full applicability and all immutable transitions | still partial |
| complete historical derivation | not established |

The old `Bavati.md` wording should be corrected by a dedicated documentation
task. This audit deliberately leaves it untouched so that the correction can
identify the changed claim and its provenance explicitly.

Sources: [1.3.8 with inherited conditions and examples](https://ashtadhyayi.com/sutraani/1/3/8),
[1.3.8 commentary and description](https://sanskritdictionary.com/panini/1-3-8),
[3.4.113 tiṅśit sārvadhātukam](https://sanskritdictionary.com/panini/3-4-113),
and [7.3.84 commentary including *bhavati*](https://sanskritdictionary.com/panini/7-3-84).

## English summary

The initial `S` of `Sap` is an it marker through 1.3.8, not 1.3.7; 3.4.113
provides the `sArvaDAtuka` designation. The surviving surface `a` must not be
mistaken for the designated affix occurrence or for a metadata tag.

## Українська

Початковий `S` у `Sap` є it marker через 1.3.8, а не 1.3.7; 3.4.113 надає
designation `sArvaDAtuka`. Збережений surface `a` не можна вважати ні самим
designated affix occurrence, ні metadata tag.

Нормативно: у Derivation IR треба зберегти одну term identity з
`source_form: Sap`, `surface_form: a`, окремими it-designations для `S` і
`p`, окремим `sArvaDAtuka` designation та двома provenance-bearing lopa
transitions. Це закриває конкретний source blocker `Bavati`, але не робить
увесь trace complete: застосовність, state hashes і решта переходів ще мають
окремо пройти evidence gates.

## Deutsch

Das initiale `S` von `Sap` ist durch 1.3.8 ein it-Marker, nicht durch 1.3.7;
3.4.113 liefert die Designation `sArvaDAtuka`. Das verbleibende Oberflächen-
`a` darf weder mit der designierten Affix-Occurrence noch mit einem
Metadaten-Tag verwechselt werden.
