# Sarvam — повна довідка можливостей через наш протокол зв'язку

Статус: v0.1, зібрано 2026-08-18. Доповнює
`docs/sarvam-integration-guide.md` (`shiva-sutras`) — той документ
пояснює *як* користуватись Sarvam (два канали, баг з reasoning-токенами,
методологія незалежної перевірки); цей документ — *що саме* доступно
через ці канали, зведено з (а) реальних схем 24 MCP-інструментів
(`mcp__sarvam-ai__sarvam_tools_*`), (б) офіційної документації
Sarvam (`docs.sarvam.ai`), (в) живого тестування в цій сесії.

**Важливо:** Sarvam — незалежний гіпотезогенератор, не source of
truth (`sarvam-integration-guide.md`). Ця довідка описує *що можна
викликати*, не підтверджує *правильність відповідей* для нашого
домену (Sanskrit/Pāṇini) — див.
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md)
для конкретного підтвердженого прикладу помилки на `bhAz`.

## Два канали доступу (нагадування)

- **MCP tools** (`mcp__sarvam-ai__sarvam_tools_*`, `sarvam_code_*`) —
  для Claude Code сесій із налаштованим MCP-сервером `sarvam-ai`.
- **HTTP proxy** (`C:/GitHub/sarvam-proxy/server.py`,
  OpenAI-сумісний, `POST /v1/chat/completions`) — для звичайних
  скриптів поза Claude Code.
- Не писати третій wrapper — обидва канали вже покривають усі відомі
  випадки.

## Повний реєстр `sarvam_tools_*` (24 інструменти)

### Текст / LLM

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_llm_complete` | Chat completion, модель `sarvam-105b` (105B MoE, reasoning) | **Баг**: reasoning з'їдає `max_tokens` (типово 2048), лишаючи порожній `content` при `finish_reason: "length"`. Офіційно підтверджено `docs.sarvam.ai`: не задавати `max_tokens` для коротких відповідей, або `reasoning_effort=null` (ненадійно — у нас спрацювало раз, потім ні) |
| `sarvam_tools_recall` | RAG-подібне питання-відповідь по файлах (аудіо транскрибується, текст читається напряму, до 24000 символів) | до 20 файлів (`max_files`), директорії обходяться рекурсивно |
| `sarvam_tools_text_analytics` | Типізовані запитання до тексту (`boolean`/`enum`/`short answer`/`long answer`/`number`) — структурована екстракція без ручного промпту | — |

### Переклад / локалізація

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_translate` | Переклад EN↔22 індійські мови, 2 моделі: `mayura:v1` (11 мов, стилі formal/colloquial/code-mixed) чи `sarvam-translate:v1` (22 мови, лише formal) | **`sa-IN` (санскрит) є в enum `source`/`target`** для перекладу |
| `sarvam_tools_localize` | Масовий переклад JSON/`key=value` файлів локалізації, вкладені структури, пише сусідній файл із суфіксом мови | до 500 рядків (`max_strings`) за виклик |

### Транслітерація / ідентифікація

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_transliterate` | Конвертація писемності без перекладу (Devanagari→Latin тощо) | **`sa-IN` НЕ підтримується** — ні в реальному API (перевірено живим викликом цієї сесії: помилка `Input should be 'auto', 'en-IN', 'hi-IN', ...`), ні в офіційній документації (`docs.sarvam.ai`: "Transliteration API currently supports: English, Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu" — санскриту немає). Обхідний шлях: `hi-IN` як спільна деванагарі-писемність, з усвідомленням, що це не санскритська модель |
| `sarvam_tools_identify_language` | Визначення мови+писемності тексту (BCP-47 код + назва писемності) | Корисно як препроцесинг перед TTS/translate |

### Мовлення (STT/TTS/дублювання)

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_stt_transcribe` | Розпізнавання мовлення, модель `saaras:v3`, режими `transcribe`/`translate`/`verbatim`/`translit`/`codemix` | `sa-IN` є в enum мов інструмента, **але зовнішні джерела (пошук 2026-08-18) не підтверджують санскрит у офіційному переліку Saaras v3** — суперечність між enum і документацією, не перевірено живим викликом у цій сесії |
| `sarvam_tools_stt_batch_submit`/`_status` | Пакетна транскрипція довгих файлів (>30с), діаризація, таймстемпи | Повний конвеєр (job→upload→poll) автоматизований в одному виклику |
| `sarvam_tools_stt_translate` | **DEPRECATED** — використовувати `stt_transcribe` з `mode='translate'` | — |
| `sarvam_tools_tts_speak`/`_stream` | Синтез мовлення, модель `bulbul:v3`, 25+ голосів, 11 мов | `sa-IN` **немає** серед `target_language_code` (лише `en-IN, hi-IN, bn-IN, ta-IN, te-IN, gu-IN, kn-IN, ml-IN, mr-IN, pa-IN, od-IN`) — і в enum інструмента, і за зовнішніми джерелами; до ~500 символів за виклик |
| `sarvam_tools_dub` | Дублювання аудіо: STT→переклад→TTS одним викликом | Вихідні мови обмежені тим самим переліком 11, що й TTS |
| `sarvam_tools_voice` | Голосовий агент "з кінця в кінець": транскрибує→LLM-відповідь→синтезує | Комбінує обмеження STT+LLM+TTS |

### Вимова

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_pronunciation_create/get/list/delete` | Словники вимови "слово→вимова" для контролю TTS | Максимум 100 слів/словник, 10 словників/користувач |

### Документи / зображення

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_vision_extract` | Витяг тексту/структури з документа чи зображення (Document Intelligence), збереження таблиць, 23 мови | До 10 сторінок/документ, повний async-конвеєр автоматизований |
| `sarvam_tools_vision_job_status` | Опитування статусу job для `vision_extract` | — |

### Службові

| Інструмент | Що робить |
|---|---|
| `sarvam_tools_set_api_key` | Встановити/оновити API-ключ |
| `sarvam_tools_upgrade` | Перевірити/оновити версію MCP-сервера |

### `sarvam_code_*` (окрема група — допомога з написанням коду, не runtime-виклики)

`sarvam_code_api_reference`, `sarvam_code_languages`, `sarvam_code_pricing`,
`sarvam_code_recommend_model`, `sarvam_code_snippet`, `sarvam_code_speakers`,
`sarvam_code_validate_request` — довідкові інструменти для написання
власного коду проти Sarvam API (документація, приклади, підбір
моделі, валідація запиту перед відправкою), **не викликають Sarvam
API самі по собі**. Не досліджені детально в цій задачі — окрема
нагода, якщо колись знадобиться писати прямі HTTP-виклики поза MCP.

## Санскрит (`sa-IN`) — зведена матриця підтримки

| Інструмент | `sa-IN` в enum схеми | Підтверджено зовні (docs/форуми) | Перевірено живим викликом |
|---|---|---|---|
| `translate` | ✅ | ✅ (Sarvam-Translate заявляє 22 мови, санскрит серед них) | ні |
| `transliterate` | ✅ (в схемі!) | ❌ (офіційно не в списку 11 підтримуваних мов) | ❌ **підтверджено помилкою API** цієї сесії |
| `stt_transcribe`/`stt_batch_submit` | ✅ | ⚠️ суперечливо (не знайдено в жодному зовнішньому переліку) | ні |
| `tts_speak`/`tts_stream`/`dub` | ❌ (немає в enum) | ❌ (11 мов, санскриту немає) | ні |
| `localize` | ✅ | не перевірено окремо | ні |

**Висновок:** enum-схеми MCP-інструментів системно оптимістичніші за
реальну підтримку санскриту, ніж і сам API (підтверджено для
`transliterate`), і зовнішня документація. **Перед будь-яким новим
використанням `sa-IN` в цьому репозиторії — спершу пробний виклик,
не довіра enum-списку.**

## Джерела

- Живі схеми 24 `mcp__sarvam-ai__sarvam_tools_*` інструментів,
  завантажені через `ToolSearch` 2026-08-18.
- Живий виклик `sarvam_tools_transliterate` з `sa-IN` — помилка API,
  запротокольовано в цій сесії.
- [Sarvam AI Chat Completion API docs](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview) — reasoning_content/max_tokens.
- [Transliteration API docs](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-processing/transliteration) — офіційний перелік 11 мов без санскриту.
- [explainx.ai — Sarvam AI Capabilities guide (2026)](https://explainx.ai/blog/sarvam-ai-capabilities-api-models-guide-2026) — зведений огляд моделей/мов.
- `docs/sarvam-integration-guide.md` (`shiva-sutras`) — методологія
  використання й перевірене обхідне рішення для reasoning-багу.
- [`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md) — конкретний приклад ненадійності для нашого домену.
