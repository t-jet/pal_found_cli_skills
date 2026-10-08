# foundry_sdk.v2.sql_queries.models.ParameterListValue


A parameter value that is a list of other parameter values. All values in the list must be of the same type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| values | values | typing.List[ParameterValue] | required; no default | No additional field description in SDK source. |
| element_type | elementType | ColumnType | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['list'] | 'list' | No additional field description in SDK source. |

```python
class ParameterListValue(core.ModelBase):
    """A parameter value that is a list of other parameter values. All values in the list must be of the same type."""

    values: typing.List[ParameterValue]
    element_type: ColumnType = pydantic.Field(alias=str("elementType"))  # type: ignore[literal-required]
    type: typing.Literal["list"] = "list"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.sql_queries.models.ColumnType](ColumnType.md)
- [foundry_sdk.v2.sql_queries.models.ParameterValue](ParameterValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterListValue.md)
