# Pratyāhāra exhaustive test audit

Status: `PANINI-PRATYAHARA-EXHAUSTIVE-TEST`. This is a source/test-vector
audit; it does not modify the experimental machine generator.

## English summary

The canonical SLP1 vectors distinguish sounds from it markers and an ordered
scan from set membership. They expose errors in the current Foundation note and
machine artifact around rows 9–11. A future generator must consume a versioned
source manifest and pass the vectors before it can be treated as derived data.
The Ukrainian section is normative.

## Українська

### [PANINI]

Тестовий вектор фіксує послідовність 14 Māheśvara/Śiva Sūtras у SLP1 та
розділяє phoneme від кінцевого `it`-marker. Незалежно звірені рядки, критичні
для попередньої розбіжності:

```text
9.  G Q D [z]
10. j b g q d [S]
11. K P C W T c w t [v]
```

Тому canonical записи pratyāhāra для цих прикладів — `ac`, `ik`, `ec`, `yaR`,
`hal` у SLP1. Верхній регістр не можна замінювати довільно: `S` і `z`, `Q` і
`q`, `C` і `c` — різні SLP1 symbols.

Вектор ще не є versioned edition manifest. Він має статус
`source-checked-test-vectors`, а machine input потребує наступного кроку:
ліцензійно й revision-ідентифікованого source artifact з hash, як вимагає
`pratyahara-set-provenance.md`.

### [INTERPRETATION]

`hal` показує важливу межу формалізації. Лінійний scan від першого `h` до
marker `l` проходить через ще один `h` у рядку 14. Для алгоритму це
`expected_stream` з двома occurrence; для фонемної належності — `expected_set`
з одним `h`. Реалізація мусить оголосити, який саме результат вона повертає;
не можна непомітно вважати list, multiset і set одним типом.

Так само `start_sound` із повторюваною appearance не може резолвитися за
принципом «перший збіг» без explicit policy. Negative vector `hR` навмисно
вимагає такої policy замість припущення.

### [MY-LISP HYPOTHESIS]

Майбутній expander приймає:

```yaml
input: { start_sound: <SLP1>, end_marker: <SLP1> }
source: { manifest_id: <versioned-id>, sha256: <digest> }
mode: ordered-stream | unique-set
```

і повертає `error:unknown-it-marker`, `error:ambiguous-start` або явний
результат. Він не читає pre-generated `AC`/`HAL` globals як джерело істини.

#### Негативні acceptance tests

1. marker `c` не входить до expansion `ac`.
2. `G Q D [z]` не нормалізується до `G q D [S]`.
3. `j b g q d [S]` не нормалізується до marker `z`.
4. `hal` має або ordered stream з повторним `h`, або unique set без дубліката;
   API не має маскувати вибір.
5. До проходження цих tests `panini/machine/siva-sutras.my` лишається
   experimental artifact і не є source evidence.

Пов'язані матеріали: `pratyahara-exhaustive-v0.1.yaml`,
`pratyahara-set-provenance.md`, `foundation/pratyahara.md`,
`derivation-ir-v0.1.md`.

## Deutsch

Die Vektoren trennen Laute von it-Markern sowie linearen Scan von
Set-Mitgliedschaft. Insbesondere lauten die kritischen SLP1-Zeilen 9–11
`G Q D [z]`, `j b g q d [S]`, `K P C W T c w t [v]`. Ein künftiger Expander
muss versionierte Quellen mit Hash verwenden und explizit zwischen
ordered-stream und unique-set unterscheiden. Die ukrainische Fassung ist
normativ.
