# foundry_sdk.v2.models.models.LiveDeploymentStatus


The current operational status of a live deployment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| state | state | LiveDeploymentState | required; no default | The current operational state of the deployment. |
| is_ready | isReady | bool | required; no default | Whether the deployment is ready to serve inference requests. A deployment may be active but not ready if it has been autoscaled to zero replicas. |

```python
class LiveDeploymentStatus(core.ModelBase):
    """The current operational status of a live deployment."""

    state: LiveDeploymentState
    """The current operational state of the deployment."""

    is_ready: bool = pydantic.Field(alias=str("isReady"))  # type: ignore[literal-required]
    """Whether the deployment is ready to serve inference requests. A deployment may be active but not ready if it has been autoscaled to zero replicas."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.LiveDeploymentState](LiveDeploymentState.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LiveDeploymentStatus.md)
