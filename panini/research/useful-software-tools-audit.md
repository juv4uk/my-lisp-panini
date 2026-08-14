# Useful software tools audit: adoption boundaries

Status: `PANINI-USEFUL-SOFTWARE-TOOLS-FULL-AUDIT`, 2026-08-13. This is a
selection policy, not authorization to add dependencies or alter My Lisp.

## English

## [PANINI]

No software tool determines what a Pāṇinian category means. Tools can preserve
scripts, normalize forms, generate analyses, record derivations, or validate
our claims against an independent implementation. Their output belongs to
`[INTERPRETATION]` or `[MY-LISP HYPOTHESIS]` until supported by separately
recorded textual evidence.

## Tool matrix

| Tool | Capability relevant to us | License/status found | Recommended role | Decision |
|---|---|---|---|---|
| [indic_transliteration](https://indic-transliteration.github.io/indic_transliteration_py/build/html/indic_transliteration_sanscript.html) | SLP1, IAST, Devanāgarī, Indic scripts | MIT/BSD documentation; active PyPI releases | external round-trip conformance oracle | **adopt for test fixtures only** |
| [Aksharamukha](https://github.com/virtualvinodh/aksharamukha) | broad script conversion and orthographic options, including SLP1 | repository AGPL-3.0; web API says GPL-3.0 | broad presentation-layer comparison | **evaluate only; do not link/vendor before license resolution** |
| [Vidyut](https://github.com/ambuda-org/vidyut) | morphology, derivation trace, sandhi, typed Sanskrit data | active Rust toolkit | independent implementation and trace oracle | **adopt as external comparison suite** |
| [Sanskrit Heritage](https://sanskrit.inria.fr/) | morphology, segmentation, sentence analysis | engine/data terms require separate review | independent computational tradition | **evaluate as oracle, no vendoring** |
| [sanskrit_parser](https://kmadathil.github.io/sanskrit_parser/build/html/sanskrit_parser_doc.html) | parser/generator, sandhi split, dependency analysis | open-source project; uses Sanskrit Data and Heritage inputs | later parser behaviour comparison | **watch until Phase 2; audit its data licenses first** |
| [CLTK](https://docs.cltk.org/) | generic classical-language NLP pipelines | MIT | corpus plumbing and experiment harness | **watch; not a Panini engine** |
| [Tree-sitter](https://github.com/tree-sitter/tree-sitter) | incremental concrete syntax trees, Rust/Wasm bindings | MIT | My Lisp IDE syntax, error recovery, editor queries | **adopt only after language syntax stabilizes** |
| [egg](https://docs.rs/egg/latest/egg/) | e-graphs and equality saturation | Rust library | explore equivalence classes / optimization hypotheses | **research-only; never default derivation semantics** |
| [Soufflé](https://github.com/souffle-lang/souffle) | Datalog/Horn-clause analysis compiled to native code | open-source tool for analysis | offline queries over provenance/trace graphs | **evaluate offline only; not VM rule executor** |
| [Panini-NLP](https://pypi.org/project/panini-nlp/) | registry/graph, sandhi, claimed neuro-symbolic stack | MIT, Alpha; 0.1/0.2 releases yanked | counterexample and architecture review | **experimental reference only** |

## Architecture findings

### Transliteration

Use `indic_transliteration` as an external test oracle for a fixed fixture set:
SLP1 → IAST → SLP1 and SLP1 → Devanāgarī → SLP1 where mapping is expected to
be reversible. The result must never replace our own canonical-ID policy or
silently normalize a registry file. Aksharamukha has wider script coverage and
orthographic controls, but its repository and hosted API present different
copyleft labels; therefore it is comparison-only until a license review records
the exact component and version.

### Morphology and parsing

Vidyut, Sanskrit Heritage, and `sanskrit_parser` solve different problems and
must not be treated as interchangeable. Vidyut is strongest for a traceable
derivation implementation; Heritage provides independent segmentation and
analysis; `sanskrit_parser` explicitly combines open data with Heritage for
parser/generator work. None supplies a license to call parser output a Pāṇinian
fact. Their first project use is a small, version-pinned differential test set,
not a production dependency.

### Program-language infrastructure

Tree-sitter is appropriate for the future IDE layer, because it builds a
concrete syntax tree and stays useful under syntax errors. It is inappropriate
as the evaluator or semantic parser. Do not begin a grammar until the My Lisp
P5 contract approves syntax and semantic-call boundaries.

`egg` and Soufflé are deliberately limited. Equality saturation assumes an
equivalence relation and explores rewrites in many directions; Pāṇinian
derivation has ordering, applicability, scope, optionality, and possibly
non-reversible steps. Soufflé is useful for asking monotonic questions over a
finished provenance graph (for example, "which active claims depend on an
unverified citation?"). It is not the operational authority for a derivation
engine or conflict resolver.

## Adoption protocol

Before adding any tool, create an ADR-style record with:

```yaml
tool: <name>
version_or_commit: <pinned revision>
license: <verified SPDX or unresolved>
role: test-oracle | IDE | offline-analysis | runtime-candidate
input_boundary: <canonical SLP1 / display-only / corpus format>
output_status: interpretation | hypothesis | test-result
data_dependencies: [<separately licensed assets>]
reproducible_command: <Guix command>
exit_criterion: <measurable reason to retain or remove>
```

Runtime admission additionally requires: a stable interface, an explicit
failure model, deterministic fixtures, Guix packaging, and approval by the
relevant My Lisp owner. No web API is a build dependency or source of canonical
runtime data.

## Immediate, deferred, prohibited work

| Horizon | Work | Constraint |
|---|---|---|
| Now | create transliteration differential fixtures against `indic_transliteration` and CDSL workflow | test-only, no registry rewrite |
| Now | retain Vidyut/Heritage output snapshots for selected examples | version and source provenance required |
| After P5 | prototype Tree-sitter grammar for IDE display | concrete syntax only, no evaluator semantics |
| After trace IR | run Soufflé over exported provenance data | offline audit, never authoritative execution |
| Research only | test a tiny `egg` model for equivalence hypotheses | no ordered derivation claim |
| Prohibited now | embed external parser/service output as My Lisp semantics | violates P5 and evidence gates |

## Українська

Аудит показує чотири різні ролі інструментів.

1. **Тести транслітерації:** `indic_transliteration` — найкращий кандидат для
   external round-trip fixtures SLP1/IAST/Devanāgarī. Він не має ставати
   внутрішнім каноном замість нашого SLP1.
2. **Незалежні санскритські oracles:** Vidyut, Sanskrit Heritage,
   `sanskrit_parser`. Порівнюємо outputs і фіксуємо revision, але не переносимо
   їхню семантику або дані в My Lisp без окремого gate.
3. **Інфраструктура мови:** Tree-sitter корисний для IDE після стабілізації
   синтаксису P5, а не для evaluator.
4. **Експериментальні формальні засоби:** Soufflé придатний для offline-запитів
   до provenance graph; `egg` — лише для дослідження еквівалентностей. Жоден
   не повинен непомітно стати rule engine Паніні, бо втрачаються порядок,
   scope, optionality та причини конфлікту.

Aksharamukha залишаємо comparison-only: його широке script coverage цікаве,
але ліцензію конкретного компонента треба звірити до використання. Кожне
підключення потребує pinned revision, Guix-команди, data-license audit і
вимірюваного exit criterion.

## Deutsch

Das Audit trennt vier Werkzeugrollen.

1. **Transliterations-Tests:** `indic_transliteration` eignet sich für externe
   SLP1/IAST/Devanāgarī-Round-Trip-Fixtures, ersetzt aber niemals unseren
   kanonischen SLP1-Standard.
2. **Unabhängige Sanskrit-Orakel:** Vidyut, Sanskrit Heritage und
   `sanskrit_parser` werden mit gepinnter Revision verglichen, nicht ohne Gate
   in My-Lisp-Semantik oder Daten übernommen.
3. **Sprachinfrastruktur:** Tree-sitter ist nach Stabilisierung der P5-Syntax
   für die IDE sinnvoll, nicht für den Evaluator.
4. **Experimentelle formale Werkzeuge:** Soufflé eignet sich für Offline-
   Provenance-Abfragen, `egg` nur für Gleichheitsforschung. Keines darf
   unbemerkt zum Pāṇini-Rule-Engine werden, weil Ordnung, Scope, Optionalität
   und Konfliktgründe sonst verloren gehen.

Aksharamukha bleibt comparison-only, bis die Lizenz des konkreten Components
geprüft ist. Jede Aufnahme verlangt gepinnte Revision, Guix-Befehl,
Datenlizenz-Audit und ein messbares Exit-Kriterium.
