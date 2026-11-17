fn main()
{
    let x = 1;
    match x
    {
        1 => {
            DoWork(1);
            DoWork(2);
        }
        2 => DoWork(3),
        3 => { DoWork(4); },
        _ =>
        {
            DoWork(5);
        }
    }
}
