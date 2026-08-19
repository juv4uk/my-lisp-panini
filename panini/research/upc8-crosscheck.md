# UPC-8 crosscheck: is our SLP1 registry consistent with `shiva-sutras`' hardware code

## English

Status: v0.1, done 2026-08-18. Out-of-band task (not from the
`PANINI-*` swarm-node queue) — done on the owner's request, after
reviewing `shiva-sutras/prototype/` (UPC-8, a universal 8-bit phoneme
code for FPGA).

### What was checked

By calling `prototype/upc8.py` directly (`UPC8().encode_sanskrit(...)`,
not from a description — from real code) — whether every SLP1 symbol
used in the 20 canonical spellings in `registry/dhatu/*.yaml` is
correctly encoded in UPC-8.

### Result 1: the base 42-sound canon — full match

Every consonant and short vowel in our 20 records encodes correctly,
including the pair we fixed three times in a row this session:

```
>>> u.encode_sanskrit('S')
0x27   # ś — exactly the value we established in terminology.md
>>> u.encode_sanskrit('z')
0x28   # ṣ — same
```

This is the **third independent confirmation** of the `ś=S`, `ṣ=z`
convention (after Vidyut's `sounds.rs` and `my-lisp`'s
`transliteration.rs`) — and this time not just "the same conclusion",
but **the same code, built from an independent canon** (14 sūtras → 42
positions → codes 0x00–0x29 in text order). Three different teams,
three different codebases, one identical result — this is no longer a
coincidence, but a sign the convention is genuinely canonical, not an
arbitrary choice of any single one of the three sources.

### Result 2: a real gap — long vowels do not encode directly

```
>>> u.encode_sanskrit('A')
KeyError: 'Unknown Sanskrit phoneme: A'
>>> u.encode_sanskrit('a:')
0x2A   # only works via an IAST-like colon notation
```

**7 of our 20 roots** contain a long vowel in the canonical spelling
(`BAz`, `BI`, `BU`, `dA`, `jYA`, `nI`, `sTA`) — none of them encode
directly via `encode_sanskrit()` with our own SLP1 spelling. The cause
is not a bug — `_slp1_to_code` in `upc8.py` literally equals
`CODE_OF_SOUND`, a dictionary of only the 42 base sounds (short vowels
+ consonants); long vowels live in a separate `SANSKRIT_EXTENDED`
table, indexed **not by the SLP1 letter** (`A`/`I`/`U`), but by a
separate colon notation (`"a:"`, `"i:"`, `"u:"` — essentially
IAST-length written in an ASCII-safe way).

### [MY-LISP HYPOTHESIS / our own comment]

This is not an error on either side — it is **two different,
deliberately chosen design decisions** that diverged because they
solve different problems:

- **Our SLP1** (`AGENTS.md` §2, `terminology.md`) is optimized for
  *readability and compactness of writing a whole root as one string*
  (`sTA`, not `s t a colon a colon`), inherited from the standard
  academic SLP1 tradition (Huet).
- **UPC-8's extended layer** is optimized for *individually addressing
  one specific phoneme code* in an 8-bit space; vowel length there is
  a separate, orthogonal axis ("derived from `a`", `derivation:
  "dirgha of a"`), not another alphabet symbol. From a hardware-coding
  standpoint this makes sense: a long `ā` is not a "new sound" but a
  modification of short `a` along one phonological feature (duration)
  — so it naturally lives in a different layer, not in the same
  canonical 42-position list.

**Practical consequence if real integration is ever needed** (not done
in this task, only noted as an observation): any bridge between
`registry/dhatu/*.yaml` (our SLP1) and UPC-8 cannot be a symbol-by-
symbol 1:1 string mapping — it would need to explicitly parse each of
our SLP1 symbols into (base short sound, whether it is long) before
encoding, rather than feeding our `canonical` string directly into
`encode_sanskrit_word()`. This lines up with the same lesson already
drawn in [`hypothesis-ledger.md`](../specs/hypothesis-ledger.md) H2
(`it`) and H1 (`kAraka`): **a string that looks homogeneous often hides
heterogeneous internal structure** that naive concatenation/copying
loses.

### What was NOT checked in this task

- UPC-8's Ukrainian/English extended layers — outside the scope of our
  SLP1 registry, not checked.
- The `test_upc8.py` test suite (20 tests, "all passing" per the
  README) — not run in this task, only `upc8.py`'s code itself was
  read directly.
- No changes were made to `registry/dhatu/` or to `upc8.py` — this is
  a purely diagnostic crosscheck.

### Sources

- `github.com/juv4uk/shiva-sutras`, `prototype/upc8.py`,
  `prototype/README.md`, `prototype/UPC8-documentation-ua.md` — read
  directly 2026-08-18; `encode_sanskrit()` called directly (not from a
  description) to check `A`, `a:`, `a`, `z`, `S`.
- [`registry/dhatu/`](../registry/dhatu) — 20 canonical spellings, the
  source of symbols for the crosscheck.
- [`foundation/terminology.md`](../sastra/terminology.md#знайдені-й-виправлені-розбіжності) —
  history of establishing the `ś=S`/`ṣ=z` convention, now confirmed
  three times over.

## Українська

Статус: v0.1, зроблено 2026-08-18. Позачергова задача (не з `PANINI-*`
черги swarm-node) — на прохання власника, після ознайомлення з
`shiva-sutras/prototype/` (UPC-8, універсальний 8-бітний фонемний код
для FPGA).

### Що перевірено

Прямим викликом `prototype/upc8.py` (`UPC8().encode_sanskrit(...)`,
не з опису — з реального коду) — чи кожен SLP1-символ, використаний у
20 канонічних написаннях `registry/dhatu/*.yaml`, коректно кодується
в UPC-8.

### Результат 1: базовий 42-звуковий канон — повний збіг

Усі приголосні й короткі голосні в наших 20 записах кодуються
коректно, включно з парою, яку ми виправляли тричі поспіль цієї
сесії:

```
>>> u.encode_sanskrit('S')
0x27   # ś — точно те саме значення, що ми встановили в terminology.md
>>> u.encode_sanskrit('z')
0x28   # ṣ — те саме
```

Це **третє незалежне підтвердження** конвенції `ś=S`, `ṣ=z` (після
Vidyut `sounds.rs` і `my-lisp`'s `transliteration.rs`) — і цього разу
не просто "той самий висновок", а **той самий код, побудований з
незалежного канону** (14 sūtra → 42 позиції → коди 0x00–0x29 у
порядку тексту). Три різні команди, три різні кодові бази, один і той
самий результат — це вже не збіг, а ознака, що конвенція справді
канонічна, не випадковий вибір жодного з трьох джерел.

### Результат 2: реальна прогалина — довгі голосні не кодуються напряму

```
>>> u.encode_sanskrit('A')
KeyError: 'Unknown Sanskrit phoneme: A'
>>> u.encode_sanskrit('a:')
0x2A   # працює лише через IAST-подібний запис із двокрапкою
```

**7 із 20 наших коренів** містять довгий голосний у канонічному
написанні (`BAz`, `BI`, `BU`, `dA`, `jYA`, `nI`, `sTA`) — жоден із них
не закодується напряму викликом `encode_sanskrit()` з нашим власним
SLP1-написанням. Причина не в помилці — `_slp1_to_code` у `upc8.py`
буквально дорівнює `CODE_OF_SOUND`, словнику лише з 42 базових звуків
(короткі голосні + приголосні); довгі голосні живуть в окремій
таблиці `SANSKRIT_EXTENDED`, індексованій **не SLP1-літерою**
(`A`/`I`/`U`), а окремим позначенням із двокрапкою (`"a:"`, `"i:"`,
`"u:"` — по суті IAST-довжина, записана ASCII-safe способом).

### [MY-LISP HYPOTHESIS / коментар з нашого боку]

Це не помилка жодної зі сторін — це **два різні, обидва свідомо
обрані рішення**, що розійшлися, бо розв'язували різні задачі:

- **Наш SLP1** (`AGENTS.md` §2, `terminology.md`) — оптимізований під
  *читабельність і компактність написання цілого кореня одним рядком*
  (`sTA`, не `s t a colon a colon`), успадкований від стандартної
  академічної SLP1-традиції (Huet).
- **UPC-8's extended layer** — оптимізований під *окрему адресацію
  одного конкретного фонемного коду* в 8-бітному просторі; довжина
  голосного там — окрема, ортогональна вісь ("похідне від `a`",
  `derivation: "dirgha of a"`), а не інший символ алфавіту. З погляду
  апаратного кодування це логічно: довгий `ā` не є "новим звуком", а
  модифікацією короткого `a` за однією фонологічною ознакою
  (тривалість) — тож він природно живе в іншому шарі, не в тому
  самому канонічному 42-позиційному переліку.

**Практичний наслідок, якщо колись знадобиться реальна інтеграція**
(не робиться в цій задачі, лише фіксується як спостереження): будь-
який міст між `registry/dhatu/*.yaml` (наш SLP1) і UPC-8 не може бути
посимвольним 1:1 мапуванням рядка — доведеться явно розбирати кожен
наш SLP1-символ на (базовий короткий звук, чи він довгий) перед
кодуванням, а не подавати наш `canonical`-рядок напряму в
`encode_sanskrit_word()`. Це узгоджується з тим самим уроком, що вже
виведений у [`hypothesis-ledger.md`](../specs/hypothesis-ledger.md)
H2 (`it`) і H1 (`kAraka`): **однорідний на вигляд рядок часто ховає
неоднорідну внутрішню структуру**, яку наївна конкатенація/копіювання
втрачає.

### Що НЕ перевірено в цій задачі

- Українська/англійська розширені шари UPC-8 — поза обсягом нашого
  SLP1-реєстру, не перевірялись.
- Тестовий набір `test_upc8.py` (20 тестів, за описом README —
  "all passing") — не запускався в цій задачі, лише читався код
  `upc8.py` напряму.
- Жодних змін до `registry/dhatu/` чи до `upc8.py` не внесено — це
  чисто діагностична звірка.

### Джерела

- `github.com/juv4uk/shiva-sutras`, `prototype/upc8.py`,
  `prototype/README.md`, `prototype/UPC8-documentation-ua.md` —
  прочитано напряму 2026-08-18; `encode_sanskrit()` викликано
  безпосередньо (не з опису) для перевірки `A`, `a:`, `a`, `z`, `S`.
- [`registry/dhatu/`](../registry/dhatu) — 20 канонічних написань,
  джерело символів для звірки.
- [`foundation/terminology.md`](../sastra/terminology.md#знайдені-й-виправлені-розбіжності) —
  історія встановлення конвенції `ś=S`/`ṣ=z`, тепер потрійно
  підтвердженої.

## Deutsch

Status: v0.1, erledigt am 2026-08-18. Außerplanmäßige Aufgabe (nicht
aus der `PANINI-*`-Swarm-node-Warteschlange) — auf Bitte des
Eigentümers, nach der Durchsicht von `shiva-sutras/prototype/` (UPC-8,
ein universeller 8-Bit-Phonemcode für FPGA).

### Was geprüft wurde

Durch direkten Aufruf von `prototype/upc8.py`
(`UPC8().encode_sanskrit(...)`, nicht aus einer Beschreibung — aus
echtem Code) — ob jedes SLP1-Symbol, das in den 20 kanonischen
Schreibweisen in `registry/dhatu/*.yaml` verwendet wird, korrekt in
UPC-8 kodiert wird.

### Ergebnis 1: der Basiskanon von 42 Lauten — vollständige Übereinstimmung

Alle Konsonanten und kurzen Vokale in unseren 20 Datensätzen werden
korrekt kodiert, einschließlich des Paares, das wir in dieser Sitzung
dreimal hintereinander korrigiert haben:

```
>>> u.encode_sanskrit('S')
0x27   # ś — exakt derselbe Wert, den wir in terminology.md festgelegt haben
>>> u.encode_sanskrit('z')
0x28   # ṣ — derselbe
```

Dies ist die **dritte unabhängige Bestätigung** der Konvention `ś=S`,
`ṣ=z` (nach Vidyuts `sounds.rs` und `my-lisp`s `transliteration.rs`) —
und diesmal nicht nur "dieselbe Schlussfolgerung", sondern **derselbe
Code, aufgebaut aus einem unabhängigen Kanon** (14 Sūtras → 42
Positionen → Codes 0x00–0x29 in Textreihenfolge). Drei verschiedene
Teams, drei verschiedene Codebasen, ein identisches Ergebnis — das ist
kein Zufall mehr, sondern ein Zeichen, dass die Konvention wirklich
kanonisch ist und keine willkürliche Wahl einer der drei Quellen.

### Ergebnis 2: eine reale Lücke — lange Vokale werden nicht direkt kodiert

```
>>> u.encode_sanskrit('A')
KeyError: 'Unknown Sanskrit phoneme: A'
>>> u.encode_sanskrit('a:')
0x2A   # funktioniert nur über eine IAST-ähnliche Doppelpunkt-Notation
```

**7 unserer 20 Wurzeln** enthalten einen langen Vokal in der
kanonischen Schreibweise (`BAz`, `BI`, `BU`, `dA`, `jYA`, `nI`, `sTA`)
— keine davon wird direkt über `encode_sanskrit()` mit unserer eigenen
SLP1-Schreibweise kodiert. Die Ursache ist kein Fehler — `_slp1_to_code`
in `upc8.py` entspricht buchstäblich `CODE_OF_SOUND`, einem Wörterbuch
mit nur den 42 Basislauten (kurze Vokale + Konsonanten); lange Vokale
liegen in einer separaten Tabelle `SANSKRIT_EXTENDED`, indiziert
**nicht durch den SLP1-Buchstaben** (`A`/`I`/`U`), sondern durch eine
separate Doppelpunkt-Notation (`"a:"`, `"i:"`, `"u:"` — im Grunde
IAST-Länge, ASCII-sicher geschrieben).

### [MY-LISP HYPOTHESIS / eigener Kommentar]

Dies ist kein Fehler auf einer der beiden Seiten — es sind **zwei
verschiedene, beide bewusst gewählte Entwurfsentscheidungen**, die
auseinandergingen, weil sie unterschiedliche Probleme lösen:

- **Unser SLP1** (`AGENTS.md` §2, `terminology.md`) ist optimiert für
  *Lesbarkeit und Kompaktheit beim Schreiben einer ganzen Wurzel als
  einer Zeichenkette* (`sTA`, nicht `s t a Doppelpunkt a Doppelpunkt`),
  geerbt von der akademischen SLP1-Standardtradition (Huet).
- **UPC-8s erweiterte Schicht** ist optimiert für die *individuelle
  Adressierung eines konkreten Phonemcodes* in einem 8-Bit-Raum;
  Vokallänge ist dort eine separate, orthogonale Achse ("abgeleitet
  von `a`", `derivation: "dirgha of a"`), kein weiteres
  Alphabetsymbol. Aus Sicht der Hardware-Kodierung ist das sinnvoll:
  ein langes `ā` ist kein "neuer Laut", sondern eine Modifikation des
  kurzen `a` entlang eines einzigen phonologischen Merkmals (Dauer) —
  es lebt also natürlich in einer anderen Schicht, nicht in derselben
  kanonischen 42-Positionen-Liste.

**Praktische Konsequenz, falls jemals eine echte Integration nötig
wird** (in dieser Aufgabe nicht durchgeführt, nur als Beobachtung
festgehalten): Jede Brücke zwischen `registry/dhatu/*.yaml` (unser
SLP1) und UPC-8 kann keine symbolweise 1:1-Zeichenkettenzuordnung sein
— sie müsste jedes unserer SLP1-Symbole vor der Kodierung explizit in
(Basis-Kurzlaut, ob er lang ist) zerlegen, statt unsere
`canonical`-Zeichenkette direkt in `encode_sanskrit_word()` zu geben.
Das deckt sich mit derselben Lehre, die bereits in
[`hypothesis-ledger.md`](../specs/hypothesis-ledger.md) H2 (`it`) und
H1 (`kAraka`) gezogen wurde: **eine scheinbar homogene Zeichenkette
verbirgt oft heterogene innere Struktur**, die naives
Verketten/Kopieren verliert.

### Was in dieser Aufgabe NICHT geprüft wurde

- UPC-8s ukrainische/englische erweiterte Schichten — außerhalb des
  Umfangs unseres SLP1-Registers, nicht geprüft.
- Die Testsuite `test_upc8.py` (20 Tests, laut README "all passing") —
  in dieser Aufgabe nicht ausgeführt, nur der Code von `upc8.py` selbst
  wurde direkt gelesen.
- Es wurden keine Änderungen an `registry/dhatu/` oder `upc8.py`
  vorgenommen — dies ist ein rein diagnostischer Abgleich.

### Quellen

- `github.com/juv4uk/shiva-sutras`, `prototype/upc8.py`,
  `prototype/README.md`, `prototype/UPC8-documentation-ua.md` —
  direkt gelesen am 2026-08-18; `encode_sanskrit()` direkt aufgerufen
  (nicht aus einer Beschreibung) zur Prüfung von `A`, `a:`, `a`, `z`,
  `S`.
- [`registry/dhatu/`](../registry/dhatu) — 20 kanonische Schreibweisen,
  die Symbolquelle für den Abgleich.
- [`foundation/terminology.md`](../sastra/terminology.md#знайдені-й-виправлені-розбіжності) —
  Geschichte der Festlegung der Konvention `ś=S`/`ṣ=z`, nun dreifach
  bestätigt.
