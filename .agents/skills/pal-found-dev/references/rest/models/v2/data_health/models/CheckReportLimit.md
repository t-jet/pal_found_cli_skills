# foundry_sdk.v2.data_health.models.CheckReportLimit



The maximum number of check reports to return in a single request.


Validation rules:
 * must be greater than or equal to 1
 * must be less than or equal to 100


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CheckReportLimit: typing_extensions.TypeAlias = int
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckReportLimit.md)
