# foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName


The API name of an Ontology interface link type. Obtain it from the permitted Ontology interface metadata for the target enrollment, and use that exact API name in link requests. A display label is not a reliable substitute.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InterfaceLinkTypeApiName: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceLinkTypeApiName.md)
