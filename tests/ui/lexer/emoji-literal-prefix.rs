macro_rules! lexes { ($($_: tt) *) => {} }

lexes!( 🐛#);
//~ ERROR identifiers cannot contain emoji
lexes!( 🐛 "foo");
lexes!( 🐛 'q');
lexes!( 🐛 'q);

fn main() {}
