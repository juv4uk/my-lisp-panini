# Architecture Recovery Review — my-lisp-panini

**Дата:** 2026-08-25 · **Автор:** Vyasa (COMPILER STEWARD)
**Тип:** read-only recovery review · **Задача:** ARCH-RECOVERY-REVIEW-PANINI
**Ресурси:** читання + ОДИН targeted прогон acceptance-suite (77 PASS, секунди)

---

## 1. Живе evidence цього огляду [VERIFIED сьогодні]

`my-lisp panini/tests/machine-acceptance.my` з кореня репо (cwd критичний —
внутрішні load-и відносні): **77 × [PASS], 0 fail**, включно з:
- bavati покрокова деривація (7 кроків, guna-precondition unknown recorded)
- yaml parser: BU class 1 / parasmaipadin seT витягнуті з реєстру

Це самохостинговий `panini/machine-model-v0.1` (11 модулів .my: compiler,
rules, runtime-prelude, meta, dhatu-registry-loader + negative-fixtures),
тест-сьюіт написаний прямо Lisp-ом незалежно від спільного ядра
(TESTING.md) — і він зелений на поточному contract-3.0 бінарнику my-lisp.

## 2. As-built шари

```
ЗНАННЯ      panini/{hypotheses,registry,research,sastra,specs}   (~40 док-файлів)
МАШИНА      panini/machine/ v0.1 (.my, macro-free fixture prelude)
ПРОТОТИПИ   prototype/derivation_ir (proof-carrying IR v0.1, Python)
LEGACY      scratch/ (python-скрипти добору даних — bootstrap/reference)
КООРДИНАЦІЯ tasks.my + repo.my + ecosystem/; validate_dependencies.py
```

## 3. Сильне

1. **Acceptance-suite зелений на чужому бінарнику** — найсильніший
   міжрепозиторний доказ сумісності, який я бачив у рої.
2. Negative-fixtures каталог існує (негативні тести — рідкість у рої).
3. Реєстровий ремонт зроблено свіжо (6311034 sakshi: registry repair +
   research batch; 4 задачі закрито з evidence).
4. documentation-languages.md фіксує мовну політику документів.

## 4. Фронти / борги

| # | Пріоритет | Що |
|---|---|---|
| 1 | MED | derivation_ir (proof-carrying) досі Python-прототип — за директивою міграції кандидат у .my, але потребує окремого дизайну proof-сертифікатів |
| 2 | MED | machine-foundation-reconciliation: звірка machine-model ↔ registry-примітивів після нещодавніх масових закриттів |
| 3 | LOW | TESTING.md вказує шлях tests/machine-acceptance.my, фактично panini/tests/ — оновити шлях |
| 4 | LOW | scratch/ python-скрипти — маркувати bootstrap/reference явно |

## 5. Висновок
Домен живіший, ніж виглядав із реєстру: самохостингова машина працює,
негативні тести є, регістр свіжий. Головний стратегічний пункт —
переведення derivation_ir у .my після ратифікації proof-моделі.

---
*Read-only. Єдиний прогін — targeted acceptance (77 PASS).*
