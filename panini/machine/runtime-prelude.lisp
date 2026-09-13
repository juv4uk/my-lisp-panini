;; Minimal, macro-free prelude for executable Panini machine fixtures.
;; It isolates fixture acceptance from the evolving shared My Lisp core.

(def list (lambda args args))

(def not
  (lambda (value)
    (cond
      (value (quote ()))
      (t t))))

(def second (lambda (values) (car (cdr values))))
(def third (lambda (values) (car (cdr (cdr values)))))

(def equal?
  (lambda (left right)
    (cond
      ((atom left) (cond ((atom right) (eq left right)) (t (quote ()))))
      ((atom right) (quote ()))
      ((equal? (car left) (car right)) (equal? (cdr left) (cdr right)))
      (t (quote ())))))

(def member?
  (lambda (item values)
    (cond
      ((atom values) (quote ()))
      ((equal? item (car values)) t)
      (t (member? item (cdr values))))))

(def assoc
  (lambda (key entries)
    (cond
      ((atom entries) (quote ()))
      ((equal? key (car (car entries))) (car entries))
      (t (assoc key (cdr entries))))))
