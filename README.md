# my-lisp-panini

**A formal foundation before a hypothesis · Формальний фундамент перед гіпотезою · Ein formales Fundament vor einer Hypothese**

[English](#english) · [Українська](#українська) · [Deutsch](#deutsch)

## English

`my-lisp-panini` studies Pāṇini's grammar (*Aṣṭādhyāyī*) as a formal system
in its own right, not as an exercise in translating Lisp into Sanskrit. We
first establish what Pāṇini's system is; only then do we test which
computational constructions might follow from it. No correspondence from
`cons`/`car`/`cdr`/`lambda` to Sanskrit terminology is assumed in advance.

Our ultimate goal is to build an **executable epistemology of Pāṇini**, where the system works with `(symbol value proof)` through **Proof-Carrying Derivations**. 

## Cross-Repo Epistemic Architecture

This repository is part of a larger epistemic chain. We consume facts from upstream repositories and build computational hypotheses upon them.

```text
[shiva-sutras]
(Upstream Authority: Canon, pratyāhāra, markers, mathematics, epistemic tests)
       │
       ▼ (qualified claims)
       │
[my-lisp-panini]
(Downstream/Upstream: Pāṇinian ontology, saṃjñā, dhātu, derivations)
       │
       ▼ (computational hypotheses)
       │
[My Lisp]
(Downstream: Symbolic semantics, inference, proof-carrying IR, VM)
```

The full mandate and methodology are in [AGENTS.md](AGENTS.md). Internal
identifiers use ASCII SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST and Devanāgarī
are presentation forms only. Every formalized entity must strictly separate 4 layers of provenance: `[PANINI]`, `[SCHOLARLY INTERPRETATION]`, `[COMPUTATIONAL INTERPRETATION]`, and `[MY-LISP HYPOTHESIS]`.

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

Наша мета — побудувати **executable epistemology Паніні**, де система працює зі `(symbol value proof)` через **Proof-Carrying Derivations**.

Повний мандат і методологія — в [AGENTS.md](AGENTS.md). Внутрішні
ідентифікатори використовують ASCII SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST і
деванаґарі є лише presentation forms. Кожна формалізована сутність повинна строго розділяти 4 шари походження: `[PANINI]`, `[SCHOLARLY INTERPRETATION]`, `[COMPUTATIONAL INTERPRETATION]` і `[MY-LISP HYPOTHESIS]`.

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

Unser Ziel ist der Aufbau einer **executable epistemology von Pāṇini**, wobei das System mit `(symbol value proof)` durch **Proof-Carrying Derivations** arbeitet.

Das vollständige Mandat und die Methodik stehen in [AGENTS.md](AGENTS.md).
Interne Bezeichner verwenden ASCII-SLP1 (`kartf`, `karaRa`, `dhAtu`); IAST und
Devanāgarī dienen nur der Darstellung. Jede formalisierte Entität muss 4 Herkunftsschichten strikt trennen: `[PANINI]`, `[SCHOLARLY INTERPRETATION]`, `[COMPUTATIONAL INTERPRETATION]` und `[MY-LISP HYPOTHESIS]`.

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

Agents connect through WSL2 and use the declared Guix environment for project
commands; the exact swarm procedure is in
[panini/swarm-agent-guide.md](panini/swarm-agent-guide.md) · Агенти
підключаються через WSL2 і використовують задеклароване Guix-оточення для
команд проєкту; точна процедура рою — у
[panini/swarm-agent-guide.md](panini/swarm-agent-guide.md) · Agenten verbinden
sich über WSL2 und verwenden die deklarierte Guix-Umgebung für
Projektbefehle; das genaue Schwarmverfahren steht in
[panini/swarm-agent-guide.md](panini/swarm-agent-guide.md).

## Documentation languages · Мови документації · Dokumentationssprachen

Human-facing project documentation is maintained in English, Ukrainian, and
German. Code, SLP1, sūtra text, machine-readable data, quotations, URLs, and
vendored third-party material are not translated. See
[panini/documentation-languages.md](panini/documentation-languages.md).

## License · Ліцензія · Lizenz

[MIT](LICENSE)
