# foundry_sdk.v2.ontologies.models.LoadGeotemporalSeriesRequest


The request body for loading entries from a geotemporal series reference property.

A geotemporal series represents time-indexed geographic observations for an object, such as the location history
of a vehicle or aircraft. Each entry in the response is a map of property names to values, following the same
structure as `OntologyObjectV2`.

The `range` field is required and restricts results to a specific time window. Both `startTime` and `endTime`
are required on `range`. The `additionalProperties` field controls which additional properties appear in each
returned entry. Results are paginated; use `pageToken` from a previous response to retrieve additional pages.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| range | range | AbsoluteTimeRange | required; no default | No additional field description in SDK source. |
| additional_properties | additionalProperties | typing.List[SelectedPropertyApiName] | required; no default | The additional property API names to include in each entry. The "time" and "position" properties are always<br>    included and do not need to be specified here. Use this to request additional geotemporal series metadata<br>    properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal<br>    integration will be omitted from the response entries. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | No additional field description in SDK source. |

```python
class LoadGeotemporalSeriesRequest(core.ModelBase):
    """
    The request body for loading entries from a geotemporal series reference property.

    A geotemporal series represents time-indexed geographic observations for an object, such as the location history
    of a vehicle or aircraft. Each entry in the response is a map of property names to values, following the same
    structure as `OntologyObjectV2`.

    The `range` field is required and restricts results to a specific time window. Both `startTime` and `endTime`
    are required on `range`. The `additionalProperties` field controls which additional properties appear in each
    returned entry. Results are paginated; use `pageToken` from a previous response to retrieve additional pages.
    """

    range: AbsoluteTimeRange
    additional_properties: typing.List[SelectedPropertyApiName] = pydantic.Field(alias=str("additionalProperties"))  # type: ignore[literal-required]
    """
    The additional property API names to include in each entry. The "time" and "position" properties are always
    included and do not need to be specified here. Use this to request additional geotemporal series metadata
    properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal
    integration will be omitted from the response entries.
    """

    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.ontologies.models.AbsoluteTimeRange](AbsoluteTimeRange.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApiName](SelectedPropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LoadGeotemporalSeriesRequest.md)
