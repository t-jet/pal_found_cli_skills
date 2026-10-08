# foundry_sdk.v2.ontologies.models.GeoJsonString


A GeoJSON geometry specification.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| geo_json | geoJson | str | required; no default | A GeoJSON geometry string. Supported geometry types include Point, MultiPoint, LineString,<br>    MultiLineString, Polygon, MultiPolygon, and GeometryCollection. |
| type | type | typing.Literal['geoJson'] | 'geoJson' | No additional field description in SDK source. |

```python
class GeoJsonString(core.ModelBase):
    """A GeoJSON geometry specification."""

    geo_json: str = pydantic.Field(alias=str("geoJson"))  # type: ignore[literal-required]
    """
    A GeoJSON geometry string. Supported geometry types include Point, MultiPoint, LineString,
    MultiLineString, Polygon, MultiPolygon, and GeometryCollection.
    """

    type: typing.Literal["geoJson"] = "geoJson"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GeoJsonString.md)
