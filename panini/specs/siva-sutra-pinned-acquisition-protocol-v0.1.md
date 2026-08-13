# Śiva Sūtra pinned acquisition protocol v0.1

Status: acquisition policy for `PANINI-SIVA-SUTRA-PINNED-ACQUISITION-PROTOCOL`.
It creates no network build dependency and imports no source text by itself.

## [PANINI]

An acquired digital presentation is evidence about a particular edition or
presentation, not identical with the Pāṇinian object of study. This protocol’s
hashes, file paths, and licences are project metadata; they are not Pāṇinian
categories.

## [INTERPRETATION]

A stable URL is not an immutable source. A web page may be revised without
changing its URL; conversely, a local hash pins bytes but says nothing by itself
about editorial quality. Reproducibility therefore requires both a source
locator and a content-addressed acquisition record, while responsible reuse
also requires a separately recorded licence and attribution.

## [MY-LISP HYPOTHESIS]

### Preconditions

An acquisition may start only after a rights review records:

1. the source identifies the **fourteen phoneme-ordering** Śiva/Māheśvara
   Sūtras rather than the Kashmir Śaiva work with the similar title;
2. a licence permits the intended project use;
3. the source’s title, canonical URL, retrieval date, licence URL, and required
   attribution are known;
4. the acquisition is deliberate and one-off, never a test-time network fetch.

The current candidate is recorded in `research/siva-sutra-source-rights-review.md`.
It is eligible for this protocol but has **not** been acquired by this task.

### Acquisition record

```yaml
id: acquisition:siva-sutras:<source-key>:<UTC-timestamp>
subject: siva-sutras-phoneme-ordering
source:
  title: <verbatim source title>
  canonical_url: <https URL>
  retrieved_at: YYYY-MM-DDTHH:MM:SSZ
  publisher_revision: <tag|commit|date|none>
rights:
  license: <SPDX-or-human-identifier>
  license_url: <canonical licence URL>
  attribution: <required credit text>
  reuse_status: permitted | restricted | unresolved
artifact:
  local_path: sources/siva-sutras/<filename>
  sha256: <64 lowercase hex characters>
  media_type: text/html | application/pdf | text/plain
  byte_count: <positive integer>
  fetch_method: manual-browser-download | reviewed-command
conversion:
  input_representation: devanagari | IAST | other
  output_representation: SLP1
  converter: manual-checked | tool:<name>@<revision>
  conversion_record: conversion:siva-sutras:<stable-key>
verification:
  row_check: pending | pass | fail
  compared_to:
    - registry/siva-sutras/siva-sutras-slp1-provisional-v0.1.yaml
    - tests/pratyahara-exhaustive-v0.1.yaml
  reviewer: <human-or-agent-id>
status: acquired | verified | rejected | superseded
```

The local artifact is private acquisition evidence until its licence and
repository inclusion are separately reviewed. A hash may be committed without
committing restricted source bytes.

### Conversion record

```yaml
id: conversion:siva-sutras:<stable-key>
input_acquisition: acquisition:siva-sutras:<source-key>:<UTC-timestamp>
method: manual-checked | deterministic-tool
tool:
  name: <name>|null
  revision: <version-or-commit>|null
  invocation: <exact non-network command>|null
rows:
  - ordinal: 1
    source_locator: <page/line/table-cell>
    source_value: <display transcription>
    slp1_sounds: [a, i, u]
    slp1_marker: R
    check: pass | fail | unresolved
overall: pass | fail | unresolved
notes: <ambiguity, editorial variant, or display limitation>
```

Manual conversion remains allowed because display layouts may not be
machine-readable, but every row must be independently inspectable. A tool
cannot be treated as an oracle for the source’s text merely because conversion
round-trips successfully.

### Admission gates

```text
rights review passed
       ↓
one-off source acquisition + SHA-256
       ↓
attribution and licence record complete
       ↓
all 14 rows checked against two local comparison artifacts
       ↓
conversion record reviewed
       ↓
eligible evidence for a separate machine-alignment gate
```

Failure at any stage leaves `machine_input_status: prohibited`. Passing this
protocol only creates evidence eligibility. The later
`PANINI-MACHINE-SIVA-SUTRA-ALIGNMENT-GATE` must still decide whether a machine
representation correctly references the verified project conversion.

### Negative cases

1. A URL, citation, or screenshot without source bytes/hash is not pinned.
2. A SHA-256 without URL, retrieval time, and rights record is not attributable.
3. A permissive software licence for a parser does not license grammar text or
   table data.
4. A conversion that matches thirteen rows but leaves one marker unresolved is
   `overall: unresolved`, not pass.
5. A web fetch during test execution violates this protocol even if its hash
   happens to match a previous acquisition.

## English summary

This protocol separates rights, byte-level pinning, conversion, and row-level
verification. Passing it makes a source acquisition eligible evidence, not
automatic runtime input or a claim about Pāṇini’s own data model.

## Українська

Цей протокол відокремлює права, фіксацію bytes/hash, конверсію та перевірку
кожного рядка. Його проходження робить придбаний source artifact придатним
доказом, але не автоматичним runtime input і не твердженням про власну модель
даних Паніні.

Нормативно: жодного мережевого fetch під час тесту; hash без URL, часу
отримання, licence та attribution не є достатнім; неперевірений хоча б один із
14 рядків зберігає статус `unresolved`. Навіть повністю перевірений acquisition
лише відкриває окремий machine-alignment gate.

## Deutsch

Dieses Protokoll trennt Rechte, Byte-Pinning per Hash, Konversion und die
Prüfung jeder Zeile. Sein Bestehen macht eine Quellenakquisition zu zulässiger
Evidenz, jedoch weder automatisch zu Runtime-Input noch zu einer Behauptung
über Pāṇinis eigenes Datenmodell.
