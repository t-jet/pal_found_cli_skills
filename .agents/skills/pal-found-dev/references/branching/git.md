# Git review and branch settings

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

A Code Repository branch versions source and its published job specifications. Commit
checks, code review, merge, Function release and dataset build establish distinct states.
A repository's default branch determines the usual base/target; verify its configured
name instead of assuming it matches the global branch main or dataset root.

Protection requires pull requests and configured checks/reviews. Owners manage settings;
Editors and Owners can merge when policy passes. Required reviewer membership does not
grant repository access. Repository fallback settings apply only to builds/actions from
that repository; separately configure schedules or other build launchers.

## Prerequisites

Prepare repository RID, approved target branch, branch protection, dependencies and tests.
Use a separate sandbox branch per developer/file to avoid overwriting uncommitted work.
Prepared Git/local tools can inspect source; real checks, reviews and builds require
repository and data access. Owners authorize settings/security changes.

## Procedure

1. Open Settings > Branches and inspect Default branch, protection, merge modes and fallbacks.
   Keep security approval requirements when altering marking propagation.
2. In Code > branch menu create a sandbox branch from the intended base. Save code there.
   Follow [repository authoring](../pipelines/repositories.md) and [tests](../pipelines/testing.md).
3. Preview with declared data; run unit tests; commit and inspect every required check,
   especially ci/foundry-publish before relying on new JobSpecs.
4. Open Pull requests, create a proposal targeting the approved branch, inspect the complete
   diff and assign required reviewers with repository access. Resolve conflicts/check failures.
5. Merge using an allowed mode. Verify the resulting target commit, then run the intended
   target-branch build or Function release and inspect actual output/version.

## Worked example

Illustrative policy: production branch requires successful publishing, at least one approval
and no rejected reviews. Sandbox `fix-null-totals` changes a join's null handling. Preview
one null case and run the [SQL fixture](../../examples/sql/verify_fixture.py) as local
arithmetic evidence when adapting the SQL join; Spark/Foundry execution is separate.

A successful check plus a reviewer rejection still blocks this policy. Correct the code,
rerun checks and obtain approval. A squash merge produces one target commit; a normal
merge retains source commits plus a merge commit; fast-forward requires a direct path.
Whichever mode is chosen, production data remains old until its target build completes.

## Expected result and checks

Record base/head/merged commit, configured policy, checks, review and output transaction.
Stable Function tags can be restricted to protected branches. A prerelease on a feature
branch can support testing without entering a stable consumer's version range. Follow
[Function publication](../ontology/functions.md) for releasing, not only source merge.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Protected branch rejects edit | Use a sandbox and PR; satisfy its policy. |
| Reviewer cannot open PR | Grant approved repository access; reviewer requirement alone gives none. |
| Publishing check failed | Inspect failure; repair declarations/dependencies and recommit before building. |
| Schedule uses different inputs | Inspect schedule branch/fallbacks; repository settings do not govern it. |
| Wrong code merged | Prepare a reviewed corrective/revert change; verify target output after its build. |

Optional source attribution: [repository navigation](https://www.palantir.com/docs/foundry/code-repositories/navigation),
[branch policies](https://www.palantir.com/docs/foundry/code-repositories/branch-settings).
