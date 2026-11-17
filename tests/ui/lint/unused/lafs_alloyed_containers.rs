//@ run-pass
#![deny(unused_parens)]
#![deny(unused_braces)]
#![allow(non_snake_case)]
#![allow(non_camel_case_types)]

struct Security_Context;

fn VerifySecurityContext(_: & Security_Context) {}

fn AcquirePipelineLock(_: usize) {}

fn DispatchTelemetryEvent(_: & Security_Context, _: usize) {}

fn ExecutePrimaryPayload(_: & Security_Context) {}

fn ReleasePipelineLock(_: usize) {}

fn DispatchTransaction<T>(_Payload: T) {}

fn ProcessUserData(_A: usize, _B: usize, _C: usize, _D: usize) {}

fn main()
{
    let ItemIdentifier = Security_Context;
    let PipelineConfigIndex = 0;

    // State 1 — Monolith (Fits within 160-col Canvas Limit & <= 4 statements)
    ProcessUserData(1, 2, 3, 4);
    let ProcessItemMono = | Item: & Security_Context, Index: usize | { VerifySecurityContext(Item); AcquirePipelineLock(Index); };
    ProcessItemMono( & ItemIdentifier, PipelineConfigIndex);

    // State 2 — Alloyed Boundary Run: ([( ... )]) (Tuple inside Array inside Call — 0 unused braces/parens)
    DispatchTransaction
    ([(
        VerifySecurityContext( & ItemIdentifier),
        AcquirePipelineLock(PipelineConfigIndex),
        DispatchTelemetryEvent( & ItemIdentifier, PipelineConfigIndex),
        ExecutePrimaryPayload( & ItemIdentifier),
        ReleasePipelineLock(PipelineConfigIndex),
    )]);

    // State 2 — Alloyed Boundary Run: ([{ ... }]) (Multi-statement Block inside Array inside Call — 0 unused braces)
    DispatchTransaction
    ([{
        VerifySecurityContext( & ItemIdentifier);
        AcquirePipelineLock(PipelineConfigIndex);
        DispatchTelemetryEvent( & ItemIdentifier, PipelineConfigIndex);
        ExecutePrimaryPayload( & ItemIdentifier);
        ReleasePipelineLock(PipelineConfigIndex);
    }]);

    // State 1 — Monolith First for short expressions that fit the Canvas Limit
    let _ = { let X = 10; X * 2 };
    let _ = | X: usize | { X + 1 };
    let _ = [42];

    let PrimaryClusterNodeAllocationQuota: usize = 100_000;
    let SecondaryFailoverReplicationThreshold: usize = 200_000;
    let TelemetryIngestionBufferCapacityBytes: usize = 300_000;
    let MaximumConcurrentPipelineWorkerThreads: usize = 400_000;

    // State 3 — Detached Symmetry for calls (Exceeds 160-col Canvas Limit; multiple sibling arguments)
    ProcessUserData
    (
        PrimaryClusterNodeAllocationQuota + SecondaryFailoverReplicationThreshold,
        SecondaryFailoverReplicationThreshold + TelemetryIngestionBufferCapacityBytes,
        TelemetryIngestionBufferCapacityBytes + MaximumConcurrentPipelineWorkerThreads,
        MaximumConcurrentPipelineWorkerThreads + PrimaryClusterNodeAllocationQuota,
    );

    // State 3 — Detached Symmetry for arrays (Exceeds 160-col Canvas Limit; multiple sibling elements)
    let _Arr: [usize; 4] =
    [
        PrimaryClusterNodeAllocationQuota + SecondaryFailoverReplicationThreshold,
        SecondaryFailoverReplicationThreshold + TelemetryIngestionBufferCapacityBytes,
        TelemetryIngestionBufferCapacityBytes + MaximumConcurrentPipelineWorkerThreads,
        MaximumConcurrentPipelineWorkerThreads + PrimaryClusterNodeAllocationQuota,
    ];

    // State 3 — Detached Symmetry for closure parameters and body (Signature > 160 cols & Body > 4 statements)
    let ProcessItemDetached =
    |
    PrimarySecurityContextReference: & Security_Context,
    SecondarySecurityContextReference: & Security_Context,
    ActivePipelineConfigurationIndex: usize,
    FallbackReplicationPipelineIndex: usize,
    |
    {
        VerifySecurityContext(PrimarySecurityContextReference);
        VerifySecurityContext(SecondarySecurityContextReference);
        AcquirePipelineLock(ActivePipelineConfigurationIndex);
        DispatchTelemetryEvent(PrimarySecurityContextReference, ActivePipelineConfigurationIndex);
        ExecutePrimaryPayload(PrimarySecurityContextReference);
        ReleasePipelineLock(FallbackReplicationPipelineIndex);
    };
    ProcessItemDetached( & ItemIdentifier, & ItemIdentifier, PipelineConfigIndex, PipelineConfigIndex);

    // Grouped patterns (Monolith)
    let [A, B] = [10, 20];
    assert_eq!(A + B, 30);
}
