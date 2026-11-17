pub trait ProcessItem<T>
where
    T: Clone + Send,
{
    type Output;
    const RETRY_LIMIT: usize = 3;

    fn execute(&self, item: T) -> Self::Output;
}

pub struct ItemWorker;

impl<T> ProcessItem<T> for ItemWorker
where
    T: Clone + Send,
{
    type Output = Result<T, ()>;
    const RETRY_LIMIT: usize = 5;

    fn execute(&self, item: T) -> Self::Output
    {
        Ok(item)
    }
}
