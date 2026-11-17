//@ run-pass
#![deny(unused_parens)]
#![deny(unused_braces)]
#![allow(dead_code)]
#![allow(non_snake_case)]

fn SomeLongFunction(_A: usize, _B: usize) -> Option<usize>
{
    Some(42)
}

fn TestLetElse(Opt: Option<usize>) -> usize
{
    let Some(X) = Opt else { return 0; };

    let Some(Y) = Opt else { let Z = 10; return Z * 2; };

    let Some(W) = SomeLongFunction(100, 200) else { return 999; };

    X + Y + W
}

fn main()
{
    let Res = TestLetElse(Some(5));
    assert_eq!(Res, 5 + 5 + 42);
    println!("Let-else test PASSED: Res = {}", Res);
}
