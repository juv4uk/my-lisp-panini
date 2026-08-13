# Panini ↔ My Lisp semantic-ID mapping / Відповідність semantic ID Panini ↔ My Lisp / Semantic-ID-Zuordnung Panini ↔ My Lisp

## English

**Status:** design-only, `PANINI-MYLISP-SEMANTIC-ID-MAPPING-SPEC`. This is not
a runtime registry and does not authorize a parser, evaluator, or `rules.my`
change.

| Panini canonical SLP1 | My Lisp semantic ID | Status |
|---|---|---|
| `dA` | `DHATU_DA` | experimental mapping |
| `gam` | `DHATU_GAM` | experimental mapping |
| `kf` | `DHATU_KF` | experimental mapping |
| `jYA` | `DHATU_JNA` | experimental mapping; concrete Dhātupāṭha record must remain gaṇa-9 sense |
| `dfS` | `DHATU_DRS` | experimental mapping |
| `Sru` | `DHATU_SRU` | experimental mapping; Panini registry marks gaṇa as disputed |
| `vac` | `DHATU_VAC` | experimental mapping |
| `liK` | `DHATU_LIKH` | experimental mapping |
| `paW` | `DHATU_PATH` | experimental mapping |
| `sTA` | `DHATU_STHA` | experimental mapping |
| `BU` | `DHATU_BHU` | experimental mapping |
| `grah` | `DHATU_GRAH` | experimental mapping |
| six core kāraka | corresponding `KARAKA_*` IDs | experimental mapping; roles are not case aliases |

**Invariants:** semantic ID is the runtime identity; SLP1 is canonical spelling;
IAST/Devanāgarī are display only; `dhatupatha_code` identifies an attested root
record when needed; an operational gloss is not a Paninian definition. Future
P5 resolution may use this mapping only after My Lisp gate review.

## Українська

**Статус:** лише design, `PANINI-MYLISP-SEMANTIC-ID-MAPPING-SPEC`. Це не
runtime registry і не дозволяє змінювати parser, evaluator чи `rules.my`.

| Panini canonical SLP1 | My Lisp semantic ID | Статус |
|---|---|---|
| `dA` | `DHATU_DA` | experimental mapping |
| `gam` | `DHATU_GAM` | experimental mapping |
| `kf` | `DHATU_KF` | experimental mapping |
| `jYA` | `DHATU_JNA` | experimental mapping; конкретний Dhātupāṭha запис має лишатися gaṇa-9 sense |
| `dfS` | `DHATU_DRS` | experimental mapping |
| `Sru` | `DHATU_SRU` | experimental mapping; Panini registry позначає gaṇa як disputed |
| `vac` | `DHATU_VAC` | experimental mapping |
| `liK` | `DHATU_LIKH` | experimental mapping |
| `paW` | `DHATU_PATH` | experimental mapping |
| `sTA` | `DHATU_STHA` | experimental mapping |
| `BU` | `DHATU_BHU` | experimental mapping |
| `grah` | `DHATU_GRAH` | experimental mapping |
| шість core kāraka | відповідні `KARAKA_*` ID | experimental mapping; ролі не є aliases відмінків |

**Інваріанти:** semantic ID є runtime identity; SLP1 — canonical spelling;
IAST/Devanāgarī — лише display; `dhatupatha_code` ідентифікує attested root
record, коли це потрібно; operational gloss не є панінійським означенням.
Майбутній P5 resolution може використати mapping лише після My Lisp gate review.

## Deutsch

**Status:** ausschließlich Design, `PANINI-MYLISP-SEMANTIC-ID-MAPPING-SPEC`.
Dies ist kein Runtime-Registry und erlaubt keine Änderung an Parser, Evaluator
oder `rules.my`.

Die zwölf Dhātu werden ihren vorhandenen `DHATU_*`-IDs und die sechs Kāraka
ihren `KARAKA_*`-IDs zugeordnet. Alle Zuordnungen sind experimentell. `jYA`
bleibt an den Sinn der gaṇa 9 gebunden; `Sru` behält den strittigen gaṇa-Status.
Semantic ID ist Runtime-Identität, SLP1 kanonische Schreibweise,
IAST/Devanāgarī nur Darstellung. Ein operational gloss ist keine paninische
Definition. P5 darf diese Zuordnung erst nach dem My-Lisp-Gate verwenden.
