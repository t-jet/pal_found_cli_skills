# foundry_sdk.v2.ontologies.models.ExtractPropertyExpression


Extracts the specified date part from a date or timestamp.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| property | property | DerivedPropertyDefinition | required; no default | No additional field description in SDK source. |
| part | part | ExtractDatePart | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['extract'] | 'extract' | No additional field description in SDK source. |

```python
class ExtractPropertyExpression(core.ModelBase):
    """Extracts the specified date part from a date or timestamp."""

    property: DerivedPropertyDefinition
    part: ExtractDatePart
    type: typing.Literal["extract"] = "extract"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.DerivedPropertyDefinition](DerivedPropertyDefinition.md)
- [foundry_sdk.v2.ontologies.models.ExtractDatePart](ExtractDatePart.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExtractPropertyExpression.md)
