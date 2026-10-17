# foundry_sdk.v2.core.models.ChangeDataCaptureConfiguration


Change data capture uses the stream as a keyed update feed. Supply at least one key field in its stream schema, then choose the CDC configuration that matches the incoming change records. A key groups updates to the same entity; a key alone does not deduplicate records.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ChangeDataCaptureConfiguration: typing_extensions.TypeAlias = FullRowChangeDataCaptureConfiguration
```

## Referenced definitions

- [foundry_sdk.v2.core.models.FullRowChangeDataCaptureConfiguration](FullRowChangeDataCaptureConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ChangeDataCaptureConfiguration.md)
