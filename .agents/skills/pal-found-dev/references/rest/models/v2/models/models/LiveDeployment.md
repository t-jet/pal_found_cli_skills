# foundry_sdk.v2.models.models.LiveDeployment


LiveDeployment

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | LiveDeploymentRid | required; no default | No additional field description in SDK source. |
| model_version | modelVersion | LiveDeploymentModelVersion | required; no default | The currently deployed model version. |
| branch | branch | typing.Optional[core_models.BranchName] | None | The model branch this deployment tracks. Present for direct deployments that follow the latest model version on a branch; absent for deployment types that are not branch-scoped. |
| runtime_configuration | runtimeConfiguration | LiveDeploymentRuntimeConfiguration | required; no default | The compute resource configuration for the deployment. |
| status | status | LiveDeploymentStatus | required; no default | The current operational status of the deployment. |

```python
class LiveDeployment(core.ModelBase):
    """LiveDeployment"""

    rid: LiveDeploymentRid
    model_version: LiveDeploymentModelVersion = pydantic.Field(alias=str("modelVersion"))  # type: ignore[literal-required]
    """The currently deployed model version."""

    branch: typing.Optional[core_models.BranchName] = None
    """The model branch this deployment tracks. Present for direct deployments that follow the latest model version on a branch; absent for deployment types that are not branch-scoped."""

    runtime_configuration: LiveDeploymentRuntimeConfiguration = pydantic.Field(alias=str("runtimeConfiguration"))  # type: ignore[literal-required]
    """The compute resource configuration for the deployment."""

    status: LiveDeploymentStatus
    """The current operational status of the deployment."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.models.models.LiveDeploymentModelVersion](LiveDeploymentModelVersion.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRid](LiveDeploymentRid.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRuntimeConfiguration](LiveDeploymentRuntimeConfiguration.md)
- [foundry_sdk.v2.models.models.LiveDeploymentStatus](LiveDeploymentStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LiveDeployment.md)
