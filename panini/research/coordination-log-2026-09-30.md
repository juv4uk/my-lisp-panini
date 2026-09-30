# Coordination log — 2026-09-30 (сесія «паніні», 378e10)

Статус: робочий журнал, не claim. Записано за вказівкою sdvova («старайся все документувати»).
Жодних змін коду чи реєстру в цій сесії; єдиний новий файл — цей.

## Учасники (за `ListAgents`, 2026-09-30)

| Ім'я | ID | Примітка |
|---|---|---|
| паніні | 378e10 | ця сесія, my-lisp-panini |
| шіва | 6ae74c | раніше «Активний агент у додатку» |
| координатор | 32ce6f | раніше «Память»; веде UPC-14 у shiva-sutras |

Ранні спроби `SendMessage` за старими іменами не доходили («No agent named …»); сесії
перейменувалися. Адресація тепер за іменами з таблиці.

## Дефект #15: хибні номери сутр (підтверджено читанням, не виправлено)

Джерело істини всередині репо: `panini/registry/sutras.lisp` (рядки 3973–3978 у версії з issue;
у поточному файлі 8.4.53/55/58 стоять ближче до рядка 3975, перевір grep-ом).
8.4.53 = JalAM jaS JaSi; 8.4.55 = Kari ca; 8.4.58 = anusvArasya yayi parasavarRaH.

Хибні мітки:
- `panini/machine/sandhi.lisp`: 8.4.55 «khari savarṇe» (рядки 15, 82, 152), 8.4.58 «jhalāṃ jhaŚi» (114, 156).
- `panini/tests/sandhi-tests.lisp`: заголовки тестів і dispatch-рядки.
- `panini/machine/derivation.lisp`: 18, 237 (очепятка «jjal-jhashi»), 295, 313, 503;
  рядок 164 «6.1.78: iko yaṇ aci» змішує 6.1.77 з 6.1.78.
- `k + a → k` у тесті джерело-нейтральний: «not JAS»; 8.2.39 (кінцевий t перед голосним → d) не реалізовано.

## Фікстура pratyahara-exhaustive-v0.1 × граф shiva-sutras (EXPERIMENTAL-імпорт)

Імпорт з `shiva-sutras`, гілка `work/44-upc14v2-graph-sonnet`, коміт `fa7e99e484ce30b61482a4d2ae62cb9414268456`,
статус upstream: чернетка (PR #45/#46), не claim. Скрипт: `g.pratyahara(g.SOUNDS[start], marker)`.

- Збіг (set і stream): `ac-vowels`, `ik-close-vowels`, `ec-diphthongs`, `yaR-semivowels`, `hal-consonants` (h двічі в stream).
- Негативи: `unknown-marker` збіг за суттю; `marker-is-not-sound` збіг.
- Розбіжність: `later-h-is-not-initial-h-for-hR`. Фікстура вимагає явної політики початкового входження;
  граф мовчки бере перше `h` і повертає `h y v r l`.
- iṇ = `pratyahara(i,'R',2)` = `i u f x e o E O h y v r l` (у фікстурі кейсу iṇ немає).

## Голосне сандхі 6.1.77–109: джерельна таблиця

[Р] = `panini/registry/sutras.lisp`; [К] = Kāśikā, `shiva-sutras/ksetra/astadhyayi/sources/KASIKA-6.1.N.yaml`
(GRETIL jvkasipu.htm, sha256 `e78965557a…`, ед. Sharma, AUTHENTICITY-VERIFIED (Attributed)).

| Сутра | Ліворуч | Праворуч | Результат | Винятки / апавади (за [К]) |
|---|---|---|---|---|
| 6.1.77 iko yaRaci | ik | ac | відповідний yaR | plutapūrva: bho3i indram → bho3yindram |
| 6.1.78 eco'yavAyAvaH | ec | ac | ay / av / Ay / Av (yathāsaṅkhyam) | 6.1.109 — апавада |
| 6.1.87 AdguRaH | avarṇa | ac | одна guṇa-заміна | lṛ: lapratvam iṣyate |
| 6.1.88 vfdDireci | avarṇa | ec | vṛddhi | апавада до 6.1.87 |
| 6.1.97 ato guRe | apadānta a | guṇa | pararūpa | апавада до 6.1.101; apadānta: daṇḍāgram |
| 6.1.101 akaH savarRe dIrGaH | ak | savarṇa ac | одна dīrgha | vārttika ṛti ṛ vā, lṛti lṛ vā |
| 6.1.109 eNaH padAntAdati | padānta eṅ | ati | pūrvarūpa | апавада до 6.1.78; agne 'tra, vāyo 'tra |

Adhikāra: 6.1.84 ekaḥ pūrvaparayoḥ ([К]: діє до 6.1.112 виключно; [Р]: до 6.1.111). Під ним: 87, 88, 97, 101, 109.
6.1.77 і 6.1.78 стоять до 6.1.84 (заміна одного звука, не ekādeśa пари). `aci` як adhikāra до 6.1.108 ([К] 6.1.77).

Модель у `panini/machine/derivation.lisp`: 6.1.84 не змодельовано; `expand-eco-in-list` не перевіряє
padānta (6.1.109 не блокує ay/av); `savarṇa-pair?` — жорстка таблиця a/A i/I u/U f/F без x/X і без vārttika ṛ/ḷ.

Шар [SCHOLARLY]: не перевірялося. Шар [MY-LISP HYPOTHESIS]: не додавався.

## Повідомлення від «шіва» (shiva-sutras), 2026-09-30

Чи EXPERIMENTAL-імпорт: файл `docs/upc14v2-independent-review-2026-09-30.md` не закомічено, sha немає; це слова сесії, не claim.
- Повторила тести UPC-14 v2 на `fa7e99e`: 29+13+15 = 57 OK.
- Kāśikā 8.4.44: заборона na śāt, а не палаталізація.
- ṛ/ḷ savarṇa у моделі UPC-14 False, хоча Kāśikā (рядок 53198 файлу kAshikAvRRitti.md) його визнає.
  Стосується нас: `savarṇa-pair?` у `derivation.lisp` теж без ṛ/ḷ і без vārttika «ṛti ṛ vā».
- Поділ aperture ūṣman/vowel введено, щоб відтворити рядок 392, а не виведено з Kāśikā.
- Запропонувала звірити цю таблицю та номери 8.4.55/8.4.58 з Kāśikā; я попросив зробити це лише читанням.
- Її файл: лише `docs/upc14v2-independent-review-2026-09-30.md`; конфліктів із моїм немає.

## Відкриті рішення (за sdvova)

- Що брати цій сесії: #15 (виправити мітки) чи пріоритет №7 (одна доказова деривація).
- Чи вносити 164-й рядок derivation.lisp як пункт до #15 (координатор уже вніс інші місця коментарем).
- gh не авторизований у цій сесії; тексти issues #15/#16 отримані від координатора листом.
