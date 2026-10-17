# foundry_sdk.v2.data_health.errors.CheckAlreadyExistsParameters


A check of the given type for the given subject(s) already exists. The conflicting check will be returned
if the provided token has permission to view it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| conflictingCheck | conflictingCheck | typing_extensions.NotRequired[data_health_models.Check] | TypedDict key may be omitted | No additional field description in SDK source. |

```python
class CheckAlreadyExistsParameters(typing_extensions.TypedDict):
    """
    A check of the given type for the given subject(s) already exists. The conflicting check will be returned
    if the provided token has permission to view it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    conflictingCheck: typing_extensions.NotRequired[data_health_models.Check]
```

## Referenced definitions

- [foundry_sdk.v2.data_health.models.Check](../models/Check.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckAlreadyExistsParameters.md)
