# Pipelines and development workflow

[Foundry development guide](../SKILL.md) | [Production operations](operations.md)

## From source data to a pipeline output

A pipeline reads source data, applies transformations, and delivers datasets
or Ontology outputs for later workflows. Batch processing runs on selected
input snapshots. Incremental processing updates an output from changes since
earlier runs when the inputs and transform support it. Streaming pipelines
process arriving data continuously and require a latency and throughput design
across every stage. Choose the mode from freshness needs, input behavior, and
operating cost. See [building pipelines](https://www.palantir.com/docs/foundry/building-pipelines/overview),
[Pipeline Builder concepts](https://www.palantir.com/docs/foundry/pipeline-builder/core-concepts),
and [pipeline types](https://www.palantir.com/docs/foundry/building-pipelines/types-of-pipelines).

Pipeline Builder connects input datasets, expressions, table transforms,
expectations, and outputs in a graph. Preview intermediate results before
delivery; then build the outputs. A transform expression produces a column,
while a table transform such as filter, join, or pivot changes a table.
Outputs can include datasets and Ontology components. Branch work lets authors
test a change before its production release. See [Pipeline Builder overview](https://www.palantir.com/docs/foundry/pipeline-builder/overview),
[transforms](https://www.palantir.com/docs/foundry/pipeline-builder/transforms-overview),
and [core concepts](https://www.palantir.com/docs/foundry/pipeline-builder/core-concepts).

Code Repositories suits transforms requiring custom libraries, external API calls,
specialized logic, or a code review workflow. Python transform repositories
support batch and incremental pipelines, expectations, reusable libraries, and
different compute engines. SQL transform repositories use Spark SQL for batch
transforms. Foundry SQL transforms do not support incremental execution;
choose a supported Python transform when the design requires incremental
semantics. Sources: [Code Repositories](https://www.palantir.com/docs/foundry/code-repositories/overview),
[Python transforms](https://www.palantir.com/docs/foundry/transforms-python/overview),
[SQL transforms](https://www.palantir.com/docs/foundry/transforms-sql/overview).

## Author Python transforms

A Python transform declares its inputs and outputs, then implements logic in a
function. Foundry registers that function in a pipeline; a build resolves the
inputs and executes the transform. Choose PySpark or a single-node engine from
the data size and library needs. Treat schemas, null behavior, and output
contracts as part of the interface consumed by downstream datasets. Start with
[transform definitions](https://www.palantir.com/docs/foundry/transforms-python/transforms),
[pipeline registration](https://www.palantir.com/docs/foundry/transforms-python/pipelines),
and [compute engines](https://www.palantir.com/docs/foundry/transforms-python/compute-engines).

An incremental transform can process added or modified input relative to prior
successful output. Its behavior depends on input transactions and whether a
full recompute is required. Plan the first build, backfills, schema changes,
and fallback to full computation; an input change is not automatically a usable
incremental update. See [incremental transforms](https://www.palantir.com/docs/foundry/transforms-python/incremental-usage)
and [incremental pipeline guidance](https://www.palantir.com/docs/foundry/building-pipelines/incremental-pipelines-overview).

Keep shared code in a supported Python library and declare dependencies in
the repository instead of relying on a developer's local environment.
[Using Python libraries](https://www.palantir.com/docs/foundry/transforms-python/use-python-libraries)
explains the supported packaging path. Consult the [Python transforms library
API](https://www.palantir.com/docs/foundry/api-reference/transforms-python-library/api-overview)
for decorator and I/O details.

## Author SQL transforms

Use a SQL transform when a table can be produced with a maintainable Spark SQL
query. Declare inputs and output in its repository configuration; reference
datasets using the syntax documented by Foundry rather than assuming a normal
database connection or dialect. Check the query with a preview and validate
column names and types before publishing. For syntax and supported operations,
read [SQL transforms](https://www.palantir.com/docs/foundry/transforms-sql/overview)
and the [Spark SQL reference](https://www.palantir.com/docs/foundry/transforms-sql/spark-reference).

## Develop, test, and release

1. Create a repository branch and make a small transform change. Code
   Repositories exposes files, branches, tags, pull requests, and checks.
2. Preview the transform against representative input on the intended branch.
   A preview helps inspect logic before a full build but does not establish
   production correctness.
3. Test code-level behavior with repository or Python unit tests. Add data
   expectations for output properties such as key uniqueness, row count, or
   required values. A failed expectation can fail a build.
4. Commit, run checks, review the pull request, then merge using repository
   branch rules. Tag or release when the repository workflow requires it.
5. Build target datasets on the production branch and inspect build and job
   status, output data, and downstream health before treating the change as
   delivered. A merged code change alone does not refresh a dataset.

See [repository navigation](https://www.palantir.com/docs/foundry/code-repositories/navigation),
[transform preview](https://www.palantir.com/docs/foundry/code-repositories/preview-transforms),
[repository tests](https://www.palantir.com/docs/foundry/code-repositories/unit-tests),
[Python unit tests](https://www.palantir.com/docs/foundry/transforms-python/unit-tests),
[data expectations](https://www.palantir.com/docs/foundry/transforms-python/data-expectations-getting-started),
and [branch settings](https://www.palantir.com/docs/foundry/code-repositories/branch-settings).
For a complete release design, read [branching and release process](https://www.palantir.com/docs/foundry/building-pipelines/branching-release-process),
[recommended project structure](https://www.palantir.com/docs/foundry/building-pipelines/recommended-project-structure),
and [building a production pipeline](https://www.palantir.com/docs/foundry/building-pipelines/building-production-pipeline).

In local VS Code development, configure the supported Foundry tooling and
authentication, then use local preview and tests before committing. The local
environment and the Foundry build environment can differ, especially in
compute size, secrets, and data access. Follow [Python local development](https://www.palantir.com/docs/foundry/transforms-python/local-development),
[local preview](https://www.palantir.com/docs/foundry/transforms-common/local-preview),
and the [local versus hosted VS Code guide](https://www.palantir.com/docs/foundry/vs-code/local-vs-workspace-guide).
Code Workspaces provide JupyterLab, RStudio, and VS Code workflows backed by
repositories. Publish workspace-backed transforms through the workspace's
publication workflow. See [Code Workspaces getting started](https://www.palantir.com/docs/foundry/code-workspaces/getting-started/index.html)
and [working with data](https://www.palantir.com/docs/foundry/code-workspaces/data).

## Understand builds, dataset branches, and transactions

A dataset stores snapshots produced by committed transactions. A dataset branch
points to a transaction; builds resolve which upstream data and transform
logic to use, then execute jobs for required outputs. Dataset branches and
Git branches have different lifecycles. A branch can fall back to another
branch for missing data; inspect the resolved branch when a build reads an
unexpected snapshot. See [datasets](https://www.palantir.com/docs/foundry/data-integration/datasets),
[data branching](https://www.palantir.com/docs/foundry/data-integration/branching),
and [builds](https://www.palantir.com/docs/foundry/data-integration/builds).

For Python transforms, Foundry opens transactions on outputs and commits them
when the job succeeds. If a transform swallows a write error or never writes
an output, the job can still succeed and commit an empty snapshot. Test output
contents and expectations, not only job success. See [Python transform
transactionality](https://www.palantir.com/docs/foundry/transforms-python/transforms).
For direct dataset writes through an API, create a transaction, upload or
change data within it, then commit or abort it. Transaction creation is not
equivalent to a completed build. See [create](https://www.palantir.com/docs/foundry/api/datasets-resources/transactions/create-transaction),
[commit](https://www.palantir.com/docs/foundry/api/datasets-resources/transactions/commit-transaction/),
and [abort](https://www.palantir.com/docs/foundry/api/datasets-v2-resources/transactions/abort-transaction).
