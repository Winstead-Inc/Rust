#![warn(clippy::if_not_else)]

pub fn test_neq_mono(x: i32) -> i32
{
    if x != 5 { 10 } else { 20 }
}

pub fn test_neq_multi(x: i32) -> i32
{
    if x != 5
    {
        println!("Non-five");
        10
    }
    else
    {
        println!("Five");
        20
    }
}
