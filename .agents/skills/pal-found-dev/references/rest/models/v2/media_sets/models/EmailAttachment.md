# foundry_sdk.v2.media_sets.models.EmailAttachment


Metadata about an email attachment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| attachment_index | attachmentIndex | int | required; no default | The index of the attachment in the email. |
| file_name | fileName | typing.Optional[str] | default None | The file name of the attachment, if available. |
| mime_type | mimeType | str | required; no default | The verified MIME type of the attachment. |

```python
class EmailAttachment(core.ModelBase):
    """Metadata about an email attachment."""

    attachment_index: int = pydantic.Field(alias=str("attachmentIndex"))  # type: ignore[literal-required]
    """The index of the attachment in the email."""

    file_name: typing.Optional[str] = pydantic.Field(alias=str("fileName"), default=None)  # type: ignore[literal-required]
    """The file name of the attachment, if available."""

    mime_type: str = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]
    """The verified MIME type of the attachment."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EmailAttachment.md)
