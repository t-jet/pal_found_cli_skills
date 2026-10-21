# Query operations

These records describe the `query` commands in `pal-found-functions`. Each record gives inputs, behavior, results, and examples.

### query.execute

- **Purpose and behavior:** Runs a global query with supplied parameter values and returns its computed result as one JSON object. Unless `--version` is set, Foundry uses the latest published version on the selected branch, which may be a prerelease. For an Ontology-scoped function, use `streaming-execute` with `--ontology`.
- **CLI inputs:** positionals `query_api_name`; required `--parameters`; optional `--attribution`, `--branch`, `--preview`, `--trace-parent`, `--trace-state`, `--transaction-id`, `--version`.
- **Input meaning:** `--parameters`: JSON object keyed by the query's parameter IDs; values must match their declared types. `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--branch`: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch. `--version`: The version of the query to execute. When used with `branch`, the specified version must exist on the branch. `--attribution` is a plain string identifying the calling application; `--preview` enables endpoint preview behavior when that feature is available; `--trace-parent` passes the caller's distributed trace parent identifier; `--trace-state` passes additional distributed trace state; `--transaction-id` selects a transaction to read from. Transactions are experimental and may not support every workflow.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query is published, the caller may execute it, and supplied parameters match its declared IDs and types. Use `query get` to inspect that contract first.
- **Result:** Returns `ExecuteQueryResponse` computed from the supplied inputs.
- **Failure:** Unknown query API name, invalid parameters, or denied execution returns a structured error. A timeout leaves the execution outcome unknown.
- **Example:** `pal-found-functions query execute <QUERY_API_NAME> --parameters '{"limit":10}'`

### query.get

- **Purpose and behavior:** Gets a specific query type with the given API name. By default, this gets the latest version of the query.
- **CLI inputs:** positionals `query_api_name`; optional `--preview`, `--version`.
- **Input meaning:** `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--version`: Version of the query metadata to retrieve; omit it to get the latest version. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query is published and the caller may inspect its metadata. No execution parameters are needed.
- **Result:** Returns `Query` for the selected query.
- **Failure:** An unknown query identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-functions query get <QUERY_API_NAME>`

### query.get_by_rid

- **Purpose and behavior:** Gets a specific query type with the given RID. By default, this gets the latest version of the query.
- **CLI inputs:** required `--rid`; optional `--include-prerelease`, `--preview`, `--version`.
- **Input meaning:** `--rid`: RID of the published query. `--version`: Version of the query metadata to retrieve; omit it to get the latest stable version. `--include-prerelease` allows prerelease versions when resolving the latest version; by default, only stable versions are considered; `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query RID identifies a published query the caller may inspect. No execution parameters are needed.
- **Result:** Returns `Query` for the selected query.
- **Failure:** An unknown query identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-functions query get-by-rid --rid <RID>`

### query.get_by_rid_batch

- **Purpose and behavior:** Gets a list of query types by RID in bulk. By default, this gets the latest version of each query. Queries are filtered from the response if they don't exist or the requesting token lacks the required permissions. The maximum batch size for this endpoint is 100.
- **CLI inputs:** positionals `body`; optional `--preview`.
- **Input meaning:** `body`: JSON array of request objects in the SDK request-element schema. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** Supply at most 100 query RIDs; the caller needs read access to each returned query. Missing and inaccessible entries are omitted.
- **Result:** Returns `GetByRidQueriesBatchResponse` for the selected query.
- **Failure:** Inaccessible or missing requested RIDs may be omitted from the batch response; compare returned entries with the request.
- **Example:** `pal-found-functions query get-by-rid-batch '[{"rid":"ri.function-registry.main.function.example"}]'`

### query.streaming_execute

- **Purpose and behavior:** Runs a query through the SDK's Server-Sent Events (SSE) endpoint. The CLI buffers each event's JSON payload and writes the complete output as newline-delimited JSON (NDJSON). Each line is a data batch (`"type":"data"`) or an execution error (`"type":"error"`). A nonstreaming function produces one data line; a streaming function may produce several. This endpoint supports all query function types and uses the latest published version on the selected branch unless `--version` is set. The latest version may be a prerelease.
- **CLI inputs:** positionals `query_api_name`; required `--parameters`; optional `--attribution`, `--branch`, `--ontology`, `--preview`, `--trace-parent`, `--trace-state`, `--transaction-id`, `--version`.
- **Input meaning:** `--parameters`: JSON object keyed by the query's parameter IDs; values must match their declared types. `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--branch`: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch. `--version`: The version of the query to execute. When used with `branch`, the specified version must exist on the branch. `--attribution` is a plain string identifying the calling application; `--ontology` takes an Ontology RID or API name and selects an Ontology-scoped function. Omit it to execute a global function. `--preview` enables endpoint preview behavior when that feature is available; `--trace-parent` passes the caller's distributed trace parent identifier; `--trace-state` passes additional distributed trace state; `--transaction-id` selects a transaction to read from. Transactions are experimental and may not support every workflow.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query is published and the caller may inspect or execute it; execution parameters must match its declared input names and types.
- **Result:** After consuming and closing the SSE stream, writes buffered UTF-8 NDJSON to stdout. Each data line has a `value` containing the result batch. An error line carries the execution error details. The shared `--format` and `--pretty` options do not reformat this output.
- **Failure:** Inspect every line for `"type":"error"`, even when the command exits successfully. A transport failure or timeout before stream completion returns a CLI error and writes no partial NDJSON. Earlier data from that incomplete attempt is not printed.
- **Example:** `pal-found-functions query streaming-execute <QUERY_API_NAME> --parameters '{"limit":10}'`
