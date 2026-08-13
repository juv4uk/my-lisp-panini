# dadAti conflict review: source evidence versus executable evidence

## English

### Scope

This review distinguishes source evidence from an executable machine fixture.
It does not certify a complete historical derivation.

### What the source model expresses

`rules.my` represents 2.4.72 as the general (`utsarga`) Sap-deletion rule and
2.4.75 as a class-3 (`juhotyAdi`) rule whose `:utsarga` field names 2.4.72.
`meta.my` therefore selects 2.4.75 through its explicit
`apavada-of?` predicate before reaching its later-sūtra fallback. This is a
coherent **machine encoding** of the intended general-rule/exception relation.

The model then expresses a further Slu-tag, reduplication, and short-vowel
sequence for `dadAti`. Its test currently asserts only the final text
`"dadAti"`; the test comments themselves correctly say that no
provenance-bearing trace is yet exposed.

### Limits and required evidence

`apavAda > utsarga` in this source is a declared relation, not an inferred
proof from the sūtra corpus. The final spelling does not prove that 2.4.75 was
selected rather than another path. A valid conflict-level test must expose:

1. both applicable rule identifiers, 2.4.72 and 2.4.75;
2. the encoded `:utsarga` relation;
3. the selected winner, 2.4.75;
4. the selection reason `apavAda-over-utsarga`; and
5. the state transition that adds the Slu-related tag.

On 2026-08-14, the macro-free fixture entry point executed all five required
observations in the My Lisp VM: both IDs, the encoded relation, `apavAda` as
the trace reason and 2.4.75 as winner, plus two visible Slu tags. This is
executable evidence for the declared machine fixture only; it is not a proof
that the historical corpus mandates this implementation.

### Semantic identifier boundary

The newer `SemanticCall` bridge uses `DHATU_DA` and `KARAKA_KARTR`. These may
be internal experimental identifiers, but they are not canonical SLP1 strings
(`dA`, `kartf`). They therefore need an explicit mapping/provenance layer and
must not be presented as the foundation's canonical identifiers.

## Українська

### Межа review

Цей review розділяє source evidence і виконуваний machine fixture для `dadAti`.
Він не сертифікує повну історичну деривацію.

### Що виражає source-модель

`rules.my` подає 2.4.72 як загальне (`utsarga`) правило вилучення Sap, а 2.4.75
— як правило для класу 3 (`juhotyAdi`), поле `:utsarga` якого вказує на 2.4.72.
Тому `meta.my` обирає 2.4.75 через явний predicate `apavada-of?`, ще до
fallback на пізніше sūtra. Це узгоджене **машинне кодування** задуманої пари
загального правила та винятку.

Далі модель кодує Slu-tag, редуплікацію та скорочення голосного для `dadAti`.
Наявний тест перевіряє лише фінальний текст `"dadAti"`; його коментар слушно
вказує, що provenance-bearing trace ще не відкрито.

### Межі й потрібний доказ

`apavAda > utsarga` у source — оголошене відношення, а не доведений висновок з
корпусу sūtra. Фінальне написання не доводить, що обрано 2.4.75, а не інший
шлях. Коректний conflict-level test має показати:

1. обидва застосовні ID правил: 2.4.72 і 2.4.75;
2. закодоване відношення `:utsarga`;
3. переможця 2.4.75;
4. причину `apavAda-over-utsarga`; і
5. state transition, що додає Slu-пов'язаний tag.

2026-08-14 macro-free fixture entrypoint виконав усі п'ять потрібних
спостережень у My Lisp VM: обидва ID, закодоване відношення, `apavAda` як
причину trace і 2.4.75 як переможця, а також два видимі Slu tags. Це виконуване
evidence лише для оголошеного machine fixture; воно не доводить, що історичний
корпус вимагає саме такої реалізації.

### Межа semantic identifiers

Новий bridge `SemanticCall` використовує `DHATU_DA` і `KARAKA_KARTR`. Це можуть
бути внутрішні експериментальні IDs, але не канонічні рядки SLP1 (`dA`,
`kartf`). Отже, їм потрібен явний mapping/provenance layer; їх не можна
подавати як канонічні identifiers фундаменту.

## Deutsch

### Umfang

Dieses Review trennt Source-Evidence von einem ausführbaren `dadAti`-
Maschinenfixture. Es bestätigt keine vollständige historische Derivation.

### Aussage des Source-Modells

`rules.my` kodiert 2.4.72 als allgemeine (`utsarga`) Sap-Löschung und 2.4.75
als Klassen-3-Regel mit Verweis auf 2.4.72 im Feld `:utsarga`. `meta.my` wählt
damit 2.4.75 mittels `apavada-of?`, bevor der spätere-Sūtra-Fallback greift.
Das ist eine kohärente **Maschinenkodierung** der Regel/Ausnahme-Beziehung.

Der Endtext `"dadAti"` allein beweist keine Regelwahl. Am 2026-08-14 prüfte
der makrofreie Fixture-Einstiegspunkt in der My-Lisp-VM beide Regeln, die
deklarierte `utsarga`-Relation, `apavAda` als Grund, Gewinner 2.4.75 und zwei
sichtbare Slu-Tags. Das ist ausführbare Evidenz nur für das deklarierte
Maschinenfixture, kein Beweis einer historischen Pāṇini-Interpretation.

### Grenze semantischer IDs

`DHATU_DA` und `KARAKA_KARTR` sind mögliche interne experimentelle IDs, aber
nicht die kanonischen SLP1-Strings `dA` und `kartf`; dafür ist eine explizite
Mapping-/Provenance-Schicht erforderlich.
