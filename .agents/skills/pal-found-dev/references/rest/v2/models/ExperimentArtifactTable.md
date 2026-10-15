# ExperimentArtifactTable: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Experiment artifact tables can be read as JSON rows or Parquet bytes. The caller must bound output and close streams for large artifacts.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.Model.Experiment.ArtifactTable` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### json

Read table rows as a bounded JSON response. Keep the artifact identity and detect truncation before treating rows as complete.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ExperimentArtifactTable/json.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ExperimentArtifactTable/invoke_json.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### parquet

Read the artifact as Parquet bytes through a bounded stream and close the response after consumption.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ExperimentArtifactTable/parquet.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ExperimentArtifactTable/parquet.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
