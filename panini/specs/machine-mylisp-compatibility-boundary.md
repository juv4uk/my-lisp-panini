# Machine / My Lisp compatibility boundary

## English

### Status

This is a design and verification boundary, not a change to either runtime.
It records the blockers found by the read-only execution audit on 2026-08-13
and assigns implementation ownership to the Panini-machine maintainer.

### Observed blockers

1. `panini/machine/tests.my` loads a host-specific `c:/GitHub/...` path.
2. `panini/machine/rules.my` uses a three-part `def` form, while the current
   My Lisp runtime accepts `(def name expression)`.
3. `panini/machine/siva-sutras.my` refers to `last-char`, which is not
   available in the current My Lisp runtime.

### Compatibility contract

- A machine source file must define parameterized helpers through the documented
  `(def name (lambda (...) ...))` form unless My Lisp explicitly adds and
  documents another form.
- A machine helper may use only documented My Lisp core operations, or define
  its own small local helper with tests. It must not assume an undocumented
  `last-char` primitive.
- The test entry point must resolve source files without a checkout-specific
  absolute path. A portable loader design must be validated from the repository
  root in WSL before it is described as cross-platform.
- Test transport is separate from language semantics: a BOM introduced by a
  Windows pipeline is a harness input defect, not evidence about parsing.

### Acceptance evidence

The owner may close the implementation task only after recording all of:

1. Direct loading of `siva-sutras.my`, `compiler.my`, `rules.my`, and
   `tests.my` under the declared WSL/Guix environment.
2. An executable `run-tests` invocation that reaches the dadAti conflict test.
3. One negative test for an unsupported helper or malformed `def` form.
4. The exact command, runtime revision, and result in the task handoff.

### Ownership boundary

Panini-2 owns this contract and independent verification. Panini-1 / the
Antigravity machine maintainer owns edits under `panini/machine/`. My Lisp owns
any change to the language surface. No side may infer approval to change the
other side from this document.

## Українська

### Статус

Це межа проєктування й перевірки, а не зміна будь-якого runtime. Документ
фіксує блокери з read-only аудиту 2026-08-13 і залишає реалізацію власникові
Panini-machine.

### Виявлені блокери

1. `panini/machine/tests.my` завантажує прив'язаний до хоста шлях
   `c:/GitHub/...`.
2. `panini/machine/rules.my` використовує тричастинну форму `def`, тоді як
   поточний My Lisp приймає `(def name expression)`.
3. `panini/machine/siva-sutras.my` посилається на `last-char`, якого немає в
   поточному My Lisp runtime.

### Контракт сумісності

- Параметризований helper у machine-коді треба визначати документованою формою
  `(def name (lambda (...) ...))`, доки My Lisp явно не додасть іншу форму.
- Helper може використовувати лише документовані core-операції My Lisp або
  власний малий локальний helper з тестами. Не можна припускати primitive
  `last-char`, якого немає в документації.
- Точка входу тестів не повинна залежати від абсолютного шляху конкретного
  checkout. Portable loader треба перевірити з кореня репозиторію у WSL, перш
  ніж називати його cross-platform.
- Транспорт тесту відокремлений від семантики мови: BOM із Windows pipeline є
  дефектом вводу harness, а не доказом про parser.

### Докази прийняття

Власник може закрити задачу реалізації лише після фіксації всього такого:

1. Прямого завантаження `siva-sutras.my`, `compiler.my`, `rules.my` і
   `tests.my` у задекларованому WSL/Guix середовищі.
2. Виклику `run-tests`, який справді доходить до dadAti conflict test.
3. Одного negative test для непідтримуваного helper або некоректної форми
   `def`.
4. Точної команди, revision runtime і результату в handoff задачі.

### Межа відповідальності

Panini-2 відповідає за цей контракт та незалежну перевірку. Panini-1 /
Antigravity-власник machine відповідає за зміни в `panini/machine/`. My Lisp
відповідає за зміни мовної поверхні. Цей документ не дає жодній стороні
дозволу змінювати частину іншої.

## Deutsch

### Status

Dies ist eine Entwurfs- und Verifikationsgrenze, keine Runtime-Aenderung. Sie
hält die im Read-only-Audit vom 2026-08-13 gefundenen Blocker fest und lässt
die Umsetzung beim Panini-Machine-Verantwortlichen.

### Beobachtete Blocker

1. `panini/machine/tests.my` lädt einen hostgebundenen Pfad `c:/GitHub/...`.
2. `panini/machine/rules.my` verwendet eine dreiteilige `def`-Form, waehrend
   das aktuelle My Lisp `(def name expression)` erwartet.
3. `panini/machine/siva-sutras.my` verwendet nicht vorhandenes `last-char`.

### Kompatibilitaetsvertrag

- Parametrisierte Helper verwenden die dokumentierte Form
  `(def name (lambda (...) ...))`.
- Es dürfen nur dokumentierte My-Lisp-Core-Operationen oder getestete lokale
  Helper verwendet werden.
- Der Test-Einstiegspunkt darf keinen checkout-spezifischen absoluten Pfad
  brauchen; der Loader ist in WSL vom Repository-Stamm zu pruefen.
- Ein BOM aus einer Windows-Pipeline ist ein Harness-Eingabefehler, keine
  Parser-Aussage.

### Abnahmebelege

Erforderlich sind direkte Loads aller vier Machine-Dateien, ein `run-tests`
bis zum dadAti-Konflikttest, ein negativer Test und die genaue Ausfuehrungs-
provenienz im Handoff.

### Verantwortungsgrenze

Panini-2 pflegt Vertrag und unabhängige Prüfung. Panini-1 / Antigravity pflegt
`panini/machine/`; My Lisp pflegt seine Sprachoberfläche.
