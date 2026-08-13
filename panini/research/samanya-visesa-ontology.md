# Sāmānya / Viśeṣa — Universal і Particular у системі Паніні

Статус: виконано (`PHILOSOPHY-SAMANYA-VISESA-ONTOLOGY`)  
Автор: my-lisp-panini-1 · 2026-08-13  
Зв'язок: → `PANINI-SAMJNA-AS-CATEGORIZATION-NOT-JUST-TAG`, → `PANINI-TWO-INSTANCE-RELATIONSHIP-RESEARCH`

---

## Центральне питання

Індійська філософська традиція (особливо Nyāya-Vaiśeṣika) фундаментально
розрізняє:

- **sāmānya** (सामान्य) — загальне, universal, клас, рід
- **viśeṣa** (विशेष) — особливе, particular, індивід, відмінна риса

Питання: чи відтворює система Паніні цю онтологічну пару, і якщо так —
де саме і як?

---

## [PANINI] Де проходить межа у граматичній системі

### saMjYā = sāmānya у дії

`saMjYā`-механізм робить рівно те, що онтологічно визначає `sāmānya`:
**встановлює клас** (universal), якому можуть належати конкретні об'єкти
(particulars).

Приклад:
- Universal (sāmānya): клас `guRa` = {a, e, o} — введений sūtra 1.1.2
- Particular (viśeṣa): конкретний звук `e` у поточному кроці деривації
- Відношення: `e` є `guRa` (belongs-to, не is-identical-to)

Друга ілюстрація через `kāraka`:
- Universal: клас `kartf` — визначений критерієм "незалежний ініціатор"
  (sūtra 1.4.54 `svatantraH kartā`)
- Particular: конкретний `devadatta` у реченні `devadatto gacchati`
- Відношення: `devadatta` є `kartf` в **цьому конкретному реченні** —
  не завжди і не за властивістю самого `devadatta`

Це ключова відмінність від тегу: `devadatta` не "tagged" як `kartf`
назавжди — він задовольняє критерій `kartf` ситуативно.

### Паніні і Nyāya-Vaiśeṣika — пряма традиційна спорідненість

Традиційні коментатори (Patañjali у Mahābhāṣya) явно використовують
поняття `sāmānya`/`viśeṣa` при поясненні граматики. Граматична традиція
і ньяйська онтологічна традиція розвивались паралельно і взаємозалежно.

Це не інтерпретація — це задокументований факт індійської інтелектуальної
історії. (Конкретні посилання: Mahābhāṣya Patañjali ad 1.1.1; Staal 1966
"Word Order in Sanskrit and Universal Grammar".)

---

## [INTERPRETATION] Три рівні відношення universal–particular у Паніні

### Рівень 1: Фонологічний
- Universal: pratyāhāra (`AC` = всі голосні)
- Particular: конкретний звук `a`/`i`/`u`/...
- Механізм членства: звук входить до праtяхари за позицією у Śiva-sūtra

### Рівень 2: Морфологічний
- Universal: `saMjYā`-клас (`guRa`, `vfdDi`, `sarvanAma`)
- Particular: конкретна форма або слово (`e`, `sarva`)
- Механізм членства: перелік або морфологічна поведінка

### Рівень 3: Семантико-синтаксичний
- Universal: `kāraka`-роль (`kartf`, `karman`)
- Particular: іменний елемент у конкретному реченні
- Механізм членства: **предикат**, перевірюваний у реченні

Три рівні використовують один інструмент (`saMjYā`) для різних типів
відношення universal–particular.

---

## [MY-LISP HYPOTHESIS] Наслідки для типової системи VM

### Проблема поточної реалізації

У `panini-core.my` та `rules.my` немає розрізнення між:
- universal-класом (тип, клас, категорія)
- particular-об'єктом (конкретний term, конкретний звук)
- відношенням між ними (belongs-to, satisfies-criterion)

`term-add-tag` реалізує щось між: додає ім'я класу як атрибут терма,
але без будь-якої перевірки критерію членства.

### Гіпотетична архітектура

```
Universal (sāmānya):
  (defsamjna 'guRa '(a e o))           ;; перелічуваний клас
  (defsamjna 'kartf (lambda (x ctx) ;; предикатний клас
    (is-independent-agent? x ctx)))

Particular (viśeṣa):
  конкретний Term у Prakriyā

Відношення:
  (samjna? term 'guRa ctx)             ;; перевіряє членство
```

Це суттєво інша архітектура, ніж `term-add-tag`. Але вона дорожча
обчислювально і складніша в реалізації.

### Прагматичне рішення для v0.1

Для `derive-Bavati` поточний `term-add-tag` є достатнім — там немає
предикатних класів, лише перелічувані. Переходити на повну
universal/particular архітектуру варто при реалізації `kāraka`-аналізу
речення (не деривації).

**Це зафіксовано як архітектурний розрив між v0.1 і майбутнім
sentence-analysis шаром.**

---

## Відкриті питання

1. Чи є sāmānya/viśeṣa у Паніні лише термінологічним збігом із
   Nyāya, чи це глибша онтологічна спільність? Вимагає окремого
   дослідження первинних коментарів.

2. `PANINI-TWO-INSTANCE-RELATIONSHIP-RESEARCH`: якщо `devadatta` є
   `kartf` ситуативно (particular відповідає universal у контексті) —
   то що є "instance" у граматичній системі? Речення? Деривація? Крок?

3. Для `PANINI-SAMJNA-MACHINE-REPR-REDESIGN`: перелічуваний vs.
   предикатний клас потребують різних структур даних. Гібридна
   реалізація (`defsamjna` з optional predicate) — кандидат.

---

## Джерела

- Традиція Nyāya-Vaiśeṣika: Padārthadharmasaṃgraha Praśastapāda
  (класичне джерело sāmānya/viśeṣa) — не перевірено безпосередньо
  у цій задачі, відомо з загального контексту
- Patañjali, Mahābhāṣya ad 1.1.1 — традиційне джерело спорідненості
  граматики і онтології (відомо з вторинної літератури)
- [`research/samjna-categorization-vs-tag.md`](samjna-categorization-vs-tag.md)
- [`foundation/samjna.md`](../foundation/samjna.md)
- [`foundation/karaka.md`](../foundation/karaka.md)
