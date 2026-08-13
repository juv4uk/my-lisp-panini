# Межа `avyaya`, `nipAta` та `upasarga`

Статус: завершено (`PANINI-AVYAYA-BOUNDARY-RESEARCH`).

## Висновок

Не існує підстав моделювати всі «невідмінювані» слова одним незмінним машинним
типом. `avyaya` і `nipAta` — різні `saMjYA` з частковим перетином, а один
лексичний елемент зі списку `prAdi` може одержувати `nipAta` або `upasarga`
залежно від контексту `kriyAyoga`.

## [PANINI]

| Категорія | Джерело | Мінімальний зміст |
|---|---|---|
| `avyaya` | 1.1.37 `svarAdinipAtam avyayam` | `svarAdi` та `nipAta` отримують `avyaya-saMjYA` |
| `avyaya` | 1.1.38 `taddhitaS cAsarvavibhaktiH` | до попереднього додано відповідні taddhita-форми |
| `nipAta` | 1.4.56 `prAg rIzvarAn nipAtaH` | заголовок ділянки, де працює позначення `nipAta` |
| `nipAta` | 1.4.57 `cAdayo 'sattve` | `cAdi` пов'язано з `nipAta` за умови `asattva` |
| `nipAta` | 1.4.58 `prAdayaH` | `prAdi` отримує відповідне позначення через контекст попередніх sūtra |
| `upasarga` | 1.4.59 `upasargAH kriyAyoge` | `prAdi` отримує `upasarga-saMjYA` у зв'язку з дією |

Отже, 1.1.37 не стверджує `avyaya = nipAta`: він об'єднує щонайменше
`svarAdi` та `nipAta`. 1.1.38 додає ще іншу умову для taddhita. Зворотне
включення (`avyaya` → `nipAta`) з цих sūtra не випливає.

Для `prAdi` не слід створювати два лексикони. Той самий запис може нести різні
контекстні категорії. Сам текст sūtra 1.4.59 дає лише умову `kriyAyoga`; він
не визначає сучасний машинний механізм розбору цього зв'язку.

## [INTERPRETATION]

Переклад `avyaya` як «невідмінюване» може допомагати читанню, але не є повною
онтологією. Коментарі до 1.1.37 пояснюють призначення `avyaya-saMjYA` через
незміну за граматичними категоріями, водночас перелік `svarAdi` має
ākṛtigaṇa-аспект. Тому твердження «це замкнений список» не можна записувати
як універсальний факт v0.1.

Так само `nipAta` не слід зводити до англійського *particle*: 1.4.57 дає
умову `asattva` для `cAdi`, а 1.4.58–59 показують функціонально залежне
позначення `prAdi`. Потрібен окремий аналіз кожного правила та списку.

## [MY-LISP HYPOTHESIS]

Майбутній реєстр може тримати лексичний запис і відокремлені контекстні
позначення:

```yaml
lexical_family: prAdi
contextual_designations:
  - { designation: nipAta, source: "1.4.58", condition: inherited-context }
  - { designation: upasarga, source: "1.4.59", condition: kriyAyoga }
```

Це лише архітектурна гіпотеза. Заборонені скорочення: `avyaya = one token
type`, `nipAta = particle`, `prAdi = always prefix`, `upasarga = lexical
string without context`.

## Виправлення попередньої нотатки

`foundation/nipata-avyaya.md` раніше називала `nipAta` «закритим лексичним
класом» і без достатньої обмовки описувала `avyaya` як клас слів, що не
відмінюються. Ці формули потрібно читати лише як неперевірену інтерпретацію,
не як дані для registry або VM. Ця нотатка має пріоритет для меж категорій.

## Джерела

- [Aṣṭādhyāyī.com: 1.1.37 та коментарі](https://ashtadhyayi.com/sutraani/1/1/37)
  — текст, Kāśikā та явне позначення `avyaya-saMjYA`.
- [Sanskrit Dictionary: 1.1.37](https://sanskritdictionary.com/panini/1-1-37)
  — незалежна навігація до тексту й коментарів.
- [Aṣṭādhyāyī GitHub: 1.4](https://ashtadhyayi.github.io/suutra/1.4/)
  — послідовність 1.4.56–59.
- `registry/sutras/index.yaml` — локальні записи; їхній статус і межі описано
  у `research/sutra-local-corpus-provenance.md`.
