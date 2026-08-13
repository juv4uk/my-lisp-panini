# Derivation corpus stress protocol v0.1

Status: `proposed`. Research protocol; it does not add a My Lisp feature.

## English — reference translation

### Goal

Grow the corpus of documented, reproducible derivations until the existing
Panini Machine exposes its limits. The purpose is not to demonstrate that the
machine is universally adequate, nor to add My Lisp semantics. A failure,
`unknown`, `partial`, or `blocked` result with evidence is a successful research
observation.

My Lisp is presently the laboratory runtime for bounded executable fixtures.
`panini/machine/panini-core.my` remains a machine snapshot; the structured
records under `panini/registry/` and their source provenance remain authoritative.

### Corpus stages

| Stage | Target | Required diversity |
|---|---:|---|
| C20 | 20 derivations | several dhātu classes; suffixation, guṇa/sandhi, designations, at least one conflict and one negative fixture |
| C50 | 50 derivations | multiple scopes and rule interactions; at least five justified `partial`/`blocked` or rejected paths |
| C100 | 100 derivations | broad enough to reveal recurring missing concepts, unsupported scheduler assumptions, and provenance gaps |

The number alone is not acceptance. Each added case must have a documented
source path, a bounded machine claim, and an explicit evidence grade.

### Required record for each case

1. Input form and canonical SLP1 identifiers.
2. Source references and their provenance categories.
3. Terms, designations, immutable initial state, and expected surface result
   when the evidence warrants one.
4. Candidate rules, visibility conditions, conflicts, operations, and the
   complete append-only trace.
5. Final status: `verified`, `derived`, `needs-check`, `disputed`, `partial`,
   `blocked`, or rejected negative fixture.
6. A note separating `[PANINI]`, `[INTERPRETATION]`, and
   `[MY-LISP HYPOTHESIS]`.

### Stress signals and response

Do not patch around a stress signal silently. Record it first:

| Signal | Required response |
|---|---|
| A rule cannot be selected from current evidence | retain candidates; emit `unknown` or `blocked` |
| A visibility or precedence rule is unclear | record the unresolved relation; do not invent a universal scheduler |
| A term needs a distinction absent from the IR | add a counterexample and assess whether it is Paninian, interpretive, or implementation-only |
| A surface result disagrees with the fixture | preserve the trace and add a negative or disputed case before changing a rule |
| A kāraka resembles a modern role | keep the Paninian identifier separate from any interpretation bridge |

No datum may cross namespaces implicitly. For example, `panini:kartf`, an
interpretive `agent`, and a possible `my-lisp:semantic-agent` are distinct
claims. Any mapping must be an explicit experimental hypothesis with evidence,
confidence, and status; revising it must not rewrite Panini records or history.

### Acceptance for a stage

A stage is accepted only when every case runs through the canonical execution
path where executable, negative cases are rejected for the stated reason, and
all non-final outcomes remain visible in the portfolio. The stage report must
summarize recurring failures before proposing any new IR field, scheduler rule,
or My Lisp integration.

## Українська — нормативна

### Мета

Розширювати корпус документованих і відтворюваних деривацій доти, доки наявна
Panini Machine не покаже власні межі. Мета не в тому, щоб довести її загальну
достатність, і не в тому, щоб додати семантику My Lisp. Збій, `unknown`,
`partial` або `blocked` з доказами — успішне дослідницьке спостереження.

My Lisp нині є лабораторним runtime для обмежених виконуваних fixture.
`panini/machine/panini-core.my` лишається machine snapshot; авторитетними
лишаються структуровані записи в `panini/registry/` та їхнє source provenance.

### Етапи корпусу

| Етап | Мета | Обов'язкова різноманітність |
|---|---:|---|
| C20 | 20 деривацій | кілька класів dhātu; suffixation, guṇa/sandhi, designations, щонайменше один conflict і один negative fixture |
| C50 | 50 деривацій | кілька scope і взаємодій правил; щонайменше п'ять обґрунтованих `partial`/`blocked` або відхилених шляхів |
| C100 | 100 деривацій | корпус, достатній для виявлення повторюваних відсутніх понять, необґрунтованих scheduler-припущень і provenance-прогалин |

Саме число не є критерієм прийняття. Кожен випадок має мати задокументований
source path, обмежене машинне твердження та явний evidence grade.

### Обов'язковий запис для кожного випадку

1. Вхідна форма та canonical SLP1 identifiers.
2. Source references і їхні provenance-категорії.
3. Terms, designations, immutable initial state й очікуваний surface result,
   якщо докази дають підстави його стверджувати.
4. Candidate rules, visibility conditions, conflicts, operations і повний
   append-only trace.
5. Підсумковий статус: `verified`, `derived`, `needs-check`, `disputed`,
   `partial`, `blocked` або відхилений negative fixture.
6. Нотатка з окремими рівнями `[PANINI]`, `[INTERPRETATION]` і
   `[MY-LISP HYPOTHESIS]`.

### Сигнали стресу та реакція

Не можна мовчки латати сигнал стресу. Спочатку його фіксують:

| Сигнал | Обов'язкова реакція |
|---|---|
| Неможливо вибрати правило з наявних доказів | зберегти кандидатів; видати `unknown` або `blocked` |
| Незрозуміле правило visibility чи precedence | зафіксувати unresolved relation; не вигадувати універсальний scheduler |
| Term потребує відсутнього в IR розрізнення | додати counterexample і визначити, чи це Panini, інтерпретація або лише реалізація |
| Surface result не збігається з fixture | зберегти trace й додати negative або disputed випадок до зміни правила |
| Kāraka схожа на сучасну роль | не змішувати Panini ID та interpretation bridge |

Жодне дане не переходить між namespace неявно. Наприклад, `panini:kartf`,
інтерпретаційне `agent` і можливе `my-lisp:semantic-agent` — різні твердження.
Будь-яке відображення між ними є явною експериментальною гіпотезою з evidence,
confidence і status; його перегляд не повинен переписувати Panini records або
історію.

### Прийняття етапу

Етап приймається лише тоді, коли всі виконувані випадки проходять canonical
execution path, negative cases відхиляються з указаною причиною, а всі
неостаточні результати лишаються видимими в portfolio. Звіт етапу має
підсумувати повторювані збої **до** пропозиції нового поля IR, scheduler-правила
або інтеграції My Lisp.

## Deutsch — Referenzübersetzung

### Ziel

Der Korpus dokumentierter, reproduzierbarer Derivationen wird erweitert, bis
die bestehende Panini Machine ihre Grenzen zeigt. Es geht weder um einen Beweis
universeller Angemessenheit noch um neue My-Lisp-Semantik. Ein belegter Fehler,
`unknown`, `partial` oder `blocked` ist eine erfolgreiche Beobachtung.

My Lisp ist derzeit die Labor-Runtime für begrenzte ausführbare Fixtures.
`panini/machine/panini-core.my` bleibt ein Machine-Snapshot; die strukturierten
Einträge in `panini/registry/` und ihre Source-Provenance bleiben autoritativ.

### Korpusphasen

| Phase | Ziel | Erforderliche Vielfalt |
|---|---:|---|
| C20 | 20 Derivationen | mehrere dhātu-Klassen; Suffixation, guṇa/sandhi, Designations, mindestens ein Konflikt und ein negatives Fixture |
| C50 | 50 Derivationen | mehrere Scopes und Regelinteraktionen; mindestens fünf begründete `partial`/`blocked` oder verworfene Wege |
| C100 | 100 Derivationen | genug Fälle für wiederkehrende fehlende Begriffe, unbelegte Scheduler-Annahmen und Provenance-Lücken |

Jeder Fall benötigt Source Path, begrenzte Maschinenbehauptung und expliziten
Evidence Grade. Stresssignale werden nicht still repariert: unklare Auswahl
bleibt `unknown`/`blocked`, unklare Sichtbarkeit bleibt unresolved, und ein
abweichendes Ergebnis wird vor einer Regeländerung als negatives oder
`disputed` Fixture erhalten.

`panini:kartf`, ein interpretatives `agent` und mögliches
`my-lisp:semantic-agent` bleiben getrennte Behauptungen. Eine Abbildung ist
eine explizite experimentelle Hypothese mit Evidence, Confidence und Status.
Eine Phase wird erst akzeptiert, wenn der kanonische Ausführungspfad,
negative Ablehnungen und alle nicht-finalen Ergebnisse im Portfolio sichtbar
sind; der Bericht fasst wiederkehrende Fehler vor jeder neuen IR-, Scheduler-
oder My-Lisp-Integration zusammen.
