# foundry_sdk.v2.ontologies.models.PreciseTimeUnit


The unit of a fixed-width duration. Each day is 24 hours and each week is 7 days.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PreciseTimeUnit: typing_extensions.TypeAlias = typing.Literal[
    "NANOSECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PreciseTimeUnit.md)
