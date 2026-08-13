# Tripādī: rule-exception audit for machine scheduling

Status: `PANINI-TRIPADI-RULE-EXCEPTION-AUDIT`. This corrects an unsafe
oversimplification in earlier project notes: Tripādī cannot be represented
responsibly as an unconditional one-pass numeric loop.

## English summary

8.2.1 `pūrvatrāsiddham` is the textual anchor for an asiddha relation over the
later portion of the grammar, but commentarial presentations also discuss
exceptions and same-topic behavior. A future engine therefore needs an explicit
visibility relation with provenance, not merely `for rule in sorted(rules)`.
The Ukrainian section is normative.

## Українська

### [PANINI]

Sūtra 8.2.1 `pUrvatrAsidDam` є текстовою точкою входу для `asiddha`-механізму
у пізній частині Aṣṭādhyāyī. Доступні цифрові коментарні матеріали подають її
як adhikāra до кінця adhyāya та описують відношення Tripādī до попередньої
частини граматики. Це **не** тотожне текстовому твердженню, що будь-які два
правила 8.2–8.4 завжди виконуються однією простою numeric loop без винятку.

### [INTERPRETATION]

Два незалежні коментарні presentation layers додають важливі межі:

1. `pūrvatrāsiddham` читається як asiddha/visibility relation щодо попередніх
   правил, а не як звичайна команда «ніколи не повертайся назад».
2. Ashtadhyayi.com окремо застерігає, що Tripādī sūtras одного `prakaraṇa`
   можуть бути `siddha` щодо одне одного. Отже, саме належність до section і
   числовий порядок не вичерпують relation.
3. Коментарна сторінка для 8.2.1 на SanskritDictionary наводить додаткові
   обмеження, зокрема винятки, пов'язані з типом rule relation/condition.

Ці матеріали є інтерпретаційними джерелами, не заміною критичного видання чи
повного коментарного аудиту. Але їх достатньо, щоб відхилити сильне раннє
твердження в `tripadi-scope-investigation.md`, ніби strict single pass вже
доведений як універсальна семантика.

### [MY-LISP HYPOTHESIS]

#### Безпечний scheduler contract

Майбутній rule engine не повинен кодувати Tripādī лише так:

```text
for rule in rules.sorted_by_sutra_number(): apply(rule)
```

Замість цього кожна перевірка видимості потребує явного record:

```yaml
visibility_relation:
  later_rule: <sutra-or-machine-ID>
  earlier_rule: <sutra-or-machine-ID>
  scope: tripadi | same-prakarana | cross-section | unknown
  status: asiddha | siddha | exception | unresolved
  basis: sutra | commentary | implementation-policy
  provenance: [prov:<stable-id>]
```

Rule scheduler може використати numeric order лише як **один вхід** у policy;
він не може видати `complete` trace, якщо visibility relation не відома або
якщо її замінила необґрунтована fallback-евристика.

#### Мінімальні negative tests

1. Два rule IDs з 8.2–8.4 без explicit visibility record не дають права
   автоматично оголосити `later-wins`.
2. Rule pair, позначена `same-prakarana`, не успадковує generic `asiddha`
   result без окремого джерельного/коментарного record.
3. `asiddha` relation не перетворюється на deletion попередньої state history:
   trace зберігає state, але policy може обмежити його видимість для іншого
   rule check.
4. Legacy numeric-loop execution має `trace_status: partial` до появи
   per-relation provenance.

#### Архітектурний наслідок

Derivation IR уже має `scope`, `conditions`, `rule-decision` і
`conflict-resolved`. Для Tripādī потрібна ще одна явно типізована грань:
`visibility_relation`. Вона відрізняється від conflict priority: `asiddha`
відповідає на питання «який state/rule effect видно під час check», тоді як
`conflict-resolved` відповідає «який із одночасно застосовних candidates
обрано». Злиття цих двох питань у `vipratiSeDa` або numeric loop було б
архітектурною помилкою.

### Рішення й наступний gate

1. Ранній документ `tripadi-scope-investigation.md` лишається історичним
   exploration artifact; його strict-loop VM-висновок не є foundation contract.
2. До `PANINI-TRIPADI-VISIBILITY-RELATION-SCHEMA` заборонено оголошувати
   Tripādī scheduler complete.
3. Перший executable prototype мусить мати мінімум один explicit exception
   fixture і один `unresolved` case; він не може приховати їх fallback order.

Джерела: [8.2.1 і коментарний огляд на SanskritDictionary](https://sanskritdictionary.com/panini/8-2-1),
[Tripādī discussion on Ashtadhyayi.com](https://ashtadhyayi.com/sutraani/ssk31),
[навчальне пояснення asiddha rules](https://learnsanskrit.org/vyakarana/sounds/asiddha-rules/).

Пов'язані локальні матеріали: `tripadi-scope-investigation.md`,
`foundation/rule-system.md`, `derivation-ir-v0.1.md`,
`derivation-ir-trace-events-v0.1.md`.

## Deutsch

8.2.1 liefert einen Anker für eine asiddha-Sichtbarkeitsrelation, aber keine
vollständige Rechtfertigung einer bedingungslosen numerischen Ein-Pass-Schleife.
Kommentarische Darstellungen erwähnen same-prakaraṇa- und weitere Ausnahmen.
Ein künftiger Scheduler braucht daher provenienzgebundene
`visibility_relation`-Datensätze, getrennt von Konfliktpriorität. Die
ukrainische Fassung ist normativ.
