# Query type operations

These records describe the `query_type` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### query_type.get

- **Purpose and behavior:** Gets a specific query type with the given API name.
- **CLI inputs:** positionals `ontology`, `query_api_name`; optional `--sdk-package-rid`, `--sdk-version`, `--version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `query_api_name`: Published query API name; discover it with query metadata, not a query RID. `--version`: The version of the Query to get. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can inspect the query type in the selected ontology.
- **Result:** Returns `QueryTypeV2` for the selected query type.
- **Failure:** An unknown query type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies query-type get palantir getEmployeesInCity`

### query_type.list

- **Purpose and behavior:** Lists the query types for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.
- **CLI inputs:** positionals `ontology`; optional `--page-size`, `--page-token`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from stderr metadata's `next_page_token`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can inspect the query type in the selected ontology.
- **Result:** CLI prints a list of query types; page count and any continuation token appear in stderr metadata. SDK page model: `ListQueryTypesResponseV2`. An empty list means no entries in the fetched pages; follow a continuation token if present.
- **Failure:** An unknown ontology or denied read scope produces a structured error; an empty successful list is not an error.
- **Example:** `pal-found-ontologies query-type list palantir`
