# Action operations

These records describe the `action` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### action.apply

- **Purpose and behavior:** Applies an action using the given parameters. Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible. Edits to objects or links in Object Storage V2 will be visible immediately after the action completes. Note that a 200 HTTP status code only indicates that the request was received and processed by the server. See the validation result in the response body to determine if the action was applied successfully. Note that parameter default values are not currently supported by this endpoint.
- **CLI inputs:** positionals `ontology`, `action`; optional `--parameters`, `--branch`, `--options`, `--sdk-package-rid`, `--sdk-version`, `--transaction-id`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `action`: API name defined in the ontology; discover it through the corresponding metadata command. `--parameters`: JSON object keyed by the action or query parameter IDs; values must match their declared types. `--branch`: The Foundry branch to apply the action against. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. `--options` supplies SDK action execution options as a JSON object; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--transaction-id` reads or applies changes in the specified transaction; transaction support is experimental.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The action type exists, the caller may apply it, and parameters satisfy its declared schema and rules.
- **Result:** Returns `SyncApplyActionResponseV2`; inspect its validation result to determine whether the action applied. HTTP 200 alone means only that the server processed the request.
- **Failure:** Schema or rule validation can fail inside a processed response; inspect the validation result. A timeout leaves the edit outcome unknown.
- **Example:** `pal-found-ontologies action apply palantir rename-employee --parameters '{"id":80060,"newName":"Anna Smith-Doe"}'`

### action.apply_batch

- **Purpose and behavior:** Applies multiple actions (of the same Action Type) using the given parameters. Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible. Edits to objects or links in Object Storage V2 will be visible immediately after the action completes. Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not call Functions may receive a higher limit. Note that notifications are not currently supported by this endpoint.
- **CLI inputs:** positionals `ontology`, `action`; optional `--requests`, `--branch`, `--options`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology` selects the Ontology by API name or RID; `action` is an action type API name from `action-type list`. `--requests` is an array of request objects, each with its own `parameters` object keyed by action parameter IDs. `--branch` selects an experimental Foundry branch; omit it for the default branch. `--options` supplies SDK action execution options as a JSON object; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The action type exists, the caller may apply it, and parameters satisfy its declared schema and rules.
- **Result:** Returns `BatchApplyActionResponseV2` with results for the submitted action requests; inspect each validation result before assuming edits applied.
- **Failure:** Schema or rule validation can fail inside a processed response; inspect the validation result. A timeout leaves the edit outcome unknown.
- **Example:** `pal-found-ontologies action apply-batch palantir rename-employee --requests '[{"parameters":{"id":80060,"newName":"Anna Smith-Doe"}},{"parameters":{"id":80061,"newName":"Joe Bloggs"}}]'`

### action.apply_with_overrides

- **Purpose and behavior:** Same as regular apply action operation, but allows specifying overrides for UniqueIdentifier and CurrentTime generated action parameters.
- **CLI inputs:** positionals `ontology`, `action`; optional `--overrides`, `--request`, `--branch`, `--sdk-package-rid`, `--sdk-version`, `--transaction-id`.
- **Input meaning:** `ontology` selects the Ontology by API name or RID; `action` is an action type API name from `action-type list`. `--request` contains a single apply request with its `parameters` object. `--overrides` supplies generated UniqueIdentifier values or an action execution time when the action requires them. `--branch` selects an experimental Foundry branch; omit it for the default branch. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--transaction-id` reads or applies changes in the specified transaction; transaction support is experimental.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The action type exists, the caller may apply it, and parameters satisfy its declared schema and rules.
- **Result:** Returns `SyncApplyActionResponseV2`; inspect its validation result before assuming edits applied.
- **Failure:** Schema or rule validation can fail inside a processed response; inspect the validation result. A timeout leaves the edit outcome unknown.
- **Example:** `pal-found-ontologies action apply-with-overrides palantir rename-employee --overrides '{"uniqueIdentifierLinkIdValues":{"fd28fa5c-3028-4eca-bdc8-3be2c7949cd9":"4efdb11f-c1e3-417c-89fb-2225118b65e3"},"actionExecutionTime":"2025-10-25T13:00:00Z"}' --request '{"parameters":{"id":80060,"newName":"Anna Smith-Doe"}}'`
