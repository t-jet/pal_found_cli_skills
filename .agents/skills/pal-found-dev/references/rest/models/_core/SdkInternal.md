# foundry_sdk._core.api_client.SdkInternal


The definition below supplies its fields or permitted values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## TypedDict keys

Nullable values and omitted keys are distinct.

| Key | Type | Presence |
| --- | --- | --- |
| response_mode | NotRequired[ResponseMode] | may be omitted |

```python
SdkInternal = TypedDict("SdkInternal", {"response_mode": NotRequired[ResponseMode]})
```

## Referenced definitions

- [foundry_sdk._core.api_client.ResponseMode](ResponseMode.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](SdkInternal.md)
