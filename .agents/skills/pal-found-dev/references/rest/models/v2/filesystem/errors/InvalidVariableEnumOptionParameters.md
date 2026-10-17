# foundry_sdk.v2.filesystem.errors.InvalidVariableEnumOptionParameters


The value passed in the request to create project from template for an enum type variable is not a valid option.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| variableId | variableId | str | TypedDict key required | No additional field description in SDK source. |
| invalidOption | invalidOption | str | TypedDict key required | No additional field description in SDK source. |
| validOptions | validOptions | typing.List[str] | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidVariableEnumOptionParameters(typing_extensions.TypedDict):
    """The value passed in the request to create project from template for an enum type variable is not a valid option."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    variableId: str
    invalidOption: str
    validOptions: typing.List[str]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidVariableEnumOptionParameters.md)
