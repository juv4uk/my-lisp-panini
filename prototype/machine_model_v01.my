; panini-machine-model v0.1 -- first iteration
; Pure-functional rule engine over a derivation graph.
; State  = (graph . appliedRuleIds); node = (id type . tags).
; Conflict resolution v0.1: LAST matching rule in registry order wins
; (documented simplification of vipratishedha / para-sutra precedence).
; Uses only McCarthy-core primitives verified against the :9999 oracle.

(def cadr  (lambda (x) (car (cdr x))))
(def caddr (lambda (x) (car (cdr (cdr x)))))
(def nullq (lambda (x) (atom x)))

(def memberq (lambda (x xs)
  (cond ((nullq xs) ())
        ((eq (car xs) x) t)
        (t (memberq x (cdr xs))))))

(def tags-include (lambda (tags tag)
  (cond ((nullq tags) (cons tag ()))
        ((eq (car tags) tag) tags)
        (t (cons (car tags) (tags-include (cdr tags) tag))))))

; ---- node ----
; node = (id type . tags)
(def make-node  (lambda (id type tags) (cons id (cons type tags))))
(def node-id    (lambda (n) (car n)))
(def node-type  (lambda (n) (cadr n)))
(def node-tags  (lambda (n) (cddr n)))

(def node-add-tag (lambda (n tag)
  (cond ((memberq tag (node-tags n)) n)
        (t (make-node (node-id n) (node-type n)
                       (tags-include (node-tags n) tag))))))

; ---- rules ----
; rule = (id matchfn applyfn)
(def mk-rule     (lambda (id matchfn applyfn) (cons id (cons matchfn (cons applyfn ())))))
(def rule-match  (lambda (r) (cadr r)))
(def rule-apply  (lambda (r) (caddr r)))
(def rule-id     (lambda (r) (car r)))

(def pick-winner (lambda (rules n acc)
  ; last matching rule in registry order wins
  (cond ((nullq rules) acc)
        (((rule-match (car rules)) n)
         (pick-winner (cdr rules) n (car rules)))
        (t (pick-winner (cdr rules) n acc)))))

; ---- engine ----
; sg: (rules nodes accGraph accIds) -> (newGraph . newIds-reversed)
(def sg (lambda (rules nodes accG accIds)
  (cond ((nullq nodes) (cons accG accIds))
        (t ((lambda (w)
               (cond ((nullq w)
                      (sg rules (cdr nodes)
                          (cons (car nodes) accG) accIds))
                     (t
                      (sg rules (cdr nodes)
                          (cons ((rule-apply w) (car nodes)) accG)
                          (cons (rule-id w) accIds)))))
             (pick-winner rules (car nodes) ()))))))

(def rev2 (lambda (xs acc)
  (cond ((nullq xs) acc)
        (t (rev2 (cdr xs) (cons (car xs) acc))))))

(def append2 (lambda (a b)
  (cond ((nullq a) b)
        (t (cons (car a) (append2 (cdr a) b))))))

; state = (graph . traceIds)
(def step (lambda (st rules)
  ((lambda (r)
     (cons (car r)
           (append2 (rev2 (cdr r) ()) (cdr st))))
   (sg rules (car st) () ()))))

; ---- demo: saMjna tagging + vipratishedha-later-wins ----
(def match-phonemes (lambda (n) (eq (node-type n) (quote phonemes))))
(def match-action   (lambda (n) (eq (node-type n) (quote action))))

(def RULES
  (cons (mk-rule (quote R-1-1-1-vrddhi) match-phonemes
                 (lambda (n) (node-add-tag n (quote vrddhi))))
  (cons (mk-rule (quote R-1-1-2-guna)  match-phonemes
                 (lambda (n) (node-add-tag n (quote guna))))
  (cons (mk-rule (quote R-1-3-1-dhatu) match-action
                 (lambda (n) (node-add-tag n (quote dhatu))))
        ()))))

(def DEMO-GRAPH
  (cons (make-node (quote b1) (quote phonemes) ())
  (cons (make-node (quote d1) (quote action) ())
  (cons (make-node (quote k1) (quote entity) ())
        ()))))

(step (cons DEMO-GRAPH ()) RULES)
