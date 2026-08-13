# Adhikāra scope boundaries: text-level evidence

## [PANINI]

An `adhikAra` is a governing sūtra whose content is carried into following
sūtras. The digital Aṣṭādhyāyī explicitly labels 3.2.84 `bhUte` as an
adhikāra and describes its scope through 3.2.123; it also labels 4.1.3
`striyAm` as an adhikāra through 4.1.81. These are concrete scope claims, not
a general rule that every heading has the same extent.

Textual evidence also shows termination: the commentary on 7.3.36 says that
all carried material except `aNgasy` 6.4.1 ceases there; the commentary on
7.1.81 says `nityam` terminates the carry-over of `vA` from 7.1.79. Therefore
scope needs positive provenance and a documented endpoint, not merely a static
edge to every later rule.

Sources: [3.2.84](https://ashtadhyayi.com/sutraani/3/2/84),
[4.1.3](https://ashtadhyayi.com/sutraani/4/1/3),
[7.3.36](https://ashtadhyayi.com/sutraani/7/3/36), and
[7.1.81](https://ashtadhyayi.com/sutraani/lsk365).

## [INTERPRETATION]

The source pages incorporate traditional commentary, so their stated endpoints
are implementation-useful readings rather than a replacement for all primary
commentarial work. The four examples establish two kinds of evidence a
registry must distinguish: an explicitly reported span, and an explicit
termination or restriction of a carried word.

## [MY-LISP HYPOTHESIS]

A machine representation may use scoped bindings, but a static DAG is
insufficient if it hides why a binding ends. Each inherited item should retain:

- `source_sutra`;
- `carried_item`;
- `scope_evidence` (`stated-span`, `termination`, or `unverified`);
- `end_sutra` when evidence states one; and
- a provenance link to the commentary/source.

No generic runtime rule may infer an end solely from the next heading until
that behaviour is separately evidenced.

## English summary

The examples show that adhikāra scope is neither an unrestricted textual range
nor a graph edge without a stopping condition. A machine model must record both
the source of a carried item and evidence for its endpoint.

## Українська

Приклади показують, що scope `adhikAra` не є ані необмеженим текстовим
діапазоном, ані просто ребром графа без умови зупинки. Машинна модель має
зберігати і джерело успадкованого елемента, і доказ його кінцевої межі.

## Deutsch

Die Beispiele zeigen: Der Umfang eines `adhikAra` ist weder ein unbegrenzter
Textbereich noch eine Graphkante ohne Endbedingung. Ein Maschinenmodell muss
Quelle des übertragenen Elements und Evidenz für dessen Ende speichern.
