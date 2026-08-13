# `Slu → dvirvacana` для `dadAti`: джерельний аудит

Статус: `partial`. Аудит закриває вузький міст від `Slu` у 2.4.75 до
подвоєння в 6.1.10. Він не завершує деривацію `dadAti`, не встановлює
`abhyAsa`-designation і не додає scheduler.

## English

The source record for 2.4.75 explicitly gives `Slu` for `Sap` after
`juhotyAdi`. Its Kāśikā material states that the `Slu` provision is for
`dvirvacana`, and cites `Slau` (6.1.10) in the explanation. This admits a
bounded source transition from the source-path `Slu` marker to a distinct
reduplicated occurrence. It does not yet establish later designation, hrasva,
or surface assembly.

## Українська

### [PANINI]

2.4.75 `juhotyAdibhyaH SluH` задає `Slu` для `Sap` після `juhotyAdi`.
Коментар Kāśikā, доступний разом із цією sūtra, пояснює `Slu` як постанову
заради `dvirvacana` і прямо згадує `Slau` 6.1.10. Отже, для `dA` із
зафіксованим `juhotyAdi`-контекстом є достатня джерельна підстава для
обмеженого твердження:

```text
dA + Slu + ti
  → dA(reduplicated occurrence) + dA + Slu + ti
```

Це не означає, що `Slu` є surface-рядком, що сучасний IR відтворює текстову
операцію буквально, або що результат уже має designation `abhyAsa`.

Джерело: [2.4.75 з anuvṛtti та Kāśikā-коментарем](https://sanskritdictionary.com/panini/2-4-75).
У доступному коментарі наведено формулу `ślau ... dvirvacanārtham` і приклад
`juhoti`; це підтримує саме міст до подвоєння, не всі пізніші етапи.

### [INTERPRETATION]

Мінімальний immutable IR-перехід створює **новий occurrence**, а не мутує
`term:root-dA`:

```yaml
before: state:fixture:dadati:slu
rule: "6.1.10"
after: state:fixture:dadati:dvirvacana
operation: create-reduplicated-root-occurrence
relation:
  from: term:root-dA
  to: term:reduplicated-dA
  kind: implementation
```

Термін `reduplicated-dA` навмисно не названо `abhyasa-dA`: 6.1.4 і конкретне
призначення `abhyAsa` мають залишитися наступною evidence-перевіркою.

### [MY-LISP HYPOTHESIS]

Цей результат виправдовує тільки загальну machine-вимогу: structural
duplication створює окремий identity-bearing occurrence і provenance relation.
Він не виправдовує My Lisp primitive `duplicate-root`, глобальний порядок
правил чи переведення `Slu` в runtime tag без окремого contract.

## Незакриті межі

1. 6.1.4: який саме occurrence отримує `abhyAsa`-designation.
2. 7.4.59: умови та typed hrasva operation.
3. Побудова surface `dadAti` з immutable state.
4. Повний lakāra/tiṅ prefix і всі його conditions.

## Deutsch

Die Kāśikā-Erklärung zu 2.4.75 verbindet `Slu` ausdrücklich mit
`dvirvacana` und verweist auf 6.1.10. Dadurch ist ein begrenzter Übergang zu
einem separaten reduplizierten Term-Vorfall belegt, nicht jedoch `abhyAsa`,
hrasva oder die vollständige Oberflächenform `dadAti`.
