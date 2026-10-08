# foundry_sdk.v2.models.models.DirectCreateLiveDeploymentTarget


Creates a live deployment that tracks the latest model version on a branch.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| model_rid | modelRid | ModelRid | required; no default | No additional field description in SDK source. |
| branch | branch | str | required; no default | The model branch for the deployment. |
| type | type | typing.Literal['direct'] | 'direct' | No additional field description in SDK source. |

```python
class DirectCreateLiveDeploymentTarget(core.ModelBase):
    """Creates a live deployment that tracks the latest model version on a branch."""

    model_rid: ModelRid = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    branch: str
    """The model branch for the deployment."""

    type: typing.Literal["direct"] = "direct"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelRid](ModelRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DirectCreateLiveDeploymentTarget.md)
