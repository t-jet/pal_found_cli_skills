# foundry_sdk.v2.media_sets.models.GetMediaItemInfoResponse


GetMediaItemInfoResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| view_rid | viewRid | core_models.MediaSetViewRid | required; no default | No additional field description in SDK source. |
| path | path | typing.Optional[core_models.MediaItemPath] | None | No additional field description in SDK source. |
| logical_timestamp | logicalTimestamp | LogicalTimestamp | required; no default | No additional field description in SDK source. |
| attribution | attribution | typing.Optional[MediaAttribution] | None | No additional field description in SDK source. |
| originally_uploaded_file_mime_type | originallyUploadedFileMimeType | typing.Optional[core_models.MediaType] | default None | No additional field description in SDK source. |
| mime_type | mimeType | typing.Optional[core_models.MediaType] | default None | No additional field description in SDK source. |
| size_bytes | sizeBytes | typing.Optional[int] | default None | The size of the media item in bytes. |

```python
class GetMediaItemInfoResponse(core.ModelBase):
    """GetMediaItemInfoResponse"""

    view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    path: typing.Optional[core_models.MediaItemPath] = None
    logical_timestamp: LogicalTimestamp = pydantic.Field(alias=str("logicalTimestamp"))  # type: ignore[literal-required]
    attribution: typing.Optional[MediaAttribution] = None
    originally_uploaded_file_mime_type: typing.Optional[core_models.MediaType] = pydantic.Field(alias=str("originallyUploadedFileMimeType"), default=None)  # type: ignore[literal-required]
    mime_type: typing.Optional[core_models.MediaType] = pydantic.Field(alias=str("mimeType"), default=None)  # type: ignore[literal-required]
    size_bytes: typing.Optional[int] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    """The size of the media item in bytes."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MediaItemPath](../../core/models/MediaItemPath.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.core.models.MediaType](../../core/models/MediaType.md)
- [foundry_sdk.v2.media_sets.models.LogicalTimestamp](LogicalTimestamp.md)
- [foundry_sdk.v2.media_sets.models.MediaAttribution](MediaAttribution.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetMediaItemInfoResponse.md)
