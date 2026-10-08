# foundry_sdk.v1.ontologies.models.SearchObjectsResponse


SearchObjectsResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[OntologyObject] | required; no default | No additional field description in SDK source. |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| total_count | totalCount | core_models.TotalCount | required; no default | No additional field description in SDK source. |

```python
class SearchObjectsResponse(core.ModelBase):
    """SearchObjectsResponse"""

    data: typing.List[OntologyObject]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v1.core.models.TotalCount](../../core/models/TotalCount.md)
- [foundry_sdk.v1.ontologies.models.OntologyObject](OntologyObject.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchObjectsResponse.md)
