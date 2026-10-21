# foundry_sdk.v2.ontologies.models.ParameterNameActionTypesQueryV2


Returns action types with a parameter whose name matches the given string predicate.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| value | value | FullTextStringPredicateV2 | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['parameterName'] | 'parameterName' | No additional field description in SDK source. |

```python
class ParameterNameActionTypesQueryV2(core.ModelBase):
    """Returns action types with a parameter whose name matches the given string predicate."""

    value: FullTextStringPredicateV2
    type: typing.Literal["parameterName"] = "parameterName"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.FullTextStringPredicateV2](FullTextStringPredicateV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterNameActionTypesQueryV2.md)
