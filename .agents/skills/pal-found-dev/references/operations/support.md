# Diagnose, recover and verify pipelines

[Production operations](../operations.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Pipeline support connects business freshness to execution and data state. A schedule run
marked Succeeded indicates it launched a build; that build can still run or fail. An
Ignored run can mean no stale work remained. Triggers during a prior run wait for it to
finish. Pausing resets trigger state and ignores observed events while paused; resuming
requires checking that intended inputs will be processed.

Maintain a runbook with output contract, support hours, rotation, upstream contacts,
escalation, recurring issues and handover. Recovery can repair code, configuration,
permissions or upstream data. Replaying before diagnosis can duplicate writes or waste
compute. [Monitoring](monitoring.md) defines evaluated alerts and responder ownership.

## Prerequisites

Prepare schedule/output IDs, branch/fallback chain, freshness/schema/count contract, last
healthy build and permitted recovery actions. Owners authorize schedule/code/security
changes. Real builds and diagnosis require enrollment access; local fixtures test logic
only. Source outages and platform faults require their responsible support/admin owners.

## Procedure

1. Start from the alert/output. Record symptom, observed time and consumer impact. Follow
   [lineage](lineage.md) to the first failing invoked job, inputs and output state.
2. Inspect schedule history and linked build/jobs. Compare healthy/failed runs, source
   commit, schema/counts, queue versus computation time and execution permissions.
   In Builds use job Compare, including Input Changes and Code Changes. Compare
   requires output transactions; otherwise inspect logs and source/input baseline.
3. Preserve logs before canceling a hanging build: job report > Logs > _driver.log > Download.
   Spark details > Executors > Snapshot can preserve evidence. Keep these artifacts in
   the organization's approved restricted location.
4. Classify upstream, owned change or platform issue. Repair owned defects through the
   review/release path. Escalate external faults with IDs, times and observed scope.
5. Rebuild the intended schedule where safe to retain schedule history. Reconcile APPEND,
   stream or external effects before retrying. For incremental changes determine whether
   compatible history remains or an approved recompute is needed.
6. Verify completed build, committed output, schema/counts/freshness, consumer state and
   passing check evaluation. Restore paused schedules/checks and record handover.

For schedule creation/correction, open dataset Actions > Manage Schedules > Create schedule
in Data Lineage. Verify graph branch/fallbacks; choose targets, exclusions, trigger and
build type: single targets, full upstream or connecting path. Inspect proposed scope
before saving. Time/update triggers can use Any/All combinations. Choose approved
project-scoped execution where appropriate; user-scoped schedules follow that user's access.
Project scope can be unavailable when rights are insufficient, datasets remove markings
or require a user account, or targets cannot resolve to a distinct project set. Diagnose
that restriction before changing scope; user-scoped runs fail if that user loses access.

## Worked example

Illustrative incident: orders updated at 10:00, totals still shows 09:00 values, schedule
run says Succeeded but linked totals job FAILED on a new text amount column. Dashboard
still displays old committed output. Compare schema against the healthy job.

Prepare a reviewed validation/cast fix in an isolated branch. Test valid values and
invalid text; decide whether invalid input must fail the contract instead of disappearing.
Merge/release, rebuild production schedule and inspect intended orders transaction,
new committed totals, row values and freshness check. If source data violates the agreed
contract, escalate to its owner and clearly identify old output as stale. This walkthrough
is illustrative, not a recorded incident or authorized production mutation.

## Expected result and checks

Evidence names cause, change, source commit, input/output transactions, build/job completion,
current values and consumer verification. A manual dataset job alone cannot repair a
misconfigured schedule. Confirm the next scheduled run uses corrected context within its
SLA. Hand over unresolved risks with owner/time and report downstream recovery status.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Launch succeeded, output old | Inspect linked build and transaction; launch status is insufficient. |
| Repeated jobs queued | Inspect overlaps/input locks and schedule scope before increasing resources. |
| Timeout with uncertain write | Reconcile existing effect; resume using the workload's idempotency policy. |
| Incremental history incompatible | Review schema/history and approve the required recompute before rerun. |
| Broad service failure | Record reproducibility/scope and escalate; avoid speculative code changes. |

Optional source attribution: [schedule behavior](https://www.palantir.com/docs/foundry/data-integration/schedules),
[configuration](https://www.palantir.com/docs/foundry/building-pipelines/create-schedule),
[job comparison/logs](https://www.palantir.com/docs/foundry/optimizing-pipelines/debug-job),
[pipeline diagnosis](https://www.palantir.com/docs/foundry/optimizing-pipelines/debug-pipeline),
[support ownership](https://www.palantir.com/docs/foundry/maintaining-pipelines/support-processes).
