# foundry_sdk.v1.core.models.UnsupportedType


UnsupportedType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| unsupported_type | unsupportedType | str | required; no default | No additional field description in SDK source. |
| params | params | typing.Dict[UnsupportedTypeParamKey, UnsupportedTypeParamValue] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['unsupported'] | 'unsupported' | No additional field description in SDK source. |

```python
class UnsupportedType(core.ModelBase):
    """UnsupportedType"""

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    params: typing.Dict[UnsupportedTypeParamKey, UnsupportedTypeParamValue]
    type: typing.Literal["unsupported"] = "unsupported"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.UnsupportedTypeParamKey](UnsupportedTypeParamKey.md)
- [foundry_sdk.v1.core.models.UnsupportedTypeParamValue](UnsupportedTypeParamValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UnsupportedType.md)
