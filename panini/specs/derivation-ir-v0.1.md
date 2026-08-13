# Derivation IR v0.1

Status: foundation-level machine-model proposal for `PANINI-DERIVATION-IR-DESIGN`.
It is data design only: no evaluator, parser syntax, registry migration, or
claim that this structure is itself Pāṇini.

## English summary

Derivation IR v0.1 represents a reproducible derivation as immutable states,
typed terms, declared rule references, and an append-only evidence trace.
Paninian identifiers stay SLP1; implementation IDs stay explicitly namespaced.
The Ukrainian section is normative.

## Українська

### [PANINI]

Панінійська деривація не тотожна нашому serializable IR. Цей формат не має
перетворювати `dhAtu`, `pratyaya`, `it`, `saMjYA`, anuvṛtti чи kāraka на
готові VM primitives без окремого доказу. Його скромніша мета — не втратити
різницю між джерелом, інтерпретацією, rule reference і машинним переходом.

### [INTERPRETATION]

Наявні дослідження вже показали чотири практичні потреби: зберігати
source-oriented форму поряд із поточною формою, позначати designations окремо
від технічних metadata, не зливати alternatives із результатом та фіксувати
reason policy для конфлікту. Vidyut надихає деякі розрізнення, але його
мутабельні terms і optional history не є нашим форматом даних.

### [MY-LISP HYPOTHESIS]

#### Межа та власники

`derivation-ir-v0.1` є обмінним контрактом між майбутнім rule engine,
пояснювальним trace та зовнішніми fixtures. Він не є My Lisp AST і не дозволяє
вмикати semantic calls до проходження P5 gate. Реалізація під
`panini/machine/` належить machine maintainer; зміна surface My Lisp належить
власнику My Lisp; Panini Foundation визначає тут лише доказові інваріанти.

#### Кореневий запис

```yaml
ir_version: panini-derivation-ir/0.1
derivation_id: drv:<stable-id>
input:
  terms: [term:<stable-id>]
states: [state:<content-hash>]
rules: [rule:<stable-id>]
trace: trace:<stable-id>
result:
  state: state:<content-hash> | null
  status: success | partial | blocked | invalid
provenance: [prov:<stable-id>]
```

`input.terms`, `states`, `rules` і `trace` — посилання, а не дублікати. Це
запобігає тихому розходженню між output, rule registry та evidence trace.
`result.status: success` дозволений лише якщо trace завершено успішною
`trace-terminated` подією. `partial` не є failure, але не може служити
доказом повного priority/order test.

#### Term

```yaml
id: term:<stable-id>
kind: dhAtu | pratyaya | prAtipadika | opaque
source_form: <SLP1-string>
surface_form: <SLP1-string>
designations:
  - id: <SLP1-panini-vocabulary-id>
    provenance: [prov:<stable-id>]
metadata:
  namespace: machine | import | display
  values: {}
```

- `source_form` не змінюється для одного term identity; повна substitution
  створює новий term або явно обґрунтований relation у transition.
- `surface_form` — поточна SLP1 форма, а не IAST/Devanāgarī display string.
- `designations` моделюють **наше** посилання на задокументовану категоризацію;
  вони не стверджують, що кожен machine tag є saṃjñā.
- `metadata` не може мати SLP1-ID без namespace: це захищає від змішування
  `dhAtu` з `machine:dhatu`.
- `opaque` дозволяє import/fixture дані без вигаданого онтологічного класу.

#### State

```yaml
id: state:sha256:<digest>
schema: panini-state/0.1
terms: [term:<stable-id>]
relations:
  - kind: scope | attachment | semantic-role | implementation
    from: term:<stable-id>
    to: term:<stable-id>|entity:<stable-id>
    provenance: [prov:<stable-id>]
serialization: canonical-json | canonical-sexp
```

Стан immutable. Його hash обчислюють з canonical bytes полів `schema`, order
`terms` і нормалізованих `relations`, але не з display labels, timestamps або
локальних файлових шляхів. Relation `semantic-role` дозволений лише як
машинна гіпотеза з окремим provenance; він не оголошує kāraka готовим graph
edge Паніні.

#### Rule reference

```yaml
id: rule:<stable-id>
kind: sutra-reference | interpreted-rule | machine-rule
canonical_ref: "1.4.2" | null
machine_ref: "machine:<namespace>:<name>" | null
conditions: [condition:<stable-id>]
operation: operation:<stable-id> | null
provenance: [prov:<stable-id>]
```

Рівно одне з `canonical_ref` та `machine_ref` є обов'язковим. `sutra-reference`
не містить executable operation тільки тому, що має номер sūtra. Лише
`machine-rule` може мати executable `operation`, і він мусить залежати від
окремих interpretation/implementation provenance records.

#### Operation і transition

```yaml
id: operation:<stable-id>
kind: replace | insert | delete | attach-designation | split | fuse | opaque
target: term:<stable-id>|relation:<stable-id>
arguments: {}

transition:
  rule: rule:<stable-id>
  before: state:sha256:<digest>
  after: state:sha256:<digest>
  operation: operation:<stable-id>
  trace_event: evt:<ordinal>
```

Операція не містить «магічного» неявного контексту: усе, що визначає її
застосовність, має бути в `conditions`, state relations або попередніх
trace events. `opaque` застосовується для результату, який можна спостерігати,
але ще неможливо відповідально формалізувати; він примусово знижує result до
`partial`.

#### Мінімальні acceptance gates

1. Один serialized IR приклад містить хоча б `dhAtu`, `pratyaya`, два immutable
   states, machine-rule reference та transition trace.
2. Validator відхиляє IAST/Devanāgarī у `source_form`/`surface_form` і змішаний
   або непроіменований namespace metadata.
3. Validator відхиляє executable operation на `sutra-reference` без
   `interpreted-rule`/`machine-rule` bridge та provenance.
4. Один conflict fixture проходить через event contract: candidates, policy,
   decision, після чого окремий transition.
5. До `MYLISP-P5-PANINI-FOUNDATION-GATE-REVIEW` IR лишається data fixture;
   він не змінює parser/evaluator semantics.

Пов'язані документи: `derivation-ir-trace-events-v0.1.md`,
`trace-evidence-model-v0.1.md`, `provenance-type-schema-v0.1.md`,
`machine-mylisp-compatibility-boundary.md`.

## Deutsch

Derivation IR v0.1 beschreibt unveränderliche Zustände, typisierte Terms,
explizite Regelreferenzen und einen append-only Evidenztrace. SLP1 bleibt für
Pāṇini-Vokabular kanonisch; Machine-IDs sind namespaced. Das Format ist ein
Datendesign und weder ein My-Lisp-AST noch eine Behauptung über eine direkte
paninische VM-Struktur. Die ukrainische Fassung ist normativ.
