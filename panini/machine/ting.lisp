;; Tiṅ system — 18 endings + vikaraṇa table + it-lopa + lakāra.
;;
;; Epistemic layer: PĀṆINIAN FORMAL USE + ENGINEERING
;; Depends on: phonology.my
;; Sources: Aṣṭādhyāyī 3.1.68-81, 3.4.77-85, Kāśikā on 3.1.73

(load "panini/machine/phonology.my")

;; ==========================================
;; Tiṅ endings — laṭ (present, 3.4.77-70)
;; SLP1 encoding
;; ==========================================

(def ting-para-raw
  (quote ((tip . (t i p))    ;; 3rd sg
          (tas . (t a s))    ;; 3rd dual
          (jhi . (J i))      ;; 3rd pl
          (sip . (s i p))    ;; 2nd sg
          (thas . (t h a s)) ;; 2nd dual
          (tha . (t h a))    ;; 2nd pl
          (mip . (m i p))    ;; 1st sg
          (vas . (v a s))    ;; 1st dual
          (mas . (m a s))))) ;; 1st pl

(def ting-atma-raw
  (quote ((ta . (t a))         ;; 3rd sg
          (AtAm . (A t A m))   ;; 3rd dual
          (ja . (j a))         ;; 3rd pl
          (thAs . (t h A s))   ;; 2nd sg
          (AthAm . (A t h A m));; 2nd dual
          (Dvam . (D v a m))   ;; 2nd pl
          (iTw . (i T w))      ;; 1st sg
          (vahi . (v a h i))   ;; 1st dual
          (mahIM . (m a h I M))))) ;; 1st pl

;; ==========================================
;; Tiṅ endings — loṭ (imperative, 3.4.85-89)
;;
;; loṭ tiṅ differ from laṭ:
;;   3sg: tip → tu (3.4.88)
;;   3du: tas → tām
;;   3pl: jhi → ntu (i→u change)
;;   2sg: sip → hi → lopa (zero ending)
;;   2du: thas → tam
;;   2pl: tha → ta
;;   1sg: mip → ani (3.4.89)
;;   1du: vas → ava
;;   1pl: mas → ama
;;
;; Pre-cleaned (no hal-lopa needed, no jhi→nti needed)
;; ==========================================

(def lot-ting-para
  (quote ((tip . (t u))       ;; 3sg: tu
          (tas . (t A m))     ;; 3du: tām
          (jhi . (n t u))     ;; 3pl: ntu
          (sip . ())           ;; 2sg: zero (hi → lopa)
          (thas . (t a m))    ;; 2du: tam
          (tha . (t a))        ;; 2pl: ta
          (mip . (a n i))     ;; 1sg: ani
          (vas . (a v a))     ;; 1du: ava
          (mas . (a m a)))))  ;; 1pl: ama

;; ==========================================
;; 1.3.3: hal antyam — last sound if hal → it
;; 1.3.4: na vibhaktau tusmāḥ — t,u,s,m at end (not vibhakti) → it
;; 1.3.5: ādir ñiṭuḍavaḥ — initial ñ,ṭ,ḍ → it
;; 1.3.9: tasya lopaḥ — it sounds are deleted
;; ==========================================

(def remove-it-markers
  (lambda (sounds it-markers)
    (cond
      ((atom sounds) (quote ()))
      ((member (car sounds) it-markers)
       (remove-it-markers (cdr sounds) it-markers))
      (t (cons (car sounds)
               (remove-it-markers (cdr sounds) it-markers))))))

;; 8.2.66 + 8.4.62: jhi → nti (J→n, then voiced→voiceless before khar not needed here)
(def apply-jhi-adesha
  (lambda (ting-label ting-clean)
    (cond
      ((equal? ting-label (quote jhi)) (quote (n t i)))
      (t ting-clean))))

;; ==========================================
;; Vikaraṇa table (ALL 10 CLASSES, SLP1-corrected)
;;
;; Sources: Aṣṥādhyāyī 3.1.68-81
;;   3.1.68: Śap (class 1)
;;   3.1.69: ŚyaN (class 4)
;;   3.1.73: Śnu (class 5) — Kāśikā: "śapo 'pavādaḥ / sunoti"
;;   3.1.77: Śa (class 6)
;;   3.1.78: ŚnāM (class 7) — M=anusvāra is it
;;   3.1.79: u (class 8) — plain "u", NOT "Śu"!
;;   3.1.81: Śnā (class 9)
;;   3.1.25: Ṇic (class 10)
;;
;; Key: Śnu's u is NOT it (only ś). Class 8 uses plain "u".
;; ==========================================

(def vikarana-table
  (quote (
    (1  . ((z a p)   (z p)))      ;; Śap → a; ś,p = it
    (2  . (()        ()))          ;; no vikaraṇa (adhātuka)
    (4  . ((z y a)   (z)))         ;; Śya → ya; ś = it
    (5  . ((z n u)   (z)))         ;; Śnu → nu; ś = it (u stays!)
    (6  . ((z a)     (z)))         ;; Śa → a; ś = it
    (7  . ((z n A)   (z A)))       ;; Śnā(M) → nā; ś,ā = it (M not encoded)
    (8  . ((u)       ()))          ;; u →0u; no it (3.1.79: plain "u")
    (9  . ((z n A)   (z A)))       ;; Śnā → nā; ś,ā = it
    (10 . ((R i c)   (R c))))))    ;; Ṇic → i; ṇ,c = it

(def get-vikarana
  (lambda (class-num)
    (car (cdr (assoc class-num vikarana-table)))))

(def get-vikarana-it-markers
  (lambda (class-num)
    (car (cdr (cdr (assoc class-num vikarana-table))))))

;; ṭit check: which classes trigger guṇa (7.3.84)?
;; Class 1:  Śap — ṭit (tradition), guṇa on dhātu vowel
;; Class 4:  Śya — NOT ṭit, no guṇa
;; Class 5:  Śnu — ṭit, guṇa/yaṇ on vikaraṇa vowel (Journal 0018)
;; Class 6:  Śa  — NOT ṭit, no guṇa
;; Class 7:  Śnā — ṭit (guṇa, but nā is complex — deferred)
;; Class 8:  u   — ṭit (ārdhadhātuka, 7.3.84 applies)
;; Class 9:  Śnā — ṭit (deferred)
;; Class 10: Ṇic — ṇiṭ, guṇa on ALL vowels of aṅga (Journal 0017)
(def vikarana-has-tit?
  (lambda (class-num)
    (cond
      ((equal? class-num 1) t)
      ((equal? class-num 4) (quote ()))
      ((equal? class-num 5) t)
      ((equal? class-num 6) (quote ()))
      ((equal? class-num 7) t)
      ((equal? class-num 8) t)
      ((equal? class-num 9) t)
      ((equal? class-num 10) t)
      (t (quote ())))))

;; Śnu/Śu classes: 5, 8 (special guṇa/yaṇ handling, 6.4.87)
(def is-snu-class?
  (lambda (class-num)
    (cond
      ((equal? class-num 5) t)
      ((equal? class-num 8) t)
      (t (quote ())))))

;; Class 10 special: Ṇic "i" becomes part of the AṄGA
(def is-nic-class?
  (lambda (class-num)
    (equal? class-num 10)))

(def get-vikarana-clean
  (lambda (class-num)
    (remove-it-markers
      (get-vikarana class-num)
      (get-vikarana-it-markers class-num))))

;; ==========================================
;; Lakāra dispatch: get tiṅ by lakāra
;; ==========================================

;; laṭ: raw tiṅ with hal-lopa + jhi→nti
(def get-lat-ting-para
  (lambda (ting-label)
    (apply-jhi-adesha
      ting-label
      (remove-hal-antyam
        (cdr (assoc ting-label ting-para-raw))))))

;; loṭ: pre-cleaned tiṅ (no processing needed)
(def get-lot-ting-para
  (lambda (ting-label)
    (cdr (assoc ting-label lot-ting-para))))

;; laṅ tiṅ (imperfect, 3.2.111 + 3.4.78):
;; DIFFERENT from laṭ! No final -i, 3pl=n (not nti), 1sg=m (not mi).
;; These are the laṅ-specific endings (verified 15/15 = 100%).
;;
;; 3sg: tip → t (not ti!)
;; 3du: tas → tām
;; 3pl: jhi → n (not nti!)
;; 2sg: sip → s
;; 2du: thas → tam
;; 2pl: tha → ta
;; 1sg: mip → m (not mi!)
;; 1du: vas → va
;; 1pl: mas → ma

(def lan-ting-para
  (quote ((tip . (t))         ;; 3sg: t
          (tas . (t A m))     ;; 3du: tām
          (jhi . (n))          ;; 3pl: n (NOT nti!)
          (sip . (s))          ;; 2sg: s
          (thas . (t a m))    ;; 2du: tam
          (tha . (t a))        ;; 2pl: ta
          (mip . (m))          ;; 1sg: m (NOT mi!)
          (vas . (v a))        ;; 1du: va
          (mas . (m a)))))    ;; 1pl: ma

(def get-laN-ting-para
  (lambda (ting-label)
    (cdr (assoc ting-label lan-ting-para))))

;; Generic: get tiṅ by lakāra
(def get-ting-para
  (lambda (ting-label lakara)
    (cond
      ((equal? lakara (quote loT))
       (get-lot-ting-para ting-label))
      ((equal? lakara (quote laN))
       (get-laN-ting-para ting-label))
      (t
       ;; laṭ (default)
       (apply-jhi-adesha
         ting-label
         (remove-hal-antyam
           (cdr (assoc ting-label ting-para-raw))))))))

;; Helper: remove last sound if hal (1.3.3)
(def remove-hal-antyam
  (lambda (sounds)
    (cond
      ((atom sounds) (quote ()))
      ((atom (cdr sounds))
       (cond
         ((in-hal? (car sounds)) (quote ()))
         (t sounds)))
      (t (cons (car sounds) (remove-hal-antyam (cdr sounds)))))))



;; ==========================================
;; Tiṅ endings — liṅ (optative, 3.4.107-112)
;;
;; Architecture: optative REPLACES vikaraṇa entirely.
;; The marker sī replaces the laṭ vikaraṇa.
;; Two ending types based on aṅga-final vowel:
;;   e-type: a-final aṅga (classes 1, 4, 6, 10)
;;   yā-type: u-final aṅga (classes 5, 8)
;;
;; Pre-computed (verified 15/15 = 100%, Journal 0024)
;; ==========================================

;; e-type endings (for a-final aṅga)
(def lin-ting-para
  (quote ((tip . (e t))              ;; 3sg: et
          (tas . (e y A t a m))      ;; 3du: eyātam
          (jhi . (e y u s))          ;; 3pl: eyus
          (sip . (e s))              ;; 2sg: es
          (thas . (e s t A m))       ;; 2du: estām
          (tha . (e s t a))          ;; 2pl: esta
          (mip . (e y a m))          ;; 1sg: eyam
          (vas . (e v a))            ;; 1du: eva
          (mas . (e m a)))))         ;; 1pl: ema

;; yā-type endings (for u-final aṅga, classes 5/8)
(def lin-ting-snu
  (quote ((tip . (y A t))            ;; 3sg: yāt
          (tas . (y A t A m))        ;; 3du: yātām
          (jhi . (y u s))            ;; 3pl: yus
          (sip . (y A s))            ;; 2sg: yās
          (thas . (y A s t A m))     ;; 2du: yāstām
          (tha . (y A s t a))        ;; 2pl: yāsta
          (mip . (y A m))            ;; 1sg: yām
          (vas . (y A v a))          ;; 1du: yāva
          (mas . (y A m a h i)))))   ;; 1pl: yāmahi

;; ==========================================
;; Ātmanepada laṭ tiṅ — ṭere ādeśa (3.4.79)
;;
;; When vikaraṇa has ṭit: wholesale replacement (ādeśa)
;; ta→te, ātām→etām, ja→anta, thās→se, āthām→ethām,
;; dhvam→dhve, iṭ→e, vahi→āvahe, mahīṃ→āmahe
;;
;; Pre-computed (verified 12/12 = 100%, Journal 0025)
;; ==========================================

(def lat-atma-ting-tit
  (quote ((ta . (t e))               ;; 3sg: te
          (AtAm . (e t A m))         ;; 3du: etām
          (ja . (a n t a))           ;; 3pl: anta
          (thAs . (s e))             ;; 2sg: se
          (AthAm . (e t h A m))      ;; 2du: ethām
          (Dvam . (D v e))           ;; 2pl: dhve
          (iTw . (e))                ;; 1sg: e
          (vahi . (A v a h e))       ;; 1du: āvahe
          (mahIM . (A m a h e)))))   ;; 1pl: āmahe

;; ==========================================
;; Ātmanepada tiṅ dispatch
;; ==========================================

;; laṭ ātmanepada: use ṭere table when ṭit, raw+hal-lopa otherwise
(def get-lat-ting-atma
  (lambda (ting-label has-tit)
    (cond
      (has-tit
       (cdr (assoc ting-label lat-atma-ting-tit)))
      (t
       ;; Non-ṭit: raw endings with hal-lopa
       (remove-hal-antyam
         (cdr (assoc ting-label ting-atma-raw))))))

;; Generic ātmanepada dispatch by lakāra
(def get-ting-atma
  (lambda (ting-label lakara has-tit)
    (cond
      ((equal? lakara (quote laT))
       (get-lat-ting-atma ting-label has-tit))
      (t
       ;; loṭ/laṅ/liṅ ātmanepada: deferred
       (get-lat-ting-atma ting-label has-tit)))))

;; ==========================================
;; liṅ tiṅ dispatch
;; ==========================================

(def get-lin-ting-para
  (lambda (ting-label is-snu)
    (cond
      (is-snu
       (cdr (assoc ting-label lin-ting-snu)))
      (t
       (cdr (assoc ting-label lin-ting-para))))))

;; ==========================================
;; Updated generic dispatch: get tiṅ by lakāra
;; ==========================================

(def get-ting-para-v2
  (lambda (ting-label lakara is-snu)
    (cond
      ((equal? lakara (quote loT))
       (get-lot-ting-para ting-label))
      ((equal? lakara (quote laN))
       (get-laN-ting-para ting-label))
      ((equal? lakara (quote liN))
       (get-lin-ting-para ting-label is-snu))
      ((equal? lakara (quote lRw))
       ;; lṛṭ uses SAME tiṅ as laṭ (3.4.77: lasya)
       (apply-jhi-adesha
         ting-label
         (remove-hal-antyam
           (cdr (assoc ting-label ting-para-raw)))))
      (t
       ;; laṭ (default)
       (apply-jhi-adesha
         ting-label
         (remove-hal-antyam
           (cdr (assoc ting-label ting-para-raw))))))))

;; ==========================================
;; 3.4.79: ṭere — FULL ādeśa (updated)
;;
;; Original: only ta→te
;; Updated: dispatches to pre-computed ṭere table
;; ==========================================

(def apply-tere-full
  (lambda (ting-label has-tit is-atmanepada)
    (cond
      ((and is-atmanepada has-tit)
       (cdr (assoc ting-label lat-atma-ting-tit)))
      (t
       ;; Return nil to signal "no ṭere applied"
       (quote ())))))


;; ==========================================
;; 3.4.79: ṭere
;; ==========================================

(def apply-tere
  (lambda (ting-clean has-tit is-atmanepada)
    (cond
      ((and is-atmanepada has-tit (equal? ting-clean (quote (t a))))
       (quote (t e)))
      (t ting-clean))))
