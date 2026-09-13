;; Minimal machine-level rule selection. It is not a universal Panini scheduler.

(def rule-field
  (lambda (name rule)
    (cdr (assoc name rule))))

(def rule-utsarga
  (lambda (rule)
    (rule-field (quote utsarga) rule)))

(def rule-id
  (lambda (rule)
    (rule-field (quote id) rule)))

(def apavada-of?
  (lambda (candidate general)
    (equal? (rule-utsarga candidate) (rule-id general))))

(def resolve-declared-apavada
  (lambda (first second)
    (cond
      ((apavada-of? first second) first)
      ((apavada-of? second first) second)
      (t (quote ())))))

;; This trace records only a relation declared by this machine fixture. It is
;; neither a universal scheduler nor a proof of historical precedence.
(def resolve-declared-apavada-traced
  (lambda (first second)
    (cond
      ((apavada-of? first second) (list (quote resolved-by) (quote apavAda) first))
      ((apavada-of? second first) (list (quote resolved-by) (quote apavAda) second))
      (t (list (quote unresolved) (quote ()))))))
