fn Validate(_: usize) {}
fn Execute(_: usize) {}
fn DoWork(_: usize) {}
fn Step1(_: usize) {}
fn Step2(_: usize) {}
fn Step3(_: usize) {}
fn Step4(_: usize) {}
fn Step5(_: usize) {}

fn main()
{
    // Short closure fits on one line -> State 1 Monolith:
    let F1 = |x: usize| x + 1;

    // Short closure with block -> State 1 Monolith:
    let F2 = |x: usize| { Validate(x); Execute(x); };

    // Closure exceeding canvas -> State 3 Detached:
    let F3 =
    |
        FirstLongParameterNameForClosureExceedingTheCanvasLimit: usize,
        SecondLongParameterNameForClosureExceedingTheCanvasLimit: usize,
        ThirdLongParameterNameForClosureExceedingTheCanvasLimit: usize,
    |
    {
        DoWork(FirstLongParameterNameForClosureExceedingTheCanvasLimit);
        DoWork(SecondLongParameterNameForClosureExceedingTheCanvasLimit);
        DoWork(ThirdLongParameterNameForClosureExceedingTheCanvasLimit);
    };

    // Short parameters, multiline body (> 4 statements):
    let F4 = |x: usize|
    {
        Step1(x);
        Step2(x);
        Step3(x);
        Step4(x);
        Step5(x);
    };
}
