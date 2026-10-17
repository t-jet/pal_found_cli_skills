# foundry_sdk.v2.streams.models.ReadPosition



Position to start reading from when registering a subscriber or resetting offsets.

- `earliest`: Start reading from the beginning of each partition (offset 0). Use this to
  reprocess all historical data in the stream.
- `latest`: Start reading from the current end of each partition. Use this to skip
  historical data and only process new records arriving after registration.
- `specific`: Start reading from explicit offsets for each partition. Use this for precise
  replay scenarios or to resume from a known checkpoint.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ReadPosition: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SpecificPosition", "EarliestPosition", "LatestPosition"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.streams.models.EarliestPosition](EarliestPosition.md)
- [foundry_sdk.v2.streams.models.LatestPosition](LatestPosition.md)
- [foundry_sdk.v2.streams.models.SpecificPosition](SpecificPosition.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReadPosition.md)
