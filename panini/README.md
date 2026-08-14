# panini

[English](#english) · [Українська](#українська) · [Deutsch](#deutsch)

## English

Research foundation for Pāṇini's grammar, intended for possible future use in My Lisp. The project reconstructs the grammar before proposing a machine model. Its governing methodology is [AGENTS.md](../AGENTS.md).

`panini-foundation-v0.1` is the current milestone. It contains evidence-aware foundation notes, machine-readable registries, research audits, derivation examples, specifications, and read-only validation tools.

## Українська

Дослідницький фундамент граматики Паніні для можливого майбутнього використання в My Lisp. Проєкт реконструює граматику перед тим, як пропонувати machine model. Його головна методологія міститься в [AGENTS.md](../AGENTS.md).

Поточний milestone — `panini-foundation-v0.1`. Він містить foundation notes з урахуванням доказів, машинно-читані registry, research audits, приклади деривації, специфікації та read-only інструменти перевірки.

## Deutsch

Forschungsgrundlage für Pāṇinis Grammatik zur möglichen späteren Verwendung in My Lisp. Das Projekt rekonstruiert die Grammatik, bevor es ein Maschinenmodell vorschlägt. Die maßgebliche Methodik steht in [AGENTS.md](../AGENTS.md).

Der aktuelle Meilenstein ist `panini-foundation-v0.1`. Er enthält evidenzbewusste Foundation-Notizen, maschinenlesbare Register, Forschungsaudits, Ableitungsbeispiele, Spezifikationen und schreibgeschützte Validierungswerkzeuge.

## Structure · Структура · Struktur

The project follows a strict 4-layer architecture (plus supporting folders) to separate traditional grammar from computational interpretations:

- `sastra/` — traditional Paninian definitions, evidence-bounded, zero CS-analogies · традиційні визначення Паніні без CS-аналогій · traditionelle Definitionen ohne CS-Analogien;
- `hypotheses/` — machine models mapping Paninian concepts to computational structures (e.g., Lisp AST, inference rules) · машинні моделі та переходи до CS · Maschinenmodelle;
- `formal/` — intermediate formal models and IR (Intermediate Representation) · формальні моделі · formale Modelle;
- `implementation/` — actual execution in My Lisp / VM / FPGA · реалізація в My Lisp · Ausführung in My Lisp;
- `registry/` — machine-readable records (dhātu, sūtras) · машинно-читані записи · maschinenlesbare Einträge;
- `research/` — source audits and external library analysis · аудити джерел (Vidyut, AI4Bharat) · Quellenaudits;
- `examples/derivations/` — traced examples · простежені приклади · nachvollzogene Beispiele;
- `specs/` — project boundaries · межі проєкту · Projektgrenzen.

For WSL2, Guix, and swarm-node coordination, see [swarm-agent-guide.md](swarm-agent-guide.md) · Інструкція для WSL2, Guix і координації swarm-node — у [swarm-agent-guide.md](swarm-agent-guide.md) · Anleitung für WSL2, Guix und die Koordination mit swarm-node: [swarm-agent-guide.md](swarm-agent-guide.md).

See [documentation-languages.md](documentation-languages.md) for the translation policy · Правила перекладу — у [documentation-languages.md](documentation-languages.md) · Die Übersetzungsregeln stehen in [documentation-languages.md](documentation-languages.md).
