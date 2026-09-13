;; Panini machine compatibility helpers for documented My Lisp + core.my.

(def list-last
  (lambda (values)
    (cond
      ((atom (cdr values)) (car values))
      (t (list-last (cdr values))))))

(def list-but-last
  (lambda (values)
    (cond
      ((atom (cdr values)) (quote ()))
      (t (cons (car values) (list-but-last (cdr values)))))))

(def machine-rule
  (lambda (id condition action provenance)
    (list (cons (quote id) id)
          (cons (quote condition) condition)
          (cons (quote action) action)
          (cons (quote provenance) provenance))))

(def machine-rule-id
  (lambda (rule)
    (cdr (assoc (quote id) rule))))
