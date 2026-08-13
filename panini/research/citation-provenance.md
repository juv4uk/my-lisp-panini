# Citation provenance

`citation-provenance.yaml` is the machine-readable inventory for all 50
Aṣṭādhyāyī IDs cited in `panini/foundation/` and `panini/examples/` as of
2026-08-13.

It deliberately separates three questions that had previously been folded into
one prose claim:

1. Does the repository have a local text record for this sūtra?
2. Was the citation cross-checked against the Sanskrit/learnsanskrit.org rule
   corpus during `PANINI-SUTRA-CITATION-VERIFICATION`?
3. What exact documents rely on the citation?

`index.yaml` remains the local raw text registry. This file does not make it a
critical edition, and implementation sources such as Vidyut or
`panini/machine/` cannot elevate a citation's status.

## Use

Before adding a new assertion that depends on a sūtra:

1. Add its ID here and its `used_by` path.
2. Point `text_ref` to a stable local text record.
3. Assign `needs-check` until a primary corpus or edition has been checked.
4. Record a commentary or an implementation as a separate interpretation
   source, never by overwriting the primary text record.

The immediate follow-up is to move `needs-check` entries to a recorded primary
source. This is intentionally visible technical debt, not an invitation to
silently fill uncertain text from memory.
