# panini-nlp — code-level audit

Статус: v0.1 (`PANINI-NLP-AUDIT`). Статус джерела: **EXPERIMENTAL
REFERENCE, не authoritative** (`AGENTS.md` §16) — це прямо
підтверджено знахідками нижче, не лише декларується.

Джерело: `panini_nlp-0.2.0.tar.gz` (PyPI, вже завантажений у корені
цього репозиторію), розпаковано й прочитано напряму: `__init__.py`,
`rules/adhyaya_1.py` (2810 рядків), `rules/__init__.py`, `sandhi.py`,
`semantics.py` — код, не опис із PyPI.

## What panini-nlp models

Заявлено (за описом PyPI, цитованим в `AGENTS.md` §16): "модель
Aṣṭādhyāyī як обчислюваного directed graph, registry sūtra/dhātu,
deterministic/neuro-symbolic processing". Реально код складається з
двох дуже різних за якістю шарів:

1. **`rules/adhyaya_1.py`–`adhyaya_8.py`** (сумарно **34 010 рядків**)
   — по одній функції на кожну з ~3959 sūtra, кожна автогенерована
   скриптом `scripts/scaffold_rules.py`, з коментарем `# Auto-generated`.
2. **Hand-written топ-рівневі модулі** (`sandhi.py`, `morphology.py`,
   `semantics.py`, `samasa.py`, `chandas.py`, `meaning.py`,
   `validator.py`) — це те, що реально імпортується як публічний API
   в `__init__.py`.

## How it models it — і головна знахідка цього аудиту

**Шар 1 (`rules/adhyaya_*.py`) — це майже повністю порожні заглушки.**
Приклад, дослівно з коду:

```python
@registry.register("1.1.1", text="वृद्धिरादैच् ।")
def rule_1_1_1(ctx=None):
    """
    1.1.1: वृद्धिरादैच् ।
    """
    pass
```

Це повторюється (з тим самим патерном — Devanāgarī-текст sūtra,
докрстрінг, і `pass` замість реалізації) для практично всіх 3959
sūtra. Сам `RuleRegistry` (`rules/__init__.py`) — це **плаский
словник** `id → Sutra(id, text, description)` + окремий словник
`id → Callable` (де майже кожен `Callable` — порожня функція). **Це
не directed graph**: немає полів для залежностей, посилань на інші
правила, порядку застосування чи механізму конфлікт-резолюції в самій
структурі даних. Твердження PyPI-опису про "computable directed
graph" не підтверджується кодом реєстру.

**Шар 2 (`sandhi.py`, `semantics.py` та ін.) — реально працюючий, але
дуже вузький.** `SandhiEngine.apply()` містить справжню, робочу
умовну логіку для **4 конкретних sandhi-sūtra** (6.1.77, 6.1.87,
6.1.88, 6.1.101 — перевірено, номери й Sanskrit-текст ("iko yaṇaci",
"ādguṇaḥ", "vṛddhireci", "akaḥ savarṇe dīrghaḥ") виглядають коректно
й впізнавано) з реальним порівнянням фонем і застосуванням заміни —
не заглушка. Але це **4 правила з 3959**, не "повна модель Aṣṭādhyāyī".

## What corresponds directly to Pāṇini

- `semantics.py` (`SemanticParser`) реалізує **точно ту саму модель**,
  що обговорюється (і критикується як спрощення) в
  [`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md):
  "Each verb becomes an Action node... Each noun becomes an Entity
  node... Edges represent Kāraka relations." Це незалежне
  підтвердження, що ACTION→role→entity — поширена, природна перша
  гіпотеза для комп'ютерної реалізації kāraka — і водночас додаткове
  свідчення, що вона популярна *попри* те, що наш власний аналіз уже
  показав її спрощеність.
- Модуль явно цитує **Briggs (1985), "Knowledge Representation in
  Sanskrit and Artificial Intelligence"** як натхнення — реальна,
  перевірювана академічна праця (класична стаття в AI Magazine про
  застосовність панініївської семантики до представлення знань),
  вартий уваги для майбутнього дослідження, не досліджений в цій
  задачі детальніше.
- Малий набір реально реалізованих sandhi-правил відповідає тому
  самому фонологічному шару Aṣṭādhyāyī, що й у `PANINI-HERITAGE-AUDIT`
  і `PANINI-VIDYUT-AUDIT`.

## What is implementation machinery

- `compression.py` (`.meru`-формат, msgpack+zlib) — суто інженерне
  рішення для стиснення словникових даних, не Paninian факт.
- `RuleRegistry`-декоратор (`registry.register(id, text=...)`) —
  Python-специфічний патерн реєстрації, не концепція граматики.
- `gnn/` (Graph Neural Network модулі, `models.py`, `inference.py`,
  `features.py`) — це і є "neuro-symbolic" частина заявленого опису;
  **вміст не прочитано в цій задачі** (позначено як TODO нижче) —
  вимагає окремої перевірки, чи це реально навчена модель, чи також
  каркас.

## What we could reuse (як ідею, обережно)

- Патерн "невеликий, реально работаючий набір правил з чіткими
  sūtra-посиланнями, а не намагання одразу покрити все 3959" —
  іронічно, саме те, що `AGENTS.md` §6 радить для `dhAtu`-реєстру
  ("20 добре досліджених, а не 2000 поверхових") — `sandhi.py`
  фактично дотримується цього принципу для sandhi, `rules/adhyaya_*`
  — ні. Хороший антиприклад того, чого варто уникати (покриття
  вшир без глибини).

## What we should NOT reuse

- **Автогенерація тисяч порожніх функцій-заглушок як "реєстру
  правил".** Це створює оманливе враження повноти (3959 зареєстрованих
  ID) без жодної реальної семантики за 99%+ з них — саме той тип
  псевдо-авторитетності, проти якого застерігає `AGENTS.md` §16
  ("EXPERIMENTAL REFERENCE, не authoritative"). Якщо
  `panini-machine-model-v0.1` колись матиме "реєстр усіх sūtra", він
  повинен чітко розрізняти "зареєстровано ID+текст" від "реалізовано
  логіку" — не змішувати ці два стани в одному полі, як тут.
- Плаский словник без представлення залежностей — якщо колись
  знадобиться граф залежностей sūtra (для `PANINI-RULE-CONFLICTS-VIPRATISEDHA`-
  подібної логіки), ця структура даних непридатна як приклад.

## Відкрите питання

- `gnn/` модулі — не прочитані в цій задачі. Якщо колись знадобиться
  оцінити "neuro-symbolic" частину заяви PyPI-опису, це вимагає
  окремого прочитання `gnn/models.py`/`gnn/inference.py`.

## Джерела

- `panini_nlp-0.2.0.tar.gz` (PyPI), розпаковано й прочитано напряму
  2026-08-13: `panini_nlp/__init__.py`, `panini_nlp/rules/__init__.py`,
  `panini_nlp/rules/adhyaya_1.py`, `panini_nlp/sandhi.py`,
  `panini_nlp/semantics.py`.
