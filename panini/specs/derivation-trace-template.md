# Шаблон доказового trace деривації

Статус: v0.1, дослідницький формат (`PANINI-DERIVATION-TRACE-EVIDENCE-TEMPLATE`).

## Призначення

Цей шаблон призначено для **ручного, перевірюваного** trace. Він не є форматом
VM, не доводить повноти деривації та не дозволяє перетворити послідовність
кроків на executable grammar без окремого машинного milestone.

Кожен крок мусить відрізняти:

1. факт про текст або традиційне джерело;
2. інтерпретацію, яка пов'язує факт зі станом;
3. технічний опис стану, обраний нами для trace.

## Обов'язковий каркас

```yaml
trace_id: example-id
status: draft                 # draft | source-checked | disputed | blocked
goal:
  display_iast: "…"
  canonical_slp1: "…"

initial_terms:
  - term_id: root
    form_slp1: "…"
    asserted_categories:
      - designation: dhAtu
        source:
          kind: dhatupatha
          reference: "…"
          evidence_status: source-checked

steps:
  - ordinal: 1
    operation_summary: "Український стислий опис, що саме стверджується"
    input_state: "…"          # наш запис стану, не цитата Паніні
    source:
      kind: sutra              # sutra | commentary | traditional-principle | implementation-convenience
      reference: "3.1.68"
      text_ref: "registry/sutras/index.yaml#sutras.3.1.68"
      evidence_status: corpus-checked
    inherited_context:
      - source: "…"           # sūtra/adhikāra або commentary
        status: explicit | inferred | unresolved
        note: "Що саме успадковано й чому"
    interpretation:
      claim: "Як джерело застосовано до цього кроку"
      status: source-checked | interpretation | disputed
    transformation:
      before: "…"
      after: "…"
      representation_status: my-lisp-hypothesis
    alternatives:
      - status: rejected | unresolved
        reason: "Правило, умова або відсутній доказ"
    output_state: "…"

result:
  form_slp1: "…"
  display_iast: "…"
  confidence: source-checked | partial | blocked

open_issues:
  - "…"
```

## Інваріанти

- `source.reference` сам по собі не доводить `operation_summary`.
- `inherited_context.status: inferred` не можна подавати як прямий текст
  sūtra.
- `transformation` — завжди наше представлення. Воно має явно нести
  `representation_status`, навіть якщо джерело кроку безсумнівне.
- За відсутності джерела або прозорого коментарного ланцюга крок не
  «здогадується»: його статус `unresolved` або весь trace має `blocked`.
- Не підміняти `evidence_status` наявністю ID у локальному індексі. Значення
  береться з `registry/sutras/citation-provenance.yaml`.

## Мінімальна перевірка перед публікацією trace

1. Кожен sūtra-ID присутній у provenance-реєстрі.
2. Кожна згадана зміна форми має `before` і `after` у SLP1.
3. Кожен неявний anuvṛtti/adhikāra-контекст має статус `inferred` або
   `unresolved`, а не маскується як текст правила.
4. Відкинуті варіанти та конфлікти не вилучаються; їх записують у
   `alternatives`.
5. Кінцева форма не є доказом правильності шляху: trace перевіряють крок за
   кроком.

## Зв'язок із наявними прикладами

`examples/derivations/Bavati.md` і `dadAti.md` корисні як навчальні ланцюги,
але не задовольняють автоматично цей шаблон: у них потрібно окремо додати
структурований стан, provenance кожного кроку, спадкований контекст і
альтернативи. Це свідомо відкладено; не переписувати приклади масово без
окремого аудиту.

## Джерела

- [`rule-provenance-schema.md`](rule-provenance-schema.md) — поділ походження
  тверджень про правила.
- [`../foundation/anuvrtti.md`](../foundation/anuvrtti.md) — обмеження
  представлення спадкованого контексту.
- [`../research/derivation-examples-verification.md`](../research/derivation-examples-verification.md)
  — поточний стан доказів прикладів.
