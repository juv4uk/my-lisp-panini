# Sarvam Ontology Verification Report — 40 Concepts

**Validator:** Sakshi (opencode)  
**Дата:** 2026-08-27  
**Source:** sarvam-concept-evidence.md (40 meaningful glosses)  
**Status:** WITNESS — needs Shiva domain review

---

## Quality Distribution

| Category | Count | % | Description |
|---|---|---|---|
| OK (real translation) | 10 | 25% | Meaningful English gloss |
| Transliteration only | 25 | 62.5% | Romanized Sanskrit, no semantic value |
| Error | 5 | 12.5% | API timeout, meta-description, wrong meaning, case error, IAST error |
| **Total** | **40** | **100%** | |

## Errors Requiring Immediate Fix

| Concept | Sarvam Output | Problem | Correct |
|---|---|---|---|
| brahmāṇḍa | ERR:The read operation timed out | API failure | Re-translate |
| hetu | "The reason is that the word hetu is derived from..." | Meta-description | Should be "Cause, reason" |
| asiddha | Siddha | Wrong meaning | asiddha = "not established" (negation) |
| jāyate | JAYATE | ALL CAPS artifact | Should be "is born, arises" |
| apādāna | Apadaana | IAST error | Should be "Apādāna" |

## Context Verification

| Context Source | Concepts Found | Notes |
|---|---|---|
| sastra/ (ontology, dhatu, karaka, paribhasha) | 10/40 | Core Pāṇinian entities only |
| research/ (other analysis docs) | 2/40 | anuvṛtti, bhūvādayo have real usage context |
| sarvam-full-evidence.md only | 37/40 | Circular — no independent corpus verification |
| Not found anywhere | 1/40 | brahmāṇḍa |

## Key Finding

**37 of 40 concepts have NO independent corpus context.** They exist only as Sarvam translation entries. The concepts were auto-extracted from the corpus but never verified against:
- The actual Sanskrit source texts in `sanskritworld_texts_md/`
- The Pāṇinian sastra/ analysis documents
- The Śiva-sūtra canon

This means the translations are **ungrounded** — they have no evidence linking them to actual usage in the corpus.

## Recommendations

1. **Fix 5 errors immediately** (brahmāṇḍa, hetu, asiddha, jāyate, apādāna)
2. **Context extraction needed:** For each of 40 concepts, find 1-2 actual usage examples from the Sanskrit corpus
3. **IAST verification:** Cross-check all 40 IAST spellings against canonical Sanskrit dictionaries (Monier-Williams, Apte)
4. **Quality gate:** Do not promote to Obsidian knowledge graph until context extraction + IAST verification complete
5. **Domain review:** Shiva agent should verify Pāṇinian-specific terms (anudātta, anuvṛtti, apavāda, apādāna, asiddha, aṣṭādhyāyī, bhūvādayo, dṛṣṭānta, gaṇa, hetu)

## Epistemic Status

- Quality distribution: CONFIRMED (manual inspection)
- Context gap: CONFIRMED (37/40 ungrounded)
- Error identification: CONFIRMED (5 clear errors)
- Recommendations: PROPOSED (needs owner/Shiva decision)
