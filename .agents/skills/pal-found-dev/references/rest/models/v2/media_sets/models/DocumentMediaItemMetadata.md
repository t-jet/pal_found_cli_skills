# foundry_sdk.v2.media_sets.models.DocumentMediaItemMetadata


Metadata for document media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | DocumentDecodeFormat | required; no default | No additional field description in SDK source. |
| pages | pages | typing.Optional[int] | None | The number of pages in the document. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| title | title | typing.Optional[str] | None | The title of the document, if available. |
| author | author | typing.Optional[str] | None | The author of the document, if available. |
| type | type | typing.Literal['document'] | 'document' | No additional field description in SDK source. |

```python
class DocumentMediaItemMetadata(core.ModelBase):
    """Metadata for document media items."""

    format: DocumentDecodeFormat
    pages: typing.Optional[int] = None
    """The number of pages in the document."""

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    title: typing.Optional[str] = None
    """The title of the document, if available."""

    author: typing.Optional[str] = None
    """The author of the document, if available."""

    type: typing.Literal["document"] = "document"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.DocumentDecodeFormat](DocumentDecodeFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DocumentMediaItemMetadata.md)
