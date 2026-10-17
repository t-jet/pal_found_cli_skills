# v2.sql_queries resources and operations


Use SQL query resources for permitted Foundry dataset reads. Author the documented SELECT dialect, select branch and result format, then decode the returned Arrow or other declared payload and verify row/schema expectations within a byte budget. Read the selected operation contract before invocation; stage, API version and result lifetime remain operation-specific.

| Operation | Stage |
| --- | --- |
| [v2.sql_queries.SqlQuery.cancel](../../contracts/v2/sql_queries/SqlQuery/cancel.md) | Stable |
| [v2.sql_queries.SqlQuery.execute](../../contracts/v2/sql_queries/SqlQuery/execute.md) | Stable |
| [v2.sql_queries.SqlQuery.execute_ontology](../../contracts/v2/sql_queries/SqlQuery/execute_ontology.md) | Public Beta |
| [v2.sql_queries.SqlQuery.get_results](../../contracts/v2/sql_queries/SqlQuery/get_results.md) | Stable |
| [v2.sql_queries.SqlQuery.get_status](../../contracts/v2/sql_queries/SqlQuery/get_status.md) | Stable |

[All services](../../catalog.md) | [SDK handling](../../client-behavior.md)

[Part 1](index.md)
