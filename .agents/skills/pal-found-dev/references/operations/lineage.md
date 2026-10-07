# Trace branch and build provenance

[Production operations](../operations.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Data Lineage shows dependencies and resource/build information, helping trace how an
output was produced and which consumers can be affected by an upstream change. A graph
edge establishes a dependency; selected branches and recorded transactions establish
the actual data used. Current upstream state can be newer than a successful old output.
[Branch resolution](../branching/datasets.md) explains fallback inputs and test outputs.

Builds contain jobs. A multi-output job updates its defined outputs together; a failed
build can still contain completed jobs that already wrote output. Inspect each relevant
job/output rather than assuming every dataset in a failed build retained old data.

## Prerequisites

Prepare resource IDs, expected production branch, last healthy time and business output
contract. Obtain RIDs/paths from dataset details and graph nodes. Resource/build view
access is required for real inspection. Local synthetic records support reasoning and
do not prove live provenance. Owners arrange missing access and upstream support contacts.

## Procedure

1. Open Data Lineage from the output dataset/project or search for its resource. Verify
   graph branch/fallback settings before investigating values.
2. Select the output and expand upstream/downstream resources. Inspect node details:
   schema, latest build, generating logic and out-of-date information where available.
3. Open Build timeline at bottom left. Choose the time window, select relevant datasets
   and click the suspected job for status, times and build/job/schedule links.
4. Open its report. Record source commit, resolved input transactions, output transaction
   and execution identity available in the report.
5. Compare with a healthy job and dataset history. Identify the first changed input/schema,
   source, context or execution failure. Inspect downstream consumers for impact.
6. After authorized repair/rebuild, repeat the trace and verify intended committed output
   and consumer state. Use [support](support.md) for recovery decisions.

## Worked example

Illustrative graph: orders → customer_totals → dashboard. At 10:00 orders/O2 commits;
customer_totals/T1 still contains the 09:00 result from orders/O1. A 10:05 totals job failed
because O2 changed amount from numeric to text. The dashboard can still render T1.

| Evidence | Interpretation |
| --- | --- |
| Orders latest O2; attempted totals job used O2 and failed | Inspect the input schema and computation failure. |
| Totals committed T1 from O1 | Visible data does not prove successful processing of O2. |
| Dashboard uses totals/master | Test-branch totals cannot repair this consumer. |

Open failed job Compare against the healthy job; inspect Input Changes and source commit.
After a reviewed fix, rebuild production and verify new totals from the intended orders
version. Reload the consumer and confirm its data/branch selection. This record is
illustrative, not a Foundry execution report.

## Expected result and checks

The investigation identifies affected branch, first failing dependency, healthy/failed
job IDs, input/output transactions, changed schema/source and downstream impact. Latest
successful time alone cannot establish business freshness. Keep a shareable lineage view
in the enrollment runbook without exporting restricted data.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Graph healthy but values stale | Compare actual input/output transactions and consumer branch. |
| Downstream job canceled | Trace its failed upstream; inspect the first invoked failing job. |
| Generating code missing | Check JobSpec publication, selected/fallback branch and authorized view access. |
| Unexpected partial pipeline output | Inspect completed jobs and their individual transactions. |
| No healthy comparison exists | Record source/input baseline and reproduce in an isolated authorized branch. |

Optional source attribution: [lineage overview](https://www.palantir.com/docs/foundry/data-lineage/overview),
[navigation](https://www.palantir.com/docs/foundry/data-lineage/navigation),
[build timeline](https://www.palantir.com/docs/foundry/data-lineage/build-timeline),
[build lifecycle](https://www.palantir.com/docs/foundry/data-integration/builds).
