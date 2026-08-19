# Specification map / Карта специфікацій / Spezifikationskarte

## English

Specifications establish project boundaries and review conditions; they do not
by themselves prove claims about Pāṇini. Use the linked research records for
evidence and retain the three/four-layer labeling there. This map lists all
24 files currently in `panini/specs/` (refreshed 2026-08-19, `PANINI-SPECIFICATION-MAP-REFRESH` —
previously listed only 7, silently omitting 17 as the directory grew).

### Foundation and milestones

- [panini-foundation-v0.1.md](panini-foundation-v0.1.md) defines the current
  Foundation milestone and its intentionally limited scope.
- [gate-review.md](gate-review.md) records the criteria for moving from the
  Foundation to a machine model.
- [panini-derivation-machine-v0.1-milestone.md](panini-derivation-machine-v0.1-milestone.md)
  is the normative milestone superseding any near-term plan to integrate
  Pāṇinian vocabulary into My Lisp before derivation evidence exists.
- [my-lisp-p5-gate.md](my-lisp-p5-gate.md) permits only a joint,
  evidence-bound parser/evaluator review with My Lisp's P5 stage; it does not
  authorize a rename or premature integration.
- [panini-machine-model-reconciliation.md](panini-machine-model-reconciliation.md)
  replaces an earlier closure statement that overclaimed theoretical
  completeness, with an explicit boundary (2026-08-14).

### Bridge to My Lisp (hypotheses, not implementations)

- [bridge-to-my-lisp.md](bridge-to-my-lisp.md) lists provisional interface
  hypotheses; it is not a decision to modify My Lisp.
- [my-lisp-semantic-id-mapping.md](my-lisp-semantic-id-mapping.md) is a
  design-only mapping between Pāṇinian and My Lisp semantic IDs; not a
  runtime registry or parser/evaluator change.
- [mylisp-runtime-capability-contract.md](mylisp-runtime-capability-contract.md)
  fixes acceptance evidence to one exact executable, not a nearby checkout.
- [machine-mylisp-compatibility-boundary.md](machine-mylisp-compatibility-boundary.md)
  records blockers found by a read-only execution audit (2026-08-13); a
  verification boundary, not a runtime change.
- [machine-execution-path-v0.1.md](machine-execution-path-v0.1.md) names the
  one canonical executable path for `panini-machine-model-v0.1`
  (`panini/tests/machine-acceptance.my`).

### Derivation IR and trace contracts

- [derivation-ir-v0.1.md](derivation-ir-v0.1.md) is a data-design-only
  foundation-level machine-model proposal: no evaluator, parser, or registry
  migration, and no claim the structure itself is Pāṇini.
- [derivation-ir-trace-events-v0.1.md](derivation-ir-trace-events-v0.1.md)
  is a proposed event contract refining `trace-evidence-model-v0.1.md`.
- [trace-evidence-model-v0.1.md](trace-evidence-model-v0.1.md) specifies what
  a future derivation trace must expose for review.
- [trace-canonical-serialization-v0.1.md](trace-canonical-serialization-v0.1.md)
  fixes byte-level reproducibility for content-addressed Derivation IR states.
- [derivation-trace-template.md](derivation-trace-template.md) and
  [rule-provenance-schema.md](rule-provenance-schema.md) define auditable
  machine-facing record shapes.
- [derivation-machine-explanation-boundary-v0.1.md](derivation-machine-explanation-boundary-v0.1.md)
  is the contract for `PANINI-MACHINE-EXPLANATION-BOUNDARY`.
- [tripadi-visibility-relation-v0.1.md](tripadi-visibility-relation-v0.1.md)
  operationalizes the bounded conclusion of
  `research/tripadi-rule-exception-audit.md`; authorizes no parser, evaluator,
  or registry change.
- [derivation-corpus-stress-protocol-v0.1.md](derivation-corpus-stress-protocol-v0.1.md)
  is a research protocol; it does not add a My Lisp feature.

### Provenance and epistemic control

- [provenance-type-schema-v0.1.md](provenance-type-schema-v0.1.md) defines a
  common typed record for source claims, interpretations, and hypotheses.
- [philosophy-control-layer-v0.1.md](philosophy-control-layer-v0.1.md)
  governs admission and labelling of claims used by the project; not a
  reconstruction of a Pāṇinian mechanism or a rule executor.
- [anuvrtti-representation-boundary.md](anuvrtti-representation-boundary.md)
  and [karaka-role-cardinality.md](karaka-role-cardinality.md) document
  explicit representation constraints.
- [hypothesis-ledger.md](hypothesis-ledger.md) tracks hypotheses rather than
  presenting them as established Paninian facts.
- [siva-sutra-pinned-acquisition-protocol-v0.1.md](siva-sutra-pinned-acquisition-protocol-v0.1.md)
  is an acquisition policy; it creates no network build dependency and
  imports no source text by itself.

### External tools and oracles

- [external-oracle-fixture-policy-v0.1.md](external-oracle-fixture-policy-v0.1.md)
  governs comparisons with independent software; does not authorize a new
  runtime dependency or historical claim.
- [external-tool-adr-template.md](external-tool-adr-template.md) is a
  normative template filled out **before** adding any new external
  dependency, service, generator, or corpus tool.

## Українська

Специфікації встановлюють межі проєкту й умови перевірки; самі по собі вони не
доводять тверджень про Паніні. Для доказів використовуйте пов'язані
дослідницькі записи та зберігайте в них три/чотиришарове маркування. Ця карта
перелічує всі 24 файли, що зараз є в `panini/specs/` (оновлено 2026-08-19,
`PANINI-SPECIFICATION-MAP-REFRESH` — раніше перелічувала лише 7, мовчки
пропускаючи 17, доданих у міру росту директорії).

### Фундамент і milestone-и

- [panini-foundation-v0.1.md](panini-foundation-v0.1.md) визначає поточний
  milestone фундаменту й його навмисно обмежений обсяг.
- [gate-review.md](gate-review.md) фіксує критерії переходу від фундаменту до
  machine model.
- [panini-derivation-machine-v0.1-milestone.md](panini-derivation-machine-v0.1-milestone.md) —
  нормативний milestone, що скасовує будь-який найближчий план інтеграції
  панінійської термінології в My Lisp до появи доказів деривації.
- [my-lisp-p5-gate.md](my-lisp-p5-gate.md) дозволяє лише спільний,
  доказово обґрунтований парсер/evaluator-рев'ю зі стадією P5 My Lisp; не
  дозволяє перейменування чи передчасну інтеграцію.
- [panini-machine-model-reconciliation.md](panini-machine-model-reconciliation.md)
  замінює попереднє твердження про завершення, що перебільшувало теоретичну
  повноту, явною межею (2026-08-14).

### Міст до My Lisp (гіпотези, не реалізації)

- [bridge-to-my-lisp.md](bridge-to-my-lisp.md) перелічує попередні гіпотези
  інтерфейсу; це не рішення змінювати My Lisp.
- [my-lisp-semantic-id-mapping.md](my-lisp-semantic-id-mapping.md) — лише
  дизайн-відповідність між панінійськими й My Lisp semantic ID; не runtime
  реєстр і не зміна парсера/evaluator-а.
- [mylisp-runtime-capability-contract.md](mylisp-runtime-capability-contract.md)
  прив'язує доказову базу прийняття до одного конкретного виконуваного
  файлу, не до "приблизного" checkout.
- [machine-mylisp-compatibility-boundary.md](machine-mylisp-compatibility-boundary.md)
  фіксує блокери, знайдені read-only аудитом виконання (2026-08-13); межа
  верифікації, не зміна runtime.
- [machine-execution-path-v0.1.md](machine-execution-path-v0.1.md) називає
  єдиний канонічний виконуваний шлях для `panini-machine-model-v0.1`
  (`panini/tests/machine-acceptance.my`).

### Derivation IR і trace-контракти

- [derivation-ir-v0.1.md](derivation-ir-v0.1.md) — лише дизайн даних,
  foundation-рівня пропозиція machine-моделі: без evaluator-а, парсера чи
  міграції реєстру, і без твердження, що структура сама по собі є Паніні.
- [derivation-ir-trace-events-v0.1.md](derivation-ir-trace-events-v0.1.md) —
  пропонований контракт подій, що уточнює `trace-evidence-model-v0.1.md`.
- [trace-evidence-model-v0.1.md](trace-evidence-model-v0.1.md) визначає, що
  майбутній derivation trace має розкривати для рев'ю.
- [trace-canonical-serialization-v0.1.md](trace-canonical-serialization-v0.1.md)
  фіксує байтову відтворюваність для content-addressed станів Derivation IR.
- [derivation-trace-template.md](derivation-trace-template.md) та
  [rule-provenance-schema.md](rule-provenance-schema.md) задають форми
  записів, придатні для аудиту й машинного використання.
- [derivation-machine-explanation-boundary-v0.1.md](derivation-machine-explanation-boundary-v0.1.md) —
  контракт для `PANINI-MACHINE-EXPLANATION-BOUNDARY`.
- [tripadi-visibility-relation-v0.1.md](tripadi-visibility-relation-v0.1.md)
  операціоналізує обмежений висновок
  `research/tripadi-rule-exception-audit.md`; не дозволяє зміни парсера,
  evaluator-а чи реєстру.
- [derivation-corpus-stress-protocol-v0.1.md](derivation-corpus-stress-protocol-v0.1.md) —
  дослідницький протокол; не додає нову можливість My Lisp.

### Походження й епістемічний контроль

- [provenance-type-schema-v0.1.md](provenance-type-schema-v0.1.md) задає
  спільний типізований запис для джерельних тверджень, інтерпретацій і
  гіпотез.
- [philosophy-control-layer-v0.1.md](philosophy-control-layer-v0.1.md)
  регулює допуск і маркування тверджень, що використовує проєкт; не є
  реконструкцією панінійського механізму чи виконавцем правил.
- [anuvrtti-representation-boundary.md](anuvrtti-representation-boundary.md)
  та [karaka-role-cardinality.md](karaka-role-cardinality.md) документують
  явні обмеження представлення.
- [hypothesis-ledger.md](hypothesis-ledger.md) відстежує гіпотези, а не видає
  їх за встановлені панінійські факти.
- [siva-sutra-pinned-acquisition-protocol-v0.1.md](siva-sutra-pinned-acquisition-protocol-v0.1.md) —
  політика отримання джерел; сама по собі не створює мережеву build-залежність
  і не імпортує первинний текст.

### Зовнішні інструменти й оракули

- [external-oracle-fixture-policy-v0.1.md](external-oracle-fixture-policy-v0.1.md)
  регулює порівняння з незалежним ПЗ; не дозволяє нову runtime-залежність чи
  історичне твердження.
- [external-tool-adr-template.md](external-tool-adr-template.md) — нормативний
  шаблон, що заповнюють **до** додавання будь-якої нової зовнішньої
  залежності, сервісу, генератора чи корпусного інструмента.

## Deutsch

Spezifikationen bestimmen Projektgrenzen und Prüfbedingungen; sie beweisen
für sich genommen keine Behauptungen über Pāṇini. Für Evidenz sind die
verlinkten Forschungsaufzeichnungen zu verwenden, einschließlich ihrer
Drei-/Vierebenen-Kennzeichnung. Diese Karte listet alle 24 Dateien, die
derzeit in `panini/specs/` liegen (aktualisiert am 2026-08-19,
`PANINI-SPECIFICATION-MAP-REFRESH` — zuvor wurden nur 7 aufgeführt, 17 mit
dem Wachstum des Verzeichnisses stillschweigend ausgelassen).

### Fundament und Meilensteine

- [panini-foundation-v0.1.md](panini-foundation-v0.1.md) definiert den
  aktuellen Foundation-Meilenstein und seinen bewusst begrenzten Umfang.
- [gate-review.md](gate-review.md) hält die Kriterien für den Übergang von der
  Foundation zu einem Maschinenmodell fest.
- [panini-derivation-machine-v0.1-milestone.md](panini-derivation-machine-v0.1-milestone.md)
  ist der normative Meilenstein, der jeden kurzfristigen Plan zur Integration
  paninischer Terminologie in My Lisp vor Vorliegen von Ableitungsevidenz
  ersetzt.
- [my-lisp-p5-gate.md](my-lisp-p5-gate.md) erlaubt nur eine gemeinsame,
  evidenzbasierte Parser-/Evaluator-Prüfung mit der P5-Stufe von My Lisp;
  keine Umbenennung oder verfrühte Integration.
- [panini-machine-model-reconciliation.md](panini-machine-model-reconciliation.md)
  ersetzt eine frühere Abschlussaussage, die theoretische Vollständigkeit
  überbehauptete, durch eine explizite Grenze (2026-08-14).

### Brücke zu My Lisp (Hypothesen, keine Implementierungen)

- [bridge-to-my-lisp.md](bridge-to-my-lisp.md) listet vorläufige
  Schnittstellenhypothesen; keine Entscheidung, My Lisp zu ändern.
- [my-lisp-semantic-id-mapping.md](my-lisp-semantic-id-mapping.md) ist eine
  reine Design-Zuordnung zwischen paninischen und My-Lisp-Semantic-IDs; kein
  Laufzeitregister, keine Parser-/Evaluator-Änderung.
- [mylisp-runtime-capability-contract.md](mylisp-runtime-capability-contract.md)
  bindet die Abnahme-Evidenz an genau eine ausführbare Datei, nicht an einen
  ungefähren Checkout.
- [machine-mylisp-compatibility-boundary.md](machine-mylisp-compatibility-boundary.md)
  hält Blocker fest, die ein Nur-Lese-Ausführungsaudit fand (2026-08-13); eine
  Verifikationsgrenze, keine Laufzeitänderung.
- [machine-execution-path-v0.1.md](machine-execution-path-v0.1.md) benennt
  den einzigen kanonischen ausführbaren Pfad für `panini-machine-model-v0.1`
  (`panini/tests/machine-acceptance.my`).

### Derivation-IR- und Trace-Verträge

- [derivation-ir-v0.1.md](derivation-ir-v0.1.md) ist reines Datendesign, ein
  Vorschlag auf Foundation-Ebene: kein Evaluator, kein Parser, keine
  Registermigration, keine Behauptung, die Struktur selbst sei Pāṇini.
- [derivation-ir-trace-events-v0.1.md](derivation-ir-trace-events-v0.1.md)
  ist ein vorgeschlagener Ereignisvertrag, der `trace-evidence-model-v0.1.md`
  verfeinert.
- [trace-evidence-model-v0.1.md](trace-evidence-model-v0.1.md) legt fest, was
  eine künftige Derivation-Trace zur Prüfung offenlegen muss.
- [trace-canonical-serialization-v0.1.md](trace-canonical-serialization-v0.1.md)
  legt byte-genaue Reproduzierbarkeit für inhaltsadressierte
  Derivation-IR-Zustände fest.
- [derivation-trace-template.md](derivation-trace-template.md) und
  [rule-provenance-schema.md](rule-provenance-schema.md) definieren
  auditierbare, maschinenbezogene Datensatzformen.
- [derivation-machine-explanation-boundary-v0.1.md](derivation-machine-explanation-boundary-v0.1.md)
  ist der Vertrag für `PANINI-MACHINE-EXPLANATION-BOUNDARY`.
- [tripadi-visibility-relation-v0.1.md](tripadi-visibility-relation-v0.1.md)
  operationalisiert die begrenzte Schlussfolgerung von
  `research/tripadi-rule-exception-audit.md`; erlaubt keine Parser-,
  Evaluator- oder Registeränderung.
- [derivation-corpus-stress-protocol-v0.1.md](derivation-corpus-stress-protocol-v0.1.md)
  ist ein Forschungsprotokoll; fügt My Lisp kein Feature hinzu.

### Herkunft und epistemische Kontrolle

- [provenance-type-schema-v0.1.md](provenance-type-schema-v0.1.md) definiert
  einen gemeinsamen typisierten Datensatz für Quellenbehauptungen,
  Interpretationen und Hypothesen.
- [philosophy-control-layer-v0.1.md](philosophy-control-layer-v0.1.md)
  regelt die Zulassung und Kennzeichnung von Behauptungen, die das Projekt
  verwendet; keine Rekonstruktion eines paninischen Mechanismus, kein
  Regelausführer.
- [anuvrtti-representation-boundary.md](anuvrtti-representation-boundary.md)
  und [karaka-role-cardinality.md](karaka-role-cardinality.md) dokumentieren
  explizite Repräsentationsgrenzen.
- [hypothesis-ledger.md](hypothesis-ledger.md) verfolgt Hypothesen, statt sie
  als gesicherte paninische Tatsachen darzustellen.
- [siva-sutra-pinned-acquisition-protocol-v0.1.md](siva-sutra-pinned-acquisition-protocol-v0.1.md)
  ist eine Beschaffungsrichtlinie; schafft für sich genommen keine
  Netzwerk-Build-Abhängigkeit und importiert keinen Quelltext.

### Externe Werkzeuge und Orakel

- [external-oracle-fixture-policy-v0.1.md](external-oracle-fixture-policy-v0.1.md)
  regelt Vergleiche mit unabhängiger Software; erlaubt keine neue
  Laufzeitabhängigkeit oder historische Behauptung.
- [external-tool-adr-template.md](external-tool-adr-template.md) ist eine
  normative Vorlage, die **vor** dem Hinzufügen jeder neuen externen
  Abhängigkeit, jedes Dienstes, Generators oder Korpuswerkzeugs auszufüllen
  ist.
