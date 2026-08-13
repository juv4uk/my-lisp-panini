# Trace fixtures

## English summary

These fixtures test data-contract boundaries for derivation traces. They do
not certify a historical derivation or replace executable integration tests.
The Ukrainian section is normative.

## Українська

Fixtures у цьому каталозі призначені для перевірки **структури доказового
trace**, а не для прихованого проголошення результату Панінійським фактом.

- `partial` fixture може тестувати наявність candidate rules, decision,
  provenance та transition, але не проходить acceptance gate повного порядку.
- `complete` fixture потребуватиме hashes canonical states, executable command,
  всі required provenance records і `trace-terminated: success`.
- Зміна output або policy створює новий fixture ID; старий результат лишається
  для аудиту, а не переписується.

Див. `derivation-ir-v0.1.md`, `derivation-ir-trace-events-v0.1.md` і
`trace-evidence-model-v0.1.md` у `panini/specs/`.

Поточний стан портфеля, прогалини та наступні evidence gates:
`../../research/derivation-machine-v0.1-portfolio-audit.md`.

## Deutsch

Diese Fixtures prüfen die Datenvertragsgrenzen von Derivations-Traces und
bestätigen keine historische Derivation. Ein `partial` Fixture darf Struktur
und Provenienz prüfen, aber keinen vollständigen Prioritätsnachweis ersetzen.
Die ukrainische Fassung ist normativ.
