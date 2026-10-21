# Experiment: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An experiment stores run metadata, parameters, series metadata and metrics. Search returns matches; get retrieves the selected experiment for inspection.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.Model.Experiment` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### get

Read one experiment including metadata, parameters and metric summaries. Check the experiment RID before loading its artifacts or series.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/Experiment/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/Experiment/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### search

Search experiments using explicit nested predicates and inspect returned hits. Maximum response size is 100, so refine or page according to the contract.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/Experiment/search.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/Experiment/search.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
