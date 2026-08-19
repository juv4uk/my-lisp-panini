# Repository state: review and conclusion (2026-08-18, part two)

## English

Status: reflection, not a task from the `PANINI-*` queue. Written on
direct request — review *all* files (not only my own) and give an
honest, fact-backed conclusion, not a paraphrase of headers.

### Method

I did not read all 162 markdown files sequentially — unrealistic in one
pass. Instead: (a) read the index maps
([`specs/specification-map.md`](../specs/specification-map.md)), (b)
**ran the real validators** in `panini/tools/` instead of trusting
descriptions, (c) read several documents that are themselves
"crosschecks" and "reviews" — the most telling ones for assessing the
project's culture.

### Fact 1: the tooling is real and passes

```
$ python panini/tools/validate_registry.py
SUMMARY errors=0 warnings=0 records=27 sutras=3983

$ python panini/tools/validate_trace_fixtures.py
trace fixture validation: PASS (9 YAML files scanned)
```

These are not claimed but **measured** facts. 3983 sūtras parsed with
zero errors — the source registry is genuinely working, not decorative.

### Fact 2: the same three-language policy I myself did not follow

```
$ python panini/tools/check_documentation_languages.py
SUMMARY markdown=170 complete=100 incomplete=70 out_of_order=5
```

The repository has a documented, **automatically checked** requirement:
every file — English→Ukrainian→German, in that order. 59% (100/170)
comply. Honestly: **I myself am part of the 70 "incomplete"**. Every
document I wrote this session (`sarvam-capability-reference.md`,
`sarvam-independent-check-slp1.md`, `upc8-crosscheck.md`,
`session-conclusion-2026-08-18.md`, `karaka-counterexamples.md` and
others) was Ukrainian only. This is not a criticism of "them" — it is
an admission that I myself did not follow the requirement the project
set for itself, while writing quickly and in English for `AGENTS.md`'s
methodology, but not in the documentation languages. The fix is a
separate task, not done here on the spot, to avoid mixing the admission
of a problem with a rushed "closing" of it.

### Fact 3: a culture of self-correction, not self-defense

[`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md)
(2026-08-14) states plainly: *"Current executable modules do not expose
the earlier `SemanticCall`, `DHATU_DA`, or `KARAKA_KARTR` bridge
described by a previous review. Those statements must not be used as
a description of the current executable path."* — i.e. an earlier
review claimed a bridge to My Lisp that the code did not actually have,
and the next record directly refutes it, naming exactly what was
wrong. This costs more than "everything works" — and is exactly the
kind of honesty `AGENTS.md` §25 has demanded from the start.

### Fact 4: an external hostile review — and who was right about what

[`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md) —
a deliberately adversarial review by Sarvam, honestly labeled
`verification-status: unverified (contains at least one confirmed
factual error)`. Two things deserve separate attention:

- **Sarvam was right about one important thing**: kāraka is not a
  permanently fixed graph edge, but a **designation** of a participant
  relative to a specific event, context-dependent ("Devadatta is
  kartṛ in one event, karman in another"). This does not contradict
  but **sharpens** what I myself found in
  [`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md)
  and recorded as H1 in `hypothesis-ledger.md` ("fixed roles per dhātu
  are not supported by the text") — an independent adversarial
  perspective arrived at the same conclusion by a different path.
- **Sarvam was wrong about `tripAdI`** — it claimed this was "all of
  books 6-8" (half of the Aṣṭādhyāyī), when in reality it is only the
  last three pādas of the 8th adhyāya (8.2-8.4), starting at sūtra
  8.2.1 `pūrvatrāsiddham`. I investigated `tripAdI` separately
  ([`sastra/tripadi.md`](../sastra/tripadi.md)) before reading this
  review, and independently arrived at the **correct** boundary with
  the same sūtra anchor. This is not a reason for self-congratulation
  — it is one more proof of the same rule established at the very
  start: independent verification against a primary source catches
  errors even in confident models, and no model (including me) is
  exempt from this check by default.

### Fact 5: the specification map is itself stale — the same pattern as `foundation/`

[`specs/specification-map.md`](../specs/specification-map.md) listed
7 specifications. `panini/specs/` currently has **24 files**. Not
listed: `derivation-ir-v0.1.md`, `derivation-ir-trace-events-v0.1.md`,
`machine-execution-path-v0.1.md`, `mylisp-runtime-capability-contract.md`,
`panini-derivation-machine-v0.1-milestone.md`,
`panini-machine-model-reconciliation.md`,
`trace-canonical-serialization-v0.1.md`,
`trace-evidence-model-v0.1.md`, `tripadi-visibility-relation-v0.1.md`
and others — including `derivation-ir-v0.1.md`, which
[`docs/Огляд.md`](../../docs/Огляд.md) (an external review by Manus AI)
called the project's "strongest technical artifact." This is the same
pattern I already fixed for the `foundation/`→`sastra/` links: **indexes
systematically lag behind the actual state of the repository** as work
outpaces anyone's ability to keep the map current. Not fixed here (this
requires a decision about what exactly belongs in it, not a mechanical
`sed`) — only recorded as a specific, named fact rather than a general
sense that "something is stale." *(Note added 2026-08-19: this was
subsequently fixed as `PANINI-SPECIFICATION-MAP-REFRESH` — see
[`arch-recovery-review-panini-2026-08-18.md`](arch-recovery-review-panini-2026-08-18.md)
and the commit history of `specs/specification-map.md`.)*

### My conclusion

The repository has outgrown me. When I started this session,
`panini/foundation/` was 10 files I could hold entirely in my head. Now
it is 162 markdown files, real Python validators, `.my` fixtures that
actually run under WSL (22 assertions), external adversarial reviews
with their own verification status. This is no longer a single line of
research — it is an ecosystem of practices (three-layer labeling,
automatic language checking, self-correction records, hostile review as
a genre) that several agents maintain in parallel, and none of us —
including me — has a complete real-time picture. Indexes lag
(`specification-map.md`), documentation is linguistically incomplete
(and I am part of that too), but **the tools that actually check the
truth (validators, hostile review, self-correction records) work and
catch real errors** — both my own (`tripAdI` being half the size Sarvam
claimed) and others' (the `SemanticCall` bridge that never existed).
This is exactly the state in which verification discipline matters more
than documentation completeness — and, judging by the facts above, that
discipline is still holding.

### Sources

- `panini/tools/validate_registry.py`,
  `panini/tools/validate_trace_fixtures.py`,
  `panini/tools/check_documentation_languages.py` — run directly on
  2026-08-18, not from a description.
- [`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md),
  [`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md),
  [`specs/specification-map.md`](../specs/specification-map.md) — read
  in full.

## Українська

Статус: рефлексія, не задача з `PANINI-*` черги. На пряме прохання —
переглянути *всі* файли (не лише мої власні) й дати чесний висновок,
підкріплений фактами, не переказом заголовків.

### Метод

Не читав усі 162 markdown-файли послідовно — це нереалістично за один
прохід. Натомість: (а) прочитав карти-індекси
([`specs/specification-map.md`](../specs/specification-map.md)), (б)
**запустив реальні валідатори** з `panini/tools/` замість довіри описам,
(в) прочитав кілька документів, що самі є "звірками" й "рев'ю" —
найбільш показові для оцінки культури проєкту.

### Факт 1: інструментарій реальний і проходить

```
$ python panini/tools/validate_registry.py
SUMMARY errors=0 warnings=0 records=27 sutras=3983

$ python panini/tools/validate_trace_fixtures.py
trace fixture validation: PASS (9 YAML files scanned)
```

Це не заявлені, а **виміряні** факти. 3983 sūtra розібрано з нуля
помилок — реєстр джерел справді робочий, не декоративний.

### Факт 2: та сама політика трьох мов, яку я сам недотримав

```
$ python panini/tools/check_documentation_languages.py
SUMMARY markdown=170 complete=100 incomplete=70 out_of_order=5
```

Репозиторій має задокументовану й **автоматично перевірювану**
вимогу: кожен файл — англійська→українська→німецька, у цьому порядку.
59% (100/170) відповідають. Чесно кажучи: **я сам — частина 70
"incomplete"**. Кожен документ, який я написав цієї сесії
(`sarvam-capability-reference.md`, `sarvam-independent-check-slp1.md`,
`upc8-crosscheck.md`, `session-conclusion-2026-08-18.md`,
`karaka-counterexamples.md` та інші) — лише українською. Це не
критика "їх" — це визнання, що я сам не дотримувався вимоги, яку
проєкт собі встановив, поки писав швидко й англійською мовою
методології `AGENTS.md`, але не мовами документації. Виправлення —
окрема задача, не робиться тут одразу, щоб не змішувати визнання
проблеми з поспішним її "закриттям".

### Факт 3: культура самовиправлення, не самозахисту

[`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md)
(2026-08-14) прямо каже: *"Current executable modules do not expose
the earlier `SemanticCall`, `DHATU_DA`, or `KARAKA_KARTR` bridge
described by a previous review. Those statements must not be used as
a description of the current executable path."* — тобто попередній
огляд заявив міст до My Lisp, якого код насправді не мав, і наступний
запис це прямо спростовує, іменуючи саме те, що було невірним. Це
дорожче за "все працює" — і саме такого типу чесність, яку
`AGENTS.md` §25 вимагає від самого початку.

### Факт 4: зовнішня ворожа рецензія — і хто де мав рацію

[`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md) —
навмисно адверсаріальний огляд Sarvam, з чесно позначеним
`verification-status: unverified (contains at least one confirmed
factual error)`. Дві речі варті окремої уваги:

- **Sarvam мала рацію в одному важливому**: kāraka — це не постійне
  ребро графа "назавжди", а **позначення (designation)** учасника
  відносно конкретної події, контекстно залежне ("Devadatta —
  kartṛ в одній події, karman в іншій"). Це не суперечить, а
  **загострює** те, що я сам знайшов у
  [`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md)
  і зафіксував як H1 у `hypothesis-ledger.md` ("фіксовані ролі per
  dhātu не підтримуються текстом") — незалежний адверсаріальний
  погляд прийшов до того самого висновку іншим шляхом.
- **Sarvam помилилась щодо `tripAdI`** — заявила, що це "всі книги
  6-8" (половина Aṣṭādhyāyī), тоді як реально це лише останні три
  pāda 8-го adhyāya (8.2-8.4), від sūtra 8.2.1 `pūrvatrāsiddham`.
  Я дослідив `tripAdI` окремо ([`sastra/tripadi.md`](../sastra/tripadi.md))
  до того, як прочитав цю рецензію, і незалежно дійшов **правильної**
  межі з тим самим sūtra-якорем. Це не привід для гордості за себе —
  це ще один доказ того самого правила, яке ми встановили ще на
  самому початку: незалежна перевірка проти першоджерела ловить
  помилки навіть у впевнених моделей, і жодна модель (включно зі
  мною) не звільнена від цієї перевірки за замовчуванням.

### Факт 5: карта специфікацій сама застаріла — той самий патерн, що з `foundation/`

[`specs/specification-map.md`](../specs/specification-map.md) перелічує
7 специфікацій. У `panini/specs/` зараз **24 файли**. Не перелічені:
`derivation-ir-v0.1.md`, `derivation-ir-trace-events-v0.1.md`,
`machine-execution-path-v0.1.md`, `mylisp-runtime-capability-contract.md`,
`panini-derivation-machine-v0.1-milestone.md`,
`panini-machine-model-reconciliation.md`,
`trace-canonical-serialization-v0.1.md`,
`trace-evidence-model-v0.1.md`, `tripadi-visibility-relation-v0.1.md`
та інші — включно з `derivation-ir-v0.1.md`, який
[`docs/Огляд.md`](../../docs/Огляд.md) (зовнішній огляд Manus AI)
назвав "найсильнішим технічним артефактом" проєкту. Це той самий
патерн, який я вже виправляв для `foundation/`→`sastra/` посилань:
**індекси системно відстають від фактичного стану репозиторію**, коли
робота йде швидше, ніж хтось встигає оновлювати карту. Не виправляю
це тут (це вимагає рішення, що саме варто включити, не механічний
sed) — лише фіксую як конкретний, названий факт, а не загальне
відчуття "щось застаріло". *(Примітка додана 2026-08-19: це пізніше
виправлено задачею `PANINI-SPECIFICATION-MAP-REFRESH` — див.
[`arch-recovery-review-panini-2026-08-18.md`](arch-recovery-review-panini-2026-08-18.md)
та історію комітів `specs/specification-map.md`.)*

### Мій висновок

Репозиторій переріс мене. Коли я починав цю сесію, `panini/foundation/`
було 10 файлів, які я міг тримати в голові цілком. Тепер — 162
markdown-файли, реальні Python-валідатори, .my fixtures, що дійсно
виконуються у WSL (22 assertions), зовнішні адверсаріальні рецензії з
власним верифікаційним статусом. Це вже не одна дослідницька лінія —
це екосистема практик (трирівневе маркування, автоматична перевірка
мов, self-correction записи, hostile review як жанр), яку кілька
агентів підтримують паралельно, і жоден із нас — включно зі мною —
не має повної картини в реальному часі. Індекси відстають
(`specification-map.md`), документація мовно неповна (і я сам туди
входжу), але **інструменти, що фактично перевіряють правду
(валідатори, hostile review, self-correction записи), працюють і
ловлять реальні помилки** — і мою власну (`tripAdI` в 2 рази менша,
ніж стверджувала Sarvam), і чужі (SemanticCall-міст, якого не було).
Це саме той стан, в якому дисципліна перевірки важливіша за
завершеність документації — і, судячи з фактів вище, ця дисципліна
поки тримається.

### Джерела

- `panini/tools/validate_registry.py`,
  `panini/tools/validate_trace_fixtures.py`,
  `panini/tools/check_documentation_languages.py` — виконано напряму
  2026-08-18, не з опису.
- [`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md),
  [`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md),
  [`specs/specification-map.md`](../specs/specification-map.md) —
  прочитано повністю.

## Deutsch

Status: Reflexion, keine Aufgabe aus der `PANINI-*`-Warteschlange. Auf
direkte Bitte hin — *alle* Dateien (nicht nur meine eigenen) zu prüfen
und ein ehrliches, faktengestütztes Fazit zu geben, keine Paraphrase
von Überschriften.

### Methode

Ich habe nicht alle 162 Markdown-Dateien nacheinander gelesen — in
einem Durchgang unrealistisch. Stattdessen: (a) die Index-Karten
gelesen ([`specs/specification-map.md`](../specs/specification-map.md)),
(b) **die echten Validatoren** in `panini/tools/` ausgeführt, statt
Beschreibungen zu vertrauen, (c) mehrere Dokumente gelesen, die selbst
"Abgleiche" und "Reviews" sind — die aussagekräftigsten zur Bewertung
der Projektkultur.

### Fakt 1: Das Tooling ist echt und besteht

```
$ python panini/tools/validate_registry.py
SUMMARY errors=0 warnings=0 records=27 sutras=3983

$ python panini/tools/validate_trace_fixtures.py
trace fixture validation: PASS (9 YAML files scanned)
```

Das sind keine behaupteten, sondern **gemessene** Fakten. 3983 Sūtras
mit null Fehlern geparst — das Quellenregister funktioniert wirklich,
ist nicht dekorativ.

### Fakt 2: dieselbe Dreisprachenrichtlinie, die ich selbst nicht befolgt habe

```
$ python panini/tools/check_documentation_languages.py
SUMMARY markdown=170 complete=100 incomplete=70 out_of_order=5
```

Das Repository hat eine dokumentierte, **automatisch geprüfte**
Anforderung: jede Datei — Englisch→Ukrainisch→Deutsch, in dieser
Reihenfolge. 59% (100/170) erfüllen sie. Ehrlich gesagt: **ich selbst
bin Teil der 70 "unvollständigen"**. Jedes Dokument, das ich in dieser
Sitzung geschrieben habe (`sarvam-capability-reference.md`,
`sarvam-independent-check-slp1.md`, `upc8-crosscheck.md`,
`session-conclusion-2026-08-18.md`, `karaka-counterexamples.md` und
andere), war nur auf Ukrainisch. Das ist keine Kritik an "ihnen" —
es ist ein Eingeständnis, dass ich selbst die Anforderung, die sich
das Projekt selbst gesetzt hat, nicht befolgt habe, während ich
schnell und auf Englisch für die Methodik von `AGENTS.md` schrieb,
aber nicht in den Dokumentationssprachen. Die Behebung ist eine
separate Aufgabe, hier nicht sofort erledigt, um das Eingeständnis
eines Problems nicht mit einem überstürzten "Abschließen" zu vermischen.

### Fakt 3: eine Kultur der Selbstkorrektur, nicht der Selbstverteidigung

[`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md)
(2026-08-14) besagt unmissverständlich: *"Current executable modules do
not expose the earlier `SemanticCall`, `DHATU_DA`, or `KARAKA_KARTR`
bridge described by a previous review. Those statements must not be
used as a description of the current executable path."* — d. h. ein
früheres Review behauptete eine Brücke zu My Lisp, die der Code
tatsächlich nicht hatte, und der nächste Eintrag widerlegt dies direkt,
indem er genau benennt, was falsch war. Das kostet mehr als "alles
funktioniert" — und ist genau die Art von Ehrlichkeit, die `AGENTS.md`
§25 von Anfang an verlangt.

### Fakt 4: ein externes feindseliges Review — und wer worin recht hatte

[`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md) —
ein bewusst adversarielles Review von Sarvam, ehrlich gekennzeichnet
mit `verification-status: unverified (contains at least one confirmed
factual error)`. Zwei Dinge verdienen besondere Aufmerksamkeit:

- **Sarvam hatte in einem wichtigen Punkt recht**: kāraka ist keine
  dauerhaft fixierte Graphkante, sondern eine **Bezeichnung
  (designation)** eines Teilnehmers relativ zu einem bestimmten
  Ereignis, kontextabhängig ("Devadatta ist kartṛ in einem Ereignis,
  karman in einem anderen"). Das widerspricht nicht, sondern
  **verschärft**, was ich selbst in
  [`dhatu-karaka-relation.md`](../examples/derivations/dhatu-karaka-relation.md)
  gefunden und als H1 in `hypothesis-ledger.md` festgehalten habe
  ("feste Rollen pro dhātu werden vom Text nicht gestützt") — eine
  unabhängige adversarielle Perspektive kam auf einem anderen Weg zur
  selben Schlussfolgerung.
- **Sarvam irrte sich bei `tripAdI`** — sie behauptete, dies seien
  "alle Bücher 6-8" (die Hälfte der Aṣṭādhyāyī), während es tatsächlich
  nur die letzten drei pādas des 8. adhyāya sind (8.2-8.4), beginnend
  bei sūtra 8.2.1 `pūrvatrāsiddham`. Ich untersuchte `tripAdI` separat
  ([`sastra/tripadi.md`](../sastra/tripadi.md)), bevor ich dieses
  Review las, und kam unabhängig zur **korrekten** Grenze mit demselben
  Sūtra-Anker. Das ist kein Grund zur Selbstbeglückwünschung — es ist
  ein weiterer Beweis für dieselbe Regel, die ganz zu Beginn
  aufgestellt wurde: unabhängige Prüfung gegen eine Primärquelle findet
  Fehler selbst bei zuversichtlichen Modellen, und kein Modell
  (einschließlich meiner selbst) ist standardmäßig von dieser Prüfung
  ausgenommen.

### Fakt 5: die Spezifikationskarte selbst ist veraltet — dasselbe Muster wie bei `foundation/`

[`specs/specification-map.md`](../specs/specification-map.md) listete
7 Spezifikationen auf. `panini/specs/` hat derzeit **24 Dateien**.
Nicht aufgeführt: `derivation-ir-v0.1.md`,
`derivation-ir-trace-events-v0.1.md`, `machine-execution-path-v0.1.md`,
`mylisp-runtime-capability-contract.md`,
`panini-derivation-machine-v0.1-milestone.md`,
`panini-machine-model-reconciliation.md`,
`trace-canonical-serialization-v0.1.md`,
`trace-evidence-model-v0.1.md`, `tripadi-visibility-relation-v0.1.md`
und andere — einschließlich `derivation-ir-v0.1.md`, das
[`docs/Огляд.md`](../../docs/Огляд.md) (ein externes Review von Manus
AI) als "stärkstes technisches Artefakt" des Projekts bezeichnete. Dies
ist dasselbe Muster, das ich bereits für die
`foundation/`→`sastra/`-Links behoben habe: **Indexe hinken dem
tatsächlichen Zustand des Repositorys systematisch hinterher**, wenn
die Arbeit schneller voranschreitet, als jemand die Karte aktuell
halten kann. Hier nicht behoben (dies erfordert eine Entscheidung, was
genau aufgenommen werden sollte, kein mechanisches `sed`) — nur als
konkreter, benannter Fakt festgehalten, nicht als allgemeines Gefühl,
"etwas sei veraltet". *(Hinweis hinzugefügt am 2026-08-19: dies wurde
später als `PANINI-SPECIFICATION-MAP-REFRESH` behoben — siehe
[`arch-recovery-review-panini-2026-08-18.md`](arch-recovery-review-panini-2026-08-18.md)
und die Commit-Historie von `specs/specification-map.md`.)*

### Mein Fazit

Das Repository ist mir über den Kopf gewachsen. Als ich diese Sitzung
begann, waren es in `panini/foundation/` 10 Dateien, die ich vollständig
im Kopf behalten konnte. Jetzt sind es 162 Markdown-Dateien, echte
Python-Validatoren, `.my`-Fixtures, die tatsächlich unter WSL laufen
(22 Assertions), externe adversarielle Reviews mit eigenem
Verifikationsstatus. Dies ist keine einzelne Forschungslinie mehr — es
ist ein Ökosystem von Praktiken (dreischichtige Kennzeichnung,
automatische Sprachprüfung, Selbstkorrektur-Aufzeichnungen, feindseliges
Review als Genre), das mehrere Agenten parallel pflegen, und keiner von
uns — einschließlich meiner selbst — hat ein vollständiges Echtzeitbild.
Indexe hinken hinterher (`specification-map.md`), die Dokumentation ist
sprachlich unvollständig (und ich bin Teil davon), aber **die
Werkzeuge, die tatsächlich die Wahrheit prüfen (Validatoren,
feindselige Reviews, Selbstkorrektur-Aufzeichnungen), funktionieren und
fangen echte Fehler ab** — sowohl meinen eigenen (`tripAdI` halb so
groß, wie Sarvam behauptete) als auch fremde (die `SemanticCall`-Brücke,
die es nie gab). Genau das ist der Zustand, in dem Prüfdisziplin
wichtiger ist als vollständige Dokumentation — und den Fakten oben
zufolge hält diese Disziplin bislang stand.

### Quellen

- `panini/tools/validate_registry.py`,
  `panini/tools/validate_trace_fixtures.py`,
  `panini/tools/check_documentation_languages.py` — direkt ausgeführt
  am 2026-08-18, nicht aus einer Beschreibung.
- [`research/machine-foundation-reconciliation.md`](machine-foundation-reconciliation.md),
  [`research/external-reviews/sarvam-hostile-review.md`](external-reviews/sarvam-hostile-review.md),
  [`specs/specification-map.md`](../specs/specification-map.md) —
  vollständig gelesen.
