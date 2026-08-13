# Шаблон ADR для зовнішнього програмного засобу

Статус: нормативний шаблон для `PANINI-EXTERNAL-TOOL-ADR-TEMPLATE`.

Цей документ заповнюють **до** додавання нової залежності, сервісу, генератора,
корпусного інструмента або іншого зовнішнього програмного засобу. Публічний
репозиторій чи веб-API самі по собі не є підставою для інтеграції.

## Українська

### 1. Рішення

- **Інструмент:** `<назва>`
- **Рішення:** `прийняти | оцінити ізольовано | відкласти | відхилити`
- **Роль:** `test-oracle | IDE | offline-analysis | runtime-candidate | data-converter`
- **Власник рішення:** `<node або відповідальний агент>`
- **Дата й revision:** `<YYYY-MM-DD, tag/commit/package hash>`

### 2. Проблема та межа

Яку конкретну проблему вирішує інструмент? Який компонент нашої системи
залишається його власником? Не пишіть «покращує санскритську підтримку»:
потрібна вимірювана межа, наприклад «перевіряє 40 SLP1 → IAST fixtures».

```text
Проблема:
Межа входу:
Межа виходу:
Що інструмент НЕ визначає:
```

### 3. Походження, ліцензія й дані

```yaml
tool:
  upstream: <canonical URL>
  revision: <immutable tag/commit/package hash>
  license:
    value: <SPDX або unresolved>
    checked_at: <URL до LICENSE або офіційної сторінки>
    status: verified | needs-review | incompatible
data_dependencies:
  - artifact: <name>
    revision: <revision>
    license: <SPDX/terms>
    allowed_use: navigation | comparison | test | import-pending
```

Ліцензія коду й ліцензія даних фіксуються окремо. Для hosted API також
фіксуються terms, rate limits і те, що API ніколи не є build dependency або
джерелом canonical runtime data.

### 4. Доказовий статус результатів

| Вихід інструмента | Статус у проєкті | Що потрібно зберегти |
|---|---|---|
| транслітерація/нормалізація | test-result | input, output, scheme, revision |
| морфологічний аналіз | interpretation | query, output, oracle revision |
| rule trace | implementation evidence | trace, rule IDs, provenance |
| corpus annotation | corpus evidence | artifact revision, schema, license |

Жоден output не може автоматично отримати статус `[PANINI]`. Для кожного
результату треба створити або послатися на `ProvenanceRecord`.

### 5. Відтворюваність у WSL / Guix

```bash
wsl -u my-lisp-panini -- bash -lc \
  'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm -- <command>'
```

Записати точну команду, очікуваний exit code, hashes вхідних fixtures і спосіб
отримання залежностей. Якщо інструмент не працює в Guix без неперевірюваного
мережевого стану, він не є runtime candidate.

### 6. Failure model і приватність

- Як інструмент поводиться з невалідним SLP1, Unicode або неоднозначним вводом?
- Чи може він мовчки нормалізувати/втратити інформацію?
- Чи відправляє він текст, код або дані на зовнішній сервіс?
- Який fallback існує без мережі?

### 7. Приймальні та вихідні критерії

```yaml
acceptance:
  - <детерміністичний fixture або вимірюваний тест>
  - <перевірена ліцензія коду і даних>
  - <Guix команда успішна>
exit_criterion:
  - <умова видалення/відмови, наприклад нереверсивна SLP1 втрата>
```

### 8. Наслідки та наступні задачі

Опишіть мінімальні нові файли, тести, provenance записи й owner boundaries.
Заборонено використовувати ADR як мовчазний дозвіл змінювати My Lisp, VM або
registry: такі зміни потребують окремих задач і відповідних gate.

## English summary

This template is an admission gate for external tools. It requires a pinned
revision, separate code/data license review, a narrow ownership boundary,
reproducible WSL/Guix command, provenance status for output, failure model, and
measurable acceptance and removal criteria. Tool output is never automatically
`[PANINI]` evidence.

## Deutsch

Diese Vorlage ist ein Zulassungstor für externe Werkzeuge. Sie verlangt eine
fixierte Revision, getrennte Prüfung von Code- und Datenlizenz, eine enge
Verantwortungsgrenze, reproduzierbaren WSL/Guix-Befehl, Provenienzstatus der
Ausgabe, Fehlermodell sowie messbare Annahme- und Entfernungskriterien.
Werkzeugausgabe wird niemals automatisch zu `[PANINI]`-Evidenz.
