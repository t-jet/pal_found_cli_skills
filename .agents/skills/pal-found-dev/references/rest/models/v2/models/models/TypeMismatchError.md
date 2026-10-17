# foundry_sdk.v2.models.models.TypeMismatchError


Input type does not match expected type in model API.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| expected_type | expectedType | str | required; no default | The expected type from the model API specification |
| actual_type | actualType | str | required; no default | The actual type provided in the input |
| type | type | typing.Literal['typeMismatch'] | 'typeMismatch' | No additional field description in SDK source. |

```python
class TypeMismatchError(core.ModelBase):
    """Input type does not match expected type in model API."""

    expected_type: str = pydantic.Field(alias=str("expectedType"))  # type: ignore[literal-required]
    """The expected type from the model API specification"""

    actual_type: str = pydantic.Field(alias=str("actualType"))  # type: ignore[literal-required]
    """The actual type provided in the input"""

    type: typing.Literal["typeMismatch"] = "typeMismatch"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TypeMismatchError.md)
