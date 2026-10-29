# Experiment series operations

These records describe the `experiment_series` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

## Reading series data

SDK 1.101.0 `Series` is `DoubleSeriesV1`: `type` is `doubleV1` and
`series` is a list of entries containing numeric `value`, integer `timestamp`
(milliseconds since Unix epoch), and integer `step`. For example,
`{"type":"doubleV1","series":[{"value":0.25,"timestamp":1000,"step":0}]}`
records value 0.25 at one second after the epoch with step 0. `step` is a
recorded sequence coordinate; the SDK does not define its unit or establish that
it counts epochs or seconds. Use the producer's meaning. Discover names in
`experiment get`'s `series[].name`. An empty series slice contains no entries;
it does not establish that the whole experiment has no series data. Increase
`--offset` by the number of entries consumed to read subsequent slices; stop
when an empty slice is returned or your chosen entry/request budget is reached.

### experiment_series.json

- **Purpose and behavior:** Retrieve raw time-series data for a single series in JSON format. Results are paginated with a default page size of 200 and a maximum of 1000.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`, `experiment_series_name`; optional `--offset`, `--page-size`.
- **Input meaning:** `model_rid`: RID of the model that owns the experiment. `experiment_rid`: RID of that experiment. `experiment_series_name`: Name of the metric or time series recorded for the experiment; use the name returned when it was created. `--offset` skips this many experiment table rows or series entries before returning results; `--page-size` sets the requested maximum entries in one result page.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model, experiment, and series name identify a readable metric series.
- **Result:** Returns `Series` for this experiment series request.
- **Failure:** Unknown series name or denied experiment access returns a structured error.
- **Example:** `pal-found-models experiment-series json <MODEL_RID> <EXPERIMENT_RID> <EXPERIMENT_SERIES_NAME>`

### experiment_series.parquet

- **Purpose and behavior:** Retrieve raw time-series data for a single series as a streamed binary response in Apache Parquet format.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`, `experiment_series_name`; required `--output`.
- **Input meaning:** `model_rid`: RID of the model that owns the experiment. `experiment_rid`: RID of that experiment. `experiment_series_name`: Name of the metric or time series recorded for the experiment; use the name returned when it was created. `--output` sets a filename, without directory separators, under the configured download root. The CLI creates a separate subdirectory and prints the saved path.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the experiment series and has room to save its file locally.
- **Result:** Saves the Parquet stream under the configured download root and prints a download metadata envelope with the saved path and checksums.
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-models experiment-series parquet <MODEL_RID> <EXPERIMENT_RID> <EXPERIMENT_SERIES_NAME> --output result.parquet`
