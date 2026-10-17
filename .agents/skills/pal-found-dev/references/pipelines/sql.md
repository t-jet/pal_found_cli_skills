# SQL transforms

[Pipeline topics](../pipelines.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

SQL transforms maintain Spark SQL in a Code Repository and produce dataset outputs.
They support batch filtering, joins, aggregations and window calculations. They do
not support incremental transforms; choose the local [Python lifecycle](python-transforms.md)
when computation must preserve incremental state. SQL Studio and the REST SQL Query
service execute interactive queries; neither query submission nor returned rows
publishes a repository transform. See the local [REST catalog](../rest-api.md) for
SQL Query operations.

## Prerequisites

Prepare a SQL-capable Code Repository, a development branch, readable input datasets
with schemas, an allowed output location and permission to publish/build there.
Obtain case-sensitive dataset paths from the enrollment resource browser; record
their RIDs and selected data branches separately. Repository branch and dataset
branch are distinct [contexts](../branching/contexts.md).

Locally you can author the query and validate fixture arithmetic. Foundry preview,
repository checks, publishing and output builds require authorized enrollment access.
Administrators provide unavailable runtime/resource queues and permissions. A local
SQL engine is not proof of Foundry dialect or publication support.

## Procedure

1. Use the SQL repository template or add a SQL transform through its authoring UI.
   Choose an output and add the source datasets; inspect the resulting dependency
   graph before computing. Do not invent Python decorator bindings for SQL.
2. Write `CREATE TABLE` with the output's backtick-quoted path and a `SELECT` whose
   dataset paths declare inputs. Omit the terminating semicolon. Dataset, column and
   alias case matters. Name every calculated column. In `WHERE` and `GROUP BY`, use
   expressions or a subquery rather than referring to an alias from the same select.
3. Specify retained columns, casts, join keys, null policy and duplicate handling.
   Avoid `SELECT *` when consumers depend on a stable schema.
4. Preview on the intended branches; compare column names/types and values to the
   fixture below. Preview sampling cannot establish production cardinality.
5. Save, run repository checks, propose review and publish the approved revision.
   Follow [release steps](releases.md) to build the output on its intended branch.
   Record build status and the committed output transaction, not only preview rows.

## Worked example

Illustrative input `/Demo/orders`: `order_id STRING`, `customer_id STRING`,
`amount DECIMAL(12,2)`. Rows: `(o1,c1,10.00)`, `(o2,c1,7.50)`, `(o3,c2,NULL)`.
`/Demo/customers`: `customer_id STRING`, `region STRING`. Rows: `(c1,West)`,
`(c2,East)`. Require unique customer keys before joining; duplicate keys multiply
orders. Null amounts count as zero for this particular business rule.

```sql
CREATE TABLE `/Demo/customer_totals` AS
SELECT
    o.customer_id AS customer_id,
    c.region AS region,
    CAST(SUM(COALESCE(o.amount, 0)) AS DECIMAL(12,2)) AS total_amount,
    COUNT(*) AS order_count
FROM `/Demo/orders` o
JOIN `/Demo/customers` c ON o.customer_id = c.customer_id
GROUP BY o.customer_id, c.region
```

Expected rows, independent of ordering: `(c1,West,17.50,2)`, `(c2,East,0.00,1)`.
The same [query asset](../../examples/sql/customer_totals.sql) has a
[local arithmetic fixture](../../examples/sql/verify_fixture.py). Run `python -B verify_fixture.py`
from that example directory with prepared Python. It uses SQLite to check this
query's join/null arithmetic, not Spark decimal types, Foundry grammar or publication.
Output schema: two strings, decimal `(12,2)`, and Spark `BIGINT` count. An inner join
excludes unmatched customer IDs; replace it with a left join only when keeping such
orders is intended, and then define the null-region policy. Duplicate customer keys
are an input-quality failure, not a reason to blindly apply `DISTINCT` to the result.

## Expected result and checks

Check input key uniqueness, unmatched keys, output key uniqueness, totals and schema.
Add a second `c1` customer row to demonstrate join multiplication and reject that
fixture before release. Verify the null rule explicitly with `o3`.

Preview success means the selected sample computed. Published checks mean a revision
is available. A running build is pending. Completion requires a successful build and
visible committed data on the requested output branch. A failed build can leave the
previous successful output visible; inspect its transaction/build identity.

## Failures and recovery

| Observation | Diagnosis and next step |
| --- | --- |
| Parse error | Remove trailing semicolon; verify CTAS and backticks, not another SQL dialect. |
| Missing dataset/column | Compare exact case, resource path, input schema and permissions. |
| Unexpected totals | Check duplicate join keys, unmatched inputs, null policy and preview sampling. |
| Incremental state required | Move that workload to Python; repeated SQL builds remain batch computations. |
| Published code but stale output | Inspect build/branch and upstream freshness; fix cause before rebuilding. |
| Missing enrollment/runtime | Finish authoring and fixture plan locally; record the blocked preview/build step. |

Optional source attribution: [SQL overview](https://www.palantir.com/docs/foundry/transforms-sql/overview),
[Spark SQL syntax](https://www.palantir.com/docs/foundry/transforms-sql/spark-reference),
[batch repository pipeline](https://www.palantir.com/docs/foundry/building-pipelines/create-batch-pipeline-cr).
