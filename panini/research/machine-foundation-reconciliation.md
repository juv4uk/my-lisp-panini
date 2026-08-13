# Machine / foundation reconciliation

## English

### Status — reconciled with an explicit boundary (2026-08-14)

`panini/machine/` is an executable **machine-fixture** prototype. It is not a
certified implementation of Pāṇini, and it is not an approved My Lisp language
integration.

### Observed machine facts

- The WSL acceptance entry point loads a local macro-free prelude and then the
  machine modules. It completed 22 assertions in the current My Lisp VM.
- The `dadAti` fixture records an explicit machine relation: 2.4.75 names
  2.4.72 as `utsarga`; the resolver emits `resolved-by / apavAda / 2.4.75`.
- The fixture makes Slu-related state tags observable. It does not claim that
  this short trace is a complete historical derivation.
- Current executable modules do not expose the earlier `SemanticCall`,
  `DHATU_DA`, or `KARAKA_KARTR` bridge described by a previous review. Those
  statements must not be used as a description of the current executable path.

### Three-level boundary

- **[PANINI]** The corpus and its commentarial traditions remain the source for
  the meaning, applicability, and interaction of sūtra.
- **[INTERPRETATION]** An `utsarga`/`apavAda` relation can be represented as an
  explicit implementation relation; this is not by itself an exhaustive
  account of conflict resolution.
- **[MY-LISP HYPOTHESIS]** Immutable terms, tags, and a small selection trace
  are useful machine experiments. They are not My Lisp primitives and must not
  be promoted merely because the fixture runs.

### Gate result

`PANINI-MACHINE-TEST-EXECUTION-COMPAT` is now supported by real WSL execution.
It does **not** close `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW`: parser and
evaluator integration remain separate work. A future end-to-end derivation
must supply sūtra/commentary provenance, candidate-rule evidence, visibility,
conflict evidence, each state transition, and an explicit unresolved result
where the sources do not decide.

## Українська

### Статус — звірено з явною межею (2026-08-14)

`panini/machine/` є виконуваним прототипом **machine-fixture**. Це не
сертифікована реалізація Паніні й не затверджена мовна інтеграція My Lisp.

### Спостережувані факти машини

- WSL acceptance entrypoint завантажує локальний macro-free prelude, а потім
  machine-модулі. У поточній My Lisp VM він завершив 22 assertions.
- Fixture `dadAti` фіксує явне машинне відношення: 2.4.75 називає 2.4.72 як
  `utsarga`; resolver видає `resolved-by / apavAda / 2.4.75`.
- Fixture робить Slu-пов'язані state tags спостережуваними. Він не стверджує,
  що цей короткий trace є повною історичною деривацією.
- Поточні виконувані модулі не містять раніше описаного bridge `SemanticCall`,
  `DHATU_DA` або `KARAKA_KARTR`. Ті попередні твердження не можна вживати як
  опис нинішнього виконуваного шляху.

### Трирівнева межа

- **[PANINI]** Корпус і традиції коментарів лишаються джерелом значення,
  застосовності та взаємодії sūtra.
- **[INTERPRETATION]** Відношення `utsarga`/`apavAda` можна подавати як явне
  відношення реалізації; само по собі воно не є вичерпним описом вирішення
  конфліктів.
- **[MY-LISP HYPOTHESIS]** Незмінні terms, tags і малий selection trace —
  корисні машинні експерименти. Це не primitives My Lisp, і їх не можна
  підвищувати до такого статусу лише тому, що fixture запускається.

### Результат gate

`PANINI-MACHINE-TEST-EXECUTION-COMPAT` тепер підтверджено реальним виконанням
у WSL. Це **не** закриває `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW`: інтеграція
parser і evaluator лишається окремою роботою. Майбутня end-to-end деривація
мусить подати provenance sūtra/коментаря, evidence кандидатних правил,
visibility, conflict evidence, кожен state transition і явний unresolved
результат там, де джерела не дають відповіді.

## Deutsch

### Status — mit expliziter Grenze abgeglichen (2026-08-14)

`panini/machine/` ist ein ausführbarer **Machine-Fixture**-Prototyp. Es ist
weder eine zertifizierte Pāṇini-Implementierung noch eine bestätigte
My-Lisp-Sprachintegration.

### Beobachtete Maschinenfakten

- Der WSL-Acceptance-Einstiegspunkt lädt ein lokales makrofreies Prelude und
  danach die Machine-Module. In der aktuellen My-Lisp-VM liefen 22 Assertions.
- Das `dadAti`-Fixture hält eine explizite Maschinenrelation fest: 2.4.75
  benennt 2.4.72 als `utsarga`; der Resolver liefert
  `resolved-by / apavAda / 2.4.75`.
- Das Fixture macht Slu-bezogene Zustands-Tags sichtbar. Es behauptet nicht,
  dass dieser kurze Trace eine vollständige historische Derivation sei.
- Die aktuellen ausführbaren Module enthalten nicht die früher beschriebene
  `SemanticCall`-/`DHATU_DA`-/`KARAKA_KARTR`-Bridge. Jene Aussagen dürfen den
  heutigen ausführbaren Pfad nicht beschreiben.

### Dreiebenengrenze

- **[PANINI]** Korpus und Kommentierungstraditionen bleiben die Quelle für
  Bedeutung, Anwendbarkeit und Wechselwirkung der sūtra.
- **[INTERPRETATION]** Eine `utsarga`/`apavAda`-Relation kann als explizite
  Implementierungsrelation dargestellt werden; sie ist allein keine
  vollständige Konfliktauflösung.
- **[MY-LISP HYPOTHESIS]** Unveränderliche Terms, Tags und ein kleiner
  Auswahltrace sind nützliche Maschinenexperimente. Sie sind keine My-Lisp-
  Primitives und werden nicht allein durch ein laufendes Fixture dazu.

### Gate-Ergebnis

`PANINI-MACHINE-TEST-EXECUTION-COMPAT` wird nun durch echte WSL-Ausführung
gestützt. Dies schließt `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW` **nicht**:
Parser- und Evaluatorintegration bleiben getrennte Arbeit. Eine spätere
End-to-End-Derivation muss Sūtra-/Kommentarprovenienz, Kandidatenregeln,
Sichtbarkeit, Konfliktevidenz, jeden Zustandsübergang und ein explizites
`unresolved` bei unentscheidbaren Quellen liefern.
