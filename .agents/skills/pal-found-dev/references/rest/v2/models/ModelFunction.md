# ModelFunction: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Model Function defines callable behavior for a Model. Check the function definition and compatible model version before replacing it.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### create

Create a function definition for a Model. Verify returned definition and parameter schema before callers use it.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelFunction/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelFunction/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read the function definition and verify its Model RID and input/output schema.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelFunction/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelFunction/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### replace

Replace a Model function definition. Compare the returned schema with clients that depend on it before deployment.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelFunction/replace.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelFunction/replace.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
