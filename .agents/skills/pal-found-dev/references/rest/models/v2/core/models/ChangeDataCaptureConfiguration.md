# foundry_sdk.v2.core.models.ChangeDataCaptureConfiguration



Configuration for utilizing the stream as a change data capture (CDC) dataset. To configure CDC on a stream, at
least one key needs to be provided.

For more information on CDC in
Foundry, see the [Change Data Capture](https://palantir.com/docs/foundry/data-integration/change-data-capture/) user documentation.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ChangeDataCaptureConfiguration: typing_extensions.TypeAlias = FullRowChangeDataCaptureConfiguration
```

## Referenced definitions

- [foundry_sdk.v2.core.models.FullRowChangeDataCaptureConfiguration](FullRowChangeDataCaptureConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ChangeDataCaptureConfiguration.md)
