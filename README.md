# my-lisp-panini

**A formal foundation before a hypothesis · Formalnyy fundament pered hipotezoyu · Ein formales Fundament vor einer Hypothese**

[English](#english) · [Ukrainian (ASCII)](#ukrainian-ascii) · [Deutsch](#deutsch)

## English

`my-lisp-panini` studies Pāṇini's grammar (*Aṣṭādhyāyī*) as a formal system
in its own right, not as an exercise in translating Lisp into Sanskrit. We
first establish what Pāṇini's system is; only then do we test which
computational constructions might follow from it. No correspondence from
`cons`/`car`/`cdr`/`lambda` to Sanskrit terminology is assumed in advance.

The full mandate and methodology are in [AGENTS.md](AGENTS.md). Internal
identifiers use ASCII SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST and Devanāgarī
are presentation forms only. Each research document separates `[PANINI]`,
`[INTERPRETATION]`, and `[MY-LISP HYPOTHESIS]`.

The first milestone, `panini-foundation-v0.1`, contains ontology, sources,
and evidence-bound examples — no parser, complete NLP system, or My Lisp
change. `panini-machine-model-v0.1` begins only after that foundation
stabilizes.

## Ukrainian (ASCII)

`my-lisp-panini` doslidzhuye hramatyku Panini (*Aṣṭādhyāyī*) yak samostiynu
formalnu systemu, a ne yak vpravu z perekladu Lisp sanskrytom. Spershu
vstanovlyuyemo, yakoyu ye systema Panini; lyshe potim pereviryayemo, yaki
obchyslyuvalni konstruktsiyi mozhut iz neyi vyplyvaty. Vidpovidnosti
`cons`/`car`/`cdr`/`lambda` do sanskrytskykh terminiv nikoly ne prypuskayutsya
napered.

Povnyy mandat i metodolohiya — v [AGENTS.md](AGENTS.md). Vnutrishni
identyfikatory vykorystovuyut ASCII SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST i
devanahari ye lyshe presentation forms. Kozhen doslidnytskyy dokument rozdilyaye
`[PANINI]`, `[INTERPRETATION]` i `[MY-LISP HYPOTHESIS]`.

Pershyy milestone, `panini-foundation-v0.1`, mistyt ontolohiyu, dzherela y
dokazovo prostezheni pryklady — bez parser-a, povnoyi NLP-systemy chy zmin My
Lisp. `panini-machine-model-v0.1` pochynayetsya lyshe pislya stabilizatsiyi
tsoho fundamentu.

## Deutsch

`my-lisp-panini` erforscht Pāṇinis Grammatik (*Aṣṭādhyāyī*) als eigenständiges
formales System, nicht als Übung zur Übersetzung von Lisp ins Sanskrit.
Zuerst wird festgestellt, was Pāṇinis System ist; erst danach wird geprüft,
welche Rechenkonstruktionen sich daraus ergeben könnten. Eine Entsprechung
von `cons`/`car`/`cdr`/`lambda` zu Sanskrit-Begriffen wird nie vorab
angenommen.

Das vollständige Mandat und die Methodik stehen in [AGENTS.md](AGENTS.md).
Interne Bezeichner verwenden ASCII-SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST und
Devanāgarī dienen nur der Darstellung. Jedes Forschungsdokument trennt
`[PANINI]`, `[INTERPRETATION]` und `[MY-LISP HYPOTHESIS]`.

Der erste Meilenstein, `panini-foundation-v0.1`, enthält Ontologie, Quellen
und beweisgebundene Beispiele — ohne Parser, vollständiges NLP-System oder
Änderung an My Lisp. `panini-machine-model-v0.1` beginnt erst nach der
Stabilisierung dieses Fundaments.

## Repository structure · Struktura repozytoriyu · Repository-Struktur

- [panini/foundation/](panini/foundation) — ontology and terminology ·
  ontolohiya y terminolohiya · Ontologie und Terminologie;
- [panini/registry/](panini/registry) — machine-readable records ·
  mashynno-chytani zapysy · maschinenlesbare Einträge;
- [panini/research/](panini/research) — source and hypothesis audits ·
  audyty dzherel i hipotez · Quellen- und Hypothesenaudits;
- [panini/examples/derivations/](panini/examples/derivations) — traced examples ·
  prostezheni pryklady · nachvollzogene Beispiele;
- [panini/specs/](panini/specs) — specifications · spetsyfikatsiyi · Spezifikationen.

Agents connect through WSL2 and use the declared Guix environment for project
commands; the exact swarm procedure is in
[panini/swarm-agent-guide.md](panini/swarm-agent-guide.md) · Ahenty
pidklyuchayutsya cherez WSL2 i vykorystovuyut zadeklarovane Guix-otochennya dlya
komand proyektu; tochna protsedura royiu — u
[panini/swarm-agent-guide.md](panini/swarm-agent-guide.md) · Agenten verbinden
sich über WSL2 und verwenden die deklarierte Guix-Umgebung für
Projektbefehle; das genaue Schwarmverfahren steht in
[panini/swarm-agent-guide.md](panini/swarm-agent-guide.md).

## Documentation languages · Movy dokumentatsiyi · Dokumentationssprachen

Human-facing project documentation is maintained in English, Ukrainian, and
German. Code, SLP1, sūtra text, machine-readable data, quotations, URLs, and
vendored third-party material are not translated. See
[panini/documentation-languages.md](panini/documentation-languages.md).

## License · Litsenziya · Lizenz

[MIT](LICENSE)
