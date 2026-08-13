# Trace evidence model v0.1

Status: design contract for `PANINI-TRACE-EVIDENCE-MODEL`. It specifies what a
future derivation trace must expose for review. It authorizes neither a runtime
change nor a claim that this record shape is a category of the Aṣṭādhyāyī.

## English summary

The project needs more than an output form or an ordered list of rule labels.
An auditable trace must connect every state transition and conflict decision to
typed provenance, declare its completeness, and preserve rejected or omitted
information explicitly. The normative contract is in the Ukrainian section.

## Українська

### [PANINI]

Ця модель не стверджує, що Паніні подає деривацію як програмний журнал подій.
Вона лише захищає від помилкового перенесення машинних понять назад у джерело.
Текст sūtra, коментар, реконструкція застосовності та результат обчислення —
різні види тверджень. Їхній зв'язок має бути видимим, а не припущеним із
кінцевої форми.

### [INTERPRETATION]

`vidyut-term-lifecycle-delta.md` показує корисне розрізнення між застосованим
кроком і optional decision, але також фіксує межу: журнал Vidyut може бути
вимкнений і не мусить містити до-стан, повний набір кандидатів або причину
відхилення. `provenance-type-schema-v0.1.md` уже визначає, як посилатися на
доказ твердження; ця специфікація визначає, як такі записи збираються в
перевірний trace.

### [MY-LISP HYPOTHESIS]

#### Мінімальна форма

```yaml
trace_id: trace:<stable-id>
subject:
  kind: derivation | semantic-call
  id: <stable-id>
trace_status: complete | partial | omitted | invalid
steps:
  - id: step:<ordinal>
    event: transition | decision | conflict | observation
    before: state:<content-hash> | null
    after: state:<content-hash> | null
    rule: <canonical-sutra-id-or-machine-rule-id> | null
    provenance: [prov:<stable-id>]
    depends_on: [step:<ordinal>]
    explanation: <short falsifiable statement>
    verification: verified | needs-check | disputed | derived
```

`state` не є прихованим мутабельним об'єктом: hash і canonical serialization
повинні давати змогу незалежно відтворити або принаймні порівняти стан. Якщо
повна serialisation недоступна через розмір чи приватність, trace отримує
`partial`, а причина міститься в `explanation`.

#### Події та інваріанти

| Подія | Обов'язкові поля | Заборонене спрощення |
|---|---|---|
| `transition` | `before`, `after`, `rule`, хоча б один `provenance` | Вважати зміну форми доказом підстави правила |
| `decision` | рішення, policy/reason у `explanation`, provenance | Зливати відмову optional rule із незастосовністю |
| `conflict` | усі відомі candidates, winner або `unresolved`, policy/reason | Показувати лише переможця й називати порядок доведеним |
| `observation` | стан або результат, provenance, verification | Видавати зовнішній результат за внутрішній trace |

1. `complete` означає, що для кожного здійсненого переходу наявні до- і
   після-стан, rule reference та provenance. Це не означає, що історична
   інтерпретація безспірна.
2. `partial` зберігає корисні факти, але не може бути входом для тесту, який
   перевіряє повний порядок або конфліктне рішення.
3. `omitted` дозволений для batch-generation лише як явне значення; відсутній
   trace ніколи не трактується як успішний trace.
4. `invalid` ставиться, коли hash не збігається, посилання на provenance
   відсутнє або подія порушує власні інваріанти. Такий trace не можна
   використовувати як oracle.
5. `provenance` посилається на `ProvenanceRecord`, а не дублює або підміняє
   джерельний текст. Сутри й SLP1-ID лишаються канонічними в тих реєстрах, де
   їм належить бути.
6. Подія `conflict` не робить `vipratiSedha` універсальним алгоритмом. Вона
   лише зобов'язує реалізацію назвати фактичну policy та доказ її застосування.

#### Мінімальний приклад конфлікту

```yaml
id: step:07
event: conflict
before: state:8cc1
after: state:8cc1
rule: null
provenance:
  - prov:sutra:1.4.2-text
  - prov:machine:dadati-apavada-choice
depends_on: [step:06]
explanation: >
  Candidates machine:2.4.72 and machine:2.4.75 were considered; 2.4.75 was
  selected by the declared apavada relation. Historical adequacy remains
  needs-check.
verification: needs-check
```

Цей запис навмисно не переходить у новий стан: вибір між кандидатами є окремою
подією від застосування вибраного правила. Наступний `transition` мусить мати
`depends_on: [step:07]`.

#### Межа з Vidyut і тестами

Vidyut можна використовувати як зовнішній generator/oracle для зіставлення
результату, але його `Step` не можна автоматично перетворювати на `complete`
trace: відсутні обов'язкові поля цієї моделі. Відповідно, fixture має окремо
зберігати: джерело, версію інструмента, вхід, вихід, профіль trace та статус
перевірки. Тест кінцевої форми і тест пояснення конфлікту — різні тести.

### Критерії приймання наступної реалізації

1. Реалізація виводить `trace_status` для кожного derivation result.
2. Один приклад містить `transition`, `decision` і `conflict` як різні події.
3. Валідатор відхиляє `complete` trace без `before`, `after`, `rule` або
   provenance для transition.
4. Жоден тест не називає машинну policy панінійським фактом без окремого
   джерельного запису й status.

Пов'язані документи: `provenance-type-schema-v0.1.md`,
`vidyut-term-lifecycle-delta.md`, `dadati-conflict-review.md` і
`derivation-trace-template.md`.

## Deutsch

Das Modell verlangt für einen prüfbaren Trace nicht nur eine Endform, sondern
getrennte Übergangs-, Entscheidungs-, Konflikt- und Beobachtungsereignisse.
Jedes Ereignis verweist auf typisierte Provenienz und erklärt seinen
Vollständigkeitsstatus. Die ukrainische Fassung ist der vollständige normative
Vertrag; dieses Modell behauptet nicht, dass seine Datenstruktur eine
paninische Kategorie sei.
