# Śiva Sūtra source-rights review

Status: `PANINI-SIVA-SUTRA-SOURCE-RIGHTS-REVIEW`. This review assesses source
admission for the project’s fourteen phoneme-ordering sūtras, also called
Māheśvara Sūtras. It does not concern the distinct Kashmir Śaiva text commonly
called *Śiva Sūtras*.

## [PANINI]

The fourteen-row sound ordering and its final `it` markers are inputs to the
project’s account of pratyāhāra. This report does not establish an edition,
textual history, or a historical explanation of the popular Śiva attribution.
Those are separate philological questions.

## [INTERPRETATION]

### Candidate assessed

Learn Sanskrit Online’s lesson [“The Shiva Sutras”](https://www.learnsanskrit.org/vyakarana/sounds/the-shiva-sutras/)
displays all fourteen rows in Devanāgarī and IAST, identifies final markers as
`it`, and states that the page is available under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It explicitly
distinguishes the final marker from the listed sounds and notes the repeated
`ha` and ambiguous `R` endpoint. The project independently checked the page
on 2026-08-13.

This is a better rights candidate than the two earlier cross-check-only sources
because its licence is stated on the page. CC BY 4.0 permits reuse provided the
required attribution and licence notice are preserved. It is nevertheless a
pedagogical presentation, not by itself a critical edition.

### Admission decision

| Requirement | Result | Reason |
| --- | --- | --- |
| Explicit permitted-reuse right | pass | Page declares CC BY 4.0. |
| Correct object scope | pass | The page displays the fourteen phoneme-ordering rows, not the Kashmir Śaiva work. |
| All fourteen rows observable | pass | Rows appear in the page’s list. |
| Immutable revision or content hash | fail | The page gives no release tag, commit ID, downloadable source artifact, or content hash. |
| Attribution record prepared | pending | Needed only if source text is copied into a project artifact. |
| Independent row cross-check | pending | Existing provisional transcription and exhaustive fixtures still require a row-by-row comparison against a pinned snapshot. |

**Decision:** this source is eligible as a *rights-cleared textual
cross-check*, but is **not yet admissible as a pinned machine-data dependency**.
No text from it is copied into this repository by this task.

### Required next step

Create a separately versioned local acquisition record only after all of the
following are reviewed together:

1. exact retrieval timestamp and canonical URL;
2. source bytes and SHA-256 recorded outside the derived registry;
3. CC BY 4.0 attribution, source title, and licence link preserved;
4. reproducible IAST/Devanāgarī-to-SLP1 conversion;
5. independent fourteen-row comparison against
   `siva-sutras-slp1-provisional-v0.1.yaml` and
   `pratyahara-exhaustive-v0.1.yaml`.

The hash in step 2 pins an acquisition, not the publisher’s future revisions.
It must therefore record the limitation honestly and retain the source URL.

## [MY-LISP HYPOTHESIS]

The machine-input prohibition in
`registry/siva-sutras/siva-sutras-slp1-provisional-v0.1.manifest.yaml` remains
in force. A future importer may use a rights-cleared and pinned acquisition as
evidence for a project conversion, but must not identify its data schema with
Pāṇini’s own representation or make it authoritative over scholarly review.

Suggested follow-up task: `PANINI-SIVA-SUTRA-PINNED-ACQUISITION-PROTOCOL`.
Its output should be a policy and validator fixture, not a runtime migration.

## English summary

Learn Sanskrit Online is a CC BY 4.0 rights-cleared textual cross-check for the
fourteen phoneme-ordering Śiva Sūtras. Because it lacks an immutable revision
or source hash, it does not yet pass the machine-data admission gate.

## Українська

Learn Sanskrit Online є rights-cleared текстовим cross-check для чотирнадцяти
фонемних Śiva Sūtras: сторінка явно має CC BY 4.0. Проте вона не має
незмінного revision або hash джерельного артефакту, отже ще не проходить gate
для machine data.

Нормативно: цей висновок не дозволяє копіювати сторінку в registry і не знімає
`machine_input_status: prohibited`. Він дозволяє лише використати її як
ліцензійно зрозумілу контрольну публікацію. Наступний крок — окремий
відтворюваний acquisition protocol з attribution, зафіксованими bytes/hash та
незалежною перевіркою всіх 14 рядків.

## Deutsch

Learn Sanskrit Online ist ein lizenzrechtlich geklärter textueller Abgleich
für die vierzehn phonemischen Śiva Sūtras: Die Seite steht ausdrücklich unter
CC BY 4.0. Da jedoch keine unveränderliche Revision oder kein Quell-Hash
vorliegt, besteht sie die Zulassungsschranke für Machine-Daten noch nicht.
