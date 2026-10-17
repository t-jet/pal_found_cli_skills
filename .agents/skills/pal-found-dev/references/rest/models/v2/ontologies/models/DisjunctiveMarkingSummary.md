# foundry_sdk.v2.ontologies.models.DisjunctiveMarkingSummary



The disjunctive set of markings required to access the property value.
Disjunctive markings are represented as a conjunctive list of disjunctive sets.
The top-level set is a conjunction of sets, where each inner set should be 
treated as a unit where any marking within the set can satisfy the set.
All sets within the top level set should be satisfied.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DisjunctiveMarkingSummary: typing_extensions.TypeAlias = typing.List[typing.List["MarkingId"]]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.MarkingId](MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DisjunctiveMarkingSummary.md)
