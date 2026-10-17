# foundry_sdk.v1.core.errors.InvalidParameterCombinationParameters


The given parameters are individually valid but cannot be used in the given combination.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| validCombinations | validCombinations | typing.List[typing.List[str]] | TypedDict key required | No additional field description in SDK source. |
| providedParameters | providedParameters | typing.List[str] | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidParameterCombinationParameters(typing_extensions.TypedDict):
    """The given parameters are individually valid but cannot be used in the given combination."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    validCombinations: typing.List[typing.List[str]]
    providedParameters: typing.List[str]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidParameterCombinationParameters.md)
