# foundry_sdk.v2.ontologies.models.NumberRatioType



Ratio format options for displaying proportional values:
- PERCENTAGE: Multiply by 100 and add "%" suffix
- PER_MILLE: Multiply by 1000 and add "‰" suffix
- BASIS_POINTS: Multiply by 10000 and add "bps" suffix


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
NumberRatioType: typing_extensions.TypeAlias = typing.Literal[
    "PERCENTAGE", "PER_MILLE", "BASIS_POINTS"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberRatioType.md)
