# foundry_sdk.v2.ontologies.models.NumberFormatCurrency


Format numbers as currency values with proper symbols and styling.
Example: 1234.56 with currency "USD" displays as "USD 1,234.56" (standard) or "USD 1.2K" (compact)

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| base_format_options | baseFormatOptions | NumberFormatOptions | required; no default | No additional field description in SDK source. |
| style | style | NumberFormatCurrencyStyle | required; no default | No additional field description in SDK source. |
| currency_code | currencyCode | PropertyTypeReferenceOrStringConstant | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['currency'] | 'currency' | No additional field description in SDK source. |

```python
class NumberFormatCurrency(core.ModelBase):
    """
    Format numbers as currency values with proper symbols and styling.
    Example: 1234.56 with currency "USD" displays as "USD 1,234.56" (standard) or "USD 1.2K" (compact)
    """

    base_format_options: NumberFormatOptions = pydantic.Field(alias=str("baseFormatOptions"))  # type: ignore[literal-required]
    style: NumberFormatCurrencyStyle
    currency_code: PropertyTypeReferenceOrStringConstant = pydantic.Field(alias=str("currencyCode"))  # type: ignore[literal-required]
    type: typing.Literal["currency"] = "currency"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatCurrencyStyle](NumberFormatCurrencyStyle.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](NumberFormatOptions.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReferenceOrStringConstant](PropertyTypeReferenceOrStringConstant.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatCurrency.md)
