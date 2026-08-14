# Сутність, `saMjYA` і лексична назва: межа представлення

## English

### Thesis

The foundation must not collapse the carrier of a condition, a `saMjYA`, the
lexical spelling of its name, and an implementation tag. A designation may be
relevant only under a scope and conditions; the field name of a data model
cannot decide coexistence or displacement of designations.

### [PANINI]

This note uses 1.4.1 (`A kaDArAdeka saMjYA`) only for the narrow source-facing
observation that technical designations have applicability conditions and
scope. It does not claim that every `saMjYA` is temporary, exclusive, or a
modern type.

### [INTERPRETATION]

Keep four layers apart: an occurrence/carrier, a `saMjYA`, a canonical SLP1
lexical entry, and an implementation state such as a tag or enum. A useful
record names the designated occurrence, its defining rule, conditions,
provenance, and status. `type: kartf` alone loses that information.

### [MY-LISP HYPOTHESIS]

`Symbol("kartf")`, an enum, or an AST edge may be engineering representations,
but none proves Paninian designation in an example. A surface `:kartf` may be
syntax; canonical vocabulary remains `kartf`; only an evidence-bound trace may
assert application in context. Do not define `it = metadata`, `kartf = subject`,
or a global one-tag rule from `eka-saMjYA`.

## Українська

## Теза

У foundation не можна ототожнювати:

```text
сутність / носій умови  ≠  saMjYA  ≠  написання її назви  ≠  runtime tag
```

Це не абстрактна пересторога. В 1.4.1 Panini прямо регулює ситуації, коли
до одного носія застосовні кілька `saMjYA`; отже, `saMjYA` не можна моделювати
лише як незмінний intrinsic type об'єкта.

## [PANINI]

1.4.1 `A kaDArAdeka saMjYA` є `aDikAra` для режиму `eka-saMjYA`. Цифрове
видання пояснює його через співвідношення між попереднім і пізнішим
позначенням за умовою застосовності; це робить важливими не тільки слово,
а також scope, порядок і конфлікт позначень.
[Aṣṭādhyāyī 1.4.1](https://ashtadhyayi.com/sutraani/1/4/1)

Звідси випливають лише такі мінімальні твердження:

- `saMjYA` — технічне позначення, на яке можуть посилатися правила;
- умови його застосовності та область дії є частиною доказу;
- той самий носій може бути предметом кількох designation-правил, а їхнє
  співіснування чи витіснення не можна вирішувати назвою поля в data model.

Це не твердження, що кожна `saMjYA` завжди тимчасова, взаємовиключна або
еквівалентна сучасному «типу».

## [INTERPRETATION]

Для registry та trace корисно розрізняти чотири шари:

| Шар | Приклад | Що він не означає |
| --- | --- | --- |
| Носій / term | конкретний `upadeSa` або учасник дії | Не є назвою його класу. |
| `saMjYA` | `it`, `kartf`, `upasarga` | Не є автоматично Unicode/SLP1 symbol. |
| Лексичний запис | канонічний SLP1 `kartf` | Не доводить застосовність designation. |
| Внутрішній стан реалізації | tag, enum, AST field | Не є панініївською категорією без trace. |

У машині корисно вести окремий запис призначення:

```yaml
designation:
  canonical: kartf
  assigned_to: term-or-relation-id
  defined_by:
    - sutra: "1.4.54"
  conditions: []
  status: asserted
```

Це не обов'язкова реалізаційна схема; вона показує, яку інформацію губить
просте `type: kartf`.

## [MY-LISP HYPOTHESIS]

У My Lisp `Symbol("kartf")`, enum `Karaka::Kartr` і AST edge з role `kartf`
можуть бути корисними інженерними представленнями. Але жодне з них саме по
собі не стверджує, що Panini надав конкретному носієві `kartf`-saMjYA.

Тому межа для P5/P4 така:

1. surface `:kartf` може бути syntax marker;
2. canonical vocabulary ID має бути `kartf` без `:`;
3. AST validation може перевіряти зареєстрований ID;
4. лише evidence-bound derivation може стверджувати застосування відповідної
   `saMjYA` у конкретному прикладі.

## Практичні заборони

- Не записувати `it = metadata`, `kartf = subject` або `upasarga = prefix` як
  визначення.
- Не зливати `canonical` лексичного registry-запису з фактом designation.
- Не зберігати рішення `eka-saMjYA` як глобальну заборону на кілька tags без
  зафіксованих scope і rule conditions.

## Deutsch

### These

Das Fundament darf Träger einer Bedingung, `saMjYA`, lexikalische Schreibung
ihres Namens und Implementierungstag nicht zusammenfallen lassen. Eine
Designation kann nur unter Scope und Bedingungen relevant sein; ein Feldname
des Datenmodells entscheidet weder Koexistenz noch Verdrängung von
Designations.

### [PANINI]

Diese Notiz verwendet 1.4.1 (`A kaDArAdeka saMjYA`) nur für die enge
quellennahe Beobachtung, dass technische Designations
Anwendbarkeitsbedingungen und Scope besitzen. Sie behauptet nicht, jede
`saMjYA` sei temporär, exklusiv oder ein moderner Typ.

### [INTERPRETATION]

Vier Ebenen bleiben getrennt: Vorkommen/Träger, `saMjYA`, kanonischer
SLP1-Lexikoneintrag und Implementierungszustand wie Tag oder Enum. Ein
nützlicher Record nennt das designierte Vorkommen, definierende Regel,
Bedingungen, Provenance und Status. `type: kartf` allein verliert diese
Information.

### [MY-LISP HYPOTHESIS]

`Symbol("kartf")`, Enum oder AST-Kante können Engineering-Repräsentationen
sein, beweisen aber keine paninische Designation. `:kartf` kann Syntax sein,
der kanonische Wortschatz bleibt `kartf`; nur ein evidenzgebundener Trace darf
Anwendung im Kontext behaupten. `it = metadata`, `kartf = subject` und eine
globale Ein-Tag-Regel aus `eka-saMjYA` bleiben unzulässig.

## Висновок

Foundation повинен зберігати vocabulary та докази призначення окремо. Це
дозволяє майбутній машинній моделі експериментувати з type/tag/edge дизайном,
не переписуючи ці рішення як історичні факти про Panini.
