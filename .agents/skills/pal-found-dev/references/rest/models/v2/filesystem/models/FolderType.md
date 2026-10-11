# foundry_sdk.v2.filesystem.models.FolderType


The folder type distinguishes an ordinary folder, Project and Space. Read the literal values below and use the matching resource operation when traversing the hierarchy. Project and Space also carry access context that an ordinary folder path does not convey.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
FolderType: typing_extensions.TypeAlias = typing.Literal["FOLDER", "SPACE", "PROJECT"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FolderType.md)
