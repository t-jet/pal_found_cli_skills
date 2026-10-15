# Model: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Model groups versions and branches. Creation yields an empty Model; a usable version must be created or promoted separately.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.Model` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### create

Create an empty Model in the chosen location. Retain its RID and create or promote a version before deployment.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/Model/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/Model/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read Model metadata by RID and verify branch/version state before selecting a version.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/Model/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/Model/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### promote_version

Copy an existing version into the target Model branch. The copy receives a new version RID; use that returned RID for later deployment.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/Model/promote_version.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/Model/promote_version.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
