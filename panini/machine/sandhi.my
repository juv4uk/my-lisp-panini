;; Sandhi Engine — sound combination rules from Aṣṭādhyāyī.
;;
;; Each sandhi rule directly references pratyāhāras that are computed
;; from the Śiva-sūtras by resolve-pratyahara. The sūtra names ARE the
;; pratyāhāras: "iko yaṇ aci" literally means "IK → YAN before AC".
;;
;; Epistemic layer: ENGINEERING
;; Depends on: phonology.my (pratyāhāra predicates)
;; Upstream: SS-PRATYAHARA-001, L-001-001
;;
;; Implemented rules:
;;   6.1.77  iko yaN aci         — IK vowels → YAN semivowels before vowels
;;   8.3.23  mo'nusvāraḥ         — final m → anusvāra (M) before consonants
;;   6.1.88  vṛddhir eco         — (delegated to apply-eco-sandhi in phonology.my)
;;   8.4.55  khari savarṇe       — stop devoicing before voiceless consonants
;;   8.3.59  ādeśapratyayāḥ      — word-initial vowel changes (placeholder)

(load "panini/machine/phonology.my")

;; ==========================================
;; Helper: nth element of a list (0-indexed)
;; ==========================================
(def list-nth
  (lambda (n lst)
    (cond
      ((atom lst) (quote ()))
      ((equal? n 0) (car lst))
      (t (list-nth (- n 1) (cdr lst))))))

;; ==========================================
;; 6.1.77: iko yaN aci
;; "Of IK [i u f x], [the replacement is] YAN [y v r l], before AC [vowels]"
;;
;; When a word ends in an IK vowel and the next word starts with
;; an AC vowel, the final IK vowel is replaced by the corresponding
;; YAN semivowel.
;;
;; The correspondence is by position:
;;   i → y  (1st of IK → 1st of YAN)
;;   u → v  (2nd → 2nd)
;;   f → r  (3rd → 3rd)
;;   x → l  (4th → 4th)
;; ==========================================

;; Find position of a sound in a list (0-indexed)
(def list-position
  (lambda (sound lst)
    (cond
      ((atom lst) (quote ()))
      ((equal? sound (car lst)) 0)
      (t (+ 1 (list-position sound (cdr lst)))))))

;; Map IK sound to corresponding YAN sound by position
(def ik-to-yan
  (lambda (sound)
    (list-nth (list-position sound IK) YAN)))

;; Main rule: apply 6.1.77 if conditions met
(def sandhi-iko-yan-aci
  (lambda (final-sound next-sound)
    (cond
      ((and (in-ik? final-sound) (in-ac? next-sound))
       (ik-to-yan final-sound))
      (t final-sound))))

;; ==========================================
;; 8.3.23: mo'nusvāraḥ
;; "m [at word-end becomes] anusvāra [before HAL consonants]"
;;
;; When a word ends in 'm' and the next word starts with a HAL
;; consonant, m → M (anusvāra).
;; ==========================================

(def sandhi-manusvara
  (lambda (final-sound next-sound)
    (cond
      ((and (equal? final-sound (quote m)) (in-hal? next-sound))
       (quote M))
      (t final-sound))))

;; ==========================================
;; 8.4.55: khari savarṇe (simplified)
;; "[Before] KHAR [voiceless], [a stop] becomes savarṇa [same-class voiceless]"
;;
;; When a voiced stop (JAS or JHASH) is followed by a voiceless
;; consonant (KHAR), it devoices to the corresponding voiceless stop.
;;
;; The mapping is by place of articulation (varga):
;;   j → k, b → p, g → k, q → p, d → t   (JAS → voiceless unaspirated)
;;   J → K, B → P, G → K, Q → P, D → T   (JHASH → voiceless aspirated)
;;
;; Note: this is a simplified version. The full rule involves
;; savarṇa (same-place) matching, which requires a varga table.
;; Here we use explicit mappings for the 5 vargas.
;; ==========================================

(def stop-devoice-map
  (quote ((j . k) (b . p) (g . k) (q . p) (d . t)
          (J . K) (B . P) (G . K) (Q . P) (D . T))))

(def stop-devoice
  (lambda (sound)
    (cdr (assoc sound stop-devoice-map))))

(def sandhi-khari-savarne
  (lambda (final-sound next-sound)
    (cond
      ((and (or (in-jas? final-sound) (in-jhash? final-sound))
            (in-khar? next-sound))
       (stop-devoice final-sound))
      (t final-sound))))

;; ==========================================
;; 8.4.58: jhalāṃ jhaŚi (simplified)
;; "JhaL [consonants] [before] JhaS [voiced stops] → [become voiced]"
;;
;; When a voiceless stop (KHAR member that is also in JAL) is followed
;; by a voiced stop (JAS or JHASH), it voices to the corresponding
;; voiced stop.
;;
;; Reverse of 8.4.55: k→g, p→b, t→d, K→G, P→B, T→D, etc.
;; ==========================================

(def stop-voice-map
  (quote ((k . g) (p . b) (t . d) (c . j) (w . q)
          (K . G) (P . B) (T . D) (C . J) (W . Q))))

(def stop-voice
  (lambda (sound)
    (cdr (assoc sound stop-voice-map))))

(def sandhi-jhalam-jhashi
  (lambda (final-sound next-sound)
    (cond
      ((and (in-khar? final-sound)
            (member? final-sound (quote (k p t c w K P T C W)))
            (or (in-jas? next-sound) (in-jhash? next-sound)))
       (stop-voice final-sound))
      (t final-sound))))

;; ==========================================
;; Combined sandhi application
;;
;; Apply rules in the correct order (later adhyāya rules take
;; precedence per the paribhāṣā "vipratishedhe param kāryam"):
;;   8.4.x > 8.3.x > 8.2.x > 6.1.x
;; ==========================================

(def apply-sandhi
  (lambda (final-sound next-sound)
    (cond
      ;; 8.4.55: devoicing before voiceless (highest priority)
      ((and (or (in-jas? final-sound) (in-jhash? final-sound))
            (in-khar? next-sound))
       (stop-devoice final-sound))
      ;; 8.4.58: voicing before voiced stops
      ((and (in-khar? final-sound)
            (member? final-sound (quote (k p t c w K P T C W)))
            (or (in-jas? next-sound) (in-jhash? next-sound)))
       (stop-voice final-sound))
      ;; 8.3.23: m → anusvāra before consonants
      ((and (equal? final-sound (quote m)) (in-hal? next-sound))
       (quote M))
      ;; 6.1.77: IK → YAN before vowels
      ((and (in-ik? final-sound) (in-ac? next-sound))
       (ik-to-yan final-sound))
      ;; No sandhi applies
      (t final-sound))))

;; ==========================================
;; Word-level sandhi: join two sound-lists
;;
;; Takes two lists of SLP1 sound symbols (word-end and word-start),
;; applies sandhi to the junction, and returns the combined list.
;; ==========================================

(def last-sound
  (lambda (sounds)
    (cond
      ((atom sounds) (quote ()))
      ((atom (cdr sounds)) (car sounds))
      (t (last-sound (cdr sounds))))))

(def but-last-sounds
  (lambda (sounds)
    (cond
      ((atom sounds) (quote ()))
      ((atom (cdr sounds)) (quote ()))
      (t (cons (car sounds) (but-last-sounds (cdr sounds)))))))

(def join-words
  (lambda (word1 word2)
    (cond
      ((atom word1) word2)
      ((atom word2) word1)
      (t
       ((lambda (final next)
          (append (but-last-sounds word1)
                  (cond
                    ((equal? (apply-sandhi final next) final)
                     (cons final word2))
                    ((atom (apply-sandhi final next))
                     (cons (apply-sandhi final next) (cdr word2)))
                    (t
                     (append (apply-sandhi final next) (cdr word2))))))
        (last-sound word1)
        (car word2))))))

;; ==========================================
;; SLP1 symbol → string conversion for display
;; ==========================================

(def symbol-list->string
  (lambda (symbols)
    (cond
      ((atom symbols) "")
      (t (string-append (symbol->string (car symbols))
                        (symbol-list->string (cdr symbols)))))))
