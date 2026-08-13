# Panini machine: runtime acceptance record — 2026-08-14

Status: `passed-with-boundaries`. This is an independently executed machine-compatibility
record. It is not a source claim about Pāṇini and it does not authorize edits
under `panini/machine/`.

## English

The supplied My Lisp executable was run from the Panini repository root with
the documented load sequence and `(run-tests)`. After the compatibility
rewrite, it reaches the completion marker and reports 14 passing assertions.
The harness still treats REPL diagnostics as failures.

## Українська

### [PANINI]

Жодного панініївського твердження цей запис не робить. Це лише результат
виконання нашого machine prototype проти конкретного My Lisp runtime.

### [INTERPRETATION]

Повторно виконано у WSL як користувач `my-lisp-panini`:

```sh
cd /mnt/c/GitHub/my-lisp-panini
guix shell -m manifest.scm -- \
  python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

Runtime revision: `bd36d21`. Стан My Lisp worktree був dirty, тому цей запуск
не є відтворюваним release-перевірянням. Початкові blocker-и були усунені в
`panini/machine/` без зміни My Lisp runtime:

1. Тричастинний `def` замінено формою `(def name (lambda (...) ...))`.
2. Виклики `last-char` замінено локальним `list-last`.
3. `if`, `setq`, `defmacro` з `&key` та інші непідтримувані форми прибрано з
   виконуваного machine path; entrypoint спершу завантажує документований
   `../my-lisp/lib/core.my`.
4. Прямий запуск `machine-acceptance.my` тепер завершується code `0`, друкує
   14 `[PASS]` і `Tests complete.`; harness теж повертає `0`.

Залишкові межі: runtime revision є dirty, а `derive-Bavati`, `derive-dadAti`
і `derive-kArayati` — вузькі `machine-fixture` outputs. Вони підтверджують
сумісність execution path, але не доводять complete Paninian derivation.

Новий harness свідомо провалюється також на `Error:`, `[FAIL]`, `unknown
symbol` або відсутньому `Tests complete.`. Після виправлення machine owner має
повторити той самий command на зафіксованому runtime revision і прикласти
transcript до handoff.

### [MY-LISP HYPOTHESIS]

Це не висновок про Panini чи про нові My Lisp primitives. Це вимога до
інженерної доказовості: REPL diagnostics мають бути перетворені harness-ом на
machine-readable failure, доки сам runtime не надає надійний nonzero exit.

## Deutsch

Der My-Lisp-Runtime `bd36d21` erreicht nach der Kompatibilitätsanpassung
`(run-tests)`: 14 Assertions bestehen und der Completion-Marker erscheint.
Die dreiteilige `def`-Form, `last-char`, `if`, `setq` und das unpassende
Macro-Profil wurden aus dem ausführbaren Pfad entfernt. Der Lauf bleibt wegen
des dirty Runtime-Worktrees und der bewusst schmalen machine-fixture outputs
nicht als vollständige Panini-Ableitung ausgewiesen.
