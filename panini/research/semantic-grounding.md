# Semantic grounding · Семантичне заземлення · Semantische Grundlegung

Status: research record for `PHILOSOPHY-SEMANTIC-GROUNDING`
Author: my-lisp-panini-1 · 2026-08-14
Links: → `PHILOSOPHY-MACHINE-UNDERSTANDING`, ← `PHILOSOPHY-SAMANYA-VISESA-ONTOLOGY`,
→ [`specs/philosophy-control-layer-v0.1.md`](../specs/philosophy-control-layer-v0.1.md)

## English

### Central question

What does it mean for a semantic claim about the Pāṇinian system to be
*grounded* in our machine model — as opposed to merely displayed, asserted, or
carried over from an interpretation?

### [PANINI]

"Grounding" is not a term of the Aṣṭādhyāyī; this note does not attribute it
to the source. What the source does provide is the pattern that a
semantic-functional role is fixed by a *checkable criterion in context*, not by
a form in isolation:

- `kāraka` roles are determined by sentence conditions, e.g. `svatantraH kartA`
  (1.4.54): `devadatta` is `kartf` in a given sentence because he satisfies the
  criterion there, not because the word is permanently tagged.
- `saMjYA` establishes a class (e.g. `guRa` by 1.1.2) whose membership later
  rules check against an occurrence.

The role is therefore anchored to a checkable relation between the item and its
context, not to the display label of the item.

### [INTERPRETATION]

We distinguish two senses of "semantics":

| Sense | Question | Checkable? |
| --- | --- | --- |
| display semantics | What does the record look like when rendered? | no — it is a presentation artifact |
| truth-condition semantics | What condition must hold for the claim to be true? | yes — against an exhibit |

A semantic claim is *grounded in our sense* when it is a truth-condition claim:
there is a concrete exhibit (a state, a relation, a trace event, a test) that
can confirm or disconfirm it. A readable rendering is not a grounding; it can
only point at one. This is our modern methodological distinction, not a claim
about Pāṇini's own method.

### [MY-LISP HYPOTHESIS]

#### Grounding criteria

A machine semantic claim `C` about a stable subject `S` is **grounded** when all
of the following hold:

1. **Stable subject** — `S` is addressable (a term id, state id, or relation id
   in the IR), not a free-floating phrase.
2. **Exhibit** — there is a concrete checkable exhibit: a test assertion, a
   typed state transition, or a relation record that instantiates `C`.
3. **Falsifier** — `C` names a condition or counterexample that would
   disconfirm it (per the control-layer `falsifier` check).
4. **Provenance at the right layer** — `C` carries provenance records and its
   epistemic layer (`panini` / `interpretation` / `my-lisp-hypothesis`) matches
   the exhibit; a trace result cannot upgrade an interpretation.
5. **Display is not proof** — a surface observation is recorded as a
   `trace-observation` event, never as verification of the intermediate chain.

These map onto the control-layer decision gates
(`specs/philosophy-control-layer-v0.1.md`): `grounded` ↔ an admitted machine
claim with a present falsifier; `interpretation` ↔ `needs-check`; `display`
↔ a presentation artifact.

#### Worked cases

| Claim | Exhibit | Grounding status |
| --- | --- | --- |
| `devadatta` is `kartf` in this sentence | kāraka membership satisfied against the sentence (sāmānya/viśeṣa relation, `research/samanya-visesa-ontology.md`) | grounded as a situated membership claim |
| `Bavati` is the surface form | `bavati-surface-terms` observation (`rules.my`) | display observation; not grounded as proof of guna/sandhi |
| `it`-designation on final `p` of `tip` | provenance-bearing trace record (`bavati` step 3) | grounded as a recorded machine claim at its layer |
| guna precondition for 7.3.84 | no source-backed bridge from it-analysis to sArvadhAtuka | not grounded; must remain an explicit unknown |

#### Machine consequence

Grounding is a *property of the record*, not of the rendering. Until a claim
has an exhibit and a falsifier, the machine must keep it at `needs-check` or
`unknown` (as the `Bavati` trace does with its four unknowns). This is the
contract that `PHILOSOPHY-MACHINE-UNDERSTANDING` should later make executable.

### Open questions

1. Does grounding require an *executable* exhibit, or is a documented,
   independently inspectable exhibit sufficient?
2. Should the machine expose a grounding predicate (`grounded?`,
   `falsifier-present?`) as part of the control layer, or is this a
   documentation contract only?
3. Where does grounding end and historical verification begin — and how does
   the boundary stay auditable when a display observation matches a derivation?
4. Is a "situated membership" claim (kāraka) grounded by the same criteria as a
   class-membership claim (saṃjñā), or do they need distinct exhibit types?

### Sources

- [`foundation/samjna.md`](../sastra/samjna.md) — saṃjñā as checkable designation
- [`foundation/karaka.md`](../sastra/karaka.md) — kāraka determined by sentence criteria
- [`research/samanya-visesa-ontology.md`](samanya-visesa-ontology.md) — universal/particular membership
- [`specs/philosophy-control-layer-v0.1.md`](../specs/philosophy-control-layer-v0.1.md) — admission gates, falsifier, directionality
- [`specs/derivation-machine-explanation-boundary-v0.1.md`](../specs/derivation-machine-explanation-boundary-v0.1.md) — falsifiable, exhibit-able machine explanation
- [`specs/derivation-ir-trace-events-v0.1.md`](../specs/derivation-ir-trace-events-v0.1.md) — `trace-observation` vocabulary
- Aṣṭādhyāyī 1.4.54 (`svatantraH kartA`) — criterion-based kāraka (per project citation provenance)

---

## Українська

### Центральне питання

Що означає, що семантичне твердження про систему Паніні є *заземленим*
(grounded) у нашій машинній моделі — на відміну від лише відображеного,
заявленого чи перенесеного з інтерпретації?

### [PANINI]

«Заземлення» не є терміном Аṣṭādhyāyī; ця нотатка не приписує його джерелу.
Що джерело справді дає — це патерн, за яким семантично-функціональна роль
фіксується *перевірюваним критерієм у контексті*, а не формою сама по собі:

- `kāraka`-ролі визначаються умовами речення, напр. `svatantraH kartA`
  (1.4.54): `devadatta` є `kartf` у цьому реченні, бо задовольняє критерій
  там, а не тому, що слово постійно затеговане.
- `saMjYA` встановлює клас (напр. `guRa` за 1.1.2), членство в якому пізніші
  правила перевіряють проти конкретного входження.

Отже, роль закріплена за перевірюваним відношенням між елементом і його
контекстом, а не за display-міткою елемента.

### [INTERPRETATION]

Розрізняємо два значення «семантики»:

| Значення | Питання | Перевірюване? |
| --- | --- | --- |
| display-семантика | Як запис виглядає при відображенні? | ні — це presentation artifact |
| семантика truth-condition | Яка умова має виконуватись, щоб твердження було істинним? | так — проти exhibit |

Семантичне твердження *заземлене в нашому сенсі*, коли воно є
truth-condition-твердженням: існує конкретний exhibit (стан, відношення, подія
trace, тест), який може його підтвердити чи спростувати. Читабельне
відображення не є заземленням; воно може лише вказувати на нього. Це наша
сучасна методологічна відмінність, а не твердження про метод Паніні.

### [MY-LISP HYPOTHESIS]

#### Критерії заземлення

Машинне семантичне твердження `C` про стабільний суб'єкт `S` є **заземленим**,
коли виконуються всі умови:

1. **Стабільний суб'єкт** — `S` адресується (id терма, стану або відношення в
   IR), а не є вільною фразою.
2. **Exhibit** — існує конкретний перевірюваний exhibit: тестова асерція,
   типізований state transition або запис відношення, що інстанціює `C`.
3. **Фальсифікатор** — `C` називає умову або контрприклад, які його
   спростували б (перевірка `falsifier` у control layer).
4. **Provenance на правильному рівні** — `C` має provenance-записи, а його
   епістемічний рівень (`panini` / `interpretation` / `my-lisp-hypothesis`)
   відповідає exhibit; результат trace не може підвищити інтерпретацію.
5. **Display не є доказом** — спостережена поверхнева форма записується як
   подія `trace-observation`, а не як верифікація проміжного ланцюга.

Це лягає на шлюзи рішення control layer
(`specs/philosophy-control-layer-v0.1.md`): `grounded` ↔ допущене машинне
твердження з наявним фальсифікатором; `interpretation` ↔ `needs-check`;
`display` ↔ presentation artifact.

#### Розглянуті випадки

| Твердження | Exhibit | Статус заземлення |
| --- | --- | --- |
| `devadatta` є `kartf` у цьому реченні | членство kāraka задоволене проти речення (відношення sāmānya/viśeṣa, `research/samanya-visesa-ontology.md`) | заземлене як ситуативне твердження членства |
| `Bavati` є поверхневою формою | спостереження `bavati-surface-terms` (`rules.my`) | display-спостереження; не заземлене як доказ guṇa/sandhi |
| it-designation на кінцевому `p` у `tip` | provenance-bearing trace record (крок 3 `bavati`) | заземлене як зафіксоване машинне твердження на своєму рівні |
| передумова guṇa для 7.3.84 | немає джерельного мосту від it-аналізу до sArvadhAtuka | не заземлене; мусить лишатися явним unknown |

#### Машинний наслідок

Заземлення — це *властивість запису*, а не відображення. Поки твердження не
має exhibit і фальсифікатора, машина мусить тримати його на `needs-check` або
`unknown` (як це робить trace `Bavati` зі своїми чотирма unknowns). Це
контракт, який `PHILOSOPHY-MACHINE-UNDERSTANDING` має зробити виконуваним.

### Відкриті питання

1. Чи потребує заземлення *виконуваного* exhibit, чи достатньо задокументованого,
   незалежно перевірюваного?
2. Чи має машина надавати предикат заземлення (`grounded?`,
   `falsifier-present?`) як частину control layer, чи це лише документаційний
   контракт?
3. Де закінчується заземлення і починається історична верифікація — і як межа
   лишається перевірюваною, коли display-спостереження збігається з деривацією?
4. Чи «ситуативне членство» (kāraka) заземлюється тими самими критеріями, що й
   членство в класі (saṃjñā), чи їм потрібні різні типи exhibit?

### Джерела

- [`foundation/samjna.md`](../sastra/samjna.md) — saṃjñā як перевірювана позначка
- [`foundation/karaka.md`](../sastra/karaka.md) — kāraka, визначений умовами речення
- [`research/samanya-visesa-ontology.md`](samanya-visesa-ontology.md) — членство universal/particular
- [`specs/philosophy-control-layer-v0.1.md`](../specs/philosophy-control-layer-v0.1.md) — шлюзи допуску, фальсифікатор, спрямованість
- [`specs/derivation-machine-explanation-boundary-v0.1.md`](../specs/derivation-machine-explanation-boundary-v0.1.md) — фальсифіковане, exhibit-able машинне пояснення
- [`specs/derivation-ir-trace-events-v0.1.md`](../specs/derivation-ir-trace-events-v0.1.md) — словник подій `trace-observation`
- Аṣṭādhyāyī 1.4.54 (`svatantraH kartA`) — kāraka на основі критерію (за citation provenance проєкту)

---

## Deutsch

### Kernfrage

Was bedeutet es, dass eine semantische Aussage über das Pāṇini-System in
unserem Maschinenmodell *gegründet* (grounded) ist — im Unterschied zu bloß
angezeigt, behauptet oder aus einer Interpretation übernommen?

### [PANINI]

„Grundlegung" ist kein Terminus der Aṣṭādhyāyī; diese Notiz schreibt ihn der
Quelle nicht zu. Was die Quelle liefert, ist das Muster, dass eine
semantisch-funktionale Rolle durch ein *prüfbares Kriterium im Kontext*
festgelegt wird, nicht durch eine Form für sich:

- `kāraka`-Rollen ergeben sich aus Satzbedingungen, z. B. `svatantraH kartA`
  (1.4.54): `devadatta` ist in einem Satz `kartf`, weil er das Kriterium dort
  erfüllt, nicht weil das Wort dauerhaft getaggt ist.
- `saMjYA` etabliert eine Klasse (z. B. `guRa` durch 1.1.2), deren
  Zugehörigkeit spätere Regeln gegen ein Vorkommen prüfen.

Die Rolle ist also an eine prüfbare Beziehung zwischen dem Element und seinem
Kontext gebunden, nicht an die Anzeige-Etikette des Elements.

### [INTERPRETATION]

Wir unterscheiden zwei Bedeutungen von „Semantik":

| Bedeutung | Frage | Prüfbar? |
| --- | --- | --- |
| Display-Semantik | Wie sieht der Datensatz bei der Anzeige aus? | nein — ein Präsentationsartefakt |
| Wahrheitsbedingungs-Semantik | Welche Bedingung muss für die Wahrheit gelten? | ja — gegen ein Exhibit |

Eine semantische Aussage ist *in unserem Sinne gegründet*, wenn sie eine
Wahrheitsbedingungs-Aussage ist: Es gibt ein konkretes Exhibit (einen Zustand,
eine Relation, ein Trace-Ereignis, einen Test), das sie bestätigen oder
widerlegen kann. Eine lesbare Darstellung ist keine Grundlegung; sie kann nur
auf eine verweisen. Dies ist unsere moderne methodische Unterscheidung, keine
Aussage über Pāṇinis Methode.

### [MY-LISP HYPOTHESIS]

#### Grundlegungskriterien

Eine maschinelle semantische Aussage `C` über ein stabiles Subjekt `S` ist
**gegründet**, wenn alle folgenden Bedingungen gelten:

1. **Stabiles Subjekt** — `S` ist adressierbar (eine Term-, Zustands- oder
   Relations-ID im IR), keine freie Phrase.
2. **Exhibit** — es gibt ein konkretes prüfbares Exhibit: eine
   Test-Behauptung, einen typisierten Zustandsübergang oder einen
   Relationsdatensatz, der `C` instanziiert.
3. **Falsifikator** — `C` nennt eine Bedingung oder ein Gegenbeispiel, das sie
   widerlegen würde (Check `falsifier` der Control-Schicht).
4. **Provenienz auf der richtigen Ebene** — `C` trägt Provenienzdatensätze und
   seine epistemische Ebene (`panini` / `interpretation` /
   `my-lisp-hypothesis`) passt zum Exhibit; ein Trace-Ergebnis kann keine
   Interpretation anheben.
5. **Display ist kein Beweis** — eine beobachtete Oberflächenform wird als
   `trace-observation`-Ereignis aufgezeichnet, nicht als Verifikation der
   Zwischenkette.

Dies deckt sich mit den Zulassungsportalen der Control-Schicht
(`specs/philosophy-control-layer-v0.1.md`): `grounded` ↔ zugelassene
Maschinenaussage mit vorhandenem Falsifikator; `interpretation` ↔
`needs-check`; `display` ↔ Präsentationsartefakt.

#### Bearbeitete Fälle

| Aussage | Exhibit | Grundlegungsstatus |
| --- | --- | --- |
| `devadatta` ist in diesem Satz `kartf` | kāraka-Zugehörigkeit gegen den Satz erfüllt (sāmānya/viśeṣa-Relation, `research/samanya-visesa-ontology.md`) | gegründet als situierte Zugehörigkeitsaussage |
| `Bavati` ist die Oberflächenform | Beobachtung `bavati-surface-terms` (`rules.my`) | Display-Beobachtung; nicht als Beweis von guṇa/sandhi gegründet |
| it-Bezeichnung auf End-`p` in `tip` | provenienzbehafteter Trace-Datensatz (Schritt 3 von `bavati`) | gegründet als aufgezeichnete Maschinenaussage auf ihrer Ebene |
| guṇa-Voraussetzung für 7.3.84 | kein quellenbelegter Brücke von der it-Analyse zu sArvadhAtuka | nicht gegründet; muss explizit unbekannt bleiben |

#### Maschinenkonsequenz

Grundlegung ist eine *Eigenschaft des Datensatzes*, nicht der Darstellung. Bis
eine Aussage ein Exhibit und einen Falsifikator hat, muss die Maschine sie auf
`needs-check` oder `unknown` halten (wie es der `Bavati`-Trace mit seinen vier
Unbekannten tut). Dies ist der Vertrag, den `PHILOSOPHY-MACHINE-UNDERSTANDING`
später ausführbar machen soll.

### Offene Fragen

1. Erfordert Grundlegung ein *ausführbares* Exhibit oder genügt ein
   dokumentiertes, unabhängig prüfbares?
2. Soll die Maschine ein Grundlegungsprädikat (`grounded?`,
   `falsifier-present?`) als Teil der Control-Schicht anbieten, oder ist dies
   nur ein Dokumentationsvertrag?
3. Wo endet Grundlegung und beginnt historische Verifikation — und wie bleibt
   die Grenze prüfbar, wenn eine Display-Beobachtung mit einer Ableitung
   übereinstimmt?
4. Wird eine „situierte Zugehörigkeits"-Aussage (kāraka) nach denselben
   Kriterien gegründet wie eine Klassen-Zugehörigkeit (saṃjñā), oder brauchen
   sie unterschiedliche Exhibit-Typen?

### Quellen

- [`foundation/samjna.md`](../sastra/samjna.md) — saṃjñā als prüfbare Bezeichnung
- [`foundation/karaka.md`](../sastra/karaka.md) — kāraka durch Satzkriterien bestimmt
- [`research/samanya-visesa-ontology.md`](samanya-visesa-ontology.md) — Zugehörigkeit universal/particular
- [`specs/philosophy-control-layer-v0.1.md`](../specs/philosophy-control-layer-v0.1.md) — Zulassungsportale, Falsifikator, Richtung
- [`specs/derivation-machine-explanation-boundary-v0.1.md`](../specs/derivation-machine-explanation-boundary-v0.1.md) — falsifizierbare, exhibit-fähige Maschinenerklärung
- [`specs/derivation-ir-trace-events-v0.1.md`](../specs/derivation-ir-trace-events-v0.1.md) — Vokabular der `trace-observation`-Ereignisse
- Aṣṭādhyāyī 1.4.54 (`svatantraH kartA`) — kāraka auf Kriterienbasis (gemäß der Zitations-Provenienz des Projekts)
