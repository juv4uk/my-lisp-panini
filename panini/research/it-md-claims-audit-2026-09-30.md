# Аудит тверджень у sastra/it.md (розділ «Heterogeneity of Effects»), 2026-09-30

Read-only: `panini/sastra/it.md` НЕ змінено. Мета: після дозволу sdvova виправити одним PR.
Джерела: `panini/registry/sutras.lisp` (рядки :slp1/:meaning) і Kāśikā (`KASIKA-N.N.N.yaml`, sha256 `e78965557a6f…`, у `shiva-sutras/ksetra/astadhyayi/sources/`).
Рядки txt для цих сутр НЕ шукав. Що НЕ перевірено: шар [SCHOLARLY] (Cardona/Kiparsky у it.md) я не читав; тут лише шар [PANINI].

| # | Твердження в it.md | Що кажуть реєстр і Kāśikā | Статус |
|---|---|---|---|
| 1 | «Ṇit: blocks guṇa and vṛddhi strengthening» | 7.2.115 `aco YRiti`: ajanta-aṅga отримує vṛddhi перед ñit/ṇit (Kāśikā: «ñiti ṇiti ca pratyaye vṛddhir bhavati», приклади ñiti: kāraḥ, hāraḥ; ṇiti: gāvau, jaitram). Блокують guṇa/vṛddhi kit/gīt/ṅit: 1.1.5 `kkNiti ca` (Kāśikā: «kṅin-nimitte ye guṇa-vṛddhī prāpnutaḥ, te na bhavataḥ»). | ХИБНО: ṇit не блокує, а викликає vṛddhi; блокує ṅit/kit. Схоже на змішання ṇ з ṅ/k. |
| 2 | «(Ṇit) triggers samprasāraṇa (6.1.15)» | 6.1.15 `vacisvapiyajAdInAM kiti`: samprasāraṇa перед kit (Kāśikā: «kiti pratyaye parataḥ samprasāraṇam bhavati»: uktaḥ, suptaḥ, iṣṭaḥ). | ХИБНО: умова kit, не ṇit. |
| 3 | «Ñit: causes vṛddhi (7.2.115)» | 7.2.115: так, ñit і ṇit обидва (Kāśikā дає окремі приклади ñiti і ṇiti). | ВІРНО, але неповно: пропущено ṇit. |
| 4 | «Ñit … on a dhātu allows both active and middle endings (ubhayapada, 1.3.72)» | 1.3.72 `svaritaYitaH kartraBiprAye kriyAPale`: dhātu з svarita-it або ñit отримує ātmanepada, коли плід дії йде діячу; Kāśikā: «śeṣāt kartari parasmaipade prapte … ātmanepadaṃ bhavati, kartāraṃ cet kriyāphalam abhipraiti» (приклади: yajate, sunute; протилежне: yajanti yājakāḥ). | НЕТОЧНО: правило про ātmanepada за умови kartrabhiprāya (за інших умов лишається parasmaipada); слово «ubhayapada» у цій сутрі відсутнє. |
| 5 | «pit: Indicates grave (anudātta) accent (3.1.4)» | 3.1.4 `anudattO suppitO`: sup-pratyaya і pit-pratyaya anudātta (Kāśikā: «supaḥ pitaś ca pratyayā anudāttā bhavanti», приклади pacati, paṭhati). | ВІРНО. |
| 6 | «pit: explicitly allows guṇa/vṛddhi for sārvadhātuka affixes» | Прямого правила «pit дозволяє guṇa» немає. Механізм: 1.2.4 `sArvaDAtukamapit` (apit sārvadhātuka поводиться як ṅit, тобто guṇa блокується; Kāśikā: kurutaḥ, kurvanti; «apit iti kim? karoti, karoṣi, karomi» — pit-форми ṅidvat не отримують), а 7.3.84 `sArvaDAtukArDaDAtukayoH` дає guṇa. | НЕТОЧНО: guṇa для pit випливає з відсутності 1.2.4, а не з «явного дозволу». |

Спостереження: рядок «1.3.2–1.3.9» у Source Anchor і твердження про 1.3.2/1.3.3/1.3.9 в it.md збігаються з реєстром (`upadeSe'janunAsika it`, `halantyam`, `tasya lopaH`).
Пропозиція для одного PR (після слова sdvova): виправити пункти 1, 2, 4, 6 і доповнити 3; шар [PANINI] має цитувати сутри й Kāśikā, а не переказ.
