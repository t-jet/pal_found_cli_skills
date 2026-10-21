# Select and verify branch contexts

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Branch names belong to different systems. Git selects source commits; a dataset branch
selects transaction history; a build branch selects job specifications and output targets;
a global branch selects supported cross-application configurations and Function previews.
Selecting a global branch is no guarantee every dataset or SDK client shares that context.

Use an explicit context record before testing: enrollment, global branch, repository
branch/commit, build branch/fallback chain, input transactions, output transaction and
application/Function version. Values come from resource selectors, build/job details and
prepared client configuration. Similar names are insufficient evidence.

## Prerequisites

Prepare known resource IDs and a nonproduction test plan. Use [Git controls](git.md),
[dataset resolution](datasets.md) and [global lifecycle](global.md) for their individual
procedures. Local analysis can compare a context record; tenant selection/build/read
needs authorization. Branch owners or space administrators manage sharing; authorized resource/project
owners manage applicable protection rules.

## Procedure

1. Choose Git for repository-only logic, global branching for supported coordinated
   configuration changes, and an explicit dataset/build branch for data isolation.
2. Open every involved application and verify its selector/taskbar. In repository work
   record the selected branch and commit; in a build record branch and ordered fallbacks.
3. Inspect each job's resolved input branch/transaction and output branch. Stop if a fallback
   resolves unintended data. Do not silently accept production input for a privacy test.
4. Verify generated SDK resource selection and request parameters separately. A dataset
   branchName parameter controls that operation; it is not a global Ontology branch selector.
5. Test and review changes in their owning system, then deliver code/configuration and build
   production outputs in the required order. Verify the production context again.

## Worked example

Illustrative graph: orders -> totals. Repository `experiment` publishes changed totals logic.
Build branch `experiment` has fallback `master`; orders exists only on master. A successful
experiment build can legitimately read orders/master while writing totals/experiment.
A Workshop global branch with a similar title does not automatically change that read.

| State | Meaning |
| --- | --- |
| Git experiment, totals/master open in viewer | Viewer shows production data, not the test output. |
| Build experiment, orders/master fallback, totals/experiment | Test logic/output with production input. |
| Global branch selected, external OSDK client unchanged | Client's independently configured supported resources/context still apply. |

For a test requiring synthetic orders, prepare orders on the test dataset branch through
its authorized writer, configure compatible fallback ancestry and recheck resolved input.
After source merge, build the production branch; dataset test transactions are not merged.

## Expected result and checks

Evidence ties a business result to exact source and data versions. Compare output schema,
counts and expected test-only values, not merely a success banner. No test-only value
should appear in production before deliberate delivery. [Lineage](../operations/lineage.md)
provides the provenance investigation procedure.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Correct name, wrong values | Compare branch types and resolved transactions; reopen intended data branch. |
| New schema missing in Function | Check branch-aware local SDK/template and resource imports. |
| Preview succeeds but production fails | Compare main schemas, grants and input snapshots; retest in production-equivalent context. |
| Unsupported resource appears unchanged | Use its independent release path and record that integration boundary. |

Optional source attribution: [build branch resolution](https://www.palantir.com/docs/foundry/data-integration/branching),
[Pipeline Builder coordination](https://www.palantir.com/docs/foundry/pipeline-builder/branches-overview),
[global integration limits](https://www.palantir.com/docs/foundry/global-branching/integrations).
