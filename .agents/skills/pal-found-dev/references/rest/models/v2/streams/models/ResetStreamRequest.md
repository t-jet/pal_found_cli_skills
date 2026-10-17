# foundry_sdk.v2.streams.models.ResetStreamRequest


ResetStreamRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| schema_ | schema | typing.Optional[core_models.StreamSchema] | default None | The Foundry schema to apply to the new stream. <br><br>    If omitted, the schema of the existing stream on the branch will be used. |
| partitions_count | partitionsCount | typing.Optional[PartitionsCount] | default None | The number of partitions for the Foundry stream.<br>    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions<br>    are recommended.<br><br>    If omitted, the partitions count of the existing stream on the branch will be used. |
| stream_type | streamType | typing.Optional[StreamType] | default None | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and<br>    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.<br><br>    If omitted, the stream type of the existing stream on the branch will be used. |
| compressed | compressed | typing.Optional[Compressed] | None | Whether or not compression is enabled for the stream.<br><br>    If omitted, the compression setting of the existing stream on the branch will be used. |

```python
class ResetStreamRequest(core.ModelBase):
    """ResetStreamRequest"""

    schema_: typing.Optional[core_models.StreamSchema] = pydantic.Field(alias=str("schema"), default=None)  # type: ignore[literal-required]
    """
    The Foundry schema to apply to the new stream. 

    If omitted, the schema of the existing stream on the branch will be used.
    """

    partitions_count: typing.Optional[PartitionsCount] = pydantic.Field(alias=str("partitionsCount"), default=None)  # type: ignore[literal-required]
    """
    The number of partitions for the Foundry stream.
    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.

    If omitted, the partitions count of the existing stream on the branch will be used.
    """

    stream_type: typing.Optional[StreamType] = pydantic.Field(alias=str("streamType"), default=None)  # type: ignore[literal-required]
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.

    If omitted, the stream type of the existing stream on the branch will be used.
    """

    compressed: typing.Optional[Compressed] = None
    """
    Whether or not compression is enabled for the stream.

    If omitted, the compression setting of the existing stream on the branch will be used.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.StreamSchema](../../core/models/StreamSchema.md)
- [foundry_sdk.v2.streams.models.Compressed](Compressed.md)
- [foundry_sdk.v2.streams.models.PartitionsCount](PartitionsCount.md)
- [foundry_sdk.v2.streams.models.StreamType](StreamType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResetStreamRequest.md)
