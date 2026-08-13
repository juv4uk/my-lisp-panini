# Surface operation boundary for `dadAti`: source audit

Status: `partial`. The form `dadAti` is independently attested as a Sanskrit
form of the root `dA`, and the preceding local `dvirvacana`, `abhyAsa`, and
`hrasva` bridges have dedicated source audits. This record asks the narrower
question whether those facts authorize one final, source-backed IR operation
from `da + dA + ti` to `dadAti`.

## English

They do not, yet. The surveyed sources attest the form and explain individual
local rules, but this audit has not assembled a complete source account of the
remaining conditions, term order, and surface realization. Therefore the
Derivation IR fixture must retain `dadAti` only as an observation after its
last verified state, with no `state-transition` claiming final assembly.

## Українська

### [PANINI]

Наявні джерела незалежно засвідчують форму `dadAti` для кореня `dA`, а
попередні аудити встановлюють вузькі мости `Slu → dvirvacana` (6.1.10),
designation `abhyAsa` (6.1.4) та hrasva (7.4.59). Проте це **не** є повним
джерельним обліком усіх умов, порядку term-ів і реалізації surface form.
Жодна з цих часткових перевірок сама не формулює один останній перехід
`da + dA + ti → dadAti`.

Джерела: [форма `dadāti` у словниковому записі](https://en.wiktionary.org/wiki/dad%C4%81ti),
[огляд подвоєння для `dā → dadāti`](https://learnsanskrit.org/verbs/doubling/),
[6.1.4](https://sanskritdictionary.com/panini/6-1-4) і
[7.4.59](https://sanskritdictionary.com/panini/7-4-59). Словникове або
навчальне засвідчення форми тут не використовується як доказ повної
панініївської деривації.

### [INTERPRETATION]

У Derivation IR дозволено `trace-observation` зі значенням `dadAti` після
останнього verified state. Заборонено позначати це як `state-transition`,
додавати вигаданий універсальний `assemble-surface` або підвищувати fixture
до `complete`. Навчальний приклад оновлено саме так: його фінальний рядок
явно є спостереженою form, а не доведеним кроком.

### [MY-LISP HYPOTHESIS]

Майбутня символьна система мусить розрізняти `observed result` і `derived
result`. Це корисна загальна вимога до evidence model, але не переносить
жодної санскритської surface-операції у My Lisp і не виправдовує її як
primitive.

## Незакриті межі

1. Повний rule path після локального hrasva-кроку.
2. Порядок, scope і взаємодії наступних правил.
3. Machine contract для surface realization.
4. End-to-end evidence trace із усіма альтернативами та non-applications.

## Deutsch

Die Form `dadAti` ist belegt, und die lokalen Schritte `dvirvacana`,
`abhyAsa` und hrasva wurden separat abgegrenzt. Daraus folgt jedoch kein
einziger, vollständig belegter IR-Übergang `da + dA + ti → dadAti`. Das
Fixture darf die Form daher nur beobachten, nicht als vollständige Ableitung
oder als universelle Oberflächenoperation behaupten.
