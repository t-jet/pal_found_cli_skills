# Python transform lifecycle

[Pipeline guide](../pipelines.md) | [Development guide](../../SKILL.md)

## Concept and lifecycle

A Python transform binds input datasets and output datasets to compute logic.
Foundry resolves those resources and executes the registered transform during
a build. Single-node engines include pandas, Polars and DuckDB; PySpark uses
distributed execution. Select an engine from data shape, memory needs,
library compatibility and supported features. Engine changes can alter APIs
and limits. SQL transforms have separate semantics.

## Prerequisites

Supply the repository/package, input and output identifiers or authorized
paths, exact schemas, chosen engine, prepared runtime/dependencies and
read/write permissions. Examples below use current documented APIs: the
single-node `transform.using` with `input.pandas()`/`output.write_table`, and
PySpark `transform_df` with DataFrame arguments. A prepared older template
must expose the chosen API before this example can execute; do not assume
decorators from different runtime generations are interchangeable.

`transform.using` requires `transforms >=3.68.0` and, in Code Repositories,
`transformsLangPythonPluginVersion >=1.978.0`. Verify both prepared versions.
An older template can reject `.using` even if ordinary Python imports work;
use an approved compatible runtime/template before running these examples.

Local business fixtures require ordinary Python. Actual decorators and data
expectations require the prepared Palantir transforms libraries and chosen
engine. Tenant preview/build needs enrollment access; local real-data preview
also requires administrator enablement and input download permissions.

## Procedure

1. Specify input/output schemas and the handling of nulls, duplicates, empty
   tables and unmatched references before choosing compute logic.
2. Choose single-node processing when the selected algorithm and tables fit
   its resources. Use distributed DataFrame operations for workloads needing
   Spark; avoid collecting unbounded data into a driver-side Python list.
3. Declare `Input` and `Output` resources, preserving the repository's naming
   and authorization context. Extract reusable business logic for unit tests.
4. Implement the compute function with the chosen engine's I/O API; return the
   DataFrame for `transform_df`, or explicitly write the table with
   `transform.using`. Register the module using [repository guidance](repositories.md).
5. Add output checks, run [tests](testing.md), inspect preview schemas/results
   and follow [release](releases.md). Decide incremental behavior separately
   using [transactions](transactions.md).

## Worked example

Illustrative small tables:

| Dataset | Columns and values |
| --- | --- |
| Orders | `order_id:string="o1"`, `customer_id:string="c1"`, `total_cents:long=1200` |
| Customers | `customer_id:string="c1"`, `customer_name:string="Ada"` |
| Output | `order_id`, `customer_id`, `customer_name` strings; `total_cents` long. |

The [single-node transform](../../examples/pipelines/single_node_transform.py)
calls [shared business rules](../../examples/pipelines/order_rules.py) to join
customers, reject duplicate keys, reject unresolved customers and validate
nonnegative integer amounts. Its input table conversion is intentionally
bounded to small tables; it is not a streaming or distributed algorithm.
Keep the shared module adjacent, and adapt its relative import when moving
the code into your repository package. Replace all `/EXAMPLE/...` paths with
approved resource paths verified in the tenant.

The [PySpark variant](../../examples/pipelines/pyspark_transform.py) uses a
left DataFrame join and explicit output selection. An unmatched reference
produces a null customer name, which fails its output expectation. Duplicated
customer rows can duplicate order rows, which fails the primary-key check.
The two variants use different execution APIs; tests must assess the chosen
one rather than treating a helper test as a Spark run.

From this skill's root, run the prepared Python business fixture:

```bash
python -B examples/pipelines/fixture_run.py
```

Expected joined row: `{"order_id":"o1","customer_id":"c1","customer_name":"Ada","total_cents":1200}`.
The runner also rejects duplicate order/customer keys, unresolved customers
and a negative amount. It executes shared business logic used by the real
single-node transform; it does not execute a Foundry build or its decorators.

## Expected result and checks

Preview and build output have the declared columns, types and intended row
count. The joined order retains its identity and amount and resolves `Ada`.
Failure data cannot become an accepted output. Check output schema/content,
expectation results, selected input context and build/job outcome separately.
On an empty output, explicitly inspect its published schema; do not infer
types from an empty Python record list.

## Failures and recovery

An unresolved customer requires correcting input/reference data or explicitly
changing the business rule, rather than dropping bad rows silently. Duplicate
join keys require a defined deduplication rule or input correction. Memory
failure requires reducing materialization or selecting an appropriate engine.
An API missing from the prepared runtime is a provisioning/version mismatch;
do not invent an equivalent decorator. Do not swallow a write exception:
successful execution can otherwise commit an unintended empty output.

Optional sources: [transforms](https://www.palantir.com/docs/foundry/transforms-python/transforms),
[compute engines](https://www.palantir.com/docs/foundry/transforms-python/compute-engines),
[data expectations](https://www.palantir.com/docs/foundry/transforms-python/data-expectations-getting-started).
