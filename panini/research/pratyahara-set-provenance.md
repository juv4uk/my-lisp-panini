# Provenance sound sets для `pratyAhAra`

## Висновок

У Foundation v0.1 можна документувати механізм `pratyAhAra` і приклади на
кшталт `ac`, але не можна вважати наявні pre-generated machine sets
authoritative. Перш ніж будь-який set стане machine input, потрібен
versioned Śiva Sūtra source і окрема перевірка алгоритму розгортання.

## [PANINI]

`pratyAhAra` пов'язаний із послідовністю Śiva/Māheśvara Sūtras і `it`
markers; 1.1.71 `Adir antyena sahetA` є центральною прямою citation для
механізму позначення. У локальному citation provenance registry 1.1.71 має
status `corpus-checked`, але локальний `index.yaml` загалом не є критичним,
відтворювано імпортованим виданням.

Отже, у trace слід зберігати не лише результат set, а й:

```yaml
pratyahara: ac
start_sound: a
end_marker: c
siva_source_id: "..."
source_revision: "..."
expansion_algorithm_revision: "..."
```

## Provenance gate

Машинний sound-set import допускається лише з manifest:

```yaml
source_id: siva-sutras-<edition>-<revision>
work: maheSvara-sUtra
edition_or_corpus: "..."
access_url: "..."
license_or_rights: "..."
retrieved_at: "YYYY-MM-DD"
input_sha256: "..."
transliteration_source: "original|documented-conversion"
conversion_revision: "..."
independent_check: "..."
```

Без `input_sha256` і conversion record твердження «повний список звірено»
є корисною робочою нотаткою, але не відтворюваним джерелом наборів.

## Machine audit: не використовувати як джерело

`panini/machine/siva-sutras.my` має розбіжності з SLP1-списком, поданим у
`foundation/pratyahara.md`:

| Рядок | Foundation SLP1 | Machine запис | Ризик |
| --- | --- | --- | --- |
| 9 | `G Q D [z]` | `G Q D S` | marker `S` не збігається з canonical `z`. |
| 10 | `j b g q d [S]` | `j b g q d S` | рядок збігається; попередня розбіжність була помилкою Foundation. |
| 11 | `K P C W T c w t [v]` | `K P C W T c w t V` | marker `V` не збігається з `v`. |

Це audit finding, не дозвіл переписати machine model без окремої
source-level звірки. Воно показує, чому compiled set не може бути доказом
тексту або SLP1 нормалізації.

## [INTERPRETATION]

Розгортання `ac` у набір голосних — корисний пояснювальний приклад. Але
«почати з першого символу й зупинитися на першому відповідному marker» є
вже формалізацією алгоритму. Її треба тестувати на повторюваних звуках та
повторюваних marker-значеннях, а не вважати очевидною через строкове
представлення.

## [MY-LISP HYPOTHESIS]

Bitset, enum, таблиця або FPGA mask можуть бути ефективним compiled form
перевіреного set. Їхні порядок бітів, ширина слова, кешування й час
виконання не випливають із 1.1.71. Усі вони потребують окремої machine spec
після джерельної та algorithmic verification.

## Наступні дії

1. Вибрати один versioned Śiva Sūtra source і додати manifest з hash.
2. Додати незалежні fixtures для `ac`, `hal`, `ik`, `ec`, `yaR` та
   негативні випадки з неоднозначним marker lookup.
3. Лише після 1–2 виправляти або приймати `siva-sutras.my` як похідний
   machine artifact; до того позначати його experimental.
