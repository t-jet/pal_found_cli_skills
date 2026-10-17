# foundry_sdk.v1.ontologies.models.ContainsQuery


Returns objects where the specified array contains a value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | FieldNameV1 | required; no default | No additional field description in SDK source. |
| value | value | PropertyValue | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['contains'] | 'contains' | No additional field description in SDK source. |

```python
class ContainsQuery(core.ModelBase):
    """Returns objects where the specified array contains a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["contains"] = "contains"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.FieldNameV1](FieldNameV1.md)
- [foundry_sdk.v1.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ContainsQuery.md)
