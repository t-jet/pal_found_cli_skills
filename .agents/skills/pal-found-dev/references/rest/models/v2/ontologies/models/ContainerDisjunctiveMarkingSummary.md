# foundry_sdk.v2.ontologies.models.ContainerDisjunctiveMarkingSummary



The disjunctive set of markings for the container of this property value,
such as the project of a dataset. These markings may differ from the marking
on the actual property value, but still must be satisfied for accessing the property        
All markings from a conjunctive set must be met for access.

Disjunctive markings are represented as a conjunctive list of disjunctive sets.
The top-level set is a conjunction of sets, where each inner set should be 
treated as a unit where any marking within the set can satisfy the set.
All sets within the top level set should be satisfied.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ContainerDisjunctiveMarkingSummary: typing_extensions.TypeAlias = typing.List[
    typing.List["MarkingId"]
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.MarkingId](MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ContainerDisjunctiveMarkingSummary.md)
