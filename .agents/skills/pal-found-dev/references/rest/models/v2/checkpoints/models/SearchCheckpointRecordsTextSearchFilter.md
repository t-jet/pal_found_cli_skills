# foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsTextSearchFilter


Filter for text search on justification fields.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | SearchCheckpointRecordsTextSearchFilterField | required; no default | No additional field description in SDK source. |
| query | query | str | required; no default | No additional field description in SDK source. |
| match_type | matchType | JustificationMatchType | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['textSearch'] | 'textSearch' | No additional field description in SDK source. |

```python
class SearchCheckpointRecordsTextSearchFilter(core.ModelBase):
    """Filter for text search on justification fields."""

    field: SearchCheckpointRecordsTextSearchFilterField
    query: str
    match_type: JustificationMatchType = pydantic.Field(alias=str("matchType"))  # type: ignore[literal-required]
    type: typing.Literal["textSearch"] = "textSearch"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.JustificationMatchType](JustificationMatchType.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsTextSearchFilterField](SearchCheckpointRecordsTextSearchFilterField.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchCheckpointRecordsTextSearchFilter.md)
