# UPC-14: вимоги споживача (my-lisp-panini) і незалежна друга реалізація, 2026-10-01

Статус: вхід для кандидата в канон, не claim. Зона запису: лише my-lisp-panini; код/доки shiva-sutras не чіпав.
Шари: [PANINI] там, де є сутра чи Kāśikā; решта це вимоги споживача ([MY-LISP HYPOTHESIS]) і вимірювання.

## Що запускав / читав / не перевірив

- Запускав: `python3 panini/tools/second_impl_pratyahara_savarna.py --graph /home/agents/work/shiva-upc7/prototype` (upc14v2 з worktree `work/44-upc14v2-graph-sonnet`, `7986023`).
- Читав: `panini/specs/derivation-ir-v0.1.md`, `panini/specs/panini-foundation-v0.1.md`, `panini/sastra/pratyahara.md`, `panini/machine/siva-sutras.lisp`, `panini/machine/derivation.lisp` (`savarṇa-pair?`), дослідження в `panini/research/` (it-samjna-exhaustive-matrix, savarna-rl-source-audit-2026-09-30, vowel-sandhi table у coordination-log), `KASIKA-1.1.9.yaml`, `kAshikAvRRitti.txt` 375-403.
- Не перевірив: [SCHOLARLY] шар (Cardona, Kiparsky); Siddhāntakaumudī і Mahābhāṣya на 1.1.9; запуск `machine/` на SENS (несумісний, див. PR #26); `e/ai`, `o/au` savarṇa.

## (1) Що my-lisp-panini мусить отримувати від UPC-14

| # | Потрібно / не потрібно / не знаю | Вимога | Де в наших специфікаціях |
|---|---|---|---|
| 1 | ПОТРІБНО | Стабільний SLP1-ідентифікатор кожного з 42 звуків; round-trip SLP1; жодних IAST/Devanāgarī як ID | AGENTS §2; `specs/derivation-ir-v0.1.md` (Term: `source_form`, `surface_form` SLP1) |
| 2 | ПОТРІБНО | Запит pratyāhāra `(початок, маркер, nth маркера, вхід початку)` → потік І множина; невідомий маркер = помилка; повторюваний початок (`h`, `R`) = явна політика, не мовчазний вибір | `tests/pratyahara-exhaustive-v0.1.yaml` (потік vs множина), кандидати v0.2 (PR #21); `machine/siva-sutras.lisp` (`resolve-pratyahara`) |
| 3 | ПОТРІБНО | Маркер (it) як окремий вид сутності, НЕ звук і НЕ член множини; 14 маркерних клітин у порядку сутр | `sastra/pratyahara.md` (1.1.71), `research/it-samjna-exhaustive-matrix.md` (1.3.2–1.3.9), кейс `marker-is-not-sound` у v0.1 |
| 4 | ПОТРІБНО | Запит savarṇa `(a, b)`, ТРИЗНАЧНИЙ: так / ні / не визначено джерелом; прапорець vārttika для ṛ/ḷ | `research/savarna-rl-source-audit-2026-09-30.md`; `machine/derivation.lisp` `savarṇa-pair?` (зараз лише a/A, i/I, u/U, f/F, без ḷ) |
| 5 | ПОТРІБНО | Результат sandhi-запиту як МНОЖИНА варіантів (`vā`) + список застосованих сутр (для trace), не один рядок | `specs/derivation-ir-trace-events-v0.1.md`, `specs/trace-evidence-model-v0.1.md`; vowel 6.1.77–109 таблиця в `research/coordination-log-2026-09-30.md` |
| 6 | ПОТРІБНО | Довгі й назалізовані голосні (A I U F, інших варіантів) як перші класи: наш `derivation.lisp` вже використовує `A I U F` | `machine/derivation.lisp` (`savarṇa-pair?`, `apply-savarṇa-dīrgha`); ці звуки НЕ входять у 42 звуки Śiva-sūtra |
| 7 | ПОТРІБНО | Походження кожної відповіді: репо, claim, статус, sha, EXPERIMENTAL-позначка для невизнаного | AGENTS §21b; `coordination/dependencies.yaml`; `ecosystem/imports/shiva_claims.lisp` |
| 8 | НЕ ПОТРІБНО | Ширина коду (7 чи 14 біт), розкладка полів, FPGA/ISA-кодування, ефекти апаратури | Foundation Independence Test (AGENTS §21); `specs/bridge-to-my-lisp.md` |
| 9 | НЕ ПОТРІБНО | Внутрішні поля вершини (place/aperture/nasal/voice/asp) у публічному інтерфейсі; споживачу потрібні лише відповіді запитів 2–6 | `specs/derivation-ir-v0.1.md` (IR посилається на правила, а не на біти) |
| 10 | НЕ ПОТРІБНО | Операції rewrite як частина кодека (it-lopa, 6.1.84 ekādeśa як станова зміна): це rule engine | `machine/derivation.lisp`, `specs/panini-derivation-machine-v0.1-milestone.md` |
| 11 | НЕ ЗНАЮ | Чи брати від UPC-14 sandhi-запити як канон: наші власні реалізації спрощені й мають відомі пробіли (8.2.39, 6.1.84), тож потрібне джерело-перевірене еталонне значення, а не друга копія | PR #19/#29 (мітки), `research/sutra-ref-audit-2026-09-30.md` |
| 12 | НЕ ЗНАЮ | adhikāra/anuvṛtti і tripādī-видимість: чи постачає їх UPC-14, чи окремий граф сутр (координатора); ми зберігаємо їх як зовнішні анотовані дані | `specs/anuvrtti-representation-boundary.md`, `specs/tripadi-visibility-relation-v0.1.md` |

## (2) Незалежна друга реалізація: порівняння з upc14v2

Реалізація: `panini/tools/second_impl_pratyahara_savarna.py`. Вхід ТІЛЬКИ: 14 сутр із `tests/pratyahara-exhaustive-v0.1.yaml` та класи savarṇa з Kāśikā 1.1.9 (`vargyo vargyeṇa savarṇaḥ`; `rephoṣmaṇāṃ savarṇā na santi`; `ya/va/la` окремо; vārttika ṛ~ḷ, txt 400-403). Код upc14v2 імпортується лише на кроці порівняння.

| Перевірка | Обсяг | Розбіжностей |
|---|---|---|
| Pratyāhāra: усі комбінації (початок, вхід початку, маркер, nth ∈ {1,2}), що існують на шляху сутр | 305 | 0 |
| Pratyāhāra: іменовані (42 з `pratyahara-usage.yaml`, з виправленими `haś`, `jhaś`, `yaṇ`; `aṇ`×2) | 42 | 0 |
| Savarṇa без vārttika: усі пари 42 звуків | 861 | 0 (2 пари `e~ai`, `o~au` НЕ визначені джерелом; граф каже `False`) |
| Savarṇa з vārttika (ṛ~ḷ): усі пари | 861 | 0 (ті самі 2 невизначені) |

Застереження про силу доказу (чесно): (а) pratyāhāra: обидві реалізації скануть той самий лінійний шлях сутр з вибором входження, тож це подвійна перевірка РЕАЛІЗАЦІЇ, а не підтвердження традиції; традиційну сторону (occurrence-resolution) я прийняв як EXPERIMENTAL-імпорт з `shiva-sutras`; (б) savarṇa: мій оракул береться з Kāśikā 1.1.9 (класи за varga, окремі сонорні/ūṣman, vārttika), а upc14v2 виводить із ознак (place, aperture): збіг 861/861 пар означає, що ознаки відтворюють ці класи, але ознаки самі є моделюванням шіви/координатора; (в) пари з довгими й назалізованими звуками не входять у 42 і не перевірялися; (г) невизначені `e~ai`, `o~au`: Kāśikā 1.1.9 дає кожному sandhyakṣara власні 12 різновидів і не називає їх savarṇa, але й не заперечує прямо.

## (3) Питання до власника або шіви (до 5), щоб UPC-14 став кандидатом у канон

1. Що саме стверджує кандидат у канон: лише «ця структура коректно кодує Śiva-sūtra і відповіді на запити 2–4» (інженерний claim) чи також щось про Паніні? Яким буде статус нових claim-ID (наприклад `proved-in-model` чи `EXPERIMENTAL`), щоб downstream міг їх імпортувати без підвищення статусу?
2. `e~ai` і `o~au` savarṇa: UPC-14 каже «ні», Kāśikā 1.1.9 мовчить. Яке джерело (Siddhāntakaumudī, Mahābhāṣya) вирішує питання, і чи може кодек повертати «не визначено» замість булевого?
3. Довгі, назалізовані й плутові голосні (наприклад `A I U F`): чи входять вони в канон як перші класи з SLP1-ID? Без цього споживач не може виразити 6.1.101 (`akaḥ savarṇe dīrghaḥ`).
4. Політика початку, що повторюється (`hR`, `later-h-is-not-initial-h-for-hR`): помилка за замовчуванням чи opt-in strict; це рішення sdvova (і воно визначає семантику фікстури v0.1).
5. Vārttika ṛ~ḷ: частина канону чи прапорець `vartika=True` поза каноном? І чи повертає sandhi-запит множину варіантів (`vā`) як вимагає наш IR (вимога 5)?
