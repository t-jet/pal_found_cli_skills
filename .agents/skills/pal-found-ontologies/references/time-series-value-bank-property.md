# Time series value bank property operations

These records describe the `time_series_value_bank_property` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### time_series_value_bank_property.get_latest_value

- **Purpose and behavior:** Get the latest value of a property backed by a timeseries. If a specific geotime series integration has both a history and a live integration, we will give precedence to the live integration.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property_name`; optional `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property_name`: The API name of the timeseries property. To find the API name for your property value bank property, check the **Ontology Manager** or use the **Get object type** endpoint. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has a value-bank time-series property and the caller may read its values.
- **Result:** Returns `Optional[TimeseriesEntry]` for the selected time series value bank property.
- **Failure:** Unknown series or denied object access fails; a stream may stop after partial output on timeout.
- **Example:** `pal-found-ontologies time-series-value-bank-property get-latest-value palantir employee 50030 performance`

### time_series_value_bank_property.stream_values

- **Purpose and behavior:** Stream all of the points of a time series property (this includes geotime series references).
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--output-filename`, `--range`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--range` bounds the time-series or geotemporal values to retrieve; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the time series value bank property and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies time-series-value-bank-property stream-values palantir employee 50030 <PROPERTY> --range '{"type":"relative","startTime":{"when":"BEFORE","value":5,"unit":"MONTHS"},"endTime":{"when":"BEFORE","value":1,"unit":"MONTHS"}}'`
