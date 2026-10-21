# foundry_sdk.v2.data_health.models.PercentageValue



A percentage value in the range 0.0 to 100.0.

Validation rules:
 * must be greater than or equal to 0.0
 * must be less than or equal to 100.0


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PercentageValue: typing_extensions.TypeAlias = float
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PercentageValue.md)
