# foundry_sdk.v2.streams.models.StreamType


`LOW_LATENCY` is the default and suits most streams. `HIGH_THROUGHPUT` can add latency. Choose it only when in-platform metrics show average batch size equals the SDK's stated max match size, or jobs fail because Kafka producer batches expire.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
StreamType: typing_extensions.TypeAlias = typing.Literal["LOW_LATENCY", "HIGH_THROUGHPUT"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StreamType.md)
