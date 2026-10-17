# foundry_sdk.v2.ontologies.models.NumberFormatAffix


Attach arbitrary text before and/or after the formatted number.
Example: prefix "USD " and postfix " total" displays as "USD 1,234.56 total"

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| base_format_options | baseFormatOptions | NumberFormatOptions | required; no default | No additional field description in SDK source. |
| affix | affix | Affix | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['affix'] | 'affix' | No additional field description in SDK source. |

```python
class NumberFormatAffix(core.ModelBase):
    """
    Attach arbitrary text before and/or after the formatted number.
    Example: prefix "USD " and postfix " total" displays as "USD 1,234.56 total"
    """

    base_format_options: NumberFormatOptions = pydantic.Field(alias=str("baseFormatOptions"))  # type: ignore[literal-required]
    affix: Affix
    type: typing.Literal["affix"] = "affix"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.Affix](Affix.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](NumberFormatOptions.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatAffix.md)
