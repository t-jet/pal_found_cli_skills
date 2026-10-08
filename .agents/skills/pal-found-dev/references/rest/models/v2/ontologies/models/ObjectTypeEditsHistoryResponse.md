# foundry_sdk.v2.ontologies.models.ObjectTypeEditsHistoryResponse


Response containing the history of edits for objects of a specific object type.
Only contains object edits (create, modify, delete) - link edits are not included.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[ObjectEditHistoryEntry] | required; no default | List of historical edits for this object type |
| total_count | totalCount | typing.Optional[int] | default None | Count of items in the data array above |
| next_page_token | nextPageToken | typing.Optional[str] | default None | Token for retrieving the next page of results |

```python
class ObjectTypeEditsHistoryResponse(core.ModelBase):
    """
    Response containing the history of edits for objects of a specific object type.
    Only contains object edits (create, modify, delete) - link edits are not included.
    """

    data: typing.List[ObjectEditHistoryEntry]
    """List of historical edits for this object type"""

    total_count: typing.Optional[int] = pydantic.Field(alias=str("totalCount"), default=None)  # type: ignore[literal-required]
    """Count of items in the data array above"""

    next_page_token: typing.Optional[str] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    """Token for retrieving the next page of results"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectEditHistoryEntry](ObjectEditHistoryEntry.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeEditsHistoryResponse.md)
