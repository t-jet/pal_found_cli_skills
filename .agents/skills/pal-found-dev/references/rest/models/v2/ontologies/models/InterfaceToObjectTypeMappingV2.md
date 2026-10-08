# foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMappingV2


Represents an implementation of an interface (the mapping of interface property to how it is implemented.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfaceToObjectTypeMappingV2: typing_extensions.TypeAlias = typing.Dict[
    "InterfacePropertyApiName", "InterfacePropertyTypeImplementation"
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyTypeImplementation](InterfacePropertyTypeImplementation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceToObjectTypeMappingV2.md)
