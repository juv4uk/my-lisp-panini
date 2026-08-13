# Інструменти Panini

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
