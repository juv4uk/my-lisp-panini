# Panini → My Lisp bridge boundary

## English — reference translation

### Purpose

This document defines a **research boundary**, not an immediate integration
plan. `panini-foundation` reconstructs and tests a formal derivation model;
My Lisp is not its present target. A Paninian term — including `dhAtu`,
`saMjYA`, `kAraka`, `anuvftti`, or `asiddha` — does not become a My Lisp
primitive merely because it has a machine representation.

### What runs now

The canonical local Panini execution path is specified in
[`machine-execution-path-v0.1.md`](machine-execution-path-v0.1.md). It loads
the `panini/machine/` modules and runs the acceptance suite as an **isolated
executable experiment**. This tests one fixture's compatibility with My Lisp;
it does not integrate Panini into its parser, evaluator, VM, or semantic
reasoning system.

`panini/machine/panini-core.my` is an executable registry snapshot. The
authoritative structured records remain under `panini/registry/`; importing a
snapshot is not importing historical or philological claims into My Lisp.

### Evidence boundary and deferrals

Before any later step, use this evidence order: probe the exact runtime,
execute negative loader checks, run canonical acceptance, then reconcile the
result with Paninian sources and record provenance. A result run only by
another agent or executable is *peer-reported* until reproduced in the stated
environment. See the runtime capability contract and `machine/TESTING.md`.

Semantic-call parsing/evaluation, role surface syntax, treating kāraka as graph
edges or saṃjñā as types/tags, a general scheduler/conflict policy, and all VM,
inference, CUDA, and FPGA transfer are deferred. They require a corpus of
reproducible end-to-end derivations with complete evidence traces. When sources
leave applicability, precedence, or visibility open, `unknown`, `partial`, or
`blocked` is the correct outcome — never an unlabelled heuristic.

### Assertion levels and opening condition

Every bridge decision must distinguish `[PANINI]`, `[INTERPRETATION]`, and
`[MY-LISP HYPOTHESIS]`. Contextual visibility over immutable history is a
current machine model for studying `asiddha`; it is not a claim that My Lisp
already has, or must acquire, that semantics.

Bridge work may be considered only after **Panini Derivation Machine 0.1** has
reproducibly shown, for several different derivations, source, terms,
designations, immutable states, candidate rules, visibility, conflict
resolution, operations, surface result, and provenance for every decision.

## Українська — нормативна

### Призначення

Цей документ визначає **межу дослідження**, а не план негайної інтеграції.
`panini-foundation` реконструює та перевіряє формальну модель деривації;
My Lisp не є її поточною ціллю. Жоден термін Паніні — зокрема `dhAtu`,
`saMjYA`, `kAraka`, `anuvftti` чи `asiddha` — не стає primitive My Lisp лише
через наявність машинного представлення.

### Що виконується зараз

Канонічний локальний шлях перевірки Panini визначено у
[`machine-execution-path-v0.1.md`](machine-execution-path-v0.1.md). Він
завантажує модулі `panini/machine/` і запускає acceptance-набір як **ізольований
виконуваний експеримент**. Це перевіряє сумісність конкретного fixture з
My Lisp, але не інтегрує Panini в його parser, evaluator, VM або систему
семантичного виведення.

`panini/machine/panini-core.my` є виконуваним snapshot реєстрів; його
авторитетні структуровані дані лишаються в `panini/registry/`. Перенесення
snapshot у My Lisp не є перенесенням історичних або філологічних тверджень.

### Межа доказів і відкладення

Перед будь-яким наступним кроком застосовується такий порядок доказів:
перевірити можливості конкретного runtime, запустити негативні loader-перевірки,
запустити canonical acceptance-набір, а потім звірити результат із джерелами
Panini та provenance запису. Результат, який виконано лише іншим агентом або
іншим бінарником, позначається як *peer-reported*, доки його не відтворено у
визначеному середовищі. Деталі — у
[`mylisp-runtime-capability-contract.md`](mylisp-runtime-capability-contract.md)
та [`machine/TESTING.md`](../machine/TESTING.md).

Свідомо відкладено: semantic call у parser/evaluator, канонічний surface-синтаксис
ролей, перетворення kāraka на graph edge або `saMjYA` на type/tag, загальний
scheduler/conflict policy і перенесення до VM, inference engine, CUDA чи FPGA.
Для цього потрібен корпус відтворюваних end-to-end деривацій з повним evidence
trace. Якщо джерело не визначає застосовність, precedence або visibility,
коректний результат — `unknown`, `partial` чи `blocked`, а не непозначена
евристика.

### Рівні тверджень і умова відкриття мосту

Кожне майбутнє bridge-рішення мусить явно розділяти:

```text
[PANINI]             Що засвідчують sūtra та джерела.
[INTERPRETATION]     Як це пояснює дослідник або реалізація.
[MY-LISP HYPOTHESIS] Яку обмежену обчислювальну аналогію ми перевіряємо.
```

Наприклад, contextual visibility над immutable history є поточною машинною
моделлю для дослідження `asiddha`; це не твердження, що My Lisp уже має або
повинен мати таку семантику.

Обговорення інтеграції дозволене лише після milestone **Panini Derivation
Machine 0.1**: кілька різних деривацій мають відтворювано показувати source,
terms, designations, immutable states, candidate rules, visibility, conflict
resolution, operations, surface result та повний доказ походження кожного
рішення. Тоді окремо оцінюється, що є даними, алгоритмом, зручністю реалізації
або справді корисною абстракцією My Lisp.

## Deutsch — Referenzübersetzung

### Zweck

Dieses Dokument beschreibt eine **Forschungsgrenze**, keinen unmittelbaren
Integrationsplan. `panini-foundation` rekonstruiert und prüft ein formales
Modell der Derivation; My Lisp ist gegenwärtig nicht sein Ziel. Ein
paninischer Begriff wie `dhAtu`, `saMjYA`, `kAraka`, `anuvftti` oder `asiddha`
wird nicht allein wegen einer Maschinenrepräsentation zu einem My-Lisp-Primitive.

### Der gegenwärtig ausführbare Teil

Der kanonische lokale Ausführungspfad steht in
[`machine-execution-path-v0.1.md`](machine-execution-path-v0.1.md). Er lädt
`panini/machine/` und führt die Acceptance-Suite als **isoliertes ausführbares
Experiment** aus. Damit wird die Kompatibilität eines bestimmten Fixture mit
My Lisp geprüft, nicht Panini in Parser, Evaluator, VM oder semantisches
Schließen integriert.

`panini/machine/panini-core.my` ist ein ausführbarer Snapshot der Register;
die autoritativen strukturierten Datensätze bleiben in `panini/registry/`.

### Beweisgrenze und Aufschub

Vor jedem weiteren Schritt gilt: exakte Runtime prüfen, negative Loader-Tests
ausführen, die kanonische Acceptance ausführen und das Ergebnis mit Quellen und
Provenance abgleichen. Ein Ergebnis eines anderen Agenten oder einer anderen
ausführbaren Datei bleibt *peer-reported*, bis es in der angegebenen Umgebung
reproduziert wurde.

Semantic Calls im Parser/Evaluator, Rollensyntax, die Gleichsetzung von kāraka
mit Graphkanten oder saṃjñā mit Typen/Tags, ein allgemeiner Scheduler sowie
VM-, Inference-, CUDA- und FPGA-Übertragungen werden bewusst aufgeschoben.
Ohne belegte Anwendbarkeit, Präzedenz oder Sichtbarkeit sind `unknown`,
`partial` oder `blocked` korrekt — keine unmarkierte Heuristik.

### Aussageebenen und Öffnungsbedingung

Jede Bridge-Entscheidung trennt `[PANINI]`, `[INTERPRETATION]` und
`[MY-LISP HYPOTHESIS]`. Kontextuelle Sichtbarkeit über unveränderlicher Historie
ist ein Maschinenmodell zur Untersuchung von `asiddha`, nicht die Behauptung,
dass My Lisp diese Semantik bereits hat oder erhalten muss.

Die Brücke wird erst nach **Panini Derivation Machine 0.1** erwogen: mehrere
unterschiedliche Derivationen müssen vollständig, unveränderlich, erklärbar
und mit Provenance reproduzierbar sein.
