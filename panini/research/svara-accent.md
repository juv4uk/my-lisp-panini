# Svara (Accent) · Сварa — наголос

Status: research record `PANINI-RESEARCH-SVARA` · sakshi · 2026-08-24
Upstream context: shiva-sutras `extensions/phonological-dimensions-v0.2.yaml`
(H-SS-EXT-001, HYPOTHESIS — не адаптовано до архітектури shiva-sutras).

## [PANINI]

Класична трійка сварів:

| Svara | Опис |
|---|---|
| **udātta** | високий тон (акцентний склад) |
| **anudātta** | низький (безакцентний, слідує за udātta) |
| **svarita** | поєднаний (виникає з колізії udātta+anudātta) |

Aṣṭādhyāyī регулює accent мінімально: ведійські svara-системи — поза
основним корпусом правил; окремі правила (напр., 8.x про udātta-звʼязки)
фрагментарні. Наголос живе переважно у ведійській традиції
(pada-pāṭha vs saṃhitā-pāṭha рецитації).

Звʼязок із tripadi.md: сучасна граматологія відносить svara-правила до
пізніх/поверхневих коригувань tripādī-зони.

## [SCHOLARLY INTERPRETATION]

Ведійські акцентні системи (та їхня втрата в класичній санскриті) —
одна з найбільших тем порівняльної акцентології; Паніні фіксує
наслідки (напр., accent на суфіксальних формах) частіше ніж сам механізм.

## [COMPUTATIONAL INTERPRETATION]

Accent як ознака складу (enum {udātta, anudātta, svarita}); у v0.1 моделі
— необовʼязковий атрибут, вимкнений для класичного санскриту.

## [MY-LISP HYPOTHESIS]

Якщо модель колись підтримає ведійські тексти: accent-поле вузла +
phonological-dimensions осі як словник розмірностей (upstream H-SS-EXT-001,
потребує reconciliation перед адаптацією — чесний статус).
