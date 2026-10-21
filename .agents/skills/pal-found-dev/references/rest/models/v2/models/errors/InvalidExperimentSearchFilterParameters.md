# foundry_sdk.v2.models.errors.InvalidExperimentSearchFilterParameters


The search filter is invalid. This can occur when using an unsupported operator and value type
combination in a parameter filter, filtering by an unsupported status, or providing a malformed filter.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| reason | reason | str | TypedDict key required | A human-readable description of why the filter is invalid. |

```python
class InvalidExperimentSearchFilterParameters(typing_extensions.TypedDict):
    """
    The search filter is invalid. This can occur when using an unsupported operator and value type
    combination in a parameter filter, filtering by an unsupported status, or providing a malformed filter.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    """A human-readable description of why the filter is invalid."""
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidExperimentSearchFilterParameters.md)
