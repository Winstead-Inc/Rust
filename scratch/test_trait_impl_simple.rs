pub trait SimpleTrait
{
    fn simple_method(&self);
}

impl SimpleTrait for ItemWorker
{
    fn simple_method(&self)
    {
        println!("Simple");
    }
}
