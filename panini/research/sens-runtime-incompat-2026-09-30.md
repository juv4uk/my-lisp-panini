# machine/ на рантаймі SENS: що ламається (2026-09-30)

Read-only дослідження; код не змінено. Бінарник: `/home/agents/GitHub/sens/target/release/sens` (sens HEAD 2bd0f3d5, 2026-09-29).

## Що запускав

- `sens panini/tests/machine-acceptance.lisp` на `master`: падає одразу, `failed to read file panini/machine/runtime-prelude.my` (старі `.my`-шляхи після міграції 81dde7c). Це виправляє PR #25.
- Те саме на гілці `fix/loader-paths-after-lisp-migration` (PR #25): `load` проходить (prelude читається), далі `Error: unknown symbol: atom`.
- Проби окремих виразів у SENS: `(atom 1)` і `(pair? …)`, `(null? …)`: unknown symbol. `(atom? 1)` повертає `(structural-kind atom)`, `(eq 1 1)` і `(eq? 1 1)` повертають `(identity-relation same)`, а не булеве значення.

## Висновок (з проб; повного аналізу коду SENS не робив)

`panini/machine/*.lisp` написано під рантайм, де `atom`, `eq`, `null?` булеві й без префікса (старий My Lisp). У SENS `atom` немає, а предикати повертають структурні значення. У `machine/` символ `(atom …)` зустрічається в 16 файлах (напр. `derivation.lisp` 32, `sandhi.lisp` 10). Тож після PR #25 тести все одно не проходять: потрібне окреме рішення, портувати `machine/` на семантику SENS чи тримати старий рантайм (`my-lisp.exe`) для цих тестів. Це архітектурний вибір, не механічна заміна: одна лише підміна `atom`→`atom?` дасть не-булеві результати в `cond`.

## Не перевірено

- Чи в SENS є булевий режим чи префлюд для сумісності (я не шукав у його документації).
- Чи старий `my-lisp.exe` (Windows) проходить `machine-acceptance.lisp` після #25 (його запуск у цій сесії заблоковано).
