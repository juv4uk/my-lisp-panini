# Vidyut Code-Level Audit (v2 — Детальний)

Аудит вихідного коду `vidyut-prakriya` (Rust). Досліджено 4 ключові файли:
- `sounds.rs` — фонеми та pratyāhāra
- `it_samjna.rs` — видалення it-маркерів (1.3.2–1.3.9)
- `core/term.rs` — структура Term (морфема)
- `core/prakriya.rs` — стан деривації та Rule enum

---

## 1. sounds.rs — Реалізація Pratyāhāra

### Ключова знахідка: Set як bitmask-подібний масив
Vidyut представляє кожен `pratyāhāra` як тип `Set`, що внутрішньо є **масивом з 128 байтів** (один байт на ASCII/SLP1 символ):

```rust
pub const AC: Set = s(&["ac"]);  // усі голосні
pub const HAL: Set = s(&["hal"]); // усі приголосні
pub const JHAL: Set = s(&["Jal"]);
pub const IK: Set = s(&["ik"]);
```

Перевірка `set.contains(sound)` — це буквально `array[sound as usize] != 0` — **O(1) lookup**.

Це повністю підтверджує Гіпотезу №2 (`pratyAhAra = bitmask`). Vidyut реалізував саме це!

### Структура Sutra для Śiva Sūtras
```rust
struct Sutra {
    sounds: &'static str,  // звуки в сутрі
    it: Sound,             // кінцевий it-маркер
}
```
Śiva Sūtras закодовані як масив таких структур, де кожна сутра знає свій кінцевий `it`. Функція `s(&["ac"])` обходить масив і збирає всі звуки від початку `a` до кінця `c`.

### Фонетичні властивості (Uccarana)
Vidyut зберігає артикуляційні властивості кожного звука у `HashMap<Sound, Uccarana>`:
- `Sthana` (місце артикуляції): `Kantha`, `Talu`, `Murdha`, `Danta`, `Oshtha`
- `Ghosha` (дзвінкість): `Ghoshavat` / `Aghosha`
- `Prana` (аспірація): `Alpaprana` / `Mahaprana`

**Для My Lisp:** Це натхнення — при аналізі сандгі нам теж потрібні ці властивості. Але замість `HashMap` у Lisp ми можемо використати a-list або property list.

---

## 2. it_samjna.rs — Реалізація It-Маркерів (1.3.2–1.3.9)

### Ключова знахідка: два рівні — текст і теги
Vidyut використовує **двоетапну стратегію**:

1. **Фаза ідентифікації:** Система аналізує `upadesha` (канонічну форму) терміну і визначає, які звуки є `it`. Результат — набір тегів (`EnumSet<Tag>`) на об'єкті `Term`.
2. **Фаза видалення (1.3.9 `tasya lopaH`):** Тільки після повної ідентифікації всіх `it` — одноразове видалення з текстового рядка.

```rust
// Коментар у коді Vidyut:
// "All it sounds are removed at once by 1.3.9 'tasya lopaH'. Before then,
//  keep the text in the term unchanged. Instead, mutate a new temporary
//  string and copy it over as part of 1.3.9."
```

Це точна реалізація механізму Паніні! `it` не видаляється одразу — спочатку він "позначається" як тег, а потім прибирається разом.

### Типи тегів від it-маркерів
```rust
t.add_tags(&[T::irit, T::svaritet]);  // від "i~r"
```
Кожен `it`-маркер залишає слід у вигляді `Tag` — набору значень `enum`. Наприклад, наявність `p-it` забороняє певний наголос, а `ñ-it` сигналізує про ātmanepada.

**Для My Lisp:** Підтверджено Гіпотезу №1 (it = Compiler Metadata). У нашій VM `it` буде зберігатися як `(metadata (p-it t) (n-it nil))` на вузлі AST.

---

## 3. core/term.rs — Структура Term

### Ключова знахідка: подвійне представлення (u та text)
```rust
pub struct Term {
    pub(crate) u: Option<TermString>,    // upadesha — канонічна форма з it
    pub(crate) text: TermString,          // поточний текст (без it, зі змінами)
    pub(crate) tags: EnumSet<Tag>,        // saṃjñā та метадані
    pub(crate) morph: Morph,             // тип морфеми
    pub(crate) gana: Option<Gana>,       // клас dhātu
    ...
}
```

Це **двошарова модель**:
- `u` = незмінна пам'ять про початкову форму (upadesha)
- `text` = змінний поточний стан (після правил)

### Morph enum — класифікація морфем
```rust
enum Morph {
    None, Abhyasa, Agama(Agama),
    BasicPratipadika,
    Dhatu(Aupadeshika),     // dhātu
    Krt(Krt),               // kṛt-pratyaya
    Sanadi(Sanadi),         // санаді-pratyaya
    Sup(Sup),               // вібгакті-суфікс
    Tin(Tin),               // особові закінчення
    Vikarana(Vikarana),     // вікарана (клас-маркер)
    ...
}
```

Це повна онтологія морфем у вигляді **tagged union (Rust enum)**. Кожен вузол "стрічки" деривації знає свій тип.

**Для My Lisp:** Замість Rust enum — ми будемо використовувати Lisp-теги. Наприклад, `(dhAtu BU)`, `(pratyaya Sap)`, `(vikarana a)`.

---

## 4. core/prakriya.rs — Стан Деривації та Rule Enum

### Ключова знахідка: Rule як typed enum з source tracking
```rust
pub enum Rule {
    Ashtadhyayi(&'static str),  // "1.4.54"
    Varttika(&'static str),
    Dhatupatha(&'static str),
    Unadipatha(&'static str),
    Kashika(&'static str),      // коментар Кашіки
    ...
}
```

Кожне правило — це не просто рядок `"1.4.54"`, а **типізований ідентифікатор з джерелом**. Це дозволяє системі розрізняти правило з Aṣṭādhyāyī від варттіки або коментаря Кашіки.

Назви джерел зберігаються у строгому **SLP1** (підтвердження нашого підходу):
```rust
Self::Ashtadhyayi(_) => "azwADyAyI",
Self::Dhatupatha(_)  => "DAtupAWaH",
```

### Decision enum — журнал рішень
```rust
pub enum Decision { Accept, Decline }
```
Prakriya зберігає не тільки застосовані правила, але і **відхилені**! Це критично для відтворення деривації та debugging.

---

## 5. Підсумкова Таблиця: Vidyut vs My Lisp Hypothesis

| Компонент | Vidyut (Rust) | My Lisp Hypothesis | Відповідність |
|---|---|---|---|
| `pratyAhAra` | `Set` = 128-byte array, O(1) | Множина / Bitmask | ✅ Підтверджено |
| `it`-маркери | Двоетапний: теги → `tasya lopaH` | Метадані вузла AST | ✅ Підтверджено |
| `saṃjñā` | `EnumSet<Tag>` на кожному Term | Property list / tagged symbols | ✅ Підтверджено |
| `prakriyA` | Mutable Vec\<Term> + Rule log | State transitions на незмінному графі | ⚠️ Відмінність! |
| `Rule` | Typed enum + &str ID | Декларативний об'єкт у Rule Graph | ⚠️ Відмінність! |
| Порядок правил | Жорстко закодований в Rust | Динамічний Inference Engine | ❌ Навмисна відмінність |

### Ключова відмінність
Vidyut використовує **mutable Vec\<Term>** — лінійна мутація стрічки. Це ефективно для NLP-генерації, але не підходить для нашого символьного AI, де нам потрібні:
1. **Незмінні (immutable) структури** — щоб можна було відслідкувати будь-який проміжний стан.
2. **Граф замість стрічки** — щоб kāraka-зв'язки були першокласними об'єктами, а не просто позиціями у масиві.
3. **Декларативні правила** — щоб Rule Engine міг сам вирішувати конфлікти (vipratiṣedha), а не покладатися на жорстко закодований порядок фаз.

---

## 6. Висновки для panini-machine-model-v0.1

1. **Використати ідею двошарового Term:** у нашому Lisp кожен елемент деривації має `upadesha` (незмінний) і `text` (поточний стан).
2. **Множини звуків (Set) реалізувати як Lisp-константи** (як вже зроблено в `panini-core.my`).
3. **Rule enum → Lisp tagged list:** `(rule "1.4.54" :source astaDyAyI)`.
4. **Зберегти журнал рішень** (Accept/Decline) для кожного кроку деривації.
5. **НЕ копіювати** mutable Vec\<Term> — будувати незмінний граф з kāraka-ребрами.
