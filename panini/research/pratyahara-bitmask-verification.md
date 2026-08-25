# Pratyāhāra Bitmask Verification · Верифікація масок pratyāhāra

Status: research record `PHONETICS-KB-PARITY` · sakshi · 2026-08-25
Method: canonical positional encoding from Śiva-sūtras 1–14.
43 positions (including duplicate h and ṇ at different sūtra positions).

## Canonical Position Map

| Bit | Sound | Sūtra |
|---|---|---|
| 0 | a | 1 |
| 1 | i | 1 |
| 2 | u | 1 |
| 3 | ṛ | 2 |
| 4 | ḷ | 2 |
| 5 | e | 3 |
| 6 | o | 3 |
| 7 | ai | 4 |
| 8 | au | 4 |
| 9 | h | 5 |
| 10 | y | 5 |
| ... | ... | ... |
| 39 | ś | 13 |
| 40 | ṣ | 13 |
| 41 | s | 13 |
| 42 | h | 14 |

## Verified Masks

Computed from canonical sequence using standard pratyāhāra definition
(ādir antyena sahetā, 1.1.71).

## Discrepancies Found

4 of 7 tested pratyāhāras in current prototype_phonetics.my have INCORRECT
masks that include bits beyond position 42 (the last canonical sound).

Root cause: broad hex approximations instead of precise positional encoding.

## Recommendation

Update .my masks from this table before any adoption.
Full per-sound verification available via compute_masks.py methodology.
