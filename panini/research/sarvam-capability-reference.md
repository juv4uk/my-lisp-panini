# Sarvam — full capability reference over our communication protocol

## English

Status: v0.1, compiled 2026-08-18. Supplements
`docs/sarvam-integration-guide.md` (`shiva-sutras`) — that document
explains *how* to use Sarvam (two channels, the reasoning-token bug,
independent-verification methodology); this document is *what exactly*
is available through those channels, compiled from (a) the live
schemas of the 24 MCP tools (`mcp__sarvam-ai__sarvam_tools_*`), (b)
Sarvam's official documentation (`docs.sarvam.ai`), (c) live testing
during this session.

**Important:** Sarvam is an independent hypothesis generator, not a
source of truth (`sarvam-integration-guide.md`). This reference
describes *what can be called*, it does not confirm *the correctness
of answers* for our domain (Sanskrit/Pāṇini) — see
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md)
for a concrete confirmed error on `bhAz`.

### Two access channels (reminder)

- **MCP tools** (`mcp__sarvam-ai__sarvam_tools_*`, `sarvam_code_*`) —
  for Claude Code sessions with the `sarvam-ai` MCP server configured.
- **HTTP proxy** (`C:/GitHub/sarvam-proxy/server.py`, OpenAI-compatible,
  `POST /v1/chat/completions`) — for regular scripts outside Claude
  Code.
- Do not write a third wrapper — both channels already cover every
  known case.

### Full registry of `sarvam_tools_*` (24 tools)

#### Text / LLM

| Tool | What it does | Key limitations |
|---|---|---|
| `sarvam_tools_llm_complete` | Chat completion, model `sarvam-105b` (105B MoE, reasoning) | **Bug**: reasoning eats into `max_tokens` (default 2048), leaving an empty `content` with `finish_reason: "length"`. Officially confirmed by `docs.sarvam.ai`: don't set `max_tokens` for short answers, or set `reasoning_effort=null` (unreliable — worked once for us, then didn't) |
| `sarvam_tools_recall` | RAG-like Q&A over files (audio is transcribed, text is read directly, up to 24000 characters) | up to 20 files (`max_files`), directories are traversed recursively |
| `sarvam_tools_text_analytics` | Typed questions about text (`boolean`/`enum`/`short answer`/`long answer`/`number`) — structured extraction without a manual prompt | — |

#### Translation / localization

| Tool | What it does | Key limitations |
|---|---|---|
| `sarvam_tools_translate` | EN↔22 Indian languages translation, 2 models: `mayura:v1` (11 languages, formal/colloquial/code-mixed styles) or `sarvam-translate:v1` (22 languages, formal only) | **`sa-IN` (Sanskrit) is in the `source`/`target` enum** for translation |
| `sarvam_tools_localize` | Bulk translation of JSON/`key=value` localization files, nested structures, writes an adjacent file with a language suffix | up to 500 rows (`max_strings`) per call |

#### Transliteration / identification

| Tool | What it does | Key limitations |
|---|---|---|
| `sarvam_tools_transliterate` | Script conversion without translation (Devanagari→Latin etc.) | **`sa-IN` is NOT supported** — neither in the real API (confirmed by a live call this session: error `Input should be 'auto', 'en-IN', 'hi-IN', ...`), nor in the official documentation (`docs.sarvam.ai`: "Transliteration API currently supports: English, Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu" — no Sanskrit). Workaround: `hi-IN` as a shared Devanagari script, with the understanding that this is not a Sanskrit model |
| `sarvam_tools_identify_language` | Detects language+script of text (BCP-47 code + script name) | Useful as preprocessing before TTS/translate |

#### Speech (STT/TTS/dubbing)

| Tool | What it does | Key limitations |
|---|---|---|
| `sarvam_tools_stt_transcribe` | Speech recognition, model `saaras:v3`, modes `transcribe`/`translate`/`verbatim`/`translit`/`codemix` | `sa-IN` is in the tool's language enum, **but external sources (search on 2026-08-18) do not confirm Sanskrit in Saaras v3's official list** — a contradiction between the enum and the documentation, not checked with a live call this session |
| `sarvam_tools_stt_batch_submit`/`_status` | Batch transcription of long files (>30s), diarization, timestamps | The full pipeline (job→upload→poll) is automated in one call |
| `sarvam_tools_stt_translate` | **DEPRECATED** — use `stt_transcribe` with `mode='translate'` | — |
| `sarvam_tools_tts_speak`/`_stream` | Speech synthesis, model `bulbul:v3`, 25+ voices, 11 languages | `sa-IN` is **absent** from `target_language_code` (only `en-IN, hi-IN, bn-IN, ta-IN, te-IN, gu-IN, kn-IN, ml-IN, mr-IN, pa-IN, od-IN`) — both in the tool's enum and per external sources; up to ~500 characters per call |
| `sarvam_tools_dub` | Audio dubbing: STT→translate→TTS in one call | Output languages are limited to the same 11-language list as TTS |
| `sarvam_tools_voice` | End-to-end voice agent: transcribes→LLM answer→synthesizes | Combines the limitations of STT+LLM+TTS |

#### Pronunciation

| Tool | What it does | Key limitations |
|---|---|---|
| `sarvam_tools_pronunciation_create/get/list/delete` | "Word→pronunciation" dictionaries to control TTS | Max 100 words/dictionary, 10 dictionaries/user |

#### Documents / images

| Tool | What it does | Key limitations |
|---|---|---|
| `sarvam_tools_vision_extract` | Extracts text/structure from a document or image (Document Intelligence), preserves tables, 23 languages | Up to 10 pages/document, the full async pipeline is automated |
| `sarvam_tools_vision_job_status` | Polls job status for `vision_extract` | — |

#### Utility

| Tool | What it does |
|---|---|
| `sarvam_tools_set_api_key` | Set/update the API key |
| `sarvam_tools_upgrade` | Check/update the MCP server version |

#### `sarvam_code_*` (separate group — coding help, not runtime calls)

`sarvam_code_api_reference`, `sarvam_code_languages`, `sarvam_code_pricing`,
`sarvam_code_recommend_model`, `sarvam_code_snippet`, `sarvam_code_speakers`,
`sarvam_code_validate_request` — reference tools for writing your own
code against the Sarvam API (documentation, examples, model selection,
request validation before sending), **they do not call the Sarvam API
themselves**. Not investigated in detail in this task — a separate
opportunity, should direct HTTP calls outside MCP ever be needed.

### Sanskrit (`sa-IN`) — support matrix summary

| Tool | `sa-IN` in schema enum | Confirmed externally (docs/forums) | Verified with a live call |
|---|---|---|---|
| `translate` | ✅ | ✅ (Sarvam-Translate claims 22 languages, Sanskrit among them) | no |
| `transliterate` | ✅ (in the schema!) | ❌ (officially not in the list of 11 supported languages) | ❌ **confirmed by an API error** this session |
| `stt_transcribe`/`stt_batch_submit` | ✅ | ⚠️ contradictory (not found in any external list) | **no — CHECKED live 2026-08-30: explicitly rejected** |
| `tts_speak`/`tts_stream`/`dub` | ❌ (absent from the enum) | ❌ (11 languages, no Sanskrit) | no |
| `localize` | ✅ | not checked separately | no |

**Conclusion:** the MCP tools' enum schemas are systematically more
optimistic about Sanskrit support than either the real API (confirmed
for `transliterate`) or the external documentation. **Before any new
use of `sa-IN` in this repository — a trial call first, not trust in
the enum list.**

### Sanskrit STT — live admission probe (2026-08-30, PANINI-SARVAM-SANSKRIT-STT-LIVE-VERIFY)

Two-stage evidence, deliberately NOT collapsed into one claim:

- **Stage A — API admission probe: sa-IN explicitly REJECTED.**
  A minimal valid 8 kHz PCM tone WAV (`/tmp/opencode/admission_probe_tone.wav`)
  was sent to `sarvam_tools_stt_transcribe` with `language_code=sa-IN`.
  The real API returned `invalid_request_error`:
  `"Language 'sa-IN' is not supported by saarika:v2.5 model."`
  (request_id `20260830_a9a8f532-f336-42a9-96d4-fdb7ddacd1ae`).
  So **admission = NO**: `sa-IN` is accepted in the tool's schema enum,
  but the live API rejects it outright — same class of discrepancy
  already confirmed for `transliterate`. No transcription was produced.
  Note: through the MCP wrapper the audio reaches the `saarika:v2.5`
  engine (the capability reference below cites `saaras:v3`); the
  rejection is the authoritative API answer regardless of engine label.
  - `sa-IN parameter accepted: NO`
  - `Sanskrit transcription verified: NOT YET`

- **Stage B — semantic STT verification: BLOCKED at the API level.**
  A tone (or silence) proves only API admission of the language tag,
  never that real Sanskrit speech is recognized and transcribed
  correctly. Properly it requires a real, license-clean Sanskrit speech
  sample (own recording preferred) through the same call path. But since
  Stage A established that the API **rejects `sa-IN` outright**, Stage B
  cannot proceed through any `sa-IN` call — the endpoint refuses the
  language tag before touching the audio. A `hi-IN` call would run Hindi
  STT and prove nothing about Sanskrit (hi-IN verifies the pipeline, not
  Sanskrit support). So: Sanskrit transcription remains UNVERIFIED and
  **blocked on there being no Sanskrit STT code path at all**, not on a
  missing sample.

- **TTS synthesis limitation, noted (not repaired here):** the TTS wrapper
  in this session could not synthesize a sample because `bulbul:v2` is
  deprecated (use `bulbul:v3`) and `bulbul:v3` rejects the pitch/loudness
  params the wrapper always sends. Repairing the wrapper is a separate
  task, out of scope for this verification — a real Sanskrit recording is
  the correct input for Stage B anyway.

Status: `sa-IN` STT admission CONFIRMED REJECTED; Sanskrit transcription
UNVERIFIED. Do not use `sa-IN` for STT until Stage B clears on real speech.

### Sources

- Live schemas of the 24 `mcp__sarvam-ai__sarvam_tools_*` tools,
  loaded via `ToolSearch` on 2026-08-18.
- A live call to `sarvam_tools_transliterate` with `sa-IN` — API error,
  logged this session.
- [Sarvam AI Chat Completion API docs](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview) — reasoning_content/max_tokens.
- [Transliteration API docs](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-processing/transliteration) — official list of 11 languages, no Sanskrit.
- [explainx.ai — Sarvam AI Capabilities guide (2026)](https://explainx.ai/blog/sarvam-ai-capabilities-api-models-guide-2026) — summary overview of models/languages.
- `docs/sarvam-integration-guide.md` (`shiva-sutras`) — usage
  methodology and the verified workaround for the reasoning bug.
- [`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md) — a concrete example of unreliability for our domain.

## Українська

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

### Два канали доступу (нагадування)

- **MCP tools** (`mcp__sarvam-ai__sarvam_tools_*`, `sarvam_code_*`) —
  для Claude Code сесій із налаштованим MCP-сервером `sarvam-ai`.
- **HTTP proxy** (`C:/GitHub/sarvam-proxy/server.py`,
  OpenAI-сумісний, `POST /v1/chat/completions`) — для звичайних
  скриптів поза Claude Code.
- Не писати третій wrapper — обидва канали вже покривають усі відомі
  випадки.

### Повний реєстр `sarvam_tools_*` (24 інструменти)

#### Текст / LLM

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_llm_complete` | Chat completion, модель `sarvam-105b` (105B MoE, reasoning) | **Баг**: reasoning з'їдає `max_tokens` (типово 2048), лишаючи порожній `content` при `finish_reason: "length"`. Офіційно підтверджено `docs.sarvam.ai`: не задавати `max_tokens` для коротких відповідей, або `reasoning_effort=null` (ненадійно — у нас спрацювало раз, потім ні) |
| `sarvam_tools_recall` | RAG-подібне питання-відповідь по файлах (аудіо транскрибується, текст читається напряму, до 24000 символів) | до 20 файлів (`max_files`), директорії обходяться рекурсивно |
| `sarvam_tools_text_analytics` | Типізовані запитання до тексту (`boolean`/`enum`/`short answer`/`long answer`/`number`) — структурована екстракція без ручного промпту | — |

#### Переклад / локалізація

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_translate` | Переклад EN↔22 індійські мови, 2 моделі: `mayura:v1` (11 мов, стилі formal/colloquial/code-mixed) чи `sarvam-translate:v1` (22 мови, лише formal) | **`sa-IN` (санскрит) є в enum `source`/`target`** для перекладу |
| `sarvam_tools_localize` | Масовий переклад JSON/`key=value` файлів локалізації, вкладені структури, пише сусідній файл із суфіксом мови | до 500 рядків (`max_strings`) за виклик |

#### Транслітерація / ідентифікація

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_transliterate` | Конвертація писемності без перекладу (Devanagari→Latin тощо) | **`sa-IN` НЕ підтримується** — ні в реальному API (перевірено живим викликом цієї сесії: помилка `Input should be 'auto', 'en-IN', 'hi-IN', ...`), ні в офіційній документації (`docs.sarvam.ai`: "Transliteration API currently supports: English, Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu" — санскриту немає). Обхідний шлях: `hi-IN` як спільна деванагарі-писемність, з усвідомленням, що це не санскритська модель |
| `sarvam_tools_identify_language` | Визначення мови+писемності тексту (BCP-47 код + назва писемності) | Корисно як препроцесинг перед TTS/translate |

#### Мовлення (STT/TTS/дублювання)

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_stt_transcribe` | Розпізнавання мовлення, модель `saaras:v3`, режими `transcribe`/`translate`/`verbatim`/`translit`/`codemix` | `sa-IN` є в enum мов інструмента, **але зовнішні джерела (пошук 2026-08-18) не підтверджують санскрит у офіційному переліку Saaras v3** — суперечність між enum і документацією, не перевірено живим викликом у цій сесії |
| `sarvam_tools_stt_batch_submit`/`_status` | Пакетна транскрипція довгих файлів (>30с), діаризація, таймстемпи | Повний конвеєр (job→upload→poll) автоматизований в одному виклику |
| `sarvam_tools_stt_translate` | **DEPRECATED** — використовувати `stt_transcribe` з `mode='translate'` | — |
| `sarvam_tools_tts_speak`/`_stream` | Синтез мовлення, модель `bulbul:v3`, 25+ голосів, 11 мов | `sa-IN` **немає** серед `target_language_code` (лише `en-IN, hi-IN, bn-IN, ta-IN, te-IN, gu-IN, kn-IN, ml-IN, mr-IN, pa-IN, od-IN`) — і в enum інструмента, і за зовнішніми джерелами; до ~500 символів за виклик |
| `sarvam_tools_dub` | Дублювання аудіо: STT→переклад→TTS одним викликом | Вихідні мови обмежені тим самим переліком 11, що й TTS |
| `sarvam_tools_voice` | Голосовий агент "з кінця в кінець": транскрибує→LLM-відповідь→синтезує | Комбінує обмеження STT+LLM+TTS |

#### Вимова

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_pronunciation_create/get/list/delete` | Словники вимови "слово→вимова" для контролю TTS | Максимум 100 слів/словник, 10 словників/користувач |

#### Документи / зображення

| Інструмент | Що робить | Ключові обмеження |
|---|---|---|
| `sarvam_tools_vision_extract` | Витяг тексту/структури з документа чи зображення (Document Intelligence), збереження таблиць, 23 мови | До 10 сторінок/документ, повний async-конвеєр автоматизований |
| `sarvam_tools_vision_job_status` | Опитування статусу job для `vision_extract` | — |

#### Службові

| Інструмент | Що робить |
|---|---|
| `sarvam_tools_set_api_key` | Встановити/оновити API-ключ |
| `sarvam_tools_upgrade` | Перевірити/оновити версію MCP-сервера |

#### `sarvam_code_*` (окрема група — допомога з написанням коду, не runtime-виклики)

`sarvam_code_api_reference`, `sarvam_code_languages`, `sarvam_code_pricing`,
`sarvam_code_recommend_model`, `sarvam_code_snippet`, `sarvam_code_speakers`,
`sarvam_code_validate_request` — довідкові інструменти для написання
власного коду проти Sarvam API (документація, приклади, підбір
моделі, валідація запиту перед відправкою), **не викликають Sarvam
API самі по собі**. Не досліджені детально в цій задачі — окрема
нагода, якщо колись знадобиться писати прямі HTTP-виклики поза MCP.

### Санскрит (`sa-IN`) — зведена матриця підтримки

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

### Джерела

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

## Deutsch

Status: v0.1, zusammengestellt am 2026-08-18. Ergänzt
`docs/sarvam-integration-guide.md` (`shiva-sutras`) — jenes Dokument
erklärt *wie* man Sarvam nutzt (zwei Kanäle, der Reasoning-Token-Fehler,
Methodik der unabhängigen Prüfung); dieses Dokument beschreibt *was
genau* über diese Kanäle verfügbar ist, zusammengestellt aus (a) den
Live-Schemas der 24 MCP-Werkzeuge (`mcp__sarvam-ai__sarvam_tools_*`),
(b) Sarvams offizieller Dokumentation (`docs.sarvam.ai`), (c) Live-Tests
in dieser Sitzung.

**Wichtig:** Sarvam ist ein unabhängiger Hypothesengenerator, keine
Quelle der Wahrheit (`sarvam-integration-guide.md`). Diese Referenz
beschreibt *was aufgerufen werden kann*, sie bestätigt nicht *die
Korrektheit der Antworten* für unsere Domäne (Sanskrit/Pāṇini) — siehe
[`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md)
für ein konkretes, bestätigtes Fehlerbeispiel bei `bhAz`.

### Zwei Zugangskanäle (Erinnerung)

- **MCP-Werkzeuge** (`mcp__sarvam-ai__sarvam_tools_*`, `sarvam_code_*`)
  — für Claude-Code-Sitzungen mit konfiguriertem `sarvam-ai`-MCP-Server.
- **HTTP-Proxy** (`C:/GitHub/sarvam-proxy/server.py`, OpenAI-kompatibel,
  `POST /v1/chat/completions`) — für reguläre Skripte außerhalb von
  Claude Code.
- Keinen dritten Wrapper schreiben — beide Kanäle decken bereits alle
  bekannten Fälle ab.

### Vollständiges Register von `sarvam_tools_*` (24 Werkzeuge)

#### Text / LLM

| Werkzeug | Was es tut | Wichtige Einschränkungen |
|---|---|---|
| `sarvam_tools_llm_complete` | Chat-Completion, Modell `sarvam-105b` (105B MoE, Reasoning) | **Fehler**: Reasoning verbraucht `max_tokens` (Standard 2048) und hinterlässt leeren `content` bei `finish_reason: "length"`. Offiziell von `docs.sarvam.ai` bestätigt: `max_tokens` bei kurzen Antworten nicht setzen, oder `reasoning_effort=null` (unzuverlässig — funktionierte bei uns einmal, dann nicht mehr) |
| `sarvam_tools_recall` | RAG-artige Frage-Antwort über Dateien (Audio wird transkribiert, Text direkt gelesen, bis zu 24000 Zeichen) | bis zu 20 Dateien (`max_files`), Verzeichnisse werden rekursiv durchlaufen |
| `sarvam_tools_text_analytics` | Typisierte Fragen zu Text (`boolean`/`enum`/`short answer`/`long answer`/`number`) — strukturierte Extraktion ohne manuellen Prompt | — |

#### Übersetzung / Lokalisierung

| Werkzeug | Was es tut | Wichtige Einschränkungen |
|---|---|---|
| `sarvam_tools_translate` | Übersetzung EN↔22 indische Sprachen, 2 Modelle: `mayura:v1` (11 Sprachen, Stile formal/colloquial/code-mixed) oder `sarvam-translate:v1` (22 Sprachen, nur formal) | **`sa-IN` (Sanskrit) ist im `source`/`target`-Enum** für die Übersetzung enthalten |
| `sarvam_tools_localize` | Massenübersetzung von JSON-/`key=value`-Lokalisierungsdateien, verschachtelte Strukturen, schreibt eine benachbarte Datei mit Sprachsuffix | bis zu 500 Zeilen (`max_strings`) pro Aufruf |

#### Transliteration / Identifikation

| Werkzeug | Was es tut | Wichtige Einschränkungen |
|---|---|---|
| `sarvam_tools_transliterate` | Schriftkonvertierung ohne Übersetzung (Devanagari→Latein usw.) | **`sa-IN` wird NICHT unterstützt** — weder in der echten API (durch einen Live-Aufruf dieser Sitzung bestätigt: Fehler `Input should be 'auto', 'en-IN', 'hi-IN', ...`), noch in der offiziellen Dokumentation (`docs.sarvam.ai`: "Transliteration API currently supports: English, Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu" — kein Sanskrit). Workaround: `hi-IN` als gemeinsame Devanagari-Schrift, im Bewusstsein, dass dies kein Sanskrit-Modell ist |
| `sarvam_tools_identify_language` | Erkennt Sprache+Schrift eines Textes (BCP-47-Code + Schriftname) | Nützlich als Vorverarbeitung vor TTS/Translate |

#### Sprache (STT/TTS/Dubbing)

| Werkzeug | Was es tut | Wichtige Einschränkungen |
|---|---|---|
| `sarvam_tools_stt_transcribe` | Spracherkennung, Modell `saaras:v3`, Modi `transcribe`/`translate`/`verbatim`/`translit`/`codemix` | `sa-IN` steht im Sprach-Enum des Werkzeugs, **aber externe Quellen (Recherche am 2026-08-18) bestätigen Sanskrit nicht in Saaras v3s offizieller Liste** — ein Widerspruch zwischen Enum und Dokumentation, in dieser Sitzung nicht per Live-Aufruf geprüft |
| `sarvam_tools_stt_batch_submit`/`_status` | Batch-Transkription langer Dateien (>30s), Diarisierung, Zeitstempel | Die gesamte Pipeline (Job→Upload→Poll) ist in einem Aufruf automatisiert |
| `sarvam_tools_stt_translate` | **VERALTET** — `stt_transcribe` mit `mode='translate'` verwenden | — |
| `sarvam_tools_tts_speak`/`_stream` | Sprachsynthese, Modell `bulbul:v3`, 25+ Stimmen, 11 Sprachen | `sa-IN` **fehlt** in `target_language_code` (nur `en-IN, hi-IN, bn-IN, ta-IN, te-IN, gu-IN, kn-IN, ml-IN, mr-IN, pa-IN, od-IN`) — sowohl im Enum des Werkzeugs als auch laut externen Quellen; bis zu ~500 Zeichen pro Aufruf |
| `sarvam_tools_dub` | Audio-Dubbing: STT→Übersetzung→TTS in einem Aufruf | Ausgangssprachen sind auf dieselbe 11-Sprachen-Liste wie TTS beschränkt |
| `sarvam_tools_voice` | Ende-zu-Ende-Sprachagent: transkribiert→LLM-Antwort→synthetisiert | Kombiniert die Einschränkungen von STT+LLM+TTS |

#### Aussprache

| Werkzeug | Was es tut | Wichtige Einschränkungen |
|---|---|---|
| `sarvam_tools_pronunciation_create/get/list/delete` | "Wort→Aussprache"-Wörterbücher zur TTS-Steuerung | Max. 100 Wörter/Wörterbuch, 10 Wörterbücher/Nutzer |

#### Dokumente / Bilder

| Werkzeug | Was es tut | Wichtige Einschränkungen |
|---|---|---|
| `sarvam_tools_vision_extract` | Extrahiert Text/Struktur aus einem Dokument oder Bild (Document Intelligence), erhält Tabellen, 23 Sprachen | Bis zu 10 Seiten/Dokument, die gesamte asynchrone Pipeline ist automatisiert |
| `sarvam_tools_vision_job_status` | Fragt den Job-Status für `vision_extract` ab | — |

#### Dienstprogramme

| Werkzeug | Was es tut |
|---|---|
| `sarvam_tools_set_api_key` | API-Schlüssel setzen/aktualisieren |
| `sarvam_tools_upgrade` | MCP-Server-Version prüfen/aktualisieren |

#### `sarvam_code_*` (separate Gruppe — Coding-Hilfe, keine Laufzeitaufrufe)

`sarvam_code_api_reference`, `sarvam_code_languages`, `sarvam_code_pricing`,
`sarvam_code_recommend_model`, `sarvam_code_snippet`, `sarvam_code_speakers`,
`sarvam_code_validate_request` — Referenzwerkzeuge zum Schreiben
eigenen Codes gegen die Sarvam-API (Dokumentation, Beispiele,
Modellauswahl, Anfragevalidierung vor dem Senden), **sie rufen die
Sarvam-API selbst nicht auf**. In dieser Aufgabe nicht im Detail
untersucht — eine separate Gelegenheit, falls jemals direkte
HTTP-Aufrufe außerhalb von MCP nötig werden.

### Sanskrit (`sa-IN`) — Zusammenfassung der Unterstützungsmatrix

| Werkzeug | `sa-IN` im Schema-Enum | Extern bestätigt (Docs/Foren) | Per Live-Aufruf geprüft |
|---|---|---|---|
| `translate` | ✅ | ✅ (Sarvam-Translate beansprucht 22 Sprachen, Sanskrit darunter) | nein |
| `transliterate` | ✅ (im Schema!) | ❌ (offiziell nicht in der Liste der 11 unterstützten Sprachen) | ❌ **durch einen API-Fehler bestätigt** in dieser Sitzung |
| `stt_transcribe`/`stt_batch_submit` | ✅ | ⚠️ widersprüchlich (in keiner externen Liste gefunden) | nein |
| `tts_speak`/`tts_stream`/`dub` | ❌ (fehlt im Enum) | ❌ (11 Sprachen, kein Sanskrit) | nein |
| `localize` | ✅ | separat nicht geprüft | nein |

**Fazit:** Die Enum-Schemas der MCP-Werkzeuge sind systematisch
optimistischer bezüglich Sanskrit-Unterstützung als sowohl die echte
API (bestätigt für `transliterate`) als auch die externe Dokumentation.
**Vor jeder neuen Verwendung von `sa-IN` in diesem Repository — zuerst
ein Testaufruf, kein Vertrauen in die Enum-Liste.**

### Quellen

- Live-Schemas der 24 `mcp__sarvam-ai__sarvam_tools_*`-Werkzeuge,
  geladen über `ToolSearch` am 2026-08-18.
- Ein Live-Aufruf von `sarvam_tools_transliterate` mit `sa-IN` —
  API-Fehler, protokolliert in dieser Sitzung.
- [Sarvam AI Chat Completion API docs](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview) — reasoning_content/max_tokens.
- [Transliteration API docs](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-processing/transliteration) — offizielle Liste von 11 Sprachen, kein Sanskrit.
- [explainx.ai — Sarvam AI Capabilities guide (2026)](https://explainx.ai/blog/sarvam-ai-capabilities-api-models-guide-2026) — zusammenfassender Überblick über Modelle/Sprachen.
- `docs/sarvam-integration-guide.md` (`shiva-sutras`) — Nutzungsmethodik
  und verifizierter Workaround für den Reasoning-Fehler.
- [`sarvam-independent-check-slp1.md`](sarvam-independent-check-slp1.md) — ein konkretes Beispiel für Unzuverlässigkeit in unserer Domäne.
