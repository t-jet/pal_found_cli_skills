# foundry_sdk.v2.media_sets.models.EmailMediaItemMetadata


Metadata for email media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | EmailDecodeFormat | required; no default | No additional field description in SDK source. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| sender | sender | typing.List[Mailbox] | required; no default | The sender(s) of the email. |
| date | date | core.AwareDatetime | required; no default | The date the email was sent. |
| attachment_count | attachmentCount | int | required; no default | The number of attachments in the email. |
| to | to | typing.List[MailboxOrGroup] | required; no default | The recipient(s) of the email. |
| cc | cc | typing.List[MailboxOrGroup] | required; no default | The CC recipient(s) of the email. |
| subject | subject | typing.Optional[str] | None | The subject of the email. |
| attachments | attachments | typing.List[EmailAttachment] | required; no default | The attachments of the email. |
| type | type | typing.Literal['email'] | 'email' | No additional field description in SDK source. |

```python
class EmailMediaItemMetadata(core.ModelBase):
    """Metadata for email media items."""

    format: EmailDecodeFormat
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    sender: typing.List[Mailbox]
    """The sender(s) of the email."""

    date: core.AwareDatetime
    """The date the email was sent."""

    attachment_count: int = pydantic.Field(alias=str("attachmentCount"))  # type: ignore[literal-required]
    """The number of attachments in the email."""

    to: typing.List[MailboxOrGroup]
    """The recipient(s) of the email."""

    cc: typing.List[MailboxOrGroup]
    """The CC recipient(s) of the email."""

    subject: typing.Optional[str] = None
    """The subject of the email."""

    attachments: typing.List[EmailAttachment]
    """The attachments of the email."""

    type: typing.Literal["email"] = "email"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.media_sets.models.EmailAttachment](EmailAttachment.md)
- [foundry_sdk.v2.media_sets.models.EmailDecodeFormat](EmailDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.Mailbox](Mailbox.md)
- [foundry_sdk.v2.media_sets.models.MailboxOrGroup](MailboxOrGroup.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EmailMediaItemMetadata.md)
