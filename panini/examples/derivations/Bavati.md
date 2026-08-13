# Трасування Деривації: `Bavati` (bhavati — "він є")

Це перший повністю трасований приклад деривації у нашому проекті.
Мета — показати кожен крок із посиланням на сутру Паніні, перш ніж кодувати будь-яке правило у Lisp.

**Вхід:** семантична намір — "він є" (3-я особа, однина, теперішній час, parasmaipada)
**Вихід:** `Bavati` (SLP1) = bhavati (IAST) = भवति (Devanagari)

---

## Початковий Стан (Input)

```
DHATU: BU   (клас 1, BvAdi, значення: sattAyAm — "to be/become")
PERSON: praTama-puruza (3-я особа)
NUMBER: eka-vacana (однина)
VOICE: parasmaipada
TENSE: vartamAna (теперішній час)
```

---

## Крок 1 — Вибір Лакари (Tense Marker)

**Сутра: 3.2.123** `vartamAne laT`

"У теперішньому часі (вартамані) застосовується лакара `laT`."

```
Стан: BU + laT
```

`laT` — це абстрактна позначка часу. Вона сама по собі не має фонетичної форми — це `saṃjñā` для класу закінчень.

---

## Крок 2 — Вибір Особового Закінчення (Tiṅ)

**Сутра: 3.4.78** `tiptasjhi...`

`laT` замінюється на набір 18 особових закінчень (`tiN`). Для 3-ї особи, однини, parasmaipada — вибирається `tip`.

```
Стан: BU + tip
```

---

## Крок 3 — It-видалення з `tip` (1.3.9)

**Сутра: 1.3.3** `halantyam`
"Кінцевий приголосний (hal) у upadesha є it."

`tip`: кінцевий `p` — it маркер.

**Сутра: 1.3.9** `tasya lopaH`
"It зникає."

```
Designations у trace: `it(final-p)` за 1.3.3; lopa за 1.3.9.
Стан: BU + ti
```

> [!NOTE]
> **Ключовий момент:** `p` зникає із surface form, але факт його
> `it`-designation і застосування lopa мають лишитися окремими
> provenance-bearing trace records. Це не ототожнює `it` із compiler metadata.

---

## Крок 4 — Додавання Вікарани (Vikaraṇa Śap)

**Сутра: 3.1.68** `kartari Sap`

"Суфікс `Sap` додається між коренем і закінченням для дієслів класу 1 (BvAdi) в активному стані (kartari)."

```
Стан: BU + Sap + ti
```

---

## Крок 5 — It-видалення з `Sap`

**Сутра: 1.3.8** `laSakvatadDite`
"Початкові `l`, `S` і звуки ka-варги в нетаддгіта-суфіксі є `it`."

`Sap`: початковий `S` є `it` за 1.3.8. Кінцевий `p` окремо є `it` за
1.3.3 `halantyam`.

**Сутра: 3.4.113** `tiNSitsArvaDAtukam`
Tiṅ- і `Sit`-суфікси отримують designation `sArvaDAtuka`. Це designation
належить affix occurrence, а не буквальному surface `a`.

**Сутра: 1.3.9** `tasya lopaH`

```
Trace records для affix occurrence `Sap`:
  it(initial-S), it(final-p), sArvaDAtuka
  ← кожен із власним sutra/provenance record
Стан: BU + a + ti
```

---

## Крок 6 — Гуна-заміна (Guṇa)

**Сутра: 7.3.84** `sArvaDAtukArDaDAtukayoH`

"Перед sārvadhātuka або ārdhadhātuka суфіксом — кінцевий голосний основи (aṅga) отримує guṇa-заміну."

Affix occurrence, чия surface form тепер `a`, має designation
`sArvaDAtuka` за 3.4.113 через початковий `S` у `Sap`. Тому для цього
окремо простеженого interpretation path до `BU` застосовується guṇa:

**Сутра: 1.1.2** `adeng guRaH`
"Замінники `a`, `e`, `o` є guṇa."

Guṇa таблиця:
- `a/A` → `a` (без змін)
- `i/I` → `e`
- `u/U` → `o`  ← застосовується до `U` в `BU`
- `f/F` → `ar`

```
BU → guRa → Bo
Стан: Bo + a + ti
```

---

## Крок 7 — Сандгі: eco 'yavāyāvaḥ

**Сутра: 6.1.78** `eco 'yavAyAvaH`

"Якщо після `e`, `o`, `E`, `O` іде голосний — вони замінюються на `ay`, `av`, `Ay`, `Av` відповідно."

`o` + `a` (голосний) → `av` + `a`

```
Bo + a + ti
→ Bav + a + ti
= Bavati
```

---

## Підсумок Деривації

```
Крок | Форма          | Сутра    | Дія
-----|----------------|----------|----------------------------------
  1  | BU + laT       | 3.2.123  | Вибір лакари теперішнього часу
  2  | BU + tip       | 3.4.78   | Вибір особового закінчення
  3  | BU + ti        | 1.3.3, 1.3.9 | it-designation і lopa з tip
  4  | BU + Sap + ti  | 3.1.68   | Додавання вікарани Śap (клас 1)
  5  | BU + a + ti    | 1.3.8, 1.3.3, 1.3.9, 3.4.113 | it/lopa та sArvaDAtuka-designation Sap
  6  | Bo + a + ti    | 7.3.84   | Гуна: U → o (перед sArvaDAtukaM)
  7  | Bavati         | 6.1.78   | Сандгі: o + a → av + a
```

---

## Представлення у Our Lisp VM (Гіпотетичне)

```lisp
;; [MY-LISP HYPOTHESIS] — Не факт про Паніні, а модель нашої VM
;;
;; Деривація як послідовність state transitions на незмінному AST:

(def-derivation Bavati-derivation
  (initial-state
    (dhAtu BU :gana 1 :upadesha "BU")
    (intent (person 3) (number 1) (voice parasmaipada) (tense vartamAna)))

  (step 1 :sutra "3.2.123"
    (add-lakara laT))

  (step 2 :sutra "3.4.78"
    (select-tin tip))

  (step 3 :sutra "1.3.3 + 1.3.9"
    (record-designation tip :it 'p)
    (remove-marked-sound tip 'p)
    ;; machine record, не визначення it як metadata
    )

  (step 4 :sutra "3.1.68"
    (add-vikarana Sap :between dhAtu tin))

  (step 5 :sutra "1.3.8 + 1.3.3 + 1.3.9 + 3.4.113"
    (record-designation Sap :it 'S :basis "1.3.8")
    (record-designation Sap :it 'p :basis "1.3.3")
    (remove-marked-sounds Sap '(S p))
    (record-designation Sap :sArvaDAtuka :basis "3.4.113")
    )

  (step 6 :sutra "7.3.84"
    ;; Перевіряємо evidence-bound designation affix occurrence, не tag surface `a`.
    (when (has-designation next-suffix :sArvaDAtuka)
      (apply-guRa dhAtu)))   ;; U → o

  (step 7 :sutra "6.1.78"
    (apply-sandhi Bo a)))    ;; o + a → av + a
```

---

## Важливі спостереження для Rule Engine

1. **Порядок є критичним:** Кроки 3 і 5 (`it`-designations і lopa)
   **повинні відбуватись** до кроку 6 (guṇa), бо цей шлях guṇa залежить
   від окремо простеженого `sArvaDAtuka` designation affix occurrence.
2. **Designations мають окремий evidence trace:** `it(initial-S)`,
   `it(final-p)` і `sArvaDAtuka` — не фінальний результат і не готові VM
   tags. Вони є окремими claims між кроками, тому простого `if-else`
   недостатньо.
3. **Upadesha vs Text:** `BU` (upadesha) незмінний протягом всієї деривації. Мутує лише `text` поле: `BU → Bo → Bav`.
4. **Кожне правило — незалежний об'єкт:** Жодне з правил "не знає" про інші — воно лише перевіряє поточний стан і застосовує трансформацію.
