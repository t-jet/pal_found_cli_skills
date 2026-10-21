# foundry_sdk.v2.ontologies.models.NumberFormatRatio


Display the value as a ratio with different scaling factors and suffixes:
- PERCENTAGE: Multiply by 100 and add "%" suffix (0.15 → "15%")
- PER_MILLE: Multiply by 1000 and add "‰" suffix (0.015 → "15‰")
- BASIS_POINTS: Multiply by 10000 and add "bps" suffix (0.0015 → "15bps")

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ratio_type | ratioType | NumberRatioType | required; no default | No additional field description in SDK source. |
| base_format_options | baseFormatOptions | NumberFormatOptions | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['ratio'] | 'ratio' | No additional field description in SDK source. |

```python
class NumberFormatRatio(core.ModelBase):
    """
    Display the value as a ratio with different scaling factors and suffixes:
    - PERCENTAGE: Multiply by 100 and add "%" suffix (0.15 → "15%")
    - PER_MILLE: Multiply by 1000 and add "‰" suffix (0.015 → "15‰")
    - BASIS_POINTS: Multiply by 10000 and add "bps" suffix (0.0015 → "15bps")
    """

    ratio_type: NumberRatioType = pydantic.Field(alias=str("ratioType"))  # type: ignore[literal-required]
    base_format_options: NumberFormatOptions = pydantic.Field(alias=str("baseFormatOptions"))  # type: ignore[literal-required]
    type: typing.Literal["ratio"] = "ratio"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](NumberFormatOptions.md)
- [foundry_sdk.v2.ontologies.models.NumberRatioType](NumberRatioType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatRatio.md)
