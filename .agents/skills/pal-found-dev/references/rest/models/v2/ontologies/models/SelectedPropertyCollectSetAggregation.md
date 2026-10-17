# foundry_sdk.v2.ontologies.models.SelectedPropertyCollectSetAggregation


Lists all distinct values of a property up to the specified limit. The maximum supported limit is 100.

NOTE: A separate cardinality / exactCardinality aggregation should be used to determine the total count of
values, to account for a possible truncation of the returned set.

Ignores objects for which a property is absent, so the returned list will contain non-null values only.
Returns an empty list when none of the objects have values for a provided property.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| selected_property_api_name | selectedPropertyApiName | PropertyApiName | required; no default | No additional field description in SDK source. |
| limit | limit | int | required; no default | Maximum number of values to collect. The maximum supported limit is 100. |
| type | type | typing.Literal['collectSet'] | 'collectSet' | No additional field description in SDK source. |

```python
class SelectedPropertyCollectSetAggregation(core.ModelBase):
    """
    Lists all distinct values of a property up to the specified limit. The maximum supported limit is 100.

    NOTE: A separate cardinality / exactCardinality aggregation should be used to determine the total count of
    values, to account for a possible truncation of the returned set.

    Ignores objects for which a property is absent, so the returned list will contain non-null values only.
    Returns an empty list when none of the objects have values for a provided property.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    limit: int
    """Maximum number of values to collect. The maximum supported limit is 100."""

    type: typing.Literal["collectSet"] = "collectSet"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SelectedPropertyCollectSetAggregation.md)
