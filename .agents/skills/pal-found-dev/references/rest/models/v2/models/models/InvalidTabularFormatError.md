# foundry_sdk.v2.models.models.InvalidTabularFormatError


Tabular input has incorrect JSON structure.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| input_field_name | inputFieldName | str | required; no default | The name of the tabular input field with incorrect format |
| type | type | typing.Literal['invalidTabularFormat'] | 'invalidTabularFormat' | No additional field description in SDK source. |

```python
class InvalidTabularFormatError(core.ModelBase):
    """Tabular input has incorrect JSON structure."""

    input_field_name: str = pydantic.Field(alias=str("inputFieldName"))  # type: ignore[literal-required]
    """The name of the tabular input field with incorrect format"""

    type: typing.Literal["invalidTabularFormat"] = "invalidTabularFormat"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidTabularFormatError.md)
