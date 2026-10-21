# foundry_sdk.v2.streams.models.CommitSubscriberOffsetsRequest


CommitSubscriberOffsetsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| view_rid | viewRid | typing.Optional[ViewRid] | default None | The view RID to commit offsets for. If not provided, uses the latest view for the<br>    dataset/branch. |
| offsets | offsets | PartitionOffsets | required; no default | The last processed offset for each partition. The server will store these as<br>    read positions (offset + 1), so the next read starts after the committed offset. |

```python
class CommitSubscriberOffsetsRequest(core.ModelBase):
    """CommitSubscriberOffsetsRequest"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    The view RID to commit offsets for. If not provided, uses the latest view for the
    dataset/branch.
    """

    offsets: PartitionOffsets
    """
    The last processed offset for each partition. The server will store these as
    read positions (offset + 1), so the next read starts after the committed offset.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.streams.models.PartitionOffsets](PartitionOffsets.md)
- [foundry_sdk.v2.streams.models.ViewRid](ViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CommitSubscriberOffsetsRequest.md)
