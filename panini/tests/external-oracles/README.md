# External oracle fixtures

## English summary

This directory contains version-pinned comparison inputs for external tools.
Fixtures are never canonical registry data and a planned fixture is not a
successful oracle run. The Ukrainian section is normative.

## Українська

Цей каталог містить **порівняльні** fixtures для зовнішніх інструментів. Він
не є registry, не містить canonical identifiers як похідні від oracle і не
дає жодному зовнішньому output статус `[PANINI]`.

Файл fixture може бути у трьох станах:

| Стан | Значення | Дозволена дія |
|---|---|---|
| `planned` | входи й pinned tool визначені, але command ще не може бути відтворений | додати Guix packaging/ADR-задачу; не робити assertion про output |
| `recorded` | command виконано, output і revision збережені | використовувати як regression signal |
| `invalidated` | revision, ліцензія, command або representation більше не відповідають контракту | не запускати як test oracle; зберегти для аудиту |

Кожен fixture мусить відповідати
[`external-oracle-fixture-policy-v0.1.md`](../../specs/external-oracle-fixture-policy-v0.1.md).
Після зміни інструмента або його даних не перезаписуйте output: створіть новий
fixture ID, а старий позначте `invalidated` або збережіть як незалежний
порівняльний результат.

## Deutsch

Dieses Verzeichnis enthält versionsfixierte Vergleichseingaben für externe
Werkzeuge. Fixtures sind keine kanonischen Registerdaten und ein geplanter
Fixture ist kein erfolgreiches Oracle-Ergebnis. Die ukrainische Fassung ist
normativ.
