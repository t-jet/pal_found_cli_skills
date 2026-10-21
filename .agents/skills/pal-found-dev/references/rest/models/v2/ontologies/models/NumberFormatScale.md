# foundry_sdk.v2.ontologies.models.NumberFormatScale


Scale the numeric value by dividing by the specified factor and append an appropriate suffix.
- THOUSANDS: 1500 displays as "1.5K"
- MILLIONS: 2500000 displays as "2.5M"
- BILLIONS: 3200000000 displays as "3.2B"

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| scale_type | scaleType | NumberScaleType | required; no default | No additional field description in SDK source. |
| base_format_options | baseFormatOptions | NumberFormatOptions | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['scale'] | 'scale' | No additional field description in SDK source. |

```python
class NumberFormatScale(core.ModelBase):
    """
    Scale the numeric value by dividing by the specified factor and append an appropriate suffix.
    - THOUSANDS: 1500 displays as "1.5K"
    - MILLIONS: 2500000 displays as "2.5M"
    - BILLIONS: 3200000000 displays as "3.2B"
    """

    scale_type: NumberScaleType = pydantic.Field(alias=str("scaleType"))  # type: ignore[literal-required]
    base_format_options: NumberFormatOptions = pydantic.Field(alias=str("baseFormatOptions"))  # type: ignore[literal-required]
    type: typing.Literal["scale"] = "scale"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](NumberFormatOptions.md)
- [foundry_sdk.v2.ontologies.models.NumberScaleType](NumberScaleType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatScale.md)
