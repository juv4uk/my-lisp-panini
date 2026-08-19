# Sarvam independent check: śa/ṣa reliability

## English

Status: one-off finding, logged 2026-08-18.

### What was done

Connected `mcp__sarvam-ai__sarvam_tools_transliterate` (guide:
`docs/sarvam-integration-guide.md`, `shiva-sutras`) and used it as an
**independent check**, not as a source of truth — exactly as the guide
recommends ("don't ask it to confirm a conclusion, ask it the same cold
question").

### Test

Transliteration of `भाष्` (bhāṣ, "to speak" — the same root that already
went through 2 rounds of a wrong fix and 1 round of the final correction
in this repository, see
[`../sastra/terminology.md`](../sastra/terminology.md#знайдені-й-виправлені-розбіжності)),
Devanāgarī→Latin, `hi-IN`→`en-IN` (Sanskrit, `sa-IN`, is not accepted by
the API as `source_language_code` despite the tool schema claiming it
is — a separate, minor API bug).

**Sarvam's result:** `"bhāś"` — palatal `ś`.
**Our established fact** (Vidyut's `sounds.rs` source code + an
independent cross-check by `my-lisp-1` against Wikipedia SLP1): `bhāṣ`
has a **retroflex `ṣ`**, not `ś`.

### Conclusion

Sarvam got wrong exactly the sound pair (`ś`/`ṣ`) that this repository
itself confused three times in a row before establishing the correct
convention from Vidyut's primary source code. This is not a reason to
doubt the already-established fact (`ṣ` in `bhAz` is confirmed by two
independent authoritative sources) — it confirms Sarvam's status as an
"independent hypothesis generator, not a source of truth"
(`sarvam-integration-guide.md`): even a model trained on Indian
languages regularly confuses exactly this sound pair, which is easy to
mix up without direct access to a primary source.

**Practical takeaway for future work:** Sarvam is not fit as a
standalone source for verifying `ś`/`ṣ`-sensitive SLP1 spellings in
this repository — any future attempt to use it for this must be
cross-checked against real code/data (Vidyut, Dhātupāṭha), the same way
all other work this session was.

### Sources

- `mcp__sarvam-ai__sarvam_tools_transliterate`, call on 2026-08-18,
  latency 656.5ms, request_id
  `20260818_edb941de-c123-498f-a2e1-3d7a3b79709b`.
- `docs/sarvam-integration-guide.md` (`shiva-sutras`) — usage
  methodology.

## Українська

Статус: одноразова знахідка, залогована 2026-08-18.

### Що зроблено

Підключено `mcp__sarvam-ai__sarvam_tools_transliterate` (гайд:
`docs/sarvam-integration-guide.md`, `shiva-sutras`) і використано як
**незалежну перевірку**, не як джерело істини — саме так, як
рекомендує гайд ("не питай підтвердити висновок, постав те саме
холодне питання").

### Тест

Транслітерація `भाष्` (bhāṣ, "говорити" — той самий корінь, що вже
пройшов 2 раунди помилкового виправлення й 1 раунд остаточного
виправлення в цьому репозиторії, див.
[`../sastra/terminology.md`](../sastra/terminology.md#знайдені-й-виправлені-розбіжності))
на Devanāgarī→Latin, `hi-IN`→`en-IN` (санскрит, `sa-IN`, API не
підтримує як `source_language_code`, попри те що інструмент-схема
його заявляє — окремий дрібний баг API).

**Результат Sarvam:** `"bhāś"` — палатальне `ś`.
**Наш встановлений факт** (код Vidyut `sounds.rs` + незалежна
крос-звірка `my-lisp-1` проти Wikipedia SLP1): `bhāṣ` має
**ретрофлексне `ṣ`**, не `ś`.

### Висновок

Sarvam помилився саме на тій парі звуків (`ś`/`ṣ`), яку цей
репозиторій сам плутав тричі поспіль, перш ніж встановити правильну
конвенцію через первинний код Vidyut. Це не привід сумніватись у вже
встановленому факті (`ṣ` у `bhAz` підтверджений двома незалежними
авторитетними джерелами) — це підтвердження статусу Sarvam як
"незалежний гіпотезогенератор, не source of truth" (`sarvam-integration-guide.md`):
навіть модель, натренована на індійських мовах, регулярно плутає цю
саму пару звуків, яку легко переплутати без прямого доступу до
першоджерела.

**Практичний висновок для подальшої роботи:** Sarvam непридатний як
самостійне джерело для верифікації `ś`/`ṣ`-чутливих SLP1-написань у
цьому репозиторії — будь-яка майбутня спроба використати його для
цього має супроводжуватись звіркою проти реального коду/даних
(Vidyut, Dhātupāṭha), як і вся інша робота цієї сесії.

### Джерела

- `mcp__sarvam-ai__sarvam_tools_transliterate`, виклик 2026-08-18,
  latency 656.5ms, request_id `20260818_edb941de-c123-498f-a2e1-3d7a3b79709b`.
- `docs/sarvam-integration-guide.md` (`shiva-sutras`) — методологія
  використання.

## Deutsch

Status: einmaliger Befund, protokolliert am 2026-08-18.

### Was getan wurde

`mcp__sarvam-ai__sarvam_tools_transliterate` wurde angebunden (Leitfaden:
`docs/sarvam-integration-guide.md`, `shiva-sutras`) und als
**unabhängige Prüfung** verwendet, nicht als Quelle der Wahrheit — genau
wie es der Leitfaden empfiehlt ("keine Bestätigung einer Schlussfolgerung
erfragen, sondern dieselbe unvoreingenommene Frage stellen").

### Test

Transliteration von `भाष्` (bhāṣ, "sprechen" — dieselbe Wurzel, die in
diesem Repository bereits zwei Runden einer falschen Korrektur und eine
Runde der endgültigen Korrektur durchlief, siehe
[`../sastra/terminology.md`](../sastra/terminology.md#знайдені-й-виправлені-розбіжності)),
Devanāgarī→Latein, `hi-IN`→`en-IN` (Sanskrit, `sa-IN`, wird von der API
nicht als `source_language_code` akzeptiert, obwohl das Tool-Schema dies
behauptet — ein separater, kleiner API-Fehler).

**Ergebnis von Sarvam:** `"bhāś"` — palatales `ś`.
**Unsere festgestellte Tatsache** (Quellcode `sounds.rs` von Vidyut +
unabhängiger Abgleich durch `my-lisp-1` gegen Wikipedia-SLP1): `bhāṣ`
hat ein **retroflexes `ṣ`**, nicht `ś`.

### Fazit

Sarvam irrte sich genau bei dem Lautpaar (`ś`/`ṣ`), das dieses
Repository selbst dreimal hintereinander verwechselte, bevor die
korrekte Konvention anhand des Primärquellcodes von Vidyut festgelegt
wurde. Das ist kein Grund, an der bereits festgestellten Tatsache zu
zweifeln (`ṣ` in `bhAz` ist durch zwei unabhängige maßgebliche Quellen
bestätigt) — es bestätigt vielmehr Sarvams Status als "unabhängigen
Hypothesengenerator, keine Quelle der Wahrheit"
(`sarvam-integration-guide.md`): Selbst ein auf indische Sprachen
trainiertes Modell verwechselt regelmäßig genau dieses Lautpaar, das
ohne direkten Zugriff auf eine Primärquelle leicht zu verwechseln ist.

**Praktische Schlussfolgerung für künftige Arbeit:** Sarvam eignet sich
nicht als alleinstehende Quelle zur Verifikation von `ś`/`ṣ`-sensiblen
SLP1-Schreibweisen in diesem Repository — jeder künftige Versuch, es
dafür zu nutzen, muss gegen echten Code/echte Daten (Vidyut,
Dhātupāṭha) abgeglichen werden, wie die gesamte übrige Arbeit dieser
Sitzung.

### Quellen

- `mcp__sarvam-ai__sarvam_tools_transliterate`, Aufruf am 2026-08-18,
  Latenz 656,5ms, request_id
  `20260818_edb941de-c123-498f-a2e1-3d7a3b79709b`.
- `docs/sarvam-integration-guide.md` (`shiva-sutras`) — Verwendungsmethodik.
