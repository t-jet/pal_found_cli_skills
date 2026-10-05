# Ontology operations

These records describe the `ontology` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### ontology.get

- **Purpose and behavior:** Gets a specific ontology for a given Ontology API name or RID.
- **CLI inputs:** positionals `ontology`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can see the requested ontology; metadata reads require its RID or API name where the command asks for one.
- **Result:** Returns `OntologyV2` for the selected ontology.
- **Failure:** An unknown ontology identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies ontology get palantir`

### ontology.get_full_metadata

- **Purpose and behavior:** Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces. This endpoint is designed to return as much metadata as possible in a single request to support OSDK workflows. It may omit certain entities rather than fail the request.
- **CLI inputs:** positionals `ontology`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to load metadata from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can see the requested ontology; metadata reads require its RID or API name where the command asks for one.
- **Result:** Returns `OntologyFullMetadata` for the selected ontology.
- **Failure:** An unknown ontology identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies ontology get-full-metadata palantir`

### ontology.list

- **Purpose and behavior:** Lists the Ontologies visible to the current user.
- **CLI inputs:** .
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can see the requested ontology; metadata reads require its RID or API name where the command asks for one.
- **Result:** Returns `ListOntologiesV2Response` containing the visible matching ontology entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-ontologies ontology list`

### ontology.load_metadata

- **Purpose and behavior:** Load Ontology metadata for the requested object, link, action, query, and interface types.
- **CLI inputs:** positionals `ontology`; optional `--action-types`, `--interface-types`, `--link-types`, `--object-types`, `--query-types`, `--branch`, `--preview`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to load metadata from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--action-types` selects action type metadata to include; `--interface-types` selects interface type metadata to include; `--link-types` selects link type metadata to include; `--object-types` selects object type metadata to include; `--preview` enables endpoint preview behavior when that feature is available; `--query-types` selects query type metadata to include.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can see the requested ontology; metadata reads require its RID or API name where the command asks for one.
- **Result:** Returns `OntologyFullMetadata` for this ontology request.
- **Failure:** An unknown ontology identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies ontology load-metadata palantir --action-types '[]' --interface-types '[]' --link-types '[]' --object-types '[]' --query-types '[]'`
