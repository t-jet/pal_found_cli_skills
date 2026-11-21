# ModelFunction: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Model Function defines callable behavior for a Model. Check the function definition and compatible model version before replacing it.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.Model.Function` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### create

Create a function definition for a Model. Verify the returned function RID, function version, names and row-wise flag before callers use it. Read the compatible [Model Version](ModelVersion.md#get) to inspect its `model_api` input/output definitions; the function response does not include those schemas.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelFunction/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelFunction/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read function metadata for the requested Model RID. Verify its function RID, function version, display/API names, row-wise flag and optional Ontology binding. The Model RID is request context; input/output definitions come from the compatible [Model Version](ModelVersion.md#get), not this response.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelFunction/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelFunction/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### replace

Replace a Model function definition and verify the returned function metadata. Before deployment, compare the compatible Model Version's `model_api` input/output definitions with the needs of dependent clients.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelFunction/replace.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelFunction/replace.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
