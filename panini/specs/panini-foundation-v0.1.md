# Panini Foundation v0.1 — Специфікація

**Статус:** ЗАВЕРШЕНО  
**Версія:** 0.1  
**Дата:** 2026-08-13

Перший milestone проекту відповідає на питання, поставлені у Розділі 23 `AGENTS.md`. Це не реалізація граматики Паніні — це встановлення формального фундаменту для майбутньої машинної моделі (`panini-machine-model-v0.1`).

---

## 1. Базові Класи Сутностей

Система Паніні має **три рівні** сутностей, які необхідно строго розрізняти:

### Рівень 1: Object Language (Мова-об'єкт)
Сутності, що описують саму мову (санскрит):

| SLP1 | IAST | Клас | Опис |
|------|------|------|------|
| `dhAtu` | dhātu | operator | Вербальний корінь; предикатний вузол семантичного графа |
| `prAtipadika` | prātipadika | entity | Іменна основа; аргументний вузол |
| `pratyaya` | pratyaya | transformer | Суфікс; трансформує тип і значення основи |
| `kAraka` | kāraka | relation | Семантична роль; ребро графа між dhātu та prātipadika |

### Рівень 2: Metalanguage (Мета-мова)
Технічний апарат самої граматики:

| SLP1 | IAST | Клас | Опис |
|------|------|------|------|
| `saMjYA` | saṃjñā | tag | Технічний термін / семантичний тег |
| `it` | it (anubandha) | metadata | Маркер, що керує derivation і зникає після застосування |
| `pratyAhAra` | pratyāhāra | set | Компактне позначення множини фонем |
| `aDikAra` | adhikāra | scope | Область дії правила; задає контекст |
| `anuvftti` | anuvṛtti | context | Успадкування умов між сутрами |

### Рівень 3: Rule System (Система Правил)
| SLP1 | IAST | Клас | Опис |
|------|------|------|------|
| `sUtra` | sūtra | rule | Одиниця граматики; оголошує умову + дію |
| `paribhAzA` | paribhāṣā | meta-rule | Правило про застосування правил |
| `vipratiSeDa` | vipratiṣedha | conflict-res | Алгоритм вирішення конфліктів правил |
| `utsarga / apavAda` | utsarga/apavāda | priority | Загальне правило / виняток |

---

## 2. Canonical SLP1 Identifiers

**Внутрішнє кодування:** строгий SLP1 (ASCII-only). Жодних IAST або Devanagari у даних.

```
SLP1:   kartf         IAST: kartṛ
SLP1:   karman        IAST: karman
SLP1:   karaRa        IAST: karaṇa
SLP1:   BU            IAST: bhū
SLP1:   sattAyAm      IAST: sattāyām
SLP1:   azwADyAyI     IAST: aṣṭādhyāyī
```

**IAST** використовується виключно в `display:` полях YAML та документаціях для людини. **SLP1** є канонічним ідентифікатором VM, реєстрів, баз даних та всіх машинних представлень.

---

## 3. Object Language vs Metalanguage

| Питання | Відповідь |
|---------|-----------|
| Що є об'єктом граматики? | `dhAtu`, `prAtipadika`, та їхні похідні (subanta, tiNanta) |
| Що є метамовою? | `it`, `pratyAhAra`, `saMjYA`, `aDikAra`, `anuvftti` |
| Чи потрапляє `it` у фінальний результат? | НІ. Видаляється за правилом 1.3.9 (`tasya lopaH`) |
| Чи потрапляє `pratyAhAra` у фінальний текст? | НІ. Це мета-позначка для правил |

---

## 4. Що таке Rule (Правило)?

**[PANINI]** `sūtra` — це афоризм, що визначає умову (pattern) та дію (transformation). Умови можуть успадковуватись від попередніх сутр (`anuvṛtti`).

**[INTERPRETATION]** Сутри є найближчим аналогом до **Rewrite Rules** або Production Rules у формальних системах.

**[MY-LISP]** У нашій VM правило — це **декларативний об'єкт**:
```lisp
;; Структура Rule:
(list (cons 'id     "7.3.84")                ;; SLP1 sutra ID
      (cons 'source 'azwADyAyI)             ;; джерело
      (cons 'condition #'has-sArvaDAtukaM)  ;; предикат на стан
      (cons 'action   #'apply-guRa))        ;; трансформація Term
```
Правило — це **дані**, а не функція мови-хоста.

---

## 5. Що таке Context (Контекст)?

**[PANINI]** Контекст — це сукупність:
1. `aDikAra` — активна область дії вищого правила
2. `anuvftti` — унаслідовані умови від попередніх сутр  
3. Поточний стан `prakriyA` — які терміни вже застосовані

**[MY-LISP]** Контекст передається через:
- **Теги** (`tags`) на вузлах `Term` (між кроками деривації)
- **Lexical closure** (функції, що захоплюють `aDikAra` зі scope)
- **Граф залежностей** між правилами (DAG)

---

## 6. Що таке Derivation (Деривація)?

**[PANINI]** Деривація (`prakriyA`) — це послідовність застосувань сутр до вхідних елементів (`dhātu` + lakāra + особовий контекст), яка породжує кінцеву фонетичну форму.

**[MY-LISP]** У нашій VM деривація — це **незмінний ланцюг станів** (State Transition Chain):
```
State₀ → [Rule R₁] → State₁ → [Rule R₂] → State₂ → ... → Stateₙ (фінал)
```
Кожен стан зберігається в `history` — деривація повністю відтворювана та налагоджувана.

**Перший трасований приклад:** [panini/examples/derivations/Bavati.md](../examples/derivations/Bavati.md)

---

## 7. Як Представлені Dhātu?

**Реєстр:** `panini/registry/dhatu/*.yaml`, один файл на корінь.

**Канонічна схема:**
```yaml
canonical: BU              # SLP1 — primary ID
display:
  iast: bhū                # тільки для людини
  devanagari: भू
class: dhatu
gana: 1                    # клас дієвідмінювання (BvAdi)
pada: parasmaipada
set_anit: seT
source:
  dhatupatha: "BvAdi (gaRa 1)"
traditional_meaning: "sattAyAm"  # SLP1!
```

**У Lisp VM:**
```lisp
(BU . ((meaning . "sattAyAm") (class . 1) (properties . (parasmaipadin seT))))
```

---

## 8. Як Представлені Kāraka?

**Реєстр:** `panini/registry/karaka/*.yaml`, один файл на роль.

**Шість ролей:**
| SLP1 | Сутра | Семантична роль |
|------|-------|-----------------|
| `kartf` | 1.4.54 `svatantraH kartA` | Незалежний ініціатор дії |
| `karman` | 1.4.49 `kartur IpsitatamaM karma` | Бажана мета дії |
| `karaRa` | 1.4.42 `sADakatamaM karaRam` | Найефективніший засіб |
| `sampradAna` | 1.4.32 `karmaRA yam aBipraiti` | Реципієнт через об'єкт |
| `apAdAna` | 1.4.24 `Druvam apAye 'pAdAnam` | Нерухома точка відділення |
| `aDikaraRa` | 1.4.45 `ADAro 'DikaraRam` | Локус/підстава дії |

**У Lisp VM** kāraka — це **ребра** семантичного графа:
```
dhAtu (predicate)
  ├── (kartf)  ──▶ prAtipadika₁
  ├── (karman) ──▶ prAtipadika₂
  └── (karaRa) ──▶ prAtipadika₃
```

---

## 9. Як Правила Посилаються на Класи?

Правила посилаються на класи через **saṃjñā** (теги) та **pratyāhāra** (множини фонем).

**Приклад:** Правило 7.3.84 не каже "якщо наступний символ є S, a, або p...". Воно каже: "якщо наступний суфікс є `sArvaDAtukaM`". Тег `sArvaDAtukaM` встановлюється раніше — при видаленні `S-it` з `Śap`.

```lisp
;; Rule посилається на TAG, а не на конкретний текст:
(defun rule-7-3-84 (dhatu-term next-suffix-term)
  (if (term-has-tag next-suffix-term 'sArvaDAtukaM)
      (apply-guRa dhatu-term)
      dhatu-term))
```

---

## 10. Ключові Відкриття (My-Lisp Hypotheses Status)

| Гіпотеза | Статус після v0.1 |
|----------|-------------------|
| `kAraka` = Typed Graph Edges | ✅ Реалізовано у `panini-core.my` |
| `pratyAhAra` = Set / Bitmask | ✅ Підтверджено Vidyut аудитом, реалізовано у `rules.my` |
| `it` = Compiler Metadata | ✅ Підтверджено і реалізовано: тег + видалення |
| `anuvftti` = Lexical Closure | ✅ Підтверджено академічно (Kulkarni) |
| `paribhAzA` = defmacro / Meta-rules | ✅ Найсильніше підтверджено (Deshpande); → наступний milestone |
| `azwADyAyI` = Type 1-2 Grammar | ✅ Підтверджено (Staal); → вибір автомата |

---

## 11. Структура Репозиторію (Фінальна для v0.1)

```
panini/
├── README.md
├── foundation/
│   ├── ontology.md        ✅ Завершено
│   ├── terminology.md     ✅ Завершено
│   ├── dhatu.md           ✅ Завершено
│   ├── karaka.md          ✅ Завершено
│   ├── samjna.md          ✅ Завершено
│   ├── pratyaya.md        ✅ Завершено
│   ├── it.md              ✅ Завершено
│   ├── pratyahara.md      ✅ Завершено
│   ├── anuvrtti.md        ✅ Завершено
│   └── rule-system.md     ✅ Завершено
├── registry/
│   ├── dhatu/             ✅ 20 коренів (SLP1, окремі файли)
│   └── karaka/            ✅ 6 ролей (SLP1, окремі файли)
├── machine/
│   ├── panini-core.my     ✅ kAraka реєстр, dhAtu реєстр, action graph
│   └── rules.my           ✅ Term, Prakriya, it-samjna, guRa, sandhi
├── examples/
│   └── derivations/
│       └── Bavati.md      ✅ Перший повний трасований приклад
├── research/
│   ├── vidyut-analysis.md     ✅ Code-level audit (4 файли)
│   ├── heritage-analysis.md   ✅ OCaml/Tries/Eilenberg
│   ├── panini-nlp-analysis.md ✅ Neuro-symbolic/Graph approach
│   └── computational-hypotheses.md ✅ 6 гіпотез з джерелами
└── specs/
    └── panini-foundation-v0.1.md  ✅ ЦЕЙ ДОКУМЕНТ
```

---

## 12. Наступний Milestone: panini-machine-model-v0.1

На основі цієї специфікації наступний etap зосереджений на:

1. **`paribhAzA` як `defmacro`:** Реалізувати мета-рівень Rule Engine, де правила самі є даними, а `paribhāṣā` керує їх застосуванням.
2. **Повний Inference Engine:** Замість фіксованого порядку кроків — декларативний граф правил, де конфлікти вирішуються через `vipratiSeDa` (порядковий номер сутри).
3. **Другий приклад деривації:** `dadAti` (клас 3, juhotyādi) або `karoti` (клас 8, tanādi) — складніша деривація для тестування Rule Engine.
4. **Міст до My Lisp VM:** Завантажити `rules.my` у реальний My Lisp інтерпретатор і виконати `(derive-Bavati)`.
