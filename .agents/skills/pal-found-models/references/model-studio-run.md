# Model studio run operations

These records describe the `model_studio_run` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

## Completion and recovery

A run contains `runId`, `buildRid`, `jobRid`, integer `configVersion`,
`startedBy`, `startedTime`, optional `buildStatus`, and `resolvedOutputs`.
Correlate `runId` with the launch result and `configVersion` with the intended
configuration. Listing by configuration can return several runs; do not assume
the first is the run you launched.

`buildStatus` is `RUNNING`, `SUCCEEDED`, `FAILED`, or `CANCELED` in SDK 1.101.0.
Absent or null status leaves completion unknown. A returned run or empty output
map does not establish success. After launch, list runs using `--config-version`
and enough pages to find the returned `runId`. Choose a finite deadline and
maximum number of checks before polling, space checks to avoid request bursts,
and stop at the deadline or terminal status. If the run is missing, follow
returned page tokens within that budget; check studio/config identity and access.
If still running or status remains absent at the deadline, retain the run/build/
job IDs and inspect progress with an authorized operator. This namespace has no
run get, wait, cancel, or job-log command.

`resolvedOutputs` maps trainer output aliases to objects. SDK 1.101.0 supports
`type=model`, with `modelRid`, `modelVersionRid`, and optional
`experimentRid`. On `SUCCEEDED`, use those RIDs with `model-version get` and,
when present, `experiment get`; compare the model API to your intended use.
Missing expected aliases or a missing optional experiment require checking the
trainer/configuration contract; do not fabricate resource IDs. A successful
build does not prove deployment readiness or artifact compatibility.

On `FAILED` or `CANCELED`, inspect the identified build/job and any returned
experiment status message through authorized enrollment tooling. Correct the
configuration or capacity/access problem before launching again. A launch timeout
leaves whether a run started unknown: list and correlate existing runs before
retrying, since another launch can duplicate work and cost.

### model_studio_run.list

- **Purpose and behavior:** Lists all runs for a Model Studio.
- **CLI inputs:** positionals `model_studio_rid`; optional `--page-size`, `--page-token`, `--all`, `--max-pages`, `--config-version`.
- **Input meaning:** `model_studio_rid`: Resource identifier (RID) of the named Foundry resource. `--config-version` filters runs to a Model Studio configuration version; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from `next_page_token` in the previous call's stderr metadata; omit on the first page. By default, the CLI fetches one page. `--max-pages` fetches up to the given number of pages; `--all` fetches until no cursor remains or the configured limit of at most 40 pages is reached. If both are set, `--all` takes precedence.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The Model Studio exists and the caller may inspect its runs.
- **Result:** Prints Model Studio run entries as a list on stdout. Pagination metadata, including `next_page_token` when another page exists, follows a separator on stderr. An empty list means this page contains no entries; follow a returned token to check the next page.
- **Failure:** Unknown studio or denied run access returns a structured error; an empty list means no visible runs.
- **Example:** `pal-found-models model-studio-run list <MODEL_STUDIO_RID>`
