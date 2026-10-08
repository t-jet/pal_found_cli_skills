# foundry_sdk.v2.ontologies.models.SearchOrderByV2


Specifies the ordering of search results by a field and an ordering direction, or by relevance.
If the `fields` array is provided, `orderType` is automatically set to `fields`.
If this object is omitted entirely, the ordering is unspecified.

Setting `orderType` to `relevance` requests that results are sorted by decreasing relevance score.
For queries that include text search filters (e.g. `containsAllTerms`, `containsAnyTerm`,
`containsAllTermsInOrder`, `containsAllTermsInOrderPrefixLastTerm`) or `nearestNeighbors`, the
relevance score reflects how well each object matches the query. For other queries, the ordering
is unspecified.

When paging through results ordered by relevance, ordering is not guaranteed to be consistent
across pages: an object may appear on multiple pages or be skipped entirely. Use a single page
when result completeness is required.

Relevance ordering can be expensive and should only be used when required.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| order_type | orderType | typing.Optional[SearchOrderByType] | default None | No additional field description in SDK source. |
| fields | fields | typing.List[SearchOrderingV2] | required; no default | No additional field description in SDK source. |

```python
class SearchOrderByV2(core.ModelBase):
    """
    Specifies the ordering of search results by a field and an ordering direction, or by relevance.
    If the `fields` array is provided, `orderType` is automatically set to `fields`.
    If this object is omitted entirely, the ordering is unspecified.

    Setting `orderType` to `relevance` requests that results are sorted by decreasing relevance score.
    For queries that include text search filters (e.g. `containsAllTerms`, `containsAnyTerm`,
    `containsAllTermsInOrder`, `containsAllTermsInOrderPrefixLastTerm`) or `nearestNeighbors`, the
    relevance score reflects how well each object matches the query. For other queries, the ordering
    is unspecified.

    When paging through results ordered by relevance, ordering is not guaranteed to be consistent
    across pages: an object may appear on multiple pages or be skipped entirely. Use a single page
    when result completeness is required.

    Relevance ordering can be expensive and should only be used when required.
    """

    order_type: typing.Optional[SearchOrderByType] = pydantic.Field(alias=str("orderType"), default=None)  # type: ignore[literal-required]
    fields: typing.List[SearchOrderingV2]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderByType](SearchOrderByType.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderingV2](SearchOrderingV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchOrderByV2.md)
