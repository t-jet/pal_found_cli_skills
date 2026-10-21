# foundry_sdk.v2.filesystem.errors.InvalidVariableParameters


A variable referenced in the request to create project from template is not defined on the template.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| templateVariableId | templateVariableId | str | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidVariableParameters(typing_extensions.TypedDict):
    """A variable referenced in the request to create project from template is not defined on the template."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    templateVariableId: str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidVariableParameters.md)
