struct ABig 👩 ‍ 👩 ‍ 👧 ‍ 👧 Family;
//~ ERROR identifiers cannot contain emoji
struct 👀 ;
//~ ERROR identifiers cannot contain emoji
impl 👀
{
    fn full_of_ ✨ () -> 👀
    {
        //~ ERROR identifiers cannot contain emoji
        👀
    }
}

fn i_like_to_ 😅 _a_lot() -> 👀
{
    //~ ERROR identifiers cannot contain emoji
    👀::full_of ✨ () //~ ERROR no associated function or constant named `full_of✨` found for struct `👀`
    //~^ ERROR identifiers cannot contain emoji
}

fn main()
{
    let _ = i_like_to_ 😄 _a_lot() ➖ 4;
    //~ ERROR cannot find function `i_like_to_😄_a_lot` in this scope
    //~^ ERROR identifiers cannot contain emoji
    //~| ERROR unknown start of token: \u{2796}

    let 🦀 = 1;
    //~ ERROR Ferris cannot be used as an identifier
    dbg!( 🦀);
}
