# foundry_sdk.v2.models.models.ModelOutput


Model output configuration.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| model_rid | modelRid | ModelRid | required; no default | The RID of the output model. |
| type | type | typing.Literal['model'] | 'model' | No additional field description in SDK source. |

```python
class ModelOutput(core.ModelBase):
    """Model output configuration."""

    model_rid: ModelRid = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    """The RID of the output model."""

    type: typing.Literal["model"] = "model"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelRid](ModelRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelOutput.md)
