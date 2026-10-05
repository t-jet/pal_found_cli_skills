# Time series property v2 operations

These records describe the `time_series_property_v2` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### time_series_property_v2.get_first_point

- **Purpose and behavior:** Get the first point of a time series property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has a time-series property backed by the v2 service and the caller can read its points.
- **Result:** Returns `Optional[TimeSeriesPoint]` for the selected time series property v2.
- **Failure:** Unknown point series or denied object access fails; a stream may stop after partial output on timeout.
- **Example:** `pal-found-ontologies time-series-property-v2 get-first-point palantir employee 50030 performance`

### time_series_property_v2.get_last_point

- **Purpose and behavior:** Get the last point of a time series property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has a time-series property backed by the v2 service and the caller can read its points.
- **Result:** Returns `Optional[TimeSeriesPoint]` for the selected time series property v2.
- **Failure:** Unknown point series or denied object access fails; a stream may stop after partial output on timeout.
- **Example:** `pal-found-ontologies time-series-property-v2 get-last-point palantir employee 50030 performance`

### time_series_property_v2.stream_points

- **Purpose and behavior:** Stream all of the points of a time series property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--format`, `--output-filename`, `--aggregate`, `--range`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--aggregate` supplies an aggregate time-series request instead of raw points; `--format` sets the time-series stream encoding (JSON or ARROW); this differs from the global CLI output format; `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--range` bounds the time-series or geotemporal values to retrieve; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the time series property v2 and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies time-series-property-v2 stream-points palantir employee 50030 <PROPERTY> --range '{"type":"relative","startTime":{"when":"BEFORE","value":5,"unit":"MONTHS"},"endTime":{"when":"BEFORE","value":1,"unit":"MONTHS"}}'`
