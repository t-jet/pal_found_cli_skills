# foundry_sdk.v2.ontologies.models.NumberFormatNotation



Number notation style options:
- STANDARD: Regular number display ("1,234")
- SCIENTIFIC: Scientific notation ("1.234E3")
- ENGINEERING: Engineering notation ("1.234E3")
- COMPACT: Compact notation ("1.2K")


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
NumberFormatNotation: typing_extensions.TypeAlias = typing.Literal[
    "STANDARD", "SCIENTIFIC", "ENGINEERING", "COMPACT"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatNotation.md)
