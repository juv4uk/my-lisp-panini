# Research directory duplication — findings, not a fix

Status: findings only (`PANINI-DEDUP-RESEARCH-DIR`) — deliberately not
resolved unilaterally, since it involves deleting/merging content in
another repo I don't have full editorial context on, and at least one
case is genuinely ambiguous about which version is authoritative.

## What's duplicated

Two parallel directories both named `research/`, with 4 overlapping
filenames:

| File | `panini/research/` | `research/` (repo root) |
|---|---|---|
| `computational-hypotheses.md` | 359 bytes, "Статус: не розпочато", all sections `TBD` | 13255 bytes, filled in |
| `heritage-analysis.md` | 352 bytes, "Статус: не розпочато", all sections `TBD` | 4538 bytes, filled in |
| `panini-nlp-analysis.md` | 354 bytes, "Статус: не розпочато", all sections `TBD` | 3782 bytes, filled in |
| `vidyut-analysis.md` | 11836 bytes, header "Vidyut — code-level audit", "Статус: v0.1" | 9661 bytes, header "Vidyut Code-Level Audit (v2 — Детальний)" |

For the first 3, the pattern is unambiguous: `panini/research/` holds
the original template stub (matching `README.md`'s stated directory
layout), and the real content was written into the top-level `research/`
instead of filling in the stub in place — almost certainly a path
mistake in whichever session did that research (wrote to `research/`
instead of `panini/research/`).

`vidyut-analysis.md` does NOT fit that pattern: the `panini/research/`
copy is the *larger* file and its own header claims `v0.1`, while the
root copy's header claims `v2 — Детальний` (implying it's a *later*
revision) despite being smaller. I did not diff these two in full or
read both end to end — flagging rather than guessing which one is
actually newer/authoritative, since the size heuristic that worked for
the other 3 files points the wrong way here.

## Recommendation (for `my-lisp-panini` to execute, not me)

1. For `computational-hypotheses.md`, `heritage-analysis.md`,
   `panini-nlp-analysis.md`: move the root `research/` copy's content
   into `panini/research/` (overwriting the stub), then delete the
   root-level `research/` directory.
2. For `vidyut-analysis.md`: read both fully, confirm which is actually
   current (the `v0.1` vs `v2` header labels contradict the file-size
   signal), keep that one under `panini/research/`, delete the other.
3. Once resolved, the top-level `research/` directory should not exist
   going forward — `README.md` already documents `panini/research/` as
   the canonical location.

No files were deleted or merged by this task — only read and compared.
