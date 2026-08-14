# Два входження та їхнє відношення · Two occurrences and their relation · Zwei Vorkommen und ihre Beziehung

Статус: дослідницький запис для `PANINI-TWO-INSTANCE-RELATIONSHIP-RESEARCH`.

## English

### Bounded question

What follows when two term occurrences have the same canonical SLP1 form? The
answer is deliberately negative: spelling equality identifies neither the
same referent nor different referents. It only establishes a comparison of two
recorded forms.

### [PANINI]

This note does not attribute occurrence IDs, referent IDs, or coreference to
Pāṇini. The source-facing minimum is that a designation or kāraka claim is
assessed for an occurrence under relevant conditions; it is not licensed here
as a permanent property of a spelling.

### [INTERPRETATION]

Two records must remain distinct when their provenance, syntactic position,
derivational state, or situation differs, even if both carry `source_form:
rAma`. A safe comparison result is:

```yaml
left: term:occurrence-1
right: term:occurrence-2
observed: equal-source-form
coreference: unresolved
relation: none-asserted
```

The converse also holds: different surface forms do not alone prove different
referents. Equality/difference of forms is evidence about representations, not
evidence about an entity outside the trace.

### [MY-LISP HYPOTHESIS]

The minimum machine invariant is `term-id ≠ form`. A transition may change a
term's surface form while preserving its recorded identity; a substitution or
split must create another term ID or an explicit provenance-bearing relation.
An `entity:<id>` or `corefers-with` relation needs a separately named,
source-backed exhibit. Until then the machine returns `unresolved` rather than
creating a graph node from an SLP1 string.

### Acceptance cases

| Input | Required outcome |
| --- | --- |
| two IDs, equal `source_form` | retain two IDs; coreference `unresolved` |
| one ID, changed `surface_form` | preserve ID; record transition provenance |
| two IDs, declared relation with evidence | retain both IDs and record only that relation |
| no relation evidence | do not synthesize `entity` or coreference |

## Українська

### Обмежене питання

Що випливає з того, що два входження термів мають ту саму канонічну SLP1-форму?
Відповідь навмисно негативна: збіг написання не встановлює ані того самого,
ані різних референтів. Він встановлює лише порівняння двох зафіксованих форм.

### [PANINI]

Ця нотатка не приписує Паніні ID входжень, ID референтів чи coreference.
Джерельний мінімум інший: designation або kāraka-твердження оцінюється для
входження за релевантних умов; тут воно не ліцензується як стала властивість
написання.

### [INTERPRETATION]

Два записи мусять лишатися різними, коли відрізняються їх provenance,
синтаксична позиція, дериваційний стан або ситуація — навіть якщо в обох
`source_form: rAma`. Безпечний результат порівняння:

```yaml
left: term:occurrence-1
right: term:occurrence-2
observed: equal-source-form
coreference: unresolved
relation: none-asserted
```

Справедливе й обернене: різні surface form самі не доводять різних
референтів. Тотожність/відмінність форм є доказом про представлення, а не про
сутність поза trace.

### [MY-LISP HYPOTHESIS]

Мінімальний machine invariant: `term-id ≠ form`. Перехід може змінити surface
form терма, зберігаючи його записану identity; substitution або split мусить
створити інший term ID чи явне відношення з provenance. Для `entity:<id>` або
`corefers-with` потрібен окремо названий exhibit, підтверджений джерелом. До
того машина повертає `unresolved`, а не створює graph node зі SLP1-рядка.

### Приймальні випадки

| Вхід | Обов'язковий результат |
| --- | --- |
| два ID, рівний `source_form` | зберегти два ID; coreference `unresolved` |
| один ID, змінений `surface_form` | зберегти ID; записати provenance переходу |
| два ID, оголошене відношення з evidence | зберегти обидва ID й записати лише це відношення |
| немає evidence відношення | не синтезувати `entity` чи coreference |

## Deutsch

### Begrenzte Frage

Was folgt daraus, dass zwei Termvorkommen dieselbe kanonische SLP1-Form
besitzen? Die Antwort ist absichtlich negativ: Schriftgleichheit belegt weder
denselben noch verschiedene Referenten. Sie belegt nur den Vergleich zweier
protokollierter Formen.

### [PANINI]

Diese Notiz schreibt Pāṇini keine Vorkommens-IDs, Referent-IDs oder
Koreferenz zu. Das quellennahe Minimum lautet: Eine Designation- oder
kāraka-Behauptung wird für ein Vorkommen unter relevanten Bedingungen
beurteilt; sie wird hier nicht als dauerhafte Eigenschaft einer Schreibung
lizenziert.

### [INTERPRETATION]

Zwei Records bleiben verschieden, wenn sich Provenance, syntaktische Position,
Derivationszustand oder Situation unterscheiden, auch bei `source_form: rAma`
in beiden. Ein sicherer Vergleich meldet `equal-source-form`, aber
`coreference: unresolved` und `relation: none-asserted`. Unterschiedliche
Oberflächenformen beweisen umgekehrt ebenfalls keine verschiedenen Referenten.

### [MY-LISP HYPOTHESIS]

Das minimale Maschineninvariant ist `term-id ≠ form`. Ein Übergang darf die
Oberflächenform bei erhaltener Identity ändern; Substitution oder Split braucht
eine neue Term-ID oder eine explizite Relation mit Provenance. `entity:<id>`
oder `corefers-with` verlangt ein getrennt benanntes, quellenbelegtes Exhibit.
Bis dahin liefert die Maschine `unresolved` und keinen Graphknoten aus einem
SLP1-String.

### Abnahmefälle

Zwei IDs mit gleicher `source_form` behalten zwei IDs und `coreference:
unresolved`. Eine geänderte `surface_form` eines IDs bewahrt seine Identity
mit Übergangsprovenance. Eine evidenzierte Relation wird genau, aber keine
nicht belegte `entity`- oder Koreferenzrelation gespeichert.
