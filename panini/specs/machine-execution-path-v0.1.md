# Machine execution path v0.1 / Шлях виконання машини v0.1 / Ausführungspfad der Maschine v0.1

## English

### Canonical executable path

The only canonical executable path for `panini-machine-model-v0.1` is
`panini/tests/machine-acceptance.my`. It loads, in this order:

1. `runtime-prelude.my`;
2. `compiler.my`, `meta.my`, `siva-sutras.my`, and `rules.my`;
3. `panini-core.my` as a machine snapshot and compatibility fixture;
4. `tests.my`, then `(run-tests)`.

The companion acceptance runner and runtime probe are the canonical host-side
entry points. A result is meaningful only after the runtime capability probe
passes for that exact executable.

### Boundary

`panini-core.my` is executable but remains a bounded snapshot; the YAML
registries, especially `registry/dhatu/*.yaml`, remain authoritative project
data. Files not loaded by this entry point are research or support artifacts,
not implicit runtime modules. This declaration does not promote the machine
fixture to a complete Pāṇinian derivation or a My Lisp language feature.

### Evidence order

```text
runtime capability probe
        → loader-negative suite
        → machine acceptance suite
        → source/evidence review for each derivation claim
```

## Українська

### Канонічний виконуваний шлях

Єдиний канонічний виконуваний шлях для `panini-machine-model-v0.1` —
`panini/tests/machine-acceptance.my`. Він завантажує в такому порядку:

1. `runtime-prelude.my`;
2. `compiler.my`, `meta.my`, `siva-sutras.my` і `rules.my`;
3. `panini-core.my` як machine snapshot і compatibility fixture;
4. `tests.my`, а потім `(run-tests)`.

Супровідні acceptance runner і runtime probe є канонічними host-side точками
входу. Результат має значення лише після успішного runtime capability probe
саме для цього executable.

### Межа

`panini-core.my` є виконуваним, але лишається обмеженим snapshot; YAML
реєстри, особливо `registry/dhatu/*.yaml`, лишаються авторитетними даними
проєкту. Файли, які не завантажує цей entrypoint, є research або support
artifacts, а не неявними runtime modules. Це оголошення не підносить machine
fixture до повної панініївської деривації чи мовної можливості My Lisp.

### Порядок evidence

```text
runtime capability probe
        → loader-negative suite
        → machine acceptance suite
        → source/evidence review кожного твердження про деривацію
```

## Deutsch

### Kanonischer ausführbarer Pfad

Der einzige kanonische ausführbare Pfad für `panini-machine-model-v0.1` ist
`panini/tests/machine-acceptance.my`. Er lädt in dieser Reihenfolge:

1. `runtime-prelude.my`;
2. `compiler.my`, `meta.my`, `siva-sutras.my` und `rules.my`;
3. `panini-core.my` als Machine-Snapshot und Kompatibilitätsfixture;
4. `tests.my`, dann `(run-tests)`.

Der zugehörige Acceptance-Runner und Runtime-Probe sind die kanonischen
Host-seitigen Einstiegspunkte. Ein Ergebnis ist erst sinnvoll, wenn der
Runtime-Capability-Probe für genau dieses Executable besteht.

### Grenze

`panini-core.my` ist ausführbar, bleibt jedoch ein begrenzter Snapshot; die
YAML-Register, besonders `registry/dhatu/*.yaml`, bleiben autoritative
Projektdaten. Dateien, die dieser Einstiegspunkt nicht lädt, sind Forschungs-
oder Support-Artefakte, keine impliziten Runtime-Module. Diese Erklärung hebt
das Machine-Fixture weder zu einer vollständigen Pāṇini-Derivation noch zu
einem My-Lisp-Sprachmerkmal.

### Evidenzreihenfolge

```text
runtime capability probe
        → loader-negative suite
        → machine acceptance suite
        → source/evidence review jeder Derivationsbehauptung
```

## Portable gate runner / Портативний gate runner / Portabler Gate-Runner

### English

`panini/tests/run_portable_machine_gate.py` is the single host-side command
that executes the canonical order without suppressing later evidence after an
earlier failure. Invoke it with `--runtime` and, where available,
`--source-repo`. A nonzero result means the gate is blocked or failing; it is
not by itself a claim about Panini.

### Українська

`panini/tests/run_portable_machine_gate.py` є єдиною host-side командою, що
виконує canonical order і не приховує наступні докази після раннього FAIL.
Виклик: `--runtime` і, за наявності, `--source-repo`. Ненульовий результат
означає, що gate заблокований або не проходить; сам по собі він не є
твердженням про Паніні.

### Deutsch

`panini/tests/run_portable_machine_gate.py` ist der einzige Host-seitige
Befehl für die kanonische Reihenfolge und unterdrückt spätere Evidence nicht
nach einem frühen FAIL. Mit `--runtime` und gegebenenfalls `--source-repo`
aufrufen. Ein Exit ungleich null bedeutet blockiertes oder fehlendes Gate,
keine Panini-Behauptung.
