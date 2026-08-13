# Sva-kartṛ vs Para-kartṛ — власна і зовнішня дія в системі Паніні

Статус: виконано (`PHILOSOPHY-SVA-VS-PARA-KARTR`)  
Автор: my-lisp-panini-1 · 2026-08-13  
Зв'язок: → `foundation/karaka.md`, → `computational-hypotheses.md` H1

---

## Центральне питання

Чи розрізняє система Паніні між:
- `sva-kartṛ` — суб'єкт дії є її бенефіціаром (діє для себе)
- `para-kartṛ` — суб'єкт дії є агентом для іншого

І якщо так — як це кодується граматично і чи є наслідки для машинної моделі?

---

## [PANINI] Граматичне кодування

### Pada — parasmaipada vs ātmanepada

Паніні кодує цю відмінність через **pada** (особові закінчення):

| Pada | SLP1 | Значення | Приклад |
|------|------|----------|---------|
| parasmaipada | parasmaipada | "для іншого" — агент діє для зовнішнього | `pacati` (він варить [для когось]) |
| ātmanepada | Atmanepada | "для себе" — агент є бенефіціаром | `pacate` (він варить [для себе]) |
| ubhayapada | uBayapada | обидва можливі | деякі dhātu |

Це кодується прямо в `dhātu`-реєстрі через `pada`-властивість:
```yaml
# BU.yaml
pada: parasmaipada  # завжди для іншого
# dA.yaml
pada: ubhayapada    # може бути для себе або іншого
```

### Sūtra 1.3.72 — ātmanepada базові правила

`svaritaJit AtmanepadeZu` (1.3.72): dhātu зі svarita-it або ñit
успадковує ātmanepada. Це pāninian визначення "що робиться для себе".

### Sūtra 1.3.26 — kartari parasmaipada

Стандартне особове закінчення (parasmaipada) застосовується в kartari
(агентивному) контексті за замовчуванням.

---

## [INTERPRETATION] Семантика, а не тільки морфологія

Дослідники (Cardona, Deshpande) зазначають, що відмінність
parasmaipada/ātmanepada є **частково граматикалізованою семантичною
відмінністю**:

- Bagha-rule в традиції: деякі dhātu obligatorily ātmanepada (напр.
  `labh` — "отримувати", завжди для себе)
- Деякі допускають обидва з різним смислом:
  `yaj parasmai` (приносить жертву богам) vs `yaj ātmane` (приносить для себе)

Але це **не повна семантична система**: багато dhātu мають fixed pada
незалежно від семантики конкретного речення.

---

## [MY-LISP HYPOTHESIS] Наслідки для архітектури

### Для kāraka-графа (H1)

Відмінність sva/para додає **неявний аргумент** до графа:

```
dA (давати) — parasmaipada:
  dhAtu → kartf (devadatta)
         → karman (anna — їжа)
         → sampradAna (brAhmaRa — recipient)

dA (dawати) — ātmanepada:
  dhAtu → kartf = sampradAna (те саме!)  ← картf є бенефіціаром
         → karman (anna)
```

Тобто ātmanepada сигналізує: `kartf` і `sampradāna` є одним і тим же
об'єктом в семантичному графі. Це **злиття ролей** в одному вузлі.

Для нашого `make-action-graph` це означає:

```lisp
;; parasmaipada: окремі вузли
(make-action-graph 'give-1 'dA
  '((kartf . devadatta)
    (karman . anna)
    (sampradAna . brAhmaRa)))

;; ātmanepada: kartf = sampradAna (той самий вузол)
(make-action-graph 'give-2 'dA
  '((kartf . devadatta)
    (karman . anna)
    (sampradAna . devadatta)))  ;; ← та сама сутність
```

Поточна архітектура (alist з різними ключами) це підтримує — але
явного механізму для позначення "ці два ролі — один об'єкт" немає.

### Рівень впливу

Відмінність sva/para:
- **Не змінює** core правила деривації (правила 7.3.84, 6.1.78 etc.)
- **Змінює** вибір tiṅ-закінчень (parasmaipada vs ātmanepada парадигми)
- **Потенційно змінює** semantic graph структуру (злиття ролей)

Для v0.1 (`bhavati`, `dadāti` — обидва parasmaipada) — це не актуально.
Актуально при додаванні ātmanepada деривацій (наприклад `labhate`).

---

## Відкриті питання

1. Чи є в Паніні явний механізм для "злиття kāraka-ролей" (kartf =
   sampradāna), чи це виключно семантична інтерпретація дослідників?

2. При побудові semantic graph: чи треба явно моделювати злиття
   (`(kartf = sampradAna devadatta)`) або достатньо того, що обидва
   ключі вказують на одну сутність?

3. Чи є інші ātmanepada-ситуації де злиття відбувається з іншими парами
   kāraka (картf = karman? — так, у рефлексивних конструкціях)?

---

## Джерела

- [`foundation/karaka.md`](../foundation/karaka.md) — визначення kāraka
- [`registry/dhatu/dA.yaml`](../registry/dhatu/dA.yaml) — pada: ubhayapada
- [`registry/dhatu/BU.yaml`](../registry/dhatu/BU.yaml) — pada: parasmaipada
- Aṣṭādhyāyī 1.3.26, 1.3.72 (за пам'яттю, потребує верифікації)
- Cardona 1976 (вторинне джерело)
