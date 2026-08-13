# External oracle fixture policy v0.1

Status: acceptance policy for `PANINI-EXTERNAL-ORACLE-FIXTURE-POLICY`. It
governs comparisons with independent software; it does not authorize a new
runtime dependency, registry rewrite, or historical claim.

## English summary

An external tool may produce a useful comparison result, not a canonical fact.
Every oracle fixture therefore pins the tool and data revision, records the
exact input/output and command, assigns a non-Pāṇini evidence status, and
defines how disagreement is retained. The Ukrainian section is normative.

## Українська

### [PANINI]

Вихід Vidyut, Sanskrit Heritage, `indic_transliteration` чи іншого програмного
засобу не є сам по собі висловлюванням Паніні. Навіть збіг результату із
очікуваною формою не доводить ані текстове джерело, ані повний порядок
деривації. Fixture фіксує порівняльний експеримент, а не замінює sūtra,
коментар або окрему джерельну перевірку.

### [INTERPRETATION]

Незалежні реалізації корисні саме тому, що їхні моделі й припущення відрізняються
від наших. Збіг кількох oracles підвищує цінність сигналу для дослідження, але
не перетворює його на автоматично встановлений факт. Розбіжність є даними:
її треба зберегти з pinned revisions, а не «виправити» вибором зручного output.

### [MY-LISP HYPOTHESIS]

#### Дозволені ролі

| Oracle | Допустима роль fixture | Недопустима роль |
|---|---|---|
| `indic_transliteration` | round-trip SLP1/IAST/Devanāgarī comparison | переписування canonical SLP1 у registry |
| Vidyut | порівняння форми, аналізу або trace-поведінки | runtime authority або доказ панінійського порядку |
| Sanskrit Heritage | незалежне зіставлення сегментації/аналізу | джерело canonical semantic graph |
| hosted API | ручний, збережений comparison artifact | мережевий build dependency |

#### Нормативна форма fixture

```yaml
id: oracle:<tool>:<stable-case-id>
tool:
  name: <canonical-name>
  revision: <tag|commit|package-version|image-digest>
  invocation: <exact WSL/Guix command or recorded manual procedure>
  source: <upstream URL>
data:
  artifacts: [<name@revision>]
  license_status: verified | needs-review | incompatible
input:
  representation: SLP1 | IAST | devanagari | tool-specific
  value: <literal input or content-addressed fixture path>
expected:
  kind: transliteration | surface-form | analysis | trace-observation
  value: <literal output or content-addressed fixture path>
evidence_status: test-result | interpretation | implementation-evidence
comparison:
  result: match | mismatch | unsupported | nondeterministic
  compared_on: YYYY-MM-DD
  normalization: none | named-display-only-transform
  notes: <loss, ambiguity, unavailable trace, or discrepancy>
provenance: [prov:<stable-id>]
```

1. `input.representation` і `expected.kind` обов'язкові: не можна порівнювати
   різні шари, наприклад display transliteration і canonical identifier.
2. `normalization: none` є типовим. Будь-яке інше значення має називати
   перетворення, бути display-only і не може змінювати registry input.
3. `match` говорить лише про збіг за зафіксованої версії та команди. Він не
   означає `verified` для джерельного твердження.
4. `mismatch`, `unsupported` і `nondeterministic` є валідними результатами й
   не видаляються. Для них створюється пов'язана задача або provenance record.
5. Для `trace-observation` fixture мусить вказати, чи output є `complete`,
   `partial` або `omitted` за `trace-evidence-model-v0.1.md`; форма без
   пояснювального trace не проходить як тест rule priority.
6. Кожен artifact має бути відтворюваним без мережевого запиту під час тесту.
   Веб-інтерфейс дозволений лише для одноразового вручну збереженого результату
   з датою та процедурою отримання.

#### Розбіжність і ескалація

```text
один oracle output
        ↓
порівняльний результат (не факт Паніні)
        ↓
збіг → залишити fixture як regression signal
розбіжність → зафіксувати обидва outputs і їхні revisions
        ↓
перевірити sūtra / коментар / межі представлення окремо
        ↓
лише потім — рішення про власну модель або test expectation
```

Заборонено змінювати expectation лише для того, щоб зробити oracle зелений.
Якщо наш expectation змінюється, commit має містити посилання на окремий
`ProvenanceRecord` і пояснювати, чи змінилася джерельна оцінка, інтерпретація
або реалізаційна гіпотеза.

#### Мінімальні приймальні критерії

1. Є принаймні один pinned fixture для кожного нового tool role.
2. Тест повідомляє tool revision, fixture ID і comparison result при помилці.
3. Секрети, URL із токенами, локальні домашні шляхи та мережеві відповіді без
   збереженого artifact не потрапляють у fixture.
4. Ліцензія коду та ліцензія даних мають окремий status.
5. Додавання fixture не змінює canonical SLP1-ID, My Lisp evaluator або VM без
   іншої схваленої задачі.

Пов'язані контракти: `external-tool-adr-template.md`,
`provenance-type-schema-v0.1.md`, `trace-evidence-model-v0.1.md` та
`useful-software-tools-audit.md`.

## Deutsch

Ein externes Werkzeug liefert ein Vergleichsergebnis, keine kanonische
Tatsache. Jedes Fixture pinnt Werkzeug- und Datenrevision, Eingabe, Ausgabe,
Kommando und Evidenzstatus. Abweichungen werden mitsamt beiden Ausgaben
aufbewahrt und danach gegen Quellen sowie Darstellungsgrenzen geprüft. Die
ukrainische Fassung ist normativ und vollständig.
