# Machine-test execution audit / Аудит виконання machine-тестів / Audit der Machine-Testausführung

## English

Read-only run on 2026-08-13 did not execute the suite. `tests.my` loads a Windows path absent in WSL; `siva-sutras.my` reports unknown `last-char`; `rules.my` reports `def: expected 2; received 3`. The piped Windows input also began with a BOM. No passing `run-tests` or executable `dadAti` conflict claim may be reported until an owned task resolves these blockers.

## Українська

Read-only запуск 2026-08-13 не виконав набір тестів. `tests.my` завантажує Windows-шлях, відсутній у WSL; `siva-sutras.my` має unknown `last-char`; `rules.my` має `def: expected 2; received 3`. Windows stdin у пайпі також починався з BOM. Не можна повідомляти про passing `run-tests` або executable conflict claim для `dadAti`, поки окрема owned задача не усуне блокери.

## Deutsch

Der Read-only-Lauf am 2026-08-13 führte die Suite nicht aus. `tests.my` lädt einen in WSL fehlenden Windows-Pfad; `siva-sutras.my` meldet unbekanntes `last-char`; `rules.my` meldet `def: expected 2; received 3`. Der gepipte Windows-Eingang begann außerdem mit einem BOM. Bis eine eigene Aufgabe diese Blocker behebt, darf kein erfolgreicher `run-tests`-Lauf oder ausführbarer dadAti-Konfliktclaim gemeldet werden.

## Isolated source facts / Локалізовані факти коду / Isolierte Source-Fakten

**English.** Direct execution isolates `rules.my:35`: `(def make-term
(upadesha type) ...)` is incompatible with the current two-form `def`; and
`siva-sutras.my:27`: `last-char` is unavailable in the current runtime.

**Українська.** Прямий запуск локалізує `rules.my:35`: `(def make-term
(upadesha type) ...)` несумісний із поточним двоформним `def`; та
`siva-sutras.my:27`: `last-char` відсутній у поточному runtime.

**Deutsch.** Direkte Ausführung isoliert `rules.my:35`: `(def make-term
(upadesha type) ...)` ist mit dem aktuellen zweiformigen `def` unvereinbar;
und `siva-sutras.my:27`: `last-char` fehlt im aktuellen Runtime.
