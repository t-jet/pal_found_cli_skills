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
- **CLI inputs:** positionals `model_rid`; optional `--page-size`, `--page-token`, `--all`, `--max-pages`, `--order-by-json`, `--where-json`.
- **Input meaning:** `model_rid`: Resource identifier (RID) of the named Foundry resource. `--where-json`: Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. `--order-by-json` sorts experiments using the SDK order-by JSON schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from `next_page_token` in the previous call's stderr metadata; omit on the first page. By default, the CLI fetches one page. `--max-pages` fetches up to the given number of pages; `--all` fetches until no cursor remains or the configured limit of at most 40 pages is reached. If both are set, `--all` takes precedence.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can inspect its experiments.
- **Result:** Prints matching experiment entries as a list on stdout. Pagination metadata, including `next_page_token` when another page exists, follows a separator on stderr. An empty list means this page contains no entries; follow a returned token to check the next page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-models experiment search <MODEL_RID>`
