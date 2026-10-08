# foundry_sdk.v2.media_sets.models.GetEmailAttachmentOperation


Retrieves the bytes of an email attachment by index.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| mime_type | mimeType | str | required; no default | The MIME type of the attachment. Must match the metadata attachment MIME type. |
| attachment_index | attachmentIndex | int | required; no default | The attachment index. |
| type | type | typing.Literal['getEmailAttachment'] | 'getEmailAttachment' | No additional field description in SDK source. |

```python
class GetEmailAttachmentOperation(core.ModelBase):
    """Retrieves the bytes of an email attachment by index."""

    mime_type: str = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]
    """The MIME type of the attachment. Must match the metadata attachment MIME type."""

    attachment_index: int = pydantic.Field(alias=str("attachmentIndex"))  # type: ignore[literal-required]
    """The attachment index."""

    type: typing.Literal["getEmailAttachment"] = "getEmailAttachment"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetEmailAttachmentOperation.md)
