# foundry_sdk.v2.language_models.errors.MultipleToolResultContentsNotSupportedParameters


Multiple tool result contents are not currently supported, but will be in the future.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| toolResultContentsSize | toolResultContentsSize | int | TypedDict key required | No additional field description in SDK source. |

```python
class MultipleToolResultContentsNotSupportedParameters(typing_extensions.TypedDict):
    """Multiple tool result contents are not currently supported, but will be in the future."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    toolResultContentsSize: int
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MultipleToolResultContentsNotSupportedParameters.md)
