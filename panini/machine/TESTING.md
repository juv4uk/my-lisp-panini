# Testing Panini Machine Model / Тестування Panini Machine Model / Tests des Panini-Maschinenmodells

## English

This document describes the testing strategy for `panini-machine-model-v0.1`.
Because the engine targets the My Lisp VM, its test suite is written directly
in Lisp.

### Test-suite location

Tests are in [tests.my](tests.my).

### Running tests

After bootstrapping the My Lisp VM, load the environment and run `(run-tests)`:

```lisp
> (load "panini/machine/compiler.my")
> (load "panini/machine/meta.my")
> (load "panini/machine/rules.my")
> (load "panini/machine/tests.my")
> (run-tests)
```

### Test structure

The suite uses a small `assert-equal` helper to check state transitions.

1. **Unit tests: phonology and morphology.** They cover individual helper
   functions and phoneme operations: `test-eco-sandhi` checks Rule 6.1.78
   (`e/o/ai/au + vowel → ay/av/Ay/Av`); `test-guna` checks the Rule 1.1.2
   correspondence (`i → e`, `u → o`, `f → ar`).
2. **Integration tests: derivation traces.** They check a complete
   `prakriyA` and its final SLP1 output: `test-bavati-derivation` follows
   `BU + Sap + tip → Bavati`; `test-dadati-derivation` is planned to exercise
   an `apavAda` conflict between class 3 and the more general `Sap`-vikaraṇa.

### Adding a test

After adding a rule through `def-panini-rule`, add a unit test for every new
phonological operation and one complete integration trace for a word using it.
These are machine-prototype tests, not self-sufficient proof that a rule models
Pāṇini correctly; citation provenance and an evidence-bound derivation trace
are also required.

## Українська

Цей документ описує стратегію тестування `panini-machine-model-v0.1`.
Оскільки engine призначений для власної VM My Lisp, набір тестів написано
безпосередньо Lisp-ом.

## Розташування набору тестів

Тести містяться у [tests.my](tests.my).

## Запуск тестів

Після bootstrap VM My Lisp завантажте середовище й виконайте `(run-tests)`:

```lisp
> (load "panini/machine/compiler.my")
> (load "panini/machine/meta.my")
> (load "panini/machine/rules.my")
> (load "panini/machine/tests.my")
> (run-tests)
```

## Будова тестів

Набір використовує просту функцію `assert-equal` для перевірки state
transition.

### 1. Unit-тести: фонологія та морфологія

Перевіряють окремі helper-функції та операції над фонемами:

- `test-eco-sandhi` — Rule 6.1.78 (`e/o/ai/au + vowel → ay/av/Ay/Av`);
- `test-guna` — відповідність Rule 1.1.2 (`i → e`, `u → o`, `f → ar`).

### 2. Інтеграційні тести: traces деривації

Перевіряють повну деривацію (`prakriyA`) та фінальний SLP1 output:

- `test-bavati-derivation` — ланцюг `BU + Sap + tip → Bavati`;
- `test-dadati-derivation` — запланований тест конфлікту між класом 3 і
  загальнішим `Sap`-vikaraṇa через `apavAda`.

## Додавання тесту

Після додавання правила через `def-panini-rule`:

1. додайте unit-тест, якщо є нова фонологічна операція;
2. додайте повний integration trace для слова, яке цю операцію використовує.

Ці тести є machine prototype tests, а не самодостатнім доказом того, що
правило реалізує Паніні коректно. Для цього також потрібні citation provenance
та evidence-bound derivation trace.

## Deutsch

Dieses Dokument beschreibt die Teststrategie für `panini-machine-model-v0.1`.
Da die Engine für die My-Lisp-VM bestimmt ist, ist die Testsuite direkt in Lisp
geschrieben.

### Ort der Testsuite

Die Tests liegen in [tests.my](tests.my).

### Tests ausführen

Nach dem Bootstrap der My-Lisp-VM die Umgebung laden und `(run-tests)`
ausführen:

```lisp
> (load "panini/machine/compiler.my")
> (load "panini/machine/meta.my")
> (load "panini/machine/rules.my")
> (load "panini/machine/tests.my")
> (run-tests)
```

### Struktur der Tests

Die Suite verwendet einen kleinen Helfer `assert-equal`, um
Zustandsübergänge zu prüfen.

1. **Unit-Tests: Phonologie und Morphologie.** Sie prüfen einzelne
   Hilfsfunktionen und Phonemoperationen: `test-eco-sandhi` prüft Regel 6.1.78
   (`e/o/ai/au + vowel → ay/av/Ay/Av`); `test-guna` prüft die Entsprechung aus
   Regel 1.1.2 (`i → e`, `u → o`, `f → ar`).
2. **Integrationstests: Ableitungstraces.** Sie prüfen eine vollständige
   `prakriyA` und ihre finale SLP1-Ausgabe: `test-bavati-derivation` verfolgt
   `BU + Sap + tip → Bavati`; `test-dadati-derivation` ist geplant, um einen
   `apavAda`-Konflikt zwischen Klasse 3 und dem allgemeineren `Sap`-vikaraṇa
   zu prüfen.

### Einen Test hinzufügen

Nach dem Hinzufügen einer Regel mit `def-panini-rule` einen Unit-Test für jede
neue phonologische Operation und einen vollständigen Integrationstrace für ein
Wort, das sie verwendet, ergänzen. Diese Tests sind Tests eines
Maschinenprototyps, kein eigenständiger Nachweis, dass eine Regel Pāṇini korrekt
modelliert; Zitatprovenienz und ein evidenzgebundener Ableitungstrace sind
ebenfalls erforderlich.
