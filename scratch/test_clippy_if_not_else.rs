#![warn(clippy::if_not_else)]

pub fn test_if(b: bool) -> i32
{
    if !b
    {
        println!("Branch 1");
        1
    }
    else
    {
        println!("Branch 2");
        2
    }
}
