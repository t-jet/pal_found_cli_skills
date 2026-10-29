# ExperimentSeries: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An experiment series contains values over time or training steps. JSON access is paged; Parquet access returns a binary artifact.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.Model.Experiment.Series` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### json

Read one series as paged JSON. Default page size is 200 and maximum is 1,000; carry continuation state.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ExperimentSeries/json.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ExperimentSeries/invoke_json.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### parquet

Read a series as Parquet bytes under a size budget, then close the stream.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ExperimentSeries/parquet.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ExperimentSeries/parquet.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
