# foundry_sdk.v2.streams.models.PartitionOffsets


A map of partition IDs to offsets.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PartitionOffsets: typing_extensions.TypeAlias = typing.Dict["PartitionId", core.Long]
```

## Referenced definitions

- [foundry_sdk._core.utils.Long](../../../_core/Long.md)
- [foundry_sdk.v2.streams.models.PartitionId](PartitionId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PartitionOffsets.md)
