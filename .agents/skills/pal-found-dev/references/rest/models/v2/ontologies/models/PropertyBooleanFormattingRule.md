# foundry_sdk.v2.ontologies.models.PropertyBooleanFormattingRule


Formatting configuration for boolean property values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| value_if_true | valueIfTrue | str | required; no default | Value to display if this boolean is true |
| value_if_false | valueIfFalse | str | required; no default | Value to display if this boolean is false |
| type | type | typing.Literal['boolean'] | 'boolean' | No additional field description in SDK source. |

```python
class PropertyBooleanFormattingRule(core.ModelBase):
    """Formatting configuration for boolean property values."""

    value_if_true: str = pydantic.Field(alias=str("valueIfTrue"))  # type: ignore[literal-required]
    """Value to display if this boolean is true"""

    value_if_false: str = pydantic.Field(alias=str("valueIfFalse"))  # type: ignore[literal-required]
    """Value to display if this boolean is false"""

    type: typing.Literal["boolean"] = "boolean"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyBooleanFormattingRule.md)
