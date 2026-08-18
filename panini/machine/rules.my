;; Executable prototype operations. All derivation claims remain machine-level.

(def make-term
  (lambda (source-form surface-form term-type tags)
    (list (cons (quote source-form) source-form)
          (cons (quote surface-form) surface-form)
          (cons (quote type) term-type)
          (cons (quote tags) tags))))

(def term-source-form (lambda (term) (cdr (assoc (quote source-form) term))))
(def term-surface-form (lambda (term) (cdr (assoc (quote surface-form) term))))
(def term-type (lambda (term) (cdr (assoc (quote type) term))))
(def term-tags (lambda (term) (cdr (assoc (quote tags) term))))

(def term-add-tag
  (lambda (term tag)
    (make-term (term-source-form term)
               (term-surface-form term)
               (term-type term)
               (cons tag (term-tags term)))))

(def term-set-surface
  (lambda (term surface)
    (make-term (term-source-form term) surface (term-type term) (term-tags term))))

(def sound-string
  (lambda (sounds)
    (cond
      ((atom sounds) "")
      (t (string-append (symbol->string (car sounds)) (sound-string (cdr sounds)))))))

(def concat-terms
  (lambda (terms)
    (cond
      ((atom terms) "")
      (t (string-append (sound-string (term-surface-form (car terms)))
                        (concat-terms (cdr terms)))))))

(def apply-guRa
  (lambda (sound)
    (cond
      ((equal? sound (quote a)) (quote a))
      ((equal? sound (quote A)) (quote a))
      ((equal? sound (quote i)) (quote e))
      ((equal? sound (quote I)) (quote e))
      ((equal? sound (quote u)) (quote o))
      ((equal? sound (quote U)) (quote o))
      ((equal? sound (quote f)) (quote ar))
      ((equal? sound (quote F)) (quote ar))
      ((equal? sound (quote x)) (quote al))
      (t sound))))

(def vowel?
  (lambda (sound)
    (member? sound (quote (a A i I u U f F x X e o E O)))))

(def apply-eco-sandhi
  (lambda (sound next-sound)
    (cond
      ((not (vowel? next-sound)) sound)
      ((equal? sound (quote e)) (quote (a y)))
      ((equal? sound (quote o)) (quote (a v)))
      ((equal? sound (quote E)) (quote (A y)))
      ((equal? sound (quote O)) (quote (A v)))
      (t sound))))

;; The following outputs are deliberately narrow executable fixtures. They
;; test runtime compatibility, not complete historical derivations.

;; Executable Bavati step-trace (PANINI-MACHINE-DERIVE-BAVATI-EXECUTION).
;; Bound by research/bavati-derivation-machine-readiness.md: the trace records
;; 7 state transitions and terminates partial with explicit unknowns. The
;; observed surface form Bavati is a display observation, not a proof of the
;; unresolved guna/sandhi precondition chain. Machine level only.
(def bavati-unknowns
  (list "exact-source-supported-account-of-initial-S-in-Sap"
        "bridge-from-it-analysis-to-sarvadhatuka-precondition"
        "complete-applicability-conditions-for-each-selection"
        "independent-typed-operation-check-for-each-state-transition"))

(def bavati-result
  (list (cons (quote status) (quote partial))
        (cons (quote state) "state:bavati:sap-a-ti")
        (cons (quote unknowns) bavati-unknowns)))

(def bavati-step
  (lambda (n rule before after operation verification)
    (list (cons (quote step) n)
          (cons (quote rule) rule)
          (cons (quote before) before)
          (cons (quote after) after)
          (cons (quote operation) operation)
          (cons (quote verification) verification))))

(def bavati-steps
  (list
    (bavati-step 1 "3.2.123" "state:bavati:input" "state:bavati:lat"
                 "attach-lakara-candidate" (quote derived))
    (bavati-step 2 "3.4.78" "state:bavati:lat" "state:bavati:tip"
                 "select-tip-occurrence" (quote derived))
    (bavati-step 3 "1.3.3+1.3.9" "state:bavati:tip" "state:bavati:ti"
                 "it-designation-final-p-then-lopa" (quote derived))
    (bavati-step 4 "3.1.68" "state:bavati:ti" "state:bavati:sap-raw-ti"
                 "insert-vikarana-Sap" (quote needs-check))
    (bavati-step 5 "1.3.8+1.3.3+1.3.9+3.4.113" "state:bavati:sap-raw-ti"
                 "state:bavati:sap-a-ti" "sap-subtrace-lopa" (quote needs-check))
    (bavati-step 6 "7.3.84" "state:bavati:sap-a-ti" "state:bavati:bo-a-ti"
                 "guna-U-to-o" (quote needs-check))
    (bavati-step 7 "6.1.78" "state:bavati:bo-a-ti" "state:bavati:bavati"
                 "eco-sandhi-o-a-to-av-a" (quote needs-check))))

(def bavati-surface-terms
  (list (make-term (quote (B U)) (quote (B a v a t i)) (quote dhAtu) (quote (machine-fixture observation)))))

(def bavati-trace-result
  (lambda (trace) (car trace)))

(def bavati-trace-steps
  (lambda (trace) (cdr (car (cdr trace)))))

(def bavati-status
  (lambda (trace)
    (cdr (assoc (quote status) (bavati-trace-result trace)))))

(def bavati-unknowns-of
  (lambda (trace)
    (cdr (assoc (quote unknowns) (bavati-trace-result trace)))))

(def bavati-step-count
  (lambda (trace) (length (bavati-trace-steps trace))))

(def bavati-step-at-from
  (lambda (steps n)
    (cond
      ((equal? n 1) (car steps))
      (t (bavati-step-at-from (cdr steps) (- n 1))))))

(def bavati-step-at
  (lambda (trace n)
    (bavati-step-at-from (bavati-trace-steps trace) n)))

(def bavati-step-rule
  (lambda (step) (cdr (assoc (quote rule) step))))

(def bavati-step-after
  (lambda (step) (cdr (assoc (quote after) step))))

(def derive-Bavati
  (lambda ()
    (list bavati-result (cons (quote steps) bavati-steps))))

(def derive-dadAti
  (lambda ()
    (list (make-term (quote (d A)) (quote (d a d A t i)) (quote dhAtu) (quote (machine-fixture))))) )

(def derive-kArayati
  (lambda ()
    (list (make-term (quote (k f)) (quote (k A r a y a t i)) (quote dhAtu) (quote (machine-fixture))))))

;; Narrow conflict fixture for dadAti. These fields declare a machine relation;
;; they do not independently establish an interpretation of the sutra corpus.
(def dadati-rule-2-4-72
  (list (cons (quote id) "2.4.72")
        (cons (quote utsarga) (quote ()))
        (cons (quote kind) (quote machine-fixture))))

(def dadati-rule-2-4-75
  (list (cons (quote id) "2.4.75")
        (cons (quote utsarga) "2.4.72")
        (cons (quote kind) (quote machine-fixture))))

;; A deliberately visible state change for the conflict acceptance test.
(def dadati-apply-slu
  (lambda (dhatu sap)
    (list (term-add-tag dhatu (quote slu-applied))
          (term-add-tag sap (quote slu-elided)))))

;; Class 8 (tanAdi) derivation fixture: kR + vikaraNa SNu + sArvadhAtuka ti.
;; Machine level only: 3.1.79 supplies the vikaraNa; guNa (7.3.84) maps f -> ar
;; and u -> o. This is a declared machine relation, not a historical derivation.
(def karoti-vikarana-snu
  (list (cons (quote id) "3.1.79")
        (cons (quote kind) (quote machine-fixture))
        (cons (quote vikarana) (quote SNu))))

(def append-list
  (lambda (a b)
    (cond
      ((atom a) b)
      (t (cons (car a) (append-list (cdr a) b))))))

(def guNa-flatten
  (lambda (sound)
    (cond
      ((atom (apply-guRa sound)) (list (apply-guRa sound)))
      (t (apply-guRa sound)))))

(def apply-guRa-sounds
  (lambda (sounds)
    (cond
      ((atom sounds) (quote ()))
      (t (append-list (guNa-flatten (car sounds))
                      (apply-guRa-sounds (cdr sounds)))))))

(def derive-karoti
  (lambda ()
    (list (make-term (quote (k f)) (apply-guRa-sounds (quote (k f)))
                     (quote dhAtu) (quote (class-8 tanAdi guNa-applied machine-fixture)))
          (make-term (quote (u)) (apply-guRa-sounds (quote (u)))
                     (quote vikaraNa) (quote (SNu-3-1-79 guNa-applied machine-fixture)))
          (make-term (quote (t i)) (quote (t i)) (quote pratyaya) (quote (sArvadhAtuka machine-fixture))))))

;; Class 1 (bhvAdi) derivation fixture: pac + vikaraNa Sap + sArvadhAtuka ti.
;; Sap surfaces as a (3.1.68); no guNa applies to pac. The 3-kAraka example
;; (sTAlyAM pacati odanam) is expressed as an action graph with variable
;; kAraka arity (FIXUP-ACTION-GRAPH-ARITY): the kAraka set depends on the
;; sentence, not on the dhAtu alone. Machine level only; [MY-LISP HYPOTHESIS]
;; H1 graph-edge model (hypothesis-ledger.md).
(def pacati-sap-vikarana
  (list (cons (quote id) "3.1.68")
        (cons (quote kind) (quote machine-fixture))
        (cons (quote vikarana) (quote Sap))))

(def pac-gana
  (list (cons (quote id) "pac")
        (cons (quote gana) 1)
        (cons (quote pada) (quote ubhayapada))
        (cons (quote kind) (quote machine-fixture))))

(def derive-pacati
  (lambda ()
    (list (make-term (quote (p a c)) (quote (p a c))
                     (quote dhAtu) (quote (class-1 bhvAdi machine-fixture)))
          (make-term (quote (a)) (quote (a))
                     (quote vikaraNa) (quote (Sap-3-1-68 machine-fixture)))
          (make-term (quote (t i)) (quote (t i)) (quote pratyaya) (quote (sArvadhAtuka machine-fixture))))))

(def pacati-3karaka
  (lambda ()
    (list (cons (quote action-id) (quote action-pac))
          (cons (quote dhAtu) (quote pac))
          (cons (quote kAraka-args)
                (list (cons (quote kartf) (quote devadatta))
                      (cons (quote karman) (quote odana))
                      (cons (quote aDikaraRa) (quote sTAlI)))))))

;; Static anuvRtti-edge graph (machine fixture). Per
;; research/anuvrtti-graph-vs-dynamic-binding.md, anuvRtti is a property of
;; the text, not of execution state; each rule declares its inherited words
;; and their source sUtra explicitly instead of dynamic binding.
(def panini-rule-3-1-1
  (list (cons (quote id) "3.1.1")
        (cons (quote kind) (quote machine-fixture))
        (cons (quote inherits-from) (quote ()))
        (cons (quote inherits-words) (quote (pratyayaH)))))

(def panini-rule-3-1-68
  (list (cons (quote id) "3.1.68")
        (cons (quote kind) (quote machine-fixture))
        (cons (quote inherits-from) (quote ("3.1.1")))
        (cons (quote inherits-words) (quote (pratyayaH)))))

(def panini-rule-3-1-79
  (list (cons (quote id) "3.1.79")
        (cons (quote kind) (quote machine-fixture))
        (cons (quote inherits-from) (quote ("3.1.1")))
        (cons (quote inherits-words) (quote (pratyayaH)))))

(def anuvrtti-graph-rules
  (list panini-rule-3-1-1 panini-rule-3-1-68 panini-rule-3-1-79))

(def rule-inherits-from
  (lambda (rule)
    (cdr (assoc (quote inherits-from) rule))))

(def rule-inherits-words
  (lambda (rule)
    (cdr (assoc (quote inherits-words) rule))))

;; All source rule ids referenced by any inherits-from edge.
(def dag-source-ids
  (lambda (rules)
    (cond
      ((atom rules) (quote ()))
      (t (cons (rule-id (car rules)) (dag-source-ids (cdr rules)))))))

;; Membership in a flat list of ids.
(def dag-has-id?
  (lambda (id ids)
    (member? id ids)))

;; Every inherits-from target must exist in the rule set. Machine-level only.
(def dag-edges-resolve?
  (lambda (rules)
    (dag-edges-resolve-from? rules (dag-source-ids rules))))

(def dag-edges-resolve-from?
  (lambda (rules all-ids)
    (cond
      ((atom rules) t)
      (t (cond
           ((null-edges? (rule-inherits-from (car rules)))
            (dag-edges-resolve-from? (cdr rules) all-ids))
           (t (cond
                ((dag-has-id? (car (rule-inherits-from (car rules))) all-ids)
                 (dag-edges-resolve-from? (cdr rules) all-ids))
                (t (quote ())))))))))

(def null-edges?
  (lambda (edges)
    (cond
      ((atom edges) t)
      (t (quote ())))))

;; Negative / counterfactual fixtures (PANINI-MACHINE-NEGATIVE-TESTS).
;; Each predicate returns t when the operation is eligible, otherwise '().
;; The tests assert that ineligible or invalid cases are rejected; a passing
;; final string alone is not sufficient evidence.

;; 1. it-deletion order: an it marker may be deleted only when marked.
(def it-deletable?
  (lambda (term)
    (member? (quote it-marker) (term-tags term))))

;; 2. guNa eligibility: only short/long i u f x are eligible; a, A and the
;;    guNa results e o E O are not.
(def guNa-eligible?
  (lambda (sound)
    (member? sound (quote (i I u U f F x)))))

;; 3. SLP1 r-vowel spelling: f = R, F = RR; a bare r is not a vowel glyph.
(def slp1-r-vowel?
  (lambda (sound)
    (member? sound (quote (f F)))))

;; 4. Sap eligibility: a juhotyAdi dhAtu requires Slu first; Sap is not
;;    eligible while the dhAtu still carries the juhotyAdi tag.
(def sap-eligible?
  (lambda (dhatu)
    (not (member? (quote juhotyAdi) (term-tags dhatu)))))

;; 5. Conflict priority: mutual apavAda declarations are ambiguous and must be
;;    rejected; the declared pair must be unambiguous.
(def ambiguous-apavada?
  (lambda (a b)
    (cond
      ((apavada-of? a b) (apavada-of? b a))
      (t (quote ())))))

(def incorrect-priority-pair-a
  (list (cons (quote id) "2.4.72")
        (cons (quote utsarga) "2.4.75")
        (cons (quote kind) (quote machine-fixture))))

(def incorrect-priority-pair-b
  (list (cons (quote id) "2.4.75")
        (cons (quote utsarga) "2.4.72")
        (cons (quote kind) (quote machine-fixture))))
