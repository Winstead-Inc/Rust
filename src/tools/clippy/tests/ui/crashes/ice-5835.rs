#[rustfmt::skip]
pub struct Foo
{
    //~v tabs_in_doc_comments
    /// 位	
    ///   ^ Do not remove this tab character.
    ///   It was required to trigger the ICE.
    pub bar: u8,
}

fn main() {}
