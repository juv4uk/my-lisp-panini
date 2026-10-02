//! D7 adversarial probe (panini agent): can a digit cell of a Text7 value act as a Number through any evaluator path?
//! Local, read-only evidence; NOT part of SENS. Run: cargo test --offline --test d7_probe -- --nocapture
use sens::{eval_program, load_core_library, Session, Text7, Value};

#[test]
fn text7_never_acts_as_number() {
    // digit 5 and digit 7 cells in the PINNED-safe v3 table (0x3b, 0x3a), plus a letter cell 0x00 (k)
    let t5 = Text7::from_cells(vec![0x3b]).unwrap();
    let t57 = Text7::from_cells(vec![0x3b, 0x3a]).unwrap();
    let probes = [
        "(+ t 1)", "(+ t t)", "(- t 1)", "(* t 2)", "(< t 100)", "(= t 59)", "(= t 5)", "(equal? t 59)", "(eqv? t 59)", "(eq? t t)", "(equal? t t)",
        "(number? t)", "(string? t)", "(symbol? t)", "(atom? t)", "(null? t)", "(pair? t)", "(zero? t)", "(abs t)", "(max t 1)", "(min t 1)",
        "(string-length t)", "(string-append t \"x\")", "(number->string t)", "(string->number t)", "(length t)", "(car t)", "(cdr t)",
        "(vector-ref (vector 1 2 3) t)", "(list t t)", "(if t 1 2)", "(quote t)", "(t)", "(eval t)", "(string=? t \"1\")",
        "(eq? t 59)", "(equal? t 5)", "(eq? t 5)", "(= t2 t2)", "(+ t2 1)", "(= t2 t2)", "(equal? t t2)",
    ];
    for src in probes {
        let mut session = Session::default();
        load_core_library(&mut session).expect("core library loads");
        session.environment.define("t", Value::Text7(t5.clone()));
        session.environment.define("t2", Value::Text7(t57.clone()));
        let r = eval_program(src, &mut session);
        match r {
            Ok(v) => println!("{:<34} => OK  {}", src, v.value),
            Err(e) => println!("{:<34} => ERR {}", src, e),
        }
    }
}
