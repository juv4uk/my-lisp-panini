# Foundation v0.1: audit локальних посилань

## Обсяг

Перевірено Markdown-посилання між `foundation/`, `research/`, `specs/` та
`README.md` у стані 2026-08-13. Audit не перевіряє доступність зовнішніх URL
і не вважає URL доказом paninian твердження.

## Виправлено

У `specs/bridge-to-my-lisp.md` два шляхи мали зайвий сегмент `panini/`:

| Було | Стало | Причина |
| --- | --- | --- |
| `../panini/examples/derivations/Bavati.md` | `../examples/derivations/Bavati.md` | Файл already знаходиться під `panini/specs/`. |
| `../panini/machine/rules.my` | `../machine/rules.my` | Той самий зайвий сегмент. |

## Перевірені зв'язки

- `derivation-trace-template.md` → provenance schema, `anuvftti`, examples audit;
- `upasarga` crosswalk → `avyaya` boundary, trace template, sūtra provenance;
- `karaka` materials → relation examples і cardinality boundary;
- `samjna`/ontology/terminology → взаємні foundation notes;
- `hypothesis-ledger.md` → research та foundation матеріали через `../`.

## Залишковий portability risk

`specs/bridge-to-my-lisp.md` ще містить два `file:///C:/GitHub/my-lisp/...`
посилання. Вони описують міжрепозиторний стан на конкретній Windows-машині,
а не є portable Markdown links. Їх не змінено в цьому audit: виправлення
потребує узгодженого міжрепозиторного URL або документаційного контракту,
щоб не вигадати шлях до іншого репозиторію.

## Висновок

Локальні посилання Foundation v0.1 узгоджені після двох виправлень. Нові
документи мають використовувати відносні шляхи всередині `panini/`; зовнішні
репозиторії слід позначати як зовнішню залежність, а не як внутрішній файл.
