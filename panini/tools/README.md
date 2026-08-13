# Panini tools / Інструменти Panini / Panini-Werkzeuge

## English

`validate_registry.py` is an offline, read-only validator for the small YAML
registries. It never edits or normalizes files.

Run it in the declared Guix environment:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_registry.py
```

`--strict-provenance` additionally requires a nonempty `source` for `dhatu`
and nonempty `sources` for `karaka`/`samjna`. This mode is opt-in until legacy
records gain provenance; the validator never rewrites data.

Run negative fixtures with:

```sh
guix shell -m manifest.scm -- python3 panini/tests/test_registry_provenance.py
```

A nonzero exit code means errors were found. Warnings do not change data status
and are not permission for an automatic correction.

`check_documentation_languages.py` inventories English, Ukrainian, and German
section markers in repository-owned Markdown. It excludes vendor/reference
trees and never changes documentation. Its default report is informational;
use `--strict` only when every remaining migration item is intended to block:

```sh
guix shell -m manifest.scm -- python3 panini/tools/check_documentation_languages.py
```

`validate_trace_fixtures.py` validates the structural evidence contract of
Derivation IR fixtures: event dependencies, declared states, selected-rule
transitions, provenance, and matching termination status. It scans only files
that contain `events`; it never infers missing linguistic facts or rewrites a
fixture:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_trace_fixtures.py
guix shell -m manifest.scm -- python3 panini/tests/test_trace_fixture_validator.py
```

For an executable My Lisp integration check, use the supplied runtime path
explicitly. This acceptance harness fails on REPL diagnostics even when the
process exits with code 0:

```sh
guix shell -m manifest.scm -- python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

## Українська

`validate_registry.py` — offline, read-only validator малих YAML-реєстрів.
Він не редагує і не нормалізує файли.

Запуск через задеклароване Guix-середовище:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_registry.py
```

`--strict-provenance` додатково вимагає непорожній `source` для `dhatu` та
непорожній `sources` для `karaka`/`samjna`. Режим opt-in, доки старі записи не
отримали provenance; validator ніколи не переписує дані.

Негативні fixtures запускаються так:

```sh
guix shell -m manifest.scm -- python3 panini/tests/test_registry_provenance.py
```

Ненульовий exit code означає знайдені помилки. Попередження не змінюють
статус даних і не є дозволом на автоматичне виправлення.

`check_documentation_languages.py` інвентаризує маркери секцій English,
Українська та Deutsch у Markdown, що належить репозиторію. Він виключає
vendor/reference-дерева й ніколи не змінює документацію. Звіт у звичайному
режимі лише інформаційний; застосовуйте `--strict`, лише коли всі решта
пунктів міграції повинні блокувати:

```sh
guix shell -m manifest.scm -- python3 panini/tools/check_documentation_languages.py
```

`validate_trace_fixtures.py` перевіряє structural evidence contract
Derivation IR-fixture: залежності подій, оголошені стани, переходи після
selected rule, provenance і відповідність termination status. Він сканує лише
файли з `events`, ніколи не виводить відсутніх мовних фактів і не переписує
fixture:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_trace_fixtures.py
guix shell -m manifest.scm -- python3 panini/tests/test_trace_fixture_validator.py
```

Для виконуваної інтеграційної перевірки My Lisp передайте шлях до runtime
явно. Цей acceptance harness провалюється на REPL diagnostics, навіть якщо
process завершується з кодом 0:

```sh
guix shell -m manifest.scm -- python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```

## Deutsch

`validate_registry.py` ist ein Offline-Validator mit reinem Lesezugriff für
die kleinen YAML-Register. Er bearbeitet oder normalisiert keine Dateien.

Ausführung in der deklarierten Guix-Umgebung:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_registry.py
```

`--strict-provenance` verlangt zusätzlich ein nicht leeres `source` für
`dhatu` sowie nicht leere `sources` für `karaka`/`samjna`. Dieser Modus ist
opt-in, bis ältere Datensätze Provenienz erhalten; der Validator schreibt Daten
niemals um.

Negative Fixtures werden so ausgeführt:

```sh
guix shell -m manifest.scm -- python3 panini/tests/test_registry_provenance.py
```

Ein Exit-Code ungleich null bedeutet, dass Fehler gefunden wurden. Warnungen
ändern den Datenstatus nicht und erlauben keine automatische Korrektur.

`check_documentation_languages.py` inventarisiert die Abschnittsmarker
English, Українська und Deutsch in Markdown-Dateien, die zum Repository
gehören. Vendor-/Referenzbäume werden ausgeschlossen und die Dokumentation
wird nie verändert. Der normale Bericht ist nur informativ; `--strict` nur
verwenden, wenn alle übrigen Migrationspunkte blockieren sollen:

```sh
guix shell -m manifest.scm -- python3 panini/tools/check_documentation_languages.py
```

`validate_trace_fixtures.py` prüft den strukturellen Evidenzvertrag der
Derivation-IR-Fixtures: Ereignisabhängigkeiten, deklarierte Zustände,
Übergänge nach einer selected rule, Provenienz und passenden
Abschlussstatus. Es durchsucht nur Dateien mit `events`, leitet keine
fehlenden sprachlichen Fakten ab und schreibt keine Fixtures um:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_trace_fixtures.py
guix shell -m manifest.scm -- python3 panini/tests/test_trace_fixture_validator.py
```

Für einen ausführbaren My-Lisp-Integrationstest wird der Runtime-Pfad explizit
übergeben. Dieser Acceptance-Harness schlägt auch bei REPL-Diagnosen fehl,
selbst wenn der Prozess mit Code 0 endet:

```sh
guix shell -m manifest.scm -- python3 panini/tests/run_machine_acceptance.py \
  --runtime /mnt/c/GitHub/my-lisp/target/debug/my-lisp.exe
```
