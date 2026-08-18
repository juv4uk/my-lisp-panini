;; Panini Machine Model v0.1
;; Core Definitions for the Symbolic Virtual Machine
;; All identifiers strictly use SLP1 encoding.

;; ==========================================
;; Kāraka (Semantic Roles / Edges)
;; ==========================================
;; These represent the typed edges in our semantic graph AST.
(def karaka-registry
  (list
    (cons (quote apAdAna)    (list (cons (quote sutra) "1.4.24") (cons (quote semantic-role) (quote source))))
    (cons (quote sampradAna) (list (cons (quote sutra) "1.4.32") (cons (quote semantic-role) (quote recipient))))
    (cons (quote karaRa)     (list (cons (quote sutra) "1.4.42") (cons (quote semantic-role) (quote instrument))))
    (cons (quote aDikaraRa)  (list (cons (quote sutra) "1.4.45") (cons (quote semantic-role) (quote location))))
    (cons (quote karman)     (list (cons (quote sutra) "1.4.49") (cons (quote semantic-role) (quote patient))))
    (cons (quote kartf)      (list (cons (quote sutra) "1.4.54") (cons (quote semantic-role) (quote agent))))))

;; Helper to fetch a karaka's property
(def get-karaka
  (lambda (k-id prop)
    (cdr (assoc prop (cdr (assoc k-id karaka-registry))))))

;; ==========================================
;; Dhātu (Action / Operator Nodes)
;; ==========================================
;; AUTHORITATIVE SOURCE: panini/registry/dhatu/*.yaml (20 verified entries).
;;
;; The authoritative registry is YAML-based (registry/dhatu/*.yaml).
;; When My Lisp gains YAML/file I/O, this should be replaced by:
;;   (load-dhatu-registry "/mnt/c/GitHub/my-lisp-panini/panini/registry/dhatu/")
;;
;; *test-dhatu-registry* is a SNAPSHOT for smoke-tests only.
;; It is NOT an authoritative source. Do NOT add entries here;
;; add them to registry/dhatu/*.yaml instead.
;; See: PANINI-MACHINE-DHATU-REGISTRY-SINGLE-SOURCE
(load "panini/machine/yaml-parser.my")
(def *test-dhatu-registry* (load-dhatu-registry "panini/registry/dhatu"))
(def dhatu-registry *test-dhatu-registry*)

;; ==========================================
;; Graph Modeling (Action Instantiation)
;; ==========================================
;; An action instance represents a dhātu with its kāraka arguments.
;;
;; FIXED (PANINI-MACHINE-FIXUP-ACTION-GRAPH-ARITY):
;; Previous version had fixed arity (kartf, karman) — rejected by
;; dhatu-karaka-relation.md: kāraka set depends on the sentence,
;; not on dhātu alone (e.g. pac may or may not have aDikaraRa).
;;
;; karaka-pairs is an a-list of (kAraka-id . entity) pairs.
;; Any subset of the six kāraka roles is valid:
;;   kartf, karman, karaRa, sampradAna, apAdAna, aDikaraRa
;;
;; [MY-LISP HYPOTHESIS] — graph edge model, see hypothesis-ledger.md H1
(def make-action-graph
  (lambda (action-id dhatu karaka-pairs)
    (list (cons (quote action-id) action-id)
          (cons (quote dhAtu) dhatu)
          (cons (quote kAraka-args) karaka-pairs))))

;; Helper: get a kāraka entity from an action-graph
(def action-get-karaka
  (lambda (ag k-id)
    (cdr (assoc k-id (cdr (assoc (quote kAraka-args) ag))))))

;; ==========================================
;; Situated kAraka membership
;; ==========================================
;; [MACHINE] This bounded record keeps situation, participant, provenance, and
;; epistemic status explicit for a situated designation claim.
;;
;; [INTERPRETATION] It does not assert a permanent dhAtu/participant property,
;; identify kartf with a modern "agent" label, or create graph-edge semantics.
;; See research/semantic-grounding.md and hypothesis-ledger.md H1.
(def make-karaka-membership
  (lambda (situation-id karaka-id participant provenance status)
    (list (cons (quote kind) (quote karaka-membership))
          (cons (quote situation) situation-id)
          (cons (quote karaka) karaka-id)
          (cons (quote participant) participant)
          (cons (quote provenance) provenance)
          (cons (quote status) status))))

(def karaka-membership-field
  (lambda (membership field)
    (cdr (assoc field membership))))

;; Example only: the designation is scoped to this asserted situation. Neither
;; devadatta nor pac receives a global or fixed semantic role from this record.
(def example-pac-kartf-membership
  (make-karaka-membership (quote situation-pac-01) (quote kartf) (quote devadatta)
                          (quote prov:example:pacati) (quote needs-check)))

;; Example 1: "devadatta goes to the village" — kartf + karman only
(def example-gam
  (make-action-graph (quote action-gam) (quote gam)
    (list (cons (quote kartf) (quote devadatta))
          (cons (quote karman) (quote grAma)))))

;; Example 2: "devadatta cooks rice in the pot" — kartf + karman + aDikaraRa
;; (sTAlyAM pacati odanam — the canonical 3-kAraka pac example)
(def example-pac-full
  (make-action-graph (quote action-pac) (quote pac)
    (list (cons (quote kartf) (quote devadatta))
          (cons (quote karman) (quote odana))
          (cons (quote aDikaraRa) (quote sTAlI)))))

