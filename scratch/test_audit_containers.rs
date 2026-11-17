// 1. Function signatures with many arguments
fn VeryLongFunctionNameWithManyArguments(
    FirstArgumentWithVeryLongNameToExceedTheCanvasLimit: usize,
    SecondArgumentWithVeryLongNameToExceedTheCanvasLimit: usize,
    ThirdArgumentWithVeryLongNameToExceedTheCanvasLimit: usize,
) -> usize
{
    0
}

// 2. Generic type definitions with many type parameters
struct LongGenericStruct<
    FirstGenericTypeParameterExceedingTheCanvasLimit,
    SecondGenericTypeParameterExceedingTheCanvasLimit,
    ThirdGenericTypeParameterExceedingTheCanvasLimit,
>
{
    A: usize,
}

// 3. Array indexing expressions
fn TestIndex(Arr: &[usize])
{
    let X = Arr[
        VeryLongExpressionCalculatingTheIndexInsideTheArrayBracketsWhichExceedsTheCanvasLimit
    ];
}

// 4. Macro invocations
fn TestMacros()
{
    println!(
        "Very long formatted message with multiple arguments: {} and {}",
        FirstArgumentWithVeryLongNameToExceedTheCanvasLimit,
        SecondArgumentWithVeryLongNameToExceedTheCanvasLimit
    );

    vec![
        FirstArgumentWithVeryLongNameToExceedTheCanvasLimit,
        SecondArgumentWithVeryLongNameToExceedTheCanvasLimit,
        ThirdArgumentWithVeryLongNameToExceedTheCanvasLimit,
    ];
}

// 5. Attributes
#[derive(
    Clone,
    Copy,
    Debug,
    PartialEq,
    Eq,
    Hash,
    Default
)]
struct AttributeTest;
