# Coverage sūtra-цитат для registry `saMjYA`

## Знімок

Дата перевірки: 2026-08-13. Registry `panini/registry/samjna/` містить один
машинний запис: `prAtipadika.yaml`.

| Запис | `defined_by` | Citation provenance | Коментарний/інтерпретаційний шар | Висновок |
| --- | --- | --- | --- | --- |
| `prAtipadika` | 1.2.45, 1.2.46 | обидва `corpus-checked` | foundation note містить caveats і посилання на локальну політику corpus | Покриття прямими sūtra є достатнім для поточного вузького registry-запису. |

Це **не** означає, що всі saMjYA, описані у foundation, уже мають registry
records. Воно означає лише, що наявний registry не містить записи без прямої
цитати.

## Метод

Перевірка зіставляє:

1. `registry/samjna/*.yaml` → `defined_by[].sutra`;
2. наявність ID у `registry/sutras/index.yaml`;
3. запис у `registry/sutras/citation-provenance.yaml`;
4. status provenance та шлях у `used_by`.

Описовий range на кшталт `it range 1.3.2-1.3.9` не вважається прямою
цитатою. Для machine use він має розкладатися на окремі IDs.

## [PANINI]

`prAtipadika` у цьому registry має два прямі посилання — 1.2.45 і 1.2.46.
Вони обидва присутні в committed sūtra index і позначені `corpus-checked` у
citation provenance registry. Це підтверджує provenance самих посилань, але
не робить усі пояснення в полях registry буквальним текстом sūtra.

## [INTERPRETATION]

Висновки, які виходять за текст 1.2.45–46 (наприклад, про machine relevance
або межу object/metalevel), мусять лишатися в foundation/research документах
і бути марковані відповідним рівнем. Registry має бути компактним індексом
джерел, а не контейнером неперевіреної теорії.

## Прогалини

| Кандидат `saMjYA` | Стан | Наступна вимога |
| --- | --- | --- |
| `it` | Є дослідницька матриця 1.3.2–1.3.9, але немає registry-запису. | Створити лише після direct-citation manifest для всіх заявлених rules. |
| `upasarga` | Є crosswalk 1.4.58–59, але немає registry-запису. | Спочатку завершити versioned `prAdi-gaNa` source import. |
| `kAraka` | Представлений окремим registry, не `samjna/`. | Не дублювати: спершу визначити, чи потрібен meta-record, а не ще одна копія. |
| `pratyAhAra` | Описаний у foundation, registry-запису немає. | Вимагає окремої source policy для Śiva Sūtras і it markers. |

## Рекомендація

Не збільшувати `samjna/` заради чисельності. Наступний запис додається лише
з canonical SLP1, direct `defined_by` IDs, citation-provenance entries і
окремим визначенням межі між [PANINI] та [MY-LISP HYPOTHESIS].
