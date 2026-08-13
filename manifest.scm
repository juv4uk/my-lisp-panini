;; Guix manifest for my-lisp-panini.
;;
;; Usage:
;;   wsl -u my-lisp-panini
;;   cd /mnt/c/GitHub/my-lisp-panini
;;   guix shell -m manifest.scm --
;;
;; Phase 1 is research/documentation only (see AGENTS.md), so the manifest
;; stays minimal. Extend it as panini-machine-model-v0.1 introduces actual
;; tooling (parsers, Rust, etc.).

(specifications->manifest
 (list "git" "python" "python-pyyaml"))
