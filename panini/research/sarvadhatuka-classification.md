# Sārvadhātuka Classification · Класифікація sārvadhātuka

Status: research record `PANINI-RESEARCH-SARVADHATUKA` · sakshi · 2026-08-24
Synthesis of in-repo verified material: Bavati.md trace,
bavati-sap-initial-marker-source-audit.md (3.4.113 provenance),
semantic-grounding.md.

## [PANINI]

**Source anchor:** Aṣṭādhyāyī 3.4.113 (*tiṅśit sārvadhātukam*).

Sārvadhātuka — спільна назва для аффіксів, що вводяться **після dhātu**:
клас *tiṅ*-закінчень і *śiṭ*-позначених vikaraṇa-аффіксів. Протилежний
клас — *ārdhadhātuka* (3.4.113 вводить обидва терміни однією сутрою).

Ключові механізми класу:

1. **Парадигматичний представник — śap:** 3.1.68 (*kartari śap*) вводить
   śap у parasmaipada-активних контекстах; верифіковано живою деривацією
   Bavati.md, крок 4 (`BU + Sap + ti`, якір 3.1.68).
2. **Guṇa aṅga-final перед аффіксом класу:** кінцевий голосний основи
   отримує guṇa-заміну перед sārvadhātuka/ārdhadhātuka аффіксом
   (Bavati.md:110, крок 5 деривації).
3. **Варіанти seṭ/aniṭ/vet** обираються it-маркерами Dhātupāṭha-запису
   кореня (звʼязок із Sources/Aṣṭādhyāyī.md провенансом).

## [SCHOLARLY INTERPRETATION]

Класичне протиставлення sārvadhātuka/ārdhadhātuka організовує морфологію:
sārvadhātuka-афікси (на чолі зі śap) характеризують present-system і тягнуть
guṇa-посилення основи; ārdhadhātuka позначає пост-презентну морфологію без
цього ефекту. Сучасні описи підкреслюють: це розмежування рухає
правило-застосування, а не є семантичною класифікацією.

## [COMPUTATIONAL INTERPRETATION]

Enum `VikaraṇaClass { sarvadhātuka, ārdhadhātuka }` на аффіксах; клас гейтує:
(a) yak-вставку перед голосним-початком афікса [якор 7.3.77 — до звірки],
(b) guṇa-gating основи, (c) таймінг it-strip відносно фонологічних правил.
У машинній моделі v0.1 це поле тегу вузла деривації.

## [MY-LISP HYPOTHESIS]

Bavati proof-trace вже несе клас у ланцюзі (крок 4 → якір 3.1.68). Розвиток:
поле `vikarana-class` у реєстрі аффіксів + диференційний фіксюр-корпус з
ISA-RATIONAL G2 (спільний з Rust↔FPGA corpus) для перевірки guṇa/yak
поведінки як значеннєвої еквівалентності між бекендами.

## SARVAM WITNESS

Translate probe «सार्वधातुकम् अर्धधातुकम्» → *"Sarvadhatukam Ardhadhatukam"*
(транслітерація без перекладу). Термінологічну цінність свідок не додав;
джерельні формулювання залишаються авторитетними.
