# Hypothesis: Kāraka Computational Models

> **Status:** Experimental  
> **Source Relation:** These are theoretical projections of the Pāṇinian *kāraka* system onto computational architecture (My Lisp / Symbolic AI). They are distinct from the traditional grammatical definitions found in `panini/sastra/karaka.md`.

## English

### The Core Problem: Representing `dhātu ↔ kāraka`

In our symbolic system, how should we represent the relationship between a verbal predicate (`dhātu`) and its semantic participants (`kāraka`)? We evaluate three competing computational hypotheses.

### H1a: Kāraka as Graph Edges (Initial Hypothesis)
Under this hypothesis, the relationship forms a directed graph where the *dhātu* is a predicate node, the *kāraka* are strictly typed labeled edges, and the *prātipadika* (entities) are argument nodes.

```text
[ACTION: dhātu]
   │
   ├── (edge: kartṛ) ──────▶ [ENTITY: prātipadika 1]
   │
   ├── (edge: karman) ─────▶ [ENTITY: prātipadika 2]
   │
   └── (edge: karaṇa) ─────▶ [ENTITY: prātipadika 3]
```

**Critique (Sarvam):** A *kāraka* is not a permanent edge between a *dhātu* and an entity. The same entity can act as *kartṛ* in one event and *karman* in another (e.g., active vs. passive voice inversion). If *kāraka* is an edge, the graph would have to constantly rewire its edges to represent voice changes, implying the edges are surface-level epiphenomena rather than deep semantic primitives.

### H1b: Kāraka as Contextual Designation (Current Leading Hypothesis)
*Kāraka* is a **designation** (assignment/role) of a participant relative to an action in a specific utterance context, rather than a structural relation inherent to the verb.

- **Formula:** `entity participates in event + contextual designation`
- **Implications for My Lisp:** The role is not a permanent property of the entity. `Entity ≠ property ≠ context`. A single entity node receives a contextual role tag (designation) for the duration of a specific evaluation context.

### H1c: Kāraka as a First-Class Relation Node
Instead of edges or tags, *kāraka* is a distinct first-class relation node that links an action event to a participant entity. This would allow the relation itself to be targeted by rules (e.g., assigning case markers to the relation node rather than the entity node).

---

## Українська

### Основна проблема: Репрезентація `dhātu ↔ kāraka`

У нашій символьній системі, як ми повинні представляти зв'язок між дієслівним предикатом (`dhātu`) та його семантичими учасниками (`kāraka`)? Ми розглядаємо три конкуруючі обчислювальні гіпотези.

### H1a: Kāraka як ребра графа (Початкова гіпотеза)
Згідно з цією гіпотезою, відношення формує орієнтований граф, де *dhātu* — це вузол-предикат, *kāraka* — це строго типізовані марковані ребра, а *prātipadika* (сутності) — вузли-аргументи.

```text
[ACTION: dhātu]
   │
   ├── (edge: kartṛ) ──────▶ [ENTITY: prātipadika 1]
   │
   ├── (edge: karman) ─────▶ [ENTITY: prātipadika 2]
   │
   └── (edge: karaṇa) ─────▶ [ENTITY: prātipadika 3]
```

**Критика (Sarvam):** *kāraka* не є ребром між *dhātu* та сутністю назавжди. Одна й та сама сутність може бути *kartṛ* в одній події та *karman* в іншій (наприклад, інверсія при пасивному стані). Якщо *kāraka* — це ребро, графу довелося б постійно "перепрошивати" свої ребра для представлення стану (voice), що означає, що ребра є поверхневими епіфеноменами, а не глибокими семантичними примітивами.

### H1b: Kāraka як контекстуальне призначення (Поточна провідна гіпотеза)
*Kāraka* — це **designation** (призначення/роль) учасника відносно дії в конкретному контексті висловлювання, а не структурне відношення, притаманне самому дієслову.

- **Формула:** `entity participates in event + contextual designation`
- **Значення для My Lisp:** Роль не є постійною властивістю сутності. `Сутність ≠ властивість ≠ контекст`. Єдиний вузол сутності отримує контекстуальний тег ролі (designation) на час конкретного контексту обчислення (evaluation context).

### H1c: Kāraka як вузол-відношення першого класу
Замість ребер або тегів, *kāraka* — це окремий вузол-відношення першого класу, який пов'язує подію-дію з сутністю-учасником. Це дозволило б правилам безпосередньо впливати на саме відношення (наприклад, призначати відмінкові маркери вузлу відношення, а не вузлу сутності).

---

## Deutsch

### Das Kernproblem: Darstellung von `dhātu ↔ kāraka`

Wie sollen wir in unserem symbolischen System die Beziehung zwischen einem verbalen Prädikat (`dhātu`) und seinen semantischen Teilnehmern (`kāraka`) darstellen? Wir bewerten drei konkurrierende rechnergestützte Hypothesen.

### H1a: Kāraka als Graphenkanten (Ursprüngliche Hypothese)
Unter dieser Hypothese bildet die Beziehung einen gerichteten Graphen, in dem das *dhātu* ein Prädikatknoten, die *kāraka* streng typisierte markierte Kanten und die *prātipadika* (Entitäten) Argumentknoten sind.

```text
[ACTION: dhātu]
   │
   ├── (edge: kartṛ) ──────▶ [ENTITY: prātipadika 1]
   │
   ├── (edge: karman) ─────▶ [ENTITY: prātipadika 2]
   │
   └── (edge: karaṇa) ─────▶ [ENTITY: prātipadika 3]
```

**Kritik (Sarvam):** Ein *kāraka* ist keine dauerhafte Kante zwischen einem *dhātu* und einer Entität. Dieselbe Entität kann in einem Ereignis als *kartṛ* und in einem anderen als *karman* agieren (z. B. Aktiv- vs. Passiv-Inversion). Wenn *kāraka* eine Kante wäre, müsste der Graph seine Kanten ständig neu verdrahten, um das Genus verbi darzustellen, was impliziert, dass die Kanten Oberflächen-Epiphänomene und keine tiefensemantischen Primitive sind.

### H1b: Kāraka als Kontextuelle Bezeichnung (Aktuell Führende Hypothese)
*Kāraka* ist eine **Bezeichnung** (Zuweisung/Rolle) eines Teilnehmers in Bezug auf eine Handlung in einem spezifischen Äußerungskontext, keine dem Verb innewohnende strukturelle Beziehung.

- **Formel:** `entity participates in event + contextual designation`
- **Bedeutung für My Lisp:** Die Rolle ist keine dauerhafte Eigenschaft der Entität. `Entität ≠ Eigenschaft ≠ Kontext`. Ein einzelner Entitätsknoten erhält für die Dauer eines spezifischen Auswertungskontexts ein kontextuelles Rollen-Tag (Bezeichnung).

### H1c: Kāraka als First-Class-Beziehungsknoten
Anstelle von Kanten oder Tags ist *kāraka* ein eigenständiger First-Class-Beziehungsknoten, der ein Handlungsereignis mit einer Teilnehmerentität verbindet. Dies würde es Regeln ermöglichen, auf die Beziehung selbst abzuzielen (z. B. die Zuweisung von Kasusmarkierungen an den Beziehungsknoten statt an den Entitätsknoten).
