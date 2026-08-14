;;; PANINI-MACHINE-MODEL-PROTOTYPE v0.1
;;; -----------------------------------
;;; Прототип (псевдокод) деривації форми "labhate" (він отримує/досягає).
;;; Ціль: продемонструвати перехід від графа інтенції до поверхневої форми.

;; 1. Визначення онтології (Ontology Definition)
;; -------------------------------------------

(def-dhatu 'qu-la\B-a~z
  :clean "laB"
  :it-markers '(qu \B a~ z)
  :gana 'bhvadi
  :meaning "prāptau" (3.1.68)
  :atmanepadi t) ; Маркери диктують Atmanepada

(def-karaka 'kartr
  :semantic-role 'agent)

;; 2. Початковий стан (Vivakṣā / Initial State)
;; ------------------------------------------
;; Мовець хоче сказати: "Агент (kartṛ) отримує/досягає (labh), дія відбувається зараз (vartamāne)".

(define-state 'state-0
  (situation
    (action (node-dhatu 'qu-la\B-a~z))
    (tense 'vartamane) ; Теперішній час
    (roles
      (node-karaka 'kartr 
                   :entity (pratipadika 'devadatta) 
                   :person 3 
                   :number 'eka)))) ; eka-vacana, prathama-purusha

;; 3. Застосування Правил (Graph Rewriting)
;; ----------------------------------------

;; КРОК 1: Вибір лакари (Tense -> Lakara)
;; Сутра 3.2.123 "vartamāne laṭ"
;; :match (situation (tense 'vartamane))
;; :apply (insert-lakara 'la~w)
(define-state 'state-1
  (situation
    (action 
      (node-dhatu 'qu-la\B-a~z)
      (node-lakara 'la~w)) ; laṭ додано
    (roles ...)))

;; КРОК 2: Заміна лакари на тіṅ (Lakara -> Tin)
;; Сутра 3.4.78 "tiptasjhi..." (замінює laṭ на 18 можливих закінчень)
;; Оскільки dhātu має маркер \Y або ṅit/ñit (в нашому випадку anudātteta / ṅit -> 1.3.12 anudāttaṅita ātmanepadam),
;; ми вибираємо ātmanepada. Далі 1.4.101-108 звужують вибір до 'ta' (3rd person, singular).
(define-state 'state-2
  (situation
    (action 
      (node-anga (node-dhatu 'qu-la\B-a~z))
      (node-pratyaya 'ta :type 'tin :padam 'atmanepadam))
    (roles ...)))

;; КРОК 3: Додавання вікарани (Vikarana)
;; Сутра 3.1.68 "kartari śap"
;; :context '(sarvadhatuke, dhatoh)
;; Оскільки 'ta' є sārvadhātuka (3.4.113), а дія позначає kartṛ (агента), ми додаємо śap.
(define-state 'state-3
  (situation
    (action 
      (node-anga 
        (node-dhatu 'qu-la\B-a~z) 
        (node-vikarana 'Sa~p)) ; śap додається між dhatu і pratyaya
      (node-pratyaya 'ta))
    (roles ...)))

;; КРОК 4: Видалення it-маркерів (It-lopa)
;; Сутра 1.3.9 "tasya lopaḥ" видаляє it-маркери з dhātu ('qu', '\B', 'a~', 'z'),
;; з vikarana ('S', 'p' -> залишається 'a') і т.д.
(define-state 'state-4
  (situation
    (action 
      (node-anga 
        (node-dhatu-clean "laB") 
        (node-vikarana-clean "a"))
      (node-pratyaya 'ta))
    (roles ...)))

;; КРОК 5: Акустична трансформація (Sandhi/Adesa)
;; Сутра 3.4.79 "ṭita ātmanepadānāṃ ṭere"
;; 'ṭit' лакара (laṭ має 'ṭ' як it-маркер) змушує ātmanepada закінчення 'ta' змінити своє 'ṭi' (останню голосну) на 'e'.
;; 'ta' -> 'te'
(define-state 'state-5
  (situation
    (action 
      (node-anga 
        (node-dhatu-clean "laB") 
        (node-vikarana-clean "a"))
      (node-pratyaya-clean "te"))
    (roles ...)))

;; 4. Фінальний вихід (Surface Form)
;; ---------------------------------
;; Конкатенація вузлів дії: "laB" + "a" + "te" = "laBate" (labhate).

(define-output 'labhate
  :provenance '(state-5 state-4 state-3 state-2 state-1 state-0))
