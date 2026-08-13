# My Lisp atom provenance cross-check / Звірка provenance атомів My Lisp / Provenienzabgleich der My-Lisp-Atome

## English

**Scope:** read-only comparison of My Lisp's Rust atom registry with the
committed Panini registries. It checks identifiers and recorded provenance; it
does not validate programming-language operational meanings.

All 12 My Lisp dhātu spellings are present in `panini/registry/dhatu/`:
`kf`, `gam`, `dA`, `grah`, `jYA`, `dfS`, `Sru`, `vac`, `liK`, `paW`, `sTA`,
and `BU`. All six My Lisp kāraka spellings are likewise present. My Lisp is a
deliberate 12-root subset of the current 20-record Panini registry, not a
replacement source.

| Finding | Consequence |
|---|---|
| Semantic IDs differ from SLP1 by design | preserve `DHATU_*`/`KARAKA_*` as identity; do not use spelling as ABI identity |
| `Sru` has `gana_disputed: true` and evidence status `disputed` in Panini | My Lisp must retain the discrepancy or downgrade any asserted gaṇa claim; do not silently treat gaṇa 5 as settled |
| Atom `status` remains `Experimental` | no entry is ready to be treated as a stable runtime contract solely from this cross-check |
| Glosses/operational semantics are My Lisp choices | they remain `[MY-LISP HYPOTHESIS]`, not statements established by Dhātupāṭha or Aṣṭādhyāyī |

## Українська

**Обсяг:** read-only порівняння Rust registry атомів My Lisp із committed
реєстрами Panini. Воно перевіряє ідентифікатори та зафіксований provenance, а
не валідує operational semantics мови програмування.

Усі 12 написань dhātu My Lisp наявні в `panini/registry/dhatu/`: `kf`, `gam`,
`dA`, `grah`, `jYA`, `dfS`, `Sru`, `vac`, `liK`, `paW`, `sTA`, `BU`. Так само
наявні всі шість написань kāraka. My Lisp є свідомою 12-кореневою підмножиною
поточного Panini registry із 20 записів, а не джерелом, що його замінює.

| Знахідка | Наслідок |
|---|---|
| Semantic ID навмисно відрізняються від SLP1 | зберігати `DHATU_*`/`KARAKA_*` як identity; не робити написання ABI identity |
| `Sru` має `gana_disputed: true` та evidence status `disputed` у Panini | My Lisp мусить зберегти розбіжність або понизити будь-яке твердження про gaṇa; не вважати gaṇa 5 остаточною мовчки |
| Atom `status` лишається `Experimental` | жоден запис не готовий стати stable runtime contract лише внаслідок цієї звірки |
| Glosses/operational semantics є вибором My Lisp | вони лишаються `[MY-LISP HYPOTHESIS]`, а не фактами Dhātupāṭha чи Aṣṭādhyāyī |

## Deutsch

**Umfang:** Read-only-Vergleich des Rust-Atomregisters von My Lisp mit den
committeten Panini-Registern. Geprüft werden Identifikatoren und dokumentierte
Provenienz, nicht die operationale Semantik der Programmiersprache.

Alle zwölf Dhātu-Schreibungen und alle sechs Kāraka-Schreibungen von My Lisp
sind im Panini-Register vorhanden. My Lisp ist eine bewusste Teilmenge mit
zwölf Wurzeln des aktuellen Panini-Registers mit zwanzig Einträgen, keine
Ersatzquelle. `Sru` ist im Panini-Register als strittig markiert; My Lisp darf
gaṇa 5 daher nicht stillschweigend als endgültig behandeln. Die Atom-Status
bleiben `Experimental`, und operational meanings bleiben My-Lisp-Hypothesen.
