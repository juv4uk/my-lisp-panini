# Machine-rule provenance schema

Status: v0.1 (`PANINI-RULE-PROVENANCE-SCHEMA`).

## English — reference translation

### Problem and rule

`panini/machine/rules.my` records a sūtra identifier alongside fields such as
`:type`, `:scope`, `:match`, and `:action`. A verified identifier, for example
`"7.3.84"`, is a claim about a textual citation; it does **not** automatically
make every neighbouring field a sūtra claim. Each field has separate provenance.
Without that separation, implementation choices and interpretive classifications
look as authoritative as the cited text.

### Seven provenance categories

| Category | Meaning | Example |
|---|---|---|
| `sutra` | Direct Aṣṭādhyāyī citation with identifier | `"7.3.84"` |
| `dhatupatha` | Dhātupāṭha record, distinct from Aṣṭādhyāyī | `"01.0001"` |
| `varttika` | Kātyāyana supplement to a sūtra | not yet used |
| `commentary` | Kāśikā, Mahābhāṣya, Kaumudī, or similar | not yet used |
| `traditional-principle` | Traditional metaprinciple, not a direct sūtra claim | `antaraMga > bAhiraMga` |
| `implementation-convenience` | Engineering choice | a-list representation |
| `my-lisp-hypothesis` | Explicit project architecture hypothesis | kāraka as typed graph edges |

The first four categories describe external traditions; the last three describe
interpretation or project machinery. The classification itself is a
`my-lisp-hypothesis`: it extends Vidyut's source enum to make our own decisions
visible. Its completeness remains open.

### Applied examples

For `rules.my` rule `"7.3.84"`, the identifier is `sutra`; its `:type` is a
`my-lisp-hypothesis`; `:scope 'antaraMga` is a `traditional-principle`; and
the `:match`/`:action` notation is `implementation-convenience`. For `"6.1.78"`
the same distinction applies: the verified identifier is `sutra`, while
`bAhiraMga` scope and `eco-map` machinery have their own provenance.

`meta.my::make-rule` may eventually expose a `source` field using precisely
these category names. This document does **not** alter that macro, its callers,
or `compiler.my`; a signature change requires a separate, compatibility-aware
task.

## Українська — нормативна

### Проблема та правило

`panini/machine/rules.my` записує ідентифікатор sūtra поруч із полями `:type`,
`:scope`, `:match` і `:action`. Перевірений ідентифікатор, наприклад `"7.3.84"`,
є твердженням про текстову цитату; він **не** надає автоматично статус sūtra
кожному сусідньому полю. Кожне поле має окреме provenance. Без такого
розрізнення інженерні рішення та інтерпретаційні класифікації виглядають так
само авторитетно, як цитований текст.

### Сім категорій походження

| Категорія | Значення | Приклад |
|---|---|---|
| `sutra` | Пряма цитата Aṣṭādhyāyī з ідентифікатором | `"7.3.84"` |
| `dhatupatha` | Запис Dhātupāṭha, окремий від Aṣṭādhyāyī | `"01.0001"` |
| `varttika` | Доповнення Kātyāyana до sūtra | ще не використано |
| `commentary` | Kāśikā, Mahābhāṣya, Kaumudī чи подібний коментар | ще не використано |
| `traditional-principle` | Традиційний метапринцип, не пряма sūtra-цитата | `antaraMga > bAhiraMga` |
| `implementation-convenience` | Інженерне рішення | a-list представлення |
| `my-lisp-hypothesis` | Явна архітектурна гіпотеза проєкту | kāraka як типізовані graph edge |

Перші чотири категорії описують зовнішні традиції; останні три — інтерпретацію
або механіку проєкту. Сама класифікація є `my-lisp-hypothesis`: вона розширює
source enum Vidyut, щоб робити видимими наші власні рішення. Її повнота лишається
відкритим питанням.

### Приклади застосування

Для правила `"7.3.84"` у `rules.my` ідентифікатор має `sutra`; його `:type`
має `my-lisp-hypothesis`; `:scope 'antaraMga` — `traditional-principle`; а
нотація `:match`/`:action` — `implementation-convenience`. Для `"6.1.78"`
діє те саме розрізнення: перевірений ідентифікатор є `sutra`, тоді як scope
`bAhiraMga` й механіка `eco-map` мають власне provenance.

У майбутньому `meta.my::make-rule` може відкрити поле `source` саме з цими
назвами категорій. Цей документ **не** змінює macro, його виклики чи
`compiler.my`; зміна сигнатури потребує окремої задачі з перевіркою сумісності.

## Deutsch — Referenzübersetzung

### Problem und Regel

`panini/machine/rules.my` führt eine Sūtra-Kennung neben Feldern wie `:type`,
`:scope`, `:match` und `:action`. Eine geprüfte Kennung wie `"7.3.84"` ist eine
Behauptung über eine Textzitation; sie macht **nicht** jedes benachbarte Feld
automatisch zu einer Sūtra-Behauptung. Jedes Feld hat eigene Provenance. Ohne
diese Trennung erscheinen Implementierungsentscheidungen und interpretative
Klassifikationen so autoritativ wie der zitierte Text.

### Sieben Herkunftskategorien

| Kategorie | Bedeutung | Beispiel |
|---|---|---|
| `sutra` | Direkte Aṣṭādhyāyī-Zitation mit Kennung | `"7.3.84"` |
| `dhatupatha` | Dhātupāṭha-Eintrag, getrennt von Aṣṭādhyāyī | `"01.0001"` |
| `varttika` | Kātyāyana-Ergänzung zu einem Sūtra | noch unbenutzt |
| `commentary` | Kāśikā, Mahābhāṣya, Kaumudī oder Kommentar | noch unbenutzt |
| `traditional-principle` | Traditionelles Metaprinzip, keine direkte Sūtra-Aussage | `antaraMga > bAhiraMga` |
| `implementation-convenience` | Technische Entscheidung | a-list-Darstellung |
| `my-lisp-hypothesis` | Explizite Architekturhypothese | kāraka als typisierte Graphkanten |

Die ersten vier Kategorien beschreiben äußere Traditionen, die letzten drei
Interpretation oder Projektmechanik. Die Klassifikation selbst ist eine
`my-lisp-hypothesis`: Sie erweitert Vidyuts Source-Enum, damit unsere eigenen
Entscheidungen sichtbar bleiben. Ihre Vollständigkeit ist offen.

### Anwendungsbeispiele

Bei `rules.my` Regel `"7.3.84"` ist die Kennung `sutra`, `:type` eine
`my-lisp-hypothesis`, `:scope 'antaraMga` ein `traditional-principle` und
`:match`/`:action` `implementation-convenience`. Für `"6.1.78"` gilt dieselbe
Trennung. `meta.my::make-rule` kann später ein `source` Feld mit diesen Namen
anbieten; dieses Dokument ändert weder Macro noch Aufrufer oder `compiler.my`.
Eine Signaturänderung braucht eine eigene Kompatibilitätsaufgabe.

## Sources

- [`research/vidyut-analysis.md`](../research/vidyut-analysis.md)
- `panini/machine/rules.my`, `panini/machine/meta.my`
- [`foundation/rule-system.md`](../foundation/rule-system.md)
- [`foundation/paribhasha.md`](../foundation/paribhasha.md)
