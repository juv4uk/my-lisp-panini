; repo.my — Swarm Contract v0.1 scope declaration for my-lisp-panini.
; See my-lisp/docs/swarm-mesh-v2.md for the full spec. Format confirmed
; by example against my-idea/repo.my and fpga-lisp/repo.my.
;
; A declaration of scope, not an authorization grant -- authorities/
; non-authorities state what this repo is and is not the source of
; truth for, so other repos' agents don't have to re-derive it.
;
; Added 2026-08-26 (PANINI-VERIFY-OWN-COORDINATION-DOCS): this header
; was missing even though README.md already cited "Swarm Contract v0.1
; (see repo.my)" -- the repository form below was already correct and
; matches the sibling repos' format, only the declaring comment itself
; was absent, so the README's citation didn't actually resolve to
; anything written here.

(repository
  (id my-lisp-panini)
  (role knowledge-compiler)
  (exports
    panini-claims
    derivations)
  (imports
    shiva-claims)
  (capabilities
    sanskrit
    symbolic-reasoning
    documentation)
  (authorities
    paninian-ontology)
  (non-authorities
    shiva-canon
    my-lisp-runtime
    fpga-hardware))
