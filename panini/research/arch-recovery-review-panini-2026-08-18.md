# ARCH-RECOVERY-REVIEW-PANINI: audit of AGENTS.md against the actual repository state (2026-08-18)

## English

Status: done (`ARCH-RECOVERY-REVIEW-PANINI`, swarm task).

### Method

The same pattern already applied in `juv4uk/cml` (found via
`gh api "search/commits?q=org:juv4uk+ARCH-RECOVERY"`): check the text of
`AGENTS.md` not against memory or assumption, but against the actual
state of the filesystem and repository, using:

```bash
grep -n 'swarm-node\|9106\|--connect' AGENTS.md   # 0 matches
ls panini/coordination      # not found
ls panini/formal            # not found
find . -maxdepth 2 -iname "ecosystem"   # found, populated
find . -maxdepth 1 -iname "repo.my" -o -iname "tasks.my"   # both exist
```

### 3 discrepancies found — all fixed

1. **Missing session-start section.** `AGENTS.md` contained no mention
   at all of `swarm-node`, port 9106, or the `--connect` procedure — a
   new agent had no way to learn how to join the swarm. Added §0
   "Session start — joining the swarm" with the real launch command and
   notes that the journal survives a process restart while the process
   itself does not (verified in practice during this session's WSL
   crashes).

2. **Non-existent canonical registry.** §21b claimed that
   `panini/coordination/dependencies.yaml` was the canonical registry
   of all cross-repo imports. The `panini/coordination/` directory does
   not exist (verified with `ls`). Fixed: the section now describes the
   actual practice (inline provenance blocks in the documents that
   consume a claim, e.g. `sastra/pratyahara.md`) and states plainly
   that no centralized registry exists, rather than silently swapping
   one false claim for another.

3. **Stale directory tree.** §22 showed `sastra/ (or foundation/)` — a
   hedge that had lost its meaning after the full rename
   `foundation/`→`sastra/` (fixed earlier this session across 26 files),
   and `formal/`, which never existed as a separate directory (formal
   IR specifications actually live in `specs/`). The tree was replaced
   with one reflecting the real list of top-level directories
   (`sastra/`, `specs/`, `hypotheses/`, `machine/`, `implementation/`,
   `registry/`, `examples/derivations/`, `tests/`, `tools/`,
   `research/`), with an explicit note that this is the state as of
   2026-08-18, not the project's original sketch.

### Confirmed correct (left untouched)

- `agent-cheatsheet.my`, `repo.my`, `tasks.my` — all exist, as
  `AGENTS.md` §27-28 claims.
- `ecosystem/` — exists; the subfolders `claims, handoffs, impacts,
  imports, questions, tasks` match the description "lingua franca of
  the ecosystem".

### Why only these three, not more

The audit is deliberately limited to verifiable, concrete claims ("file
X exists", "command Y is documented") — claims that a single command
can falsify. General stylistic or methodological sections of
`AGENTS.md` (§1-20, §23-28) were not reviewed for "staleness" absent a
concrete verification criterion — this keeps the review from turning
into a subjective rewrite of someone else's text without evidence.

### Sources

- `juv4uk/cml` — the precedent for this class of task
  (`ARCH-RECOVERY-REVIEW-CML`), found via `gh api search/commits`.
- Direct bash filesystem checks, listed above.

## Українська

Статус: завершено (`ARCH-RECOVERY-REVIEW-PANINI`, swarm task).

### Метод

Той самий патерн, що вже застосований у `juv4uk/cml` (знайдено через
`gh api "search/commits?q=org:juv4uk+ARCH-RECOVERY"`): звірити текст
`AGENTS.md` не з пам'яттю чи припущенням, а з реальним станом
файлової системи й репозиторію, командами:

```bash
grep -n 'swarm-node\|9106\|--connect' AGENTS.md   # 0 matches
ls panini/coordination      # not found
ls panini/formal            # not found
find . -maxdepth 2 -iname "ecosystem"   # found, populated
find . -maxdepth 1 -iname "repo.my" -o -iname "tasks.my"   # both exist
```

### Знайдено 3 розбіжності — усі виправлено

1. **Відсутня секція старту сесії.** `AGENTS.md` не містив жодної
   згадки про `swarm-node`, порт 9106 чи процедуру `--connect` —
   новий агент не мав звідки дізнатись, як приєднатись до рою. Додано
   §0 "Session start — приєднання до рою" з реальною командою запуску
   й нотатками про те, що журнал переживає рестарт процесу, а сам
   процес — ні (перевірено на практиці під час падінь WSL цієї сесії).

2. **Неіснуючий канонічний реєстр.** §21b стверджував, що
   `panini/coordination/dependencies.yaml` — канонічний реєстр усіх
   cross-repo імпортів. Директорія `panini/coordination/` не існує
   (перевірено `ls`). Виправлено: секція тепер описує фактичну
   практику (inline-блоки походження в документах, що споживають
   claim, напр. `sastra/pratyahara.md`) і прямо називає відсутність
   централізованого реєстру, а не мовчки замінює одне неправдиве
   твердження іншим.

3. **Застаріле дерево директорій.** §22 показувало `sastra/ (або
   foundation/)` — гейдж, що втратив сенс після повного перейменування
   `foundation/`→`sastra/` (виправлено раніше цієї сесії в 26 файлах),
   і `formal/`, якої ніколи не існувало як окремої директорії
   (формальні IR-специфікації фактично живуть у `specs/`). Дерево
   замінено на таке, що відображає реальний список top-level
   директорій (`sastra/`, `specs/`, `hypotheses/`, `machine/`,
   `implementation/`, `registry/`, `examples/derivations/`, `tests/`,
   `tools/`, `research/`), з явною приміткою, що це стан на
   2026-08-18, не оригінальний ескіз проєкту.

### Підтверджено коректним (не чіпав)

- `agent-cheatsheet.my`, `repo.my`, `tasks.my` — усі існують, як і
  стверджує `AGENTS.md` §27-28.
- `ecosystem/` — існує, підпапки `claims, handoffs, impacts, imports,
  questions, tasks` відповідають опису "lingua franca екосистеми".

### Чому саме ці три, а не більше

Аудит навмисно обмежений перевірними, конкретними твердженнями
(«файл X існує», «команда Y описана») — тобто твердженнями, які
можна фальсифікувати однією командою. Загальні стилістичні чи
методологічні секції `AGENTS.md` (§1-20, §23-28) не переглядались на
предмет "застарілості" за відсутності конкретного критерію
перевірки — це запобігає перетворенню рев'ю на суб'єктивну редакцію
чужого тексту без evidence.

### Джерела

- `juv4uk/cml` — прецедент того самого класу задачі (`ARCH-RECOVERY-REVIEW-CML`), знайдений через `gh api search/commits`.
- Прямі bash-перевірки файлової системи, зазначені вище.

## Deutsch

Status: abgeschlossen (`ARCH-RECOVERY-REVIEW-PANINI`, Schwarm-Aufgabe).

### Methode

Dasselbe Muster, das bereits in `juv4uk/cml` angewandt wurde (gefunden
über `gh api "search/commits?q=org:juv4uk+ARCH-RECOVERY"`): den Text von
`AGENTS.md` nicht gegen Erinnerung oder Annahme, sondern gegen den
tatsächlichen Zustand des Dateisystems und Repositorys zu prüfen,
mittels:

```bash
grep -n 'swarm-node\|9106\|--connect' AGENTS.md   # 0 Treffer
ls panini/coordination      # nicht gefunden
ls panini/formal            # nicht gefunden
find . -maxdepth 2 -iname "ecosystem"   # gefunden, gefüllt
find . -maxdepth 1 -iname "repo.my" -o -iname "tasks.my"   # beide existieren
```

### 3 gefundene Abweichungen — alle behoben

1. **Fehlender Abschnitt zum Sitzungsstart.** `AGENTS.md` enthielt
   keinerlei Erwähnung von `swarm-node`, Port 9106 oder dem
   `--connect`-Verfahren — ein neuer Agent hatte keine Möglichkeit zu
   erfahren, wie er dem Schwarm beitritt. §0 "Session start —
   Beitritt zum Schwarm" wurde mit dem tatsächlichen Startbefehl
   ergänzt, samt Hinweis, dass das Journal einen Prozessneustart
   übersteht, der Prozess selbst jedoch nicht (in der Praxis während
   der WSL-Abstürze dieser Sitzung verifiziert).

2. **Nicht existierendes kanonisches Register.** §21b behauptete,
   `panini/coordination/dependencies.yaml` sei das kanonische Register
   aller repoübergreifenden Importe. Das Verzeichnis
   `panini/coordination/` existiert nicht (mit `ls` verifiziert).
   Behoben: Der Abschnitt beschreibt nun die tatsächliche Praxis
   (Inline-Herkunftsblöcke in den Dokumenten, die einen Claim
   konsumieren, z. B. `sastra/pratyahara.md`) und benennt das Fehlen
   eines zentralen Registers explizit, statt eine falsche Behauptung
   stillschweigend durch eine andere zu ersetzen.

3. **Veralteter Verzeichnisbaum.** §22 zeigte `sastra/ (oder
   foundation/)` — eine Absicherung, die nach der vollständigen
   Umbenennung `foundation/`→`sastra/` (früher in dieser Sitzung in 26
   Dateien behoben) ihren Sinn verloren hatte, sowie `formal/`, das nie
   als eigenes Verzeichnis existierte (formale IR-Spezifikationen
   liegen tatsächlich in `specs/`). Der Baum wurde durch einen ersetzt,
   der die reale Liste der Top-Level-Verzeichnisse widerspiegelt
   (`sastra/`, `specs/`, `hypotheses/`, `machine/`, `implementation/`,
   `registry/`, `examples/derivations/`, `tests/`, `tools/`,
   `research/`), mit einem expliziten Hinweis, dass dies der Stand vom
   2026-08-18 ist, nicht die ursprüngliche Skizze des Projekts.

### Als korrekt bestätigt (unverändert gelassen)

- `agent-cheatsheet.my`, `repo.my`, `tasks.my` — existieren alle, wie
  `AGENTS.md` §27-28 behauptet.
- `ecosystem/` — existiert; die Unterordner `claims, handoffs, impacts,
  imports, questions, tasks` entsprechen der Beschreibung "lingua
  franca des Ökosystems".

### Warum genau diese drei, nicht mehr

Das Audit ist bewusst auf überprüfbare, konkrete Behauptungen
beschränkt ("Datei X existiert", "Befehl Y ist dokumentiert") — also
Behauptungen, die ein einzelner Befehl falsifizieren kann. Allgemeine
stilistische oder methodische Abschnitte von `AGENTS.md` (§1-20,
§23-28) wurden mangels eines konkreten Prüfkriteriums nicht auf
"Veraltung" geprüft — das verhindert, dass das Review zu einer
subjektiven Überarbeitung fremden Texts ohne Evidenz wird.

### Quellen

- `juv4uk/cml` — Präzedenzfall derselben Aufgabenklasse
  (`ARCH-RECOVERY-REVIEW-CML`), gefunden über `gh api search/commits`.
- Direkte Bash-Prüfungen des Dateisystems, oben aufgeführt.
