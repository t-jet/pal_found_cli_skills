# foundry_sdk.v2.core.models.IncludeComputeUsage



Indicates whether the response should include compute usage details for the request. This feature is currently
only available for OSDK applications.
Note: Enabling this flag may slow down query performance and is not recommended for use in production.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
IncludeComputeUsage: typing_extensions.TypeAlias = bool
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](IncludeComputeUsage.md)
