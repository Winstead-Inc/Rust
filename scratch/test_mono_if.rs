#![warn(clippy::if_not_else)]

pub fn test_mono(b: bool) -> i32
{
    if !b { 1 } else { 2 }
}
