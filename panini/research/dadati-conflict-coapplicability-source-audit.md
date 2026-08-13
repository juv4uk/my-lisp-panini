# Аудит спільної застосовності 2.4.72 і 2.4.75 для `dA`

Статус: `partial`. Це джерельний аудит для
`PANINI-DADATI-CONFLICT-COAPPLICABILITY-SOURCE-AUDIT`, а не підтвердження
універсального scheduler, не виконання машини й не повна деривація `dadAti`.

## [PANINI]

`dA` у нашому реєстрі належить до `juhotyAdi`. Sūtra 2.4.72
`adiprabhRtibhyaH SapaH` подається з успадкованим `luk`; доступний
коментарієвий матеріал описує його як `luk` для `Sap` після коренів групи
`adAdi`. Натомість 2.4.75 `juhotyAdibhyaH SluH` має успадковані `SapaH` і
`luk`, але встановлює `Slu` для `Sap` після `juhotyAdi`.

Важлива негативна знахідка: коментар на сторінці 2.4.75 прямо пояснює, що
`adiprabhRtibhyaH` **не** переноситься до 2.4.75. Тому сама текстова
близькість 2.4.72 і 2.4.75 не дає підстави вважати `dA` членом обох
операндів. У зафіксованому випадку є позитивна джерельна підстава для 2.4.75
та негативна межа для прямої застосовності 2.4.72.

Джерела: [2.4.72: текст, `luk` через anuvṛtti, `adAdi`-пояснення](https://sanskritdictionary.com/panini/2-4-72),
[2.4.75: текст, `SapaH`/`luk` через anuvṛtti і коментар](https://sanskritdictionary.com/panini/2-4-75).

## [INTERPRETATION]

Це не доводить загальну теорію про всі відношення `utsarga`/`apavAda` між
сусідніми sūtra. Воно встановлює скромніше й машинно важливіше твердження:
для поточного `dA`-прикладу не слід створювати `conflict-resolved` з
кандидатами 2.4.72 та 2.4.75, доки окреме традиційне джерело не обґрунтує
спільну застосовність саме для цієї ситуації.

Наявний `dadati-apavada-conflict-v0.1.yaml` отже лишається корисним
контрфактичним **machine harness**. Його relation `apavAda > utsarga` є
властивістю профілю реалізації, а не результатом цього аудиту.

## [MY-LISP HYPOTHESIS]

У майбутньому IR має відрізняти щонайменше:

```text
source candidate      — підтверджено застосовний джерелом;
machine candidate     — введено для тесту профілю реалізації;
counterfactual pair   — корисний тест, але не історичний доказ.
```

Не можна отримувати candidate set лише з `:utsarga` поля або сусідства номерів
sūtra. Candidate set повинен мати власний provenance; лише після цього
дозволене conflict policy.

## Висновок / Conclusion / Schlussfolgerung

| Питання | Результат |
| --- | --- |
| Чи є 2.4.75 джерельним кандидатом для `dA` (`juhotyAdi`)? | `yes`, у межі перевіреної умови `Sap`. |
| Чи є 2.4.72 прямим джерельним кандидатом для цього `dA`? | `no evidence`; наявний коментар вказує на `adAdi`-межу. |
| Чи дозволений source-level conflict event 2.4.72 vs 2.4.75? | `no`, не в поточному прикладі. |
| Чи можна зберегти machine conflict harness? | `yes`, тільки з namespace `machine` і статусом `partial`. |

English: the audit rejects treating 2.4.72 and 2.4.75 as source-co-applicable
to the current `dA` case. German: Der Audit verwirft ihre quellenbasierte
Gleichanwendbarkeit im aktuellen `dA`-Fall.
