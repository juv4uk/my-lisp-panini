;; Tests for tiṅ system + verbal derivation engine
;;
;; All derivations verified against Python reference implementation.

(load "panini/machine/derivation.my")

(def test-ting-table
  (lambda ()
    ;; Parasmaipada it-lopa
    (assert-equal (quote (t i)) (get-ting-para (quote tip)) "ting: tip → ti")
    (assert-equal (quote (t a)) (get-ting-para (quote tas)) "ting: tas → ta")
    (assert-equal (quote (s i)) (get-ting-para (quote sip)) "ting: sip → si")
    (assert-equal (quote (t h a)) (get-ting-para (quote tha)) "ting: tha → tha (no it)")
    (assert-equal (quote (m i)) (get-ting-para (quote mip)) "ting: mip → mi")
    ;; Atmanepada
    (assert-equal (quote (t a)) (get-ting-atma (quote ta)) "ting: ta → ta")
    (assert-equal (quote (A t A)) (get-ting-atma (quote AtAm)) "ting: AtAm → AtA")))

(def test-vikarana
  (lambda ()
    ;; Class 1: Śap → S,a,p → remove S,p → a
    (assert-equal (quote (a)) (get-vikarana-clean 1) "vik: class 1 Śap → a")
    ;; Class 6: Śa → S,a → remove S → a
    (assert-equal (quote (a)) (get-vikarana-clean 6) "vik: class 6 Śa → a")
    ;; ṭit check
    (assert-equal t (vikarana-has-tit? 1) "vik: class 1 has ṭit")
    (assert-equal (quote ()) (vikarana-has-tit? 6) "vik: class 6 no ṭit")))

(def test-tere
  (lambda ()
    ;; 3.4.79: ta → te when ātmanepada + ṭit
    (assert-equal (quote (t e)) (apply-tere (quote (t a)) t t) "tere: ta→te (atma+ṭit)")
    (assert-equal (quote (t a)) (apply-tere (quote (t a)) (quote ()) t) "tere: ta stays (no ṭit)")
    (assert-equal (quote (t a)) (apply-tere (quote (t a)) t (quote ())) "tere: ta stays (not atma)")))

(def test-derive-pacati
  (lambda ()
    ;; pac (class 6) + Śa + tip → pac + a + ti → pacati
    (assert-equal (quote (p a c a t i)) (derive-pacati) "derive: pacati")
    (assert-equal "pacati" (derive-verb-string (quote (p a c)) 6 (quote tip) (quote ())) "derive: pacati string")))

(def test-derive-bhavati
  (lambda ()
    ;; bhU (class 1) + Śap + tip
    ;; Step 1: bhU + a + ti (it-lopa)
    ;; Step 2: guṇa U→o: bho + a + ti
    ;; Step 3: eco o→av: bhav + a + ti → bhavati
    (assert-equal (quote (b h a v a t i)) (derive-bhavati) "derive: bhavati")
    (assert-equal "bhavati" (derive-verb-string (quote (b h U)) 1 (quote tip) (quote ())) "derive: bhavati string")))

(def test-derive-labhate
  (lambda ()
    ;; labh (class 1, ātmanepada) + Śap + ta
    ;; Step 1: labh + a + ta (it-lopa)
    ;; Step 2: ṭere: ta → te (ṭit triggers)
    ;; Step 3: labh + a + te → labhate (no guṇa: final 'h' is not a vowel)
    (assert-equal (quote (l a b h a t e)) (derive-labhate) "derive: labhate")
    (assert-equal "labhate" (derive-verb-string (quote (l a b h)) 1 (quote ta) t) "derive: labhate string")))

(def test-derive-tudati
  (lambda ()
    ;; tud (class 6) + Śa + tip → tud + a + ti → tudati (no guṇa: class 6 has no ṭit)
    (assert-equal (quote (t u d a t i)) (derive-tudati) "derive: tudati")
    (assert-equal "tudati" (derive-verb-string (quote (t u d)) 6 (quote tip) (quote ())) "derive: tudati string")))

(def test-derivation-all
  (lambda ()
    (print "Running Derivation Tests...")
    (test-ting-table)
    (test-vikarana)
    (test-tere)
    (test-derive-pacati)
    (test-derive-bhavati)
    (test-derive-labhate)
    (test-derive-tudati)
    (print "Derivation tests complete.")))
