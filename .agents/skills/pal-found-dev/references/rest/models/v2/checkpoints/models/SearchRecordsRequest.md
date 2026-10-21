# foundry_sdk.v2.checkpoints.models.SearchRecordsRequest


SearchRecordsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| where | where | SearchCheckpointRecordsRequest | required; no default | No additional field description in SDK source. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | The page size for the search request. If no value is provided, a default of `100` will be used. |
| sort_direction | sortDirection | typing.Optional[SortDirection] | default None | Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC). |

```python
class SearchRecordsRequest(core.ModelBase):
    """SearchRecordsRequest"""

    where: SearchCheckpointRecordsRequest
    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    """The page size for the search request. If no value is provided, a default of `100` will be used."""

    sort_direction: typing.Optional[SortDirection] = pydantic.Field(alias=str("sortDirection"), default=None)  # type: ignore[literal-required]
    """Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC)."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsRequest](SearchCheckpointRecordsRequest.md)
- [foundry_sdk.v2.checkpoints.models.SortDirection](SortDirection.md)
- [foundry_sdk.v2.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchRecordsRequest.md)
