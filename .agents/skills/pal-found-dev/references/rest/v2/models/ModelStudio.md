# ModelStudio: models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Model Studio stores training configuration versions and launches runs. A launch uses the latest configuration, so resolve that version before starting a run.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.ModelStudio` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

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

## Configure and launch a training run

Choose an existing parent folder RID with write access. Check that the selected
trainer, worker configuration and resource configuration match the intended
run. Studio creation and training are distinct operations:

```python
studio = client.models.ModelStudio.create(
    name=studio_name, parent_folder_rid=parent_folder_rid,
    preview=True, request_timeout=30
)
assert studio.rid
loaded = client.models.ModelStudio.get(
    studio.rid, preview=True, request_timeout=30
)
assert loaded.rid == studio.rid
latest = client.models.ModelStudio.ConfigVersion.latest(
    studio.rid, preview=True, request_timeout=30
)
if latest is None:
    raise ValueError("Create a validated configuration version before launch")
run = client.models.ModelStudio.launch(
    studio.rid, preview=True, request_timeout=30
)
assert run.config_version == latest.version
run_id, build_rid = run.run_id, run.build_rid
```

`ConfigVersion.create` requires `name`, `resources`, `trainer_id` and
`worker_config`; prepare these from the [local models](../../models/v2/models/models/ModelStudioConfigVersion.md)
and the [trainer operations](ModelStudioTrainer.md). `launch` uses the latest
configuration at request time. Another writer can publish a newer version
between `latest` and `launch`; compare `run.config_version` and investigate a
mismatch before treating the run as intended. A returned run is a submitted
training run, so inspect its build status with the [run contract](ModelStudioRun.md)
under a finite polling budget. On an uncertain launch response, list runs for
this Studio and reconcile identities before starting another run.
