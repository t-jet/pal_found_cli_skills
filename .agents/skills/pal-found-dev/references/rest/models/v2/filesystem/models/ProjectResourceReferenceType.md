# foundry_sdk.v2.filesystem.models.ProjectResourceReferenceType



A type of resource that has been referenced. A FILESYSTEM resource is anything that you can find in a Foundry
file tree within a project. An EXTERNAL resource exists outside of the Foundry filesystem, such as a spark
profile or an LLM model.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ProjectResourceReferenceType: typing_extensions.TypeAlias = typing.Literal["EXTERNAL", "FILESYSTEM"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ProjectResourceReferenceType.md)
