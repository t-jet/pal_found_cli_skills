# foundry_sdk.v2.ontologies.models.ConjunctiveMarkingSummary



The conjunctive set of markings required to access the property value. 
All markings from a conjunctive set must be met for access.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ConjunctiveMarkingSummary: typing_extensions.TypeAlias = typing.List["MarkingId"]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.MarkingId](MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ConjunctiveMarkingSummary.md)
