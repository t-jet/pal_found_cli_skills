# foundry_sdk.v2.models.models.UnsupportedTypeError


Input contains an unsupported data type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| unsupported_type | unsupportedType | str | required; no default | The unsupported data type |
| type | type | typing.Literal['unsupportedType'] | 'unsupportedType' | No additional field description in SDK source. |

```python
class UnsupportedTypeError(core.ModelBase):
    """Input contains an unsupported data type."""

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    """The unsupported data type"""

    type: typing.Literal["unsupportedType"] = "unsupportedType"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UnsupportedTypeError.md)
