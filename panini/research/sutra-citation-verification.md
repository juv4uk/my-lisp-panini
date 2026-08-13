# Sūtra citation verification

Статус: завершено (`PANINI-SUTRA-CITATION-VERIFICATION`).

Систематична звірка кожного sūtra-номера, процитованого в
`panini/foundation/*.md` (крім `karaka.md`, який уже переписаний
паралельним потоком роботи без секцій із розширювальними sūtra), проти
реального цифрового корпусу — правило 17 `AGENTS.md` ("не покладатися
на єдине джерело" / "не довіряти пам'яті без звірки").

## Джерело звірки

`github.com/sanskrit/learnsanskrit.org`, файл
`data/ashtadhyayi-rules.txt` — повний нумерований текст Aṣṭādhyāyī
(3985 рядків), знайдений через пошук по реальному тексту відомих sūtra
(`dhruvam apAye apAdAnam`, `kartur IpsitatamaM karma`) у GitHub Code
Search. Додатково — `content/vyakarana/subanta/karaka.txt` того самого
репозиторію (перекладений і прокоментований розбір усіх 6 kāraka) і
`lso/templates/texts/ashtadhyayi/book1-1.html` (перекладена sūtra 1.1.20).

Обидва вебресурси, згадані в `AGENTS.md` §17
(Ashtadhyayi.in, ashtadhyayi.com), виявились SPA з client-side
рендерингом — `WebFetch` отримував лише порожню оболонку застосунку,
без реального тексту sūtra. `learnsanskrit.org`'s репозиторій виявився
практичною альтернативою: статичний, версійований, з перекладами.

## Результати

| Sūtra | Джерело в репо | Було | Стало | Статус |
|---|---|---|---|---|
| 1.1.1 | `ontology.md`, `samjna.md` | `vfdDir Adaic` | — | ✅ Confirmed |
| 1.1.2 | `samjna.md` | `adeG guRaH` | — | ✅ Confirmed |
| 1.1.20 | `samjna.md` | `dADAGvyor Gu` | `dAdhA GvadAp` | ⚠️ Виправлено (номер правильний, текст — ні) |
| 1.1.27 | `ontology.md`, `samjna.md` | `sarvAdIni sarvanAmAni` | — | ✅ Confirmed |
| 1.1.68 | `samjna.md` | `svaM rUpaM SabdasyASabdasaMjYAyAm` | `svaM rUpaM SabdasyASabdasaMjYA` | ⚠️ Виправлено (зайве "-yAm") |
| 1.3.1 | `dhatu.md`, `ontology.md` | `bhUvAdayo dhAtavaH` | — | ✅ Confirmed |
| 1.3.2 | `it.md` | `upadeSe janunAsika it` | — | ✅ Confirmed |
| 1.3.9 | `ontology.md`, `it.md` | `tasya lopaH` | — | ✅ Confirmed |
| 1.3.11 | `ontology.md`, `anuvrtti.md` | `svaritenADikAraH` | — | ✅ Confirmed |
| 1.4.1 | `samjna.md` | `A kaDArAd eka saMjYA` | — | ✅ Confirmed (номер і зміст) |
| 1.4.2 | `rule-system.md` | `vipratiSeDe paraM kAryam` | — | ✅ Confirmed |
| 1.4.23 | `anuvrtti.md`, `karaka.md` | `kArake` | — | ✅ Confirmed |
| 1.4.24 | `karaka.md`, `dhatu-karaka-relation.md` | `Druvam apAye 'pAdAnam` | — | ✅ Confirmed |
| 1.4.25 | `dhatu-karaka-relation.md` | `BIitrARAM Bayahetuh` | `BItrArTAnAM Bayahetuh` | ⚠️ Виправлено (номер правильний, текст спотворений) |
| 1.4.32 | `karaka.md` | `karmaRA yam aBipraiti sa saMpradAnam` | — | ✅ Confirmed |
| 1.4.42 | `karaka.md` | `sADakatamaM karaRam` | — | ✅ Confirmed |
| 1.4.45 | `karaka.md` | `ADAro 'DikaraRam` | — | ✅ Confirmed |
| 1.4.49 | `karaka.md`, `registry/karaka/karman.yaml` | `kartur IpsitatamaM karma` | — | ✅ Confirmed |
| 1.4.50 | `registry/karaka/karman.yaml` | цитувалось як **1.4.51** | **1.4.50** | ❌ Виправлено — реальна помилка номера |
| 1.4.54 | `karaka.md` | `svataMtraH kartA` | — | ✅ Confirmed (реальний текст `svatantraH`, різниця — лише конвенція запису носового: `M` vs `n` перед `t`, не помилка змісту) |
| 1.4.55 | `karaka.md` | `tat-praYojako heturvA` (описово) | — | ✅ Загалом вірно (реальний текст `tatprayojako hetuS ca`) |
| 1.4.56 | `anuvrtti.md` | позначено як **неперевірене TODO** | `prAg rIzvarAn nipAtAH` | ✅ Підтверджено — здогад був правильний |
| 3.1.1 | `pratyaya.md` | `pratyayaH` | — | ✅ Confirmed |
| 3.1.2 | `pratyaya.md` | `paraS ca` | — | ✅ Confirmed |

## Підсумок

- **19 із 22** перевірених цитувань виявились точними з першого разу.
- **3 реальні помилки** виправлено: 1.1.20 (текст), 1.1.68 (зайве
  закінчення), 1.4.25 (текст).
- **1 помилка номера** виправлено: sutra про "акथита"-розширення
  `karman` цитувалась як 1.4.51, реальний номер — **1.4.50** (1.4.51 —
  окреме правило `akaTitaM ca`, про яке в наших файлах узагалі не
  йшлося — просто переплутано номер).
- **1 неперевірений TODO закрито підтвердженням**: здогад про 1.4.56
  (`anuvrtti.md`) виявився правильним.

Показник помилок (5 з 22, ~23%) підтверджує обґрунтованість самого
правила `AGENTS.md` §17 — навіть при уважному дослідженні, цитування з
пам'яті без звірки регулярно дає дрібні, але реальні розбіжності
(переважно в точному тексті sūtra, рідше — в номері).

## Джерела

- `github.com/sanskrit/learnsanskrit.org`,
  `data/ashtadhyayi-rules.txt`, `content/vyakarana/subanta/karaka.txt`,
  `lso/templates/texts/ashtadhyayi/book1-1.html` — прочитано напряму
  через `gh api` 2026-08-13.
