# Experiment operations

These records describe the `experiment` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### experiment.get

- **Purpose and behavior:** Retrieve a single experiment with all metadata, parameters, series metadata, and summary metrics.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`.
- **Input meaning:** `model_rid`: Resource identifier (RID) of the named Foundry resource. `experiment_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can inspect its experiments.
- **Result:** Returns `Experiment` for the selected experiment.
- **Failure:** An unknown experiment identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-models experiment get <MODEL_RID> <EXPERIMENT_RID>`

### experiment.search

- **Purpose and behavior:** Search experiments using complex nested queries on experiment metadata, parameters, series, and summary metrics. Supports AND/OR/NOT combinations and various predicates. Returns a maximum of 100 results per page.
- **CLI inputs:** positionals `model_rid`; optional `--page-size`, `--page-token`, `--order-by-json`, `--where-json`.
- **Input meaning:** `model_rid`: Resource identifier (RID) of the named Foundry resource. `--where-json`: Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. `--order-by-json` sorts experiments using the SDK order-by JSON schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can inspect its experiments.
- **Result:** Returns `SearchExperimentsResponse` containing the visible matching experiment entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-models experiment search <MODEL_RID>`
