# Аудит консистентності термінології v0.1

Статус: завершено (`PANINI-FOUNDATION-TERMINOLOGY-CONSISTENCY`).

## Обсяг

Перевірено 19 файлів `panini/foundation/` та пов'язані `research/`/`specs/`
посилання для канонічних SLP1-ідентифікаторів із високим ризиком плутанини:
довгота голосних, `S`/`z`, `f`/`F`, а також назви ключових категорій.
Еталон — `tests/slp1-conformance.yaml` і `foundation/terminology.md`; це не
нова транслітераційна система.

## Виправлення

| Було | Стало | IAST | Причина |
|---|---|---|---|
| `paribhASA` | `paribhAzA` | *paribhāṣā* | ретрофлексний ṣ у SLP1 — `z`, не `S` |

Виправлення застосовано в `foundation/ontology.md`, `foundation/paribhasha.md`,
`foundation/samjna.md`, `research/grammar-reference-crosscheck.md`,
`specs/rule-provenance-schema.md` і `specs/hypothesis-ledger.md`.

## Перевірені інваріанти

- Не знайдено залишків `paribhASA` поза історичними/виключеними артефактами.
- `kartf`, `karman`, `karaRa`, `sampradAna`, `apAdAna`, `aDikaraRa`,
  `prAtipadika`, `pratyAhAra`, `anuvftti` та `aDikAra` в активних foundation
  документах відповідають словнику.
- Відображення IAST і деванаґарі не змінювалися цим аудитом: завдання
  стосувалося лише SLP1-дрифту, а не перегляду перекладів чи доктринальних
  тверджень.

## Межі результату

Це механічна перевірка узгодженості репозиторію, не верифікація кожного
санскритського слова за критичним виданням. Нові назви перед комітом мають
проходити `tests/slp1-conformance.yaml`, а важливі терміни — ще й окреме
джерельне дослідження.
