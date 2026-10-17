# foundry_sdk.v2.media_sets.models.VideoToArchiveTransformation


Extracts video frames to an archive format.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| encoding | encoding | ArchiveEncodeFormat | required; no default | No additional field description in SDK source. |
| operation | operation | VideoToArchiveOperation | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['videoToArchive'] | 'videoToArchive' | No additional field description in SDK source. |

```python
class VideoToArchiveTransformation(core.ModelBase):
    """Extracts video frames to an archive format."""

    encoding: ArchiveEncodeFormat
    operation: VideoToArchiveOperation
    type: typing.Literal["videoToArchive"] = "videoToArchive"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ArchiveEncodeFormat](ArchiveEncodeFormat.md)
- [foundry_sdk.v2.media_sets.models.VideoToArchiveOperation](VideoToArchiveOperation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VideoToArchiveTransformation.md)
