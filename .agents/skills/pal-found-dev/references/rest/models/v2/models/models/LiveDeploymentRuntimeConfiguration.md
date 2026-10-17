# foundry_sdk.v2.models.models.LiveDeploymentRuntimeConfiguration


The compute resource configuration for a live deployment, controlling replica scaling, CPU, memory, and GPU resources.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| min_replicas | minReplicas | int | required; no default | The minimum number of replicas to keep running. |
| max_replicas | maxReplicas | int | required; no default | The maximum number of replicas to scale to under load. |
| cpu | cpu | typing.Optional[float] | None | The number of CPU units requested. This is also set as the limit. |
| memory | memory | typing.Optional[str] | None | The amount of memory requested in human-readable format (e.g. "256MiB", "1GiB"). This is also set as the limit. |
| gpu | gpu | typing.Optional[LiveDeploymentGpu] | None | Optional GPU resources for the deployment. |
| thread_count | threadCount | typing.Optional[int] | default None | The number of threads used for query handling. Defaults to 32 if not specified. Also affects how many concurrent requests will be sent to a single replica. |
| scaling_configuration | scalingConfiguration | typing.Optional[LiveDeploymentScalingConfiguration] | default None | Autoscaling configuration for the deployment. Controls how the deployment scales replicas up and down based on load. |

```python
class LiveDeploymentRuntimeConfiguration(core.ModelBase):
    """The compute resource configuration for a live deployment, controlling replica scaling, CPU, memory, and GPU resources."""

    min_replicas: int = pydantic.Field(alias=str("minReplicas"))  # type: ignore[literal-required]
    """The minimum number of replicas to keep running."""

    max_replicas: int = pydantic.Field(alias=str("maxReplicas"))  # type: ignore[literal-required]
    """The maximum number of replicas to scale to under load."""

    cpu: typing.Optional[float] = None
    """The number of CPU units requested. This is also set as the limit."""

    memory: typing.Optional[str] = None
    """The amount of memory requested in human-readable format (e.g. "256MiB", "1GiB"). This is also set as the limit."""

    gpu: typing.Optional[LiveDeploymentGpu] = None
    """Optional GPU resources for the deployment."""

    thread_count: typing.Optional[int] = pydantic.Field(alias=str("threadCount"), default=None)  # type: ignore[literal-required]
    """The number of threads used for query handling. Defaults to 32 if not specified. Also affects how many concurrent requests will be sent to a single replica."""

    scaling_configuration: typing.Optional[LiveDeploymentScalingConfiguration] = pydantic.Field(alias=str("scalingConfiguration"), default=None)  # type: ignore[literal-required]
    """Autoscaling configuration for the deployment. Controls how the deployment scales replicas up and down based on load."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.LiveDeploymentGpu](LiveDeploymentGpu.md)
- [foundry_sdk.v2.models.models.LiveDeploymentScalingConfiguration](LiveDeploymentScalingConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LiveDeploymentRuntimeConfiguration.md)
