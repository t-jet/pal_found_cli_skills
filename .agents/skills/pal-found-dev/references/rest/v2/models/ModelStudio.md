# ModelStudio: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Model Studio stores training configuration versions and launches runs. A launch uses the latest configuration, so resolve that version before starting a run.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### create

Create a Model Studio and retain its RID for configuration and training runs.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudio/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudio/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read a Studio by RID, including the information needed to select a configuration and trainer.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudio/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudio/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### launch

Launch one training run using the latest configuration version. Check latest configuration first and record returned run identity.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudio/launch.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudio/launch.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
