# Dhātu homonym disambiguation policy

## English

**Status:** v0.1 (`PANINI-DHATU-REGISTRY-PROVENANCE-FIELDS`). Canonical SLP1
spelling is a human-friendly citation form, not a guaranteed unique key for a
complete Dhātupāṭha. The verified `jYA` case has three distinct source records;
only `09.0043` matches this registry’s gaṇa-9 “know” entry. Consequently,
`dhatupatha_code` identifies a concrete source record, while optional
`homonyms` records known alternatives. Source prefixes such as `qu-` cannot
be discarded as merely decorative without checking whether they distinguish
different roots. The detailed Ukrainian policy below defines file naming and
registry handling; it does not claim every current root has been checked.

## Deutsch

**Status:** v0.1 (`PANINI-DHATU-REGISTRY-PROVENANCE-FIELDS`). Die kanonische
SLP1-Schreibweise ist eine menschenfreundliche Zitierform, aber kein garantiert
eindeutiger Schlüssel für einen vollständigen Dhātupāṭha. Der geprüfte Fall
`jYA` besitzt drei verschiedene Quelleneinträge; nur `09.0043` entspricht dem
Registereintrag der gaṇa 9 mit „wissen“. Daher bezeichnet `dhatupatha_code`
einen konkreten Quelleneintrag, während das optionale Feld `homonyms` bekannte
Alternativen festhält. Quellpräfixe wie `qu-` dürfen nicht ohne Prüfung als
rein dekorativ verworfen werden, wenn sie verschiedene Wurzeln unterscheiden.
Die ukrainische Detailrichtlinie unten legt Dateinamen und Registerbehandlung
fest; sie behauptet nicht, dass bereits jede Wurzel geprüft wurde.

## Українська

Статус: v0.1 (`PANINI-DHATU-REGISTRY-PROVENANCE-FIELDS`).

Доповнює [`dhatupatha-disambiguation.md`](dhatupatha-disambiguation.md)
(орфографічні розбіжності: маркери, зміна приголосного) конкретно
випадком **справжньої омонімії** — коли `canonical`-написання
збігається для кількох генетично різних dhātu.

## Підтверджений випадок: `jYA`

Пряма перевірка `vidyut-prakriya/data/dhatupatha.tsv` (стовпець
`dhatu`, точний збіг без декоративних маркерів):

| Код | Форма в джерелі | Значення | Наш реєстр (gaṇa 9, "знати") |
|---|---|---|---|
| `01.0923` | `jYA` | `mAraRatozaRaniSAmanezu` (убивство/задоволення/повідомлення) | ❌ не відповідає |
| `09.0043` | `jYA\` | `avaboDane` (розуміння, усвідомлення) | ✅ відповідає — gaṇa 9, семантично близько до "знати" |
| `10.0258` | `jYA` | `niyoge` (призначення, наказ) | ❌ не відповідає |

**Три генетично різні dhātu з однаковим написанням `jYA`.** Лише
`09.0043` справді відповідає тому, що зафіксовано в
[`registry/dhatu/jYA.yaml`](../registry/dhatu/jYA.yaml) (gaṇa 9,
значення "знати"). Без цієї перевірки `canonical: jYA` виглядав би
однозначним — він не є таким у первинному джерелі.

## Побічна знахідка: `qu-`-префікс — не суто декоративний

`dhatupatha-disambiguation.md` (попередня задача) класифікував
префікс `qu-` (як у `qukf\Y`) як "декоративний it-маркер". Ця задача
уточнює: `qu-` **сам є традиційним засобом розрізнення омонімів** —
корінь `kf\Y` (без `qu`, gaṇa 5, значення `hiMsAyAm`, "насильство")
і корінь `qukf\Y` (з `qu`, gaṇa 8, значення `karaRe`, "робити") —
**різні dhātu**, що виглядали б ідентично (`kf` після зняття
акцентних маркерів), якби не префікс `qu`. Тобто префікс не просто
"шум", який можна відкинути без наслідків — він частина того, як
традиція запобігає саме цій омонімії. Це не скасовує правило
нормалізації з `dhatupatha-disambiguation.md` (наш `canonical: kf`
залишається без `qu`, бо це узгоджена цитатна форма), але означає:
**`source_form` для `kf` не можна вважати взаємозамінним із формою
без `qu`-префікса** — вони позначають різні корені.

## Політика

1. **`canonical` — НЕ гарантовано унікальний ключ** для повного
   Dhātupāṭha (~2260 записів). Це зручна цитатна форма для людей і
   міжрепозиторної сумісності, не первинний ключ.
2. **`dhatupatha_code` (`gaRa.номер`) — справжній унікальний ключ**,
   коли йдеться про конкретний запис первинного джерела. Кожен запис
   `registry/dhatu/*.yaml`, для якого `dhatupatha_code` встановлено
   (`PANINI-DHATU-REGISTRY-SCHEMA-V0.2`), тим самим однозначно
   прив'язаний до одного конкретного омоніма, не до "canonical-рядка
   загалом".
3. **Нове поле `homonyms`** (опційно, лише де відомо): список інших
   `dhatupatha_code`, що мають те саме `canonical`-написання, але є
   іншими коренями:

```yaml
homonyms:
  - { dhatupatha_code: "01.0923", meaning: "mAraRatozaRaniSAmanezu" }
  - { dhatupatha_code: "10.0258", meaning: "niyoge" }
```

4. **Колізія імені файлу**: реєстр іменує файли за `canonical`
   (`jYA.yaml`). Якщо колись знадобиться зареєструвати ДРУГИЙ омонім
   з тим самим написанням окремим повноцінним записом (не просто
   заміткою `homonyms`) — файл повинен отримати суфікс
   `dhatupatha_code` (напр. `jYA-01.0923.yaml`), а не перезаписувати
   наявний `jYA.yaml` чи створювати колізію.
5. **`qu-`-подібні префікси в `source_form` не можна відкидати як
   чисто декоративні** без перевірки: якщо два записи відрізняються
   лише таким префіксом, перевірити, чи це справді той самий корінь,
   чи традиційний засіб розрізнення омонімів (як `kf`/`qukf` вище).

## Застосування

`jYA.yaml` отримує поле `homonyms` (два записи вище). Інші 19 записів
**не перевірені на омонімію** в цій задачі (лише `jYA` мала попередньо
відому підозру з `PANINI-DHATUPATHA-SOURCE-VERIFICATION`) — систематична
перевірка всіх 20 на омонімію лишається окремою майбутньою задачею,
не вигадується тут.

## Джерела

- `vidyut-prakriya/data/dhatupatha.tsv` — прочитано напряму для цієї
  задачі (запити на точний збіг стовпця `dhatu`, без декоративних
  маркерів, для `jYA` і `kf`-родини).
- [`dhatupatha-disambiguation.md`](dhatupatha-disambiguation.md) —
  базова політика, яку ця задача доповнює.
