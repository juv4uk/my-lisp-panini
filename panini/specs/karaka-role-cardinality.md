# Kā r a k a role cardinality: межа Foundation та AST

## Статус

Це специфікація межі для `panini-foundation-v0.1`, а не зміна semantic AST.
Вона випливає з [causative stress test](../research/causative-karaka-stress-test.md)
та не встановлює єдиний «правильний» контейнер ролей для My Lisp.

## [PANINI]

Панінійські `kAraka`-saMjYA класифікують релевантні відношення в області
1.4.23, а 1.4.54–55 важливі для `kartf` і `hetu`. Зокрема, 1.4.55 пов'язує
спонукача з `kartf`; він не задає модель з одним глобальним полем `agent`.
[1.4.23](https://ashtadhyayi.com/sutraani/1/4/23),
[1.4.54](https://sanskritdictionary.com/panini/1-4-54),
[1.4.55](https://sanskritdictionary.com/panini/1-4-55).

З цього **не** випливає жодна з наступних програмних властивостей:

- що кожна `kAraka`-saMjYA має cardinality `0..1`;
- що роль може повторюватися без обмежень;
- що всі відношення належать одній плоскій події;
- що `hetu` є сьомим незалежним атомом поруч із шістьма базовими kāraka;
- що всі такі відношення мусять бути graph edges.

## [INTERPRETATION]

Для простого trace з одним `dA` зручно записати по одному учаснику для
`kartf`, `karman`, `sampradAna`. Але causative stress case міняє структуру:
спонукач пов'язаний із already designated `kartf`, а базова дія може мати
власні учасники. Отже, інваріант «один role ID трапляється не більш як раз»
не є нейтральним панінійським висновком; це обмеження конкретного AST.

## [MY-LISP HYPOTHESIS]

### Безпечний контракт першого AST-рівня

`SemanticCall{predicate, roles}` може зберігати **плоский simple-call
profile**, якщо застосовані всі умови:

```text
predicate: зареєстрований dhAtu ID
roles: кожен canonical kAraka ID не повторено
scope: один простий event
evidence: немає causative / nested-event claim
```

Це корисний validator для навчальних і базових прикладів, але не загальний
інваріант моделі Panini.

### Перехід у richer profile

Будь-яка з умов нижче вимагає відмовитися від simple-call profile або
позначити конструкцію `unsupported`:

| Ознака | Чому плоска унікальна мапа недостатня |
| --- | --- |
| `hetu`/causative claim | Потрібен зв'язок спонукача з caused `kartf`. |
| Кілька учасників одного role ID | Потрібна explicit cardinality policy, а не випадкове перетирання ключа. |
| Вкладена дія | Ролі мають належати конкретному event scope. |
| Суперечливі або альтернативні analyses | Потрібно зберігати alternatives/provenance, не обирати довільно. |

### Допустимі проектні моделі

| Модель | Перевага | Яке питання вона мусить вирішити |
| --- | --- | --- |
| `roles: Map<Role, Entity>` | Проста валідація simple calls. | Як відхилити або піднести causative case. |
| `roles: Vec<RoleBinding>` | Дозволяє повтори та provenance binding-а. | Як визначити scope і semantically valid multiplicity. |
| nested `SemanticEvent` | Виражає causation та вкладені дії. | Як зберегти trace/source для кожного event. |
| relation graph | Явно подає зв'язки між учасниками. | Як не підмінити Panini власною онтологією графа. |

Усі чотири — [MY-LISP HYPOTHESIS]. Foundation не обирає одну з них.

## Нормативна межа для реалізації

1. Canonical role IDs лишаються SLP1 (`kartf`, `karman`, …), без `:`.
2. `:kartf` допустимий лише як surface syntax, якщо parser так вирішить.
3. Validator simple-call profile має діагностувати duplicate role, а не
   мовчки зливати або перетирати значення.
4. Causative/nested case не можна «полагодити» перейменуванням `kartf` у
   сучасний `agent` або додаванням неперевіреного role ID.
5. Будь-який richer profile мусить зберігати provenance на рівні binding-а
   або event-а.

## Acceptance checks для наступної фази

- Simple `dA` приклад проходить `Map<Role, Entity>` validation.
- Duplicate canonical role у simple profile повертає явну diagnostic.
- Causative fixture або відхиляється з поясненням `requires nested event`,
  або проходить тільки через новий явно позначений richer profile.
- Жоден тест не називає AST-инваріант «Panini rule» без sūtra/trace proof.
