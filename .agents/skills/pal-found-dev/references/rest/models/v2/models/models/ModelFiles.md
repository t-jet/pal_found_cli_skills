# foundry_sdk.v2.models.models.ModelFiles



The serialized data of a machine learning model. This can include the model's parameters, architecture, and any other relevant information needed to reconstruct the model.
Must be a base64-encoded string of a dill-serialized model function.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ModelFiles: typing_extensions.TypeAlias = DillModelFiles
```

## Referenced definitions

- [foundry_sdk.v2.models.models.DillModelFiles](DillModelFiles.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelFiles.md)
