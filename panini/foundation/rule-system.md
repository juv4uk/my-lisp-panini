# rule-system: конфлікти правил (`vipratiSeDa`)

Статус: v0.1 (`PANINI-RULE-CONFLICTS-VIPRATISEDHA`).

## English

This document separates three layers: the Pāṇinian rule at Aṣṭādhyāyī 1.4.2,
its traditional interpretation, and a possible machine design. `vipratiSeDa`
is not a blanket "last rule wins" instruction. In this foundation it is a
residual tie-breaker: when two applicable rules conflict and neither is the
more specific exception (`apavAda`) of the other general rule (`utsarga`), the
later rule in the text is selected. This statement is subject to the cited
source-verification limits below.

The implementation observation about Vidyut is not a claim about Pāṇini:
Vidyut's imperative execution order can encode priority statically. A future
My Lisp inference engine could instead model conflict selection dynamically,
but neither architecture follows automatically from the sūtra. The remaining
research questions concern the exact hierarchy of `paribhAzA` / `nyAya` and
how Vidyut represents the general-rule/exception relation.

## Українська

Документ строго відокремлює три рівні: правило Паніні в Aṣṭādhyāyī 1.4.2,
традиційне тлумачення та можливий машинний дизайн. `vipratiSeDa` не означає
загального правила «перемагає останнє». У цьому фундаменті це залишковий
tie-breaker: коли два застосовні правила конфліктують і жодне не є
спеціальнішим винятком (`apavAda`) іншого загального правила (`utsarga`),
обирається пізніше правило тексту. Твердження обмежене станом верифікації
джерел, зазначеним нижче.

Спостереження про Vidyut не є твердженням про Паніні: його імперативний порядок
виконання може статично кодувати пріоритет. Майбутній inference engine My Lisp
міг би моделювати вибір конфлікту динамічно, але жодна архітектура не випливає
автоматично із sūtra. Відкритими лишаються точна ієрархія `paribhAzA` / `nyAya`
та спосіб, яким Vidyut представляє відношення загального правила і винятку.

## Deutsch

Das Dokument trennt drei Ebenen: die Pāṇini-Regel in Aṣṭādhyāyī 1.4.2, ihre
traditionelle Interpretation und einen möglichen Maschinenentwurf.
`vipratiSeDa` bedeutet nicht pauschal "die letzte Regel gewinnt". Es ist hier
ein verbleibender Tie-Breaker: Stehen zwei anwendbare Regeln im Konflikt und
ist keine die spezifischere Ausnahme (`apavAda`) der allgemeinen Regel
(`utsarga`) der anderen, wird die spätere Regel des Textes gewählt. Diese
Aussage unterliegt den unten genannten Grenzen der Quellenprüfung.

Die Beobachtung zu Vidyut ist keine Pāṇini-Behauptung: Eine imperative
Ausführungsreihenfolge kann Priorität statisch kodieren. Ein zukünftiger
My-Lisp-Inference-Engine könnte Konflikte dynamisch auflösen; keine der beiden
Architekturen folgt jedoch automatisch aus dem Sūtra. Offen bleiben die genaue
Hierarchie von `paribhAzA` / `nyAya` und Vidyuts Modellierung von
Allgemeinregel und Ausnahme.

## [PANINI]

`vipratiSeDa` (विप्रतिषेध, "взаємне заперечення/конфлікт") —
ситуація, коли до одного й того самого мовного матеріалу застосовні
**два різні правила**, що дають різні результати. Механізм розв'язання
заданий sūtra **1.4.2** `vipratiSeDe paraM kAryam` — "у разі конфлікту,
[застосовується] пізніше [за текстовим порядком] правило" (`para` тут
означає "пізніше в тексті Aṣṭādhyāyī", не "пізніше в часі виконання").

### Це не єдиний і не основний механізм пріоритету

Важливо не плутати `vipratiSeDa` (1.4.2) із загальнішим і частіше
застосовуваним принципом `utsarga`–`apavAda` (загальне правило →
спеціальний виняток), який уже згадувався при звірці з
`reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md`
(`PANINI-GRAMMAR-REFERENCE-CROSSCHECK`,
[`research/grammar-reference-crosscheck.md`](../research/grammar-reference-crosscheck.md)):

- **`utsarga`–`apavAda`**: коли одне правило є *окремим випадком*
  іншого (домен одного правила — підмножина домену іншого),
  спеціальніше правило перемагає **незалежно від порядку в тексті**.
  Це базовий, найпоширеніший принцип пріоритету в Aṣṭādhyāyī.
- **`vipratiSeDa` (1.4.2)**: застосовується **лише тоді, коли жодне з
  двох правил не є окремим випадком іншого** (домени перетинаються, але
  жоден не включає інший повністю) — тобто це механізм для *залишкових*
  конфліктів, які `utsarga`–`apavAda` не може розв'язати через
  відношення включення доменів. У цьому вужчому випадку рішення суто
  формальне: перемагає те правило, що йде пізніше в лінійному порядку
  тексту Aṣṭādhyāyī.

Це ключове структурне уточнення: `vipratiSeDa` — не головний механізм
розв'язання конфліктів, а **резервний**, що спрацьовує, коли
основний принцип (спеціальність домену) не дає відповіді.

## [INTERPRETATION]

Традиційна коментаторська традиція (Mahābhāṣya та пізніші
`paribhAzA`-збірники) обговорює додаткові `nyAya` (інтерпретивні
максими), які фактично застосовуються *до* звернення до 1.4.2 —
наприклад, принципи на кшталt "правило, що спирається на вужчу
(`antaraNga`) умову, застосовується раніше за правило з ширшою
(`bahiraNga`) умовою" чи пріоритет обов'язкових (`nitya`) правил над
факультативними. Це означає: реальний порядок розв'язання конфлікту в
традиції — це **ієрархія кількох принципів**, де текстовий порядок
(1.4.2) — лише останній інструмент, коли жоден вищий принцип не
спрацював. Точний повний перелік і порядок цих принципів **не
досліджений вичерпно в цій задачі** — це велика окрема тема
`paribhAzA`-літератури (`PANINI-RULE-KINDS-VIDHI-ETC` частково
торкається `paribhAzA` як типу правила, але не цієї конкретної
ієрархії).

Порівняння з нашим твердженням у `PANINI-VIDYUT-AUDIT`: Vidyut кодує
кожен крок деривації через явний `Rule`-тип із джерелом і номером —
але сам порядок *застосування* конкретних правил у коді Vidyut
визначається порядком виклику Rust-функцій в imperативному конвеєрі
(`ashtadhyayi.rs`, не досліджено детально в цій задачі), а не
обчислюється динамічно за принципом `vipratiSeDa`/`utsarga`-`apavAda`
під час виконання. Це важлива відмінність: **реальна виробнича
реалізація "зашиває" порядок конфлікт-резолюції на етапі написання
коду**, а не моделює сам принцип 1.4.2 як загальний рушій — сильний
сигнал для `[MY-LISP HYPOTHESIS]` нижче.

## [MY-LISP HYPOTHESIS]

Якщо `panini-machine-model-v0.1` колись реалізовуватиме
конфлікт-резолюцію, на основі спостереження вище є дві принципово різні
архітектури:

1. **Статичний порядок** (як у Vidyut) — послідовність застосування
   правил визначена наперед розробником/компілятором, `vipratiSeDa` як
   принцип ніколи не обчислюється явно під час виконання — він уже
   "вкомпільований" у порядок виклику функцій.
2. **Динамічний inference** — рушій, що на кожному кроці перевіряє
   набір застосовних правил і сам обчислює пріоритет за ієрархією
   `utsarga`-`apavAda` → (нижчі `nyAya`, не досліджені тут) →
   `vipratiSeDa` (1.4.2) як останній tie-breaker.

Жоден варіант не диктується напряму джерелом — це архітектурне
рішення, яке `AGENTS.md` §12 явно віддає на розсуд подальшого
проєктування, не Paninian факт. Важливо, що навіть найсерйозніша наявна
реалізація (Vidyut) обрала варіант (1), а не (2) — вартий уваги
прецедент, але не доказ, що (2) неможливий чи гірший для наших цілей
(символьний ШІ, а не лише генерація форм).

## Відкриті питання

- Повний перелік `nyAya`/`paribhAzA`, що передують `vipratiSeDa` в
  реальній традиції розв'язання конфліктів — не досліджено.
- Чи Vidyut десь явно моделює `utsarga`-`apavAda` як перевірку домену
  на етапі виконання (а не лише порядком коду) — не перевірено
  (`ashtadhyayi.rs` не прочитаний у цій задачі).
- Зв'язок із задачею `PANINI-PRATYAYA-DERIVATION` — там залишилось
  відкритим питання "як розв'язується конкуренція кількох застосовних
  `pratyaya`" — ця задача дає часткову відповідь (спершу
  `utsarga`-`apavAda`, потім, за відсутності, 1.4.2), але не вичерпну.

## Джерела

- Aṣṭādhyāyī sūtra 1.4.2 — **не звірено** проти цифрового джерела в
  цій задачі (правило 17, `AGENTS.md`) — TODO для
  `PANINI-SUTRA-CITATION-VERIFICATION`.
- `reference-from-engineer-1/PANINI-GRAMMAR-REFERENCE.md` §1 (таблиця
  типів правил) — джерело початкового розрізнення `utsarga`-`apavAda`
  vs. інших типів, вже звірене в `PANINI-GRAMMAR-REFERENCE-CROSSCHECK`.
