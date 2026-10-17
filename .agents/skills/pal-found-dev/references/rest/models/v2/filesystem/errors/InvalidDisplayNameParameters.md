# foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters


The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be
less than or equal to 700 characters.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| displayName | displayName | filesystem_models.ResourceDisplayName | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidDisplayNameParameters(typing_extensions.TypedDict):
    """
    The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be
    less than or equal to 700 characters.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: filesystem_models.ResourceDisplayName
```

## Referenced definitions

- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../models/ResourceDisplayName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidDisplayNameParameters.md)
