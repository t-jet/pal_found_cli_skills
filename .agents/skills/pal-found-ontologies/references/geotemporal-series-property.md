# Geotemporal series property operations

These records describe the `geotemporal_series_property` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### geotemporal_series_property.get_geotemporal_series_latest_value

- **Purpose and behavior:** Get the latest recorded location for a geotemporal series reference property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property_name`; optional `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property_name`: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has a geotemporal series property the caller may read.
- **Result:** Returns `Optional[GeotemporalSeriesEntry]` for the selected geotemporal series property.
- **Failure:** Missing series property or denied read access fails; a stream may stop after partial output on timeout.
- **Example:** `pal-found-ontologies geotemporal-series-property get-geotemporal-series-latest-value palantir airplane XYZ123 locationHistory`

### geotemporal_series_property.stream_geotemporal_series_historic_values

- **Purpose and behavior:** Stream historic points of a geotemporal series reference property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property_name`; optional `--output-filename`, `--range`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property_name`: The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint. `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--range` bounds the time-series or geotemporal values to retrieve; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the geotemporal series property and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies geotemporal-series-property stream-geotemporal-series-historic-values palantir airplane XYZ123 locationHistory --range '{"type":"relative","startTime":{"when":"BEFORE","value":5,"unit":"MONTHS"},"endTime":{"when":"BEFORE","value":1,"unit":"MONTHS"}}'`
