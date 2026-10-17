# foundry_sdk.v2.admin.errors.AttributesNotEditableParameters


One or more attributes are not editable. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are not editable.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| attributeNames | attributeNames | typing.List[str] | TypedDict key required | No additional field description in SDK source. |

```python
class AttributesNotEditableParameters(typing_extensions.TypedDict):
    """One or more attributes are not editable. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are not editable."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    attributeNames: typing.List[str]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AttributesNotEditableParameters.md)
