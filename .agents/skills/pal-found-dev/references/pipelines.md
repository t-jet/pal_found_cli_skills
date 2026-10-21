# Pipelines and development workflow

[Foundry development guide](../SKILL.md) | [Production operations](operations.md)

A pipeline turns source data into datasets or Ontology inputs consumed by
applications. Its contract includes input schemas, transformations, output
schemas, freshness, permissions and recovery. A successful code check or preview
is separate from a production build and its committed output.

## Choose the pipeline and development tool

Batch computation reads selected input state and computes an output. Incremental
computation uses supported changes and prior state; it needs a valid initial
build, compatible input histories and a deliberate recompute strategy.
Streaming continuously processes arrivals and requires end-to-end latency,
throughput and state management. A batch schedule provides periodic refresh;
it does not turn a batch algorithm into a streaming pipeline.

Pipeline Builder expresses inputs, transformations, expectations and outputs
as a graph. Inspect intermediate results and validate a join's keys, nulls and
cardinality before delivering output. Its supported computation modes and
operations govern whether an algorithm is batch, incremental or streaming.
Code Repositories gives developers source control, transform registration,
dependency declarations, tests, checks and review. Choose it for custom Python
or SQL logic and libraries that need those controls. A Code Workspace provides
an interactive notebook/editor environment; reproducible publication needs
declared inputs, outputs and dependencies rather than hidden notebook state.

## Local development procedures

| Task | Local procedure and examples |
| --- | --- |
| Author a SQL transform and validate its output | [SQL transforms](pipelines/sql.md) |
| Explore notebook data and publish an output | [Workspace exploration and publication](pipelines/workspaces.md) |
| Navigate and register a repository pipeline | [Repository lifecycle](pipelines/repositories.md) |
| Author a typed Python transform and join | [Python transforms](pipelines/python-transforms.md) |
| Exercise logic, Preview and failing expectations | [Testing and data checks](pipelines/testing.md) |
| Distinguish local VS Code, hosted tools and real data access | [Local development](pipelines/local-development.md) |
| Protect branches, review/release code and verify production output | [Release and production design](pipelines/releases.md) |
| Choose snapshot/incremental execution and verify committed state | [Transactions and incremental execution](pipelines/transactions.md) |

## Follow the output through delivery

1. Identify source datasets, branches, schemas, freshness and permitted
   identities. Locate the owning project and production output.
2. Declare inputs/outputs and register the transform. Make source changes on
   the intended Git branch; declare libraries in the repository environment.
3. Run representative fixtures and inspect Preview. Exercise duplicate/null
   inputs and expected failures, then configure production expectations.
4. Run repository checks and review the exact commit. Merge or release using
   the configured branch protection and production selection rules.
5. Build selected production datasets. Verify resolved upstream branches,
   job/build status, committed transactions, output contents and downstream
   consumer health before treating the change as delivered.

Prepared local fixtures validate deterministic logic without public access.
Preview against enrollment data, repository checks, builds and committed writes
require authorized platform connectivity. Missing access is an explicit
prerequisite failure; a locally complete procedure can report that boundary
without retrieving additional public documentation.

Dataset branches track transaction histories and may resolve missing data
through fallback. Git branches track code. A Git merge does not combine dataset
contents. Transform output transactions commit when the job succeeds, while a
multi-job pipeline build has several output histories. Inspect actual data;
swallowed write errors or skipped writes can leave an unintended empty snapshot.

For exact version-specific direct-write inputs and statuses, use the
[local REST SDK contracts](rest-api.md). Keep transaction identities for bounded
commit/abort reconciliation. Repeating a timed-out write without inspecting its
known transaction can duplicate effects.

Optional provenance: [pipeline types](https://www.palantir.com/docs/foundry/building-pipelines/types-of-pipelines),
[Pipeline Builder concepts](https://www.palantir.com/docs/foundry/pipeline-builder/core-concepts),
[tool comparison](https://www.palantir.com/docs/foundry/building-pipelines/considerations-pb-cr).
