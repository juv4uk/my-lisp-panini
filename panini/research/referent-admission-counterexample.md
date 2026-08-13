# Referent admission counterexample

Status: `admission-denied`. This is a negative test of the proposed
`entity:<id>` admission rule, using the current causative participant fixture.
It does not claim a full sentence analysis or a theory of reference in Pāṇini.

## English

The strongest available temptation is a causative analysis: an instigator and
a caused participant appear in a structured situation, so a modern event model
might introduce entities immediately. The counterexample shows why that is too
early. Existing term occurrences, their situation-scoped classifications, and
explicit relations already express what the fixture can evidence. Equal lexical
spelling would still not prove coreference.

## Українська

### [PANINI]

1.4.54–55 розрізняють `kartf` і causative `hetu` у релевантному відношенні.
Це дає підставу фіксувати classification claims **для учасника в певній
ситуації**, але не створює в нашому доказовому матеріалі універсальну
онтологію референтів. Самі sūtra не постачають нам стабільний ID на кшталт
`entity:rAma`.

### [INTERPRETATION]

Візьмемо найсильніший доступний test case:

```text
situation: causative-instigation
term:participant-rAma       → kartf, qualifier hetu
term:participant-devadatta  → kartf, qualifier caused-action-participant
```

Тут потрібні:

1. різні term IDs для різних зафіксованих occurrences;
2. situation scope для кожного classification claim;
3. relation/qualifier, що не дає загубити causative залежність;
4. provenance і status, зокрема `unresolved` для неперевіреного caused
   participant.

Усе це вже виражається поточним fixture. Введення `entity:rAma` нічого не
пояснює: воно лише перетворює human-readable SLP1 spelling на недоведене
твердження про тотожність поза trace.

Ще важливіше, два різні occurrences з однаковими `source_form: rAma` не
доводять ані coreference, ані різності референта. Без text location,
discourse scope та окремого source-backed relation обидва висновки мають
статус `unknown`.

### [MY-LISP HYPOTHESIS]

Негативний acceptance test для майбутньої машини:

```yaml
input:
  - { term: term:participant-rAma-1, source_form: rAma }
  - { term: term:participant-rAma-2, source_form: rAma }
attempt: infer-coreference-from-SLP1
result: blocked
reason: lexical-form-equality-is-not-referent-evidence
```

Навіть у causative profile корисний мінімум — `term` + `situation` +
provenance-bound relation. `entity:<id>` допускається лише коли документований
приклад вимагає **позитивного**, вузько названого зв'язку (`corefers-with`,
`denotes`, `participant-in`) між occurrences, який не виражається цими
засобами. Тоді entity/referent relation лишається `machine:` до окремого
review.

## Висновок

Контрприклад не проходить admission: каузативна складність вимагає richer
relation shape, але не referent node. Це захищає My Lisp від неявного
перетворення SLP1-лексеми, gloss або role designation на «сутність світу».

## Deutsch

Der Kausativfall verlangt eine reichere Relationsform, aber keinen
Referent-Knoten. Zwei Term-Vorfälle mit derselben SLP1-Form beweisen weder
Koreferenz noch Verschiedenheit. Die Zulassung von `entity:<id>` bleibt daher
blockiert, bis eine dokumentierte, eng benannte Relation sie erfordert.
