# Trace canonical serialization: implementation audit

Status: `partial`. This is an audit of the project specification and fixtures,
not a claim about Pāṇini.

## English

The Derivation IR specification correctly requires immutable states to be
content-addressed from canonical bytes. But the current fixture corpus uses
`state:fixture:*` identifiers and explicitly declares
`serialization: fixture-sexpr-not-hashed`. No implementation currently fixes
the byte grammar, Unicode normalization, relation sort key, map-key order,
hash algorithm, or test vectors. Consequently, the current fixtures are
valuable evidence models but cannot yet demonstrate reproducible
content-addressed states.

## Українська

### [PANINI]

Цей аудит не має панініївського твердження. Канонічна серіалізація, SHA-256 і
content addressing — властивості нашої machine model, а не висновки з sūtra.

### [INTERPRETATION]

У `derivation-ir-v0.1.md` вже записано правильний намір: hash state має
походити з canonical bytes `schema`, ordered `terms` і normalized `relations`,
без display labels, timestamps та локальних шляхів. Проте конкретний алгоритм
canonical bytes ще не визначено. Наявні trace fixtures чесно вказують
`serialization: fixture-sexpr-not-hashed` і застосовують IDs
`state:fixture:*`, а не `state:sha256:<digest>`.

Отже, нині заборонено називати fixture-derived state content-addressed або
перевіреним reproducible hash. YAML-файл сам по собі не є canonical bytes:
відступи, порядок ключів, quoting, line endings та Unicode можуть відрізнятися
без зміни наміру людини.

Мінімальний наступний contract має окремо зафіксувати:

1. один serialization format і версію;
2. UTF-8, Unicode normalization та line-ending policy;
3. exact order `terms` і total ordering для `relations`;
4. map-key order, escaping та відсутність presentation fields;
5. hash algorithm, digest encoding і prefix;
6. щонайменше два published input-bytes → digest test vectors;
7. validator, який відхиляє `state:sha256:*`, якщо digest не збігається.

До цього моменту `fixture-sexpr-not-hashed` є правильним explicit boundary, а
не недоліком, який слід приховати.

### [MY-LISP HYPOTHESIS]

Для майбутньої immutable knowledge machine важливий не конкретний JSON чи
S-expression, а contract: однаковий semantic state мусить мати однакові bytes
і digest незалежно від хоста. Проте цей contract ще не можна переносити в My
Lisp як готовий primitive або storage format; спершу потрібні versioned test
vectors і незалежна перевірка.

## Deutsch

Die Derivation-IR-Spezifikation fordert zurecht content-addressed,
unveränderliche Zustände. Die aktuellen Fixtures verwenden jedoch ausdrücklich
`fixture-sexpr-not-hashed` und `state:fixture:*`. Byte-Grammatik,
Normalisierung, Sortierung, Hashverfahren und Testvektoren fehlen noch. Daher
sind die Fixtures wertvolle Evidenzmodelle, aber noch kein Nachweis
reproduzierbarer content-addressed States.
