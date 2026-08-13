# Panini machine: runtime acceptance record — 2026-08-14

Status: `blocked`. This is an independently executed machine-compatibility
record. It is not a source claim about Pāṇini and it does not authorize edits
under `panini/machine/`.

## English

The supplied My Lisp executable was run from the Panini repository root with
the documented load sequence and `(run-tests)`. It did not reach the test
completion marker. The REPL itself exited with code 0 despite evaluation
diagnostics, so the new acceptance harness treats diagnostics as failures.

## Українська

### [PANINI]

Жодного панініївського твердження цей запис не робить. Це лише результат
виконання нашого machine prototype проти конкретного My Lisp runtime.

### [INTERPRETATION]

Виконано у WSL як користувач `my-lisp-panini`:

```sh
cd /mnt/c/GitHub/my-lisp-panini
guix shell -m manifest.scm -- \
  python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

Runtime revision: `bd36d21`. Стан My Lisp worktree був dirty, тому цей запуск
не є відтворюваним release-перевірянням. Фактичні blocker-и:

1. `compiler.my`, `rules.my` і `tests.my` використовують тричастинну форму
   `def`, тоді як runtime повідомляє «expected 2; received 3».
2. `siva-sutras.my` викликає відсутній symbol `last-char`.
3. Окремий Lisp-level probe показав, що поточний runtime також не має `if`,
   хоча наявний `tests.my` використовує цю форму. Це незалежний compatibility
   blocker, а не причина підміняти test entrypoint власною умовною логікою.
4. Через ці помилки `(run-tests)` лишається unknown symbol і completion marker
   `Tests complete.` не з'являється.
5. Інтерактивний REPL повернув process exit `0` попри diagnostics, тоді як
   прямий запуск `machine-acceptance.my` завершився nonzero під час load.
   Отже, transport mode теж є частиною test provenance; shell exit code без
   transcript сам по собі не є достатнім acceptance evidence.

Новий harness свідомо провалюється також на `Error:`, `[FAIL]`, `unknown
symbol` або відсутньому `Tests complete.`. Після виправлення machine owner має
повторити той самий command на зафіксованому runtime revision і прикласти
transcript до handoff.

### [MY-LISP HYPOTHESIS]

Це не висновок про Panini чи про нові My Lisp primitives. Це вимога до
інженерної доказовості: REPL diagnostics мають бути перетворені harness-ом на
machine-readable failure, доки сам runtime не надає надійний nonzero exit.

## Deutsch

Der My-Lisp-Runtime `bd36d21` erreichte `(run-tests)` nicht: dreiteilige
`def`-Formen und das fehlende `last-char` blockieren die Loads. Da die REPL
trotz Diagnosen mit Exit-Code 0 endete, wertet der neue Acceptance-Harness
Diagnosen und einen fehlenden Completion-Marker als Fehler. Der Lauf bleibt
`blocked`, bis der Machine-Owner ihn auf einer festgehaltenen Runtime-Revision
wiederholen kann.
