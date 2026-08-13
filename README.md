# my-lisp-panini

**A formal foundation before a hypothesis · Формальний фундамент перед гіпотезою · Ein formales Fundament vor einer Hypothese**

[English](#english) · [Українська](#українська) · [Deutsch](#deutsch)

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

## Українська

`my-lisp-panini` досліджує граматику Паніні (*Aṣṭādhyāyī*) як самостійну
формальну систему, а не як вправу з перекладу Lisp санскритом. Спершу
встановлюємо, якою є система Паніні; лише потім перевіряємо, які
обчислювальні конструкції можуть із неї випливати. Відповідності
`cons`/`car`/`cdr`/`lambda` до санскритських термінів ніколи не припускаються
наперед.

Повний мандат і методологія — в [AGENTS.md](AGENTS.md). Внутрішні
ідентифікатори використовують ASCII SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST і
деванаґарі є лише presentation forms. Кожен дослідницький документ розділяє
`[PANINI]`, `[INTERPRETATION]` і `[MY-LISP HYPOTHESIS]`.

Перший milestone, `panini-foundation-v0.1`, містить онтологію, джерела й
доказово простежені приклади — без parser-а, повної NLP-системи чи змін My
Lisp. `panini-machine-model-v0.1` починається лише після стабілізації цього
фундаменту.

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

## Repository structure · Структура репозиторію · Repository-Struktur

- [panini/foundation/](panini/foundation) — ontology and terminology ·
  онтологія й термінологія · Ontologie und Terminologie;
- [panini/registry/](panini/registry) — machine-readable records ·
  машинно-читані записи · maschinenlesbare Einträge;
- [panini/research/](panini/research) — source and hypothesis audits ·
  аудити джерел і гіпотез · Quellen- und Hypothesenaudits;
- [panini/examples/derivations/](panini/examples/derivations) — traced examples ·
  простежені приклади · nachvollzogene Beispiele;
- [panini/specs/](panini/specs) — specifications · специфікації · Spezifikationen.

## Documentation languages · Мови документації · Dokumentationssprachen

Human-facing project documentation is maintained in English, Ukrainian, and
German. Code, SLP1, sūtra text, machine-readable data, quotations, URLs, and
vendored third-party material are not translated. See
[panini/documentation-languages.md](panini/documentation-languages.md).

## License · Ліцензія · Lizenz

[MIT](LICENSE)
