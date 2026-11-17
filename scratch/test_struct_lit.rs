#![allow(non_snake_case)]
#![allow(unused_variables)]

struct Point
{
    x: usize,
    y: usize,
}

struct LongStructName
{
    FirstFieldWithLongNameExceedingTheCanvasLimit: usize,
    SecondFieldWithLongNameExceedingTheCanvasLimit: usize,
    ThirdFieldWithLongNameExceedingTheCanvasLimit: usize,
}

fn main()
{
    // Short struct lit -> Monolith:
    let S1 = Point { x: 1, y: 2 };

    // Long struct lit -> Multiline:
    let S2 = LongStructName
    {
        FirstFieldWithLongNameExceedingTheCanvasLimit: 100,
        SecondFieldWithLongNameExceedingTheCanvasLimit: 200,
        ThirdFieldWithLongNameExceedingTheCanvasLimit: 300,
    };

    let LongStructName
    {
        FirstFieldWithLongNameExceedingTheCanvasLimit,
        SecondFieldWithLongNameExceedingTheCanvasLimit,
        ThirdFieldWithLongNameExceedingTheCanvasLimit,
    } = S2;
}
