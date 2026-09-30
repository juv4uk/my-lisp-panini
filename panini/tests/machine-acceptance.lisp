;; Lisp-level acceptance entry point for the Panini machine prototype.
;; Run from repository root with the My Lisp executable as the file argument.

(print "[PANINI-LISP-ACCEPTANCE] start")

;; These loads and run-tests are the real integration boundary.
(load "panini/machine/runtime-prelude.lisp")
(load "panini/machine/compiler.lisp")
(load "panini/machine/meta.lisp")
(load "panini/machine/siva-sutras.lisp")
(load "panini/machine/rules.lisp")
(load "panini/machine/panini-core.lisp")
(load "panini/machine/tests.lisp")
(run-tests)
