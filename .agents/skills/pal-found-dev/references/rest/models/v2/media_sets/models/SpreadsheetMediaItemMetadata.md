# foundry_sdk.v2.media_sets.models.SpreadsheetMediaItemMetadata


Metadata for spreadsheet media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | SpreadsheetDecodeFormat | required; no default | No additional field description in SDK source. |
| sheet_names | sheetNames | typing.List[str] | required; no default | The names of the sheets in the spreadsheet. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| title | title | typing.Optional[str] | None | The title of the spreadsheet, if available. |
| author | author | typing.Optional[str] | None | The author of the spreadsheet, if available. |
| type | type | typing.Literal['spreadsheet'] | 'spreadsheet' | No additional field description in SDK source. |

```python
class SpreadsheetMediaItemMetadata(core.ModelBase):
    """Metadata for spreadsheet media items."""

    format: SpreadsheetDecodeFormat
    sheet_names: typing.List[str] = pydantic.Field(alias=str("sheetNames"))  # type: ignore[literal-required]
    """The names of the sheets in the spreadsheet."""

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    title: typing.Optional[str] = None
    """The title of the spreadsheet, if available."""

    author: typing.Optional[str] = None
    """The author of the spreadsheet, if available."""

    type: typing.Literal["spreadsheet"] = "spreadsheet"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.SpreadsheetDecodeFormat](SpreadsheetDecodeFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SpreadsheetMediaItemMetadata.md)
