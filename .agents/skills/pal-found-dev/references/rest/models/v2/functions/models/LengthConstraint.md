# foundry_sdk.v2.functions.models.LengthConstraint


LengthConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| minimum_length | minimumLength | typing.Optional[int] | default None | No additional field description in SDK source. |
| maximum_length | maximumLength | typing.Optional[int] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['length'] | 'length' | No additional field description in SDK source. |

```python
class LengthConstraint(core.ModelBase):
    """LengthConstraint"""

    minimum_length: typing.Optional[int] = pydantic.Field(alias=str("minimumLength"), default=None)  # type: ignore[literal-required]
    maximum_length: typing.Optional[int] = pydantic.Field(alias=str("maximumLength"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["length"] = "length"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LengthConstraint.md)
