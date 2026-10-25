# Function identifiers and parameters

`query execute`, `query streaming-execute`, and `query get` take the published
query API name, not its RID. `get-by-rid` takes `--rid`; `get-by-rid-batch`
takes a JSON array of objects with a `rid` field. The batch endpoint returns
at most 100 requested queries and omits missing or inaccessible entries.

`--parameters` is a JSON object keyed by the published query's parameter IDs.
`--attribution` is a plain string, such as `my-app`; it is not JSON-decoded.
Inspect `query get` first to learn the parameter names and declared types.
Values follow the SDK's `DataValue` encoding; for example a numeric `limit`
is `--parameters '{"limit":10}'`. `--version` selects a published function
version; without it execution uses the latest version, which may be a
prerelease. With `--branch`, that version must exist on the branch. `--transaction-id` selects a transaction to
read from; transactions are experimental and may not support every workflow.
For `streaming-execute`, `--ontology` selects an Ontology-scoped function by
Ontology RID or API name; omitting it selects a global function.

`streaming-execute` consumes SDK Server-Sent Events (SSE), buffers their JSON
payloads, and writes NDJSON lines after the stream completes. Each line contains
data or an execution error. Check every line's `type`; an error line can appear
even when the command exits successfully. A transport failure or timeout before
completion produces no partial NDJSON on stdout.

`value-type get` takes a value type RID. `version-id get` takes that RID and
a version ID. These commands inspect type metadata and do not execute query
logic.
