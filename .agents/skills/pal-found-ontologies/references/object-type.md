# Object type operations

These records describe the `object_type` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### object_type.get

- **Purpose and behavior:** Gets a specific object type with the given API name.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `ObjectTypeV2` for the selected object type.
- **Failure:** An unknown object type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies object-type get palantir employee`

### object_type.get_by_rid_batch

- **Purpose and behavior:** Gets a list of object types by RID in bulk. Object types are filtered from the response if they don't exist or the requesting token lacks the required permissions. The maximum batch size for this endpoint is 100.
- **CLI inputs:** positionals `ontology`; optional `--requests`, `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to load the object type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--requests` supplies a JSON array of individual request objects for the batch call.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `GetObjectTypeByRidBatchResponse` for the selected object type.
- **Failure:** Inaccessible or missing requested RIDs may be omitted from the batch response; compare returned entries with the request.
- **Example:** `pal-found-ontologies object-type get-by-rid-batch palantir --requests '[{"objectTypeRid":"ri.ontology.main.object-type.example"}]'`

### object_type.get_edits_history

- **Purpose and behavior:** Returns the history of edits (additions, modifications, deletions) for objects of a specific object type. This endpoint provides visibility into all actions that have modified objects of this type. The edits are returned in reverse chronological order (most recent first) by default. Note that filters are ignored for OSv1 object types.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--page-size`, `--page-token`, `--branch`, `--filters`, `--include-all-previous-properties`, `--object-primary-key`, `--sort-order`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch from which we will get edits history. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. `--filters` filters object edit history using the SDK edit-history filter schema; `--include-all-previous-properties` includes all prior object property values in edit history when true; `--object-primary-key` selects the object whose edit history to read by primary-key value; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--sort-order` sets ascending or descending edit-history order.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `ObjectTypeEditsHistoryResponse` for the selected object type.
- **Failure:** An unknown object type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies object-type get-edits-history palantir Employee`

### object_type.get_full_metadata

- **Purpose and behavior:** Gets the full metadata for a specific object type with the given API name.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--branch`, `--preview`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--preview` enables endpoint preview behavior when that feature is available; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `ObjectTypeFullMetadata` for the selected object type.
- **Failure:** An unknown object type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies object-type get-full-metadata palantir employee`

### object_type.get_outgoing_link_type

- **Purpose and behavior:** Get an outgoing link for an object type.
- **CLI inputs:** positionals `ontology`, `object_type`, `link_type`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `link_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `LinkTypeSideV2` for the selected object type.
- **Failure:** An unknown object type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies object-type get-outgoing-link-type palantir Employee directReport`

### object_type.list

- **Purpose and behavior:** Lists the object types for the given Ontology. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.
- **CLI inputs:** positionals `ontology`; optional `--page-size`, `--page-token`, `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `ListObjectTypesV2Response` containing the visible matching object type entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-ontologies object-type list palantir`

### object_type.list_outgoing_link_types

- **Purpose and behavior:** List the outgoing links for an object type.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--page-size`, `--page-token`, `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The ontology is visible and the object type API name, RID, or outgoing link type identifies a defined type.
- **Result:** Returns `ListOutgoingLinkTypesResponseV2` containing the visible matching object type entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-ontologies object-type list-outgoing-link-types palantir Flight`
