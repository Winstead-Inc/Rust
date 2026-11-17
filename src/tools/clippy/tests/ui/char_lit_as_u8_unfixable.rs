#![warn(clippy::char_lit_as_u8)]

fn main()
{
    // no suggestion, since a byte literal won't work.
    let _ = '❤' as u8;
    //~^ char_lit_as_u8
}
