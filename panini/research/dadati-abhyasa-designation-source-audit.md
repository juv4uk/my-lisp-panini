# `abhyAsa` designation for `dadAti`: source audit

Status: `partial`. This audit closes only the source bridge from the
reduplicated occurrence established under 6.1.10 to its `abhyAsa` designation
under 6.1.4. It does not establish hrasva under 7.4.59 or a complete surface
derivation of `dadAti`.

## English

Pāṇini 6.1.4, `pUrvo'BhyAsaH`, is a saMjYA rule. Its inherited context is the
locally relevant pair of replacements. The source record and its Kāśikā
commentary state that the first member of that pair receives the technical
designation `abhyAsa`; `juhoti` appears among the examples. This supports a
bounded transition after the independently recorded `Slu → dvirvacana` bridge:
the prior, distinct reduplicated occurrence receives a designation. It does
not authorize changing that occurrence's surface form.

## Українська

### [PANINI]

6.1.4 `pUrvo'BhyAsaH` позначено як правило `saMjYA`. З anuvṛtti воно діє в
релевантному тут контексті двох елементів, установлених подвоєнням. Джерельний
запис і Kāśikā пояснюють: перший із цієї пари отримує технічну назву
`abhyAsa`; серед наведених прикладів є `juhoti`. Отже, після окремо
зафіксованого мосту `Slu → dvirvacana` джерела підтримують вузьке твердження:
попередній окремий occurrence одержує designation `abhyAsa`.

Джерело: [Aṣṭādhyāyī 6.1.4 з anuvṛtti й традиційними коментарями](https://sanskritdictionary.com/panini/6-1-4).
Сторінка наводить текст `pUrvo'BhyAsaH`, класифікує його як `saMjYA`, а Kāśikā
визначає перший член двох установлених елементів як `abhyAsa`.

### [INTERPRETATION]

У fixture це не створює третій кореневий term і не мутує `term:root-dA`.
Натомість у новому immutable state той самий `term:reduplicated-dA`, створений
попереднім переходом 6.1.10, має relation до `designation:abhyAsa`:

```yaml
before: state:fixture:dadati:dvirvacana
rule: "6.1.4"
after: state:fixture:dadati:abhyasa
operation: attach-abhyasa-designation-to-prior-reduplicated-occurrence
```

`attach-...` — назва операції IR, а не переклад формулювання sūtra. Вона
відокремлює identity occurrence від його source/surface form і від designation.

### [MY-LISP HYPOTHESIS]

Цей результат підтримує лише загальну вимогу: scoped designation може бути
додана до незмінного occurrence без переписування його identity чи surface
representation. Він не доводить, що `abhyAsa` є типом, тегом або primitive My
Lisp; таке рішення потребує корпусу незалежних деривацій.

## Незакриті межі

1. Умови й точна операція 7.4.59 для hrasva.
2. Подальші фонологічні та морфологічні переходи до `dadAti`.
3. Повний lakAra/tiṅ context і його умови.
4. Виконувана типізована операція IR для designation.

## Deutsch

6.1.4 `pUrvo'BhyAsaH` ist eine `saMjYA`-Regel. Der Quelleneintrag und der
Kāśikā-Kommentar bestimmen im einschlägigen Paar den ersten Bestandteil als
`abhyAsa`; `juhoti` wird als Beispiel genannt. Deshalb darf das Fixture nach
dem belegten Übergang `Slu → dvirvacana` dem früheren reduplizierten Vorfall
eine Designation zuordnen. Weder hrasva noch die endgültige Oberflächenform
`dadAti` sind damit belegt.
