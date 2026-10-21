# foundry_sdk.v2.models.models.ModelVersionPromotedSource


Model version promoted from another model version.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| previous_model_rid | previousModelRid | ModelRid | required; no default | No additional field description in SDK source. |
| previous_model_version_rid | previousModelVersionRid | ModelVersionRid | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['promoted'] | 'promoted' | No additional field description in SDK source. |

```python
class ModelVersionPromotedSource(core.ModelBase):
    """Model version promoted from another model version."""

    previous_model_rid: ModelRid = pydantic.Field(alias=str("previousModelRid"))  # type: ignore[literal-required]
    previous_model_version_rid: ModelVersionRid = pydantic.Field(alias=str("previousModelVersionRid"))  # type: ignore[literal-required]
    type: typing.Literal["promoted"] = "promoted"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelRid](ModelRid.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](ModelVersionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelVersionPromotedSource.md)
