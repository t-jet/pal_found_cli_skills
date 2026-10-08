# foundry_sdk.v2.ontologies.models.NumberScaleType



Scale factor options for large numbers:
- THOUSANDS: Divide by 1,000 and add "K" suffix
- MILLIONS: Divide by 1,000,000 and add "M" suffix
- BILLIONS: Divide by 1,000,000,000 and add "B" suffix


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
NumberScaleType: typing_extensions.TypeAlias = typing.Literal["THOUSANDS", "MILLIONS", "BILLIONS"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberScaleType.md)
