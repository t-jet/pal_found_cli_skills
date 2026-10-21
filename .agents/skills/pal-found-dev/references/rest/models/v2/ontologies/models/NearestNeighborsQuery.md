# foundry_sdk.v2.ontologies.models.NearestNeighborsQuery



Queries support either a vector matching the embedding model defined on the property, or text that is 
automatically embedded.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
NearestNeighborsQuery: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["DoubleVector", "NearestNeighborsQueryText"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.DoubleVector](DoubleVector.md)
- [foundry_sdk.v2.ontologies.models.NearestNeighborsQueryText](NearestNeighborsQueryText.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NearestNeighborsQuery.md)
