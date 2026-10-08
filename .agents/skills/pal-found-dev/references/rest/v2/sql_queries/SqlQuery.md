# SQL query execution and result retrieval

[SQL operations](index.md) | [REST client behavior](../../client-behavior.md)

## Concept and prerequisites

The SQL Queries API submits a query, tracks its ID and returns results separately. Only the user who invoked a query can operate on it. Query results are limited to one million rows by default; design bounded selection and paging/storage behavior before running expensive work. Prepare SQL text, an authorized identity, accessible datasets and branch choices. `execute_ontology` is a different, synchronous Ontology SQL route with Arrow output.

## Procedure and operations

| Operation | Use and check |
| --- | --- |
| [execute](../../contracts/v2/sql_queries/SqlQuery/execute.md) ([fixture](../../../../examples/rest/089/v2/sql_queries/SqlQuery/invoke_execute.py)) | Submit SQL with optional fallback branch IDs and serialization format. Retain returned query ID; submission does not mean result availability. Default result format is Apache Arrow. |
| [get_status](../../contracts/v2/sql_queries/SqlQuery/get_status.md) ([fixture](../../../../examples/rest/089/v2/sql_queries/SqlQuery/invoke_get_status.py)) | Poll a known query ID with finite attempts and a deadline. Distinguish running, success and failure before retrieving data. |
| [get_results](../../contracts/v2/sql_queries/SqlQuery/get_results.md) ([fixture](../../../../examples/rest/089/v2/sql_queries/SqlQuery/invoke_get_results.py)) | Fetch results in the format selected at submission. This route long polls and times out after one minute; retry while the same query still runs, preserving its ID and the overall deadline. Close/consume the response according to the SDK wrapper mode. |
| [cancel](../../contracts/v2/sql_queries/SqlQuery/cancel.md) ([fixture](../../../../examples/rest/089/v2/sql_queries/SqlQuery/invoke_cancel.py)) | Request cancellation of a running query. A query already stopped yields an effective no-op. Check status if the final state matters. |
| [execute_ontology](../../contracts/v2/sql_queries/SqlQuery/execute_ontology.md) ([fixture](../../../../examples/rest/089/v2/sql_queries/SqlQuery/invoke_execute_ontology.py)) | Execute Ontology SQL synchronously. Select Ontology, optional branch and parameters; decode Apache Arrow results and apply a finite row/byte budget. A dry run checks the query without treating it as a normal result execution. |

## Worked example and expected result

Each linked contract has a matching [offline SDK fixture](../../../../examples/rest/089/v2/sql_queries/SqlQuery/invoke_get_results.py) for request, response and declared errors. Run `python -B examples/rest/089/v2/sql_queries/SqlQuery/invoke_get_results.py` from the skill root to inspect the result transport. For an application flow, submit one query, retain its ID, poll status, then retrieve results in the chosen format and validate expected columns/row count. Ontology SQL does not use this submit/status/result sequence.

## Failures and recovery

Denied access needs identity and dataset/Ontology grant checks; another user's query ID cannot be reused. A timed-out result long poll does not imply query failure; retry the same ID within a finite budget. A timed-out submit is ambiguous and must be reconciled before another potentially expensive execution. Cancellation may race with success; inspect status. Avoid logging sensitive SQL parameters or result rows while diagnosing errors.

## Access boundary

Offline fixtures use synthetic SQL and transport. Live SQL execution, result retrieval, cancellation and data access require authorized enrollment; fixtures do not prove a query's performance or tenant schema.
