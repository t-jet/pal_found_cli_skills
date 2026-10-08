# foundry_sdk.v2.filesystem.models.FolderType



A folder can be a regular Folder, a
[Project](https://palantir.com/docs/foundry/getting-started/projects-and-resources/#projects) or a
[Space](https://palantir.com/docs/foundry/security/orgs-and-spaces/#spaces).


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
FolderType: typing_extensions.TypeAlias = typing.Literal["FOLDER", "SPACE", "PROJECT"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FolderType.md)
