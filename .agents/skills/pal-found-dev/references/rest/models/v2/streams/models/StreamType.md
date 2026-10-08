# foundry_sdk.v2.streams.models.StreamType



LOW_LATENCY: The default stream type. Recommended for most use cases.

HIGH_THROUGHPUT: Best for streams that send large amounts of data every second. Using this stream type might
introduce some non-zero latency at the expense of a higher throughput. This stream type is only
recommended if you inspect your stream metrics in-platform and observe that the average batch size is equal
to the max match size, or if jobs using the stream are failing due to Kafka producer batches expiring. For
additional information on inspecting stream metrics, refer to the 
[stream monitoring](https://palantir.com/docs/foundry/data-integration/stream-monitoring/#viewing-metrics) documentation.

For more information, refer to the [stream types](https://palantir.com/docs/foundry/data-integration/streams/#stream-types)
documentation.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
StreamType: typing_extensions.TypeAlias = typing.Literal["LOW_LATENCY", "HIGH_THROUGHPUT"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StreamType.md)
