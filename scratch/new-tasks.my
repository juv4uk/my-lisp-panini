;; Задачі на основі огляду проекту my-lisp-panini-1
;; 2026-08-13 — додано як наслідок project-review.md

((tasks . (

  ;; =============================================
  ;; CRITICAL FIXES — технічний борг з gate-review
  ;; =============================================

  ("PANINI-MACHINE-FIXUP-ACTION-GRAPH-ARITY" . (
    (priority . 10.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PANINI-MACHINE-DHATU-REGISTRY-SINGLE-SOURCE" . (
    (priority . 9.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-FIXUP-ACTION-GRAPH-ARITY"))
    (done . ())
  ))

  ("PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST" . (
    (priority . 9.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-DHATU-REGISTRY-SINGLE-SOURCE"))
    (done . ())
  ))

  ;; =============================================
  ;; TESTING — мінімальні smoke-тести
  ;; =============================================

  ("PANINI-MACHINE-APPLY-GUNA-SMOKE-TEST" . (
    (priority . 8.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PANINI-BRIDGE-MY-LISP-SYNTAX-CONVERSION" . (
    (priority . 8.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-APPLY-GUNA-SMOKE-TEST"))
    (done . ())
  ))

  ("PANINI-MACHINE-DERIVE-BAVATI-EXECUTION" . (
    (priority . 7.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-BRIDGE-MY-LISP-SYNTAX-CONVERSION"))
    (done . ())
  ))

  ("PANINI-MACHINE-TESTS-MY-EXECUTION" . (
    (priority . 7.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-DERIVE-BAVATI-EXECUTION"))
    (done . ())
  ))

  ;; =============================================
  ;; ARCHITECTURE — архітектурні дослідження
  ;; =============================================

  ("PANINI-ANUVRTTI-GRAPH-REPR-VS-DYNAMIC-BINDING" . (
    (priority . 8.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PANINI-VIPRATISEDA-AS-FALLBACK-VERIFICATION" . (
    (priority . 7.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST"))
    (done . ())
  ))

  ("PANINI-TRIPADI-SCOPE-INVESTIGATION" . (
    (priority . 6.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PANINI-PARIBHASA-DEFMACRO-REAL-CONFLICT-TEST" . (
    (priority . 7.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST"))
    (done . ())
  ))

  ("PANINI-ADHIKARA-SCOPE-BOUNDARY-FROM-TEXT" . (
    (priority . 6.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-TRIPADI-SCOPE-INVESTIGATION"))
    (done . ())
  ))

  ("PANINI-MACHINE-RULE-DAG-ANUVRTTI-EDGES" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-ANUVRTTI-GRAPH-REPR-VS-DYNAMIC-BINDING"))
    (done . ())
  ))

  ;; =============================================
  ;; PHILOSOPHY — недооцінені філософські задачі
  ;; =============================================

  ("PANINI-SAMJNA-AS-CATEGORIZATION-NOT-JUST-TAG" . (
    (priority . 8.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PHILOSOPHY-SAMANYA-VISESA-ONTOLOGY" . (
    (priority . 7.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PANINI-TWO-INSTANCE-RELATIONSHIP-RESEARCH" . (
    (priority . 7.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PHILOSOPHY-SAMANYA-VISESA-ONTOLOGY"))
    (done . ())
  ))

  ("PHILOSOPHY-SPHOTA-AND-EXPR-IDENTITY" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PHILOSOPHY-SEMANTIC-GROUNDING" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PHILOSOPHY-SAMANYA-VISESA-ONTOLOGY"))
    (done . ())
  ))

  ("PHILOSOPHY-DHATU-PURITY-AND-KRIYA" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PHILOSOPHY-MACHINE-UNDERSTANDING" . (
    (priority . 5.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PHILOSOPHY-SEMANTIC-GROUNDING"))
    (done . ())
  ))

  ("PHILOSOPHY-SVA-VS-PARA-KARTR" . (
    (priority . 5.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PHILOSOPHY-ONTOLOGY-BOUNDARIES" . (
    (priority . 6.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-SAMJNA-AS-CATEGORIZATION-NOT-JUST-TAG"))
    (done . ())
  ))

  ;; =============================================
  ;; DERIVATIONS — наступні деривації
  ;; =============================================

  ("PANINI-MACHINE-DADATI-DERIVATION" . (
    (priority . 7.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-DERIVE-BAVATI-EXECUTION"
                   "PANINI-MACHINE-RESOLVE-CONFLICT-DADATI-TEST"))
    (done . ())
  ))

  ("PANINI-MACHINE-KAROTI-DERIVATION" . (
    (priority . 6.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-DADATI-DERIVATION"))
    (done . ())
  ))

  ("PANINI-MACHINE-STHALYA-PACATI-DERIVATION" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-FIXUP-ACTION-GRAPH-ARITY"
                   "PANINI-MACHINE-DADATI-DERIVATION"))
    (done . ())
  ))

  ;; =============================================
  ;; AUDIT — аудити і верифікація
  ;; =============================================

  ("PANINI-V01-EXIT-CRITERIA-AUDIT" . (
    (priority . 7.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("PANINI-MACHINE-GATE-REVIEW-V2-POST-FIX" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-DHATU-REGISTRY-SINGLE-SOURCE"
                   "PANINI-MACHINE-FIXUP-ACTION-GRAPH-ARITY"))
    (done . ())
  ))

  ("PANINI-HYPOTHESIS-LEDGER-UPDATE-AFTER-TESTS" . (
    (priority . 6.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-MACHINE-DERIVE-BAVATI-EXECUTION"))
    (done . ())
  ))

  ("PANINI-TRIPADI-RULE-EXCEPTION-AUDIT" . (
    (priority . 5.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-TRIPADI-SCOPE-INVESTIGATION"))
    (done . ())
  ))

  ("PANINI-SAMJNA-MACHINE-REPR-REDESIGN" . (
    (priority . 5.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ("PANINI-SAMJNA-AS-CATEGORIZATION-NOT-JUST-TAG"
                   "PHILOSOPHY-SAMANYA-VISESA-ONTOLOGY"))
    (done . ())
  ))

  ;; =============================================
  ;; SWARM / INFRA
  ;; =============================================

  ("SWARM-CAPABILITY-NAMING-CONVENTION" . (
    (priority . 4.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("SWARM-NODE-DEPLOY-TROUBLESHOOT" . (
    (priority . 4.0)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

  ("SWARM-REMOTE-ACCESS-DOCUMENTATION" . (
    (priority . 3.5)
    (capabilities . ("my-lisp-panini"))
    (depends-on . ())
    (done . ())
  ))

)))
