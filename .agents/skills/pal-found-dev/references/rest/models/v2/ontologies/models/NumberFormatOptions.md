# foundry_sdk.v2.ontologies.models.NumberFormatOptions


Base number formatting options that can be applied to all number formatters.
Controls precision, grouping, rounding, and notation. Consistent with JavaScript's Intl.NumberFormat.

Examples:
- useGrouping: true makes 1234567 display as "1,234,567"
- maximumFractionDigits: 2 makes 3.14159 display as "3.14"
- notation: SCIENTIFIC makes 1234 display as "1.234E3"

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| use_grouping | useGrouping | typing.Optional[bool] | default None | If true, show a locale-appropriate number grouping (e.g. thousands for en). |
| convert_negative_to_parenthesis | convertNegativeToParenthesis | typing.Optional[bool] | default None | If true, wrap negative numbers in parentheses instead of a minus sign. |
| minimum_integer_digits | minimumIntegerDigits | typing.Optional[int] | default None | No additional field description in SDK source. |
| minimum_fraction_digits | minimumFractionDigits | typing.Optional[int] | default None | No additional field description in SDK source. |
| maximum_fraction_digits | maximumFractionDigits | typing.Optional[int] | default None | No additional field description in SDK source. |
| minimum_significant_digits | minimumSignificantDigits | typing.Optional[int] | default None | No additional field description in SDK source. |
| maximum_significant_digits | maximumSignificantDigits | typing.Optional[int] | default None | No additional field description in SDK source. |
| notation | notation | typing.Optional[NumberFormatNotation] | None | No additional field description in SDK source. |
| rounding_mode | roundingMode | typing.Optional[NumberRoundingMode] | default None | No additional field description in SDK source. |

```python
class NumberFormatOptions(core.ModelBase):
    """
    Base number formatting options that can be applied to all number formatters.
    Controls precision, grouping, rounding, and notation. Consistent with JavaScript's Intl.NumberFormat.

    Examples:
    - useGrouping: true makes 1234567 display as "1,234,567"
    - maximumFractionDigits: 2 makes 3.14159 display as "3.14"
    - notation: SCIENTIFIC makes 1234 display as "1.234E3"
    """

    use_grouping: typing.Optional[bool] = pydantic.Field(alias=str("useGrouping"), default=None)  # type: ignore[literal-required]
    """If true, show a locale-appropriate number grouping (e.g. thousands for en)."""

    convert_negative_to_parenthesis: typing.Optional[bool] = pydantic.Field(alias=str("convertNegativeToParenthesis"), default=None)  # type: ignore[literal-required]
    """If true, wrap negative numbers in parentheses instead of a minus sign."""

    minimum_integer_digits: typing.Optional[int] = pydantic.Field(alias=str("minimumIntegerDigits"), default=None)  # type: ignore[literal-required]
    minimum_fraction_digits: typing.Optional[int] = pydantic.Field(alias=str("minimumFractionDigits"), default=None)  # type: ignore[literal-required]
    maximum_fraction_digits: typing.Optional[int] = pydantic.Field(alias=str("maximumFractionDigits"), default=None)  # type: ignore[literal-required]
    minimum_significant_digits: typing.Optional[int] = pydantic.Field(alias=str("minimumSignificantDigits"), default=None)  # type: ignore[literal-required]
    maximum_significant_digits: typing.Optional[int] = pydantic.Field(alias=str("maximumSignificantDigits"), default=None)  # type: ignore[literal-required]
    notation: typing.Optional[NumberFormatNotation] = None
    rounding_mode: typing.Optional[NumberRoundingMode] = pydantic.Field(alias=str("roundingMode"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatNotation](NumberFormatNotation.md)
- [foundry_sdk.v2.ontologies.models.NumberRoundingMode](NumberRoundingMode.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatOptions.md)
