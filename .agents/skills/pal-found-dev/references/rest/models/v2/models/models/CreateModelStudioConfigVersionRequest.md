# foundry_sdk.v2.models.models.CreateModelStudioConfigVersionRequest


CreateModelStudioConfigVersionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | ModelStudioConfigVersionName | required; no default | Human readable name of the configuration version and experiment. |
| resources | resources | ResourceConfiguration | required; no default | The compute resources allocated for training runs. |
| changelog | changelog | typing.Optional[str] | None | Changelog describing changes in this version. |
| worker_config | workerConfig | ModelStudioWorkerConfig | required; no default | The worker configuration including inputs, outputs, and custom settings. |
| trainer_id | trainerId | TrainerId | required; no default | The identifier of the trainer to use for this configuration. |

```python
class CreateModelStudioConfigVersionRequest(core.ModelBase):
    """CreateModelStudioConfigVersionRequest"""

    name: ModelStudioConfigVersionName
    """Human readable name of the configuration version and experiment."""

    resources: ResourceConfiguration
    """The compute resources allocated for training runs."""

    changelog: typing.Optional[str] = None
    """Changelog describing changes in this version."""

    worker_config: ModelStudioWorkerConfig = pydantic.Field(alias=str("workerConfig"))  # type: ignore[literal-required]
    """The worker configuration including inputs, outputs, and custom settings."""

    trainer_id: TrainerId = pydantic.Field(alias=str("trainerId"))  # type: ignore[literal-required]
    """The identifier of the trainer to use for this configuration."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionName](ModelStudioConfigVersionName.md)
- [foundry_sdk.v2.models.models.ModelStudioWorkerConfig](ModelStudioWorkerConfig.md)
- [foundry_sdk.v2.models.models.ResourceConfiguration](ResourceConfiguration.md)
- [foundry_sdk.v2.models.models.TrainerId](TrainerId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateModelStudioConfigVersionRequest.md)
