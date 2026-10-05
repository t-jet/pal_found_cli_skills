# Model studio run operations

These records describe the `model_studio_run` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model_studio_run.list

- **Purpose and behavior:** Lists all runs for a Model Studio.
- **CLI inputs:** positionals `model_studio_rid`; optional `--page-size`, `--page-token`, `--config-version`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource. `--config-version` filters runs to a Model Studio configuration version; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists and the caller may inspect its runs.
- **Result:** Returns `ListModelStudioRunsResponse` containing the visible matching model studio run entries; an empty page means none matched that page.
- **Failure:** Unknown studio or denied run access returns a structured error; an empty list means no visible runs.
- **Example:** `pal-found-models model-studio-run list <MODEL_STUDIO_RID>`
