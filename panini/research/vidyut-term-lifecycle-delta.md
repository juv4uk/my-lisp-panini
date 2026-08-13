# Vidyut term lifecycle delta

Status: code-level audit for `PANINI-VIDYUT-TERM-LIFECYCLE-DELTA`, read from
the local Vidyut checkout on 2026-08-13. Scope: `vidyut-prakriya`; this is not
a claim that its Rust data model is a direct representation of Pāṇini.

## What the code does

### Lifecycle

1. `Term::make_upadesha` initializes `u`, `text`, and `sthanivat` from the
   supplied upadeśa. `make_dhatu` additionally records `Morph::Dhatu`, gaṇa,
   and optional antar-gaṇa.
2. During derivation, a mutable `Prakriya` owns `Vec<Term>`. `Term.text` is
   changed for operations such as guṇa, vṛddhi, and lopa; `u` normally retains
   the original aupadeśika form and is changed only for full substitution.
3. `Prakriya::run` / `run_at` mutate state then call `step`. A `Step` stores
   one `Rule` and a post-operation snapshot of `StepTerm`s. `StepTerm` exposes
   text and `was_changed`, while its tags remain private.
4. Optional rules are separately represented by `RuleChoice { rule, decision }`
   with `Accept` or `Decline`. A declined optional rule is logged as a choice,
   not as a normal applied `Step`.
5. History is configurable. With `VyakaranaBuilder::log_steps(false)`, the
   generated form remains available but `history()` is empty.

Code anchors: `vidyut-prakriya/src/core/term.rs`,
`core/prakriya.rs` (`Term`, `Step`, `StepTerm`, `RuleChoice`, `run`, `step`),
and `vyakarana.rs` (`log_steps`).

## [PANINI]

The audit establishes facts about Vidyut's implementation only. It does not
establish that the Aṣṭādhyāyī itself has Rust-like mutable terms, snapshots, or
a configurable logging mode. Upadeśa, it-related material, substitutions, and
derivational ordering need their own textual and commentarial evidence.

## [INTERPRETATION]

Vidyut makes two useful interpretive distinctions explicit:

- a term can preserve a source-oriented representation (`u`) while exposing a
  transformed surface representation (`text`); and
- an optional rule decision is different from an applied derivation step.

Its trace is intentionally pragmatic rather than proof-complete. A step has a
post-state and a heuristic `was_changed` flag, but no mandatory pre-state,
applicability set, rejection reason for non-optional rules, or generic conflict
winner explanation. Step logging can also be disabled for performance.

## [MY-LISP HYPOTHESIS]

Our future derivation IR should reuse the distinctions, not the data layout.

| Concern | Vidyut | Panini Foundation proposal |
|---|---|---|
| Source vs current form | `u` and mutable `text` | immutable `source_form` plus explicit state transition |
| Applied rule | post-state `Step` | transition with pre-state hash, post-state hash, rule provenance |
| Optionality | `RuleChoice` Accept/Decline | `DecisionEvent` with policy and reason |
| Conflict | not a generic trace reason | `ConflictEvent` with candidates, winner, and evidence record |
| Observability | optional history | provenance/verification profile must declare whether evidence is complete |
| Metadata | private tags plus morph | separate `panini_designation` and `implementation_metadata` namespaces |

The important delta is explanatory completeness. For My Lisp and symbolic AI,
a final form alone is insufficient: an audit trace must make visible the
candidate rules, chosen rule, decision policy, and provenance record. For bulk
generation, a no-trace profile can be permitted only if the resulting object is
explicitly marked `trace_status: omitted`.

## English summary

Vidyut preserves both an upadeśa-oriented and a transformed form, and it logs
applied rules separately from optional accept/decline choices. Its trace is a
valuable production design, but it is optional and does not generically explain
conflict resolution. Our IR should retain provenance and explanation even when
it chooses a different implementation strategy.

## Українська

Vidyut зберігає і upadeśa-орієнтовану, і змінену форму; застосовані правила
він відокремлює від optional accept/decline choices. Його trace — цінний
виробничий дизайн, але він опційний і не пояснює конфліктне рішення загальним
способом. Наш IR має зберегти provenance та пояснення навіть за іншої
стратегії реалізації.

## Deutsch

Vidyut bewahrt sowohl eine upadeśa-orientierte als auch eine transformierte
Form und trennt angewandte Regeln von optionalen Accept/Decline-Entscheidungen.
Sein Trace ist ein wertvolles Produktionsdesign, aber optional und ohne
allgemeine Konflikterklärung. Unser IR soll Provenienz und Erklärung auch bei
einer anderen Implementierungsstrategie erhalten.
