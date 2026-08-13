# Provenance `prAdi`-gaṇa: рішення для Foundation v0.1

## Результат

`prAdi` не слід вносити до registry як самостійно набраний список 22
«префіксів». Для Foundation v0.1 доступні джерела достатні, щоб встановити
посилання `1.4.58 → prAdi-gaṇa` і робочу політику provenance, але недостатні,
щоб імпортувати повний машинний інвентар без revision-pinned transcription.

## [PANINI]

1.4.58 `prAdayaH` посилається на gaṇa, а 1.4.59
`upasargAH kriyAyoge` надає відповідну saMjYA в заданій умові. Цифрове
видання 1.4.59 пояснює, що йдеться про елементи `prAdi-gaṇa`, але воно не
замінює критичне видання самого gaṇapāṭha.
[Aṣṭādhyāyī 1.4.58](https://ashtadhyayi.com/sutraani/1/4/58),
[Aṣṭādhyāyī 1.4.59](https://ashtadhyayi.com/sutraani/1/4/59)

## Кандидати джерел

| Джерело | Що встановлено | Чого не робимо автоматично |
| --- | --- | --- |
| *The Gaṇapāṭha*, Kurukshetra University, 1967 | Бібліографічний запис описує видання як critical edition, 482 с., Sanskrit/English; має стабільні LCCN/OCLC/OL ідентифікатори. | Не копіюємо текст: у поточному audit немає отриманого, перевіреного цифрового примірника або ліцензії на транскрипцію. |
| Скан `Gaṇapāṭha of Pāṇini`, Asiatic Society of Mumbai | Wikimedia позначає файл public domain у зазначених юрисдикціях і дає посилання на першоджерело скану. | Не робимо OCR-список нормативним: потрібні сторінки, читання й контроль варіантів. |
| Ashtadhyayi.com 1.4.58–59 | Швидка навігація sūtra, anuvṛtti та пояснювальний список. | Не видаємо веб-список за versioned gaṇapāṭha edition. |

Бібліографія критичного видання:
[Open Library: *The Gaṇapāṭha*](https://openlibrary.org/books/OL47982704M/The_Ga%E1%B9%87ap%C4%81%E1%B9%ADha).

Скан для майбутньої колації:
[Wikimedia Commons: Gaṇapāṭha of Pāṇini](https://commons.wikimedia.org/wiki/File%3A%E0%A4%97%E0%A4%A3%E0%A4%AA%E0%A4%BE%E0%A4%A0_of_%E0%A4%AA%E0%A4%BE%E0%A4%A3%E0%A4%BF%E0%A4%A8%E0%A4%BF._%28IA_dli.granth.16409%29.pdf).

## [INTERPRETATION]

Поширений список із 22 елементів корисний для навігації, але має щонайменше
три ризики: змішування написань/варіантів, неявний вибір видання та втрату
різниці між членством у gaṇa і `upasarga`-saMjYA за `kriyAyoga`. Тому число
елементів або їхній порядок не є field у v0.1, доки не вказані edition і
точна локація в ньому.

## Реєстрова політика

Майбутній імпорт дозволений лише з manifest такого виду:

```yaml
source_id: ganapatha-<edition>-<revision>
work: ganapatha
edition: "..."
locator: "page/section/..."
access_url: "..."
license_or_rights: "..."
transcription_method: manual|reviewed-ocr
slp1_normalization: documented
review_status: independently-checked
```

Кожен елемент має містити `source_id`, `locator`, source spelling і окремий
canonical SLP1 після documented normalization. Не можна виводити ID зі
сучасного IAST-переліку без збереження source form.

## [MY-LISP HYPOTHESIS]

My Lisp може колись використати компактний registry `prAdi` для resolution,
але це проектний індекс, не синонім `upasarga` і не правило string-prefix.
До появи manifest і evidence-bound trace заборонено робити на його основі
parser, VM semantics або FPGA encoding.

## Наступна дія

Взяти один обраний, доступний примірник, зафіксувати checksum/revision,
вручну звірити сторінку `prAdi` і лише після незалежної перевірки створити
окремий registry import commit.
