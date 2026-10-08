# foundry_sdk.v2.models.models.SearchExperimentsParameterFilter


Filter that atomically binds a parameter name to a value comparison,
ensuring both conditions are evaluated on the same parameter.
Supported combinations:
- EQ: boolean, double, integer, or datetime value
- GT/LT: double, integer, or datetime value
- CONTAINS: string value (substring match on the parameter's string value)

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parameter_name | parameterName | ParameterName | required; no default | The exact name of the parameter to filter on. |
| operator | operator | SearchExperimentsParameterFilterOperator | required; no default | The comparison operator to apply. |
| value | value | typing.Any | required; no default | The value to compare against. |
| type | type | typing.Literal['parameterFilter'] | 'parameterFilter' | No additional field description in SDK source. |

```python
class SearchExperimentsParameterFilter(core.ModelBase):
    """
    Filter that atomically binds a parameter name to a value comparison,
    ensuring both conditions are evaluated on the same parameter.
    Supported combinations:
    - EQ: boolean, double, integer, or datetime value
    - GT/LT: double, integer, or datetime value
    - CONTAINS: string value (substring match on the parameter's string value)
    """

    parameter_name: ParameterName = pydantic.Field(alias=str("parameterName"))  # type: ignore[literal-required]
    """The exact name of the parameter to filter on."""

    operator: SearchExperimentsParameterFilterOperator
    """The comparison operator to apply."""

    value: typing.Any
    """The value to compare against."""

    type: typing.Literal["parameterFilter"] = "parameterFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ParameterName](ParameterName.md)
- [foundry_sdk.v2.models.models.SearchExperimentsParameterFilterOperator](SearchExperimentsParameterFilterOperator.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsParameterFilter.md)
