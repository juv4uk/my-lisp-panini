# Causative derivational-stage identity audit

Status: `partial`. This audit asks what identity record is minimally required
when a root receives `Ric` in the selected `bhAvayati` causative example. It
does not implement recursion, add an entity model, or decide a My Lisp AST.

## English

The evidence supports a derived **term occurrence** with a new `dhAtu`
designation after the relevant sanādi-ending condition. It does not support
mutating the identity of the source root, nor does it require a semantic
referent node. The recursive-versus-flat execution model remains a machine
question.

## Українська

### [PANINI]

3.1.26 `hetumati ca` introduces `Ric` after a dhātu when the causative meaning
is to be expressed. Its accessible commentary describes the `hetu` as the
instigator of an independent `kartf`; це узгоджується з окремим boundary
audit kāraka, але не перетворює `hetu` на новий root або entity.

3.1.32 `sanAdyantA DAtavaH` є saMjYA-правилом. Доступний традиційний
матеріал explicates the set as including `RiN`/`Ric` among the relevant
sanādi affixes and states that forms ending in them receive `dhAtu`
designation. Отже, у межі прикладу є джерельна підстава розрізняти:

```text
term:root-BU              — первинний root occurrence
term:causative-BU-Ric     — похідний occurrence після Ric
designation:dhAtu         — призначення похідному occurrence за 3.1.32
```

Це не є твердженням, що `BU` «стає іншим об'єктом» або що source root
припиняє існувати в immutable history.

Sources: [3.1.26 `hetumati ca` with commentary](https://sanskritdictionary.com/panini/3-1-26),
[3.1.32 `sanAdyantA DAtavaH` and commentarial material](https://sanskritdictionary.com/panini/3-1-32),
and [1.4.55 for the causative `hetu`/`kartf` boundary](https://sanskritdictionary.com/panini/1-4-55).

### [INTERPRETATION]

The minimal immutable representation is a relation, not an overwrite:

```yaml
before: term:root-BU
rule: "3.1.26"
after: term:causative-BU-Ric
relation: derived-from
designation:
  target: term:causative-BU-Ric
  id: dhAtu
  rule: "3.1.32"
```

`source_form`, later `surface_form`, and the `dhAtu` designation therefore
remain independently inspectable. This is enough to preserve the question
whether later lakāra/tiṅ rules address a derived stage without claiming that a
machine must execute a recursive call.

The following remain unresolved and must block a complete causative trace:

1. the complete marker/lopa account for `Ric`;
2. the exact typed transition from `BU + Ric` to the cited intermediate form;
3. the verified order and conditions of vṛddhi/sandhi;
4. whether a chosen executable profile should model later derivation as nested
   invocation or as one flattened immutable trace.

### [MY-LISP HYPOTHESIS]

No `entity:<id>` is admitted. The derived occurrence can be related to its
source root through `derived-from`, while its new `dhAtu` status is an
evidence-bearing designation. A future machine may use either:

```text
nested derivation state        — implementation profile
flat append-only stage trace   — implementation profile
```

Neither is licensed as a Paninian primitive or as a change to My Lisp. The
essential evidence boundary is only: **do not overwrite root identity merely
because a later stage obtains a dhAtu designation.**

## Deutsch

Die Evidenz stützt einen abgeleiteten **Term-Vorfall** mit einer neuen
`dhAtu`-Designation nach der einschlägigen sanādi-Endung. Sie stützt weder
eine Mutation der Identität der Ausgangswurzel noch einen semantischen
Referent-Knoten. Rekursive oder flache Ausführung bleibt eine Maschinenfrage.
