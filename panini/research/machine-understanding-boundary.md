# Межа машинного розуміння · Machine understanding boundary · Grenze maschinellen Verstehens

Статус: дослідницький запис для `PHILOSOPHY-MACHINE-UNDERSTANDING`.

## English

### Question and answer

The project must not use “the machine understands Pāṇini” as a success claim.
It mixes three different assertions that require different evidence:

| Assertion | Machine-testable? | Permitted conclusion |
| --- | --- | --- |
| **Operational competence**: a program applies its declared transition to a typed state. | yes | the implementation conforms to its declared contract for this fixture |
| **Evidential explanation**: it returns inspectable state, rule, decision and provenance references. | yes | this particular transition is reproducible and explainable at its recorded layer |
| **Historical/semantic understanding**: it knows what Pāṇini meant or has recovered the traditional system. | no, not from a program trace alone | requires independent philological and interpretive review |

### [PANINI]

“Machine understanding” is not attributed to the Aṣṭādhyāyī. The relevant
source-facing observation is narrower: a rule can be stated with a condition,
and later applications depend on whether a particular occurrence satisfies
that condition. A source citation supports a source claim only; it does not
establish what a modern machine understands.

### [INTERPRETATION]

For this project, call a machine result **operationally adequate** only when it
has all of the following:

1. a stable subject (term, state, relation, or rule occurrence ID);
2. declared input conditions and a typed result or an explicit blocked result;
3. a reproducible operation/transition record;
4. provenance whose layer matches the assertion; and
5. an inspectable falsifier or negative fixture.

This develops, but does not replace, the existing grounding and explanation
contracts. Surface agreement is only a `trace-observation`; it cannot prove
unrecorded intermediate steps. `unknown`, `needs-check`, and `unresolved` are
therefore competent outcomes, not errors to conceal.

### [MY-LISP HYPOTHESIS]

If a later My Lisp interface needs a status, it should report a bounded
capability rather than an authority claim:

```yaml
subject: state:sha256:<digest>
capability: execute-transition | exhibit-evidence | classify-claim
result: pass | fail | blocked | unresolved
support: [state, transition, decision, provenance, test]
outside_boundary:
  - historical-intent
  - complete-traditional-derivation
  - semantic-understanding
```

This is a proposal for machine records, not a My Lisp primitive. It deliberately
does not define an `understands?` predicate: such a name would overstate what
the evidence establishes.

### Acceptance implications

- An executable fixture may claim contract conformance, never historical
  authority.
- A natural-language explanation must resolve to inspectable references;
  prose is not its own evidence.
- A missing source bridge, applicability proof, or conflict relation produces
  `blocked` or `unresolved`, not a default scheduler choice.
- Any future broader understanding claim must name a new exhibit type and an
  independent review procedure before admission.

### Links

- [`semantic-grounding.md`](semantic-grounding.md)
- [`../specs/philosophy-control-layer-v0.1.md`](../specs/philosophy-control-layer-v0.1.md)
- [`../specs/derivation-machine-explanation-boundary-v0.1.md`](../specs/derivation-machine-explanation-boundary-v0.1.md)
- [`derivation-trace-counterexamples.md`](derivation-trace-counterexamples.md)

## Українська

### Питання й відповідь

Проєкт не повинен оголошувати успіхом фразу «машина розуміє Паніні». Вона
змішує три твердження з різними вимогами до доказу:

| Твердження | Чи перевіряє машина? | Дозволений висновок |
| --- | --- | --- |
| **Операційна компетентність**: програма застосовує оголошений перехід до типізованого стану. | так | реалізація відповідає оголошеному контракту для цього fixture |
| **Доказове пояснення**: вона повертає доступні для огляду посилання на стан, правило, рішення й provenance. | так | цей конкретний перехід відтворюваний і пояснюваний на зафіксованому рівні |
| **Історичне/семантичне розуміння**: вона знає намір Паніні або відновила традиційну систему. | ні, не лише за program trace | потрібна незалежна філологічна й інтерпретаційна перевірка |

### [PANINI]

«Машинне розуміння» не приписується Aṣṭādhyāyī. Релевантне джерельне
спостереження вужче: правило може мати умову, а пізніше застосування залежить
від того, чи задовольняє конкретне входження цю умову. Посилання на sūtra
підтримує лише джерельне твердження; воно не доводить, що розуміє сучасна
машина.

### [INTERPRETATION]

У цьому проєкті машинний результат називаємо **операційно достатнім** лише за
наявності всього такого:

1. стабільного суб'єкта: ID терма, стану, відношення або входження правила;
2. оголошених умов входу й типізованого результату або явного blocked result;
3. відтворюваного запису операції/переходу;
4. provenance, рівень якого відповідає твердженню; та
5. доступного для огляду фальсифікатора або негативного fixture.

Це розвиває, але не замінює чинні контракти заземлення й пояснення. Збіг
поверхневої форми є лише `trace-observation`; він не доводить незаписані
проміжні кроки. Тому `unknown`, `needs-check` і `unresolved` — компетентні
результати, а не помилки, які слід приховати.

### [MY-LISP HYPOTHESIS]

Якщо майбутньому інтерфейсу My Lisp знадобиться статус, він має повідомляти
обмежену здатність, а не авторитетне твердження:

```yaml
subject: state:sha256:<digest>
capability: execute-transition | exhibit-evidence | classify-claim
result: pass | fail | blocked | unresolved
support: [state, transition, decision, provenance, test]
outside_boundary:
  - historical-intent
  - complete-traditional-derivation
  - semantic-understanding
```

Це пропозиція для machine records, а не primitive My Lisp. Вона навмисно не
визначає предикат `understands?`: така назва перебільшувала б те, що встановлює
доказ.

### Наслідки для приймання

- Виконуваний fixture може стверджувати відповідність контракту, але не
  історичний авторитет.
- Природномовне пояснення мусить розкриватися в посилання, які можна оглянути;
  проза сама не є доказом.
- Відсутній джерельний міст, доказ застосовності чи relation конфлікту дає
  `blocked` або `unresolved`, а не вибір scheduler за замовчуванням.
- Будь-яке ширше твердження про розуміння мусить до допуску назвати новий тип
  exhibit і незалежну процедуру перевірки.

### Посилання

- [`semantic-grounding.md`](semantic-grounding.md)
- [`../specs/philosophy-control-layer-v0.1.md`](../specs/philosophy-control-layer-v0.1.md)
- [`../specs/derivation-machine-explanation-boundary-v0.1.md`](../specs/derivation-machine-explanation-boundary-v0.1.md)
- [`derivation-trace-counterexamples.md`](derivation-trace-counterexamples.md)

## Deutsch

### Frage und Antwort

Das Projekt darf „die Maschine versteht Pāṇini“ nicht als Erfolg behaupten.
Die Formulierung vermischt drei Aussagen mit verschiedenen Evidenzanforderungen:

| Aussage | Maschinell prüfbar? | Zulässige Folgerung |
| --- | --- | --- |
| **Operationale Kompetenz**: Ein Programm wendet seinen deklarierten Übergang auf einen typisierten Zustand an. | ja | Die Implementierung erfüllt für dieses Fixture ihren deklarierten Vertrag |
| **Evidenzielle Erklärung**: Sie liefert prüfbare Verweise auf Zustand, Regel, Entscheidung und Provenance. | ja | Dieser Übergang ist auf seiner protokollierten Ebene reproduzierbar und erklärbar |
| **Historisch-semantisches Verstehen**: Sie kennt Pāṇinis Absicht oder hat das traditionelle System rekonstruiert. | nicht aus einem Program-Trace allein | unabhängige philologische und interpretative Prüfung nötig |

### [PANINI]

„Maschinelles Verstehen“ wird der Aṣṭādhyāyī nicht zugeschrieben. Die relevante
quellennahe Beobachtung ist enger: Eine Regel kann eine Bedingung enthalten,
und spätere Anwendung hängt davon ab, ob ein bestimmtes Vorkommen diese erfüllt.
Ein Sūtra-Zitat stützt nur eine Quellenbehauptung, nicht das Verstehen einer
modernen Maschine.

### [INTERPRETATION]

Ein Ergebnis ist hier nur dann **operational hinreichend**, wenn es einen
stabilen Gegenstand, deklarierte Eingabebedingungen und typisiertes oder
blockiertes Resultat, einen reproduzierbaren Operationsrecord, ebenengerechte
Provenance sowie einen prüfbaren Falsifikator oder ein Negativfixture besitzt.
Oberflächenübereinstimmung ist lediglich `trace-observation`. Daher sind
`unknown`, `needs-check` und `unresolved` kompetente, nicht zu verbergende
Ergebnisse.

### [MY-LISP HYPOTHESIS]

Ein künftiger My-Lisp-Status sollte begrenzte Fähigkeiten wie
`execute-transition`, `exhibit-evidence` oder `classify-claim` mit
`pass`, `fail`, `blocked` oder `unresolved` berichten. Historische Absicht,
vollständige traditionelle Derivation und semantisches Verstehen bleiben
ausdrücklich außerhalb der Grenze. Das ist ein Vorschlag für Machine Records,
kein My-Lisp-Primitive; einen Prädikatnamen `understands?` definiert er bewusst
nicht.

### Folgen für die Abnahme

Ein ausführbares Fixture kann nur Vertragskonformität, nicht historische
Autorität behaupten. Prosa muss auf prüfbare Referenzen zurückführbar sein.
Fehlende Quellenbrücke, Anwendbarkeit oder Konfliktrelation führt zu `blocked`
oder `unresolved`, nicht zu einer Scheduler-Standardwahl. Eine weitergehende
Verstehensbehauptung braucht vor Zulassung einen neuen Exhibit-Typ und ein
unabhängiges Prüfverfahren.
