# Model studio run operations

These records describe the `model_studio_run` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model_studio_run.list

- **Purpose and behavior:** Lists all runs for a Model Studio.
- **CLI inputs:** positionals `model_studio_rid`; optional `--page-size`, `--page-token`, `--all`, `--max-pages`, `--config-version`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource. `--config-version` filters runs to a Model Studio configuration version; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from `next_page_token` in the previous call's stderr metadata; omit on the first page. By default, the CLI fetches one page. `--max-pages` fetches up to the given number of pages; `--all` fetches until no cursor remains or the configured limit of at most 40 pages is reached. If both are set, `--all` takes precedence.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists and the caller may inspect its runs.
- **Result:** Prints Model Studio run entries as a list on stdout. Pagination metadata, including `next_page_token` when another page exists, follows a separator on stderr. An empty list means this page contains no entries; follow a returned token to check the next page.
- **Failure:** Unknown studio or denied run access returns a structured error; an empty list means no visible runs.
- **Example:** `pal-found-models model-studio-run list <MODEL_STUDIO_RID>`
