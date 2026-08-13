# Trilingual documentation migration · Тримовна міграція документації · Dreisprachige Dokumentationsmigration

## English

This file tracks translation coverage for repository-owned, human-facing
documentation. It excludes source code, SLP1, sūtra text, YAML data, URLs,
verbatim quotations, `scratch/` vendor trees, and external reference copies.

| Area | Current canonical content | Migration state |
| --- | --- | --- |
| Root README | English, Ukrainian, German | complete |
| `panini/README.md` | English, Ukrainian, German | complete |
| Language policy | English, Ukrainian, German | complete |
| Machine testing guide | Ukrainian | queued for trilingual expansion |
| Foundation notes | primarily Ukrainian | in progress |
| Research audits | primarily Ukrainian | queued |
| Specifications | primarily Ukrainian | queued |

## Українська

Цей файл відстежує покриття перекладом власної людської документації
репозиторію. Він не охоплює source code, SLP1, текст sūtra, YAML-дані, URL,
дослівні цитати, vendor-дерева `scratch/` та зовнішні reference copies.

| Ділянка | Поточний канонічний зміст | Стан міграції |
| --- | --- | --- |
| Кореневий README | англійська, українська, німецька | завершено |
| `panini/README.md` | англійська, українська, німецька | завершено |
| Мовна політика | англійська, українська, німецька | завершено |
| Гід із machine testing | українська | у черзі на тримовне розширення |
| Foundation notes | переважно українська | у роботі |
| Research audits | переважно українська | у черзі |
| Специфікації | переважно українська | у черзі |

## Deutsch

Diese Datei verfolgt die Übersetzungsabdeckung der vom Repository gepflegten,
menschenlesbaren Dokumentation. Ausgenommen sind Quellcode, SLP1, Sūtra-Text,
YAML-Daten, URLs, wörtliche Zitate, eingebundene `scratch/`-Bäume und externe
Referenzkopien.

| Bereich | Aktueller kanonischer Inhalt | Migrationsstand |
| --- | --- | --- |
| Root-README | Englisch, Ukrainisch, Deutsch | abgeschlossen |
| `panini/README.md` | Englisch, Ukrainisch, Deutsch | abgeschlossen |
| Sprachrichtlinie | Englisch, Ukrainisch, Deutsch | abgeschlossen |
| Machine-Testing-Leitfaden | Ukrainisch | für dreisprachige Erweiterung vorgemerkt |
| Foundation-Notizen | überwiegend Ukrainisch | in Arbeit |
| Forschungsaudits | überwiegend Ukrainisch | vorgemerkt |
| Spezifikationen | überwiegend Ukrainisch | vorgemerkt |

## Order · Порядок · Reihenfolge

1. Foundation concepts referenced by the README and machine boundary.
2. Specifications that define project contracts.
3. Research audits and worked examples.
4. User-facing testing and tool documentation.

Translations must preserve evidence boundaries: translation never changes a
claim from `[INTERPRETATION]` or `[MY-LISP HYPOTHESIS]` into `[PANINI]`.
