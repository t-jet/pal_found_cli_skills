# foundry_sdk.v2.core.models.TraceState


W3C `tracestate` is a string header carrying vendor-specific tracing state alongside `traceparent`. Pass through the state supplied by the active tracing context; this SDK alias does not construct or validate vendor entries.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TraceState: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TraceState.md)
