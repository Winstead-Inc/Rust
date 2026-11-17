fn main()
{
    let ItemIdentifier = 42;
    let PipelineConfigIndex = 0;

    // State 1 Monolith:
    ProcessUserData(1, 2, 3, 4);

    // State 2 Alloyed:
    DispatchTransaction
    ([(
        VerifySecurityContext(&ItemIdentifier),
        AcquirePipelineLock(PipelineConfigIndex),
        ReleasePipelineLock(PipelineConfigIndex),
    )]);
}
