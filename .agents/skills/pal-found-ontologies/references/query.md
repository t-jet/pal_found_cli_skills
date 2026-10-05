# Query operations

These records describe the `query` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### query.execute

- **Purpose and behavior:** Executes a Query using the given parameters. By default, the latest version of the Query is executed. Optional parameters do not need to be supplied.
- **CLI inputs:** positionals `ontology`, `query_api_name`; optional `--parameters`, `--attribution`, `--branch`, `--sdk-package-rid`, `--sdk-version`, `--transaction-id`, `--version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--parameters`: JSON object keyed by the action or query parameter IDs; values must match their declared types. `--branch`: The Foundry branch to execute the query from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. When provided without `version`, the latest version on this branch is used, including pre-release versions. When provided with `version`, the specified version must exist on the branch. `--attribution` identifies the calling application for attribution; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--transaction-id` reads or applies changes in the specified transaction; transaction support is experimental; `--version` selects a specific published query version instead of the latest.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The query type exists in the ontology and the caller may execute it with parameters matching its declaration.
- **Result:** Returns `ExecuteQueryResponse` computed from the supplied inputs.
- **Failure:** Unknown query type, parameter mismatch, or denied execution returns an error; a timeout leaves execution outcome unknown.
- **Example:** `pal-found-ontologies query execute palantir getEmployeesInCity --parameters '{"city":"New York"}'`
