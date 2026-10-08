# foundry_sdk.v2.streams.models.ReadSubscriberRecordsResponse


Response containing records grouped by partition ID.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| records_by_partition | recordsByPartition | typing.Dict[PartitionId, PartitionRecords] | required; no default | Records grouped by partition ID. |

```python
class ReadSubscriberRecordsResponse(core.ModelBase):
    """Response containing records grouped by partition ID."""

    records_by_partition: typing.Dict[PartitionId, PartitionRecords] = pydantic.Field(alias=str("recordsByPartition"))  # type: ignore[literal-required]
    """Records grouped by partition ID."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.streams.models.PartitionId](PartitionId.md)
- [foundry_sdk.v2.streams.models.PartitionRecords](PartitionRecords.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReadSubscriberRecordsResponse.md)
