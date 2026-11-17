macro_rules! my_custom_macro
{
    ($($x:stmt)*) =>
    {
        $($x)*
    };
}

fn main()
{
    my_custom_macro!
    {
        println!("Line 1");
        println!("Line 2");
    }

    // Short macro call with braces -> Monolith:
    my_custom_macro! { 42 };
}
