# Audit of Metalanguage Boundaries / Аудит меж метамови / Prüfung der Metasprachengrenzen

Status: completed (`PANINI-PHILOSOPHER-METALANGUAGE-BOUNDARIES`)
Author: my-lisp-panini-1
Related: `ontology.md`, `samjna.md`, `rules.my`

---

## 🇺🇸 English: Audit Findings
### Problem Definition
A "category mistake" occurs when an implementation or theoretical model confuses different levels of Pāṇini's grammatical architecture. The main levels are:
1. **Object Language**: The actual Sanskrit words being generated (e.g., `dadāti`, `bhavati`).
2. **Metalanguage (Upadeśa / Saṃjñā)**: The artificial terms used to describe the rules (e.g., `ṭip`, `śap`, `guṇa`, `kāraka`).
3. **Implementation Mechanism**: How a computer executes the rules (e.g., Lisp macros, tag checks, graph nodes).

### Cited Examples of Category Mistakes in Current/Past Models
1. **Confusing Saṃjñā with Tags**: Treating a `saṃjñā` (a formal categorization with membership criteria) simply as an arbitrary string tag (`(term-add-tag term 'sArvaDAtukaM)`). *Resolved by `samjna-categorization-vs-tag.md` research.*
2. **Confusing Anuvṛtti with Dynamic Binding**: Equating textual rule-inheritance (`anuvṛtti`) with Lisp's dynamic scoping (`let` bindings in `with-adhikara`). *Resolved by `anuvrtti-graph-vs-dynamic-binding.md` research.*
3. **Confusing Kāraka with Syntactic Subject/Object**: Mapping `kartṛ` directly to "subject" without realizing `kartṛ` is a semantic-level predicate (the independent initiator of action).

### Architectural Guardrails
To prevent future boundary violations, the `meta.my` engine must explicitly separate the **Pāṇinian rule layer** (the definition of `apavāda`, `utsarga`, `adhikāra`) from the **Lisp execution layer** (how the graph is traversed). We must never translate Lisp primitives as Pāṇinian terms unless proven computationally homologous.

---

## 🇺🇦 Українська: Результати аудиту
### Визначення проблеми
"Категорійна помилка" (category mistake) виникає, коли реалізація або теоретична модель плутає різні рівні граматичної архітектури Паніні. Основними рівнями є:
1. **Об'єктна мова (Object Language)**: Фактичні санскритські слова, що генеруються (наприклад, `dadāti`, `bhavati`).
2. **Метамова (Upadeśa / Saṃjñā)**: Штучні терміни, що використовуються для опису правил (наприклад, `ṭip`, `śap`, `guṇa`, `kāraka`).
3. **Механізм реалізації (Implementation Mechanism)**: Те, як комп'ютер виконує правила (наприклад, Lisp макроси, перевірка тегів, вузли графа).

### Наведені приклади категорійних помилок у поточних/минулих моделях
1. **Плутання Saṃjñā з Тегами**: Сприйняття `saṃjñā` (формальної категоризації з критеріями членства) просто як довільного рядкового тегу (`(term-add-tag term 'sArvaDAtukaM)`). *Вирішено дослідженням `samjna-categorization-vs-tag.md`.*
2. **Плутання Anuvṛtti з Динамічним Зв'язуванням**: Прирівнювання текстового успадкування правил (`anuvṛtti`) до динамічної області видимості Lisp (`let` binding у `with-adhikara`). *Вирішено дослідженням `anuvrtti-graph-vs-dynamic-binding.md`.*
3. **Плутання Kāraka з Синтаксичним Підметом/Додатком**: Пряме відображення `kartṛ` на "підмет" без усвідомлення того, що `kartṛ` є предикатом семантичного рівня (незалежний ініціатор дії).

### Архітектурні запобіжники
Щоб запобігти майбутнім порушенням меж, рушій `meta.my` повинен чітко відокремлювати **рівень правил Паніні** (визначення `apavāda`, `utsarga`, `adhikāra`) від **рівня виконання Lisp** (як відбувається обхід графа). Ми ніколи не повинні перекладати примітиви Lisp як терміни Паніні, якщо не доведено їхню обчислювальну гомологічність.

---

## 🇩🇪 Deutsch: Prüfungsergebnisse
### Problemdefinition
Ein "Kategorienfehler" tritt auf, wenn eine Implementierung oder ein theoretisches Modell verschiedene Ebenen von Pāṇinis grammatikalischer Architektur verwechselt. Die Hauptebenen sind:
1. **Objektsprache**: Die tatsächlichen Sanskrit-Wörter, die generiert werden (z. B. `dadāti`, `bhavati`).
2. **Metasprache (Upadeśa / Saṃjñā)**: Die künstlichen Begriffe, die zur Beschreibung der Regeln verwendet werden (z. B. `ṭip`, `śap`, `guṇa`, `kāraka`).
3. **Implementierungsmechanismus**: Wie ein Computer die Regeln ausführt (z. B. Lisp-Makros, Tag-Prüfungen, Graphknoten).

### Zitierte Beispiele für Kategorienfehler in aktuellen/früheren Modellen
1. **Verwechslung von Saṃjñā mit Tags**: Die Behandlung einer `saṃjñā` (einer formalen Kategorisierung mit Mitgliedschaftskriterien) einfach als ein beliebiges String-Tag (`(term-add-tag term 'sArvaDAtukaM)`). *Gelöst durch die Forschung in `samjna-categorization-vs-tag.md`.*
2. **Verwechslung von Anuvṛtti mit Dynamic Binding**: Die Gleichsetzung von textueller Regelvererbung (`anuvṛtti`) mit der dynamischen Gültigkeitsbereich von Lisp (`let`-Bindungen in `with-adhikara`). *Gelöst durch die Forschung in `anuvrtti-graph-vs-dynamic-binding.md`.*
3. **Verwechslung von Kāraka mit syntaktischem Subjekt/Objekt**: Die direkte Zuordnung von `kartṛ` zu "Subjekt", ohne zu erkennen, dass `kartṛ` ein Prädikat auf semantischer Ebene ist (der unabhängige Initiator der Handlung).

### Architektonische Leitplanken
Um zukünftige Grenzverletzungen zu verhindern, muss die `meta.my`-Engine die **Pāṇinianische Regelebene** (die Definition von `apavāda`, `utsarga`, `adhikāra`) strikt von der **Lisp-Ausführungsebene** (wie der Graph durchlaufen wird) trennen. Wir dürfen Lisp-Primitive niemals als Pāṇini-Begriffe übersetzen, es sei denn, ihre computergestützte Homologie ist bewiesen.
