# foundry_sdk.v2.ontologies.models.ObjectTypeEditsHistoryRequest


Request object for querying object type edits history, containing both filters and pagination parameters

If objectPrimaryKey property is set, the method will return edits history for the particular object.
Otherwise, the method will return edits history for all objects of this object type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_primary_key | objectPrimaryKey | typing.Optional[ObjectPrimaryKeyV2] | default None | No additional field description in SDK source. |
| filters | filters | typing.Optional[EditsHistoryFilter] | None | No additional field description in SDK source. |
| sort_order | sortOrder | typing.Optional[EditsHistorySortOrder] | default None | No additional field description in SDK source. |
| include_all_previous_properties | includeAllPreviousProperties | typing.Optional[bool] | default None | No additional field description in SDK source. |
| page_size | pageSize | typing.Optional[int] | default None | The maximum number of edits to return per page. Defaults to 100. |
| page_token | pageToken | typing.Optional[str] | default None | Token for retrieving the next page of results |

```python
class ObjectTypeEditsHistoryRequest(core.ModelBase):
    """
    Request object for querying object type edits history, containing both filters and pagination parameters

    If objectPrimaryKey property is set, the method will return edits history for the particular object.
    Otherwise, the method will return edits history for all objects of this object type.
    """

    object_primary_key: typing.Optional[ObjectPrimaryKeyV2] = pydantic.Field(alias=str("objectPrimaryKey"), default=None)  # type: ignore[literal-required]
    filters: typing.Optional[EditsHistoryFilter] = None
    sort_order: typing.Optional[EditsHistorySortOrder] = pydantic.Field(alias=str("sortOrder"), default=None)  # type: ignore[literal-required]
    include_all_previous_properties: typing.Optional[bool] = pydantic.Field(alias=str("includeAllPreviousProperties"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[int] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    """The maximum number of edits to return per page. Defaults to 100."""

    page_token: typing.Optional[str] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    """Token for retrieving the next page of results"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.EditsHistoryFilter](EditsHistoryFilter.md)
- [foundry_sdk.v2.ontologies.models.EditsHistorySortOrder](EditsHistorySortOrder.md)
- [foundry_sdk.v2.ontologies.models.ObjectPrimaryKeyV2](ObjectPrimaryKeyV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeEditsHistoryRequest.md)
