# Execution identity and branch authorization

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Compute Function application permissions use its configured service identity; caller
access does not replace those grants. Pipeline mode gets scoped job access to declared
resource aliases. Sources separately configure network destinations and secrets. A valid
token, successful TLS connection and permission to read/write the resource are independent
checks. Use [execution modes](../compute/execution.md) and [Sources](../compute/integration.md).

Global branch Owner/Viewer roles control branch management, not resource editing.
Resource grants, protection policies and approvals govern authored changes. Proposal
merge permission can rely on preauthorized resource approvals; it need not imply the
merger can independently edit every resource.

## Prerequisites

Prepare module/app/resource RIDs, permission mode, actual service or job identity,
Sources, input/output aliases with branches and expected durable effects. Prepare branch
roles separately from resource roles. Local synthetic bindings verify parsing only.
Administrators/owners authorize OAuth, Source import/network policy, resource access,
branch sharing/protection; real execution/permission checks require enrollment.

## Procedure

1. Inspect Compute Configure for permission mode, service application and declared pipeline
   aliases. Confirm actual resource RIDs and branches using the resource picker/details.
2. Inspect Source network policy and module import authorization. Permit only the approved
   Foundry/external host. Verify TLS trust without disabling certificate checks.
3. Run a bounded allowed operation and an intentionally denied operation under the module
   identity. Inspect logs without exposing tokens/secrets. Follow explicit transaction or
   stream acknowledgment protocol; process exit alone establishes no atomic batch commit.
4. In Global Branching Security inspect branch roles/organizations. Identify branch Owner
   and required resource reviewers; verify each author has resource edit access.
5. Test the resource in the chosen branch context, then satisfy proposal checks/approvals.
   After delivery verify production resource effects under production execution identity.

## Worked example

Illustrative module reads incoming/demo and writes outgoing/demo. Developer can read both,
but service user can read only incoming. An allowed read plus denied write diagnoses the
service grant/output restriction; adding the hostname Source cannot fix it. Conversely,
service read/write grants with no egress Source fail at the network boundary.

For a coordinated branch change, giving collaborator branch Owner permits proposal
management but does not grant module editing or dataset access. Arrange the approved
resource grants, validate branch-specific aliases, and keep the two authorization records
separate. The [binding fixture](../../examples/compute/verify_fixture.py) detects absent
aliases; it neither authenticates nor proves the real grants.

## Expected result and checks

Capture permission mode, actual identity, host/Source, aliases/branches, read/write results,
proposal checks and final resource state. Confirm no personal token substitutes for the
service/job identity. If a nullable alias branch falls back to master but demo is required,
correct configuration before executing. An unknown write requires reconciliation before replay.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Developer succeeds, module denied | Inspect actual service/job grants and OAuth restrictions. |
| Token valid but connection fails | Inspect Source host/network policy and TLS trust. |
| Branch Owner cannot edit resource | Request approved resource edit rights separately. |
| Proposal cannot merge | Resolve conflicts, required reviews and Do not merge control. |
| Job writes wrong branch | Stop processing; reconcile effects and correct configured binding before restarting. |

Optional source attribution: [Compute execution identity](https://www.palantir.com/docs/foundry/compute-modules/execution-modes),
[Sources](https://www.palantir.com/docs/foundry/compute-modules/sources),
[global branch roles](https://www.palantir.com/docs/foundry/global-branching/branch-security).
