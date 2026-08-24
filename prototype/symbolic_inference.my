; symbolic-inference v0.1 -- anuvrtti-based universal inference
; Extends machine_model v0.1: rules carry (id ctx matchfn applyfn);
; ctx = required adhikara markers. Rule fires only when EVERY marker
; is active. adhikara rules have empty ctx and their applyfn EXTENDS
; the context -- sequential inheritance demo 3.1.1 -> 3.1.2 -> 3.1.68.
; Pure functional; McCarthy-core primitives only.

(def cadr  (lambda (x) (car (cdr x))))
(def caddr (lambda (x) (car (cdr (cdr x)))))
(def nullq (lambda (x) (atom x)))

(def memberq (lambda (x xs)
  (cond ((nullq xs) ())
        ((eq (car xs) x) t)
        (t (memberq x (cdr xs))))))

(def contains-all (lambda (need have)
  (cond ((nullq need) t)
        ((memberq (car need) have) (contains-all (cdr need) have))
        (t ()))))

; ---- state ----
; state = (graph . (ctx . traceIds))
(def make-state (lambda (graph ctx trace) (cons graph (cons ctx trace))))
(def st-graph   (lambda (s) (car s)))
(def st-ctx     (lambda (s) (car (cdr s))))
(def st-trace   (lambda (s) (cdr (cdr s))))

; ---- nodes ----
(def make-node (lambda (id type tags) (cons id (cons type tags))))
(def node-type (lambda (n) (cadr n)))
(def node-tags (lambda (n) (cddr n)))
(def tags-include (lambda (tags tag)
  (cond ((nullq tags) (cons tag ()))
        ((eq (car tags) tag) tags)
        (t (cons (car tags) (tags-include (cdr tags) tag))))))
(def node-has-tag (lambda (n tag) (memberq tag (node-tags n))))
(def node-add-tag (lambda (n tag)
  (cond ((node-has-tag n tag) n)
        (t (make-node (car n) (node-type n)
                       (tags-include (node-tags n) tag))))))

(def map-add-sap-target (lambda (g)
  (cond ((nullq g) ())
        (t (cons (node-add-tag (car g) (quote sap-target))
                  (map-add-sap-target (cdr g)))))))

; ---- rules ----
; rule = (id ctx matchfn applyfn); proper 3-element list
(def mk-rule (lambda (id ctx matchfn applyfn)
  (cons id (cons ctx (cons matchfn (cons applyfn ()))))))
(def r-id    (lambda (r) (car r)))
(def r-ctx   (lambda (r) (cadr r)))
(def r-match (lambda (r) (caddr r)))
(def r-apply (lambda (r) (car (cdr (cdr (cdr r))))))

(def rule-fires (lambda (r st)
  (cond ((contains-all (r-ctx r) (st-ctx st))
         ((r-match r) st))
        (t ()))))

; ---- engine ----
(def pick-winner (lambda (rules st acc)
  (cond ((nullq rules) acc)
        ((rule-fires (car rules) st)
         (pick-winner (cdr rules) st (car rules)))
        (t (pick-winner (cdr rules) st acc)))))

(def step (lambda (st rules)
  ((lambda (w)
     (cond ((nullq w) st)
           (t ((r-apply w)
                (make-state (st-graph st) (st-ctx st)
                            (cons (r-id w) (st-trace st)))))))
   (pick-winner rules st ()))))

; ---- adhikara chain demo ----
(def RULES
  (cons
    (mk-rule (quote R-3-1-1-pratyayah) ()
             (lambda (st) t)
             (lambda (st)
               (make-state (st-graph st)
                           (cons (quote pratyayah) (st-ctx st))
                           (st-trace st))))
  (cons
    (mk-rule (quote R-3-1-2-paras-ca) (quote (pratyayah))
             (lambda (st) t)
             (lambda (st)
               (make-state (st-graph st)
                           (cons (quote paras-ca) (st-ctx st))
                           (st-trace st))))
  (cons
    (mk-rule (quote R-3-1-68-kartari-sap) (quote (pratyayah paras-ca))
             (lambda (st) t)
             (lambda (st)
               (make-state
                 (map-add-sap-target (st-graph st))
                 (st-ctx st)
                 (st-trace st))))
    ()))))
(def S0 (make-state
          (cons (make-node (quote d1) (quote action) (quote (unprocessed))) ())
          ()
          ()))
(def S1 (step S0 RULES))
(def S2 (step S1 RULES))
(def S3 (step S2 RULES))
S3
