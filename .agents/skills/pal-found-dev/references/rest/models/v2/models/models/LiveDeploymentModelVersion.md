# foundry_sdk.v2.models.models.LiveDeploymentModelVersion


Identifies the model and model version associated with a live deployment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| model_rid | modelRid | ModelRid | required; no default | No additional field description in SDK source. |
| model_version_rid | modelVersionRid | ModelVersionRid | required; no default | No additional field description in SDK source. |

```python
class LiveDeploymentModelVersion(core.ModelBase):
    """Identifies the model and model version associated with a live deployment."""

    model_rid: ModelRid = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    model_version_rid: ModelVersionRid = pydantic.Field(alias=str("modelVersionRid"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelRid](ModelRid.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](ModelVersionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LiveDeploymentModelVersion.md)
