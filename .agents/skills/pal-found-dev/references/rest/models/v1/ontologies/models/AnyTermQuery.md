# foundry_sdk.v1.ontologies.models.AnyTermQuery


Returns objects where the specified field contains any of the whitespace separated words in any
order in the provided value. This query supports fuzzy matching.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | FieldNameV1 | required; no default | No additional field description in SDK source. |
| value | value | str | required; no default | No additional field description in SDK source. |
| fuzzy | fuzzy | typing.Optional[Fuzzy] | None | No additional field description in SDK source. |
| type | type | typing.Literal['anyTerm'] | 'anyTerm' | No additional field description in SDK source. |

```python
class AnyTermQuery(core.ModelBase):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: FieldNameV1
    value: str
    fuzzy: typing.Optional[Fuzzy] = None
    type: typing.Literal["anyTerm"] = "anyTerm"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.FieldNameV1](FieldNameV1.md)
- [foundry_sdk.v1.ontologies.models.Fuzzy](Fuzzy.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnyTermQuery.md)
