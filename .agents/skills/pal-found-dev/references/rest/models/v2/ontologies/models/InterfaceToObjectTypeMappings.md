# foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMappings


Map from object type to the interface-to-object-type mapping for that object type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfaceToObjectTypeMappings: typing_extensions.TypeAlias = typing.Dict[
    "ObjectTypeApiName", "InterfaceToObjectTypeMapping"
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMapping](InterfaceToObjectTypeMapping.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceToObjectTypeMappings.md)
