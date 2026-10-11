# foundry_sdk._core.api_client.ResponseMode


An SDK transport response mode. `DECODED` returns the operation's ordinary typed result; `ITERATOR` traverses paged results; `RAW` exposes status and explicit decoding; `STREAMING` keeps the response open in a context manager. The table and SSE values are specialized operation formats. Choose through the public response wrapper supported by the operation, rather than passing `_sdk_internal` as application input.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ResponseMode = Literal[
    "DECODED", "ITERATOR", "RAW", "STREAMING", "ARROW_TABLE", "PARQUET_TABLE", "SSE"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](ResponseMode.md)
