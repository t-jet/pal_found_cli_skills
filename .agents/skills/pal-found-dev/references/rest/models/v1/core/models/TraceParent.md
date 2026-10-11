# foundry_sdk.v1.core.models.TraceParent


W3C `traceparent` is a string header for correlating Foundry telemetry across requests. Its trace ID is 16 bytes encoded as 32 hexadecimal characters and, for Foundry, must come from a time-based UUID. Preserve the same trace ID across related requests.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TraceParent: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TraceParent.md)
