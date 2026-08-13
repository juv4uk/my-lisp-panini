# Тестування Panini Machine Model

Цей документ описує стратегію тестування `panini-machine-model-v0.1`.
Оскільки engine призначений для власної VM My Lisp, набір тестів написано
безпосередньо Lisp-ом.

## Розташування набору тестів

Тести містяться у [tests.my](tests.my).

## Запуск тестів

Після bootstrap VM My Lisp завантажте середовище й виконайте `(run-tests)`:

```lisp
> (load "panini/machine/compiler.my")
> (load "panini/machine/meta.my")
> (load "panini/machine/rules.my")
> (load "panini/machine/tests.my")
> (run-tests)
```

## Будова тестів

Набір використовує просту функцію `assert-equal` для перевірки state
transition.

### 1. Unit-тести: фонологія та морфологія

Перевіряють окремі helper-функції та операції над фонемами:

- `test-eco-sandhi` — Rule 6.1.78 (`e/o/ai/au + vowel → ay/av/Ay/Av`);
- `test-guna` — відповідність Rule 1.1.2 (`i → e`, `u → o`, `f → ar`).

### 2. Інтеграційні тести: traces деривації

Перевіряють повну деривацію (`prakriyA`) та фінальний SLP1 output:

- `test-bavati-derivation` — ланцюг `BU + Sap + tip → Bavati`;
- `test-dadati-derivation` — запланований тест конфлікту між класом 3 і
  загальнішим `Sap`-vikaraṇa через `apavAda`.

## Додавання тесту

Після додавання правила через `def-panini-rule`:

1. додайте unit-тест, якщо є нова фонологічна операція;
2. додайте повний integration trace для слова, яке цю операцію використовує.

Ці тести є machine prototype tests, а не самодостатнім доказом того, що
правило реалізує Паніні коректно. Для цього також потрібні citation provenance
та evidence-bound derivation trace.
