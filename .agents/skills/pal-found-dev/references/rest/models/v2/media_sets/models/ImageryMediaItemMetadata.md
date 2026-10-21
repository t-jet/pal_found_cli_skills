# foundry_sdk.v2.media_sets.models.ImageryMediaItemMetadata


Metadata for imagery (image) media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | ImageryDecodeFormat | required; no default | No additional field description in SDK source. |
| dimensions | dimensions | typing.Optional[Dimensions] | None | No additional field description in SDK source. |
| bands | bands | typing.List[BandInfo] | required; no default | Information about the bands of the image, if available. |
| attributes | attributes | typing.Dict[ImageAttributeDomain, typing.Dict[ImageAttributeKey, str]] | required; no default | The metadata attributes described in the image header in the form of a map <domain, <key, value>>.<br>    For the default domain, or when the domain is not specified, the domain key will be the empty string (""). |
| icc_profile | iccProfile | typing.Optional[str] | default None | The base64-encoded ICC profile for the image, if available. |
| geo | geo | typing.Optional[GeoMetadata] | None | No additional field description in SDK source. |
| pages | pages | typing.Optional[int] | None | The number of pages associated with this image. Usually 1, but may be more for some formats<br>    (multi-page TIFFs, for example). |
| orientation | orientation | typing.Optional[Orientation] | None | No additional field description in SDK source. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| type | type | typing.Literal['imagery'] | 'imagery' | No additional field description in SDK source. |

```python
class ImageryMediaItemMetadata(core.ModelBase):
    """Metadata for imagery (image) media items."""

    format: ImageryDecodeFormat
    dimensions: typing.Optional[Dimensions] = None
    bands: typing.List[BandInfo]
    """Information about the bands of the image, if available."""

    attributes: typing.Dict[ImageAttributeDomain, typing.Dict[ImageAttributeKey, str]]
    """
    The metadata attributes described in the image header in the form of a map <domain, <key, value>>.
    For the default domain, or when the domain is not specified, the domain key will be the empty string ("").
    """

    icc_profile: typing.Optional[str] = pydantic.Field(alias=str("iccProfile"), default=None)  # type: ignore[literal-required]
    """The base64-encoded ICC profile for the image, if available."""

    geo: typing.Optional[GeoMetadata] = None
    pages: typing.Optional[int] = None
    """
    The number of pages associated with this image. Usually 1, but may be more for some formats
    (multi-page TIFFs, for example).
    """

    orientation: typing.Optional[Orientation] = None
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["imagery"] = "imagery"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.BandInfo](BandInfo.md)
- [foundry_sdk.v2.media_sets.models.Dimensions](Dimensions.md)
- [foundry_sdk.v2.media_sets.models.GeoMetadata](GeoMetadata.md)
- [foundry_sdk.v2.media_sets.models.ImageAttributeDomain](ImageAttributeDomain.md)
- [foundry_sdk.v2.media_sets.models.ImageAttributeKey](ImageAttributeKey.md)
- [foundry_sdk.v2.media_sets.models.ImageryDecodeFormat](ImageryDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.Orientation](Orientation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ImageryMediaItemMetadata.md)
