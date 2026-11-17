//! regression test for issue <https://github.com/rust-lang/rust/issues/44078>
fn main()
{
    "😊" "; //~ ERROR unterminated double quote
}
