# foundry_sdk.v2.data_health.models.TrendType



The type of trend to validate:
- NON_INCREASING: Values should not increase over time
- NON_DECREASING: Values should not decrease over time
- STRICTLY_INCREASING: Values should strictly increase over time
- STRICTLY_DECREASING: Values should strictly decrease over time
- CONSTANT: Values should remain constant over time


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TrendType: typing_extensions.TypeAlias = typing.Literal[
    "NON_INCREASING", "NON_DECREASING", "STRICTLY_INCREASING", "STRICTLY_DECREASING", "CONSTANT"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TrendType.md)
