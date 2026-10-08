# ModelStudioTrainer: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Trainer IDs and versions select supported Model Studio training behavior. Choose from the visible trainer list before saving a configuration.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### get

Read a specific trainer ID and optional version, then validate its settings before creating a Studio configuration.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioTrainer/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioTrainer/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### list

List visible trainers; pick a returned ID/version rather than assuming a global trainer name.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioTrainer/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioTrainer/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
