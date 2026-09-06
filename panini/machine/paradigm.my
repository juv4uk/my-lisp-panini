;; Paradigm Generator — generate all 9 laṭ parasmaipada forms.
;;
;; Given a dhātu and class number, produces all 9 parasmaipada
;; (and optionally ātmanepada) forms of the present tense (laṭ).
;;
;; This module exercises the full derivation pipeline at scale and
;; honestly documents where the machine succeeds and where it fails.
;;
;; Epistemic layer: ENGINEERING
;; Depends on: derivation.my (full pipeline)

(load "panini/machine/derivation.my")

;; ==========================================
;; Parasmaipada paradigm (9 forms)
;; ==========================================

(def paradigm-para-labels
  (quote (tip tas jhi sip thas tha mip vas mas)))

(def paradigm-para-glosses
  (quote ("3rd sg" "3rd dual" "3rd pl" "2nd sg" "2nd dual" "2nd pl" "1st sg" "1st dual" "1st pl")))

;; Generate one parasmaipada form
(def paradigm-para-form
  (lambda (dhatu class-num ting-label)
    (derive-verb dhatu class-num ting-label (quote ()))))

;; Generate all 9 parasmaipada forms → list of (label . sounds)
(def paradigm-para
  (lambda (dhatu class-num)
    (list
      (cons (quote tip)  (paradigm-para-form dhatu class-num (quote tip)))
      (cons (quote tas)  (paradigm-para-form dhatu class-num (quote tas)))
      (cons (quote jhi)  (paradigm-para-form dhatu class-num (quote jhi)))
      (cons (quote sip)  (paradigm-para-form dhatu class-num (quote sip)))
      (cons (quote thas) (paradigm-para-form dhatu class-num (quote thas)))
      (cons (quote tha)  (paradigm-para-form dhatu class-num (quote tha)))
      (cons (quote mip)  (paradigm-para-form dhatu class-num (quote mip)))
      (cons (quote vas)  (paradigm-para-form dhatu class-num (quote vas)))
      (cons (quote mas)  (paradigm-para-form dhatu class-num (quote mas))))))

;; ==========================================
;; Atmanepada paradigm (9 forms)
;; ==========================================

(def paradigm-atma-labels
  (quote (ta AtAm ja thAs AthAm Dvam iTw vahi mahIM)))

;; Generate one ātmanepada form
(def paradigm-atma-form
  (lambda (dhatu class-num ting-label)
    (derive-verb dhatu class-num ting-label t)))

;; Generate all 9 ātmanepada forms
(def paradigm-atma
  (lambda (dhatu class-num)
    (list
      (cons (quote ta)    (paradigm-atma-form dhatu class-num (quote ta)))
      (cons (quote AtAm)  (paradigm-atma-form dhatu class-num (quote AtAm)))
      (cons (quote ja)    (paradigm-atma-form dhatu class-num (quote ja)))
      (cons (quote thAs)  (paradigm-atma-form dhatu class-num (quote thAs)))
      (cons (quote AthAm) (paradigm-atma-form dhatu class-num (quote AthAm)))
      (cons (quote Dvam)  (paradigm-atma-form dhatu class-num (quote Dvam)))
      (cons (quote iTw)   (paradigm-atma-form dhatu class-num (quote iTw)))
      (cons (quote vahi)  (paradigm-atma-form dhatu class-num (quote vahi)))
      (cons (quote mahIM) (paradigm-atma-form dhatu class-num (quote mahIM))))))

;; ==========================================
;; Full paradigm (both padas)
;; ==========================================

(def paradigm-full
  (lambda (dhatu class-num)
    (list
      (cons (quote parasmaipada) (paradigm-para dhatu class-num))
      (cons (quote atmanepada)  (paradigm-atma dhatu class-num)))))

;; ==========================================
;; Print paradigm (human-readable)
;; ==========================================

(def print-para-paradigm
  (lambda (dhatu class-num)
    (print (string-append "=== parasmaipada ==="))
    (print-para-paradigm-aux
      (paradigm-para dhatu class-num)
      (quote ("3rd sg" "3rd dual" "3rd pl" "2nd sg" "2nd dual" "2nd pl" "1st sg" "1st dual" "1st pl")))))

(def print-para-paradigm-aux
  (lambda (forms glosses)
    (cond
      ((atom forms) (quote ()))
      (t
       (print (string-append
         (car glosses) ": "
         (symbol-list->string (cdr (car forms)))))
       (print-para-paradigm-aux (cdr forms) (cdr glosses))))))

;; ==========================================
;; Known gaps (honest documentation)
;; ==========================================
;;
;; The paradigm generator reveals where the machine is incomplete.
;; These are NOT bugs — they are missing rules, documented honestly.
;;
;; GAP 1: jhi (3rd pl) — produces "pacajhi" instead of "pacanti"
;;   Missing: 8.4.62 (jhaSAm jaS tribhiH) — JhaS consonants replaced
;;   by JaS in 3rd person plural. Also, jhi has complex it-lopa:
;;   the 'i' in jhi is NOT a hal (not final consonant), so it-lopa
;;   gives 'jh' which should become 'j' → then 'anti' not 'ajhi'.
;;   Requires: proper jhi handling + 8.4.62.
;;
;; GAP 2: gam (class 1) — produces "gamati" instead of "gacchati"
;;   Missing: 8.2.30 (m → cch before vowel in specific contexts)
;;   Actually: 7.3.77 (iko'ci) — gam gets guṇa/vṛddhi before vowel,
;;   but the real rule is: gam → gacch (special stem formation)
;;   This is an irregular stem change, not a regular sandhi.
;;
;; GAP 3: labh parasmaipada — produces "labhati" instead of "labhate"
;;   This is NOT a gap — labh simply takes ātmanepada, not parasmaipada.
;;   The machine correctly generates the parasmaipada form; the user
;;   must select the correct pada for the dhātu.
;;
;; GAP 4: ātmanepada AtAm, AthAm — produces "labhaAtA" etc.
;;   These forms need further sandhi/lopa rules:
;;   - AtAm: final m is it → AtA, but the combined form needs
;;     vowel sandhi (a+A → A by 6.1.101)
;;   - iTw: w is it → iT, but iT + labh → labhaiT needs reordering
;;   These are known limitations of the current sandhi engine.
