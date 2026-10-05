# Query operations

These records describe the `query` commands in `pal-found-functions`. Each record gives inputs, behavior, results, and examples.

### query.execute

- **Purpose and behavior:** Runs a published query with supplied parameter values and returns its computed result. Unless `--version` is set, Foundry uses the latest version on the selected branch. This older endpoint remains for compatibility; `streaming-execute` supports every query function type.
- **CLI inputs:** positionals `query_api_name`; required `--parameters`; optional `--attribution`, `--branch`, `--preview`, `--trace-parent`, `--trace-state`, `--transaction-id`, `--version`.
- **Input meaning:** `--parameters`: JSON object keyed by the action or query parameter IDs; values must match their declared types. `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--branch`: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch. `--version`: The version of the query to execute. When used with `branch`, the specified version must exist on the branch. `--attribution` identifies the calling application for attribution; `--preview` enables endpoint preview behavior when that feature is available; `--trace-parent` passes the caller's distributed trace parent identifier; `--trace-state` passes additional distributed trace state; `--transaction-id` reads or applies changes in the specified transaction; transaction support is experimental.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query is published, the caller may execute it, and supplied parameters match its declared IDs and types. Use `query get` to inspect that contract first.
- **Result:** Returns `ExecuteQueryResponse` computed from the supplied inputs.
- **Failure:** Unknown query API name, invalid parameters, or denied execution returns a structured error. A timeout leaves the execution outcome unknown.
- **Example:** `pal-found-functions query execute <QUERY_API_NAME> --parameters '{"limit":10}'`

### query.get

- **Purpose and behavior:** Gets a specific query type with the given API name. By default, this gets the latest version of the query.
- **CLI inputs:** positionals `query_api_name`; optional `--preview`, `--version`.
- **Input meaning:** `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--version`: Published version of the function to invoke; omit it to use the default published version. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query is published and the caller may inspect its metadata. No execution parameters are needed.
- **Result:** Returns `Query` for the selected query.
- **Failure:** An unknown query identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-functions query get <QUERY_API_NAME>`

### query.get_by_rid

- **Purpose and behavior:** Gets a specific query type with the given RID. By default, this gets the latest version of the query.
- **CLI inputs:** required `--rid`; optional `--include-prerelease`, `--preview`, `--version`.
- **Input meaning:** `--rid`: RID of the published query. `--version`: Published version to invoke; omit it to use the default published version. `--include-prerelease` includes prerelease query versions when true; `--preview` enables endpoint preview behavior when that feature is available.
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

- **Purpose and behavior:** Runs a published query and returns newline-delimited JSON (NDJSON). Each line is a data batch or an error. A nonstreaming function returns one line; a streaming function may return several. For example, five records in batches of three yield two data lines. This endpoint supports all query function types and uses the latest version on the selected branch unless `--version` is set.
- **CLI inputs:** positionals `query_api_name`; required `--parameters`; optional `--attribution`, `--branch`, `--ontology`, `--preview`, `--trace-parent`, `--trace-state`, `--transaction-id`, `--version`.
- **Input meaning:** `--parameters`: JSON object keyed by the action or query parameter IDs; values must match their declared types. `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--branch`: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch. `--version`: The version of the query to execute. When used with `branch`, the specified version must exist on the branch. `--attribution` identifies the calling application for attribution; `--ontology` selects the Ontology used to resolve the query's object inputs; `--preview` enables endpoint preview behavior when that feature is available; `--trace-parent` passes the caller's distributed trace parent identifier; `--trace-state` passes additional distributed trace state; `--transaction-id` reads or applies changes in the specified transaction; transaction support is experimental.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query is published and the caller may inspect or execute it; execution parameters must match its declared input names and types.
- **Result:** Writes raw UTF-8 NDJSON to stdout. Each line carries a data batch or an error; a nonstreaming function produces one line. The CLI preserves these lines regardless of the shared `--format` setting.
- **Failure:** A line of NDJSON may contain an error instead of data; inspect each line. Timeout can interrupt the stream after partial output.
- **Example:** `pal-found-functions query streaming-execute <QUERY_API_NAME> --parameters '{"limit":10}'`
