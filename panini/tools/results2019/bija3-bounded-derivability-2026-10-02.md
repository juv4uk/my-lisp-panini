# SENS #2019: bounded derivability of the bīja3 seeds (finite evidence, NOT a proof), 2026-10-02

Tool: `panini/tools/review_sens_2019_derivability.py` (independent implementation; model and assumptions are in its docstring).
Exact assumptions: values = atoms {NIL,T,A,B} (variant {NIL,T}) + pairs + ERR; ERR is not observable inside a term (every
operation propagates it); `()` = constant NIL; QUOTE = introduce a constant atom T/A/B; EQ defined on atoms only; COND = ITE(p,a,b)
(p = NIL → b, any other → a), strict (ERR argument → ERR) as the main branch, lazy (the selected branch wins over an ERR
in the other) as the second branch. Derivable(t,B): a term over the variables and the basis B whose value vector equals t on a
finite test set (unary 8 values, binary 8×8, ternary p∈{NIL,T}×a,b∈4 values) within term size N (value-vector dedup, term cap).
A "not found" means "not within size N", not "underivable". No lambda, no recursion, no ERR-catching construct.

| Model | N | function seeds derivable from ALL the other seeds | minimal generating subsets of the 8 seeds |
|---|---|---|---|
| atoms=4, strict COND | 6 and 7 | none: ATOM, CAR, CDR, EQ, CONS, COND all "not found" (1.2k–4.1k terms at N=6; 4.0k–21.4k at N=7) | exactly ONE: {QUOTE, ATOM, EQ, CONS, CAR, CDR, COND}; `()` is derivable (e.g. NIL = EQ('T,'A)) |
| atoms=4, lazy COND | 6 | same: none derivable | same one subset |
| atoms=2 ({NIL,T}), strict | 6 | none | TWO: {(), ATOM, EQ, CONS, CAR, CDR, COND} and {QUOTE, ATOM, EQ, CONS, CAR, CDR, COND} (T = ATOM(NIL), NIL = EQ('T,'T)... the pair `()`/QUOTE is interchangeable): an equivalence class, issue outcome 4 for that pair |

Reading: in this finite model the six function seeds are pairwise independent (no one is rebuilt from the other five plus the
constants); `()` is redundant when QUOTE exists and atoms A,B exist; with only the atoms NIL,T, `()` and QUOTE are
interchangeable. The independence of ATOM, EQ, COND rests on ERR being unobservable: a construct that can catch ERR (or a
lambda/closure calculus) changes the result; laziness of COND alone does not (ERR still cannot be tested).
Not covered: alternative bases (no candidate class given), stability Lisp I → 1.5 (corpus step C), lambda/recursion, deeper terms.
