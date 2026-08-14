;; SLP1 oracle fixtures — pinned, test-only guix environment.
;; PANINI-GUIX-INDIC-TRANSLITERATION (2026-08-13).
;; NO registry change (my-lisp-panini channels.scm / manifest.scm are
;; untouched) and no oracle-runtime change. This file is a self-contained
;; pinned source for the indic_transliteration v2.3.82 test oracle used by
;; panini/tools/run_indic_transliteration_fixture.py. Build natively with:
;;   guix build -m slp1-fixtures-manifest.scm
;; Run the fixture with:
;;   guix shell -m slp1-fixtures-manifest.scm -- \
;;     python3 tools/run_indic_transliteration_fixture.py <fixture.yml>
(use-modules (guix)
             (guix profiles)
             (guix build-system python)
             (gnu packages python)
             (gnu packages python-build)
             (gnu packages python-xyz)
             ((guix licenses) #:prefix license:))

(define-public python-indic-transliteration
  (package
    (name "python-indic-transliteration")
    (version "2.3.82")
    (source
     (origin
       (method url-fetch)
       (uri (string-append
             "https://files.pythonhosted.org/packages/a2/c1/"
             "65ae96680758615e042415fb1d3a1e573c2419387205135501d96be97bb8/"
             "indic_transliteration-2.3.82-py3-none-any.whl"))
       (sha256
        (base32 "06c00dixkqfwdxalaahpqjkn3nh0lf57x81vq08sih8l9x28lfr4"))))
    (build-system python-build-system)
    (arguments
     (list #:phases
           #~(modify-phases %standard-phases
               (delete 'build)
               (delete 'check)
               (delete 'sanity-check)
               (replace 'install
                 (lambda* (#:key outputs #:allow-other-keys)
                   (let ((out (assoc-ref outputs "out")))
                     (invoke "python" "-m" "pip"
                             "install" "--no-index" "--no-deps"
                             "--prefix" out
                             (string-append (getcwd)
                                            "/indic_transliteration-2.3.82-py3-none-any.whl"))))))))
    (propagated-inputs
     (list python-regex
           python-tqdm
           python-roman
           python-typer
           python-toml))
    (home-page "https://github.com/indic-transliteration/indic_transliteration_py")
    (synopsis "Indic transliteration (SLP1/IAST/Devanagari) test oracle")
    (description
     "Transliteration tools converting text between Indic script encodings
(SLP1, IAST, Devanagari and others). Pinned here strictly as an external
test oracle for panini SLP1 conformance fixtures: MIT-licensed, test-only,
not part of the registry.")
    (license license:expat)))

(packages->manifest
 (list python python-indic-transliteration python-pyyaml))
