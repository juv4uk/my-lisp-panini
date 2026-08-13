# Paribhāṣā — Мета-Правила Граматики Паніні

Цей документ досліджує `paribhAzA` як клас особливих правил, що керують
застосуванням інших правил. Це найважливіший концептуальний фундамент для
побудови нашого Inference Engine.

## [PANINI]

### Що таке Paribhāṣā?

`paribhAzA` — це "правила про правила". На відміну від `viDi-sUtra`
(об'єктних правил, що описують мову), `paribhAzA` описують, **як читати
і застосовувати** об'єктні правила.

Паніні не зібрав їх в одному місці. Вони розсіяні по `azwADyAyI`, і деякі є
неявними (виведеними з практики). Систематизацію здійснив Наґеша Бгатта (~1700
н.е.) у `paribhAzenduSeKara` (~133 paribhāṣā).

### Чотири Типи Paribhāṣā

```
1. saMjYA-paribhAzA     → визначення термінів (meta-vocabulary)
2. viDi-paribhAzA       → умови застосування правил
3. niyama-paribhAzA     → обмеження (restrictions)
4. adhikAra-paribhAzA   → область дії (scope rules)
```

---

### Чотири типи sūtra (не плутати з "Чотири типи paribhāṣā" вище)

Прогалина, знайдена в `PANINI-GRAMMAR-REFERENCE-CROSSCHECK` (див.
[`research/grammar-reference-crosscheck.md`](../research/grammar-reference-crosscheck.md)):
`reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md` §1 наводить
таблицю з 7 типів sūtra, з яких `saMjYA`/`aDikAra`/`anuvftti` вже
досліджені в цьому репозиторії (`samjna.md`, `anuvrtti.md`), а 4 інших
— ні. Ось вони, коротко (кожен потребує окремого поглибленого
дослідження в майбутньому, це лише перше визначення):

- **`viDi`** (विधि, "операційне") — правило, що реально щось *робить*:
  замінює, видаляє, приєднує звук чи морфему. Це "виконавчий" тип
  sūtra — на відміну від `saMjYA` (яке лише називає), `viDi` змінює
  форму. Приклад: 7.3.84 (`guRa`-заміна) — типовий `viDi`.
- **`niyama`** (नियम, "обмеження") — правило, що звужує область дії
  іншого, ширшого правила, не скасовуючи його повністю. Відрізняється
  від `apavAda` (виняток, що повністю замінює загальне правило в
  своїй вужчій області) тим, що `niyama` лише *обмежує вибір* серед
  уже дозволених варіантів, не вводить нову дію.
- **`atideSa`** (अतिदेश, "розширення") — правило формату "розглядай X
  як Y" — переносить властивості/поведінку одного класу об'єктів на
  інший, який формально ним не є. `sTAnivad-bhAva` (P5 вище, sūtra
  1.1.56) — класичний приклад `atideSa`: замінник (`Adeza`)
  розглядається "як" оригінал (`sTAnin`) для подальших правил, хоча
  формально є іншим об'єктом.
- **`paribhASA`** (परिभाषा) — див. основний розділ цього документа;
  єдиний із чотирьох, для якого в цьому репозиторії вже є глибоке
  дослідження.

**[MY-LISP HYPOTHESIS] щодо цього розрізнення:** якщо
`panini-machine-model-v0.1` колись моделюватиме типи правил окремими
тегами, `viDi` й `atideSa` — це, ймовірно, різні *ефекти* виконання
правила (мутація стану vs. розширення застосовності іншого правила),
тоді як `niyama` — це *модифікатор* застосовності самого `viDi`, а не
окремий тип дії. Це припущення, не факт — жодне з чотирьох понять
глибоко не досліджене окремо в цій задачі, лише визначене на рівні
словника.

## Ключові Paribhāṣā з Academic Sources

### P1: vipratiSeDe paraM kAryam (1.4.2)

**Текст SLP1:** `vipratiSeDe paraM kAryam`
**IAST:** vipratiṣedhe paraṃ kāryam

"Коли два рівносильних правила конфліктують, застосовується те, що стоїть
пізніше в azwADyAyI (para = later)."

Це **default** (останній ресурс) для вирішення конфліктів. Застосовується
лише коли правила є `tulyabala` (рівносильні) — жодне з нижчих принципів
не може вирішити конфлікт.

### P2: apavAdo balIyAn (utsarga-apavāda)

"Виняток (apavAda) завжди перемагає загальне правило (utsarga)."

Це не окрема сутра, а принцип, що діє через **структуру** azwADyAyI. Якщо
два правила застосовні й одне є специфічнішим (narrower scope), специфічне
перемагає, навіть якщо воно стоїть РАНІШЕ по номеру.

```
utsarga: загальне правило (широке застосування)
apavAda: виняток (вужче, специфічне)
→ apavAda > utsarga (незалежно від позиції)
```

### P3: antararaMga > bAhiraMga

"Внутрішнє правило (antaraMga) перемагає зовнішнє (bAhiraMga)."

`antaraMga` — правило, умови якого виконуються в більш вузькому
(внутрішньому) домені деривації.
`bAhiraMga` — правило, умови якого залежать від зовнішнього контексту.

Це стосується ситуацій **одночасного** спрацювання — правило, що діє в
"ближчому" контексті, має пріоритет.

### P4: nitya > anitya

"Постійне (nitya) правило перемагає непостійне (anitya)."

Правило є `nitya` (обов'язковим), якщо його застосування залишається
коректним **незалежно** від того, чи застосовано конкуруюче правило.
Тобто: якщо навіть після конкуруючого правила умова все ще справджується,
це `nitya`.

### P5: sTAnivad-bhAva (1.1.56)

**Текст SLP1:** `sTAnivadAdeSo'nalvidhO` (виправлено 2026-08-13,
`PANINI-RULE-KINDS-VIDHI-ETC` — попередній текст
"`sTAnivad Adezo'nalogitAyAm`" мав спотворене закінчення, не звірене
проти джерела; звірено проти `sanskrit/learnsanskrit.org`,
`data/ashtadhyayi-rules.txt`, з конвертацією їхньої нестандартної
конвенції `z`=ś у справжній SLP1 `S`=ś, підтверджений
`PANINI-DHATUPATHA-SOURCE-VERIFICATION`)

"Замінник (Adeza) діє як оригінал (sTAnin) для наступних правил,
за винятком правил про звуки (*al*-vidhi, буквально "правило про [окремий]
звук" — `al` тут pratyAhAra, що охоплює всі звуки)."

Це принцип **зворотної сумісності**: коли одну форму замінено іншою,
наступні правила "бачать" оригінальну форму, не замінник.

Наприклад, якщо `U` → `o` (guṇa), то наступні правила про наголос
або сандгі, які залежали від наявності `U`, все ще спрацьовують — бо
замінник `o` "поводиться як" `U` для певних правил.

---

## Ієрархія Пріоритетів (Priority Hierarchy)

З академічних джерел (Università Ca' Foscari Venezia, Kiparsky):

```
КОНФЛІКТ ПРАВИЛ
       │
       ▼
1. antaraMga > bAhiraMga?  ← перевіряємо першим
       │ ні
       ▼
2. nitya > anitya?          ← постійне vs непостійне
       │ ні
       ▼
3. apavAda > utsarga?       ← виняток vs загальне
       │ ні
       ▼
4. vipratiSeDe paraM kAryam ← DEFAULT: пізніше в тексті перемагає
       │
       ▼
     РЕЗУЛЬТАТ
```

**Важливо:** Кроки 1-3 мають пріоритет над кроком 4. Кожен крок
перевіряється по черзі, і якщо конфлікт вирішено — решта кроків пропускається.

---

## [INTERPRETATION]

Дослідники (Unive.it, 2024) підкреслюють:

> "The rules 1-3 must be checked before resorting to 1.4.2. Only when
> conflicting rules are deemed tulyabala (equally powerful) — meaning they
> do not fall into nitya-anitya, antaraṅga-bahiraṅga, or apavāda-utsarga
> — the later rule in serial order prevails."

Це означає, що `vipratiSeDe paraM kAryam` (1.4.2) — **не** головний
алгоритм. Це лише останній fallback. Більшість реальних конфліктів
вирішується через P2 або P3.

---

## [MY-LISP HYPOTHESIS]

### Paribhāṣā як Meta-level Rule Dispatch

У нашій VM paribhāṣā — це **мета-рівень диспетчеризації** (`defmacro` рівень).
Коли Inference Engine знаходить два правила, що можуть застосуватись
до одного стану, він викликає не правила напряму — він викликає
`resolve-conflict`, який сам є реалізацією paribhāṣā:

```lisp
;; [MY-LISP HYPOTHESIS]
;;
;; resolve-conflict — реалізація ієрархії paribhAzA.
;; Приймає два конкуруючих правила і стан prakriyA.
;; Повертає єдине правило, яке треба застосувати.
;;
(def resolve-conflict
  (lambda (rule-a rule-b prakriya)
    (cond
      ;; P3: antaraMga > bAhiraMga
      ((antaraMga? rule-a prakriya) rule-a)
      ((antaraMga? rule-b prakriya) rule-b)
      ;; P4: nitya > anitya
      ((and (nitya? rule-a prakriya) (not (nitya? rule-b prakriya))) rule-a)
      ((and (nitya? rule-b prakriya) (not (nitya? rule-a prakriya))) rule-b)
      ;; P2: apavAda > utsarga
      ((apavada-of? rule-a rule-b) rule-a)
      ((apavada-of? rule-b rule-a) rule-b)
      ;; P1: vipratiSeDe paraM kAryam (1.4.2) — DEFAULT
      ((later-in-ashtadhyayi? rule-a rule-b) rule-a)
      (t rule-b))))
```

### Що Визначає "Пізніше в Тексті"?

Кожне правило у нашому реєстрі має числовий ID — наприклад `"7.3.84"`.
Порівняння "пізніше" = порівняння числових ID як tuple `(adhyAya, pada, sutra)`:

```lisp
;; Розбирає "7.3.84" → (7 3 84) для порівняння
(def parse-sutra-id
  (lambda (id-str)
    ;; ... split by '.' → list of integers
    ))

;; Повертає t, якщо rule-a стоїть пізніше в azwADyAyI
(def later-in-ashtadhyayi?
  (lambda (rule-a rule-b)
    (sutra-gt? (rule-id rule-a) (rule-id rule-b))))
```

### Paribhāṣā як `defmacro` (підтверджена гіпотеза)

Ключова ідея: paribhāṣā **не є** об'єктними правилами. Вони не додають суфіксів
і не змінюють звуки. Вони визначають **умови застосування** інших правил.

У Lisp це `defmacro` — код, що виконується до виконання основного коду.
В нашому Rule Engine paribhāṣā — це **мета-функції**, що обгортають
механізм dispatch:

```
                 Rule Engine
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
  [Object Rules]            [Meta Rules / paribhAzA]
  (viDi-sUtra)             (resolve-conflict logic)
  - rule-7-3-84            - antaraMga?
  - rule-6-1-78            - nitya?
  - rule-3-1-68            - apavada-of?
                           - later-in-ashtadhyayi?
```

Це **двошарова архітектура** нашого Rule Engine:
- Шар 1: декларативні правила (a-lists у `rules.my`)
- Шар 2: мета-логіка dispatching (paribhāṣā у `meta.my`)

---

## Наступні Кроки

1. Реалізувати `resolve-conflict` у новому файлі `panini/machine/meta.my`.
2. Додати числові ID до наших правил у `rules.my`.
3. Трасувати `dadAti` — деривацію, де реально виникає конфлікт між
   правилами і потрібна ієрархія paribhāṣā для його вирішення.
