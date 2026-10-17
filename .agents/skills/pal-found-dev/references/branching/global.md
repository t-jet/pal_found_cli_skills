# Global branch lifecycle

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

A global branch coordinates changes to supported Foundry resources across applications.
Its proposal checks conflicts and approval policies before delivery to main. Resource
support and rebase behavior vary; see [integration boundaries](integrations.md).
A branch's access roles govern branch management independently of resource editing.

Editing supported resources is isolated. Creating or deleting ordinary non-Ontology
resources affects main too; Ontology entity creation/deletion is isolated. Plan resource
creation before using a branch as a sandbox. Removing a resource from a branch returns
its configuration to main and can break dependent branch changes.

| Branch state | Execution and recovery |
| --- | --- |
| Active | Retains built/indexed branch data while active. |
| Inactive | Retention policy deindexes entities, later deletes data; builds fail. Choose Activate branch. |
| Archived | Manual retirement; similar data/build effects. Restore through Global Branching. |
| Merged | Terminal; cannot restore. Verify delivered main resources. |

Retention settings belong to Control Panel > Spaces > Actions > Global branch retention
policy. Reactivation may require Ontology reindexing, repository no-op commit followed
by a repository-launched build, or Pipeline Builder deploy/build to restore deleted
JobSpecs/data. Check and resume schedules paused after failures. Starting the initial
recovery build from Data Lineage does not republish missing repository JobSpecs.

## Prerequisites

Prepare resource RIDs, dependency list, expected main state, branch title, reviewers and
authorization. Branch Owner or space Administrator is required to create a proposal.
Resource editors author changes; applicable policies decide approval. Local preparation
can enumerate changes, but branch creation, checks and merge require enrollment access.
Administrators/owners configure protection and branch sharing.

## Procedure

1. Use the application's branch selector or Global Branching application to Create new
   branch. Open it and verify the branch taskbar before saving each resource.
2. Add required resources when prompted. Save supported configuration changes and inspect
   the branch's resource list and dependencies. Avoid assuming new ordinary files are isolated.
3. Compare latest main; rebase each out-of-date resource in its owning application.
   Resolve conflicting fields deliberately, then repeat dependent tests.
4. Choose Create proposal and describe changes, impact, branch evidence and recovery.
   Inspect resource checks; assign reviewers through Manage for Awaiting approval.
5. Resolve conflicts, missing access, rejected reviews and required approvals. All resource
   checks must pass before merge. Any proposal viewer can merge approved changes when
   checks pass and Do not merge is absent; removing that gate requires a branch Owner
   (space Administrators have equivalent management rights). Choose Merge proposal,
   select all affected builds, modified-only builds or no builds according to the
   delivery plan, then inspect main
   in every affected application and verify business behavior.

## Worked example

Illustrative task: add Shipment.priority to the Ontology and a priority column to an
existing Workshop module. Record both existing RIDs through their UI details. Create
`shipment-priority`, save the type change there, then open Workshop on the same branch,
add the column, save and preview. Main should retain its prior schema/layout until merge.

Suppose main changed the same Workshop column title during this work. Save current edits,
rebase in Workshop, choose the intended title for that conflicting field, save and retest
priority rendering. Create a proposal covering both resources; obtain their approvals.
After authorized merge, verify the property and column together on main. This is an
illustrative UI walkthrough, not a recorded tenant merge.

## Expected result and checks

Evidence identifies branch, resource RIDs, saved changes, latest-main rebase, proposal
checks, approvals and merged main behavior. A green check is readiness evidence;
publication/build/indexing or application release can require additional resource-specific
steps. [Branch contexts](contexts.md) separates these states from Git and dataset branches.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Resource not on branch | Verify integration support and selector; add and save it where required. |
| Rebase fails | Open the owning application's conflict UI; resolve, save and rerun checks. |
| Proposal rejected | Correct the resource and obtain the rejecting reviewer's new approval. |
| Removed dependency breaks preview | Restore/add the required resource or remove the dependent change; retest. |
| Partial merge fails | Inspect succeeded/failed resources on the proposal; repair errors and retry. Partial merges currently cannot be reverted. |
| Inactive/archived build fails | Reactivate/restore, recover indexing/JobSpecs/data as above and resume paused schedules. |
| Main differs after merge | Inspect each resource's publication and dependent version binding before another merge. |

Optional source attribution: [global workflow](https://www.palantir.com/docs/foundry/global-branching/core-concepts),
[branch authorization](https://www.palantir.com/docs/foundry/global-branching/branch-security).
