# foundry_sdk.v2.ontologies.models.FullTextStringContainsPredicate


Matches strings which contain the given string or parts of the given string. The exact behaviour can vary
depending on the attribute searched for due to optimized text analysis.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| value | value | str | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['contains'] | 'contains' | No additional field description in SDK source. |

```python
class FullTextStringContainsPredicate(core.ModelBase):
    """
    Matches strings which contain the given string or parts of the given string. The exact behaviour can vary
    depending on the attribute searched for due to optimized text analysis.
    """

    value: str
    type: typing.Literal["contains"] = "contains"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FullTextStringContainsPredicate.md)
