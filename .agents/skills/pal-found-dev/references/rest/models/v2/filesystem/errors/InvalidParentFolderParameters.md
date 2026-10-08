# foundry_sdk.v2.filesystem.errors.InvalidParentFolderParameters


The specified parent folder is not a valid destination for the resource. For example, a project cannot be moved under a regular folder, a folder cannot be moved to a Space, etc.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parentFolderRid | parentFolderRid | filesystem_models.FolderRid | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidParentFolderParameters(typing_extensions.TypedDict):
    """The specified parent folder is not a valid destination for the resource. For example, a project cannot be moved under a regular folder, a folder cannot be moved to a Space, etc."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: filesystem_models.FolderRid
```

## Referenced definitions

- [foundry_sdk.v2.filesystem.models.FolderRid](../models/FolderRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidParentFolderParameters.md)
