# Model version operations

These records describe the `model_version` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

## API and serialization scope

SDK 1.101.0 `modelApi` has `inputs` and `outputs` arrays. Each input/output is
`parameter` or `tabular` (the SDK also carries an `unsupported` marker).
A parameter has `name`, optional `required` (default true), and `dataType`:
`{"type":"parameter","name":"threshold","dataType":{"type":"double"}}`.
A tabular entry has `name`, optional `required`, `columns`, and optional
`format` (`PANDAS`, the default, or `SPARK`). Columns have `name`, optional
`required` (default true), and `dataType`; false allows null/omitted values.

Data type objects use `type`: `date`, `boolean`, `string`, `double`, `integer`,
`float`, `long`, `timestamp`, or `any`. Arrays add recursive `itemType`:
`{"type":"array","itemType":{"type":"double"}}`. Maps add recursive
`keyType` and `valueType`:
`{"type":"map","keyType":{"type":"string"},"valueType":{"type":"any"}}`.
`any` has no additional fields. The SDK's `unsupported` marker represents a type
it cannot describe; it does not promise a usable model interface. Type-shape
validation does not establish adapter compatibility or runtime value semantics.

`ModelFiles` in this baseline is **only** `DillModelFiles`, with `type=dill`
and required `serializedModelFunction` containing base64 dill-serialized model
function bytes. There are no alternative model-files variants in this create
contract. Other lifecycle integration sources do not imply this command accepts
container images or external endpoint configuration.

Version responses contain `rid`, `modelApi`, `condaRequirements`,
`backingRepositories`, `createdTime`, optional `source`, and optional
`linkedExperiment`. The source discriminator may be `sdk`, `external`,
`importedContainerizedModel`, `modelStudio` (with `modelStudioRid`),
`codeRepository` (with `repositoryRid`, `branch`), `codeWorkspace` (with
`codeWorkspaceRid`, `branch`), or `promoted` (with `previousModelRid` and
`previousModelVersionRid`). Missing source/link fields leave provenance or
experiment association unspecified. Read a linked experiment using the owning
model and returned experiment RID. Creation/get success establishes a version
record; artifact loadability, training quality, and deployment readiness still
require validation in the intended runtime.

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
- **CLI inputs:** positionals `model_rid`; optional `--page-size`, `--page-token`, `--all`, `--max-pages`.
- **Input meaning:** `model_rid` identifies the model whose versions will be listed. Use `next_page_token` from stderr metadata as `--page-token` to fetch another page. `--page-size` sets the requested maximum entries in one result page. By default, the CLI fetches one page. `--max-pages` fetches up to the given number of pages; `--all` fetches until no cursor remains or the configured limit of at most 40 pages is reached. If both are set, `--all` takes precedence.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can read its versions.
- **Result:** Prints model version entries as a list on stdout. Pagination metadata, including `next_page_token` when another page exists, follows a separator on stderr. An empty list means this page contains no entries; follow a returned token to check the next page.
- **Failure:** An unknown model or missing read permission returns a structured error.
- **Example:** `pal-found-models model-version list <MODEL_RID>`
