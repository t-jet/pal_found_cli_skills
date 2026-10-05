# Action type operations

These records describe the `action_type` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### action_type.get

- **Purpose and behavior:** Gets a specific action type with the given API name.
- **CLI inputs:** positionals `ontology`, `action_type`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `action_type`: The name of the action type in the API. `--branch`: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the action type API name or RID identifies a defined action.
- **Result:** Returns `ActionTypeV2` for the selected action type.
- **Failure:** An unknown action type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies action-type get palantir promote-employee`

### action_type.get_by_rid

- **Purpose and behavior:** Gets a specific action type with the given RID.
- **CLI inputs:** positionals `ontology`, `action_type_rid`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `action_type_rid`: Resource identifier (RID) of the named Foundry resource. `--branch`: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the action type API name or RID identifies a defined action.
- **Result:** Returns `ActionTypeV2` for the selected action type.
- **Failure:** An unknown action type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies action-type get-by-rid palantir ri.ontology.main.action-type.7ed72754-7491-428a-bb18-4d7296eb2167`

### action_type.get_by_rid_batch

- **Purpose and behavior:** Gets a list of action types by RID in bulk. Action types are filtered from the response if they don't exist or the requesting token lacks the required permissions. The maximum batch size for this endpoint is 100.
- **CLI inputs:** positionals `ontology`; optional `--requests`, `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--requests` supplies a JSON array of individual request objects for the batch call.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the action type API name or RID identifies a defined action.
- **Result:** Returns `GetActionTypeByRidBatchResponse` for the selected action type.
- **Failure:** Inaccessible or missing requested RIDs may be omitted from the batch response; compare returned entries with the request.
- **Example:** `pal-found-ontologies action-type get-by-rid-batch palantir --requests '[{"actionTypeRid":"ri.ontology.main.action-type.example"}]'`

### action_type.list

- **Purpose and behavior:** Lists the action types for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.
- **CLI inputs:** positionals `ontology`; optional `--page-size`, `--page-token`, `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the action type API name or RID identifies a defined action.
- **Result:** Returns `ListActionTypesResponseV2` containing the visible matching action type entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-ontologies action-type list palantir`
