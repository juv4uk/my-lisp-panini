# Derivation IR trace events v0.1

Status: proposed event contract for `PANINI-IR-TRACE-EVENT-SPEC`. It refines
the evidence requirements in `trace-evidence-model-v0.1.md`; it neither
implements an evaluator nor asserts that this event vocabulary occurs in the
Aṣṭādhyāyī.

## English summary

The IR separates applicability, a selected decision, a state transition, and
conflict resolution. Each event is append-only, has a stable ID, points to
typed provenance, and can be validated without treating a final surface form as
proof. The Ukrainian section is normative.

## Українська

### [PANINI]

`applicability-check`, `rule-selected` і `state-transition` — назви нашого
майбутнього IR, а не saṃjñā або терміни тексту Паніні. Вони потрібні лише для
того, щоб не приписати джерелу приховане машинне рішення. Відношення між
sūtra, спадкованим контекстом, коментарем і перетворенням лишається окремим
provenance-твердженням.

### [INTERPRETATION]

Лінійний список applied rules недостатній: він не показує, чи правило було
перевірено на застосовність, чи існували альтернативи, і чому саме один
кандидат переміг. Vidyut також відокремлює applied step від optional choice,
але його production trace не гарантує всіх до-станів та причин конфлікту.
Тому цей контракт описує наші мінімальні пояснювальні дані, не копіюючи
внутрішню структуру Vidyut.

### [MY-LISP HYPOTHESIS]

#### Envelope

```yaml
trace_id: trace:<stable-id>
ir_version: panini-derivation-ir/0.1
trace_status: complete | partial | omitted | invalid
events:
  - event_id: evt:<monotonic-ordinal>
    kind: <event-kind>
    depends_on: [evt:<ordinal>]
    provenance: [prov:<stable-id>]
    verification: verified | needs-check | disputed | derived
    payload: {}
```

`event_id` є стабільним у межах одного `trace_id`, не перевикористовується
після виправлення й упорядковується за append-order. `depends_on` утворює DAG:
посилання в майбутнє або цикл роблять trace `invalid`. Append-order є порядком
спостереження, але **не** замінює обґрунтування rule priority.

#### Види подій

| `kind` | Призначення | Мінімальний `payload` |
|---|---|---|
| `state-observed` | зафіксувати canonical state без зміни | `state`, `serialization` |
| `applicability-check` | заявити перевірку кандидата на конкретному стані | `rule`, `state`, `outcome: applicable|inapplicable|unknown`, `conditions` |
| `rule-decision` | вибрати, відхилити або відкласти candidate | `rule`, `decision: selected|declined|deferred`, `policy`, `reason` |
| `conflict-resolved` | подати набір конкурентів і поточний результат | `candidates`, `winner|unresolved`, `policy`, `reason` |
| `state-transition` | застосувати вже обране правило | `rule`, `before`, `after`, `operation` |
| `trace-observation` | прив'язати зовнішній або частковий результат | `source`, `value`, `representation` |
| `trace-terminated` | явно завершити успіхом, помилкою або неповнотою | `outcome`, `reason` |

#### Інваріанти подій

```yaml
# 1. Rule application is never implicit.
applicability-check -> rule-decision(selected) -> state-transition

# 2. A conflict does not alter state.
conflict-resolved.before == conflict-resolved.after == referenced state

# 3. A transition changes state, except an explicit verified no-op.
state-transition.before != state-transition.after

# 4. Every rule field is either canonical sūtra ID or namespaced machine ID.
rule: "1.4.2" | "machine:2.4.75"
```

`state-transition` мусить залежати від `rule-decision(selected)`. Якщо
правило безальтернативне за поточним implementation profile, decision все
одно створюється з `policy: deterministic-profile`; це робить припущення
перевірним. Виняток — імпорт legacy trace: він позначається `partial` і не
може задовольнити acceptance test для priority.

`conflict-resolved` не може мати `winner`, якщо хоча б один candidate має
`applicability: unknown`, якщо policy не містить явного правила роботи з
невідомістю. `policy` є machine/interpretation полем, тому ніколи не отримує
`[PANINI]` статус лише через назву `vipratiSeDa`.

#### Канонічний стан і serialization

```yaml
state:
  id: state:sha256:<digest>
  form: <canonical-SLP1-serialized-terms>
  schema: panini-state/0.1
serialization: canonical-json | canonical-sexp
```

Усі Panini vocabulary IDs у `form` використовують SLP1; IAST і Devanāgarī
належать лише presentation artifact, на який посилається `trace-observation`.
Hash обчислюється з bytes canonical serialization, а не з display text.

#### Приклад: конфлікт перед переходом

```yaml
- event_id: evt:07
  kind: conflict-resolved
  depends_on: [evt:05, evt:06]
  provenance: [prov:sutra:1.4.2-text, prov:machine:dadati-apavada-choice]
  verification: needs-check
  payload:
    candidates:
      - { rule: "machine:2.4.72", applicability: applicable }
      - { rule: "machine:2.4.75", applicability: applicable }
    winner: "machine:2.4.75"
    policy: declared-apavada-relation
    reason: "Machine relation selects the more specific candidate; historical adequacy needs review."

- event_id: evt:08
  kind: state-transition
  depends_on: [evt:07]
  provenance: [prov:machine:dadati-apavada-choice]
  verification: derived
  payload:
    rule: "machine:2.4.75"
    before: "state:sha256:..."
    after: "state:sha256:..."
    operation: replace-suffix
```

#### Валідація v0.1

Валідатор мусить відхилити:

1. цикл у `depends_on` або посилання на неіснуючу подію;
2. `state-transition` без selected decision, до-/після-стану або provenance;
3. `conflict-resolved` без повного переліку відомих candidates;
4. sūtra ID у machine namespace або machine ID, виданий за canonical SLP1;
5. `complete` trace без `trace-terminated(outcome: success)`;
6. зовнішній oracle output, позначений як primary-text доказ.

Пов'язані документи: `trace-evidence-model-v0.1.md`,
`provenance-type-schema-v0.1.md`, `derivation-trace-template.md` і
`derivation-trace-counterexamples.md`.

## Deutsch

Der IR trennt Anwendbarkeitsprüfung, Regelentscheidung, Konfliktauflösung und
Zustandsübergang. Ereignisse sind append-only, provenance-gebunden und über
ein DAG von Abhängigkeiten prüfbar. Die ukrainische Fassung ist der normative
vollständige Vertrag; diese Ereignissprache ist keine Behauptung über Begriffe
der Aṣṭādhyāyī.
