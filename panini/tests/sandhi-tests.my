;; Tests for sandhi engine — all rules verified against Aṣṭādhyāyī examples.

(load "panini/machine/sandhi.my")

(def test-sandhi-iko-yan-aci
  (lambda ()
    ;; 6.1.77: IK vowels → YAN semivowels before AC vowels
    (assert-equal (quote y) (sandhi-iko-yan-aci (quote i) (quote a)) "iko: i+a → y")
    (assert-equal (quote v) (sandhi-iko-yan-aci (quote u) (quote a)) "iko: u+a → v")
    (assert-equal (quote r) (sandhi-iko-yan-aci (quote f) (quote a)) "iko: f+a → r")
    (assert-equal (quote l) (sandhi-iko-yan-aci (quote x) (quote a)) "iko: x+a → l")
    ;; Not triggered: final not in IK
    (assert-equal (quote a) (sandhi-iko-yan-aci (quote a) (quote i)) "iko: a+i → a (not IK)")
    ;; Not triggered: next not vowel
    (assert-equal (quote i) (sandhi-iko-yan-aci (quote i) (quote k)) "iko: i+k → i (not AC)")))

(def test-sandhi-manusvara
  (lambda ()
    ;; 8.3.23: m → M before HAL consonants
    (assert-equal (quote M) (sandhi-manusvara (quote m) (quote k)) "anusvāra: m+k → M")
    (assert-equal (quote M) (sandhi-manusvara (quote m) (quote p)) "anusvāra: m+p → M")
    (assert-equal (quote M) (sandhi-manusvara (quote m) (quote t)) "anusvāra: m+t → M")
    ;; Not triggered: next is vowel
    (assert-equal (quote m) (sandhi-manusvara (quote m) (quote a)) "anusvāra: m+a → m (not HAL)")
    ;; Not triggered: final not m
    (assert-equal (quote n) (sandhi-manusvara (quote n) (quote k)) "anusvāra: n+k → n (not m)")))

(def test-sandhi-khari-savarne
  (lambda ()
    ;; 8.4.55: voiced stops → voiceless before KHAR
    (assert-equal (quote k) (sandhi-khari-savarne (quote g) (quote t)) "khar: g+t → k")
    (assert-equal (quote p) (sandhi-khari-savarne (quote b) (quote s)) "khar: b+s → p")
    (assert-equal (quote K) (sandhi-khari-savarne (quote G) (quote t)) "khar: G+t → K")
    ;; Not triggered: next not voiceless
    (assert-equal (quote g) (sandhi-khari-savarne (quote g) (quote a)) "khar: g+a → g (not KHAR)")
    ;; Not triggered: final not voiced stop
    (assert-equal (quote a) (sandhi-khari-savarne (quote a) (quote t)) "khar: a+t → a (not voiced stop)")))

(def test-sandhi-jhalam-jhashi
  (lambda ()
    ;; 8.4.58: voiceless stops → voiced before JAS/JHASH
    (assert-equal (quote g) (sandhi-jhalam-jhashi (quote k) (quote d)) "jhal: k+d → g")
    (assert-equal (quote b) (sandhi-jhalam-jhashi (quote p) (quote g)) "jhal: p+g → b")
    ;; Not triggered: next not voiced stop
    (assert-equal (quote k) (sandhi-jhalam-jhashi (quote k) (quote a)) "jhal: k+a → k (not JAS)")
    ;; Not triggered: final not voiceless stop
    (assert-equal (quote a) (sandhi-jhalam-jhashi (quote a) (quote d)) "jhal: a+d → a")))

(def test-apply-sandhi-dispatch
  (lambda ()
    ;; Combined dispatch: highest-priority rule wins
    (assert-equal (quote M) (apply-sandhi (quote m) (quote k)) "dispatch: m+k → M (8.3.23)")
    (assert-equal (quote y) (apply-sandhi (quote i) (quote a)) "dispatch: i+a → y (6.1.77)")
    (assert-equal (quote k) (apply-sandhi (quote g) (quote t)) "dispatch: g+t → k (8.4.55)")
    (assert-equal (quote g) (apply-sandhi (quote k) (quote d)) "dispatch: k+d → g (8.4.58)")
    ;; No sandhi
    (assert-equal (quote a) (apply-sandhi (quote a) (quote k)) "dispatch: a+k → a (no sandhi)")))

(def test-join-words
  (lambda ()
    ;; Word-level sandhi: combine two sound-lists
    ;; agni + atra → agnyatra (6.1.77: i+a → y)
    (assert-equal (quote (a g y a w r a))
                  (join-words (quote (a g i)) (quote (a w r a)))
                  "join: agni+atra → agnyatra")
    ;; sam + skṛta → saṃskṛta (8.3.23: m+k → M)
    (assert-equal (quote (s a M s k f t a))
                  (join-words (quote (s a m)) (quote (s k f t a)))
                  "join: sam+skṛta → saṃskṛta")
    ;; No sandhi: pac + ti → pacati (no rule applies at junction)
    (assert-equal (quote (p a c a t i))
                  (join-words (quote (p a c)) (quote (a t i)))
                  "join: pac+ati → pacati (no sandhi)")))

(def test-sandhi-all
  (lambda ()
    (print "Running Sandhi Tests...")
    (test-sandhi-iko-yan-aci)
    (test-sandhi-manusvara)
    (test-sandhi-khari-savarne)
    (test-sandhi-jhalam-jhashi)
    (test-apply-sandhi-dispatch)
    (test-join-words)
    (print "Sandhi tests complete.")))
