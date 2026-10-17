# ModelVersion: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Model Version captures a versioned model artifact. Create on the intended Model and branch, then verify the returned version RID before deployment.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.Model.Version` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### create

Create a version on an existing Model and chosen branch. Verify returned version RID and metadata before promotion or deployment.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelVersion/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelVersion/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read one Model Version by RID and check its parent Model and artifact metadata.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelVersion/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelVersion/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### list

List versions for a Model with finite paging. Select an exact version RID for deployment.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelVersion/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelVersion/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
