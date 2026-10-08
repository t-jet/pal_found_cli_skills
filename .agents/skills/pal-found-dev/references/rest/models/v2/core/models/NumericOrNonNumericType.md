# foundry_sdk.v2.core.models.NumericOrNonNumericType


The time series property can either contain either numeric or non-numeric data. This enables mixed sensor types
where some sensor time series are numeric and others are categorical. A boolean property reference can be used
to determine if the series is numeric or non-numeric. Without this property, the series type can be either
numeric or non-numeric and must be inferred from the result of a time series query.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| is_non_numeric_property_type_id | isNonNumericPropertyTypeId | typing.Optional[str] | default None | The boolean property type ID specifying whether the series is numeric or non-numeric. If the value is true,<br>    the series is non-numeric. |
| type | type | typing.Literal['numericOrNonNumeric'] | 'numericOrNonNumeric' | No additional field description in SDK source. |

```python
class NumericOrNonNumericType(core.ModelBase):
    """
    The time series property can either contain either numeric or non-numeric data. This enables mixed sensor types
    where some sensor time series are numeric and others are categorical. A boolean property reference can be used
    to determine if the series is numeric or non-numeric. Without this property, the series type can be either
    numeric or non-numeric and must be inferred from the result of a time series query.
    """

    is_non_numeric_property_type_id: typing.Optional[str] = pydantic.Field(alias=str("isNonNumericPropertyTypeId"), default=None)  # type: ignore[literal-required]
    """
    The boolean property type ID specifying whether the series is numeric or non-numeric. If the value is true,
    the series is non-numeric.
    """

    type: typing.Literal["numericOrNonNumeric"] = "numericOrNonNumeric"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumericOrNonNumericType.md)
