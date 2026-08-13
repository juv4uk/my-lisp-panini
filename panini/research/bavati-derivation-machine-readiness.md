# Bhavati: Derivation Machine v0.1 readiness audit

Status: `PANINI-DERIVATION-MACHINE-EXAMPLE-01-BAVATI`. This is an admission
audit for an end-to-end fixture, not a claim of a complete historical
derivation and not an executable machine trace.

## [PANINI]

The existing teaching example derives `Bavati` from `BU` under a present-tense,
third-person singular, parasmaipada analysis. Its cited path includes 3.2.123,
3.4.78, 3.1.68, 1.3.3, 1.3.9, 7.3.84, and 6.1.78. The root registry independently
records `BU` as a `BvAdi` (gaṇa 1) dhātu.

This audit does not treat the labels “term”, “state”, “candidate”, or
“transition” as Pāṇinian terminology.

## [INTERPRETATION]

The existing example is a useful pedagogical sequence, but it has not yet met
the stronger Derivation Machine v0.1 evidence standard. Earlier verification
identified two transcription defects in the quoted sūtra text: 1.3.7 was
written as `cutuS ca` rather than `cuTU`, and 7.3.84 was transcribed
inaccurately. More importantly, the example attributes initial `S` in `Sap`
to 1.3.7; the cited `cuTU` formulation does not itself justify that claim.

This is not a minor formatting issue: the later guṇa explanation depends on
what survives lopa and on how the relevant designation is established. The
correct response is a bounded `partial` result, not a silently repaired trace.

## [MY-LISP HYPOTHESIS]

### Candidate trace path

| Stage | Intended state observation | Evidence status | Machine admission |
| --- | --- | --- | --- |
| input | `BU` with declared gaṇa 1 and inflectional intent | root record verified; intent interpretation | admissible as fixture input |
| lakāra | `BU + laT` via 3.2.123 | citation verified, applicability interpretation pending | partial |
| tiṅ selection | `BU + tip` via 3.4.78 | citation verified, selection conditions need record | partial |
| it processing | `tip → ti` and `Sap → a` with designations retained separately | final-marker lopa support known; complete initial-marker/designation proof incomplete | blocked from complete |
| vikaraṇa | insertion of `Sap` via 3.1.68 | citation verified; exact conditions need record | partial |
| guṇa | `BU → Bo` before qualifying suffix | intended surface step documented; precondition chain needs source-to-designation proof | blocked from complete |
| sandhi | `Bo + a → Bav + a`, then `Bavati` | citation verified; typed state operation needs fixture | partial |

### Minimum immutable representation

The first fixture may use only these conservative identities:

```yaml
terms:
  - { id: term:root-BU, kind: dhAtu, source_form: BU, surface_form: BU }
  - { id: term:lakara-laT, kind: opaque, source_form: laT, surface_form: laT }
  - { id: term:tin-tip, kind: pratyaya, source_form: tip, surface_form: tip }
  - { id: term:vikarana-Sap, kind: pratyaya, source_form: Sap, surface_form: Sap }
```

The inflectional intent, gaṇa classification, and any `it` consequence must be
relations/designations with their own provenance; none may be smuggled into a
term’s display label or treated as an established My Lisp type.

### Required trace outcomes

Until the gates below pass, a Bhavati trace must terminate as:

```yaml
result: { status: partial }
unknowns:
  - exact-source-supported-account-of-initial-S-in-Sap
  - bridge-from-it-analysis-to-sarvadhatuka-precondition
  - complete-applicability-conditions-for-each-selection
  - independent-typed-operation-check-for-each-state-transition
```

No conflict or Tripādī visibility relation is presently evidenced for this
bounded path. The trace must therefore not invent a conflict event merely to
exercise the IR contract. The dedicated `dadAti` example is the stronger
conflict candidate.

### Completion gates

1. Correct the teaching example’s two sūtra transcriptions in a separately
   reviewed documentation task.
2. Add a provenance-backed account of the initial `S` in `Sap`; if support is
   unavailable, preserve the unknown and keep the trace partial.
3. Record applicability checks and selected decisions for every transition.
4. Serialize each before/after state and ensure that each state transition has
   a typed operation and an append-only event.
5. Add a source-backed explanation for the guṇa precondition without equating
   an `it` effect to compiler metadata.
6. Compare the resulting surface form as a display observation, not as proof
   that every intermediate choice is historically verified.

The outcome of this audit is therefore productive but deliberately incomplete:
`Bavati` is the first baseline fixture, not yet the first complete proof trace.

## English summary

Bhavati is a strong baseline derivation but currently qualifies only for a
partial trace. Two sūtra transcriptions and, crucially, the account of initial
`S` in `Sap` need source-backed repair before its guṇa chain can be called
complete.

## Українська

`Bavati` є сильним базовим прикладом, але наразі придатний лише для `partial`
trace. Потрібно виправити дві транскрипції sūtra і, головне, джерельно
обґрунтувати початковий `S` у `Sap`, перш ніж називати complete ланцюг guṇa.

Нормативно: фінальна форма `Bavati` не є доказом усіх проміжних рішень.
Невідомий міст від `it`-аналізу до передумови `sArvaDAtuka` не маскується
metadata, fallback чи сучасною аналогією. Поки міст не має незалежного
provenance, trace завершується `partial` і явно перелічує unknowns.

## Deutsch

Bhavati ist ein starkes Grundbeispiel, erfüllt derzeit jedoch nur die
Voraussetzungen für einen `partial` Trace. Zwei Sūtra-Transkriptionen und vor
allem die quellenbelegte Erklärung des initialen `S` in `Sap` müssen geklärt
werden, bevor die Guṇa-Kette als vollständig gelten kann.
