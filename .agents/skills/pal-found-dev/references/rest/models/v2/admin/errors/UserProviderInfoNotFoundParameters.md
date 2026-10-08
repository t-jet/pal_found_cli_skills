# foundry_sdk.v2.admin.errors.UserProviderInfoNotFoundParameters


The given UserProviderInfo could not be found.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| userId | userId | core_models.UserId | TypedDict key required | No additional field description in SDK source. |

```python
class UserProviderInfoNotFoundParameters(typing_extensions.TypedDict):
    """The given UserProviderInfo could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.UserId
```

## Referenced definitions

- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UserProviderInfoNotFoundParameters.md)
