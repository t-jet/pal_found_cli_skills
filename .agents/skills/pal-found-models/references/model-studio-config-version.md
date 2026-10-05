# Model studio config version operations

These records describe the `model_studio_config_version` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model_studio_config_version.create

- **Purpose and behavior:** Creates a new Model Studio configuration version.
- **CLI inputs:** positionals `model_studio_rid`; required `--name`, `--resources-json`, `--trainer-id`, `--worker-config-json`; optional `--changelog`.
- **Input meaning:** `--name`: Human readable name of the configuration version and experiment. `--resources-json`: The compute resources allocated for training runs. `--trainer-id`: The identifier of the trainer to use for this configuration. `--worker-config-json`: JSON trainer configuration with `inputs` and `outputs` alias maps. `--changelog` describes changes in this configuration version; `model_studio_rid` is the RID of the owning Model Studio.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists; creation needs a valid trainer, compute resources, and worker configuration.
- **Result:** Returns the created `ModelStudioConfigVersion` with its server-assigned identifier.
- **Failure:** Unknown trainer or invalid resources/worker config prevents version creation; check existing versions after a timeout.
- **Example:** `pal-found-models model-studio-config-version create <MODEL_STUDIO_RID> --name 'Order forecast' --resources-json '{"gpu":"V100"}' --trainer-id autogluon --worker-config-json '{"inputs":{},"outputs":{}}'`

The trainer determines which input and output aliases are required. Replace the empty maps with those aliases and their configurations before creating a version.

### model_studio_config_version.get

- **Purpose and behavior:** Gets a specific Model Studio configuration version.
- **CLI inputs:** positionals `model_studio_rid`, `model_studio_config_version_version`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource. `model_studio_config_version_version`: The version number of this configuration.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio and requested configuration version exist, and the caller can read them.
- **Result:** Returns `ModelStudioConfigVersion` for the selected model studio config version.
- **Failure:** An unknown Model Studio or version, or missing read permission, returns a structured error.
- **Example:** `pal-found-models model-studio-config-version get <MODEL_STUDIO_RID> <MODEL_STUDIO_CONFIG_VERSION_VERSION>`

### model_studio_config_version.latest

- **Purpose and behavior:** Gets the latest configuration version for a Model Studio.
- **CLI inputs:** positionals `model_studio_rid`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists and the caller can read its configuration versions.
- **Result:** Returns `Optional[ModelStudioConfigVersion]` for the selected model studio config version.
- **Failure:** An unknown Model Studio or missing read permission returns a structured error.
- **Example:** `pal-found-models model-studio-config-version latest <MODEL_STUDIO_RID>`

### model_studio_config_version.list

- **Purpose and behavior:** Lists all configuration versions for a Model Studio.
- **CLI inputs:** positionals `model_studio_rid`; optional `--page-size`, `--page-token`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource. `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists and the caller can read its configuration versions.
- **Result:** Returns `ListModelStudioConfigVersionsResponse` containing the visible matching model studio config version entries; an empty page means none matched that page.
- **Failure:** An unknown Model Studio or missing read permission returns a structured error.
- **Example:** `pal-found-models model-studio-config-version list <MODEL_STUDIO_RID>`
