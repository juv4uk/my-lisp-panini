# E-graph counterexample: ordered derivation is not equality saturation

Status: bounded architecture analysis for
`PANINI-EGRAPH-ORDERED-DERIVATION-COUNTEREXAMPLE`. It evaluates `egg` as an
external research tool, not as evidence about Pāṇini and not as a dependency
decision.

## English summary

`egg` is optimized for equality saturation: it retains many equivalent
expressions and extracts one according to a cost function. A derivation trace,
by contrast, must preserve selected rule order, scope, optional decisions, and
state-changing operations. Therefore an e-graph cannot be the authoritative
derivation engine; it may later be used only for explicitly declared,
equivalence-safe analyses. The Ukrainian section is normative.

## Українська

### [PANINI]

Цей контрприклад не стверджує, що правила Паніні є або не є рівностями. Він
лише забороняє нашій майбутній реалізації непомітно замінити обґрунтовану
послідовність derivation механізмом, який зберігає класи еквівалентних виразів.
Питання, чи певне перетворення є оборотним, факультативним, контекстно
обмеженим або пріоритетним, потребує окремих джерельних та інтерпретаційних
записів.

### [INTERPRETATION]

Офіційна документація `egg` описує e-graph як структуру для відстеження
рівностей між виразами та library для equality saturation; `Runner` застосовує
rewrites, після чого `Extractor` вибирає один вираз за cost function. Це
продуктивна модель для оптимізації й synthesis, але вибраний «найкращий» вираз
не є поясненням історичного чи rule-governed derivation path.

### [MY-LISP HYPOTHESIS]

#### Контрприклад A: втрата напрямку

Нехай модель має state `S0` і два rule steps:

```text
R1: (root dA, suffix Sap)  ──[class-3 context]──>  (root dA, marker Slu)
R2: (root dA, marker Slu) ──[declared condition]─>  (abhyasa da dA)
```

У trace `R2` залежить від transition `R1`: `Slu` є не просто альтернативним
написанням `Sap`, а результатом machine operation з provenance і scope.

Якщо подати `R1` як e-graph equality,

```text
(root dA Sap)  =  (root dA Slu)
```

то e-class зберігає обидві форми без causal distinction. Pattern для `R2`
може бачити `Slu` як доступного представника незалежно від того, чи був R1
обраний, чи його передумови зафіксовано, чи гілку відхилено. Extractor потім
вибере дешевший expression, але не зможе довести selected decision і transition
у порядку, потрібному `derivation-ir-trace-events-v0.1.md`.

**Висновок:** direction можна зберігати як annotation, але тоді саме event DAG,
а не e-class, є авторитетним описом derivation.

#### Контрприклад B: конфлікт — не cost function

Для `dadAti` machine fixture фіксує два candidates:

```text
machine:2.4.72   general path
machine:2.4.75   declared exception path
```

Equality saturation може зберегти обидва результати та дозволити cost function
обрати коротший/менший AST. Проте така ціна не відповідає на питання:

1. чи обидва правила були застосовні до одного state;
2. яке declared relation між ними;
3. хто саме і за якою policy обрав winner;
4. чи це історична інтерпретація, machine heuristic або експеримент.

Навіть якщо extractor випадково вибере той самий результат, це збіг output, не
доказ `apavAda-over-utsarga`. `conflict-resolved` має існувати окремо від
optimization/extraction.

#### Контрприклад C: scope та факультативність

Нехай `R3` застосовний лише в scope `C` або є optional. E-graph може додати
еквівалентність після condition check, але його клас не зберігає як canonical
факт: «ця форма доступна **лише після** decision `selected` під scope `C`».
Якщо такий condition зберігати всередині enode, він перестає бути загальною
еквівалентністю; якщо не зберігати — буде витік scope/branch у чужий контекст.

#### Допустима вузька роль e-graph

| Роль | Допустимо? | Умова |
|---|---:|---|
| authoritative derivation executor | Ні | губляться direction, scope, policy, trace status |
| conflict resolver | Ні | extractor cost не є доказом пріоритету |
| presentation of explicitly proven equivalences | Так, пізніше | equivalence relation і provenance задані окремо |
| optimizer для My Lisp після semantic gate | Можливо | не змінює derivation trace і має власні tests |
| offline counterexample exploration | Так | результати мають статус hypothesis/experiment |

#### Acceptance test для майбутнього експерименту

Будь-який прототип e-graph має пройти negative test:

```text
Given: R1 has not emitted rule-decision(selected).
Expect: no trace can claim R2 state-transition solely because the e-class
        contains R1's output shape.
```

Другий negative test: якщо два кандидати в e-class мають різну declared policy,
extractor не може видати `conflict-resolved(winner=...)` без зовнішньої
provenance-bearing policy event.

### Рішення

`egg` лишається **research-only**. Якщо його додадуть, він працює над копією
вже сформованого IR як non-authoritative analysis. Canonical derivation record
залишається immutable states + event DAG + provenance; e-graph output має
`trace-observation`/`hypothesis` status, а не `state-transition` authority.

Джерела: [egg API documentation](https://docs.rs/egg/latest/egg/) та
[egg project overview](https://egraphs-good.github.io/); пов'язані локальні
контракти: `derivation-ir-v0.1.md`, `derivation-ir-trace-events-v0.1.md`,
`trace-evidence-model-v0.1.md`.

## Deutsch

E-Graphs speichern Klassen äquivalenter Ausdrücke und wählen Ergebnisse per
Kostenfunktion. Ein Derivation-Trace muss hingegen Richtung, Scope,
Optionalität, Konfliktpolicy und Provenienz bewahren. Daher bleibt `egg`
research-only: höchstens für explizit belegte Äquivalenzanalysen über einer
Kopie des fertigen IR, nie als autoritativer Derivation-Executor oder
Konfliktlöser. Die ukrainische Fassung ist normativ.
