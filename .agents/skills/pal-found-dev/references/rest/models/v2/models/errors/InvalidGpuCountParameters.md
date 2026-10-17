# foundry_sdk.v2.models.errors.InvalidGpuCountParameters


The GPU count is invalid. The GPU count must be between 1 and the maximum allowed
for the requested GPU type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| providedGpuCount | providedGpuCount | int | TypedDict key required | The GPU count that was provided in the request. |
| maxGpuCount | maxGpuCount | int | TypedDict key required | The maximum allowed GPU count for the requested GPU type. |

```python
class InvalidGpuCountParameters(typing_extensions.TypedDict):
    """
    The GPU count is invalid. The GPU count must be between 1 and the maximum allowed
    for the requested GPU type.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    providedGpuCount: int
    """The GPU count that was provided in the request."""

    maxGpuCount: int
    """The maximum allowed GPU count for the requested GPU type."""
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidGpuCountParameters.md)
