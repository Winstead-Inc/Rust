fn main()
{
    let ItemIdentifier = 42;
    let PipelineConfigIndex = 0;

    DispatchTransaction([(VerifySecurityContextAndCheckAllPermissionsAndEnsureEverythingIsValidInTheGlobalSecurityContextDatabase(&ItemIdentifier), AcquirePipelineLockAndCheckIfTheLockIsAvailableBeforeProceedingToTheNextStepInThePipeline(PipelineConfigIndex), ReleasePipelineLockAndCheckIfTheLockWasSuccessfullyReleasedWithoutAnyIssuesOrDeadlocks(PipelineConfigIndex))]);
}
