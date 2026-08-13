# Machine-rule provenance schema

Статус: v0.1 (`PANINI-RULE-PROVENANCE-SCHEMA`).

## Проблема

`panini/machine/rules.my` визначає правила через `def-panini-rule` з
полями `:type 'vidhi` і `:scope 'antaraMga`/`'bAhiraMga` поряд із
рядковим sūtra-ID (напр. `"7.3.84"`). `panini/machine/meta.my` окремо
має ще недороблене поле `source` у `make-rule` (коментар: `azwADyAyI |
DAtupAWaH | vArttika | ...`, три крапки — таксономія неповна) — і жоден
реальний виклик `make-rule` в кодовій базі його не заповнює.

Наслідок: sūtra-ID (`"7.3.84"`) — це реальна, перевірювана цитата з
Aṣṭādhyāyī. Але `:scope 'antaraMga` на цьому ж правилі — це **наша
власна класифікація** за критерієм `paribhasha.md` (P3), не щось, що
sūtra 7.3.84 сам стверджує про себе. Без явного розрізнення обидва
типи тверджень виглядають однаково авторитетно в коді — саме той
ризик, проти якого `AGENTS.md` §21 попереджає на рівні документації,
але який досі не мав відповідника на рівні коду.

## Схема: 7 категорій походження

Розширює `Rule`-enum Vidyut (`Ashtadhyayi`/`Varttika`/`Dhatupatha`/
`Unadipatha`/`Linganushasana`/`Phit`/`Kashika`/`Kaumudi`/`Anyatra` —
див. [`research/vidyut-analysis.md`](../research/vidyut-analysis.md))
трьома категоріями, яких Vidyut не потребує (бо не документує власні
архітектурні рішення як окремий тип твердження), але які прямо потрібні
нашій методології (`AGENTS.md` §21):

| Категорія | Що це | Приклад |
|---|---|---|
| `sutra` | Пряма цитата з тексту Aṣṭādhyāyī, з номером | `"7.3.84"` |
| `dhatupatha` | Запис із Dhātupāṭha (окремий традиційний текст, не сама Aṣṭādhyāyī) | `"01.0001"` (BU) |
| `varttika` | Доповнення Кātyāyana до sūtra | *(поки не використано)* |
| `commentary` | Коментар (Kāśikā, Mahābhāṣya, Kaumudī тощо) | *(поки не використано)* |
| `traditional-principle` | Метапринцип, виведений з традиції коментаторства, не сама sūtra напряму — напр. `antaraNga > bAhiraNga`, `nitya > anitya` з `paribhasha.md` | `antaraMga`-класифікація P3 |
| `implementation-convenience` | Інженерне рішення заради реалізації — не Paninian факт і не традиційний принцип | вибір структури даних, формат a-list |
| `my-lisp-hypothesis` | Наша власна архітектурна гіпотеза, явно позначена як така | "kāraka = типізовані ребра графа" |

**Ключове правило:** правило з `sutra`-ID **не отримує автоматично**
статус `sutra` для *кожного* свого поля. `:type`/`:scope`/`:action` —
кожне з них має власне походження, яке потрібно перевіряти окремо, а
не наслідувати від номера sūtra в тому самому виразі.

## Застосування до наявних правил (анотації, не переробка)

### `rules.my`, правило `"7.3.84"`

```lisp
;; Rule 7.3.84 — sArvaDAtukarDADAtukayoH (Guṇa)
;; provenance:
;;   id     = sutra        (7.3.84, звірено — PANINI-SUTRA-CITATION-VERIFICATION,
;;                           хоча сам текст цитати в rules.my не перевірявся окремо)
;;   :type  = my-lisp-hypothesis (vidhi/niyama/atideSa/paribhAzA —
;;                           класифікація типів sūtra з ontology.md §6,
;;                           САМЕ це правило не позначене в первинному
;;                           тексті як "vidhi" явним словом — це наша
;;                           типологічна класифікація)
;;   :scope = traditional-principle (antaraMga — критерій з paribhasha.md
;;                           P3, який спирається на коментаторську
;;                           традицію (Unive.it/Kiparsky), не на сам
;;                           текст sūtra 7.3.84)
;;   :match/:action = implementation-convenience (форма запису умови й
;;                           дії — наше архітектурне рішення)
(def-panini-rule "7.3.84"
  :type 'vidhi
  :scope 'antaraMga
  :match '((term ?t1 (has-type 'dhAtu)) (term ?t2 (has-tag 'sArvaDAtukaM)))
  :action '(replace-last ?t1 (apply-guRa (last-char ?t1))))
```

### `rules.my`, правило `"6.1.78"`

```lisp
;; Rule 6.1.78 — eco 'yavāyāvaḥ (Sandhi)
;; provenance:
;;   id     = sutra (6.1.78, звірено — PANINI-EXAMPLES-DERIVATIONS-VERIFY,
;;                    текст sūtra точно збігається з першоджерелом)
;;   :type  = my-lisp-hypothesis (те саме застереження, що й вище)
;;   :scope = traditional-principle (bAhiraMga — той самий P3-критерій)
;;   eco-map, apply-eco-sandhi = implementation-convenience
(def-panini-rule "6.1.78" ...)
```

### `meta.my`, `make-rule` — уточнена таксономія `source`

Було: `source  — azwADyAyI | DAtupAWaH | vArttika | ...` (неповний
список, три крапки). Стало (без зміни коду в цій задачі — лише
документація очікуваних значень, реалізація полишена для окремої
задачі):

```lisp
;; source — одне з:
;;   'sutra                     — sutra-id (напр. "7.3.84")
;;   'dhatupatha                — dhatupatha-код (напр. "01.0001")
;;   'varttika                  — ще не використовується
;;   'commentary                — ще не використовується
;;   'traditional-principle     — напр. 'antaraMga-scope, паребгаза P1-P5
;;   'implementation-convenience — наше інженерне рішення
;;   'my-lisp-hypothesis        — наша архітектурна гіпотеза
```

## [MY-LISP HYPOTHESIS] щодо самої схеми

Ця 7-категорійна схема сама є нашою гіпотезою, не Paninian фактом —
вона узагальнює Vidyut'ів `Rule`-enum (перевірена, робоча модель) під
наші додаткові потреби прозорості. Питання, чи ці 7 категорій
достатні, чи потрібні ще (напр. окрема категорія для "неперевіреного
цитування з пам'яті", яку `PANINI-SUTRA-CITATION-VERIFICATION` уже де-факто
використовувала) — відкрите, не вирішується тут.

## Не зроблено в цій задачі

- Поле `source`/провенанс **не додано як реальний параметр**
  `def-panini-rule`/`make-rule` у коді `panini/machine/` — лише
  задокументовано очікувану таксономію й показано, як вона
  застосовувалась би до двох наявних правил через коментарі. Реальна
  зміна сигнатури макроса — окрема задача (потребує узгодження з
  `panini/machine/compiler.my`, який компілює `def-panini-rule`, не
  прочитаний у цій задачі).

## Джерела

- [`research/vidyut-analysis.md`](../research/vidyut-analysis.md) —
  `Rule`-enum Vidyut, основа для розширення.
- `panini/machine/rules.my`, `panini/machine/meta.my` — прочитано
  напряму для цієї задачі.
- [`foundation/rule-system.md`](../foundation/rule-system.md),
  [`foundation/paribhasha.md`](../foundation/paribhasha.md) — джерело
  категорії `traditional-principle`.
