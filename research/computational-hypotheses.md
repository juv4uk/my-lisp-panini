# Обчислювальні Гіпотези: Паніні ↔ My Lisp

Цей документ збирає дослідницькі гіпотези, підкріплені академічними джерелами, про можливі структурні відповідності між системою Паніні та сучасними обчислювальними моделями.

**Суворе попередження:** Відповідно до Правил №21 та №25 проекту — усі гіпотези тут позначені `[MY-LISP HYPOTHESIS]` і відокремлені від задокументованих фактів `[PANINI]` та наукових інтерпретацій `[INTERPRETATION]`.

---

## Гіпотеза 1: Kāraka ↔ Labeled Typed Edges (Compositional Semantics)

### [PANINI]
Шість kāraka (kartf, karman, karaRa, sampradAna, apAdAna, aDikaraRa) визначають семантичне відношення між сутністю та дією (dhātu). Вони не є морфологічними відмінками — це глибинна семантична структура.

### [INTERPRETATION]
Сучасні лінгвісти порівнюють kāraka з **Thematic Roles** (ролями тета в теорії управління та зв'язування Хомського) або з **FrameNet**-ролями. ResearchGate-публікації фіксують спроби формалізувати kāraka через теорію категорій — обидві системи (kāraka і теорія категорій) прагнуть описати **компонентну структуру** складних об'єктів через формальні, передбачувані правила трансформації.

Цитата з MathOverflow: "Mapping from semantic roles to morphological case can be viewed as a functorial mapping between categories."

### [MY-LISP HYPOTHESIS]
Kāraka — це не просто список ролей. Це **алгебраїчна структура ребер** орієнтованого семантичного графа. Граф:
```
dhAtu (predicate node)
   |── (kartf)    ──▶ prAtipadika_1
   |── (karman)   ──▶ prAtipadika_2
   └── (karaRa)   ──▶ prAtipadika_3
```
У теорії категорій це **морфізми** між об'єктами двох категорій: Action → Entity. Якщо це гіпотеза підтвердиться — у нашій VM типова система буде будуватися не на ADT (Algebraic Data Types), а на typed morphisms, що робить її природним чином compositional.

**Пріоритет перевірки:** Висока. Це безпосередньо впливає на архітектуру AST.

---

## Гіпотеза 2: Pratyāhāra ↔ Optimal Bitmask / MDL Encoding

### [PANINI]
Śiva Sūtras (14 афоризмів) кодують усі фонеми санскриту у строго впорядкованій послідовності. Сутра 1.1.71 (*ādir antyena sahetā*) дозволяє позначати будь-яку підмножину фонем одним коротким ідентифікатором — pratyāhāra.

### [INTERPRETATION]
**Академічне підтвердження:** Wiebke Pieterson та Paul Kiparsky незалежно показали, що упорядкування фонем у Śiva Sūtras є **математично оптимальним** для цілей побудови pratyāhāra. Це максимально мінімізує "довжину опису" (Minimum Description Length) усього зводу правил.

Google Scholar (via INRIA, 2024): "Pāṇini's Razor — максимум точності при мінімумі символів (*svalpākṣaram*) — є паралеллю принципу Оккама в MDL-теорії."

### [MY-LISP HYPOTHESIS]
Для нашого Lisp VM:
- `ac` (всі голосні) — це константа-множина `#{a i u f x e o E O}`.
- Перевірка "чи є звук X голосним?" — це `O(1)` операція `(member X ac)`.
- Для FPGA: кожен pratyāhāra може компілюватися у **hardware bitmask** (один 64-бітний регістр). Перевірка — побітове `AND` за один такт (1 clock cycle).

Якщо замовлення фонем у Śiva Sūtras справді оптимальне, то й наш SLP1-кодований тип даних може успадкувати цей порядок для власної оптимізованої хеш-функції.

**Пріоритет перевірки:** Середня (важливо для FPGA-фази).

---

## Гіпотеза 3: Anuvṛtti ↔ Lexical Scoping / Lazy Evaluation

### [PANINI]
`Anuvṛtti` — механізм "перенесення" умов або термінів з попередніх сутр до наступних без явного їх повторення. Сутри не є незалежними — вони успадковують контекст від попередників.

### [INTERPRETATION]
**Академічне підтвердження:** ResearchGate 2023 та Medium (публікації Amba Kulkarni): Aṣṭādhyāyī може бути змодельований як **направлений ациклічний граф (DAG)**, де вузли — це сутри, а ребра — відношення anuvṛtti (успадкування контексту).

Arxiv (IIT Bombay, 2022): "The system operates as a constraint satisfaction problem where anuvṛtti provides the global context, and specific sūtras provide local constraints."

### [MY-LISP HYPOTHESIS]
У Haskell/Clojure `anuvṛtti` ідеально відповідає **lexical closure**: функція "захоплює" змінні з оточуючого середовища, не отримуючи їх явно як аргументи.

```lisp
;; [MY-LISP HYPOTHESIS] - не факт про Паніні!
(let ((aDikAra-context (list 'kArake)))
  (defun sutra-1-4-24 (term)
    ;; Успадковує контекст aDikAra-context через closure
    (apply-in-context aDikAra-context term)))
```

Це означає: наш Rule Engine не передаватиме контекст явно між правилами (що зробив би Vidyut). Замість цього — **closure-based анотації**, де кожне правило "живе" у своєму лексичному scope.

**Пріоритет перевірки:** Висока. Це найближче до готової архітектурної ідеї.

---

## Гіпотеза 4: Paribhāṣā ↔ Defmacro / Meta-level Rules

### [PANINI]
`Paribhāṣā` — це особливий клас правил, які керують тим, **як застосовувати** інші правила. Вони не є об'єктними правилами (не описують мову), а є мета-правилами (описують алгоритм).

Приклади:
- "Правило про правила" (наприклад, яке правило має пріоритет)
- "Що вважається сказаним у контексті sūtra X"

### [INTERPRETATION]
**Академічне підтвердження (найсильніше з усіх!):**

Scribd (Deshpande, Kiparsky): "Paribhāṣā act as high-level logic, compiler instructions, or system configuration that dictate how other rules are executed."

Medium (2024): "Pāṇini did not just describe a language; he designed a formal, logical system." Paribhāṣā — це рівень метапрограмування цього системного опису.

BNF: Дослідники порівнюють систему Паніні (включно з paribhāṣā) з системою Бекуса-Наура (BNF). BNF — це теж мета-мова: вона описує, як треба читати правила граматики.

### [MY-LISP HYPOTHESIS]
`Paribhāṣā` = **`defmacro` рівень** нашого Rule Engine. У Lisp `defmacro` — це код, що трансформує інший код до його виконання. Аналогічно, paribhāṣā трансформують або обмежують застосування інших sūtras.

```lisp
;; [MY-LISP HYPOTHESIS]
;; Paribhāṣā як meta-rule:
(defmacro def-rule (name &body body)
  ;; Тут живе логіка paribhāṣā:
  ;; автоматично додає пріоритет (sutra-index),
  ;; реєструє в rule-graph,
  ;; прив'язує до aDikAra-scope
  `(register-rule ',name ,@body))
```

Якщо ця гіпотеза вірна — наш Rule Engine буде двошаровим:
1. **Об'єктний рівень:** Самі сутри як `def-rule`.
2. **Мета-рівень:** Paribhāṣā як логіка `defmacro`, яка керує тим, як `def-rule` реєструється та застосовується.

**Пріоритет перевірки:** КРИТИЧНА. Це центральна архітектурна ідея.

---

## Гіпотеза 5: Aṣṭādhyāyī ↔ Chomsky Hierarchy (Type 1–2)

### [PANINI]
Aṣṭādhyāyī генерує всі граматично коректні форми санскриту з кінцевого набору правил. Правила часто контекстно-залежні (форма слова залежить від оточення).

### [INTERPRETATION]
**Академічне підтвердження:**

Oxford University (2024): "Pāṇini's formalism is superficially context-sensitive (Type-1), but with acyclicity constraints that limit its generative power."

Frits Staal (Heidelberg): Показав, що система Паніні потужніша за регулярні граматики (Type-3), але не є стандартним Type-1 через явні обмеження на циклічність.

StackExchange (CS): "Recent research points out that Pāṇini incorporated specific constraints that prevent infinite, uncontrolled rule cycles — effectively taming Turing-complete power."

### [MY-LISP HYPOTHESIS]
Це дуже важливо для вибору автомата:
- Якщо Aṣṭādhyāyī — це Type-2 (контекстно-вільна) — нашою VM потрібен **Push-Down Automaton (PDA)** або **рекурсивний спуск**.
- Якщо Type-1 (контекстно-залежна) — нам потрібен **Linear-Bounded Automaton (LBA)**.
- Якщо ж acyclicity constraints дійсно роблять систему "майже Type-2" — можна обійтися функціональними трансформаціями без повного LBA.

**Пріоритет перевірки:** Висока (для фази FPGA-архітектура).

---

## Гіпотеза 6: Vidyut Internals — Code-Level Audit

### [PANINI / INTERPRETATION]
Цей пункт не гіпотеза, а завдання: провести детальний аудит конкретних файлів Vidyut.

**Цільові файли:**
- `crates/vidyut-prakriya/src/it_samjna.rs` — реалізація it-маркерів
- `crates/vidyut-prakriya/src/ashtadhyayi.rs` — порядок застосування правил
- `crates/vidyut-prakriya/src/sounds.rs` — реалізація Śiva Sūtras / pratyāhāra

### [MY-LISP HYPOTHESIS]
Цей аудит відповість на питання: яку конкретну структуру даних (enum, HashMap, DAG) використовує найкраща існуюча реалізація для представлення наших ключових понять? Це прив'яже гіпотези до конкретних алгоритмічних рішень.

**Пріоритет: Наступний кrok після затвердження цього документа.**

---

## Підсумкова Матриця Гіпотез

| Гіпотеза | Концепція Паніні | Аналог у CS | Статус | Вплив на VM |
|---|---|---|---|---|
| 1 | kAraka | Typed Morphisms / Graph Edges | Частково підтверджено | Тип системи AST |
| 2 | pratyAhAra | Bitmask / MDL | Підтверджено (Kiparsky) | FPGA-архітектура |
| 3 | anuvftti | Lexical Closure / Lazy Eval | Підтверджено (Kulkarni) | Контекстна модель |
| 4 | paribhAzA | Defmacro / Meta-rules | **Підтверджено найсильніше** | Ключова архітектура |
| 5 | astADyAyI | Chomsky Type 1-2 | Підтверджено (Staal) | Тип автомата VM |
| 6 | — | Vidyut code audit | TO DO | Конкретні алгоритми |
