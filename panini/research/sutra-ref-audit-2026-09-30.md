# Аудит посилань на сутри в machine/ і tests/ (#17), 2026-09-30

Read-only. Змін у `panini/machine/` і `panini/tests/` цей коміт не містить.
Основа: `master` на 81dde7c (до виправлення міток у гілці `fix/15-sandhi-sutra-labels`).

## Що запускав / що читав / що не перевірив

- **Запускав:** `python3 panini/tools/audit_sutra_refs.py` (без залежностей). Знайшов 204 посилання формату N.N.N у `machine/*.lisp` і `tests/*.lisp`.
  Осиротілих номерів (відсутніх у реєстрі) немає: 0.
- **Читав:** рядки `registry/sutras.lisp` для кожного номера з таблиці нижче (`:slp1`), і контекст рядків у коді.
- **Не перевірив:** скрипт не розуміє змісту. Його вердикт «match» означає лише, що назву з реєстру знайдено на цьому/наступному рядку
  (24 з 204). Решта 180 позначені «NO MATCHING NAME ON LINE», але це здебільшого просто номер без назви (trace-крок, рядок даних)
  або англійський опис, а не помилка. Повна таблиця: [sutra-ref-audit-table-2026-09-30.md](sutra-ref-audit-table-2026-09-30.md).
  Українські/англійські описи поведінки поруч з номером (наприклад «voicing before voiced stops») скрипт не оцінює: чи вони правильні, перевірено вручну лише в таблиці нижче.
  Правильність самих реалізацій (чи код робить те, що каже сутра) НЕ перевірялась.

## Підтверджені дефекти (перевірено вручну проти реєстру)

| файл:рядок | що написано | реєстр | висновок |
|---|---|---|---|
| machine/sandhi.lisp:15, 82 | 8.4.55 «khari savarṇe» | 8.4.55 = `Kari ca` | хибна назва (#15) |
| machine/sandhi.lisp:114, 156; tests/sandhi-tests.lisp:41, 55 | 8.4.58 «jhalāṃ jhaŚi» / voicing | 8.4.58 = `anusvArasya yayi parasavarRaH` | хибний номер: озвучення = 8.4.53 (#15) |
| machine/derivation.lisp:18, 237 | 8.4.55 «jhalāṃ jhaśi» / «jjal-jhashi» | 8.4.55 = `Kari ca` | хибна назва (#15) |
| machine/derivation.lisp:164 | 6.1.78 «iko yaṇ aci» | 6.1.78 = `eco'yavAyAvaH`; `iko yaRaci` = 6.1.77 | хибна назва (#15) |
| machine/derivation.lisp:190 | «akas savarṇe dīrghaḥ» | `akaH savarRe dIrGaH` | очепятка (`akas` замість `akaḥ`) |
| machine/sandhi.lisp:14 | 6.1.88 «vṛddhir eco» | 6.1.88 = `vfdDireci` | хибна назва (`eco` замість `eci`) |
| machine/sandhi.lisp:12, 31 | 6.1.77 «iko yaN aci» | `iko yaRaci` | `N` = ṅ у SLP1, треба `R` (ṇ) |
| machine/phonology.lisp:118, 152 | 1.1.2 «aCo guṇaḥ» | 1.1.2 = `adeN guRaH` | хибна назва |
| machine/derivation.lisp:655, 681 | 8.4.63 «s→ṣ after i/u/ṛ/r/k» | 8.4.63 = `SaSCo'wi` (ś→ch); s→ṣ = 8.3.59 `AdeSapratyayayoH` | хибний номер (sandhi.lisp:16 сам називає 8.3.59) |
| machine/derivation.lisp:735 | 6.1.87 «a+e → e absorption» | 6.1.87 = `AdguRaH` | за Kāśikā на 6.1.97 («pace, yaje») це 6.1.97 `ato guRe`, не 6.1.87 (джерело: KASIKA-6.1.97.yaml в shiva-sutras/ksetra) |
| machine/derivation.lisp:32 | 7.3.101 «vṛddhi — vikaraṇa final a→ā» | 7.3.101 = `ato dIrGo yaYi` | «vṛddhi» тут хибний термін: це dīrgha, не vṛddhi |
| machine/derivation.lisp:351 | «6.1.3+ … augment a-» | 6.1.3 = `na ndrAH saMyogAdayaH`; аугмент aṭ = 6.4.71 `luNlaNlfNkzvaqudAttaH` | хибний номер (коментар ще й пошкоджений) |
| machine/paradigm.lisp:108 | 8.4.62 «jhaSAm jaS tribhiH» | 8.4.62 = `Jayo ho'nyatarasyAm` | хибна назва |
| machine/paradigm.lisp:115 | 8.2.30 «m → cch before vowel» | 8.2.30 = `coH kuH` (c→k) | хибний зміст |
| machine/paradigm.lisp:116 | 7.3.77 «iko'ci» | 7.3.77 = `izugamiyamAM CaH` | хибна назва (сам номер, схоже, доречний для gam→gacch) |
| machine/derivation.lisp:350 | 3.2.111 «anadyatanaṃ laṅa» | `anadyatane laN` | дрібна орфографія (`anadyatanaṃ`, зайве `a`) |

Не помилки (лише коментар чи назва в іншій формі): 6.1.101 у `derivation.lisp:17`, 8.3.59 `sandhi.lisp:16` («ādeśapratyayāḥ» замість `AdeSapratyayayoH`, варіант назви).
Ці висновки відтворюються ручним порівнянням із `registry/sutras.lisp`, а не скриптом.

## Що НЕ зроблено

Правок у `machine/` цим комітом немає. Для #15 окремо є гілка `fix/15-sandhi-sutra-labels` (лише коментарі/мітки, без зміни поведінки).
