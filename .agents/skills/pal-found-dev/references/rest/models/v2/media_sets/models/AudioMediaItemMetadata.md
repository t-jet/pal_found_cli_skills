# foundry_sdk.v2.media_sets.models.AudioMediaItemMetadata


Metadata for audio media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | AudioDecodeFormat | required; no default | No additional field description in SDK source. |
| specification | specification | AudioSpecification | required; no default | No additional field description in SDK source. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| type | type | typing.Literal['audio'] | 'audio' | No additional field description in SDK source. |

```python
class AudioMediaItemMetadata(core.ModelBase):
    """Metadata for audio media items."""

    format: AudioDecodeFormat
    specification: AudioSpecification
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["audio"] = "audio"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.AudioDecodeFormat](AudioDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.AudioSpecification](AudioSpecification.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AudioMediaItemMetadata.md)
