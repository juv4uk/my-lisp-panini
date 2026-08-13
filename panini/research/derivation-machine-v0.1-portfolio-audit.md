# Аудит портфеля Panini Derivation Machine v0.1

Статус: `partial`, 2026-08-14. Це контрольний огляд наявних evidence fixtures.
Він не підвищує жоден приклад до `complete` і не відкриває інтеграцію Panini → My Lisp.

## English

This portfolio establishes disciplined machine boundaries: immutable states,
append-only evidence, source/machine separation, and blocking unknowns. It
does not establish a complete derivation or a Panini-to-My-Lisp primitive map.

## Українська

### [PANINI]

Портфель містить різні ситуації: `Bavati` як базову форму, `dadAti` як шлях із
`Slu` і редуплікаційним питанням, класифікацію kāraka та незавершений випадок
Tripādī visibility. Наші `state`, `candidate`, `trace`, `partial` та `machine
harness` не є термінами Aṣṭādhyāyī.

### [INTERPRETATION]

| Артефакт | Що зафіксовано | Чого не доводить | Статус |
| --- | --- | --- | --- |
| `bhavati-source-path-partial-v0.1` | `BU → laT → tip → ti`; блокування на 3.1.68 | `Sap`, guṇa, sandhi, повну форму | `partial` |
| `bhavati-sap-designation-partial-v0.1` | markers/lopa/`sArvaDAtuka` для `Sap` | вибір lakāra/tiṅ, guṇa і повну деривацію | `partial` |
| `dadati-source-path-partial-v0.1` | source prefix 2.4.75 для `juhotyAdi` | 2.4.72, abhyāsa й `dadAti` transition | `partial` |
| `dadati-apavada-conflict-v0.1` | контрфактичний machine conflict | історичну co-applicability | `partial` |
| `tripadi-unresolved-visibility-v0.1` | `unresolved → block` visibility | універсальну модель asiddha | `partial` |
| `da-karaka-classification-v0.1` | evidence-bound kāraka claims | graph edge, valency або entity graph | `partial` |

### Що вже перевіряє портфель

```text
immutable before/after states        — так, у bounded transitions
append-only evidence events          — так
source vs machine namespace          — так
unknown/deferred/partial as outcome  — так
visibility separate from conflict    — так, але на різних fixtures
surface form ≠ proof                 — так
```

### Що ще відсутнє

1. Немає шляху `source → surface` із перевіреними conditions, typed operations
   і canonical state hashes.
2. Немає джерельно підтвердженого конфлікту для конкретного прикладу.
3. Visibility fixture показує правильне блокування, але не є end-to-end
   деривацією.
4. Для `Bavati` потрібні умови 3.1.68 і міст від designation affix occurrence
   до guṇa precondition.
5. Для `dadAti` потрібні передумови `Slu → dvirvacana`, `abhyAsa`, hrasva та
   surface operation.

### [MY-LISP HYPOTHESIS]

Портфель уже виправдовує лише межі дизайну:

```text
state history is immutable              — machine contract evidenced
visibility and conflict are distinct    — machine contract evidenced
unknown may block a result              — machine contract evidenced
Panini mechanism → Lisp primitive       — not established
```

Перенесення в My Lisp до закриття цих прогалин має бути окремою гіпотезою з
namespace `machine:`; цей документ не є доказом, що Паніні «вимагає» VM-конструкції.

## Наступні evidence gates

| Пріоритет | Gate | Дозволений результат |
| --- | --- | --- |
| P0 | source audit умов `kartari Sap` для `Bavati` | `partial` transition або `blocked` |
| P0 | source audit `Slu → dvirvacana` для `dadAti` | новий `partial` source prefix |
| P1 | typed operation vocabulary для перевірених переходів | machine contract |
| P1 | source-level conflict або explicit absence | acceptance evidence, не scheduler |
| P2 | 3–5 reviewable traces | milestone gate review, не автоматичне `complete` |

## Deutsch

Das Portfolio belegt bisher nur disziplinierte Maschinengrenzen:
unveränderliche Zustände, append-only Evidenz, Trennung von Quelle und
Maschinenmodell sowie blockierende Ungewissheit. Es belegt weder eine
vollständige Derivation noch eine Abbildung auf My-Lisp-Primitiven.
