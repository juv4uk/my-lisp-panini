# Scope of Tripādī / Область дії Tripādī / Geltungsbereich von Tripādī

Статус: виконано (`PANINI-TRIPADI-SCOPE-INVESTIGATION`)
Автор: my-lisp-panini-1 · 2026-08-13
Related: `meta.my` inference engine architecture

---

## 🇺🇸 English: The Tripādī Mechanism
### [PANINI] Textual Definition
The rule `pUrvatrAsidDam` (8.2.1) splits the Aṣṭādhyāyī into two distinct sections:
1. **Sapādāsaptādhyāyī** (First 7¼ chapters): The core grammar.
2. **Tripādī** (Last 3 sections, 8.2-8.4): The sequential phonological/sandhi rules.

The rule states: "For the preceding rules, [the subsequent rules in Tripādī] are as if non-existent (`asiddha`)." Furthermore, within the Tripādī itself, any later rule is non-existent for an earlier rule.

### [INTERPRETATION] Computational Meaning
- **Sapādāsaptādhyāyī**: Rules can feed and bleed each other recursively until a stable state is reached. It acts as an unordered or priority-resolved rule engine (handled by `antaraṅga`, `apavāda`, etc.).
- **Tripādī**: Rules are applied **strictly sequentially**. Once a Tripādī rule fires, its output cannot trigger any Sapādāsaptādhyāyī rule, nor can it trigger an earlier Tripādī rule.

### [MY-LISP HYPOTHESIS] VM Architecture Impact
In `meta.my`, the inference engine `(run-inference)` currently applies all rules iteratively. To correctly model Panini's architecture:
1. The engine must have **two distinct phases** (Phase 1: Sapādāsaptādhyāyī, Phase 2: Tripādī).
2. Phase 2 must apply rules in strict numerical order without cyclic evaluation.
This requires tagging rules with their section (which we already do via `rule-id`) and splitting the engine's main loop.

---

## 🇺🇦 Українська: Механізм Tripādī
### [PANINI] Текстове визначення
Правило `pUrvatrAsidDam` (8.2.1) розділяє Aṣṭādhyāyī на дві різні частини:
1. **Sapādāsaptādhyāyī** (Перші 7¼ розділів): Основна граматика.
2. **Tripādī** (Останні 3 секції, 8.2-8.4): Послідовні фонологічні/сандхі правила.

Правило стверджує: "Для попередніх правил, [наступні правила в Tripādī] є ніби неіснуючими (`asiddha`)". Більше того, в межах самої Tripādī, будь-яке пізніше правило є неіснуючим для більш раннього правила.

### [INTERPRETATION] Обчислювальне значення
- **Sapādāsaptādhyāyī**: Правила можуть викликати одне одного рекурсивно до досягнення стабільного стану. Працює як rule engine з вирішенням конфліктів (через `antaraṅga`, `apavāda` тощо).
- **Tripādī**: Правила застосовуються **суворо послідовно**. Як тільки правило з Tripādī спрацьовує, його результат не може викликати жодне правило з Sapādāsaptādhyāyī, а також не може викликати більш раннє правило з Tripādī.

### [MY-LISP HYPOTHESIS] Вплив на архітектуру VM
У `meta.my` рушій виведення `(run-inference)` наразі застосовує всі правила ітеративно. Щоб правильно змоделювати архітектуру Паніні:
1. Рушій повинен мати **дві окремі фази** (Фаза 1: Sapādāsaptādhyāyī, Фаза 2: Tripādī).
2. Фаза 2 повинна застосовувати правила у строгій числовій послідовності без циклічного обчислення.
Це вимагає поділу головного циклу обчислень на основі номерів правил.

---

## 🇩🇪 Deutsch: Der Tripādī-Mechanismus
### [PANINI] Textuelle Definition
Die Regel `pUrvatrAsidDam` (8.2.1) teilt die Aṣṭādhyāyī in zwei verschiedene Abschnitte:
1. **Sapādāsaptādhyāyī** (Die ersten 7¼ Kapitel): Die Kerngrammatik.
2. **Tripādī** (Die letzten 3 Abschnitte, 8.2-8.4): Die sequentiellen phonologischen/Sandhi-Regeln.

Die Regel besagt: "Für die vorhergehenden Regeln sind [die nachfolgenden Regeln im Tripādī] als nicht existent (`asiddha`) zu betrachten." Darüber hinaus ist innerhalb des Tripādī selbst jede spätere Regel für eine frühere Regel nicht existent.

### [INTERPRETATION] Computergestützte Bedeutung
- **Sapādāsaptādhyāyī**: Regeln können sich rekursiv gegenseitig aufrufen, bis ein stabiler Zustand erreicht ist. Es fungiert als eine durch Prioritäten aufgelöste Regelmaschine (gesteuert durch `antaraṅga`, `apavāda`, usw.).
- **Tripādī**: Regeln werden **streng sequentiell** angewendet. Sobald eine Tripādī-Regel ausgelöst wird, kann ihre Ausgabe keine Sapādāsaptādhyāyī-Regel auslösen und auch keine frühere Tripādī-Regel auslösen.

### [MY-LISP HYPOTHESIS] Auswirkungen auf die VM-Architektur
In `meta.my` wendet die Inferenzmaschine `(run-inference)` derzeit alle Regeln iterativ an. Um Paninis Architektur korrekt zu modellieren:
1. Die Maschine muss **zwei getrennte Phasen** haben (Phase 1: Sapādāsaptādhyāyī, Phase 2: Tripādī).
2. Phase 2 muss die Regeln in strenger numerischer Reihenfolge ohne zyklische Auswertung anwenden.
Dies erfordert die Aufteilung der Hauptschleife der Maschine basierend auf den Regelnummern.
