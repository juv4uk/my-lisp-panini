# Testing Panini Machine Model / Тестування Panini Machine Model / Tests des Panini-Maschinenmodells

## English

This document describes the testing strategy for `panini-machine-model-v0.1`.
Because the engine targets the My Lisp VM, its test suite is written directly
in Lisp.

### Test-suite location

The executable entry point is [machine-acceptance.my](../tests/machine-acceptance.my).
The machine assertions themselves are in [tests.my](tests.my).

### Running tests

Run the Lisp entry point from repository root. It loads the narrow macro-free
fixture prelude before the machine modules and then invokes `(run-tests)`. This
keeps acceptance evidence independent of changes in the shared My Lisp core:

```lisp
$ /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe panini/tests/machine-acceptance.my
```

### Test structure

The suite uses a small `assert-equal` helper to check state transitions.

1. **Unit tests: phonology and morphology.** They cover individual helper
   functions and phoneme operations: `test-eco-sandhi` checks Rule 6.1.78
   (`e/o/ai/au + vowel → ay/av/Ay/Av`); `test-guna` checks the Rule 1.1.2
   correspondence (`i → e`, `u → o`, `f → ar`).
2. **Integration tests: machine fixtures.** They check narrow executable
   fixture outputs, not complete historical derivation traces:
   - `test-prototype-derivations` checks the fixture outputs `Bavati`, `dadAti`, and `kArayati`.
   - `test-dadati-declared-conflict` checks both rule IDs, the declared
     `utsarga` link, the trace reason `apavAda`, the selected 2.4.75 fixture,
     and visible Slu transition tags.

### Adding a test

After adding a rule through `def-panini-rule`, add a unit test for every new
phonological operation and one complete integration trace for a word using it.
These are machine-prototype tests, not self-sufficient proof that a rule models
Pāṇini correctly; citation provenance and an evidence-bound derivation trace
are also required.

### Latest executed acceptance result

On 2026-08-14, the Lisp entry point was executed in WSL as user
`my-lisp-panini` against My Lisp revision `bd36d21`:

```sh
cd /mnt/c/GitHub/my-lisp-panini
python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

Result: **PASS** — 22 assertions printed `[PASS]`, no `[FAIL]` or runtime
diagnostics appeared, and `Tests complete.` was reached. The runtime worktree
was dirty, so this is execution evidence, not release certification. The entry
point uses `runtime-prelude.my`, not the currently changing shared core. The
three derivation outputs and the `dadAti` conflict fields are deliberately
`machine-fixture` records: this proves VM compatibility and declared fixture
behavior, not complete historical Pāṇinian derivations.

## Українська

Цей документ описує стратегію тестування `panini-machine-model-v0.1`.
Оскільки engine призначений для власної VM My Lisp, набір тестів написано
безпосередньо Lisp-ом.

### Розташування набору тестів

Виконувана точка входу — [machine-acceptance.my](../tests/machine-acceptance.my).
Самі machine assertions містяться у [tests.my](tests.my).

### Запуск тестів

Запускайте Lisp entrypoint із кореня репозиторію. Він спершу завантажує вузький
macro-free fixture prelude, далі machine-модулі й `(run-tests)`. Це зберігає
evidence виконання незалежним від змін у спільному My Lisp core:

```lisp
$ /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe panini/tests/machine-acceptance.my
```

### Будова тестів

Набір використовує просту функцію `assert-equal` для перевірки state
transition.

1. **Unit-тести: фонологія та морфологія**
   Перевіряють окремі helper-функції та операції над фонемами:
   - `test-eco-sandhi` — Rule 6.1.78 (`e/o/ai/au + vowel → ay/av/Ay/Av`);
   - `test-guna` — відповідність Rule 1.1.2 (`i → e`, `u → o`, `f → ar`).

2. **Інтеграційні тести: machine fixtures**
Перевіряють вузькі виконувані fixture outputs, а не повні історичні traces
деривації:
- `test-prototype-derivations` — outputs `Bavati`, `dadAti`, `kArayati`.
- `test-dadati-declared-conflict` — обидва ID правил, оголошений зв'язок
  `utsarga`, причину trace `apavAda`, обраний fixture 2.4.75 і видимі
  transition tags Slu.

### Додавання тесту

Після додавання правила через `def-panini-rule`:
1. додайте unit-тест, якщо є нова фонологічна операція;
2. додайте повний integration trace для слова, яке цю операцію використовує.

Ці тести є machine prototype tests, а не самодостатнім доказом того, що
правило реалізує Паніні коректно. Для цього також потрібні citation provenance
та evidence-bound derivation trace.

### Останній виконаний acceptance result

2026-08-14 Lisp entrypoint виконано у WSL користувачем `my-lisp-panini` проти
My Lisp revision `bd36d21`:

```sh
cd /mnt/c/GitHub/my-lisp-panini
python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

Результат: **PASS** — 22 assertions надрукували `[PASS]`, не з'явилися
`[FAIL]` або runtime diagnostics, досягнуто `Tests complete.`. Worktree
runtime був dirty, тому це evidence виконання, а не release certification.
Entrypoint використовує `runtime-prelude.my`, а не спільний core, що зараз
змінюється. Три derivation outputs і conflict fields `dadAti` навмисно є
`machine-fixture` records: це доводить сумісність із VM і оголошену поведінку
fixture, а не complete історичні деривації Паніні.

## Deutsch

Dieses Dokument beschreibt die Teststrategie für `panini-machine-model-v0.1`.
Da die Engine für die My-Lisp-VM bestimmt ist, ist die Testsuite direkt in Lisp
geschrieben.

### Ort der Testsuite

Der ausführbare Einstiegspunkt ist [machine-acceptance.my](../tests/machine-acceptance.my).
Die Machine-Assertions liegen in [tests.my](tests.my).

### Tests ausführen

Den Lisp-Einstiegspunkt vom Repository-Stamm ausführen. Er lädt zuerst ein
schmales makrofreies Fixture-Prelude, dann die Maschinenmodule und
`(run-tests)`. Dadurch bleibt die Ausführungsevidenz von Änderungen am
gemeinsamen My-Lisp-Core unabhängig:

```lisp
$ /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe panini/tests/machine-acceptance.my
```

### Struktur der Tests

Die Suite verwendet einen kleinen Helfer `assert-equal`, um
Zustandsübergänge zu prüfen.

1. **Unit-Tests: Phonologie und Morphologie.** Sie prüfen einzelne
   Hilfsfunktionen und Phonemoperationen: `test-eco-sandhi` prüft Regel 6.1.78
   (`e/o/ai/au + vowel → ay/av/Ay/Av`); `test-guna` prüft die Entsprechung aus
   Regel 1.1.2 (`i → e`, `u → o`, `f → ar`).
2. **Integrationstests: Machine-Fixtures.** Sie prüfen enge ausführbare
   Fixture-Ausgaben, keine vollständigen historischen Ableitungstraces:
   - `test-prototype-derivations` prüft `Bavati`, `dadAti` und `kArayati`.
   - `test-dadati-declared-conflict` prüft beide Regel-IDs, die deklarierte
     `utsarga`-Verknüpfung, den Trace-Grund `apavAda`, das Fixture 2.4.75 und
     sichtbare Slu-Übergangstags.

### Einen Test hinzufügen

Nach dem Hinzufügen einer Regel mit `def-panini-rule` einen Unit-Test für jede
neue phonologische Operation und einen vollständigen Integrationstrace für ein
Wort, das sie verwendet, ergänzen. Diese Tests sind Tests eines
Maschinenprototyps, kein eigenständiger Nachweis, dass eine Regel Pāṇini korrekt
modelliert; Zitatprovenienz und ein evidenzgebundener Ableitungstrace sind
ebenfalls erforderlich.

### Letztes ausgeführtes Acceptance-Ergebnis

Am 2026-08-14 wurde der Lisp-Einstiegspunkt in WSL als Nutzer
`my-lisp-panini` gegen My-Lisp-Revision `bd36d21` ausgeführt:

```sh
cd /mnt/c/GitHub/my-lisp-panini
python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

Ergebnis: **PASS** — 22 Assertions gaben `[PASS]` aus, ohne `[FAIL]` oder
Runtime-Diagnosen; `Tests complete.` wurde erreicht. Der Runtime-Worktree war
dirty, daher ist dies Ausführungsevidenz und keine Release-Zertifizierung. Der
Einstiegspunkt verwendet `runtime-prelude.my`, nicht den sich aktuell ändernden
gemeinsamen Core. Die drei Derivationsausgaben und die `dadAti`-Konfliktfelder
sind absichtlich `machine-fixture`-Records: Der Test belegt VM-Kompatibilität
und deklariertes Fixture-Verhalten, keine vollständigen historischen
Pāṇini-Ableitungen.
