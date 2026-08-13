# Śiva Sūtra source-manifest decision

Status: `PANINI-SIVA-SUTRA-VERSIONED-SOURCE-MANIFEST`. A reproducible project
transcription is now recorded, but no external edition has yet passed the
rights-and-revision gate for machine input.

## English summary

The repository now has a hashed provisional SLP1 transcription and a manifest
that records two textual cross-checks. Their web/PDF rights are unresolved, so
neither source is imported or authorized as a machine-data dependency. The
Ukrainian section is normative.

## Українська

### [PANINI]

Для механізму pratyāhāra послідовність Māheśvara/Śiva Sūtras є фундаментальною
даною. Але «фундаментальна» не означає «можна взяти перший знайдений web text і
покласти у runtime». Джерельний текст, транслітерація в SLP1, спосіб
перетворення та правовий статус — різні твердження, які треба зберігати окремо.

### [INTERPRETATION]

Дві незалежні доступні контрольні публікації погоджуються з критичними рядками
9–11. Вони достатні, щоб виявити розбіжність у локальних Foundation/machine
artifact і сформувати test vectors; вони **не** достатні, щоб автоматично
ліцензувати або заморозити external edition як runtime data. Їхній
license/revision status не встановлено в цьому аудиті.

### [MY-LISP HYPOTHESIS]

Створено два локальні артефакти:

| Артефакт | Роль | Статус |
|---|---|---|
| `registry/siva-sutras/siva-sutras-slp1-provisional-v0.1.yaml` | мала проектна транскрипція 14 рядків у SLP1 | `provisional-independent-transcription` |
| `registry/siva-sutras/siva-sutras-slp1-provisional-v0.1.manifest.yaml` | hash, cross-checks, conversion і admission gate | machine input заборонено |

SHA-256 транскрипції:

```text
bb0e59aad88ac8a73b27008ab2eceb55cd45a4d8f1f8f6029cf37c93bb02d304
```

Це дає відтворюваний project artifact для tests, але не скасовує правило:
machine generator не має читати його як authoritative source, доки не буде
обрано один external artifact із дозволеними правами, immutable revision/hash
та окремою перевіркою всіх 14 рядків.

#### Наступний gate

1. Знайти edition/corpus із чітким permitted-reuse license.
2. Зафіксувати exact source artifact і його hash/revision.
3. Документувати conversion до SLP1 як окремий reproducible step.
4. Порівняти external artifact, provisional transcription та
   `pratyahara-exhaustive-v0.1.yaml`.
5. Лише потім брати `PANINI-MACHINE-SIVA-SUTRA-ALIGNMENT-GATE`.

Поки цей gate не пройдено, локальні machine sets — experimental implementation
material, не `[PANINI]` source evidence.

## Deutsch

Es gibt nun eine gehashte vorläufige SLP1-Transkription samt Manifest und zwei
Textabgleichen. Die Rechte und Revisionen der externen Web/PDF-Quellen sind
jedoch ungeklärt; daher ist keine davon als Machine-Input zugelassen. Erst ein
lizenzierter, fixierter externer Artefakt mit reproduzierbarer SLP1-Konversion
darf diesen Status ändern. Die ukrainische Fassung ist normativ.
