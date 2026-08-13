# My Lisp code-level audit / Code-level audit My Lisp / Code-Level-Audit von My Lisp

## English

**Scope:** read-only audit of `/mnt/c/GitHub/my-lisp`, 2026-08-13. No My Lisp
files were changed.

`my-lisp` declares itself the ecosystem's semantic source of truth. Its
`docs/sanskrit-semantic-migration.md` requires an audit-first, phase-gated
semantic vocabulary layer and explicitly forbids mechanically renaming code.
The current Rust implementation already contains:

- `semantic/atoms.rs`: stable semantic IDs distinct from SLP1 display;
- `semantic/karaka.rs`: `SemanticCall` validates a dhātu predicate, kāraka
  role IDs, and duplicate roles;
- `syntax.rs`: the existing executable AST remains `Expr`/`ExprKind`.

The implementation comments state that parsing `(dA :kartf ...)` into
`SemanticCall` is deliberately deferred to P5. Thus Panini Foundation must not
assume that semantic calls are executable My Lisp syntax yet. The correct next
bridge is an evidence- and gate-reviewed parser/evaluator experiment, not a
change to Panini ontology or a broad renaming campaign.

## Українська

**Обсяг:** read-only audit `/mnt/c/GitHub/my-lisp`, 2026-08-13. Файли My Lisp
не змінювалися.

`my-lisp` оголошує себе семантичним source of truth екосистеми. Його
`docs/sanskrit-semantic-migration.md` вимагає audit-first, phase-gated
semantic vocabulary layer і прямо забороняє механічне перейменування коду.
У поточній Rust-реалізації вже є:

- `semantic/atoms.rs`: сталі semantic ID, відокремлені від SLP1 display;
- `semantic/karaka.rs`: `SemanticCall` валідує dhātu predicate, kāraka ID та
  дублікати ролей;
- `syntax.rs`: виконуваний AST досі є `Expr`/`ExprKind`.

Коментарі реалізації прямо відкладають парсинг `(dA :kartf ...)` у
`SemanticCall` до P5. Отже Panini Foundation не може вважати semantic calls
виконуваним синтаксисом My Lisp. Правильний наступний міст — evidence- та
gate-reviewed parser/evaluator experiment, а не зміна онтології Паніні чи
масове перейменування.

## Deutsch

**Umfang:** Read-only-Audit von `/mnt/c/GitHub/my-lisp`, 2026-08-13. Es wurden
keine My-Lisp-Dateien geändert.

`my-lisp` ist die semantische source of truth des Ökosystems. Seine Migration
verlangt audit-first, phase-gated semantic vocabulary und verbietet
mechanisches Umbenennen. Vorhanden sind Atom-IDs getrennt von SLP1,
`SemanticCall`-Validierung und der bestehende ausführbare `Expr`-AST. Das
Parsen von `(dA :kartf ...)` in `SemanticCall` ist ausdrücklich P5. Daher sind
semantic calls noch keine ausführbare My-Lisp-Syntax; der nächste Schritt ist
ein evidence- und gate-reviewed Parser/Evaluator-Experiment.
