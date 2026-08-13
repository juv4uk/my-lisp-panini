# Інструменти Panini

`validate_registry.py` — offline, read-only validator малих YAML-реєстрів.
Він не редагує і не нормалізує файли.

Запуск через задеклароване Guix-середовище:

```sh
guix shell -m manifest.scm -- python3 panini/tools/validate_registry.py
```

Ненульовий exit code означає знайдені помилки. Попередження не змінюють
статус даних і не є дозволом на автоматичне виправлення.
