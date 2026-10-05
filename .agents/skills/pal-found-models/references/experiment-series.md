# Experiment series operations

These records describe the `experiment_series` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### experiment_series.json

- **Purpose and behavior:** Retrieve raw time-series data for a single series in JSON format. Results are paginated with a default page size of 200 and a maximum of 1000.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`, `experiment_series_name`; optional `--offset`, `--page-size`.
- **Input meaning:** `model_rid`: RID of the model that owns the experiment. `experiment_rid`: RID of that experiment. `experiment_series_name`: Name of the metric or time series recorded for the experiment; use the name returned when it was created. `--offset` skips this many experiment table rows or series entries before returning results; `--page-size` sets the requested maximum entries in one result page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model, experiment, and series name identify a readable metric series.
- **Result:** Returns `Series` for this experiment series request.
- **Failure:** Unknown series name or denied experiment access returns a structured error; Parquet transfer can fail after partial output.
- **Example:** `pal-found-models experiment-series json <MODEL_RID> <EXPERIMENT_RID> <EXPERIMENT_SERIES_NAME>`

### experiment_series.parquet

- **Purpose and behavior:** Retrieve raw time-series data for a single series as a streamed binary response in Apache Parquet format.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`, `experiment_series_name`; required `--output`.
- **Input meaning:** `model_rid`: RID of the model that owns the experiment. `experiment_rid`: RID of that experiment. `experiment_series_name`: Name of the metric or time series recorded for the experiment; use the name returned when it was created. `--output` saves the downloaded artifact to this local path.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the experiment series and has room to save its file locally.
- **Result:** Saves the Parquet stream to `--output` and prints a download metadata envelope with the saved path and checksums.
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-models experiment-series parquet <MODEL_RID> <EXPERIMENT_RID> <EXPERIMENT_SERIES_NAME> --output result.parquet`
