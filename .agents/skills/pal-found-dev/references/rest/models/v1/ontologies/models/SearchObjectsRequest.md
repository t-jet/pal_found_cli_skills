# foundry_sdk.v1.ontologies.models.SearchObjectsRequest


SearchObjectsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| query | query | SearchJsonQuery | required; no default | No additional field description in SDK source. |
| order_by | orderBy | typing.Optional[SearchOrderBy] | default None | No additional field description in SDK source. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | No additional field description in SDK source. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| fields | fields | typing.List[PropertyApiName] | required; no default | The API names of the object type properties to include in the response. |

```python
class SearchObjectsRequest(core.ModelBase):
    """SearchObjectsRequest"""

    query: SearchJsonQuery
    order_by: typing.Optional[SearchOrderBy] = pydantic.Field(alias=str("orderBy"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    fields: typing.List[PropertyApiName]
    """The API names of the object type properties to include in the response."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v1.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v1.ontologies.models.SearchJsonQuery](SearchJsonQuery.md)
- [foundry_sdk.v1.ontologies.models.SearchOrderBy](SearchOrderBy.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchObjectsRequest.md)
