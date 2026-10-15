# ModelStudioRun: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Runs record training execution for a Model Studio. List them with finite paging and inspect the intended run identity/status.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.ModelStudio.Run` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### list

List Studio runs using a bounded page budget. Keep run IDs and status to distinguish active training from completed output.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioRun/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioRun/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
