# foundry_sdk.v2.ontologies.models.GetOutgoingLinkTypesByObjectTypeRidBatchRequest


GetOutgoingLinkTypesByObjectTypeRidBatchRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| requests | requests | typing_extensions.Annotated[typing.List[GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)] | required; no default | No additional field description in SDK source. |
| filter_link_type_rids | filterLinkTypeRids | typing.List[LinkTypeRid] | required; no default | If provided, only return outgoing link types with RIDs in this list.<br>    If omitted, all outgoing link types for each requested object type are returned. |

```python
class GetOutgoingLinkTypesByObjectTypeRidBatchRequest(core.ModelBase):
    """GetOutgoingLinkTypesByObjectTypeRidBatchRequest"""

    requests: typing_extensions.Annotated[
        typing.List[GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement],
        annotated_types.Len(min_length=1, max_length=100),
    ]
    filter_link_type_rids: typing.List[LinkTypeRid] = pydantic.Field(alias=str("filterLinkTypeRids"))  # type: ignore[literal-required]
    """
    If provided, only return outgoing link types with RIDs in this list.
    If omitted, all outgoing link types for each requested object type are returned.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement](GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](LinkTypeRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetOutgoingLinkTypesByObjectTypeRidBatchRequest.md)
