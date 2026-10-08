# foundry_sdk.v2.media_sets.models.GeoMetadata


Embedded geo-referencing data for an image.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| crs | crs | typing.Optional[CoordinateReferenceSystem] | None | No additional field description in SDK source. |
| geotransform | geotransform | typing.Optional[AffineTransform] | None | No additional field description in SDK source. |
| gcp_info | gcpInfo | typing.Optional[GcpList] | default None | No additional field description in SDK source. |
| gps_data | gpsData | typing.Optional[GpsMetadata] | default None | No additional field description in SDK source. |

```python
class GeoMetadata(core.ModelBase):
    """Embedded geo-referencing data for an image."""

    crs: typing.Optional[CoordinateReferenceSystem] = None
    geotransform: typing.Optional[AffineTransform] = None
    gcp_info: typing.Optional[GcpList] = pydantic.Field(alias=str("gcpInfo"), default=None)  # type: ignore[literal-required]
    gps_data: typing.Optional[GpsMetadata] = pydantic.Field(alias=str("gpsData"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.AffineTransform](AffineTransform.md)
- [foundry_sdk.v2.media_sets.models.CoordinateReferenceSystem](CoordinateReferenceSystem.md)
- [foundry_sdk.v2.media_sets.models.GcpList](GcpList.md)
- [foundry_sdk.v2.media_sets.models.GpsMetadata](GpsMetadata.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GeoMetadata.md)
