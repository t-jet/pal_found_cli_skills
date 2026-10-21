# foundry_sdk.v2.ontologies.models.PropertyLoadLevel



The load level of the property:
- APPLY_REDUCERS: Returns a single value of an array as configured in the ontology.
- EXTRACT_MAIN_VALUE: Returns the main value of a struct as configured in the ontology.
- APPLY_REDUCERS_AND_EXTRACT_MAIN_VALUE: Performs both to return the reduced main value.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyLoadLevel: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ApplyReducersAndExtractMainValueLoadLevel",
        "ApplyReducersLoadLevel",
        "ExtractMainValueLoadLevel",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ApplyReducersAndExtractMainValueLoadLevel](ApplyReducersAndExtractMainValueLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.ApplyReducersLoadLevel](ApplyReducersLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.ExtractMainValueLoadLevel](ExtractMainValueLoadLevel.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyLoadLevel.md)
