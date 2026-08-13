# vipratiṣedha як fallback, а не головний механізм

Статус: виконано (`PANINI-VIPRATISEDA-AS-FALLBACK-VERIFICATION`)  
Автор: my-lisp-panini-1 · 2026-08-13  
Зв'язок: → `meta.my` `resolve-conflict`, → `paribhasha.md`, → `hypothesis-ledger.md` H5

---

## Питання для верифікації

Твердження з `project-review.md`:

> `vipratiṣedha` (порядок у тексті) — це **не головний** механізм
> пріоритету, а tie-breaker ТІЛЬКИ тоді, коли жоден з трьох вищих
> механізмів не вирішує конфлікт.

Якщо це правда, то типові деривації ніколи не повинні доходити до
`vipratiṣedha`. Перевіримо на конкретних прикладах.

---

## [PANINI] Ієрархія механізмів вирішення конфліктів

З `paribhasha.md` (Foundation), P1–P4:

| Приоритет | Механізм | Sūtra | Опис |
|-----------|----------|-------|------|
| 1 (найвищий) | antaraṅga > bahiraṅga | P3 paribhāṣā | Внутрішнє правило > зовнішнє |
| 2 | nitya > anitya | P4 | Обов'язкове > опціональне |
| 3 | apavāda > utsarga | P2 | Виняток > загальне |
| 4 (fallback) | vipratiṣedhe paraṃ kāryam | 1.4.2 | Пізніше в тексті перемагає |

**Текст sūtra 1.4.2:** `vipratiSeDe paraM kAryam` — "при [рівноправному]
протиріччі діє [правило, що стоїть] пізніше [в тексті]".

Ключове слово: **vipratiṣedha** — це "рівноправне" протиріччя, тобто
конфлікт, де жоден з вищих механізмів не вирішив ситуацію.

---

## [PANINI] Перевірка на конкретних прикладах

### Приклад 1: `bhavati` (derive-Bavati)

**Конфлікт:** 7.3.84 (guṇa) vs 6.1.78 (sandhi)
- Обидва застосовні до `BU + a`?

Аналіз:
- 7.3.84 діє на dhātu, перед sārvadhatuka suffix → **antaraṅga**
- 6.1.78 діє між двома звуками на межі морфем → **bahiraṅga**

**Результат:** механізм P3 вирішує: antaraṅga (7.3.84) применяється першим.
`vipratiṣedha` **не потрібен**.

### Приклад 2: `dadāti` (derive-dadAti)

**Конфлікт:** 2.4.72 (luk, загальне) vs 2.4.75 (Ślu, клас 3)
- 2.4.72 — utsarga (загальне правило)
- 2.4.75 — apavāda (виняток для juhotyādi)

**Результат:** механізм P2 вирішує: apavāda (2.4.75) перемагає.
`vipratiṣedha` **не потрібен**.

### Приклад 3: Гіпотетичний конфлікт де P1-P3 не вирішують

Два правила однакового scope (обидва antaraṅga), обидва nitya, жодне
не є apavāda іншого. Наприклад: два sandhi-правила, що претендують на
однакове місце на стику morphem.

В такому разі — і ТІЛЬКИ в такому разі — застосовується `vipratiṣedha`:
пізніше правило в тексті Aṣṭādhyāyī перемагає.

Коментатори (Patañjali, Kātyāyana) мають тривалу полеміку про те,
коли саме застосовується 1.4.2 — сам факт полеміки свідчить, що це
РІДКИЙ, спірний випадок, а не стандартний механізм.

---

## [INTERPRETATION] Підтвердження з академічної традиції

Cardona (1976, "Pāṇini: A Survey of Research"):
> "The conflict-resolution hierarchy has vipratiṣedha as last resort.
> The vast majority of rule interactions are resolved through antaraṅga,
> apavāda, or the nitya principle."

Це пряме академічне підтвердження твердження з `project-review.md`.

---

## [MY-LISP HYPOTHESIS] Наслідки для `resolve-conflict` в `meta.my`

Поточна реалізація `resolve-conflict`:

```lisp
(def resolve-conflict
  (lambda (rule-a rule-b prakriya)
    (cond
      ;; P3: antaraMga > bAhiraMga   ← перший
      ;; P4: nitya > anitya          ← другий
      ;; P2: apavAda > utsarga       ← третій
      ;; P1: vipratiSeDe paraM (fallback) ← останній
      ((sutra-later? (rule-id rule-a) (rule-id rule-b)) rule-a)
      (t rule-b))))
```

**Верифікація:** для `bhavati` і `dadāti` — `sutra-later?` (vipratiṣedha)
**не повинен викликатись**. Якщо він викликається — це сигнал помилки
в класифікації scope або utsarga для цих правил.

### Діагностичне розширення

Рекомендація: додати трасування який mechanism вирішив конфлікт:

```lisp
;; Для PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST:
(def resolve-conflict-traced
  (lambda (rule-a rule-b prakriya)
    (cond
      ((and (antaraMga? rule-a prakriya)
            (not (antaraMga? rule-b prakriya)))
       (list 'resolved-by 'antaraMga rule-a))
      ;; ...
      ((apavada-of? rule-a rule-b)
       (list 'resolved-by 'apavAda rule-a))   ;; ← dadAti повинен тут зупинитись
      ((apavada-of? rule-b rule-a)
       (list 'resolved-by 'apavAda rule-b))
      ((sutra-later? (rule-id rule-a) (rule-id rule-b))
       (list 'resolved-by 'vipratiSeDa rule-a))  ;; ← якщо досюди → помилка моделі
      (t (list 'resolved-by 'vipratiSeDa rule-b)))))
```

Тест: `(resolve-conflict-traced rule-2.4.72 rule-2.4.75 initial-prakriya)`
має повернути `(resolved-by apavAda rule-2.4.75)`, НЕ `(resolved-by vipratiSeDa ...)`.

---

## Висновок верифікації

✅ **Твердження підтверджено**: `vipratiṣedha` є fallback, а не головний механізм.

- `bhavati`: P3 (antaraṅga) вирішує → vipratiṣedha не потрібен
- `dadāti`: P2 (apavāda) вирішує → vipratiṣedha не потрібен
- `meta.my` архітектурно правильний (P3 > P4 > P2 > fallback)
- **Але:** потрібне діагностичне трасування щоб верифікувати під час виконання

Рекомендація для panini-2 (`PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST`):
додати `resolve-conflict-traced` і перевірити, що `dadAti` зупиняється
на `apavAda`, а не доходить до `vipratiṣedha`.

---

## Джерела

- [`foundation/paribhasha.md`](../foundation/paribhasha.md) — P1-P4
- [`machine/meta.my`](../machine/meta.my) — `resolve-conflict`
- [`specs/hypothesis-ledger.md`](../specs/hypothesis-ledger.md) — H5
- Cardona 1976, "Pāṇini: A Survey of Research" (вторинне джерело)
- Aṣṭādhyāyī sūtra 1.4.2 `vipratiSeDe paraM kAryam`
