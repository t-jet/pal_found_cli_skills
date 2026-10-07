# Dataset branches and fallbacks

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

A dataset branch points into its transaction history. Child branches begin from a parent
branch or transaction and can advance independently. Dataset branches cannot be merged
like Git source. Deleting a branch removes its pointer without deleting transactions.
[Transactions](../pipelines/transactions.md) explains snapshot/append visibility and commits.

Build branch resolution chooses logic and inputs through an ordered fallback chain.
Outputs are built on the selected build branch; inputs can resolve to fallback data.
Repository-local fallback configuration does not automatically apply to external launchers.

## Prerequisites

Prepare dataset RIDs, committed input transactions, branch ancestry, published JobSpecs,
output rights and desired fallback chain. Use an isolated output branch and actual branch
selectors rather than invented defaults. Local arithmetic fixtures do not create branches.
Dataset creation, writes and builds need enrollment access; admins authorize access changes.

## Procedure

1. Inspect dataset branch/history and identify the intended source transaction. For SDK
   branch creation and transaction operations, use the complete [local REST catalog](../rest-api.md).
2. Configure the repository's branch fallbacks in Settings > Branches, or the specific
   Pipeline Builder/build/schedule launcher. Check configuration in the actual launcher.
3. Publish the intended transform JobSpecs and initiate the build on the explicit branch.
   Inspect graph resolution before accepting any fallback input.
4. Read job details and output history. Verify the resolved inputs and committed output,
   then compare counts/schema against expectations.
5. Review and merge source when ready. Build production using its intended source/inputs;
   production data is recomputed instead of merging test dataset history.

## Worked example

Illustrative context: source orders/master is transaction O1; totals/master is T1. Create
repository branch `test-discount`, change totals logic, publish and build on that branch
with fallback master. If orders has no test branch, it resolves to master/O1; totals gets
a test output. Verify the newly committed totals transaction in the test branch viewer.

Advance orders/master to O2 and inspect the test build's recorded O1 input. Its prior
result remains evidence for O1, not O2. Rebuild deliberately to test O2. Merging the source
then building master generates a production totals transaction from the selected inputs.
A test-branch dataset result never becomes production simply because code merged.

## Expected result and checks

Capture launcher, branch/fallback sequence, job source commit, resolved input transactions
and output state. Recheck upstream changes before delivering. A branch with an open
transaction cannot accept another transaction until it is closed; consult transaction
status before retrying an explicit writer. An aborted/unknown write is not committed data.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| No input branch | Inspect declared fallback and ancestry; prepare authorized test input or choose approved fallback. |
| Graph cannot resolve | Check JobSpec publication, fallback compatibility and resource access. |
| Another transaction cannot start | Inspect current open transaction and reconcile/commit/abort through its owner. |
| Test data appears missing | Select the test output branch and transaction, not the production viewer default. |
| Repeated APPEND duplicates data | Reconcile prior commit before replay; use an appropriate snapshot/idempotent design. |

Optional source attribution: [dataset/build branch semantics](https://www.palantir.com/docs/foundry/data-integration/branching),
[launcher-specific fallbacks](https://www.palantir.com/docs/foundry/code-repositories/branch-settings).
