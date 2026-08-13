# dadAti conflict-test readiness / Готовність conflict-тесту dadAti / Bereitschaft des dadAti-Konflikttests

## English

**Scope:** implementation-readiness audit for
`PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST`; this is not evidence for a
historical claim about Pāṇini.

The checked machine tree contains `test-dadati-derivation`, but no definition
of `derive-dadAti` was found. `run-tests` also does not invoke that test.
Therefore a passing `dadAti` conflict test cannot yet be reported. The minimal
next decision is whether the derivation harness belongs to the preceding
derivation task or to this test task; after that decision, the test must verify
both the selected rule and the final form, rather than only a final string.

## Українська

**Обсяг:** аудит готовності реалізації для
`PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST`; це не є доказом історичного
твердження про Паніні.

У перевіреному machine-tree є `test-dadati-derivation`, але визначення
`derive-dadAti` не знайдено. `run-tests` також не викликає цей тест. Отже,
не можна чесно повідомляти про passing conflict-test для `dadAti`. Мінімальне
наступне рішення: чи належить derivation harness попередній задачі деривації,
чи цій тестовій задачі; після рішення тест мусить перевіряти і вибране правило,
і фінальну форму, а не лише фінальний рядок.

## Deutsch

**Umfang:** Audit der Implementierungsbereitschaft für
`PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST`; dies ist kein Beleg für eine
historische Behauptung über Pāṇini.

Im geprüften Machine-Tree existiert `test-dadati-derivation`, aber keine
Definition von `derive-dadAti` wurde gefunden. `run-tests` ruft diesen Test
ebenfalls nicht auf. Ein bestehender dadAti-Konflikttest kann daher noch nicht
ehrlich gemeldet werden. Die minimale nächste Entscheidung lautet, ob der
Derivation-Harness zur vorherigen Derivationsaufgabe oder zu dieser Testaufgabe
gehört; danach muss der Test sowohl die gewählte Regel als auch die Endform
prüfen, nicht nur einen Endstring.
