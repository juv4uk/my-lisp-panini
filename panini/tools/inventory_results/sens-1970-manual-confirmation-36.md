# SENS #1970: ручне підтвердження 36 рядків мого першого проходу (10 «must-change» + 26 «semantic-guard»), 2026-10-02

Джерело рядків: `sens-1970-function8-first-pass-6960ae1c.tsv`; код читано у checkout sens `6960ae1c` (±2 рядки контексту). Нічого в SENS не змінено.

| # | path:line | моя евристична мітка | вердикт (після читання) | що саме | наслідок |
|---|---|---|---|---|---|
| 1 | `knowledge/semantic-lineage-core-v1.lisp:179` | semantic-guard | **semantic axiom (text)** | knowledge-аксіома «exactly one bare Sid8 token» / «one exact 8-bit function-identity space» | must-change (замінити формулювання; не змінює поведінку) |
| 2 | `.github/workflows/sid8-only-ontology.yml:1` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 3 | `.github/workflows/core1-sid8-bootstrap-self-carry.yml:1` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 4 | `.github/workflows/core1-sid8-bootstrap-self-carry.yml:29` | semantic-guard | **real guard (CI literal ban)** | grep забороняє 8-бітні літерали `"[01]{8}"`, `(QUOTE [01]{8})`, `(CONS (CONS [01]{8}` в overlay: охороняє ВІД 8-бітного запису | can-remain-as-compatibility (охоронець лишається сумісним; перевірити при D3-словах) |
| 5 | `.github/workflows/core1-sid8-bootstrap-self-carry.yml:30` | semantic-guard | **real guard (CI literal ban)** | grep забороняє 8-бітні літерали `"[01]{8}"`, `(QUOTE [01]{8})`, `(CONS (CONS [01]{8}` в overlay: охороняє ВІД 8-бітного запису | can-remain-as-compatibility (охоронець лишається сумісним; перевірити при D3-словах) |
| 6 | `.github/workflows/core1-sid8-bootstrap-self-carry.yml:31` | semantic-guard | **real guard (CI literal ban)** | grep забороняє 8-бітні літерали `"[01]{8}"`, `(QUOTE [01]{8})`, `(CONS (CONS [01]{8}` в overlay: охороняє ВІД 8-бітного запису | can-remain-as-compatibility (охоронець лишається сумісним; перевірити при D3-словах) |
| 7 | `.github/workflows/core1-sid8-bootstrap-self-carry.yml:33` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 8 | `.github/workflows/core1-sid8-bootstrap-self-carry.yml:54` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 9 | `.github/workflows/sid8-issue-lifecycle-guard.yml:1` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 10 | `.github/workflows/sid8-issue-lifecycle-guard.yml:16` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 11 | `.github/workflows/sid8-issue-lifecycle-guard.yml:23` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 12 | `.github/workflows/core1-s2-compiler.yml:30` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 13 | `.github/workflows/core1-s2-compiler.yml:50` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 14 | `.github/workflows/core1-compiler-sid-resolver.yml:1` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 15 | `.github/workflows/core1-compiler-sid-resolver.yml:20` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 16 | `.github/workflows/core1-compiler-sid-resolver.yml:40` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 17 | `.github/workflows/core1-compiler-sid-resolver.yml:50` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 18 | `.github/workflows/core1-s0.yml:36` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 19 | `.github/workflows/core1-s0.yml:62` | semantic-guard | **false positive** | ЛИШЕ НАЗВА (workflow/step name; не припущення) | не вносити в інвентар |
| 20 | `.github/workflows/ci.yml:102` | semantic-guard | **real guard (type)** | ci.yml: ідентичність SID у Rust-крейтах лише `Value::Sid(Sid8)`; заборона `SemanticRef` | must-change разом із типом ідентичності (guard зав'язаний на ім'я Sid8) |
| 21 | `.github/workflows/ci.yml:103` | semantic-guard | **real guard (type)** | ci.yml: ідентичність SID у Rust-крейтах лише `Value::Sid(Sid8)`; заборона `SemanticRef` | must-change разом із типом ідентичності (guard зав'язаний на ім'я Sid8) |
| 22 | `.github/workflows/kernel-abi-transport-boundary.yml:49` | semantic-guard | **real guard (expected output)** | kernel-abi-transport-boundary.yml:49 очікує рядок `(language-type Sens8)` | must-change при зміні типу (залежить від імені типу) |
| 23 | `.github/workflows/kernel-abi-transport-boundary.yml:58` | semantic-guard | **real guard (ABI boundary)** | kernel ABI тримає `pub semantic_id: u8` / `SemanticId(pub u8)` БЕЗ залежності від мови | can-remain: ABI-обгортка u8 це механізм транспорту, не мовна аксіома |
| 24 | `.github/workflows/kernel-abi-transport-boundary.yml:69` | semantic-guard | **real guard (ABI boundary)** | kernel ABI тримає `pub semantic_id: u8` / `SemanticId(pub u8)` БЕЗ залежності від мови | can-remain: ABI-обгортка u8 це механізм транспорту, не мовна аксіома |
| 25 | `lib/macro.lisp:1` | semantic-guard | **axiom text (comment)** | lib/macro.lisp:1 «bootstrap derivation on exact 8-bit function identities» | docs/comment: оновити формулювання |
| 26 | `crates/sens/src/syntax.rs:2` | parser/AST shape | **import only** | `use crate::Sens8;` | не окреме припущення (імпорт) |
| 27 | `crates/sens/src/syntax.rs:52` | parser/AST shape | **real (parser/AST)** | `ExprKind::Sid(Sens8)`: SID-вузол несе рівно Sens8 | must-change-before-variable-width |
| 28 | `crates/sens/src/syntax.rs:73` | parser/AST shape | **doc comment** | коментар «функція займає рівно 1 байт» | docs: оновити з типом |
| 29 | `crates/sens/src/syntax.rs:78` | parser/AST shape | **doc comment** | те саме англійською | docs: оновити з типом |
| 30 | `crates/sens/src/syntax.rs:80` | parser/AST shape | **real (parser/AST)** | `Call(Sens8, Rc<[Expr]>)`: голова виклику лише Sens8 | must-change-before-variable-width |
| 31 | `crates/sens/src/syntax.rs:95` | parser/AST shape | **real (hard guard)** | `const _: () = assert!(size_of::<Sens8>() == 1)`: збірка падає, якщо тип не 1 байт | must-change (жорсткий assert) |
| 32 | `crates/sens/src/syntax.rs:240` | parser/AST shape | **real (wire/FASL decode)** | `Sens8::from_packed_byte(value)`: декодування SID з ОДНОГО байта (FASL tag) | must-change-before-variable-width (потрібен новий wire; #2189 кадри) |
| 33 | `crates/sens/src/syntax.rs:569` | parser/AST shape | **real (wire/FASL decode)** | `Sens8::from_packed_byte(value)`: декодування SID з ОДНОГО байта (FASL tag) | must-change-before-variable-width (потрібен новий wire; #2189 кадри) |
| 34 | `crates/sens/src/parser.rs:459` | parser/AST shape | **real (reader)** | reader: `token.len() == 8` бінарних цифр → `Sens8::from_exact_bits` | must-change-before-variable-width (джерельна граматика; D3/D4-слова) |
| 35 | `crates/sens/src/parser.rs:460` | parser/AST shape | **real (reader)** | reader: `token.len() == 8` бінарних цифр → `Sens8::from_exact_bits` | must-change-before-variable-width (джерельна граматика; D3/D4-слова) |
| 36 | `contracts/core4-predicate-answer-boundary.lisp:10` | semantic-guard | **boundary statement (comment)** | core4-predicate-answer-boundary.lisp:10 «never turns a short answer into an 8-bit function…»: про ортогональність відповіді й функції, ширина не є суттю | can-remain; змінити «8-bit» на нейтральне при редагуванні |

## Підсумок

- **36 рядків:** хибних спрацювань (лише назва workflow/кроку) **15**; реальні CI-охоронці **8 рядків (4 різні охоронці)**; аксіоми/межові твердження в коментарях і знаннях **3**; рядки «must-change» (syntax.rs, parser.rs): **10 рядків = 5 різних припущень** (SID-вузол `Sid(Sens8)`, голова виклику `Call(Sens8,..)`, `assert size_of==1`, декодування з одного байта `from_packed_byte`, reader рівно 8 цифр) + 3 нереальні рядки (імпорт і 2 коментарі).
- **Точність моєї мітки «semantic-guard» для workflow-рядків: 11 реальних із 26 (42%)**; решта 15 це назви кроків із «SID8». Це гірше за 86% на вибірці з 30 і гірше за мою оцінку: мітку «semantic-guard» за шляхом `.github/workflows/` не слід вважати надійною.
- **Підтверджено для must-change:** 7 із 10 рядків кодові (52, 80, 95, 240, 569, 459, 460); 459-460 і 240/569 це 2 дублікати того самого припущення (reader; FASL-байт).
- **Не перевірено:** рядки bucket «unknown» (159), cml-репо, чи кожен «real guard» справді потребує зміни при змінній ширині (позначено лише за змістом рядка), порівняння з blocker-прапорцями #1974.
