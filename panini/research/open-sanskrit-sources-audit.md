# Open Sanskrit sources audit: selection policy

Status: `PANINI-OPEN-SANSKRIT-SOURCES-FULL-AUDIT`, 2026-08-13. This audit
selects sources for Panini Foundation and a future My Lisp bridge. It does not
import any corpus, change a registry, or license third-party material for reuse.

## [PANINI]

No digital project, implementation, translation, or treebank is identical with
Pāṇini's grammar. For a claim about the Aṣṭādhyāyī, the required evidence chain
remains: sūtra text → identified commentary/tradition where needed → a clearly
labeled modern interpretation. Datasets may test an implementation; they do
not settle the historical interpretation of a rule.

## Selection matrix

| Source | Asset and format | License/status found | Project role | Decision |
|---|---|---|---|---|
| [Ashtadhyayi.com](https://ashtadhyayi.com/) | searchable sūtras plus named commentary panels | digital reading service; edition policy must be checked per claim | fast navigation and locator discovery | **use as navigation, cross-check important claims** |
| [Vidyut](https://github.com/ambuda-org/vidyut) | Rust `vidyut-prakriya`; structured term, rule, step, decision model | active open-source project | independent implementation oracle | **use for code-level comparison, never as textual authority** |
| [CDSL / Sanskrit Lexicon](https://github.com/sanskrit-lexicon) | dictionaries; Cologne source data and SLP1 transcoding workflow | individual repositories declare licenses; MWS is CC-BY-SA-4.0 | lexical IDs, normalization, dictionary provenance | **adopt compatibility tests; import only per-repository license review** |
| [ambuda-dcs](https://github.com/ambuda-org/dcs) / DCS | sanitized annotated corpus | CC-BY 4.0 stated by repository | later conformance and disambiguation corpus | **adopt after Phase 1, preserve corpus version and annotation provenance** |
| [Sanskrit Heritage](https://sanskrit.inria.fr/) | independent morphology, segmentation, parsing tradition | engine/wrapper/data terms differ; wrappers GPLv3 and data may be CeCILL-C | independent behavioural comparison | **use as oracle; do not vendor binaries/data before license review** |
| [SARIT](https://sarit.github.io/) | TEI-encoded Sanskrit/Prakrit editions with edit history | texts state Creative Commons licensing | textual-source and TEI-model study | **use selected editions after edition/license review** |
| [UD Sanskrit](https://universaldependencies.org/sa/index.html) | CoNLL-U syntax; UFAL and Vedic treebanks | Vedic treebank CC-BY-SA-4.0 | later sentence analysis evaluation | **defer to Phase 2; never equate UD labels with kāraka** |
| [Panini-NLP](https://pypi.org/project/panini-nlp/) | Python registry/graph/sandhi claims | MIT, development status Alpha; releases 0.1/0.2 were yanked | experimental architecture comparison | **read-only experimental reference; no source-of-truth status** |
| [GRETIL](https://gretil.sub.uni-goettingen.de/gretinfobk.htm) | discovery register for scholarly e-texts, varied encodings | availability for scholarship is not a blanket reuse license | bibliographic discovery | **discovery only until title-level rights and text quality are audited** |
| [Sanskrit Documents](https://sanskritdocuments.org/) | volunteer text collection, multiple scripts | personal study/research; explicitly prohibits repost/commercial use without permission | human consultation | **do not ingest, redistribute, or use as training corpus** |
| [AI4Bharat Indic NLP catalog](https://github.com/AI4Bharat/indicnlp_catalog) | directory of tools and resources | catalog, not a Sanskrit corpus or authority | discovery | **watchlist only** |

## Evidence notes

### 1. Canonical spelling and lexical data

The strongest immediately useful path is CDSL's source-oriented workflow, not
a copied dictionary dump. The MWS repository states that canonical `mw.txt`
is SLP1 in `csl-orig`, provides SLP1/IAST/Devanāgarī transcoding tooling, and
keeps corrections as versioned change files. This supports our SLP1 policy and
our new provenance contract. It does **not** make Monier-Williams a Dhātupāṭha
authority or settle a root's gaṇa.

### 2. Derivation and morphology

Vidyut and Sanskrit Heritage are complementary independent computational
traditions. Vidyut is valuable for its explicit term lifecycle and derivation
history; Heritage is valuable as an independent morphology/segmentation/
analysis oracle. Agreement between them is useful test evidence, not proof of
a Pāṇinian claim; disagreement must be stored as alternatives with provenance.

### 3. Texts and annotation corpora

SARIT is more suitable than a generic plain-text dump when an edition and
textual variation matter because it supplies TEI markup and edit history. DCS
is the preferred later evaluation corpus because its sanitized repository states
CC-BY 4.0 and carries morphological/lexical annotation. UD treebanks become
useful only at sentence-analysis time. Their `nsubj`, `obj`, and `obl` labels
are a different annotation theory and must not be mechanically renamed to
`kartf`, `karman`, or other kāraka.

### 4. Sources excluded from machine ingestion

GRETIL indexes material with heterogeneous encoding and rights, and its
e-library warns that PDF background OCR is not proofread. Sanskrit Documents
expressly limits files to personal study/research and prohibits copying or
reposting without permission. Both are useful to locate material or inspect it
as humans; neither enters a repository dataset or training/evaluation corpus
without title-level clearance and quality review.

## Acquisition protocol

Before any future import, create one `ProvenanceRecord` per artifact with:

```yaml
id: prov:external:<provider>:<artifact>:<revision>
claim_kind: implementation | lexical-record | source-text | corpus
layer: interpretation
subject: { kind: external-artifact, id: <provider-and-revision> }
evidence:
  - kind: manual-review
    ref: <license-url-or-repository-license>
    locator: <commit-tag-release-or-edition>
    status: verified
    checked_on: YYYY-MM-DD
license: <SPDX-or-provider-terms>
normalization: original | slp1-normalized | devanagari-normalized
allowed_use: navigation | comparison | test | import-pending
```

Never normalize an imported text destructively. Store source encoding,
conversion program/version, and a reversible mapping or checksum. Never mix
corpus annotations with `[PANINI]` claims.

## Roadmap for our language

1. **Now:** Ashtadhyayi.com for navigation; CDSL for SLP1 compatibility;
   Vidyut + Heritage for independent implementation comparison.
2. **After machine trace is executable:** a small manually chosen DCS slice as
   external conformance data, with immutable artifact revision.
3. **After sentence layer is designed:** UD Sanskrit and DCS for evaluation of
   mappings, explicitly retaining a Paninian-to-UD conversion layer.
4. **Never by default:** copy bulk texts, dictionary data, or model outputs
   merely because they are publicly reachable.

## Українська

Головний результат аудиту: для нашої мови потрібна не «одна база санскриту», а
контрольована комбінація незалежних ролей.

- **Навігація до sūtra:** Ashtadhyayi.com; важливий висновок завжди звіряємо
  окремо, сайт не замінює критичне видання.
- **Канонічний SLP1 і лексична сумісність:** Cologne Digital Sanskrit
  Dictionaries / Sanskrit Lexicon. Їхній versioned correction workflow добре
  узгоджується з нашим provenance підходом.
- **Морфологічні implementation-oracles:** Vidyut та Sanskrit Heritage.
  Порівнюємо їхні результати, але не оголошуємо реалізацію історичним доказом.
- **Майбутня перевірка речень:** DCS і UD Sanskrit після появи sentence layer.
  UD dependency labels не є kāraka й потребують окремого mapping.
- **Лише discovery або заборона на імпорт:** GRETIL, Sanskrit Documents,
  AI4Bharat catalog — через неоднорідні права, OCR/encoding або каталоговий
  характер.

Кожний зовнішній артефакт до імпорту мусить отримати provenance ID, revision,
ліцензію, source encoding і дозволений тип використання. Ми не перетворюємо
відкритість URL на дозвіл копіювати дані.

## Deutsch

Das Auditergebnis: Für unsere Sprache brauchen wir keine einzige
"Sanskrit-Datenbank", sondern eine kontrollierte Kombination unabhängiger
Rollen.

- **Sūtra-Navigation:** Ashtadhyayi.com; wichtige Aussagen werden unabhängig
  geprüft, die Website ersetzt keine kritische Edition.
- **Kanonisches SLP1 und lexikalische Kompatibilität:** Cologne Digital Sanskrit
  Dictionaries / Sanskrit Lexicon mit versioniertem Korrekturworkflow.
- **Morphologische Implementierungsorakel:** Vidyut und Sanskrit Heritage;
  Ergebnisse werden verglichen, aber nie als historische Beweise ausgegeben.
- **Spätere Satzprüfung:** DCS und UD Sanskrit. UD-Dependency-Labels sind nicht
  mit kāraka identisch und benötigen eine eigene Mapping-Schicht.
- **Nur Discovery oder kein Import:** GRETIL, Sanskrit Documents und der
  AI4Bharat-Katalog wegen heterogener Rechte, OCR/Encoding oder Katalogstatus.

Jedes externe Artefakt braucht vor dem Import Provenienz-ID, Revision, Lizenz,
Quellencoding und erlaubte Nutzung. Eine öffentliche URL ist keine Erlaubnis,
Daten zu kopieren.
