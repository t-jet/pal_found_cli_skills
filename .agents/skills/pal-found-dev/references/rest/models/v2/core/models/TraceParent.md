# foundry_sdk.v2.core.models.TraceParent


The W3C Trace Context `traceparent` header value used to propagate distributed tracing information for Foundry telemetry. See https://www.w3.org/TR/trace-context/#traceparent-header for more details. Note the 16 byte trace ID encoded in the header must be derived from a time based uuid to be used within Foundry.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TraceParent: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TraceParent.md)
