# LiveDeployment: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A live deployment serves a model version with runtime configuration. Creation starts provisioning and is not evidence that inference is ready. Read deployment state before inference or replacement.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### create

Create a deployment for one model version and runtime configuration. Retain its RID and poll state with a finite budget before inference.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/LiveDeployment/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/LiveDeployment/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read a deployment RID, selected model version, state and runtime configuration before inference or replacement.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/LiveDeployment/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/LiveDeployment/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### list

List direct deployments of a Model, optionally by branch. Indirect deployments are outside this response.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/LiveDeployment/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/LiveDeployment/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### replace

Replace runtime configuration on the exact deployment. Read its state afterward because rollout to replicas is asynchronous.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/LiveDeployment/replace.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/LiveDeployment/replace.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### transform_json

Run JSON inference only against a ready deployment. Validate input schema and inspect the returned model result separately from transport success.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/LiveDeployment/transform_json.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/LiveDeployment/transform_json.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
