# foundry_sdk.v2.filesystem.models.TrashStatus



Values:
  - **DIRECTLY_TRASHED**: The resource was specifically trashed by a user. It can be restored directly.
  - **ANCESTOR_TRASHED**: A folder that contains this resource was trashed by a user. Restoring this resource requires restoring the original folder.
  - **NOT_TRASHED**: The default status of resources.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TrashStatus: typing_extensions.TypeAlias = typing.Literal[
    "DIRECTLY_TRASHED", "ANCESTOR_TRASHED", "NOT_TRASHED"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TrashStatus.md)
