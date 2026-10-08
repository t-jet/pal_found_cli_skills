# foundry_sdk.v2.filesystem.errors.ReplaceProjectPermissionDeniedParameters


Could not replace the Project.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| projectRid | projectRid | filesystem_models.ProjectRid | TypedDict key required | No additional field description in SDK source. |

```python
class ReplaceProjectPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the Project."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    projectRid: filesystem_models.ProjectRid
```

## Referenced definitions

- [foundry_sdk.v2.filesystem.models.ProjectRid](../models/ProjectRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceProjectPermissionDeniedParameters.md)
