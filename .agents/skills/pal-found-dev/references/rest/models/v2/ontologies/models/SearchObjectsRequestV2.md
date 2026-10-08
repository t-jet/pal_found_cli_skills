# foundry_sdk.v2.ontologies.models.SearchObjectsRequestV2


SearchObjectsRequestV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| where | where | typing.Optional[SearchJsonQueryV2] | None | No additional field description in SDK source. |
| order_by | orderBy | typing.Optional[SearchOrderByV2] | default None | No additional field description in SDK source. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | No additional field description in SDK source. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| select | select | typing.List[PropertyApiName] | required; no default | The API names of the object type properties to include in the response. |
| select_v2 | selectV2 | typing.Optional[typing.List[PropertyIdentifier]] | default None | The identifiers of the properties to include in the response. Only selectV2 or select should be populated,<br>    but not both. |
| exclude_rid | excludeRid | typing.Optional[bool] | default None | A flag to exclude the retrieval of the `__rid` property.<br>    Setting this to true may improve performance of this endpoint for object types in OSV2. |
| snapshot | snapshot | typing.Optional[bool] | None | A flag to use snapshot consistency when paging.<br>    Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items.<br>    Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items.<br>    This defaults to false if not specified, which means you will always get the latest results. |
| reference_signing_options | referenceSigningOptions | typing.Optional[ReferenceSigningOptions] | default None | No additional field description in SDK source. |

```python
class SearchObjectsRequestV2(core.ModelBase):
    """SearchObjectsRequestV2"""

    where: typing.Optional[SearchJsonQueryV2] = None
    order_by: typing.Optional[SearchOrderByV2] = pydantic.Field(alias=str("orderBy"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    select: typing.List[PropertyApiName]
    """The API names of the object type properties to include in the response."""

    select_v2: typing.Optional[typing.List[PropertyIdentifier]] = pydantic.Field(alias=str("selectV2"), default=None)  # type: ignore[literal-required]
    """
    The identifiers of the properties to include in the response. Only selectV2 or select should be populated,
    but not both.
    """

    exclude_rid: typing.Optional[bool] = pydantic.Field(alias=str("excludeRid"), default=None)  # type: ignore[literal-required]
    """
    A flag to exclude the retrieval of the `__rid` property.
    Setting this to true may improve performance of this endpoint for object types in OSV2.
    """

    snapshot: typing.Optional[bool] = None
    """
    A flag to use snapshot consistency when paging.
    Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items.
    Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items.
    This defaults to false if not specified, which means you will always get the latest results.
    """

    reference_signing_options: typing.Optional[ReferenceSigningOptions] = pydantic.Field(alias=str("referenceSigningOptions"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.ReferenceSigningOptions](ReferenceSigningOptions.md)
- [foundry_sdk.v2.ontologies.models.SearchJsonQueryV2](SearchJsonQueryV2.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderByV2](SearchOrderByV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchObjectsRequestV2.md)
