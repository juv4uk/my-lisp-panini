# Machine execution sweep — 2026-08-14

Scope: `PANINI-MACHINE-EXECUTION-SWEEP`. Environment: WSL user
`my-lisp-panini`, `guix shell -m manifest.scm`, runtime
`/mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe`.

## English — reference translation

### Result

The exact local executable does not satisfy the current Panini machine runtime
contract. The inspected My Lisp source checkout is revision
`4a9863920a2887eaace61882d4e0e389f668ccae`, while its available debug
executable reports `unknown symbol: sha256-hex`. Therefore it is stale relative
to the capability expected by the current acceptance fixture.

| Check | Result | Evidence |
|---|---|---|
| Runtime capability probe | FAIL | `sha256-hex` unknown; no probe markers reached |
| Portable negative loader | PASS | `malformed-def.my` and `unsupported-helper.my` rejected, 2/2 |
| Canonical machine acceptance | BLOCKED | same missing `sha256-hex`; acceptance entrypoint did not start |

This is an executable/runtime provenance observation, not a Paninian claim and
not a request to modify My Lisp. It does not contradict a separately reported
acceptance result run with another executable. Such a result remains
`peer-reported` here until the exact runtime and revision are independently
reproduced.

### Next safe action

Provide or build a My Lisp executable demonstrably matching the stated source
revision, then rerun the canonical order: capability probe, negative loader
suite, machine acceptance. Do not weaken fixtures or remove `sha256-hex` merely
to make this executable pass.

## Українська — нормативна

### Результат

Точний локальний executable не задовольняє поточний runtime contract Panini
machine. Оглянутий source checkout My Lisp має revision
`4a9863920a2887eaace61882d4e0e389f668ccae`, тоді як доступний debug executable
повертає `unknown symbol: sha256-hex`. Отже, він застарілий відносно можливості,
яку очікує поточний acceptance fixture.

| Перевірка | Результат | Evidence |
|---|---|---|
| Runtime capability probe | FAIL | `sha256-hex` невідомий; probe markers не досягнуті |
| Portable negative loader | PASS | `malformed-def.my` і `unsupported-helper.my` відхилено, 2/2 |
| Canonical machine acceptance | BLOCKED | той самий відсутній `sha256-hex`; acceptance entrypoint не стартував |

Це спостереження про provenance executable/runtime, не твердження про Паніні й
не запит змінювати My Lisp. Воно не суперечить окремо повідомленому acceptance
result, виконаному іншим executable. Такий результат тут лишається
`peer-reported`, доки exact runtime і revision не буде незалежно відтворено.

### Наступна безпечна дія

Надати або зібрати executable My Lisp, який доказово відповідає зазначеному
source revision, а тоді знову виконати canonical order: capability probe,
negative loader suite, machine acceptance. Не послаблювати fixture і не
видаляти `sha256-hex` лише для того, щоб цей executable пройшов перевірку.

## Deutsch — Referenzübersetzung

### Ergebnis

Die genaue lokale ausführbare Datei erfüllt den aktuellen Runtime-Vertrag der
Panini Machine nicht. Der geprüfte My-Lisp-Source-Checkout hat Revision
`4a9863920a2887eaace61882d4e0e389f668ccae`, die verfügbare Debug-Datei meldet
jedoch `unknown symbol: sha256-hex`. Sie ist daher gegenüber der vom aktuellen
Acceptance-Fixture erwarteten Fähigkeit veraltet.

| Prüfung | Ergebnis | Evidence |
|---|---|---|
| Runtime Capability Probe | FAIL | `sha256-hex` unbekannt; keine Probe-Marker erreicht |
| Portabler negativer Loader | PASS | `malformed-def.my` und `unsupported-helper.my` abgelehnt, 2/2 |
| Kanonische Machine Acceptance | BLOCKED | derselbe fehlende `sha256-hex`; Acceptance-Entrypoint startete nicht |

Dies ist eine Beobachtung über Executable-/Runtime-Provenance, keine Panini-
Behauptung und keine Aufforderung, My Lisp zu ändern. Ein mit einer anderen
Datei gemeldetes Ergebnis bleibt hier `peer-reported`, bis exakte Runtime und
Revision unabhängig reproduziert sind.

### Nächste sichere Handlung

Eine zum genannten Source-Revision nachweisbar passende My-Lisp-Datei bereit-
stellen oder bauen und dann die kanonische Reihenfolge erneut ausführen:
Capability Probe, negative Loader Suite, Machine Acceptance. Fixtures nicht
abschwächen und `sha256-hex` nicht nur für diesen Pass entfernen.
