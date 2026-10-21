# foundry_sdk.v2.media_sets.models.ImageSpec


Specification for image processing parameters used in vision-based extraction.
Controls how document pages are converted to images before being sent to vision models.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resizing_mode | resizingMode | ResizingMode | required; no default | No additional field description in SDK source. |
| height | height | typing.Optional[int] | None | Target height in pixels. |
| width | width | typing.Optional[int] | None | Target width in pixels. |
| mime_type | mimeType | ImageryDecodeFormat | required; no default | No additional field description in SDK source. |

```python
class ImageSpec(core.ModelBase):
    """
    Specification for image processing parameters used in vision-based extraction.
    Controls how document pages are converted to images before being sent to vision models.
    """

    resizing_mode: ResizingMode = pydantic.Field(alias=str("resizingMode"))  # type: ignore[literal-required]
    height: typing.Optional[int] = None
    """Target height in pixels."""

    width: typing.Optional[int] = None
    """Target width in pixels."""

    mime_type: ImageryDecodeFormat = pydantic.Field(alias=str("mimeType"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ImageryDecodeFormat](ImageryDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.ResizingMode](ResizingMode.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ImageSpec.md)
