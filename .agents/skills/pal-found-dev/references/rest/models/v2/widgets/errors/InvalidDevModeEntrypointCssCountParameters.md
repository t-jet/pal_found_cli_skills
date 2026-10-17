# foundry_sdk.v2.widgets.errors.InvalidDevModeEntrypointCssCountParameters


The dev mode settings contains too many CSS entrypoints. You must limit the number
of CSS entrypoints to the maximum allowed.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| reason | reason | str | TypedDict key required | No additional field description in SDK source. |
| entrypointCssCount | entrypointCssCount | int | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidDevModeEntrypointCssCountParameters(typing_extensions.TypedDict):
    """
    The dev mode settings contains too many CSS entrypoints. You must limit the number
    of CSS entrypoints to the maximum allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    entrypointCssCount: int
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidDevModeEntrypointCssCountParameters.md)
