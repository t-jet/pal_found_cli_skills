# Production release procedure

[Pipeline guide](../pipelines.md) | [Development guide](../../SKILL.md)

## Concept and lifecycle

A pipeline product may cross datasource, transformation, Ontology and workflow
projects. Each project needs resource ownership and permission boundaries.
Versioning source, reviewing a change, publishing its configured artifact and
building datasets establish separate states. A completed dataset build still
needs content, schema, freshness and downstream checks before delivery.

Git branches carry code. Dataset/build branches select data and resolved
transform context. Shared product branch names can help coordinate repositories,
but those lifecycles remain distinct. Recommended production/development/
feature branch conventions are examples, not universal tenant branch names.

## Prerequisites

A Code Repository's configured fallback applies only to its own builds and
actions. Scheduled builds and other applications do not inherit that setting.
Verify production schedule/build branch resolution separately from repository
Preview or an in-repository build.

Identify product outputs and consumers, project owners, input contracts,
repository and production branch, prepared runtime, release authority and
required checks/approvals. Record the transform/artifact revision intended for
production, the dataset branch and any fallback behavior. Required permissions
include access to inputs, authorized output writes and the relevant repository
merge/release/build operations. Platform changes occur through enrollment
access; offline work can prepare/test code and the release plan only.

## Procedure

1. Map source ingestion, transform outputs, Ontology backing data and consuming
   workflow resources to their owning projects. Define the output contract,
   refresh requirement and escalation owner at each handoff.
2. Confirm the repository's production target and working branch. Under
   `Settings > Branches`, inspect the default branch, available merge modes,
   protection and fallback settings. Required checks and reviewer policy are
   conditions to satisfy, not permissions implied by being the code author.
3. Implement and test on the working branch, with representative input
   context and security. Check schema/null/duplicate contracts and an adverse
   case. Determine whether schema or business-logic changes require a snapshot
   recompute, consumer update or coordinated release.
4. Commit and inspect Checks for the exact revision. Open the pull request
   against the intended target, resolve review findings and obtain the
   configured approvals. Merge using an allowed mode; squash and merge changes
   the target commit history differently from preserving individual commits.
5. Verify the merged target's checks and transform/artifact selection. Apply
   tags or explicit publication when this repository's configured release
   workflow uses them. Record the resulting code/artifact revision; do not
   claim that a tag alone refreshed output data.
6. Build the intended product outputs on the production dataset context.
   Inspect the build and individual jobs, resolved inputs, output transaction
   state, schema, content and freshness. Use [transaction guidance](transactions.md)
   when distinguishing data visibility from build completion.
7. Check downstream consumers and data health. Enable or resume the intended
   schedule only when its targets, branch and identity are correct. Record the
   deployed revision and output/build evidence for the product owner.

## Worked example

Illustrative product: customer ingestion in a datasource project, the Orders
transform in a pipeline project, an Order object type in an Ontology project,
and approval UI in a workflow project. Confirm real project IDs and owners;
displayed project names are not API resource identifiers.

The change rejects unmatched customer IDs. The selected branch preview shows
`o1/c1/Ada/1200`; tests additionally reject missing and duplicate references.
A failed output expectation on duplicate order keys prevents acceptance even
when an earlier preview displayed a good sample.

After correction, record the following release evidence with real values:

```json
{
  "repositoryRevision": "illustrative-reviewed-commit",
  "targetGitBranch": "actual-protected-production-branch",
  "datasetBranch": "actual-production-data-context",
  "review": "approved-for-that-revision",
  "checks": "passed-for-that-revision",
  "build": "actual-build-id",
  "outputTransaction": "actual-committed-transaction-id",
  "outputChecks": "schema-content-freshness-verified",
  "consumerChecks": "Order-and-approval-workflow-verified"
}
```

This is a release record, not a Foundry request schema. If the tenant is
unavailable, only the code/fixture results and proposed steps can be recorded;
the build/transaction/consumer fields remain pending, not invented IDs.

## Expected result and checks

The production build uses the intended reviewed logic and branch-resolved
inputs. Its output contains the accepted schema and business rows, with
committed visibility and expected freshness. Owners can identify the source
revision, build/jobs, data state and consumer checks. A schedule start or
successful upstream job alone cannot establish those results.

## Failures and recovery

Failed checks or missing approvals stop the release path. A mismatched branch
or fallback requires correcting the selected context before another build.
For an upstream permission error, repair the relevant identity/resource access;
do not widen unrelated project roles. A successful build with stale output
requires tracing resolved inputs and schedule/health evidence.
If a released change is defective, use the repository's authorized correction
or revert process and rebuild/validate affected outputs; reverting source does
not automatically reverse committed dataset data or downstream effects.

Optional sources: [project and team structure](https://www.palantir.com/docs/foundry/building-pipelines/recommended-project-structure),
[branching and release](https://www.palantir.com/docs/foundry/building-pipelines/branching-release-process),
[production pipelines](https://www.palantir.com/docs/foundry/building-pipelines/building-production-pipeline),
[branch settings](https://www.palantir.com/docs/foundry/code-repositories/branch-settings),
[builds](https://www.palantir.com/docs/foundry/data-integration/builds).
