# Function identifiers and parameters

`query execute`, `query streaming-execute`, and `query get` take the published
query API name, not its RID. `get-by-rid` takes `--rid`; `get-by-rid-batch`
takes a JSON array of objects with a `rid` field. The batch endpoint returns
at most 100 requested queries and omits missing or inaccessible entries.

`--parameters` is a JSON object keyed by the published query's parameter IDs.
Inspect `query get` first to learn the parameter names and declared types.
Values follow the SDK's `DataValue` encoding; for example a numeric `limit`
is `--parameters '{"limit":10}'`. `--version` selects a published function
version; without it execution uses the latest version. With `--branch`, that
version must exist on the branch. `streaming-execute` returns NDJSON lines
containing data or an error.

`value-type get` takes a value type RID. `version-id get` takes that RID and
a version ID. These commands inspect type metadata and do not execute query
logic.
