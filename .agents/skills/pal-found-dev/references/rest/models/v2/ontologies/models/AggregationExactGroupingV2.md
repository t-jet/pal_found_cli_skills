# foundry_sdk.v2.ontologies.models.AggregationExactGroupingV2


Divides objects into groups according to an exact value.
Either `field` or `propertyIdentifier` must be supplied, but not both.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | typing.Optional[PropertyApiName] | None | No additional field description in SDK source. |
| property_identifier | propertyIdentifier | typing.Optional[PropertyIdentifier] | default None | No additional field description in SDK source. |
| max_group_count | maxGroupCount | typing.Optional[int] | default None | The maximum number of groups to return. If omitted, defaults to 10,000.<br><br>    The server allocates resources based on the specified `maxGroupCount`. When the number of distinct<br>    values in your data is within this limit, results are accurate and the top N values are returned<br>    correctly. When distinct values exceed what the allocated resources can handle, results may become<br>    approximate.<br><br>    If you need accurate results with high-cardinality properties, set `maxGroupCount` high enough to<br>    cover your distinct values. Items exceeding the limit are excluded from results and counted in<br>    `excludedItems`. The response `accuracy` field indicates whether the results are `ACCURATE` or<br>    `APPROXIMATE`. |
| default_value | defaultValue | typing.Optional[str] | default None | Includes a group with the specified default value that includes all objects where the specified field's value is null.<br>    Cannot be used with includeNullValues. |
| include_null_values | includeNullValues | typing.Optional[bool] | default None | Includes a group with a null value that includes all objects where the specified field's value is null.<br>    Cannot be used with defaultValue or orderBy clauses on the aggregation. |
| type | type | typing.Literal['exact'] | 'exact' | No additional field description in SDK source. |

```python
class AggregationExactGroupingV2(core.ModelBase):
    """
    Divides objects into groups according to an exact value.
    Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    max_group_count: typing.Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of groups to return. If omitted, defaults to 10,000.

    The server allocates resources based on the specified `maxGroupCount`. When the number of distinct
    values in your data is within this limit, results are accurate and the top N values are returned
    correctly. When distinct values exceed what the allocated resources can handle, results may become
    approximate.

    If you need accurate results with high-cardinality properties, set `maxGroupCount` high enough to
    cover your distinct values. Items exceeding the limit are excluded from results and counted in
    `excludedItems`. The response `accuracy` field indicates whether the results are `ACCURATE` or
    `APPROXIMATE`.
    """

    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    """
    Includes a group with the specified default value that includes all objects where the specified field's value is null.
    Cannot be used with includeNullValues.
    """

    include_null_values: typing.Optional[bool] = pydantic.Field(alias=str("includeNullValues"), default=None)  # type: ignore[literal-required]
    """
    Includes a group with a null value that includes all objects where the specified field's value is null.
    Cannot be used with defaultValue or orderBy clauses on the aggregation.
    """

    type: typing.Literal["exact"] = "exact"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationExactGroupingV2.md)
