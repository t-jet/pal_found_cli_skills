# Model studio operations

These records describe the `model_studio` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model_studio.create

- **Purpose and behavior:** Creates a new Model Studio.
- **CLI inputs:** required `--name`, `--parent-folder-rid`.
- **Input meaning:** `--name`: The name of the Model Studio. `--parent-folder-rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio RID or target folder exists and the caller has the required access.
- **Result:** Returns the created `ModelStudio` with its server-assigned identifier.
- **Failure:** Invalid model studio inputs or insufficient permission produce a structured error. After a timeout, read current state before retrying.
- **Example:** `pal-found-models model-studio create --name 'Order forecast' --parent-folder-rid ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791`

### model_studio.get

- **Purpose and behavior:** Gets details about a Model Studio by its RID.
- **CLI inputs:** positionals `model_studio_rid`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio RID or target folder exists and the caller has the required access.
- **Result:** Returns `ModelStudio` for the selected model studio.
- **Failure:** An unknown model studio identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-models model-studio get <MODEL_STUDIO_RID>`

### model_studio.launch

- **Purpose and behavior:** Launches a new training run for the Model Studio using the latest configuration version.
- **CLI inputs:** positionals `model_studio_rid`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists, has a configuration version, and the caller can launch training.
- **Result:** Returns a `ModelStudioRun` for the new training run. Inspect run state later to determine whether training finished.
- **Failure:** A launch timeout does not establish whether a run started; list runs before retrying.
- **Example:** `pal-found-models model-studio launch <MODEL_STUDIO_RID>`
