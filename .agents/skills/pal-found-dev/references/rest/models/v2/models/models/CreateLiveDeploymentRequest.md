# foundry_sdk.v2.models.models.CreateLiveDeploymentRequest


CreateLiveDeploymentRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| deployment_type | deploymentType | CreateLiveDeploymentTarget | required; no default | The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment. |
| runtime_configuration | runtimeConfiguration | LiveDeploymentRuntimeConfiguration | required; no default | The compute resource configuration for the deployment. |

```python
class CreateLiveDeploymentRequest(core.ModelBase):
    """CreateLiveDeploymentRequest"""

    deployment_type: CreateLiveDeploymentTarget = pydantic.Field(alias=str("deploymentType"))  # type: ignore[literal-required]
    """The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment."""

    runtime_configuration: LiveDeploymentRuntimeConfiguration = pydantic.Field(alias=str("runtimeConfiguration"))  # type: ignore[literal-required]
    """The compute resource configuration for the deployment."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.CreateLiveDeploymentTarget](CreateLiveDeploymentTarget.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRuntimeConfiguration](LiveDeploymentRuntimeConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateLiveDeploymentRequest.md)
