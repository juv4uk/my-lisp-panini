# Documentation migration inventory / Інвентар міграції документації / Inventar der Dokumentationsmigration

## English

### Measured baseline — 2026-08-14

The offline checker reports 136 repository Markdown documents: 85 have the
required three language sections, 51 do not, and 17 have the sections in an
order different from `English → Ukrainian → German`. The result is an
inventory, not permission to mechanically translate research claims.

### Priority order

1. Complete the machine-facing specifications and derivation examples first:
   they define executable boundaries and are read by implementers.
2. Complete the research reports that make methodological, provenance, or
   source claims before descriptive surveys.
3. Normalize section order only after content exists in all three languages;
   Ukrainian remains the normative project language even though the stable
   presentation order is English, Ukrainian, German.
4. Treat `AGENTS.md` separately: it is an agent-control file in Ukrainian,
   not ordinary project documentation.

### Acceptance rule

Every migrated document must preserve the `[PANINI]`, `[INTERPRETATION]`, and
`[MY-LISP HYPOTHESIS]` boundary. A missing translation is preferable to an
invented scholarly claim. Run
`python3 panini/tools/check_documentation_languages.py` after each small batch.

## Українська

### Виміряна база — 2026-08-14

Offline checker показує 136 Markdown-документів репозиторію: 85 мають потрібні
три мовні секції, 51 їх не мають, а 17 мають інший порядок, ніж
`English → Ukrainian → German`. Це інвентар, а не дозвіл механічно перекладати
дослідницькі твердження.

### Порядок пріоритетів

1. Спершу завершити machine-facing specifications і приклади деривацій: вони
   визначають виконувані межі та потрібні реалізаторам.
2. Завершити research reports із методологічними, provenance або source
   твердженнями раніше за описові огляди.
3. Нормалізувати порядок секцій лише після появи змісту всіма трьома мовами;
   українська лишається нормативною мовою проєкту, хоча стабільний порядок
   подання — English, Ukrainian, German.
4. `AGENTS.md` розглядати окремо: це файл керування агентом українською, а не
   звичайна документація проєкту.

### Правило приймання

Кожен мігрований документ мусить зберегти межу `[PANINI]`, `[INTERPRETATION]`
та `[MY-LISP HYPOTHESIS]`. Відсутній переклад кращий за вигадане академічне
твердження. Після кожної малої партії запускати
`python3 panini/tools/check_documentation_languages.py`.

## Deutsch

### Gemessene Ausgangslage — 2026-08-14

Der Offline-Checker meldet 136 Markdown-Dokumente im Repository: 85 besitzen
die drei erforderlichen Sprachabschnitte, 51 nicht, und 17 verwenden eine
andere Reihenfolge als `English → Ukrainian → German`. Dies ist ein Inventar,
keine Erlaubnis zur mechanischen Übersetzung von Forschungsbehauptungen.

### Prioritätenfolge

1. Zuerst maschinennahen Spezifikationen und Derivationsbeispiele abschließen:
   Sie definieren ausführbare Grenzen und werden von Implementierenden gelesen.
2. Forschungsberichte mit methodischen, Provenienz- oder Quellenbehauptungen
   vor beschreibenden Übersichten vervollständigen.
3. Die Abschnittsreihenfolge erst normalisieren, wenn Inhalt in allen drei
   Sprachen existiert; Ukrainisch bleibt die normative Projektsprache, obwohl
   die stabile Darstellungsfolge Englisch, Ukrainisch, Deutsch ist.
4. `AGENTS.md` getrennt behandeln: Es ist eine ukrainische Agentensteuerdatei,
   keine gewöhnliche Projektdokumentation.

### Abnahmeregel

Jedes migrierte Dokument muss die Grenze `[PANINI]`, `[INTERPRETATION]` und
`[MY-LISP HYPOTHESIS]` wahren. Eine fehlende Übersetzung ist besser als eine
erfundene wissenschaftliche Behauptung. Nach jeder kleinen Charge
`python3 panini/tools/check_documentation_languages.py` ausführen.
