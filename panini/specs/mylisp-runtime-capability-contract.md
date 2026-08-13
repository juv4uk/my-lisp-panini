# My Lisp runtime capability contract / Контракт можливостей runtime My Lisp / My-Lisp-Runtimefähigkeitsvertrag

## English

### Purpose

Panini acceptance evidence applies to one exact executable, not merely to a
nearby My Lisp source checkout. This contract records the minimum observable
capabilities required by the current machine fixtures and prevents an
unexplained source/binary mismatch from being reported as a Panini regression.

### Required evidence

Run the offline probe with the executable and, when available, its source
checkout:

```sh
python3 panini/tests/probe_mylisp_runtime.py \
  --runtime /path/to/my-lisp \
  --source-repo /path/to/my-lisp-source
```

The probe requires `sha256-hex` with the SHA-256 digest of `"abc"`,
`string-append`, ordinary file execution, and a clean completion marker. A
handoff records runtime path, source revision, exact command, probe result,
acceptance result, and loader-negative result. The probe never builds or edits
My Lisp.

### Boundary

Passing proves only that this runtime can execute the current Panini fixture
surface. It does not approve parser/evaluator integration, establish a
Pāṇinian claim, or authorize changes to My Lisp.

## Українська

### Призначення

Panini acceptance evidence стосується одного точного executable, а не просто
сусіднього checkout вихідного коду My Lisp. Цей контракт фіксує мінімальні
спостережувані можливості, потрібні поточним machine fixtures, і не дозволяє
подавати не пояснений source/binary mismatch як регресію Паніні.

### Обов'язковий доказ

Запускайте offline probe з executable і, за наявності, його source checkout:

```sh
python3 panini/tests/probe_mylisp_runtime.py \
  --runtime /path/to/my-lisp \
  --source-repo /path/to/my-lisp-source
```

Probe вимагає `sha256-hex` із SHA-256 digest для `"abc"`, `string-append`,
звичайне виконання файлу та чистий completion marker. Handoff фіксує runtime
path, source revision, точну команду, результат probe, acceptance і
loader-negative result. Probe ніколи не будує й не редагує My Lisp.

### Межа

Проходження доводить лише, що саме цей runtime виконує поточну Panini fixture
surface. Воно не затверджує parser/evaluator integration, не встановлює
панініївського твердження та не дозволяє змінювати My Lisp.

## Deutsch

### Zweck

Panini-Acceptance-Evidenz gilt für ein genaues Executable, nicht bloß für einen
benachbarten My-Lisp-Source-Checkout. Dieser Vertrag hält die minimalen
beobachtbaren Fähigkeiten der aktuellen Machine-Fixtures fest und verhindert,
dass ein unerklärter Source/Binary-Mismatch als Panini-Regression erscheint.

### Erforderliche Evidenz

Den Offline-Probe mit Executable und, wenn vorhanden, Source-Checkout starten:

```sh
python3 panini/tests/probe_mylisp_runtime.py \
  --runtime /path/to/my-lisp \
  --source-repo /path/to/my-lisp-source
```

Der Probe verlangt `sha256-hex` mit dem SHA-256-Digest von `"abc"`,
`string-append`, normale Dateiausführung und einen sauberen Abschlussmarker.
Ein Handoff hält Runtime-Pfad, Source-Revision, genauen Befehl, Probe-Ergebnis,
Acceptance-Ergebnis und Loader-Negativ-Ergebnis fest. Der Probe baut oder
bearbeitet My Lisp nie.

### Grenze

Ein Bestehen beweist nur, dass diese Runtime die aktuelle Panini-Fixture-
Oberfläche ausführen kann. Es bestätigt keine Parser-/Evaluatorintegration,
keine Pāṇini-Behauptung und erlaubt keine Änderungen an My Lisp.
