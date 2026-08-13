# Trace canonical serialization contract v0.1 / Контракт канонічної серіалізації trace v0.1 / Vertrag zur kanonischen Trace-Serialisierung v0.1

## English

### Status and purpose

**Proposed machine contract.** It fixes byte-level reproducibility for
content-addressed Derivation IR states; it makes no claim about Pāṇini. Equal
semantic states must serialize to equal bytes and equal SHA-256 digests on all
hosts, so `state:sha256:<digest>` is reproducible evidence.

### Contract

- Serialize as compact UTF-8 JSON: no indentation or trailing whitespace, one
  LF terminator, no BOM, and NFC-normalized strings.
- Sort map keys lexicographically by UTF-8 bytes. Preserve authored `terms`
  array order; sort `relations` by relation kind, subject ID, object ID, index.
- Exclude presentation and narrative fields (`display_*`, `note`, `comment`,
  `local_path`, timestamps, provenance prose) from state bytes.
- Use lowercase-hex SHA-256 with `state:sha256:` prefix.
- A canonical state must be recomputed and rejected on any digest mismatch.
  Legacy `fixture-sexpr-not-hashed` remains structural evidence only.

### Status vocabulary

`trace_status` is trace-level (`complete | partial | omitted | invalid`);
IR `result.status` is result-level (`success | partial | blocked | invalid`).
They are distinct machine-contract vocabularies, not Pāṇinian categories.

## Українська

### Статус і призначення

**Запропонований машинний контракт.** Він фіксує байтову відтворюваність
content-addressed Derivation IR states і не робить твердження про Паніні.
Однакові семантичні стани мусять серіалізуватися в однакові bytes та SHA-256
digests на всіх hosts, тому `state:sha256:<digest>` є відтворюваним evidence.

### Контракт

- Серіалізувати як compact UTF-8 JSON: без indentation і trailing whitespace,
  з одним LF terminator, без BOM і з NFC-normalized strings.
- Сортувати map keys лексикографічно за UTF-8 bytes. Зберігати authored порядок
  масиву `terms`; сортувати `relations` за relation kind, subject ID, object
  ID, index.
- Виключати presentation і narrative fields (`display_*`, `note`, `comment`,
  `local_path`, timestamps, provenance prose) з state bytes.
- Використовувати lowercase-hex SHA-256 з prefix `state:sha256:`.
- Канонічний state мусить бути обчислений повторно й відхилений за будь-якої
  невідповідності digest. Legacy `fixture-sexpr-not-hashed` лишається лише
  structural evidence.

### Словник статусів

`trace_status` є trace-level (`complete | partial | omitted | invalid`), а IR
`result.status` — result-level (`success | partial | blocked | invalid`). Це
різні словники machine contract, а не категорії Паніні.

## Deutsch

### Status und Zweck

**Vorgeschlagener Maschinenvertrag.** Er legt die Byte-Reproduzierbarkeit
content-addressierter Derivation-IR-Zustände fest und behauptet nichts über
Pāṇini. Gleiche semantische Zustände müssen auf allen Hosts gleiche Bytes und
SHA-256-Digests liefern; damit ist `state:sha256:<digest>` reproduzierbare
Evidenz.

### Vertrag

- Als kompaktes UTF-8-JSON serialisieren: keine Einrückung oder nachgestellten
  Leerzeichen, ein LF-Terminator, kein BOM und NFC-normalisierte Strings.
- Map-Keys lexikographisch nach UTF-8-Bytes sortieren. Die verfasste
  `terms`-Arrayreihenfolge erhalten; `relations` nach Relationstyp, Subjekt-ID,
  Objekt-ID und Index sortieren.
- Präsentations- und Narrative-Felder (`display_*`, `note`, `comment`,
  `local_path`, Zeitstempel, Provenienzprosa) aus den State-Bytes ausschließen.
- SHA-256 in Kleinbuchstaben-Hex mit Präfix `state:sha256:` verwenden.
- Ein kanonischer State muss neu berechnet und bei jeder Digest-Abweichung
  abgelehnt werden. Legacy `fixture-sexpr-not-hashed` bleibt nur strukturelle
  Evidenz.

### Statusvokabular

`trace_status` ist Trace-Ebene (`complete | partial | omitted | invalid`);
IR `result.status` ist Ergebnis-Ebene (`success | partial | blocked | invalid`).
Es sind verschiedene Maschinenvertragsvokabulare, keine Pāṇini-Kategorien.

## Test vectors / Тестові вектори / Testvektoren

Vector A — empty state:

```text
{"relations":[],"schema":"panini-state/0.1","serialization":"canonical-json-sha256-v0.1","terms":[]}
```

→ `state:sha256:23aa0265da93189f9a093c2b6698ae91baa345c58a30754ee5cc6ffb7698e854`

Vector B — single `Sap` term:

```text
{"relations":[],"schema":"panini-state/0.1","serialization":"canonical-json-sha256-v0.1","terms":[{"id":"term:vikarana-Sap-raw","kind":"pratyaya","source_form":"Sap","surface_form":"Sap"}]}
```

→ `state:sha256:7b19d66e1d5e24edf54f455a34bfb8fbeee28c3058b78801c1412ea1f431a09b`

Run [`validate_trace_fixtures.py`](../tools/validate_trace_fixtures.py) to
recompute canonical state digests. Related: trace serialization audit,
Derivation IR events, trace evidence model, and Derivation IR state schema.
