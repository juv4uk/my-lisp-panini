# Panini → My Lisp: Bridge Specification

Цей документ — єдиний файл, який потрібно прочитати агенту My Lisp перед тим,
як інтегрувати `panini-foundation` у реальний інтерпретатор.

---

## 1. Що ми маємо з боку Паніні

Репозиторій `my-lisp-panini` містить:

| Файл | Вміст |
|------|-------|
| `panini/machine/panini-core.my` | Реєстри dhātu та kāraka як Lisp a-lists |
| `panini/machine/rules.my` | Rule Engine: Term, Prakriya, it-samjna, guṇa, sandhi |
| `panini/examples/derivations/Bavati.md` | Повна трасована деривація (7 кроків) |
| `panini/specs/panini-foundation-v0.1.md` | Специфікація milestone v0.1 |

---

## 2. Синтаксичні Розбіжності (потрібно виправити)

Наш код у `rules.my` написаний у "generic Lisp" стилі.
My Lisp використовує **власний синтаксис**. Потрібні такі заміни:

| `rules.my` (зараз) | My Lisp (правильно) |
|--------------------|---------------------|
| `(defun f (x) ...)` | `(def f (lambda (x) ...))` |
| `(member x lst)` | `(member? x lst)` |
| `(last lst)` | потрібна реалізація в `core.my` або `(car (reverse lst))` |
| `(butlast lst)` | потрібна реалізація |
| `(remove x lst)` | потрібна реалізація |
| `(let* (...) ...)` | вже є в My Lisp ✅ |
| `(assoc k alist)` | вже є в My Lisp ✅ |
| `(defmacro ...)` | вже є в My Lisp ✅ |

---

## 3. Що потрібно від VM (Мінімальний список)

Для того щоб `(derive-Bavati)` виконалась успішно, потрібні:

### 3.1 Обов'язкові примітиви (вже є в My Lisp)
```
cons car cdr list quote lambda def cond let let*
assoc member? not eq
```

### 3.2 Що треба додати або перевірити
```
reverse    — для (last lst)
append     — для склеювання списків
butlast    — або реалізувати через reverse/cdr/reverse
```

### 3.3 НЕ потрібно (навмисно не використовуємо)
```
defclass / defstruct   — ми використовуємо a-lists, не OOP
mutable state          — всі трансформації повертають нові списки
```

---

## 4. Ключова Архітектурна Ідея (для розуміння)

Наш Rule Engine побудований на **трьох принципах**:

**Принцип 1: Term = a-list**
```lisp
;; Кожна морфема — це a-list:
((upadesha . (B U))
 (text     . (B U))    ; змінюється
 (type     . dhAtu)
 (tags     . ()))      ; теги додаються, не видаляються
```

**Принцип 2: Трансформація незмінна**
```lisp
;; Кожна функція ПОВЕРТАЄ НОВИЙ term, не мутує старий
(term-add-tag term 'sArvaDAtukaM)  ; → новий term
(term-set-text term '(B o))        ; → новий term
```

**Принцип 3: Теги передають інформацію між правилами**
```lisp
;; Rule 7.3.84 не знає про конкретний символ 'S' у Śap.
;; Вона лише перевіряє тег, який встановила попередня rule:
(if (term-has-tag next-suffix 'sArvaDAtukaM)
    (apply-guRa dhatu) ...)
```

---

## 5. Перший Тест

Після виправлення синтаксису — запустити:
```lisp
(derive-Bavati)
```

**Очікуваний результат:**
```lisp
;; Фінальна Prakriya повинна містити три терми:
;; term 1: ((upadesha B U) (text B a v) (type dhAtu) (tags (sArvaDAtukaM ...)))
;; term 2: ((upadesha S a p) (text a) (type vikarana) (tags (sArvaDAtukaM p-it)))
;; term 3: ((upadesha t i p) (text t i) (type tiN) (tags (p-it)))
;;
;; Конкатенація text полів: B a v + a + t i = "Bavati"
```

---

## 6. Посилання

- Трасований приклад: [`examples/derivations/Bavati.md`](../examples/derivations/Bavati.md)
- Rule Engine: [`machine/rules.my`](../machine/rules.my)
- My Lisp core: [`C:/GitHub/my-lisp/lib/core.my`](file:///C:/GitHub/my-lisp/lib/core.my)
- My Lisp contract: [`C:/GitHub/my-lisp/language-contract.my`](file:///C:/GitHub/my-lisp/language-contract.my)

## 7. Статус синтаксичної конверсії (2026-08-14)

Задача `PANINI-BRIDGE-MY-LISP-SYNTAX-CONVERSION` виконана. Усі файли
`panini/machine/` тепер у документованій My Lisp формі
`(def name (lambda (...) ...))`:

| Файл | Стан |
|------|------|
| `runtime-prelude.my` | `def`-форма, без `defun`/`setq` |
| `compiler.my`, `meta.my`, `siva-sutras.my` | `def`-форма |
| `rules.my` | `def`-форма (45 визначень) |
| `panini-core.my` | конвертовано: `defun`→`def`+`lambda`, `setq`→`def`, `'()`→`list` |
| `tests.my` | `def`-форма (18 тест-функцій) |

Синтаксичні правила, яких дотримано:

1. Заборонені форми у файлах `machine/`: `defun`, `setq`, `let*` (поза
   prelude), bare-`defmacro`. Перевірено grep-ом: 0 збігів.
2. `assoc` повертає саму пару і ламається на ведучому голому символі списку;
   тому alist-и будуються як `(list (cons 'key val) ...)`, а action-graph
   має `(cons 'action-id ...)` замість голих `action-gam` на першому місці.
3. Data-реєстри у `panini-core.my` подано через `(def name (list ...))` без
   `setq` і без `'(...)`.

Перевірка: `panini-core.my` завантажується в реальному My Lisp runtime і
проходить 5 нових smoke-асерцій (`test-panini-core-syntax`); повний acceptance
— 62/62 PASS.

