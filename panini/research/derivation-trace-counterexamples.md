# Контрприклади до лінійного derivation trace

## Теза

Список кроків `state₀ → state₁ → …` корисний, але сам по собі не зберігає
усі умови застосування правил. Нижче — три bounded counterexample patterns;
це не повні derivation-приклади і не претендує на генерацію форми.

## 1. Спадкований scope: `anuvftti` / `aDikAra`

**Помилковий trace:**

```text
step 4: apply 1.4.59 → assign upasarga
```

Такий запис не показує, що 1.4.59 читається з `prAdayaH` від 1.4.58 і в
контексті відповідного розділу. Якщо trace зберігає тільки номер кроку та
пару before/after, читач не може відрізнити explicit текст від inherited
умови.

**Необхідні поля:**

```yaml
inherited_context:
  - source: "1.4.58"
    item: prAdayaH
    status: explicit-or-inferred
scope:
  source: "1.4.56"
  status: source-checked|unresolved
```

Джерело межі: [upasarga crosswalk](upasarga-foundation-crosswalk.md) та
[anuvftti foundation note](../foundation/anuvrtti.md).

## 2. Факультативність: не один наступний стан

**Помилковий trace:**

```text
step 8: rule X produces state₈
```

Якщо правило допускає варіант, лінійний trace непомітно перетворює вибір
дослідника на єдиний результат. Навіть якщо один варіант достатній для
навчального прикладу, відкинута гілка є частиною доказового стану.

**Необхідні поля:**

```yaml
alternatives:
  - branch_id: apply-rule
    status: selected
    justification: "..."
  - branch_id: do-not-apply
    status: available|rejected
    justification: "..."
```

`alternatives` у нинішньому trace template вже є, але цей контрприклад
пояснює, чому поле не можна вважати необов'язковою приміткою.

## 3. Конфлікт: порядок кроків не є поясненням пріоритету

**Помилковий trace:**

```text
step 12: apply later rule Y
```

Сам факт, що Y записано після X, не доводить, що спрацював `vipratiSeDa`.
Спершу треба показати, що обидва правила застосовні до того самого
матеріалу, що наслідки конфліктують і що інші механізми (зокрема
special/general analysis) не вирішили випадок раніше.

**Необхідні поля:**

```yaml
competing_rules:
  - reference: "X"
    applicability: asserted|checked|unresolved
  - reference: "Y"
    applicability: asserted|checked|unresolved
resolution:
  mechanism: vipratiSeDa|utsarga-apavAda|other|unresolved
  source: "1.4.2"
  status: interpretation|source-checked|unresolved
```

Джерело межі: [rule-system.md](../foundation/rule-system.md). Документ
навмисно не стверджує, що 1.4.2 — універсальний runtime scheduler.

## Мінімальне уточнення template

Для source-checked trace після v0.1 потрібні два додаткові структурні поля:

```yaml
branches: []          # для факультативних застосувань
competing_rules: []   # для фактичної конкуренції, не для кожного кроку
```

Якщо вони не застосовні, trace мусить писати `not-applicable` або пояснювати,
чому пошук альтернатив не виконувався. Відсутність поля не означає, що
альтернатив не існувало.

## [MY-LISP HYPOTHESIS]

Майбутня machine model може подати branches як tree, DAG або набір snapshots.
Це проектна оптимізація. Панініївський фундамент вимагає лише зберегти
джерело, scope, alternatives і спосіб розв'язання там, де вони стверджуються.

## Висновок

Лінійний trace залишається допустимим presentation layer для одного
обраного шляху, але доказовий record мусить уміти пояснити його scope,
відкинуті/доступні варіанти та конкуренцію. Інакше «порядок кроків» маскує
проектне рішення під властивість граматики.
