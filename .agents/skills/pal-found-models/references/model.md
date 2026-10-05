# Model operations

These records describe the `model` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model.create

- **Purpose and behavior:** Creates a new Model with no versions.
- **CLI inputs:** required `--name`, `--parent-folder-rid`.
- **Input meaning:** `--name`: Human readable name for the new model. `--parent-folder-rid`: RID of the folder where Foundry will create the model.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The parent folder exists and the caller can create resources there. No model RID exists before this call.
- **Result:** Returns the created `Model` with its server-assigned identifier.
- **Failure:** Invalid model inputs or insufficient permission produce a structured error. After a timeout, read current state before retrying.
- **Example:** `pal-found-models model create --name 'House Pricing Model' --parent-folder-rid ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791`

### model.get

- **Purpose and behavior:** Retrieves a Model by its Resource Identifier (RID).
- **CLI inputs:** positionals `model_rid`.
- **Input meaning:** `model_rid` identifies the model to retrieve; obtain it from `model create` or the model resource in Foundry.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can read it.
- **Result:** Returns `Model` for the selected model.
- **Failure:** An unknown model identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-models model get <MODEL_RID>`

### model.promote_version

- **Purpose and behavior:** Promotes an existing Model Version to the target Model. The promoted Model Version will be copied to the target Model as the latest version on the master branch, but will have a new Model Version RID.
- **CLI inputs:** positionals `model_rid`; required `--source-model-version-rid`.
- **Input meaning:** `model_rid` identifies the destination model. `--source-model-version-rid` identifies the version to copy, which can belong to another model. The destination receives a new version RID.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The source model version exists and the caller may update the target model.
- **Result:** Returns the promoted `ModelVersion`. The target model receives a copy on its master branch with a new version RID.
- **Failure:** Invalid model inputs or insufficient permission produce a structured error. After a timeout, read current state before retrying.
- **Example:** `pal-found-models model promote-version <MODEL_RID> --source-model-version-rid ri.models.main.model-version.adf94926-c3ac-41ea-beb2-4946699d08ee`
