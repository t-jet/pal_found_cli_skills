# foundry_sdk.v2.streams.models.Stream


Stream

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch_name | branchName | core_models.BranchName | required; no default | No additional field description in SDK source. |
| schema_ | schema | core_models.StreamSchema | required; no default | The Foundry schema for this stream. |
| view_rid | viewRid | ViewRid | required; no default | The view that this stream corresponds to. |
| partitions_count | partitionsCount | PartitionsCount | required; no default | The number of partitions for the Foundry stream. Defaults to 1.<br><br>    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions<br>    are recommended. |
| stream_type | streamType | StreamType | required; no default | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and<br>    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY. |
| compressed | compressed | Compressed | required; no default | Whether or not compression is enabled for the stream. Defaults to false. |

```python
class Stream(core.ModelBase):
    """Stream"""

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    schema_: core_models.StreamSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The Foundry schema for this stream."""

    view_rid: ViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    """The view that this stream corresponds to."""

    partitions_count: PartitionsCount = pydantic.Field(alias=str("partitionsCount"))  # type: ignore[literal-required]
    """
    The number of partitions for the Foundry stream. Defaults to 1.

    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.
    """

    stream_type: StreamType = pydantic.Field(alias=str("streamType"))  # type: ignore[literal-required]
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
    """

    compressed: Compressed
    """Whether or not compression is enabled for the stream. Defaults to false."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.StreamSchema](../../core/models/StreamSchema.md)
- [foundry_sdk.v2.streams.models.Compressed](Compressed.md)
- [foundry_sdk.v2.streams.models.PartitionsCount](PartitionsCount.md)
- [foundry_sdk.v2.streams.models.StreamType](StreamType.md)
- [foundry_sdk.v2.streams.models.ViewRid](ViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Stream.md)
