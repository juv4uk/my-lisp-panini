# Purity of Dhātu and Kriyā / Чистота Dhātu та Kriyā / Reinheit von Dhātu und Kriyā

Status: completed (`PHILOSOPHY-DHATU-PURITY-AND-KRIYA`)
Author: my-lisp-panini-1

---

## 🇺🇸 English: Dhātu and Kriyā Analysis
### [PANINI] Textual Definition
In Pāṇini's grammar, a `dhātu` (root) is the fundamental building block of action (`kriyā`). The rule *bhūvādayo dhātavaḥ* (1.3.1) establishes that elements like `bhū` are called `dhātu`. The concept of action (`kriyā`) is central to the assignment of semantic roles (`kāraka`), as kārakas are defined strictly by their relation to the action.

### [INTERPRETATION] Philosophical Purity
Bhartṛhari in his Vākyapadīya discusses the nature of `kriyā` extensively. Action is a process (`sādhya`), something to be accomplished, as opposed to a static entity (`siddha`). A `dhātu` purely denotes this process. It does not carry time, person, or number inherently—these are added by suffixes (`pratyaya` like `tiṅ` or `kṛt`). Thus, the `dhātu` is "pure" action potential.

### [MY-LISP HYPOTHESIS] VM Architecture Impact
In our `meta.my` model, the `dhātu` must be represented as a pure function or a stateless node. 
- It should NOT contain hardcoded state properties (like current tense).
- The `make-action-graph` creates an instance of a `kriyā` where the `dhātu` is the central operator connecting to `kāraka` arguments. 
- This confirms that our separation of `dhātu` from `tiṅ` affixes in the AST is not just a grammatical necessity, but a direct reflection of Paninian ontology.

---

## 🇺🇦 Українська: Аналіз Dhātu та Kriyā
### [PANINI] Текстове визначення
У граматиці Паніні `dhātu` (корінь) є фундаментальним будівельним блоком дії (`kriyā`). Правило *bhūvādayo dhātavaḥ* (1.3.1) встановлює, що елементи на зразок `bhū` називаються `dhātu`. Поняття дії (`kriyā`) є центральним для призначення семантичних ролей (`kāraka`), оскільки караки визначаються суворо за їхнім відношенням до дії.

### [INTERPRETATION] Філософська чистота
Бхартріхарі у своїй праці "Вак'япадія" детально розглядає природу `kriyā`. Дія — це процес (`sādhya`), те, що має бути здійснене, на противагу статичній сутності (`siddha`). `dhātu` в чистому вигляді позначає цей процес. Він не несе в собі часу, особи чи числа — вони додаються суфіксами (`pratyaya`, такими як `tiṅ` або `kṛt`). Таким чином, `dhātu` є "чистим" потенціалом дії.

### [MY-LISP HYPOTHESIS] Вплив на архітектуру VM
У нашій моделі `meta.my` `dhātu` повинен бути представлений як чиста функція або вузол без стану (stateless node).
- Він НЕ ПОВИНЕН містити жорстко закодованих властивостей стану (наприклад, поточний час).
- `make-action-graph` створює екземпляр `kriyā`, де `dhātu` є центральним оператором, що з'єднується з аргументами `kāraka`.
- Це підтверджує, що наше відділення `dhātu` від афіксів `tiṅ` в AST є не просто граматичною необхідністю, а прямим відображенням онтології Паніні.

---

## 🇩🇪 Deutsch: Analyse von Dhātu und Kriyā
### [PANINI] Textuelle Definition
In Pāṇinis Grammatik ist ein `dhātu` (Wurzel) der grundlegende Baustein der Handlung (`kriyā`). Die Regel *bhūvādayo dhātavaḥ* (1.3.1) legt fest, dass Elemente wie `bhū` als `dhātu` bezeichnet werden. Das Konzept der Handlung (`kriyā`) ist zentral für die Zuweisung semantischer Rollen (`kāraka`), da Kārakas streng durch ihre Beziehung zur Handlung definiert sind.

### [INTERPRETATION] Philosophische Reinheit
Bhartṛhari diskutiert in seinem Vākyapadīya ausführlich die Natur von `kriyā`. Handlung ist ein Prozess (`sādhya`), etwas, das vollbracht werden soll, im Gegensatz zu einer statischen Entität (`siddha`). Ein `dhātu` bezeichnet diesen Prozess in reiner Form. Es trägt nicht von Natur aus Zeit, Person oder Zahl in sich – diese werden durch Suffixe (`pratyaya` wie `tiṅ` oder `kṛt`) hinzugefügt. Somit ist das `dhātu` ein "reines" Handlungspotenzial.

### [MY-LISP HYPOTHESIS] Auswirkungen auf die VM-Architektur
In unserem `meta.my`-Modell muss das `dhātu` als reine Funktion oder als zustandsloser Knoten (stateless node) dargestellt werden.
- Es darf KEINE hartcodierten Zustandseigenschaften (wie die aktuelle Zeitform) enthalten.
- `make-action-graph` erstellt eine Instanz einer `kriyā`, bei der das `dhātu` der zentrale Operator ist, der mit `kāraka`-Argumenten verbunden wird.
- Dies bestätigt, dass unsere Trennung von `dhātu` und `tiṅ`-Affixen im AST nicht nur eine grammatikalische Notwendigkeit ist, sondern eine direkte Widerspiegelung der Pāṇinianischen Ontologie.
