# my-lisp-panini

**A formal foundation, before a hypothesis · Формальний фундамент, перш ніж гіпотеза · Ein formales Fundament, bevor eine Hypothese**

[English](#english) · [Українська](#українська) · [Deutsch](#deutsch)

## English

`my-lisp-panini` researches Pāṇini's grammar (*Aṣṭādhyāyī*) as a formal
system in its own right — **not** a translation exercise. The governing
rule, spelled out in full in [`AGENTS.md`](AGENTS.md): reconstruct what
Pāṇini's system actually is first, and only then ask what computational
constructs, if any, follow from it naturally. `cons`/`car`/`cdr`/`lambda`
are never assumed to correspond to some *dhātu* in advance — that would
have to be a research result, not a starting condition.

This repository is a sibling of [`my-lisp`](https://github.com/juv4uk/my-lisp)
in the same ecosystem (`my-lisp`, `cml`, `fpga-lisp`, `my-idea`), coordinating
over the same [swarm mesh](https://github.com/juv4uk/my-lisp/blob/master/docs/swarm-mesh-v2.md)
under node id `my-lisp-panini-1`. It produces the future `panini-foundation`
that `my-lisp`'s own Sanskrit-semantics work (`SANSKRIT-P*` tasks) can draw
on — but does not itself touch `my-lisp` until the foundation work is done.

### Canonical representation

Internal text representation is **SLP1** (ASCII, unambiguous, Git-friendly,
FPGA-friendly) — e.g. `kartf`, `karaRa`, `dhAtu`. IAST (`kartṛ`, `karaṇa`,
`dhātu`) is for documentation and human explanation; Devanāgarī is an
optional presentation layer. Neither IAST nor Devanāgarī is ever used as an
internal identifier.

### Three levels, kept strictly separate

Every research document tags its claims:

- `[PANINI]` — what the grammar's own sūtra text actually establishes.
- `[INTERPRETATION]` — how modern scholarship / implementations read it.
- `[MY-LISP HYPOTHESIS]` — how this might (or might not) inform My Lisp.

Writing `it = compiler metadata` as a flat statement is disallowed; the same
claim has to be split across the three sections above. See
[`AGENTS.md`](AGENTS.md) §21 for the full rationale.

### Structure

- [`AGENTS.md`](AGENTS.md) — the full research mandate and methodology; the
  source of truth for any agent or contributor working in this repo.
- [`panini/foundation/`](panini/foundation) — ontology and terminology of
  Pāṇini's system: [`ontology.md`](panini/foundation/ontology.md) (the
  five-level metalanguage map), [`dhatu.md`](panini/foundation/dhatu.md),
  [`karaka.md`](panini/foundation/karaka.md), plus `samjna.md`, `pratyaya.md`,
  `it.md`, `pratyahara.md`, `anuvrtti.md`, `rule-system.md`, `terminology.md`
  as they're researched.
- [`panini/registry/`](panini/registry) — machine-readable YAML records:
  [`dhatu/`](panini/registry/dhatu) (20 verb roots), [`karaka/`](panini/registry/karaka)
  (the six semantic-role categories), `samjna/`, `rules/` as they fill in.
- [`panini/research/`](panini/research) — audits of external prior art
  (Vidyut, Sanskrit Heritage, panini-nlp) as they're written, each split into
  what it models / how / what maps to Pāṇini directly / what's implementation
  machinery / what to reuse / what not to.
- [`panini/examples/derivations/`](panini/examples/derivations) — fully
  traced worked examples, e.g.
  [`dhatu-karaka-relation.md`](panini/examples/derivations/dhatu-karaka-relation.md).
- [`panini/specs/panini-foundation-v0.1.md`](panini/specs/panini-foundation-v0.1.md)
  — the first milestone's spec: base entity classes, object-language vs.
  metalanguage, what a rule/context/derivation is, canonical SLP1 identifiers.

### Milestones

Not "implement Pāṇini." Two deliberately small, sequential milestones (full
detail in `AGENTS.md` §23–24):

1. **`panini-foundation-v0.1`** — the ontology and a handful of fully-traced
   examples. No parser, no NLP system, no My Lisp changes.
2. **`panini-machine-model-v0.1`** — only after v0.1 stabilizes: symbol IDs
   for Paninian entities, rules as machine rules, derivation as state
   transition. This is the only point where a bridge to My Lisp, symbolic
   AI, the VM, or FPGA is allowed to begin.

### Coordination

Runs its own `swarm-node` (port `9106`, `--project my-lisp-panini`) alongside
the ecosystem's other four nodes, gossip-connected via `127.0.0.1:9101`.
Reproducible shell: `guix shell -m manifest.scm --`. See
[`docs/swarm-mesh-v2.md`](https://github.com/juv4uk/my-lisp/blob/master/docs/swarm-mesh-v2.md)
in `my-lisp` for the protocol this repo speaks.

## Українська

`my-lisp-panini` досліджує граматику Пāніні (*Aṣṭādhyāyī*) як формальну
систему саму по собі — **не** як вправу з перекладу. Головне правило,
детально викладене в [`AGENTS.md`](AGENTS.md): спершу реконструювати, чим
насправді є система Паніні, і лише потім питати, які обчислювальні
конструкції з неї природно випливають, якщо взагалі випливають.
`cons`/`car`/`cdr`/`lambda` ніколи не вважаються наперед відповідниками
якогось *dhātu* — це має бути результатом дослідження, а не вихідною умовою.

Цей репозиторій — сусід [`my-lisp`](https://github.com/juv4uk/my-lisp) у тій
самій екосистемі (`my-lisp`, `cml`, `fpga-lisp`, `my-idea`), координується
через той самий [swarm mesh](https://github.com/juv4uk/my-lisp/blob/master/docs/swarm-mesh-v2.md)
під ідентифікатором вузла `my-lisp-panini-1`. Він виробляє майбутній
`panini-foundation`, на який зможе спиратись власна робота `my-lisp` над
санскритською семантикою (задачі `SANSKRIT-P*`) — але сам не торкається
`my-lisp`, доки фундаментальна робота не завершена.

### Канонічне представлення

Внутрішнє текстове представлення — **SLP1** (лише ASCII, однозначна
транслітерація, Git-friendly, FPGA-friendly) — напр. `kartf`, `karaRa`,
`dhAtu`. IAST (`kartṛ`, `karaṇa`, `dhātu`) — для документації й пояснень
людині; Devanāgarī — опціональний presentation-шар. Ні IAST, ні Devanāgarī
ніколи не використовуються як внутрішні ідентифікатори.

### Три рівні, суворо розділені

Кожен дослідницький документ позначає свої твердження:

- `[PANINI]` — що фактично встановлює сам текст sūtra.
- `[INTERPRETATION]` — як це читає сучасна наука/реалізації.
- `[MY-LISP HYPOTHESIS]` — як це могло б (чи ні) вплинути на My Lisp.

Писати `it = compiler metadata` як пласке твердження заборонено; те саме
твердження має бути розбите на три секції вище. Повне обґрунтування —
[`AGENTS.md`](AGENTS.md) §21.

### Структура

- [`AGENTS.md`](AGENTS.md) — повний дослідницький мандат і методологія;
  джерело істини для будь-якого агента чи контриб'ютора в цьому репо.
- [`panini/foundation/`](panini/foundation) — онтологія й термінологія
  системи Паніні: [`ontology.md`](panini/foundation/ontology.md) (мапа
  п'яти метарівнів), [`dhatu.md`](panini/foundation/dhatu.md),
  [`karaka.md`](panini/foundation/karaka.md), а також `samjna.md`,
  `pratyaya.md`, `it.md`, `pratyahara.md`, `anuvrtti.md`, `rule-system.md`,
  `terminology.md` — у міру дослідження.
- [`panini/registry/`](panini/registry) — машинно-читані YAML-записи:
  [`dhatu/`](panini/registry/dhatu) (20 дієслівних коренів),
  [`karaka/`](panini/registry/karaka) (шість категорій семантичних ролей),
  `samjna/`, `rules/` — у міру наповнення.
- [`panini/research/`](panini/research) — аудити зовнішніх джерел (Vidyut,
  Sanskrit Heritage, panini-nlp) у міру написання, кожен розділений на what
  it models / how / what maps to Pāṇini directly / what's implementation
  machinery / what to reuse / what not to.
- [`panini/examples/derivations/`](panini/examples/derivations) — повністю
  простежені приклади, напр.
  [`dhatu-karaka-relation.md`](panini/examples/derivations/dhatu-karaka-relation.md).
- [`panini/specs/panini-foundation-v0.1.md`](panini/specs/panini-foundation-v0.1.md)
  — специфікація першого milestone: базові класи сутностей, object language
  vs. metalanguage, що таке rule/context/derivation, канонічні SLP1
  ідентифікатори.

### Milestone'и

Не «реалізувати Паніні». Два свідомо малі, послідовні milestone'и (повний
опис — `AGENTS.md` §23–24):

1. **`panini-foundation-v0.1`** — онтологія й кілька повністю простежених
   прикладів. Без parser, без NLP-системи, без змін My Lisp.
2. **`panini-machine-model-v0.1`** — лише після стабілізації v0.1: symbol ID
   для сутностей Паніні, правила як machine rules, деривація як state
   transition. Лише тут дозволяється починати міст до My Lisp, символьного
   ШІ, VM чи FPGA.

### Координація

Запускає власний `swarm-node` (порт `9106`, `--project my-lisp-panini`) поряд
з чотирма іншими вузлами екосистеми, gossip-з'єднання через
`127.0.0.1:9101`. Відтворюване оточення: `guix shell -m manifest.scm --`.
Протокол — [`docs/swarm-mesh-v2.md`](https://github.com/juv4uk/my-lisp/blob/master/docs/swarm-mesh-v2.md)
у `my-lisp`.

## Deutsch

`my-lisp-panini` erforscht Pāṇinis Grammatik (*Aṣṭādhyāyī*) als eigenständiges
formales System — **keine** Übersetzungsübung. Die leitende Regel, vollständig
in [`AGENTS.md`](AGENTS.md) ausgeführt: zuerst rekonstruieren, was Pāṇinis
System tatsächlich ist, und erst danach fragen, welche Berechnungskonstrukte
sich daraus natürlich ergeben, falls überhaupt. `cons`/`car`/`cdr`/`lambda`
werden nie im Voraus als Entsprechung eines *dhātu* angenommen — das müsste
ein Forschungsergebnis sein, keine Ausgangsbedingung.

Dieses Repository ist ein Geschwister von
[`my-lisp`](https://github.com/juv4uk/my-lisp) im selben Ökosystem (`my-lisp`,
`cml`, `fpga-lisp`, `my-idea`) und koordiniert über dasselbe
[Swarm-Mesh](https://github.com/juv4uk/my-lisp/blob/master/docs/swarm-mesh-v2.md)
unter der Knoten-ID `my-lisp-panini-1`. Es erarbeitet das künftige
`panini-foundation`, auf das `my-lisps` eigene Sanskrit-Semantik-Arbeit
(`SANSKRIT-P*`-Aufgaben) aufbauen kann — berührt `my-lisp` selbst aber erst,
wenn die Grundlagenarbeit abgeschlossen ist.

### Kanonische Darstellung

Interne Textdarstellung ist **SLP1** (nur ASCII, eindeutige Transliteration,
Git-freundlich, FPGA-freundlich) — z. B. `kartf`, `karaRa`, `dhAtu`. IAST
(`kartṛ`, `karaṇa`, `dhātu`) dient Dokumentation und menschlicher Erklärung;
Devanāgarī ist eine optionale Präsentationsschicht. Weder IAST noch
Devanāgarī werden je als interne Bezeichner verwendet.

### Drei Ebenen, strikt getrennt

Jedes Forschungsdokument kennzeichnet seine Aussagen:

- `[PANINI]` — was der Sūtra-Text selbst tatsächlich festlegt.
- `[INTERPRETATION]` — wie moderne Forschung/Implementierungen es lesen.
- `[MY-LISP HYPOTHESIS]` — wie dies My Lisp beeinflussen könnte (oder nicht).

`it = compiler metadata` als flache Aussage zu schreiben ist untersagt;
dieselbe Aussage muss auf die drei obigen Abschnitte verteilt werden. Volle
Begründung: [`AGENTS.md`](AGENTS.md) §21.

### Struktur

- [`AGENTS.md`](AGENTS.md) — das vollständige Forschungsmandat und die
  Methodik; die Quelle der Wahrheit für jeden Agenten oder Mitwirkenden in
  diesem Repo.
- [`panini/foundation/`](panini/foundation) — Ontologie und Terminologie des
  Pāṇini-Systems: [`ontology.md`](panini/foundation/ontology.md) (die
  Fünf-Ebenen-Metasprachenkarte), [`dhatu.md`](panini/foundation/dhatu.md),
  [`karaka.md`](panini/foundation/karaka.md), sowie `samjna.md`,
  `pratyaya.md`, `it.md`, `pratyahara.md`, `anuvrtti.md`, `rule-system.md`,
  `terminology.md`, sobald erforscht.
- [`panini/registry/`](panini/registry) — maschinenlesbare YAML-Einträge:
  [`dhatu/`](panini/registry/dhatu) (20 Verbwurzeln), [`karaka/`](panini/registry/karaka)
  (die sechs semantischen Rollenkategorien), `samjna/`, `rules/`, sobald
  gefüllt.
- [`panini/research/`](panini/research) — Audits externer Vorarbeiten
  (Vidyut, Sanskrit Heritage, panini-nlp), sobald verfasst, jeweils
  aufgeteilt in: was modelliert wird / wie / was direkt auf Pāṇini abbildet /
  was Implementierungsmechanik ist / was wiederverwendbar ist / was nicht.
- [`panini/examples/derivations/`](panini/examples/derivations) — vollständig
  nachvollzogene Beispiele, z. B.
  [`dhatu-karaka-relation.md`](panini/examples/derivations/dhatu-karaka-relation.md).
- [`panini/specs/panini-foundation-v0.1.md`](panini/specs/panini-foundation-v0.1.md)
  — die Spezifikation des ersten Meilensteins: grundlegende Entitätsklassen,
  Objektsprache vs. Metasprache, was eine Regel/ein Kontext/eine Ableitung
  ist, kanonische SLP1-Bezeichner.

### Meilensteine

Nicht "Pāṇini implementieren." Zwei bewusst kleine, sequenzielle Meilensteine
(volle Details in `AGENTS.md` §23–24):

1. **`panini-foundation-v0.1`** — die Ontologie und einige vollständig
   nachvollzogene Beispiele. Kein Parser, kein NLP-System, keine
   My-Lisp-Änderungen.
2. **`panini-machine-model-v0.1`** — erst nach Stabilisierung von v0.1:
   Symbol-IDs für Pāṇini-Entitäten, Regeln als Maschinenregeln, Ableitung
   als Zustandsübergang. Erst hier darf eine Brücke zu My Lisp, symbolischer
   KI, der VM oder FPGA beginnen.

### Koordination

Betreibt einen eigenen `swarm-node` (Port `9106`, `--project my-lisp-panini`)
neben den vier anderen Knoten des Ökosystems, per Gossip verbunden über
`127.0.0.1:9101`. Reproduzierbare Shell: `guix shell -m manifest.scm --`.
Protokoll: [`docs/swarm-mesh-v2.md`](https://github.com/juv4uk/my-lisp/blob/master/docs/swarm-mesh-v2.md)
in `my-lisp`.

## License · Ліцензія · Lizenz

[MIT](LICENSE)
