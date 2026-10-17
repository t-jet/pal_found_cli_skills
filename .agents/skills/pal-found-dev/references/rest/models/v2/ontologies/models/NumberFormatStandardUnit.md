# foundry_sdk.v2.ontologies.models.NumberFormatStandardUnit


Format numbers with standard units supported by Intl.NumberFormat.
Examples: "meter", "kilogram", "celsius", "percent"
Input: 25 with unit "celsius" displays as "25 degrees C"

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| base_format_options | baseFormatOptions | NumberFormatOptions | required; no default | No additional field description in SDK source. |
| unit | unit | PropertyTypeReferenceOrStringConstant | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['standardUnit'] | 'standardUnit' | No additional field description in SDK source. |

```python
class NumberFormatStandardUnit(core.ModelBase):
    """
    Format numbers with standard units supported by Intl.NumberFormat.
    Examples: "meter", "kilogram", "celsius", "percent"
    Input: 25 with unit "celsius" displays as "25 degrees C"
    """

    base_format_options: NumberFormatOptions = pydantic.Field(alias=str("baseFormatOptions"))  # type: ignore[literal-required]
    unit: PropertyTypeReferenceOrStringConstant
    type: typing.Literal["standardUnit"] = "standardUnit"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](NumberFormatOptions.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReferenceOrStringConstant](PropertyTypeReferenceOrStringConstant.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatStandardUnit.md)
