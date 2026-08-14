# Контрприклади до лінійного derivation trace

## English

### Scope

This note records three bounded counterexample patterns. It does not generate a
Sanskrit form and does not claim that a universal scheduler follows from any
one sūtra. Its narrower point is that `state0 → state1 → …` alone is not
evidence of why a rule was applicable.

### Evidence requirements

First, inherited scope (`anuvftti` / `aDikAra`) needs source, item and
explicit-or-inferred status, plus a separately statused scope: a step such as
`apply 1.4.59` otherwise hides `prAdayaH` from 1.4.58. Second, optionality
needs both selected and non-selected branches with status and justification;
absence of a field does not prove absence of an alternative. Third, sequence
does not establish `vipratiSeDa`: each candidate's applicability, conflicting
effect and actual mechanism (`vipratiSeDa`, `utsarga-apavAda`, other, or
`unresolved`) must be recorded. The mention of 1.4.2 is not a claim of a
universal runtime scheduler.

### Machine boundary

Post-v0.1 traces need `branches` and `competing_rules`, or an honest
`not-applicable` / unsearched-alternatives explanation. A tree, DAG, or
snapshot representation is `[MY-LISP HYPOTHESIS]`, not a statement about
Pāṇini.

## Українська

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

## Deutsch

### Geltungsbereich

Diese Notiz hält drei begrenzte Gegenbeispielmuster fest. Sie erzeugt keine
Sanskritform und behauptet nicht, dass aus einem einzelnen Sūtra ein
universeller Scheduler folgt. Ihr engerer Punkt lautet: `state0 → state1 → …`
allein belegt nicht, warum eine Regel anwendbar war.

### Evidenzanforderungen

Erstens benötigt geerbter Scope (`anuvftti` / `aDikAra`) Quelle, Element und
den Status `explicit-or-inferred`, außerdem einen separat statusierten Scope:
Ein Schritt wie `apply 1.4.59` verbirgt sonst `prAdayaH` aus 1.4.58. Zweitens
benötigt Optionalität gewählte und nicht gewählte Zweige mit Status und
Begründung; ein fehlendes Feld beweist nicht das Fehlen einer Alternative.
Drittens begründet Reihenfolge kein `vipratiSeDa`: Anwendbarkeit jedes
Kandidaten, kollidierende Wirkung und der tatsächlich verwendete Mechanismus
(`vipratiSeDa`, `utsarga-apavAda`, anderer oder `unresolved`) müssen
festgehalten werden. Der Bezug auf 1.4.2 ist kein Anspruch eines universellen
Runtime-Schedulers.

### Maschinengrenze

Traces nach v0.1 benötigen `branches` und `competing_rules` oder eine ehrliche
Erklärung `not-applicable` beziehungsweise ungeprüfter Alternativen. Baum,
DAG oder Snapshots sind `[MY-LISP HYPOTHESIS]`, keine Aussage über Pāṇini.

## Висновок

Лінійний trace залишається допустимим presentation layer для одного
обраного шляху, але доказовий record мусить уміти пояснити його scope,
відкинуті/доступні варіанти та конкуренцію. Інакше «порядок кроків» маскує
проектне рішення під властивість граматики.
