# foundry_sdk.v2.ontologies.models.AttachmentV2


The representation of an attachment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | AttachmentRid | required; no default | No additional field description in SDK source. |
| filename | filename | core_models.Filename | required; no default | No additional field description in SDK source. |
| size_bytes | sizeBytes | core_models.SizeBytes | required; no default | No additional field description in SDK source. |
| media_type | mediaType | core_models.MediaType | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['single'] | 'single' | No additional field description in SDK source. |

```python
class AttachmentV2(core.ModelBase):
    """The representation of an attachment."""

    rid: AttachmentRid
    filename: core_models.Filename
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    type: typing.Literal["single"] = "single"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.Filename](../../core/models/Filename.md)
- [foundry_sdk.v2.core.models.MediaType](../../core/models/MediaType.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../core/models/SizeBytes.md)
- [foundry_sdk.v2.ontologies.models.AttachmentRid](AttachmentRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AttachmentV2.md)
