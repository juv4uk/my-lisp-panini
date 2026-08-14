# Vidyut ↔ Sanskrit Heritage: differential examples

Status: comparative research for `PANINI-VIDYUT-HERITAGE-DIFFERENTIAL-EXAMPLES`.
This is not a benchmark and does not rank the systems.

## English — reference translation

### Question

Vidyut and Sanskrit Heritage must not be compared as competing answers to a
single task. The audited implementations principally occupy different points in
the generation ↔ analysis space. These examples state what each architecture
can teach the Panini Machine without importing its machinery as Paninian fact.

### Example A — a bounded generated form

**Input shape:** a chosen `dhAtu`, suffixes, and stated derivational conditions.

| Observation | Vidyut | Sanskrit Heritage | Consequence for this project |
|---|---|---|---|
| Natural task | generate a form through ordered changes | not the primary audited task | a traceable derivation fixture belongs to the generation side |
| Useful model | typed terms plus ordered `Step` journal | no reason to import a segmenter | retain immutable state/transition evidence |
| Wrong inference | `Step` is Panini itself | Heritage is inferior because it does not supply this trace | the task determines the model |

### Example B — continuous text with a possible boundary sandhi

**Input shape:** a surface string whose word boundaries are not supplied.

| Observation | Vidyut | Sanskrit Heritage | Consequence for this project |
|---|---|---|---|
| Natural task | assumes structured input for generation | explores segmentation alternatives with an automaton and backtracking | parsing is a distinct future phase |
| Honest result | no claim from a missing segmentation | more than one candidate may remain | ambiguity must remain explicit, not be collapsed to one derivation |
| Wrong inference | a generation journal parses text | a parse candidate proves a derivational history | analysis and generation need separate evidence |

### Example C — an implementation decision

**Input shape:** the need to make an operation fast or a UI inspectable.

| Observation | Vidyut | Sanskrit Heritage | Consequence for this project |
|---|---|---|---|
| Engineering choice | compact Rust term/tag structures | trie, automaton, stack/graph alternatives | classify as `implementation-convenience` |
| Paninian claim | none follows from the data structure | none follows from the data structure | never promote a useful representation to a source claim |

### Differential conclusion

For the current machine, Vidyut supports the question “how do we retain an
ordered, explainable generation trace?” Heritage supports the question “how do
we keep alternative analyses visible when input is ambiguous?” Neither answers
whether a Paninian category is a My Lisp primitive. Any future combined system
must preserve the boundary between a generated derivation trace and a parsed
candidate set.

## Українська — нормативна

### Питання

Vidyut і Sanskrit Heritage не можна порівнювати як конкурентні відповіді на
одну задачу. В аудиті вони займають різні точки простору generation ↔ analysis.
Ці приклади показують, чого кожна архітектура може навчити Panini Machine, не
переносячи її механіку як панініївський факт.

### Приклад A — обмежена згенерована форма

**Форма входу:** вибраний `dhAtu`, suffixes і зазначені умови деривації.

| Спостереження | Vidyut | Sanskrit Heritage | Висновок для проєкту |
|---|---|---|---|
| Природна задача | генерувати форму через впорядковані зміни | не є основною аудитованою задачею | traceable derivation fixture належить до generation-side |
| Корисна модель | типізовані terms і впорядкований `Step` journal | немає причини переносити segmenter | зберігати immutable state/transition evidence |
| Хибний висновок | `Step` і є Паніні | Heritage гірший, бо не дає цього trace | модель визначає задача |

### Приклад B — суцільний текст із можливим boundary sandhi

**Форма входу:** surface string, для якого word boundaries не задані.

| Спостереження | Vidyut | Sanskrit Heritage | Висновок для проєкту |
|---|---|---|---|
| Природна задача | передбачає structured input для generation | досліджує segmentation alternatives через automaton і backtracking | parsing є окремою майбутньою фазою |
| Чесний результат | немає висновку без segmentation | може лишитися кілька candidates | ambiguity мусить бути явною, не зведеною до однієї деривації |
| Хибний висновок | generation journal парсить текст | parse candidate доводить derivational history | analysis і generation потребують окремих доказів |

### Приклад C — рішення реалізації

**Форма входу:** потреба зробити operation швидкою або UI оглядовим.

| Спостереження | Vidyut | Sanskrit Heritage | Висновок для проєкту |
|---|---|---|---|
| Інженерне рішення | компактні Rust term/tag structures | trie, automaton, stack/graph alternatives | класифікувати як `implementation-convenience` |
| Панініївське твердження | жодне не випливає зі структури даних | жодне не випливає зі структури даних | не підвищувати корисне представлення до source claim |

### Диференційний висновок

Для поточної машини Vidyut допомагає відповісти: «як зберігати впорядкований,
пояснюваний generation trace?». Heritage допомагає спитати: «як залишати
видимими alternative analyses за неоднозначного input?». Жоден не відповідає,
чи є панініївська категорія primitive My Lisp. Майбутня комбінована система має
зберегти межу між generated derivation trace і parsed candidate set.

## Deutsch — Referenzübersetzung

### Frage und drei Beispiele

Vidyut und Sanskrit Heritage sind keine konkurrierenden Antworten auf dieselbe
Aufgabe. Sie liegen an verschiedenen Punkten zwischen Generation und Analyse.

Bei einer begrenzten generierten Form mit `dhAtu`, Suffixen und Bedingungen ist
Vidyuts Modell aus typisierten Terms und geordnetem `Step`-Journal natürlich;
ein Segmenter wird nicht importiert. Bei kontinuierlichem Text ohne
Wortgrenzen ist Heritage mit Automat und Backtracking natürlich; mehrere
Kandidaten dürfen sichtbar bleiben. Ein Generation-Journal parst keinen Text,
und ein Parse-Kandidat beweist keine Derivationsgeschichte.

Kompakte Rust-Strukturen bei Vidyut sowie Trie-, Automaten- und
Stack/Graph-Alternativen bei Heritage sind `implementation-convenience`; aus
ihnen folgt keine Panini-Behauptung. Vidyut hilft gegenwärtig bei erklärbarer
Generation, Heritage bei sichtbarer Analysemehrdeutigkeit. Keines macht eine
paninische Kategorie zu einem My-Lisp-Primitive. Eine spätere Kombination muss
generated derivation trace und parsed candidate set getrennt halten.

## Sources

- [`vidyut-analysis.md`](vidyut-analysis.md)
- [`heritage-analysis.md`](heritage-analysis.md)
- [`derivation-corpus-stress-protocol-v0.1.md`](../specs/derivation-corpus-stress-protocol-v0.1.md)
