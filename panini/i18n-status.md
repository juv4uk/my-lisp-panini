# Trilingual documentation migration · Trymovna mihratsiya dokumentatsiyi · Dreisprachige Dokumentationsmigration

## English

This file tracks translation coverage for repository-owned, human-facing
documentation. It excludes source code, SLP1, sūtra text, YAML data, URLs,
verbatim quotations, `scratch/` vendor trees, and external reference copies.

Ukrainian is the normative language, written in project-defined Latin ASCII.
SLP1 remains reserved for Sanskrit vocabulary and identifiers; it is not the
name of the Ukrainian ASCII orthography.

| Area | Current canonical content | Migration state |
| --- | --- | --- |
| Root README | legacy Cyrillic Ukrainian | needs ASCII-Ukrainian migration |
| `panini/README.md` | legacy Cyrillic Ukrainian | needs ASCII-Ukrainian migration |
| Language policy | English, Ukrainian ASCII, German | complete |
| Machine testing guide | legacy Cyrillic Ukrainian | queued for trilingual ASCII expansion |
| Foundation notes | primarily legacy Cyrillic Ukrainian | in progress |
| Research audits | primarily legacy Cyrillic Ukrainian | queued |
| Specifications | primarily legacy Cyrillic Ukrainian | queued |

## Ukrainian (ASCII)

Tsey fayl vidstezhuye pokryttya perekladom vlasnoyi lyudskoyi dokumentatsiyi
repozytoriyu. Vin ne okhoplyuye source code, SLP1, tekst sutra, YAML-dani, URL,
doslivni tsytaty, vendor-dereva `scratch/` ta zovnishni reference copies.

Ukrayinska ye normatyvnoyu movoyu i zapysuyetsya proyektnym latynskym ASCII-
pravopysom. SLP1 zarezervovano dlya sanskrytskoyi leksyky ta identyfikatoriv;
tse ne nazva ukrayinskoho ASCII-pravopysu.

| Dilyanka | Potochnyy kanonichnyy zmist | Stan mihratsiyi |
| --- | --- | --- |
| Korenevyy README | legacy kyrylychna ukrayinska | potribna ASCII-ukrayinska mihratsiya |
| `panini/README.md` | legacy kyrylychna ukrayinska | potribna ASCII-ukrayinska mihratsiya |
| Movna polityka | anhliyska, ukrayinska ASCII, nimecka | zaversheno |
| Hid iz machine testing | legacy kyrylychna ukrayinska | u cherzi na trymovne ASCII-rozshyrennya |
| Foundation notes | perevazhno legacy kyrylychna ukrayinska | u roboti |
| Research audits | perevazhno legacy kyrylychna ukrayinska | u cherzi |
| Spetsyfikatsiyi | perevazhno legacy kyrylychna ukrayinska | u cherzi |

## Deutsch

Diese Datei verfolgt die Übersetzungsabdeckung der vom Repository gepflegten,
menschenlesbaren Dokumentation. Ausgenommen sind Quellcode, SLP1, Sūtra-Text,
YAML-Daten, URLs, wörtliche Zitate, eingebundene `scratch/`-Bäume und externe
Referenzkopien.

Ukrainisch ist die normative Sprache und wird in einer projektdefinierten
lateinischen ASCII-Orthographie geschrieben. SLP1 bleibt für Sanskrit-
Vokabular und Identifikatoren reserviert.

| Bereich | Aktueller kanonischer Inhalt | Migrationsstand |
| --- | --- | --- |
| Root-README | Englisch, Ukrainisch, Deutsch | abgeschlossen |
| `panini/README.md` | Englisch, Ukrainisch, Deutsch | abgeschlossen |
| Sprachrichtlinie | Englisch, Ukrainisch, Deutsch | abgeschlossen |
| Machine-Testing-Leitfaden | Ukrainisch | für dreisprachige Erweiterung vorgemerkt |
| Foundation-Notizen | überwiegend Ukrainisch | in Arbeit |
| Forschungsaudits | überwiegend Ukrainisch | vorgemerkt |
| Spezifikationen | überwiegend Ukrainisch | vorgemerkt |

## Order · Poryadok · Reihenfolge

1. Foundation concepts referenced by the README and machine boundary.
2. Specifications that define project contracts.
3. Research audits and worked examples.
4. User-facing testing and tool documentation.

Translations must preserve evidence boundaries: translation never changes a
claim from `[INTERPRETATION]` or `[MY-LISP HYPOTHESIS]` into `[PANINI]`.
