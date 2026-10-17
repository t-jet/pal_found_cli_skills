# foundry_sdk.v2.core.errors.InvalidFieldSchemaParameters


The field schema failed validations

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| fieldName | fieldName | typing_extensions.NotRequired[core_models.FieldName] | TypedDict key may be omitted | No additional field description in SDK source. |
| message | message | str | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidFieldSchemaParameters(typing_extensions.TypedDict):
    """The field schema failed validations"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fieldName: typing_extensions.NotRequired[core_models.FieldName]
    message: str
```

## Referenced definitions

- [foundry_sdk.v2.core.models.FieldName](../models/FieldName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidFieldSchemaParameters.md)
