# dhatu registry schema v0.2

## English

**Status:** v0.1 (`PANINI-DHATU-REGISTRY-SCHEMA-V0.2`). This schema separates
three field layers: attested source data, normalized display data, and
evidence/provenance. `canonical` is normalized SLP1 for stable project use;
`source_form` and `dhatupatha_code` preserve source identity; evidence status
states verification rather than asserting a fact. The migration of 20 records
adds only evidence already established by prior audits and explicitly leaves
unverified or disputed items unresolved. No machine-usage layer belongs in a
dhātu record yet. The detailed Ukrainian text below is normative for the
v0.1 schema.

## Deutsch

**Status:** v0.1 (`PANINI-DHATU-REGISTRY-SCHEMA-V0.2`). Dieses Schema trennt
drei Feldschichten: belegte Quelldaten, normalisierte Darstellungsdaten und
Evidenz/Provenienz. `canonical` ist normalisiertes SLP1 für die stabile
Projektverwendung; `source_form` und `dhatupatha_code` bewahren die
Quellidentität; der Evidenzstatus beschreibt Verifikation, nicht eine
behauptete Tatsache. Die Migration der 20 Einträge ergänzt nur bereits durch
frühere Audits etablierte Evidenz und lässt ungeprüfte oder strittige Punkte
ausdrücklich offen. Eine Ebene für Machine-Nutzung gehört noch nicht in einen
dhātu-Eintrag. Der ukrainische Detailtext unten ist für das Schema v0.1
normativ.

## Українська

Статус: v0.1 (`PANINI-DHATU-REGISTRY-SCHEMA-V0.2`).

Формалізує ad-hoc поля, додані під час `PANINI-DHATUPATHA-SOURCE-VERIFICATION`
і `PANINI-DHATUPATHA-DISAMBIGUATION-POLICY` (`source_form`,
`dhatupatha_code`, `gana_disputed`), у явну, задокументовану схему —
замінює неформальний "Формат запису" з [`dhatu.md`](dhatu.md) §"Формат
запису" для нових і оновлюваних записів.

## Три шари полів — суворо розділені

Ключовий принцип (продовжує `PANINI-RULE-PROVENANCE-SCHEMA`): поля
запису поділені на три категорії за походженням, кожна зі своїм
рівнем довіри:

### 1. Attested source data — буквально з першоджерела, не редаговано

```yaml
source:
  dhatupatha_code: <gaRa.номер, напр. "08.0010">
  source_form: <буквальний aupadeSika-рядок з Dhātupāṭha, з усіма
                 декоративними маркерами, без нормалізації>
  gana: <1-10, як заявлено в первинному Dhātupāṭha>
```

### 2. Normalized display data — наша нормалізація для зручності

```yaml
canonical: <SLP1, цитатна форма без декоративних it-маркерів>
display:
  iast: <IAST>
  devanagari: <देवनागरी>
class: dhatu
pada: parasmaipada|atmanepada|ubhayapada
set_anit: seT|aniT|unknown
```

### 3. Evidence/provenance — статус перевірки, не сам факт

```yaml
evidence:
  status: verified|unverified|disputed
  verified_against: [<список джерел, напр. "vidyut-prakriya/data/dhatupatha.tsv">]
  gana_disputed: <bool, за замовчуванням false — див. PANINI-DHATUPATHA-DISAMBIGUATION-POLICY>
```

**Немає окремого шару "project hypothesis fields"** для dhatu-записів
на цьому етапі — жоден запис не потребує поля типу "як це
використовується в `panini/machine/`" (на відміну від
`PANINI-RULE-PROVENANCE-SCHEMA`, де це справді потрібно для правил).
Якщо колись знадобиться — додати `machine_usage:` як окремий, явно
позначений шар, а не змішувати з `source`/`evidence`.

## Повна схема (для нових записів)

```yaml
canonical: <SLP1>
display:
  iast: <IAST>
  devanagari: <देवनागरी>
class: dhatu
gana: <1-10>
pada: <parasmaipada|atmanepada|ubhayapada>
set_anit: <seT|aniT|unknown>
source:
  dhatupatha_code: <"NN.NNNN", опційно якщо ще не знайдено в первинному джерелі>
  source_form: <опційно, якщо ще не знайдено>
  dhatupatha: <старе текстове поле "gaRa (номер)" — лишається для сумісності>
evidence:
  status: <verified|unverified|disputed>
  verified_against: [<джерела>]
traditional_meaning: <SLP1, коротка парафраза>
notes: <застереження, історія виправлень>
```

## Міграція 20 наявних записів

Виконано **лише там, де докази вже є** (жодних вигаданих
`dhatupatha_code`/`source_form` для решти): усі 20 записів отримують
поле `evidence.status`, зведене з висновків
[`research/dhatupatha-verification.md`](../research/dhatupatha-verification.md):

| Корінь | `evidence.status` | Причина |
|---|---|---|
| `BAz`, `iz`, `Sru`, `dfS` | `verified` | SLP1-конвенція звірена проти `vidyut-prakriya/src/sounds.rs` (`PANINI-DHATUPATHA-SOURCE-VERIFICATION`) + фікстур (`PANINI-SLP1-CONFORMANCE-FIXTURES`) |
| `gam`, `kf`, `sTA` | `verified` | Знайдено й звірено `source_form`/`dhatupatha_code` в первинному Dhātupāṭha (`PANINI-DHATUPATHA-DISAMBIGUATION-POLICY`) |
| `dA`, `jYA`, `paW`, `as`, `han` | `verified` | Знайдено в первинному Dhātupāṭha з відповідним gaṇa/значенням (`PANINI-DHATUPATHA-SOURCE-VERIFICATION`) |
| `Sru` (gaṇa) | `disputed` | `gana_disputed: true` вже проставлено — джерело каже gaṇa 1, реєстр каже gaṇa 5 |
| `BU` | `verified` | Точний код `01.0001`, перший корінь списку |
| `vac`, `Buj`, `BI`, `yuj`, `nI`, `liK`, `pac` | `unverified` | Не знайдено однозначно простим пошуком у `PANINI-DHATUPATHA-SOURCE-VERIFICATION` — потребує точнішого пошуку (декоративні маркери), не позначати як `verified` без цього |

Поле `evidence.status: unverified` додано до всіх 20 файлів, де
раніше явних доказів пошуку не було зафіксовано; `verified` — лише
там, де попередня задача явно знайшла й підтвердила запис у
`vidyut-prakriya/data/dhatupatha.tsv`.

## Що НЕ зроблено в цій задачі

- `dhatupatha_code`/`source_form` **не додані** до записів, для яких
  вони ще не знайдені (`vac`, `Buj`, `BI`, `yuj`, `nI`, `liK`, `pac`) —
  це вимагало б повторного пошуку з точнішими патернами, не входить
  до обсягу цієї задачі (формалізація схеми, не нове дослідження).
- Поле `it_markers`/`related_sutras`, згадані в описі задачі, не
  додані як окремі структуровані поля — жоден із 20 записів ще не має
  систематично зібраних даних для цього (`seT`/`aniT` — це вже
  спрощений відповідник `it`-статусу, детальніший розпис — окрема
  майбутня задача).

## Джерела

- [`research/dhatupatha-verification.md`](../research/dhatupatha-verification.md),
  [`dhatupatha-disambiguation.md`](dhatupatha-disambiguation.md) —
  основа для статусів `evidence` вище.
