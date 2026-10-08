# ModelStudioRun: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Runs record training execution for a Model Studio. List them with finite paging and inspect the intended run identity/status.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### list

List Studio runs using a bounded page budget. Keep run IDs and status to distinguish active training from completed output.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioRun/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioRun/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
