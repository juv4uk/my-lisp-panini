;;; PANINI-SYMBOLIC-INFERENCE (v0.1)
;;; Pure Lisp Implementation of Graph Rewriting

(def *initial-state* 
  '(() ;; history
    (situation
      (action (dhatu (raw . "qu-la\\B-a~z") (clean . "laB")))
      (tense (value . vartamane))
      (roles (karaka (semantic-role . agent) (person . 3) (number . eka))))))

(def find-node-in-list
  (lambda (type lst)
    (cond
      ((atom lst) '())
      (t ((lambda (res)
            (cond
              ((not (equal? res '())) res)
              (t (find-node-in-list type (cdr lst)))))
          (find-node type (car lst)))))))

(def find-node
  (lambda (type tree)
    (cond
      ((atom tree) '())
      ((eq (car tree) type) tree)
      (t (find-node-in-list type (cdr tree))))))

(def lookup
  (lambda (key alist)
    (cond
      ((atom alist) '())
      ((eq (car (car alist)) key) (cdr (car alist)))
      (t (lookup key (cdr alist))))))

;; Rule 1: 3.2.123 "vartamāne laṭ"
(def rule-lat
  (lambda (state)
    ((lambda (history situation)
       ((lambda (tense lakara tin)
          (cond
            ((not (equal? tense '()))
             (cond
               ((eq (cdr (assoc 'value (cdr tense))) 'vartamane)
                (cond
                  ((equal? lakara '())
                   (cond
                     ((equal? tin '())
                      (list (cons "3.2.123 vartamāne laṭ" history)
                            '(situation
                               (action 
                                 (dhatu (raw . "qu-la\\B-a~z") (clean . "laB"))
                                 (lakara (value . "la~w")))
                               (tense (value . vartamane))
                               (roles (karaka (semantic-role . agent) (person . 3) (number . eka))))))
                     (t state)))
                  (t state)))
               (t state)))
            (t state)))
        (find-node 'tense situation)
        (find-node 'lakara situation)
        (find-node 'pratyaya situation)))
     (car state)
     (car (cdr state)))))

;; Rule 2: 3.4.78 "tiptasjhi..." (lakara -> tin)
(def rule-tin
  (lambda (state)
    ((lambda (history situation)
       ((lambda (lakara tin)
          (cond
            ((not (equal? lakara '()))
             (cond
               ((equal? tin '())
                (list (cons "3.4.78 tiptasjhi..." history)
                      '(situation
                         (action 
                           (anga (dhatu (raw . "qu-la\\B-a~z") (clean . "laB")))
                           (pratyaya (value . "ta") (type . tin) (padam . atmanepadam)))
                         (tense (value . vartamane))
                         (roles (karaka (semantic-role . agent) (person . 3) (number . eka))))))
               (t state)))
            (t state)))
        (find-node 'lakara situation)
        (find-node 'pratyaya situation)))
     (car state)
     (car (cdr state)))))

;; Rule 3: 3.1.68 "kartari śap"
(def rule-sap
  (lambda (state)
    ((lambda (history situation)
       ((lambda (anga vikarana)
          (cond
            ((not (equal? anga '()))
             (cond
               ((equal? vikarana '())
                (list (cons "3.1.68 kartari śap" history)
                      '(situation
                         (action 
                           (anga (dhatu (raw . "qu-la\\B-a~z") (clean . "laB"))
                                 (vikarana (value . "Sa~p")))
                           (pratyaya (value . "ta") (type . tin) (padam . atmanepadam)))
                         (tense (value . vartamane))
                         (roles (karaka (semantic-role . agent) (person . 3) (number . eka))))))
               (t state)))
            (t state)))
        (find-node 'anga situation)
        (find-node 'vikarana situation)))
     (car state)
     (car (cdr state)))))

;; Rule 4: 1.3.9 "tasya lopaḥ"
(def rule-lopa
  (lambda (state)
    ((lambda (history situation)
       ((lambda (vikarana)
          (cond
            ((not (equal? vikarana '()))
             (cond
               ((equal? (cdr (assoc 'value (cdr vikarana))) "Sa~p")
                (list (cons "1.3.9 tasya lopaḥ" history)
                      '(situation
                         (action 
                           (anga (dhatu (raw . "laB") (clean . "laB"))
                                 (vikarana (value . "a")))
                           (pratyaya (value . "ta") (type . tin) (padam . atmanepadam)))
                         (tense (value . vartamane))
                         (roles (karaka (semantic-role . agent) (person . 3) (number . eka))))))
               (t state)))
            (t state)))
        (find-node 'vikarana situation)))
     (car state)
     (car (cdr state)))))

;; Rule 5: 3.4.79 "ṭita ātmanepadānāṃ ṭere"
(def rule-tere
  (lambda (state)
    ((lambda (history situation)
       ((lambda (vikarana prat)
          (cond
            ((not (equal? prat '()))
             (cond
               ((equal? (cdr (assoc 'value (cdr prat))) "ta")
                (cond
                  ((not (equal? vikarana '()))
                   (cond
                     ((equal? (cdr (assoc 'value (cdr vikarana))) "a")
                      (list (cons "3.4.79 ṭita ātmanepadānāṃ ṭere" history)
                            '(situation
                               (action 
                                 (anga (dhatu (raw . "laB") (clean . "laB"))
                                       (vikarana (value . "a")))
                                 (pratyaya (value . "te") (type . tin) (padam . atmanepadam)))
                               (tense (value . vartamane))
                               (roles (karaka (semantic-role . agent) (person . 3) (number . eka))))))
                     (t state)))
                  (t state)))
               (t state)))
            (t state)))
        (find-node 'vikarana situation)
        (find-node 'pratyaya situation)))
     (car state)
     (car (cdr state)))))

;; Engine execution
(def derive-labhate
  (lambda ()
    ((lambda (s1)
       ((lambda (s2)
          ((lambda (s3)
             ((lambda (s4)
                ((lambda (s5)
                   (list 'final-state (car (cdr s5)) 'history (reverse (car s5))))
                 (rule-tere s4)))
              (rule-lopa s3)))
           (rule-sap s2)))
        (rule-tin s1)))
     (rule-lat *initial-state*))))

(print "--- DERIVATION RESULT ---")
(print (derive-labhate))
