# foundry_sdk.v2.ontologies.models.NumberFormatCustomUnit


Format numbers with custom units not supported by standard formatting.
Use this for domain-specific units like "requests/sec", "widgets", etc.
Example: 1500 with unit "widgets" displays as "1,500 widgets"

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| base_format_options | baseFormatOptions | NumberFormatOptions | required; no default | No additional field description in SDK source. |
| unit | unit | PropertyTypeReferenceOrStringConstant | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['customUnit'] | 'customUnit' | No additional field description in SDK source. |

```python
class NumberFormatCustomUnit(core.ModelBase):
    """
    Format numbers with custom units not supported by standard formatting.
    Use this for domain-specific units like "requests/sec", "widgets", etc.
    Example: 1500 with unit "widgets" displays as "1,500 widgets"
    """

    base_format_options: NumberFormatOptions = pydantic.Field(alias=str("baseFormatOptions"))  # type: ignore[literal-required]
    unit: PropertyTypeReferenceOrStringConstant
    type: typing.Literal["customUnit"] = "customUnit"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](NumberFormatOptions.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReferenceOrStringConstant](PropertyTypeReferenceOrStringConstant.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatCustomUnit.md)
