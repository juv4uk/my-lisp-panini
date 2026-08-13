# `hrasva` after `abhyAsa` in `dadAti`: source audit

Status: `partial`. This audit establishes the narrow rule-level bridge from an
already designated `abhyAsa` to vowel shortening under 7.4.59. It does not
establish every condition of the full `dadAti` derivation, rule ordering beyond
this local step, or final surface assembly.

## English

Pāṇini 7.4.59, `hrasvaH`, inherits `abhyAsasya` from 7.4.58. The accessible
source record classifies it as a `vidhi` rule and describes a short vowel as a
substitute for the vowel of an `abhyAsa`. Its Kāśikā commentary likewise says
that shortening occurs for `abhyAsa`. Given the separately verified 6.1.4
designation in this fixture, the candidate `dA → da` is source-supported as a
local hrasva operation. The source does not make the fixture's IR operation
name, state shape, or eventual `dadAti` result canonical.

## Українська

### [PANINI]

7.4.59 `hrasvaH` успадковує `abhyAsasya` з 7.4.58. Доступний джерельний запис
класифікує sūtra як `vidhi` і пояснює, що короткий голосний замінює голосний
`abhyAsa`; Kāśikā так само формулює скорочення для `abhyAsa`. Оскільки
fixture окремо перевірив designation за 6.1.4, локальний крок-кандидат
`dA → da` має джерельну підтримку як hrasva-операція.

Джерело: [Aṣṭādhyāyī 7.4.59 та традиційні коментарі](https://sanskritdictionary.com/panini/7-4-59).
Пошуковий запис цієї сторінки подає anuvṛtti `abhyAsasya` з 7.4.58, тип
`vidhi`, переклад про short vowel у reduplicate та Kāśikā-коментар
`hrasvo bhavati abhyAsasya`.

### [INTERPRETATION]

Для immutable IR безпечним є лише явний перехід від designated occurrence до
окремого результату з `source_form: dA` і `surface_form: da`, з provenance
7.4.59. Чи має результат зберігати тотожний ID, чи бути новим occurrence із
relation переходу, є питанням машинної моделі; sūtra цього формату не задає.
Тому чинний fixture не оголошується завершеною executable derivation лише на
цій підставі.

### [MY-LISP HYPOTHESIS]

Урок обмежений: правило може бути джерельно застосовним до designation, але
формат immutable transition усе одно залишається рішенням машини. Це не
обґрунтовує primitive для заміни символів у My Lisp і не дозволяє зводити
панініївську операцію до глобального rewrite без її scope та provenance.

## Незакриті межі

1. Повний набір умов, винятків і взаємодій 7.4.59 в деривації `dadAti`.
2. Машинний identity-contract для результату `dA → da`.
3. Наступні переходи до фінальної surface form `dadAti`.
4. Повний доказ порядку правил для end-to-end trace.

## Deutsch

7.4.59 `hrasvaH` übernimmt `abhyAsasya` aus 7.4.58. Der Quelleneintrag
bezeichnet die Regel als `vidhi`; der Kāśikā-Kommentar beschreibt die
Kürzung des Vokals eines `abhyAsa`. Nach der separat belegten Designation aus
6.1.4 ist `dA → da` daher als lokaler hrasva-Schritt quellenbasiert. Weder die
IR-Identität noch die endgültige Oberflächenform `dadAti` folgen daraus.
