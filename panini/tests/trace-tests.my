;; Tests for derivation trace system
;;
;; Verifies that each trace:
;; 1. Has the correct number of steps
;; 2. Has correct sūtra references at each step
;; 3. Final state matches derive-verb output
;; 4. Each step is marked "derived" (falsifiable)

(load "panini/machine/trace.my")

(def test-trace-pacati
  (lambda ()
    (assert-equal 5 (trace-count (trace-pacati)) "trace pacati: 5 steps")
    (assert-equal "3.1.77" (trace-step-rule (trace-step-at (trace-pacati) 1)) "trace pacati: step 1 rule")
    (assert-equal "1.3.5+1.3.9" (trace-step-rule (trace-step-at (trace-pacati) 2)) "trace pacati: step 2 rule")
    (assert-equal "3.4.78" (trace-step-rule (trace-step-at (trace-pacati) 3)) "trace pacati: step 3 rule")
    (assert-equal "1.3.3+1.3.9" (trace-step-rule (trace-step-at (trace-pacati) 4)) "trace pacati: step 4 rule")
    (assert-equal (quote (p a c a t i)) (trace-final (trace-pacati)) "trace pacati: final state")
    (assert-equal t (trace-matches-derivation? (trace-pacati) (derive-pacati)) "trace pacati: matches derivation")))

(def test-trace-bhavati
  (lambda ()
    (assert-equal 7 (trace-count (trace-bhavati)) "trace bhavati: 7 steps")
    (assert-equal "3.1.68" (trace-step-rule (trace-step-at (trace-bhavati) 1)) "trace bhavati: step 1 rule")
    (assert-equal "7.3.84" (trace-step-rule (trace-step-at (trace-bhavati) 5)) "trace bhavati: step 5 rule (guṇa)")
    (assert-equal "6.1.88" (trace-step-rule (trace-step-at (trace-bhavati) 6)) "trace bhavati: step 6 rule (eco)")
    (assert-equal (quote (b h a v a t i)) (trace-final (trace-bhavati)) "trace bhavati: final state")
    (assert-equal t (trace-matches-derivation? (trace-bhavati) (derive-bhavati)) "trace bhavati: matches derivation")))

(def test-trace-labhate
  (lambda ()
    (assert-equal 5 (trace-count (trace-labhate)) "trace labhate: 5 steps")
    (assert-equal "3.4.79" (trace-step-rule (trace-step-at (trace-labhate) 4)) "trace labhate: step 4 rule (ṭere)")
    (assert-equal (quote (l a b h a t e)) (trace-final (trace-labhate)) "trace labhate: final state")
    (assert-equal t (trace-matches-derivation? (trace-labhate) (derive-labhate)) "trace labhate: matches derivation")))

(def test-trace-tudati
  (lambda ()
    (assert-equal 5 (trace-count (trace-tudati)) "trace tudati: 5 steps")
    (assert-equal "3.1.77" (trace-step-rule (trace-step-at (trace-tudati) 1)) "trace tudati: step 1 rule")
    (assert-equal (quote (t u d a t i)) (trace-final (trace-tudati)) "trace tudati: final state")
    (assert-equal t (trace-matches-derivation? (trace-tudati) (derive-tudati)) "trace tudati: matches derivation")))

(def test-trace-verification
  (lambda ()
    (assert-equal (quote derived) (trace-step-verification (trace-step-at (trace-pacati) 1)) "trace: step verification = derived")
    (assert-equal (quote derived) (trace-step-verification (trace-step-at (trace-bhavati) 5)) "trace: bhavati guṇa step = derived")))

(def test-trace-all
  (lambda ()
    (print "Running Trace Tests...")
    (test-trace-pacati)
    (test-trace-bhavati)
    (test-trace-labhate)
    (test-trace-tudati)
    (test-trace-verification)
    (print "Trace tests complete.")))
