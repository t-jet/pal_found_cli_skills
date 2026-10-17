# foundry_sdk.v2.media_sets.models.VideoToImageTransformation


Extracts video frames as images.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| encoding | encoding | ImageryEncodeFormat | required; no default | No additional field description in SDK source. |
| operation | operation | VideoToImageOperation | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['videoToImage'] | 'videoToImage' | No additional field description in SDK source. |

```python
class VideoToImageTransformation(core.ModelBase):
    """Extracts video frames as images."""

    encoding: ImageryEncodeFormat
    operation: VideoToImageOperation
    type: typing.Literal["videoToImage"] = "videoToImage"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ImageryEncodeFormat](ImageryEncodeFormat.md)
- [foundry_sdk.v2.media_sets.models.VideoToImageOperation](VideoToImageOperation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VideoToImageTransformation.md)
