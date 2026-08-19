# Session conclusion 2026-08-18 (my own)

## English

Status: reflection, not a task from the `PANINI-*` queue. Written on
direct request — review this session's fresh files
([`upc8-crosscheck.md`](upc8-crosscheck.md),
[`sarvam-capability-reference.md`](sarvam-capability-reference.md),
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md),
[`sastra/tripadi.md`](../sastra/tripadi.md)) and formulate my own
conclusion, not a recap of each one.

### What actually happened this session

Three, at first glance unrelated, events — the UPC-8 crosscheck, the
`shiva-sutras` reconciliation, the Sarvam test — turned out to be the
same action applied to three different targets: **don't trust a claim
until you run it through real code and see what happens.**

- When `shiva-sutras` asserted `SS-CANON-001`/`SS-PRATYAHARA-001`, I
  did not simply import them into `pratyahara.md` — I checked byte-level
  against `ksetra/canon/siva-sutras.yaml` and found one real
  discrepancy (case `Ṇ`/`ṇ`).
- When `upc8.py` appeared, I did not take the README's word for it — I
  called `encode_sanskrit()` directly and got a `KeyError` where I
  expected success. That is exactly what the difference between
  "reading a description" and "running the code" is worth.
- When Sarvam appeared, I did not ask it to confirm what we already
  know — I asked it the same cold question (`bhAṣ`→IAST) we would ask
  if we had no answer, and it got wrong exactly the thing we had
  already gotten wrong three times ourselves.

### Main technical conclusion: triple convergence is not a coincidence

`ś=S`, `ṣ=z` is now confirmed by three independent codebases (Vidyut's
`sounds.rs`, `my-lisp`'s `transliteration.rs`, `shiva-sutras`'
`upc8.py`), built from different primary sources by different teams.
When one team asserts something, that is a claim. When three
independent engineering decisions, arrived at from different
directions, converge on one specific detail, that is no longer an
opinion but a property of the material itself. This is the strongest
kind of evidence obtained during the whole session, stronger than any
single sūtra citation.

### Main conclusion about boundaries: a homogeneous string hides heterogeneous structure

This is already the third time we run into the same pattern under
different disguises:

1. `it`-markers look like one mechanism, but are actually a family of
   20+ distinct signals (`it.md`, H2 in `hypothesis-ledger.md`).
2. `kAraka` roles look like a fixed set of slots per dhātu, but
   actually depend on the specific sentence and dhātu-specific
   extensions (`dhatu-karaka-relation.md`, H1).
3. Our SLP1 string (`sTA`, `dA`, `BAz`) looks like a single, atomic
   identifier, but UPC-8 showed the long vowel inside it is a separate
   encoding axis, not part of the same alphabet as the consonants.

These are not three separate findings. This is one lesson, applied
three times to different material: **notational convenience
systematically hides internal structure from anyone looking only at
the surface of the string.** If `panini-machine-model-v0.1` is ever
written, this — not any specific hypothesis from `hypothesis-ledger.md`
— is the most important thing to remember first.

### What this means for the project's scale

`my-lisp-panini` has stopped being an isolated inquiry into "can
anything be derived from Pāṇini's grammar for a hypothetical Lisp." It
is now one node in a chain where every SLP1-spelling check we make is
literally a check of one bit in a real hardware code table
(`shiva-sutras/prototype/upc8.py`, positions `0x00`–`0x29`) already
targeting an FPGA. A transliteration error we caught in
`terminology.md` for the sake of "research purity" now has a literal,
not metaphorical, hardware consequence. This raises, not lowers, the
cost of carelessness — and it seems to me this is exactly why further
work here should keep going slower than one might want, not faster.

### What is not finished (honestly, not hidden)

- `sarvam_tools_stt_transcribe` with `sa-IN` has not been verified by a
  live call — only against contradictory external sources
  (`sarvam-capability-reference.md`).
- `panini/machine/*.my` and the UPC-8 SLP1 extract (long vowels) are
  two separate, still-unconnected gaps, both documented, neither
  fixed (and neither should be fixed unilaterally — both involve
  decisions beyond this repository alone).
- `tripAdI` (8.2.1) — the `asiDDatva` mechanism is described carefully,
  without an exhaustive list of exceptions; admitting this is part of
  the conclusion, not a shortcoming of the work.

### Sources

All facts above are a compilation of what was already written this
session, not new research: [`upc8-crosscheck.md`](upc8-crosscheck.md),
[`sarvam-capability-reference.md`](sarvam-capability-reference.md),
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md),
[`sastra/tripadi.md`](../sastra/tripadi.md),
[`sastra/pratyahara.md`](../sastra/pratyahara.md),
[`specs/hypothesis-ledger.md`](../specs/hypothesis-ledger.md).

## Українська

Статус: рефлексія, не задача з `PANINI-*` черги. Написано на пряме
прохання — переглянути свіжі файли цієї сесії
([`upc8-crosscheck.md`](upc8-crosscheck.md),
[`sarvam-capability-reference.md`](sarvam-capability-reference.md),
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md),
[`sastra/tripadi.md`](../sastra/tripadi.md)) і сформулювати власний
висновок, не переказ кожного окремо.

### Що насправді сталося цієї сесії

Три, на перший погляд не пов'язані, події — UPC-8 crosscheck, звірка з
`shiva-sutras`, тест Sarvam — виявились однією й тією самою дією,
застосованою до трьох різних цілей: **не довіряти твердженню, поки не
проженеш його через реальний код і не подивишся, що станеться.**

- Коли `shiva-sutras` заявив `SS-CANON-001`/`SS-PRATYAHARA-001`, я не
  просто імпортував їх у `pratyahara.md` — звірив byte-level проти
  `ksetra/canon/siva-sutras.yaml` і знайшов одну реальну розбіжність
  (регістр `Ṇ`/`ṇ`).
- Коли з'явився `upc8.py`, я не повірив README на слово — викликав
  `encode_sanskrit()` напряму й отримав `KeyError` там, де очікував
  успіх. Це і є те, чого варта різниця між "прочитати опис" і
  "запустити код".
- Коли з'явився Sarvam, я не попросив його підтвердити, що ми вже
  знаємо — попросив те саме холодне питання (`bhAṣ`→IAST), яке ми б
  поставили, якби не мали відповіді, і він помилився саме там, де ми
  вже тричі помилялись самі.

### Головний технічний висновок: потрійна конвергенція — не випадковість

`ś=S`, `ṣ=z` тепер підтверджено трьома незалежними кодовими базами
(Vidyut `sounds.rs`, `my-lisp`'s `transliteration.rs`, `shiva-sutras`'
`upc8.py`), збудованими з різних першоджерел і різними командами.
Коли одна команда стверджує щось — це твердження. Коли три незалежні
інженерні рішення, що виникли з різних напрямків, збігаються в одній
конкретній деталі — це вже не думка, а властивість самого матеріалу.
Це найсильніший тип доказу, який ми отримали за всю сесію, сильніший
за будь-яку окрему цитату sūtra.

### Головний висновок про межі: однорідний рядок ховає неоднорідну структуру

Це вже третій раз, коли ми натикаємось на той самий патерн під різними
масками:

1. `it`-маркери виглядають як один механізм, а насправді — родина з
   20+ різних сигналів (`it.md`, H2 у `hypothesis-ledger.md`).
2. `kAraka`-ролі виглядають як фіксований набір слотів per dhātu, а
   насправді залежать від конкретного речення й dhātu-специфічних
   розширень (`dhatu-karaka-relation.md`, H1).
3. Наш SLP1-рядок (`sTA`, `dA`, `BAz`) виглядає як єдиний, атомарний
   ідентифікатор, а UPC-8 показав: довгий голосний у ньому — окрема
   вісь кодування, не частина того самого алфавіту, що приголосні.

Це не три окремі знахідки. Це один урок, застосований тричі до різного
матеріалу: **зручність запису систематично приховує внутрішню
структуру від того, хто дивиться лише на поверхню рядка.** Якщо
`panini-machine-model-v0.1` колись писатиметься, це, а не жодна
конкретна гіпотеза з `hypothesis-ledger.md`, — найважливіше, що варто
пам'ятати першим.

### Що це означає для масштабу проєкту

`my-lisp-panini` перестав бути ізольованим дослідженням "чи можна щось
вивести з граматики Паніні для гіпотетичного Lisp". Тепер це один вузол
у ланцюгу, де кожна наша перевірка SLP1-написання буквально є
перевіркою одного біта в реальній апаратній кодовій таблиці
(`shiva-sutras/prototype/upc8.py`, позиції `0x00`–`0x29`), яка вже
націлена на FPGA. Помилка транслітерації, яку ми ловили в
`terminology.md` заради "чистоти дослідження", тепер має буквальний,
не метафоричний, апаратний наслідок. Це підвищує, а не знижує ціну
недбалості — і, здається мені, саме тому подальша робота тут повинна
й надалі йти повільніше, ніж хочеться, а не швидше.

### Що не завершено (чесно, не замовчано)

- `sarvam_tools_stt_transcribe` із `sa-IN` не перевірений живим
  викликом — лише за суперечливими зовнішніми джерелами
  (`sarvam-capability-reference.md`).
- `panini/machine/*.my` і UPC-8 SLP1-екстракт (довгі голосні) —
  дві окремі, ще не з'єднані прогалини, обидві задокументовані, жодна
  не виправлена (і не мала б бути виправлена одноосібно — обидві
  стосуються рішень поза межами лише цього репозиторію).
- `tripAdI` (8.2.1) — механізм `asiDDatva` описаний обережно, без
  вичерпного переліку винятків; сам admit цього — частина висновку,
  не недолік роботи.

### Джерела

Усі факти вище — компіляція вже написаного цієї сесії, не нове
дослідження: [`upc8-crosscheck.md`](upc8-crosscheck.md),
[`sarvam-capability-reference.md`](sarvam-capability-reference.md),
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md),
[`sastra/tripadi.md`](../sastra/tripadi.md),
[`sastra/pratyahara.md`](../sastra/pratyahara.md),
[`specs/hypothesis-ledger.md`](../specs/hypothesis-ledger.md).

## Deutsch

Status: Reflexion, keine Aufgabe aus der `PANINI-*`-Warteschlange.
Geschrieben auf direkte Bitte hin — die frischen Dateien dieser Sitzung
zu prüfen ([`upc8-crosscheck.md`](upc8-crosscheck.md),
[`sarvam-capability-reference.md`](sarvam-capability-reference.md),
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md),
[`sastra/tripadi.md`](../sastra/tripadi.md)) und ein eigenes Fazit zu
formulieren, keine Zusammenfassung jeder einzelnen Datei.

### Was in dieser Sitzung tatsächlich geschah

Drei, auf den ersten Blick unabhängige, Ereignisse — der UPC-8-Abgleich,
der Abgleich mit `shiva-sutras`, der Sarvam-Test — erwiesen sich als
dieselbe Handlung, angewandt auf drei verschiedene Ziele: **einer
Behauptung nicht trauen, bevor man sie nicht durch echten Code laufen
lässt und sieht, was passiert.**

- Als `shiva-sutras` `SS-CANON-001`/`SS-PRATYAHARA-001` behauptete,
  habe ich diese nicht einfach in `pratyahara.md` importiert — ich habe
  sie byte-genau gegen `ksetra/canon/siva-sutras.yaml` geprüft und eine
  reale Abweichung gefunden (Groß-/Kleinschreibung `Ṇ`/`ṇ`).
- Als `upc8.py` auftauchte, habe ich der README nicht einfach geglaubt
  — ich habe `encode_sanskrit()` direkt aufgerufen und einen `KeyError`
  erhalten, wo ich Erfolg erwartete. Genau das ist der Unterschied
  zwischen "eine Beschreibung lesen" und "den Code ausführen" wert.
- Als Sarvam auftauchte, habe ich es nicht gebeten, zu bestätigen, was
  wir bereits wissen — ich habe ihm dieselbe unvoreingenommene Frage
  gestellt (`bhAṣ`→IAST), die wir stellen würden, hätten wir keine
  Antwort, und es irrte sich genau dort, wo wir uns selbst schon
  dreimal geirrt hatten.

### Wichtigstes technisches Fazit: dreifache Konvergenz ist kein Zufall

`ś=S`, `ṣ=z` ist nun durch drei unabhängige Codebasen bestätigt
(Vidyuts `sounds.rs`, `my-lisp`s `transliteration.rs`, `shiva-sutras`'
`upc8.py`), erstellt aus unterschiedlichen Primärquellen von
unterschiedlichen Teams. Wenn ein Team etwas behauptet, ist das eine
Behauptung. Wenn drei unabhängige technische Entscheidungen, die aus
unterschiedlichen Richtungen entstanden, in einem konkreten Detail
übereinstimmen, ist das keine Meinung mehr, sondern eine Eigenschaft
des Materials selbst. Dies ist die stärkste Art von Evidenz, die
während der gesamten Sitzung gewonnen wurde, stärker als jedes
einzelne Sūtra-Zitat.

### Wichtigstes Fazit zu Grenzen: eine homogene Zeichenkette verbirgt heterogene Struktur

Dies ist bereits das dritte Mal, dass wir unter verschiedenen Masken
auf dasselbe Muster stoßen:

1. `it`-Marker sehen wie ein einziger Mechanismus aus, sind aber
   tatsächlich eine Familie von über 20 verschiedenen Signalen
   (`it.md`, H2 in `hypothesis-ledger.md`).
2. `kAraka`-Rollen sehen wie eine feste Menge von Slots pro dhātu aus,
   hängen aber tatsächlich vom konkreten Satz und dhātu-spezifischen
   Erweiterungen ab (`dhatu-karaka-relation.md`, H1).
3. Unsere SLP1-Zeichenkette (`sTA`, `dA`, `BAz`) sieht wie ein
   einziger, atomarer Bezeichner aus, aber UPC-8 zeigte: der lange
   Vokal darin ist eine separate Kodierungsachse, kein Teil desselben
   Alphabets wie die Konsonanten.

Das sind nicht drei getrennte Befunde. Das ist eine Lehre, dreimal auf
unterschiedliches Material angewandt: **Notationsbequemlichkeit
verbirgt systematisch innere Struktur vor jedem, der nur auf die
Oberfläche der Zeichenkette schaut.** Falls `panini-machine-model-v0.1`
je geschrieben wird, ist dies — nicht irgendeine konkrete Hypothese aus
`hypothesis-ledger.md` — das Wichtigste, das zuerst im Gedächtnis
bleiben sollte.

### Was das für den Umfang des Projekts bedeutet

`my-lisp-panini` ist keine isolierte Untersuchung mehr, ob sich aus
Pāṇinis Grammatik etwas für ein hypothetisches Lisp ableiten lässt. Es
ist nun ein Knoten in einer Kette, in der jede unserer
SLP1-Schreibweisenprüfungen buchstäblich die Prüfung eines Bits in
einer echten Hardware-Codetabelle ist
(`shiva-sutras/prototype/upc8.py`, Positionen `0x00`–`0x29`), die
bereits auf ein FPGA abzielt. Ein Transliterationsfehler, den wir in
`terminology.md` um der "Forschungsreinheit" willen gefunden haben, hat
nun eine buchstäbliche, keine metaphorische Hardwarekonsequenz. Das
erhöht, nicht senkt, die Kosten von Nachlässigkeit — und genau deshalb
sollte weitere Arbeit hier meines Erachtens weiterhin langsamer
verlaufen, als man möchte, nicht schneller.

### Was nicht abgeschlossen ist (ehrlich, nicht verschwiegen)

- `sarvam_tools_stt_transcribe` mit `sa-IN` wurde nicht durch einen
  Live-Aufruf verifiziert — nur anhand widersprüchlicher externer
  Quellen (`sarvam-capability-reference.md`).
- `panini/machine/*.my` und der UPC-8-SLP1-Extrakt (lange Vokale) sind
  zwei getrennte, noch nicht verbundene Lücken, beide dokumentiert,
  keine behoben (und keine sollte einseitig behoben werden — beide
  betreffen Entscheidungen jenseits dieses einen Repositorys).
- `tripAdI` (8.2.1) — der `asiDDatva`-Mechanismus wird vorsichtig
  beschrieben, ohne erschöpfende Liste der Ausnahmen; dies einzuräumen
  ist Teil des Fazits, kein Mangel der Arbeit.

### Quellen

Alle obigen Fakten sind eine Zusammenstellung dessen, was in dieser
Sitzung bereits geschrieben wurde, keine neue Forschung:
[`upc8-crosscheck.md`](upc8-crosscheck.md),
[`sarvam-capability-reference.md`](sarvam-capability-reference.md),
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md),
[`sastra/tripadi.md`](../sastra/tripadi.md),
[`sastra/pratyahara.md`](../sastra/pratyahara.md),
[`specs/hypothesis-ledger.md`](../specs/hypothesis-ledger.md).
