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
- Повторено тести UPC-14 v2 на `fa7e99e`: 29+13+15 = 57 OK.
- Kāśikā 8.4.44: заборона na śāt, а не палаталізація.
- ṛ/ḷ savarṇa у моделі UPC-14 False, хоча Kāśikā (рядок 53198 файлу kAshikAvRRitti.md) його визнає.
  Стосується нас: `savarṇa-pair?` у `derivation.lisp` теж без ṛ/ḷ і без vārttika «ṛti ṛ vā».
- Поділ aperture ūṣman/vowel введено, щоб відтворити рядок 392, а не виведено з Kāśikā.
- Запропоновано звірити цю таблицю та номери 8.4.55/8.4.58 з Kāśikā; я попросив зробити це лише читанням.
- Файл шіви: лише `docs/upc14v2-independent-review-2026-09-30.md` (гілка `docs/upc14v2-review-shiva-sonnet`,
  коміт `e012465`, локально; push не пройшов через SSL); конфліктів із моїм немає.

### Результат звірки таблиці 6.1.77–109 з Kāśikā (шіва, розділ 4 її файлу)

Збігається: усі 7 рядків, приклади, adhikāra 6.1.84 (до 6.1.111 включно, реєстр те саме).
8.4.53 (рядок 83938) = JalAM jaS JaSi, 8.4.55 (83991) = Kari ca («झलां चरादेशो भवति खरि परतः», bhettā, yuyutsate),
8.4.58 (84042) = anusvāra → parasavarṇa (śaṅkitā, kuṇḍitā). Реєстр збігається; хибні лише мітки в `sandhi.lisp` і тестах.

Уточнення до моєї таблиці (прийнято, не внесено в таблицю вище, щоб не змішувати джерела):
1. 6.1.78: апавада 6.1.109 названа в Kāśikā на 6.1.109 («ayavādeśayor ayam apavādaḥ»), не на 6.1.78, і стосується лише ay/av, не āy/āv.
2. 6.1.97: за Kāśikā бʼє й vṛddhi 6.1.88 («pace, yaje ity atra vṛddhir eci iti vṛddhiḥ prāpnoti»), не лише 6.1.101.
3. 6.1.101: пропущено `aci ity eva` (kumārī śete; 1.1.10 nājjhalau) і «ḷ не має dīrgha, тому результат ṛ» (hotṝkāraḥ);
   ṛ/ḷ savarṇa задано окремим vidhi («ṛkāralṛkārayoḥ savarṇāsañjñāvidhir uktaḥ»).
4. 6.1.109: ati = коротка a (taparakaraṇam, vāyavāyāhi).

## ṛ/ḷ у 6.1.101 і 8.4.45 (текст, вставлений sdvova зі сесії шіви; не перевірено мною, EXPERIMENTAL-імпорт)

Джерело: повідомлення користувача, яке він вставив у цю сесію; належить шіві (shiva-sutras), файл `docs/upc14v2-independent-review-2026-09-30.md`
(гілка `docs/upc14v2-review-shiva-sonnet`, запушена, коміт невідомий мені). Kāśikā я за цими пунктами сам не перечитував.
- 6.1.101, чотири випадки ṛ/ḷ (за цим текстом, стосується моделі UPC-14, а не `derivation.lisp`):
  x+x → X розходження (ḷ довгого не має, рядок 389, тож F або x); f+f: {F, f}; f+x: {F, x}; x+f: {F, f} (висновок за симетрією);
  результат має бути множиною варіантів (vā), а не одним рядком.
- 8.4.45: правило опційне; усі приклади Kāśikā лише зі зупинними (vāṅ, śvaliṇ, agnicin, triṣṭub);
  носові форми y v l випливають із рядка 391 як висновок; r носової форми не має.
- Для нас: `savarṇa-pair?` у `derivation.lisp` (лише a/A i/I u/U f/F) теж повертає один рядок, а не множину варіантів.

## Відкрите питання: семантика кейсу `later-h-is-not-initial-h-for-hR`

Координатор (коміт `1264e56`, `/home/agents/work/shiva-upc7`, гілка `work/44-upc14v2-graph-sonnet`; EXPERIMENTAL-імпорт, не claim)
реалізував: типово береться перше recitation; `strict=True` кидає `AmbiguousStart`; `start_occurrence=2` для hR дає `GraphError`.
Він також змоделював 6.1.84 як `Result.ekadesa` (84 < N ≤ 111: 87, 88, 97, 101, 109 так; 77, 78 ні) і реалізував 6.1.97, 6.1.109.

Питання: чи вимагає наша фікстура помилку ЗА ЗАМОВЧУВАННЯМ, чи достатньо strict-режиму?
Відповідь із самого файлу фікстури: він НЕ вирішує це однозначно. Кейс hR очікує `requires-explicit-start-occurrence-policy`
без жодної політики у виклику, тобто читання «типово помилка» для hR; водночас кейс `hal` теж дає `start_sound: h` без політики
і очікує stream з першого h. Обидва випадки неоднозначні за формою (у обох h має два входження), фікстура розрізняє їх лише результатом.
Тому: strict opt-in сумісний з обома кейсами тільки якщо тест hR викликає strict; це рішення про семантику фікстури, воно за власником (sdvova),
а не за мною і не за upstream. Не змінюю фікстуру до його слова.

## Задачі #15/#17/#18 (виконано в цій сесії, гілки запушені, PR не створено)

- #15: гілка `fix/15-sandhi-sutra-labels` (лише коментарі/мітки: 3 файли; функції не перейменовано).
- #17: гілка `audit/17-sutra-ref-audit`: `panini/tools/audit_sutra_refs.py`, `panini/research/sutra-ref-audit-2026-09-30.md` (перевірений вручну список) і `-table-` (повна евристична таблиця). 204 посилання, 0 сиріт.
- #18: гілка `fixture/18-pratyahara-v0.2-candidates`: `panini/tests/pratyahara-exhaustive-v0.2-candidates.yaml` + `panini/tools/pratyahara_candidates.py`; 10/10 збігів зі стрімом графа (ffd8813), але це узгодженість, не незалежна перевірка.
  Попередження: у `occurrence-resolution.yaml` (shiva-sutras) виняток для aṇ приписано «8.3.32 (aṇuḍit…)», а в реєстрі 8.3.32 = `Namo hrasvAdaci NamuRnityam`; цитата «aṇudit» = 1.1.69. Джерело винятку НЕ підтверджено.
- it-saṃjñā (1.3.2–1.3.9, 1.1.71): передано координатору листом; ключове з Kāśikā на 1.3.3: маркери Śiva-sūtras (кінцеві hal, включно з l у hal) є it за 1.3.3, циклічність знімається «tantreṇa upāttam» (не розкладено). `sastra/it.md` містить сумнівне твердження про Ṇit («blocks guṇa/vṛddhi», 6.1.15): НЕвірифіковано, не виправлено.

## Відкриті рішення (за sdvova)

- Що брати цій сесії: #15 (виправити мітки) чи пріоритет №7 (одна доказова деривація).
- Чи вносити 164-й рядок derivation.lisp як пункт до #15 (координатор уже вніс інші місця коментарем).
- gh не авторизований у цій сесії; тексти issues #15/#16 отримані від координатора листом.
