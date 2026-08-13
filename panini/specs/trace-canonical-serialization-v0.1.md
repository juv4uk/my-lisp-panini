# Trace canonical serialization contract v0.1

Status: `proposed` — fixes the trace-canonical-serialization-audit blockers.
This is a machine-contract spec; it makes no claim about Pāṇini.
Створено для `PANINI-MACHINE-TRACE-FORMAT`.

## Purpose

Immutable derivation-IR states must be content-addressed: the same semantic
state must produce the same bytes and the same digest on any host, so a
`state:sha256:<digest>` ID is reproducible evidence, not a claim. This contract
fixes the exact byte grammar, normalization, ordering, hash and test vectors
that the audit listed as missing.

## 1. Serialization format

- One format: **UTF-8 JSON**, no trailing whitespace, exactly one `\n`
  terminator (POSIX line ending).
- Key order: **canonical** — every mapping serialized with keys in the
  lexicographic order of their UTF-8 bytes (not insertion order).
- No indentation: output is a single line of compact JSON (no pretty print).
- Escaping: standard JSON escaping, `\uXXXX` for non-ASCII where the encoder
  escapes; encoders may choose native UTF-8 emission for printable non-ASCII
  *only if* the digest test vectors were generated with the same choice. This
  contract fixes the reference vectors on **native UTF-8 emission**.

## 2. Unicode and line-ending policy

- Unicode normalization: **NFC** applied to every string before serialization.
- Line endings: LF (`\n`) only; CR and CRLF are rejected.
- No BOM.

## 3. Terms order and relation ordering

- `terms`: the exact array order given in the fixture is the canonical order
  (fixtures are authored once); reordering a fixture changes its state digest,
  which is the intended invalidation signal.
- `relations`: sorted by the concatenation `(relation kind) + (subject id) +
  (object id) + (index)` using UTF-8 byte order (a total order).

## 4. Map-key order, escaping, presentation fields

- Map keys sorted as in §1.
- Reserved presentation fields MUST NOT appear in state bytes: `display_*`,
  `note`, `comment`, `local_path`, timestamps, `provenance` narrative.
- Provenance is a separate trace-level concern (`trace-evidence-model-v0.1.md`),
  never a part of state bytes.

## 5. Hash algorithm

- Algorithm: **SHA-256**.
- Digest encoding: lowercase hex.
- Prefix: `state:sha256:<digest>`.

## 6. Test vectors (input bytes → digest)

Vector A — empty state:
```
{"relations":[],"schema":"panini-state/0.1","serialization":"canonical-json-sha256-v0.1","terms":[]}
```
→ `state:sha256:23aa0265da93189f9a093c2b6698ae91baa345c58a30754ee5cc6ffb7698e854`

Vector B — single term, Sap:
```
{"relations":[],"schema":"panini-state/0.1","serialization":"canonical-json-sha256-v0.1","terms":[{"id":"term:vikarana-Sap-raw","kind":"pratyaya","source_form":"Sap","surface_form":"Sap"}]}
```
→ `state:sha256:7b19d66e1d5e24edf54f455a34bfb8fbeee28c3058b78801c1412ea1f431a09b`

Vectors are independently recomputable:
`printf '%s' '<canonical bytes>' | sha256sum` must equal the digest. The
validator (panini/tools/validate_trace_fixtures.py) recomputes and rejects any
`state:sha256:*` whose digest does not match.

## 7. Validator rule

- Any state carrying `serialization: canonical-json-sha256-v0.1` MUST have an
  `id` of the form `state:sha256:<hex>` and the validator MUST recompute the
  digest from the canonical bytes and reject on mismatch.
- `serialization: fixture-sexpr-not-hashed` remains the honest value for all
  legacy fixtures; those are structural evidence only and MUST NOT be called
  content-addressed.

## Status mapping (from derivation-machine-evidence-gate-review)

- `trace_status`: `complete | partial | omitted | invalid` (trace-level).
- IR `result.status`: `success | partial | blocked | invalid` (result-level).
- Milestone exit uses the portfolio manifest, not a single `complete`.
- This spec does not rename either vocabulary; it records that they are
  distinct levels (machine-contract note, no Pāṇini claim).

## Related

- research/trace-canonical-serialization-audit.md (the blockers this fixes)
- specs/derivation-ir-trace-events-v0.1.md (event envelope)
- specs/trace-evidence-model-v0.1.md (provenance boundary)
- specs/derivation-ir-v0.1.md (state/terms/relations shape)
