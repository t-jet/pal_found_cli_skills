# foundry_sdk.v2.ontologies.models.MaxAggregationV2


Computes the maximum value for the provided field.
Either `field` or `propertyIdentifier` must be supplied, but not both.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | typing.Optional[PropertyApiName] | None | No additional field description in SDK source. |
| property_identifier | propertyIdentifier | typing.Optional[PropertyIdentifier] | default None | No additional field description in SDK source. |
| name | name | typing.Optional[AggregationMetricName] | None | No additional field description in SDK source. |
| direction | direction | typing.Optional[OrderByDirection] | None | No additional field description in SDK source. |
| type | type | typing.Literal['max'] | 'max' | No additional field description in SDK source. |

```python
class MaxAggregationV2(core.ModelBase):
    """
    Computes the maximum value for the provided field.
    Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["max"] = "max"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.AggregationMetricName](AggregationMetricName.md)
- [foundry_sdk.v2.ontologies.models.OrderByDirection](OrderByDirection.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MaxAggregationV2.md)
