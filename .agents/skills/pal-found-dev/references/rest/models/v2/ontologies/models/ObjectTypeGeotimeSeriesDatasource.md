# foundry_sdk.v2.ontologies.models.ObjectTypeGeotimeSeriesDatasource


An object type datasource backed by a Geotime series integration, providing values for Geotime series reference
properties.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| geotime_series_integration_rid | geotimeSeriesIntegrationRid | GeotimeSeriesIntegrationRid | required; no default | No additional field description in SDK source. |
| properties | properties | typing.List[PropertyApiName] | required; no default | The set of properties that are bound to the Geotime series. |
| type | type | typing.Literal['geotimeSeries'] | 'geotimeSeries' | No additional field description in SDK source. |

```python
class ObjectTypeGeotimeSeriesDatasource(core.ModelBase):
    """
    An object type datasource backed by a Geotime series integration, providing values for Geotime series reference
    properties.
    """

    geotime_series_integration_rid: GeotimeSeriesIntegrationRid = pydantic.Field(alias=str("geotimeSeriesIntegrationRid"))  # type: ignore[literal-required]
    properties: typing.List[PropertyApiName]
    """The set of properties that are bound to the Geotime series."""

    type: typing.Literal["geotimeSeries"] = "geotimeSeries"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.GeotimeSeriesIntegrationRid](GeotimeSeriesIntegrationRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeGeotimeSeriesDatasource.md)
