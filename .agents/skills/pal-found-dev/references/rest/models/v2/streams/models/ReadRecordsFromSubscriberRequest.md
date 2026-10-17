# foundry_sdk.v2.streams.models.ReadRecordsFromSubscriberRequest


ReadRecordsFromSubscriberRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| view_rid | viewRid | typing.Optional[ViewRid] | default None | The view RID to read from. If not provided, reads from the latest view for the<br>    dataset/branch. |
| limit | limit | typing.Optional[int] | None | Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value <br>    greater than 1000 is requested, only 1000 records will be returned. |
| partition_ids | partitionIds | typing.Optional[typing.List[PartitionId]] | default None | If specified, only read from these partitions. Otherwise, read from all partitions. |
| auto_commit | autoCommit | typing.Optional[bool] | default None | If true, the read position is automatically committed after reading records.<br>    The committed position will be the offset after the last record read.<br>    If false, you must call the `commitOffsets` endpoint to commit offsets.<br>    Defaults to false. |

```python
class ReadRecordsFromSubscriberRequest(core.ModelBase):
    """ReadRecordsFromSubscriberRequest"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    The view RID to read from. If not provided, reads from the latest view for the
    dataset/branch.
    """

    limit: typing.Optional[int] = None
    """
    Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value 
    greater than 1000 is requested, only 1000 records will be returned.
    """

    partition_ids: typing.Optional[typing.List[PartitionId]] = pydantic.Field(alias=str("partitionIds"), default=None)  # type: ignore[literal-required]
    """If specified, only read from these partitions. Otherwise, read from all partitions."""

    auto_commit: typing.Optional[bool] = pydantic.Field(alias=str("autoCommit"), default=None)  # type: ignore[literal-required]
    """
    If true, the read position is automatically committed after reading records.
    The committed position will be the offset after the last record read.
    If false, you must call the `commitOffsets` endpoint to commit offsets.
    Defaults to false.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.streams.models.PartitionId](PartitionId.md)
- [foundry_sdk.v2.streams.models.ViewRid](ViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReadRecordsFromSubscriberRequest.md)
