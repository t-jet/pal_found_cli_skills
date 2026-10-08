# foundry_sdk.v2.sql_queries.models.ExecuteSqlQueryRequest


ExecuteSqlQueryRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| query | query | str | required; no default | The SQL query to execute. Queries should conform to the<br>    [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT<br>    queries only. Datasets can be referenced in SQL queries by path or by RID. See the <br>    [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets)<br>    for more details. |
| fallback_branch_ids | fallbackBranchIds | typing.Optional[typing.List[core_models.BranchName]] | default None | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a<br>    is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch<br>    provided that exists. If no fallback branches are provided the default branch is used. This is<br>    `master` for most enrollments. |
| serialization_format | serializationFormat | typing.Optional[SerializationFormat] | default None | The format used to serialize query results. If not specified, defaults to `ARROW`. |

```python
class ExecuteSqlQueryRequest(core.ModelBase):
    """ExecuteSqlQueryRequest"""

    query: str
    """
    The SQL query to execute. Queries should conform to the
    [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT
    queries only. Datasets can be referenced in SQL queries by path or by RID. See the 
    [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets)
    for more details.
    """

    fallback_branch_ids: typing.Optional[typing.List[core_models.BranchName]] = pydantic.Field(alias=str("fallbackBranchIds"), default=None)  # type: ignore[literal-required]
    """
    The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a
    is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch
    provided that exists. If no fallback branches are provided the default branch is used. This is
    `master` for most enrollments.
    """

    serialization_format: typing.Optional[SerializationFormat] = pydantic.Field(alias=str("serializationFormat"), default=None)  # type: ignore[literal-required]
    """The format used to serialize query results. If not specified, defaults to `ARROW`."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.sql_queries.models.SerializationFormat](SerializationFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecuteSqlQueryRequest.md)
