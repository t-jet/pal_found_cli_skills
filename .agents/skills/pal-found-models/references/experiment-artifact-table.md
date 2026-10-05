# Experiment artifact table operations

These records describe the `experiment_artifact_table` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### experiment_artifact_table.json

- **Purpose and behavior:** Read table data from an experiment artifact as a streamed binary response containing JSON. The response body is a JSON array of row objects, where each object maps column names to values. Results are paginated by row count with a default page size of 10 and a maximum of 100.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`, `experiment_artifact_table_name`; required `--output`; optional `--offset`, `--page-size`.
- **Input meaning:** `model_rid`: RID of the model that owns the experiment. `experiment_rid`: RID of that experiment. `experiment_artifact_table_name`: Name of the table artifact saved for the experiment; use the name returned when it was created. `--offset` skips this many experiment table rows or series entries before returning results; `--output` saves the downloaded artifact to this local path; `--page-size` sets the requested maximum entries in one result page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model, experiment, and artifact table name identify a readable table.
- **Result:** Saves the JSON rows to `--output` and prints a download metadata envelope; `--offset` and `--page-size` select one page.
- **Failure:** Unknown table name, denied experiment access, or a failed transfer prevents a usable saved file.
- **Example:** `pal-found-models experiment-artifact-table json <MODEL_RID> <EXPERIMENT_RID> <EXPERIMENT_ARTIFACT_TABLE_NAME> --output result.json`

### experiment_artifact_table.parquet

- **Purpose and behavior:** Read raw table data from experiment artifacts in Parquet format.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`, `experiment_artifact_table_name`; required `--output`.
- **Input meaning:** `model_rid`: RID of the model that owns the experiment. `experiment_rid`: RID of that experiment. `experiment_artifact_table_name`: Name of the table artifact saved for the experiment; use the name returned when it was created. `--output` saves the downloaded artifact to this local path.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the experiment artifact table and has room to save its file locally.
- **Result:** Saves the Parquet stream to `--output` and prints a download metadata envelope with the saved path and checksums.
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-models experiment-artifact-table parquet <MODEL_RID> <EXPERIMENT_RID> <EXPERIMENT_ARTIFACT_TABLE_NAME> --output result.parquet`
