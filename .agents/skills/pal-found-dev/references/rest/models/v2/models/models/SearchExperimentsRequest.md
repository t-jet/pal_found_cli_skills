# foundry_sdk.v2.models.models.SearchExperimentsRequest


SearchExperimentsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| where | where | typing.Optional[SearchExperimentsFilter] | None | Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. |
| order_by | orderBy | typing.Optional[SearchExperimentsOrderBy] | default None | The field to sort by. Default is to sort by relevance. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | The maximum number of results to return. Default 50, maximum of 100. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | PageToken to identify the next page to retrieve. Leave empty for the first request. |

```python
class SearchExperimentsRequest(core.ModelBase):
    """SearchExperimentsRequest"""

    where: typing.Optional[SearchExperimentsFilter] = None
    """Optional search filter for filtering experiments. If not provided, all experiments for the model are returned."""

    order_by: typing.Optional[SearchExperimentsOrderBy] = pydantic.Field(alias=str("orderBy"), default=None)  # type: ignore[literal-required]
    """The field to sort by. Default is to sort by relevance."""

    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    """The maximum number of results to return. Default 50, maximum of 100."""

    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    """PageToken to identify the next page to retrieve. Leave empty for the first request."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.models.models.SearchExperimentsFilter](SearchExperimentsFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsOrderBy](SearchExperimentsOrderBy.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsRequest.md)
