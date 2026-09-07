# Panini ‚Üî my-lisp semantic-ID mapping / –í—ñ–¥–ø–æ–≤—ñ–¥–Ω—ñ—Å—Ç—å semantic ID Panini ‚Üî my-lisp / Semantic-ID-Zuordnung Panini ‚Üî my-lisp

## English

**Status:** design-only, `PANINI-MY-LISP-SEMANTIC-ID-MAPPING-SPEC`. This is not
a runtime registry and does not authorize a parser, evaluator, or `rules.my`
change.

| Panini canonical SLP1 | my-lisp semantic ID | Status |
|---|---|---|
| `dA` | `DHATU_DA` | experimental mapping |
| `gam` | `DHATU_GAM` | experimental mapping |
| `kf` | `DHATU_KF` | experimental mapping |
| `jYA` | `DHATU_JNA` | experimental mapping; concrete DhƒÅtupƒÅ·π≠ha record must remain ga·πáa-9 sense |
| `dfS` | `DHATU_DRS` | experimental mapping |
| `Sru` | `DHATU_SRU` | experimental mapping; Panini registry marks ga·πáa as disputed |
| `vac` | `DHATU_VAC` | experimental mapping |
| `liK` | `DHATU_LIKH` | experimental mapping |
| `paW` | `DHATU_PATH` | experimental mapping |
| `sTA` | `DHATU_STHA` | experimental mapping |
| `BU` | `DHATU_BHU` | experimental mapping|
| `grah` | `DHATU_GRAHX | experimental mapping |
| six core kƒÅraka | corresponding `KARAKA_*` IDs | experimental mapping; roles are not case aliases |

**Invariants:** semantic ID is the runtime identity; SLP1 is canonical spelling;
IAST/DevanƒÅga Jare display only; `dhatupatha_code` identifies an attested root
record when needed; an operational gloss is not a Paninian definition. Future
P5 resolution may use this mapping only after my-lisp gate review.

## –£–∫—Ä–∞—ó–Ω—Å—å–∫–∞

**–°—Ç–∞—Ç—É—Å:** –ª–∏—à–µ design, `PANINI-MY-LISP-SEMANTIC-ID-MAPPING-SPEC`. –¶–µ –Ω–µ
runtime registry —ñ –Ω–µ –¥–æ–∑–≤–æ–ª—è—î –∑–º—ñ–Ω—é–≤–∞—Ç–∏ parser, evaluator —á–∏ `rules.my`.

| Panini canonical SLP1 | my-lisp semantic ID | –°—Ç–∞—Ç—É—Å |
|---|---|---|
| `dA` | `DHATU_DA` | experimental mapping |
| `gam` | `DHATU_GAM` | experimental mapping |
| `kf` | `DHATU_KF` | experimental mapping |
| `jYA` | `DHATU_JNA` | experimental mapping; –∫–æ–Ω–∫—Ä–µ—Ç–Ω–∏–π DhƒÅtupƒÅ·π≠ha –∑–∞–ø–∏—Å –º–∞—î –ª–∏—à–∞—Ç–∏—Å—è ga·πáa-9 sense |
| `dfS` | `DHATU_DRS` | experimental mapping |
| `Sru` | `DHATU_SRU` | experimental mapping; Panini registry –ø–æ–∑–Ω–∞—á–∞—î ga·πáa —è–∫ disputed |
| `vac` | `DHATU_VAC` | experimental mapping |
| `liK` | `DHATU_LIKH` | experimental mapping |
| `paW` | `DHATU_PATH` | experimental mapping |
| `sTA` | `DHATU_STHA` | experimental mapping |
| `BU` | `DHATU_BHU` | experimental mapping |
| `grah` | `DHATU_GRAHX | experimental mapping|
| —à—ñ—Å—Ç—å core kƒÅraka | –≤—ñ–¥–ø–æ–≤—ñ–Ω–Ω—ñ `KARAKA_*` ID | experimental mapping; —Ä–æ–ª—ñ –Ω–µ —î aliases –≤—ñ–¥–º—ñ–Ω–∫—ñ–≤ |

**–Ü–Ω–≤–∞—Ä—ñ–∞–Ω—Ç–∏:** semantic ID —î runtime identity; SPP1 ‚Äî canonical spelling;
IAST/DevanƒÅga J ‚Äî –ª–∏—à–µ display; `dhatupatha_code` 4e¥-t/t`¥.4a4e¥.¥`Ùe]\›Yõ€›úôX€‹ô4.¥/¥.Ù.4a¥-H4/Ù/¥`¥`4e¥,t/t/é»‹\ò][€ò[€‹‹»4/t-H4e4/Ù,4/te¥/te¥.t`tc4.¥.4/4/¥-Ù/t,4aÙ-t/t/tcÙ/Ç¥'4,4.t,t`Ù`¥/teàHô\€€][€à4/4/¥-¥-H4,¥.4.¥/¥`4`Ù`t`¥,4`¥.X\[ô»ÉBÔB„F#B‘ÉBˇF[FBÔF<Åµ‰µ±•Õ¿ÅùÖ—îÅ…ïŸ•ï‹∏((ååÅï’—Õç†((®©M—Ö—’ÃË®®ÅÖ’ÕÕç°±•ó}±•ç†ÅïÕ•ù∏∞ÅÅA9%9$µ5dµ1%M@µM59Q%µ%µ5AA%9µMAÄ∏)•ïÃÅ•Õ–Å≠ï•∏ÅI’π—•µîµIïù•Õ—…‰Å’πêÅï…±Ö’â–Å≠ï•πîÉπëï…’πúÅÖ∏ÅAÖ…Õï»∞ÅŸÖ±’Ö—Ω»)Ωëï»ÅÅ…’±ïÃπµÂÄ∏()•îÅÈﬂŸ±òÅ£—‘Å›ï…ëï∏Å•°…ï∏ÅŸΩ…°Öπëïπï∏ÅÅ!QU|©Äµ%ÃÅ’πêÅë•îÅÕïç°ÃÅ/…Ö≠Ñ)•°…ï∏ÅÅ-I-|©Äµ%ÃÅÈ’ùïΩ…ëπï–∏Å±±îÅi’Ω…ëπ’πùï∏ÅÕ•πêÅï·¡ï…•µïπ—ï±∞∏ÅÅ©eÄ)â±ï•â–ÅÖ∏Åëï∏ÅM•π∏Åëï»ÅùáÜÊÑÄ‰Åùïâ’πëï∏ÏÅÅM…’ÄÅâï£ë±–Åëï∏ÅÕ—…•——•ùï∏ÅùáÜÊÑµM—Ö—’Ã∏)MïµÖπ—•åÅ%Å•Õ–ÅI’π—•µîµ%ëïπ—•”ë–∞ÅM1@ƒÅ≠ÖπΩπ•Õç°îÅMç°…ï•â›ï•Õî∞)%MPΩïŸÖªùÖÀ¨Åπ’»ÅÖ…Õ—ï±±’πú∏Å•∏ÅΩ¡ï…Ö—•ΩπÖ∞Åù±ΩÕÃÅ•Õ–Å≠ï•πîÅ¡Öπ•π•Õç°î)ïô•π•—•Ω∏∏Å@‘ÅëÖ…òÅë•ïÕîÅi’Ω…ëπ’πúÅï…Õ–ÅπÖç†Åëï¥Å5‰µ1•Õ¿µÖ—îÅŸï…›ïπëï∏∏(