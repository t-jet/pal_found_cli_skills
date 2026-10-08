# foundry_sdk.v2.models.models.LiveDeploymentScalingConfiguration


Autoscaling configuration that controls how the deployment scales replicas based on load thresholds and cooldown delays.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| scale_up_load_threshold | scaleUpLoadThreshold | float | required; no default | A threshold between 0.0 and 1.0. If the ratio of running jobs to job capacity exceeds this threshold for the duration of the scale-up delay, the deployment will scale up. Job capacity is the number of running replicas multiplied by the thread count (concurrency limit). |
| scale_up_delay | scaleUpDelay | core_models.Duration | required; no default | The duration that load must exceed the scale-up threshold before scaling up. |
| scale_down_delay | scaleDownDelay | core_models.Duration | required; no default | The duration that load must be below the scale-down threshold before scaling down. |

```python
class LiveDeploymentScalingConfiguration(core.ModelBase):
    """Autoscaling configuration that controls how the deployment scales replicas based on load thresholds and cooldown delays."""

    scale_up_load_threshold: float = pydantic.Field(alias=str("scaleUpLoadThreshold"))  # type: ignore[literal-required]
    """A threshold between 0.0 and 1.0. If the ratio of running jobs to job capacity exceeds this threshold for the duration of the scale-up delay, the deployment will scale up. Job capacity is the number of running replicas multiplied by the thread count (concurrency limit)."""

    scale_up_delay: core_models.Duration = pydantic.Field(alias=str("scaleUpDelay"))  # type: ignore[literal-required]
    """The duration that load must exceed the scale-up threshold before scaling up."""

    scale_down_delay: core_models.Duration = pydantic.Field(alias=str("scaleDownDelay"))  # type: ignore[literal-required]
    """The duration that load must be below the scale-down threshold before scaling down."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.Duration](../../core/models/Duration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LiveDeploymentScalingConfiguration.md)
