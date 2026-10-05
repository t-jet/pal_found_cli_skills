# Action type full metadata operations

These records describe the `action_type_full_metadata` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### action_type_full_metadata.get

- **Purpose and behavior:** Gets the full metadata associated with an action type.
- **CLI inputs:** positionals `ontology`, `action_type`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `action_type`: The name of the action type in the API. `--branch`: The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can inspect the action type in the selected ontology.
- **Result:** Returns `ActionTypeFullMetadata` for the selected action type full metadata.
- **Failure:** An unknown action type full metadata identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies action-type-full-metadata get palantir promote-employee`

### action_type_full_metadata.list

- **Purpose and behavior:** Lists the action types (with full metadata) for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.
- **CLI inputs:** positionals `ontology`; optional `--page-size`, `--page-token`, `--branch`, `--object-type-api-names`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--object-type-api-names` filters action metadata to the named object types; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can inspect the action type in the selected ontology.
- **Result:** Returns `ListActionTypesFullMetadataResponse` containing the visible matching action type full metadata entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-ontologies action-type-full-metadata list palantir`
