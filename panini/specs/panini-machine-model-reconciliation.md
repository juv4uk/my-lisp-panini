# Panini Machine Model Reconciliation / Звірка моделі машини Паніні / Abgleich des Panini-Maschinenmodells

## English

### Status

**Reconciled with an explicit boundary — 2026-08-14.** This specification
replaces an earlier closure statement that claimed complete theoretical
alignment. The current executable model is a narrow machine fixture.

### Confirmed implementation facts

- The WSL acceptance entry point loads the machine modules through a local
  macro-free prelude and records 22 passing assertions in the current My Lisp
  VM.
- The `dadAti` fixture exposes its declared relation: 2.4.75 refers to 2.4.72
  as `utsarga`; selection is traced as `resolved-by / apavAda / 2.4.75`.
- Slu-related changes are visible fixture tags, not an unqualified historical
  derivation claim.

### Boundary

**[PANINI]** Sūtra meaning, applicability, and precedence require corpus and
commentary evidence.

**[INTERPRETATION]** A declared `utsarga`/`apavAda` link is one executable
interpretation and does not exhaust conflict resolution.

**[MY-LISP HYPOTHESIS]** Immutable terms, tags, and selection traces are
machine-design experiments. Running them does not make them My Lisp primitives
or approve parser/evaluator integration.

### Open gate

Passing `PANINI-MACHINE-TEST-EXECUTION-COMPAT` proves the narrow VM acceptance
path. `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW` remains open. A later
end-to-end model must include source provenance, candidate rules, visibility,
conflict evidence, state transitions, and explicit `unresolved` outcomes.

The detailed audit is
[`research/machine-foundation-reconciliation.md`](../research/machine-foundation-reconciliation.md).

## Українська

### Статус

**Звірено з явною межею — 2026-08-14.** Ця специфікація замінює попередній
закривальний висновок, який заявляв повну теоретичну відповідність. Поточна
виконувана модель є вузьким machine fixture.

### Підтверджені факти реалізації

- WSL acceptance entrypoint завантажує machine-модулі через локальний
  macro-free prelude та фіксує 22 успішні assertions у поточній My Lisp VM.
- Fixture `dadAti` показує своє оголошене відношення: 2.4.75 посилається на
  2.4.72 як `utsarga`; вибір трасується як
  `resolved-by / apavAda / 2.4.75`.
- Slu-пов'язані зміни є видимими tags fixture, а не беззастережним історичним
  твердженням про деривацію.

### Межа

**[PANINI]** Значення, застосовність і пріоритет sūtra потребують evidence з
корпусу та коментарів.

**[INTERPRETATION]** Оголошений зв'язок `utsarga`/`apavAda` є одним
виконуваним тлумаченням і не вичерпує вирішення конфліктів.

**[MY-LISP HYPOTHESIS]** Незмінні terms, tags і selection traces — це
експерименти машинного дизайну. Їхній запуск не робить їх primitives My Lisp
і не затверджує parser/evaluator інтеграцію.

### Відкритий gate

Проходження `PANINI-MACHINE-TEST-EXECUTION-COMPAT` доводить вузький acceptance
path VM. `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW` лишається відкритим.
Майбутня end-to-end модель мусить містити source provenance, candidate rules,
visibility, conflict evidence, state transitions та явні `unresolved` outcomes.

Детальний audit наведено в
[`research/machine-foundation-reconciliation.md`](../research/machine-foundation-reconciliation.md).

## Deutsch

### Status

**Mit expliziter Grenze abgeglichen — 2026-08-14.** Diese Spezifikation ersetzt
eine frühere Abschlusserklärung, die vollständige theoretische Übereinstimmung
behauptete. Das aktuelle ausführbare Modell ist ein enges Machine-Fixture.

### Bestätigte Implementierungsfakten

- Der WSL-Acceptance-Einstiegspunkt lädt die Machine-Module über ein lokales
  makrofreies Prelude und verzeichnet 22 erfolgreiche Assertions in der
  aktuellen My-Lisp-VM.
- Das `dadAti`-Fixture zeigt seine deklarierte Relation: 2.4.75 verweist auf
  2.4.72 als `utsarga`; die Auswahl wird als
  `resolved-by / apavAda / 2.4.75` protokolliert.
- Slu-bezogene Änderungen sind sichtbare Fixture-Tags, keine uneingeschränkte
  historische Derivationsbehauptung.

### Grenze

**[PANINI]** Bedeutung, Anwendbarkeit und Priorität von sūtra benötigen
Korpus- und Kommentarevidenz.

**[INTERPRETATION]** Eine deklarierte `utsarga`/`apavAda`-Verknüpfung ist eine
ausführbare Interpretation und erschöpft die Konfliktauflösung nicht.

**[MY-LISP HYPOTHESIS]** Unveränderliche Terms, Tags und Auswahltraces sind
Maschinenexperimente. Ihre Ausführung macht sie weder zu My-Lisp-Primitives
noch bestätigt sie eine Parser-/Evaluatorintegration.

### Offenes Gate

`PANINI-MACHINE-TEST-EXECUTION-COMPAT` belegt den engen VM-Acceptance-Pfad.
`MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW` bleibt offen. Ein späteres
End-to-End-Modell muss Quellenprovenienz, Kandidatenregeln, Sichtbarkeit,
Konfliktevidenz, Zustandsübergänge und explizite `unresolved`-Ergebnisse
enthalten.

Das ausführliche Audit steht in
[`research/machine-foundation-reconciliation.md`](../research/machine-foundation-reconciliation.md).
