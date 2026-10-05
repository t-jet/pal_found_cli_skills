# Model version operations

These records describe the `model_version` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model_version.create

- **Purpose and behavior:** Creates a new Model Version on an existing model.
- **CLI inputs:** positionals `model_rid`; required `--backing-repositories-json`, `--conda-requirements-json`, `--model-api-json`, `--model-files-json`.
- **Input meaning:** `--backing-repositories-json` is an array of repository RIDs containing code or dependencies needed by the model. `--conda-requirements-json` is an array of Conda requirement strings such as `"numpy==1.24.0"`. `--model-api-json` declares named inputs and outputs, their data types, and tabular columns and formats where applicable. `--model-files-json` supplies serialized model data; the SDK's `dill` variant requires `{"type":"dill","serializedModelFunction":"<BASE64_DILL_FUNCTION>"}`. `model_rid` is the RID of the owning model.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can access it; creation needs valid model API and backing repository/file definitions.
- **Result:** Returns the created `ModelVersion` with its server-assigned identifier.
- **Failure:** Unknown model, invalid model API/files, or missing write permission returns a structured error; check versions before retrying a timed-out creation.
- **Example:** `pal-found-models model-version create <MODEL_RID> --backing-repositories-json '["<REPOSITORY_RID>"]' --conda-requirements-json '["numpy==1.24.0"]' --model-api-json '{"inputs":[{"name":"features","required":true,"type":"tabular","columns":[{"name":"score","required":true,"dataType":{"type":"double"}}],"format":"PANDAS"}],"outputs":[{"name":"prediction","required":true,"type":"tabular","columns":[{"name":"value","required":true,"dataType":{"type":"double"}}],"format":"PANDAS"}]}' --model-files-json '{"type":"dill","serializedModelFunction":"<BASE64_DILL_FUNCTION>"}'`. Replace `<BASE64_DILL_FUNCTION>` with actual base64 output of dill serialization of a model function, and use a model API that matches that function's inputs and outputs. The literal placeholder is not a usable model artifact.

### model_version.get

- **Purpose and behavior:** Retrieves a Model Version by its Resource Identifier (RID).
- **CLI inputs:** positionals `model_rid`, `model_version_rid`.
- **Input meaning:** `model_rid` identifies the owning model; `model_version_rid` identifies one version under that model.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model and version exist, and the caller can read them.
- **Result:** Returns `ModelVersion` for the selected model version.
- **Failure:** An unknown model or version, or missing read permission, returns a structured error.
- **Example:** `pal-found-models model-version get <MODEL_RID> <MODEL_VERSION_RID>`

### model_version.list

- **Purpose and behavior:** Lists all Model Versions for a given Model.
- **CLI inputs:** positionals `model_rid`; optional `--page-size`, `--page-token`.
- **Input meaning:** `model_rid` identifies the model whose versions will be listed. Use the returned `nextPageToken` as `--page-token` to fetch another page. `--page-size` sets the requested maximum entries in one result page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can read its versions.
- **Result:** Returns `ListModelVersionsResponse` containing the visible matching model version entries; an empty page means none matched that page.
- **Failure:** An unknown model or missing read permission returns a structured error.
- **Example:** `pal-found-models model-version list <MODEL_RID>`
