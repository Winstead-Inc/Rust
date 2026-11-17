// issue: rust-lang/rust#125081

fn main()
{
    let _: & str = 'β;
    //~^ ERROR expected `while`, `for`, `loop` or `{` after a label
    //~| ERROR mismatched types
}
