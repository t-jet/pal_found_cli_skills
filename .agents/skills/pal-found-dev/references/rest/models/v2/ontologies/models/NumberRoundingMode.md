# foundry_sdk.v2.ontologies.models.NumberRoundingMode



Number rounding behavior:
- CEIL: Always round up (3.1 becomes 4)
- FLOOR: Always round down (3.9 becomes 3)
- ROUND_CLOSEST: Round to nearest (3.4 becomes 3, 3.6 becomes 4)


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
NumberRoundingMode: typing_extensions.TypeAlias = typing.Literal["CEIL", "FLOOR", "ROUND_CLOSEST"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberRoundingMode.md)
