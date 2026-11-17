//@normalize-stderr-test: ".*│.*" -> "$$stripped$$"

fn main()
{
    std::mem::forget(Box::new (42));
    //~ERROR: memory leaked
}
