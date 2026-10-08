# foundry_sdk.v2.ontologies.models.InterfacePropertyStructImplementationMapping



An implementation of a struct interface property via a local struct property. Specifies a mapping of interface
struct fields to local struct fields or properties.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfacePropertyStructImplementationMapping: typing_extensions.TypeAlias = typing.Dict[
    "StructFieldApiName", "PropertyOrStructFieldOfPropertyImplementation"
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.PropertyOrStructFieldOfPropertyImplementation](PropertyOrStructFieldOfPropertyImplementation.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](StructFieldApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfacePropertyStructImplementationMapping.md)
