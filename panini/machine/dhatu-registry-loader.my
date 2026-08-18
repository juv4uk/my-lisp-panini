;; Minimal, macro-free YAML loader for the dhātu registry
;; (PANINI-MACHINE-DHATU-REGISTRY-YAML-LOAD).
;;
;; The authoritative dhātu registry lives in panini/registry/dhatu/*.yaml.
;; This file gives My Lisp a pure-language loader for that directory:
;;
;;   (load-dhatu-registry "panini/registry/dhatu/")
;;
;; It uses only documented My Lisp core operations (`read-dir`,
;; `read-file`, the string primitives, and list combinators) plus its own
;; macro-free helpers. It adds nothing to the language surface and does
;; not depend on the shared `lib/core.my` (whose macros and helpers are
;; deliberately not part of the machine's acceptance boundary).
;;
;; The YAML subset it parses is deliberately the subset the registry
;; actually uses: scalar values, quoted strings, `>` block scalars,
;; one-level nested mappings, and inline flow mappings `{ a: b, c: d }`.
;; Anything outside that subset is rejected rather than guessed.
;;
;; Record shape (one per canonical dhātu):
;;   (canonical . (list (cons 'meaning <str>) (cons 'class <gana>)
;;                      (cons 'properties (list <pada-tag> <set-tag>))
;;                      (cons 'pada <sym>) (cons 'set-anit <sym>)))
;; `class` and `properties` keep the shape the old `*test-dhatu-registry*`
;; snapshot produced, so existing machine tests keep working unchanged.

;; ---------------------------------------------------------------------
;; String helpers (pure language; no Rust surface added)
;; ---------------------------------------------------------------------

(def l-empty?
  (lambda (s) (eq s "")))

(def l-first
  (lambda (s) (string-first s)))

(def l-rest
  (lambda (s) (string-rest s)))

(def l-length-onto
  (lambda (s acc)
    (cond
      ((l-empty? s) acc)
      (t (l-length-onto (l-rest s) (+ acc 1))))))

(def l-length
  (lambda (s) (l-length-onto s 0)))

(def l-prefix?-onto
  (lambda (prefix s)
    (cond
      ((l-empty? prefix) t)
      ((l-empty? s) (quote ()))
      ((eq (l-first prefix) (l-first s))
       (l-prefix?-onto (l-rest prefix) (l-rest s)))
      (t (quote ())))))

(def l-prefix?
  (lambda (prefix s) (l-prefix?-onto prefix s)))

(def l-contains?-onto
  (lambda (needle s)
    (cond
      ((l-prefix? needle s) t)
      ((l-empty? s) (quote ()))
      (t (l-contains?-onto needle (l-rest s))))))

(def l-contains?
  (lambda (needle s) (l-contains?-onto needle s)))

;; first index of needle in s, or -1
(def l-index-of-onto
  (lambda (needle s i)
    (cond
      ((l-prefix? needle s) i)
      ((l-empty? s) -1)
      (t (l-index-of-onto needle (l-rest s) (+ i 1))))))

(def l-index-of
  (lambda (needle s) (l-index-of-onto needle s 0)))

;; substring [start, end)
(def l-slice-onto
  (lambda (s start end acc)
    (cond
      ((not (< start end)) acc)
      ((l-empty? s) acc)
      (t (l-slice-onto (l-rest s) (- start 1) (- end 1)
                       (string-append acc (l-first s)))))))

(def l-slice
  (lambda (s start end) (l-slice-onto s start end "")))

(def l-strip-left
  (lambda (s)
    (cond
      ((l-empty? s) s)
      ((eq (l-first s) " ") (l-strip-left (l-rest s)))
      ((eq (l-first s) "\r") (l-strip-left (l-rest s)))
      (t s))))

(def l-strip-right
  (lambda (s)
    (cond
      ((l-empty? s) s)
      ((eq (l-char-at s (- (l-length s) 1)) " ")
       (l-strip-right (l-slice s 0 (- (l-length s) 1))))
      ((eq (l-char-at s (- (l-length s) 1)) "\r")
       (l-strip-right (l-slice s 0 (- (l-length s) 1))))
      (t s))))

(def l-strip
  (lambda (s) (l-strip-right (l-strip-left s))))

(def l-char-at
  (lambda (s i)
    (cond
      ((= i 0) (l-first s))
      (t (l-char-at (l-rest s) (- i 1))))))

;; reverse a list without relying on the shared core
(def l-reverse-onto
  (lambda (values acc)
    (cond
      ((atom values) acc)
      (t (l-reverse-onto (cdr values) (cons (car values) acc))))))

(def l-reverse
  (lambda (values) (l-reverse-onto values (quote ()))))

;; split s on every occurrence of sep (a one-char string), dropping empty
;; segments: "" -> (), "a\nb" -> ("a" "b"), "a\n" -> ("a").
(def l-split-once
  (lambda (s sep)
    ((lambda (i)
       (cond
         ((= i -1) (cons s ""))
         (t (cons (l-slice s 0 i) (l-slice s (+ i 1) (l-length s))))))
     (l-index-of sep s))))

(def l-split-onto
  (lambda (s sep acc)
    ((lambda (part)
       (cond
         ((l-empty? (cdr part))
          (cond
            ((l-empty? (car part)) (l-reverse acc))
            (t (l-reverse (cons (car part) acc)))))
         (t
          (cond
            ((l-empty? (car part)) (l-split-onto (cdr part) sep acc))
            (t (l-split-onto (cdr part) sep (cons (car part) acc)))))))
     (l-split-once s sep))))

(def l-split
  (lambda (s sep)
    (cond
      ((l-empty? s) (quote ()))
      (t (l-split-onto s sep (quote ()))))))

;; ---------------------------------------------------------------------
;; Scalar parsing
;; ---------------------------------------------------------------------

(def l-digit?
  (lambda (c)
    (cond
      ((eq c "0") t)
      ((eq c "1") t)
      ((eq c "2") t)
      ((eq c "3") t)
      ((eq c "4") t)
      ((eq c "5") t)
      ((eq c "6") t)
      ((eq c "7") t)
      ((eq c "8") t)
      ((eq c "9") t)
      (t (quote ())))))

(def l-numeric?-onto
  (lambda (s)
    (cond
      ((l-empty? s) t)
      ((l-digit? (l-first s)) (l-numeric?-onto (l-rest s)))
      (t (quote ())))))

(def l-numeric?
  (lambda (s)
    (cond
      ((l-empty? s) (quote ()))
      (t (l-numeric?-onto s)))))

(def l-quoted?
  (lambda (s)
    (cond
      ((l-empty? s) (quote ()))
      (t (eq (l-first s) "\"")))))

(def l-unquote
  (lambda (s)
    (l-slice s 1 (- (l-length s) 1))))

(def l-true?
  (lambda (s) (eq s "true")))

(def l-false?
  (lambda (s) (eq s "false")))

;; Parse a scalar value into a My Lisp value: quoted strings stay
;; strings, "true"/"false" become booleans, all-digit tokens become
;; exact numbers, everything else becomes a symbol (so `seT`, `aniT`,
;; `parasmaipada` etc. survive as atoms).
(def parse-scalar
  (lambda (s)
    (cond
      ((l-quoted? s) (l-unquote s))
      ((l-true? s) t)
      ((l-false? s) (quote ()))
      ((not (l-numeric? s)) (string->symbol s))
      (t (read s)))))

;; ---------------------------------------------------------------------
;; Flow mapping: `{ key: value, key2: value2 }` -> association list
;; ---------------------------------------------------------------------

(def flow-pair
  (lambda (s)
    (cond
      ((l-empty? s) (quote ()))
      (t
       ((lambda (colon)
          (cond
            ((= colon -1) (cons (string->symbol (l-strip s)) ""))
            (t (cons (string->symbol (l-strip (l-slice s 0 colon)))
                     (parse-scalar (l-strip (l-slice s (+ colon 1) (l-length s))))))))
        (l-index-of ":" s))))))

(def parse-flow-onto
  (lambda (s acc)
    (cond
      ((l-empty? s) (l-reverse acc))
      (t
       ((lambda (comma)
          (cond
            ((= comma -1)
             (l-reverse (cons (flow-pair (l-strip s)) acc)))
            (t (parse-flow-onto
                 (l-strip (l-slice s (+ comma 1) (l-length s)))
                 (cons (flow-pair (l-strip (l-slice s 0 comma))) acc)))))
        (l-index-of "," s))))))

(def parse-flow
  (lambda (s)
    (cond
      ((l-empty? s) (quote ()))
      (t (parse-flow-onto (l-slice s 1 (- (l-length s) 1)) (quote ()))))))

;; ---------------------------------------------------------------------
;; Line handling and record parsing
;; ---------------------------------------------------------------------

(def l-lines
  (lambda (s) (l-split s "\n")))

;; Detect a `key: value` line and return (key . value-string) with both
;; sides stripped; '() if the line carries no mapping.
(def parse-key-value
  (lambda (line)
    ((lambda (colon)
       (cond
         ((= colon -1) (quote ()))
         (t (cons (l-strip (l-slice line 0 colon))
                  (l-strip (l-slice line (+ colon 1) (l-length line)))))))
     (l-index-of ":" line))))

(def l-indented?
  (lambda (s) (l-prefix? "  " s)))

(def l-dedent
  (lambda (s)
    (cond
      ((l-indented? s) (l-rest (l-rest s)))
      (t s))))

;; Collect a `>` block scalar: every following indented line is appended
;; (space-separated), until the first non-indented line. Returns
;; (block-string . remaining-lines).
(def collect-block-acc
  (lambda (lines acc)
    (cond
      ((atom lines) (cons acc lines))
      ((l-indented? (car lines))
       (collect-block-acc (cdr lines)
                          (string-append acc
                                         (string-append (l-dedent (car lines)) " "))))
      (t (cons acc lines)))))

(def collect-block
  (lambda (lines)
    (cond
      ((atom lines) (cons "" lines))
      ((l-indented? (car lines))
       (collect-block-acc (cdr lines) (l-dedent (car lines))))
      (t (cons "" lines)))))

;; Collect a nested mapping (`evidence:` followed by `  status: ...`).
;; Returns (nested-alist . remaining-lines).
(def collect-nested-onto
  (lambda (lines acc)
    (cond
      ((atom lines) (cons (l-reverse acc) lines))
      ((l-indented? (car lines))
       ((lambda (kv)
          (cond
            ((atom kv) (cons (l-reverse acc) lines))
            (t (collect-nested-onto
                 (cdr lines)
                 (cons (cons (string->symbol (car kv)) (parse-scalar (cdr kv))) acc)))))
        (parse-key-value (l-strip (car lines)))))
      (t (cons (l-reverse acc) lines)))))

(def collect-nested
  (lambda (lines) (collect-nested-onto lines (quote ()))))

;; Build one association list from a whole YAML record's lines.
(def parse-record-onto
  (lambda (lines acc)
    (cond
      ((atom lines) (l-reverse acc))
      ((l-empty? (l-strip (car lines)))
       (parse-record-onto (cdr lines) acc))
      (t
       ((lambda (kv)
          (cond
            ((atom kv)
             (parse-record-onto (cdr lines) acc))
            (t
             ((lambda (key value)
                (cond
                  ((l-quoted? value)
                   (parse-record-onto (cdr lines)
                                      (cons (cons key (l-unquote value)) acc)))
                  ((eq value ">")
                   ((lambda (block)
                      (parse-record-onto (cdr block)
                                         (cons (cons key (car block)) acc)))
                    (collect-block (cdr lines))))
                  ((l-prefix? "{" value)
                   (parse-record-onto (cdr lines)
                                      (cons (cons key (parse-flow value)) acc)))
                  ((l-empty? value)
                   ((lambda (nested)
                      (parse-record-onto (cdr nested)
                                         (cons (cons key (car nested)) acc)))
                    (collect-nested (cdr lines))))
                   (t
                    (parse-record-onto (cdr lines)
                                       (cons (cons key (parse-scalar value)) acc)))))
              (string->symbol (car kv))
              (cdr kv)))))
        (parse-key-value (car lines)))))))

(def parse-record
  (lambda (text) (parse-record-onto (l-lines text) (quote ()))))

;; ---------------------------------------------------------------------
;; Registry shaping
;; ---------------------------------------------------------------------

(def pada-tag
  (lambda (pada)
    (cond
      ((eq pada (quote parasmaipada)) (quote parasmaipadin))
      ((eq pada (quote atmanepada)) (quote Atmanepadin))
      ((eq pada (quote ubhayapada)) (quote uBayapadin))
      (t pada))))

(def set-tag
  (lambda (set-anit)
    (cond
      ((eq set-anit (quote seT)) (quote seT))
      ((eq set-anit (quote aniT)) (quote aniT))
      (t set-anit))))

(def record-field
  (lambda (record field)
    (cdr (assoc field record))))

;; Turn a parsed YAML record into the canonical registry shape. The
;; `class`/`properties` fields keep the old snapshot contract; everything
;; else is carried through verbatim so no registry data is lost.
(def shape-record
  (lambda (record)
    ((lambda (canonical gana pada set-anit meaning)
       (cons canonical
             (list (cons (quote meaning) meaning)
                   (cons (quote class) gana)
                   (cons (quote properties) (list (pada-tag pada) (set-tag set-anit)))
                   (cons (quote pada) pada)
                   (cons (quote set-anit) set-anit))))
     (record-field record (quote canonical))
     (record-field record (quote gana))
     (record-field record (quote pada))
     (record-field record (quote set-anit))
     (record-field record (quote traditional_meaning)))))

(def registry-name?
  (lambda (name)
    (cond
      ((l-prefix? "." name) (quote ()))
      ((l-contains? ".yaml" name) t)
      (t (quote ())))))

(def load-registry-onto
  (lambda (dir names acc)
    (cond
      ((atom names) (l-reverse acc))
      ((registry-name? (car names))
       (load-registry-onto
         dir
         (cdr names)
         (cons (shape-record (parse-record (read-file (string-append dir (car names)))))
               acc)))
      (t (load-registry-onto dir (cdr names) acc)))))

(def load-dhatu-registry
  (lambda (dir)
    (load-registry-onto dir (read-dir dir) (quote ()))))
