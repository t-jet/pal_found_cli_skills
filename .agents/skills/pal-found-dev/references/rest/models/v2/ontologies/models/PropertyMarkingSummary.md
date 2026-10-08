# foundry_sdk.v2.ontologies.models.PropertyMarkingSummary


All marking requirements applicable to a property value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| conjunctive | conjunctive | typing.Optional[ConjunctiveMarkingSummary] | None | No additional field description in SDK source. |
| disjunctive | disjunctive | typing.Optional[DisjunctiveMarkingSummary] | None | No additional field description in SDK source. |
| container_conjunctive | containerConjunctive | typing.Optional[ContainerConjunctiveMarkingSummary] | default None | No additional field description in SDK source. |
| container_disjunctive | containerDisjunctive | typing.Optional[ContainerDisjunctiveMarkingSummary] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['propertyMarkingSummary'] | 'propertyMarkingSummary' | No additional field description in SDK source. |

```python
class PropertyMarkingSummary(core.ModelBase):
    """All marking requirements applicable to a property value."""

    conjunctive: typing.Optional[ConjunctiveMarkingSummary] = None
    disjunctive: typing.Optional[DisjunctiveMarkingSummary] = None
    container_conjunctive: typing.Optional[ContainerConjunctiveMarkingSummary] = pydantic.Field(alias=str("containerConjunctive"), default=None)  # type: ignore[literal-required]
    container_disjunctive: typing.Optional[ContainerDisjunctiveMarkingSummary] = pydantic.Field(alias=str("containerDisjunctive"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["propertyMarkingSummary"] = "propertyMarkingSummary"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ConjunctiveMarkingSummary](ConjunctiveMarkingSummary.md)
- [foundry_sdk.v2.ontologies.models.ContainerConjunctiveMarkingSummary](ContainerConjunctiveMarkingSummary.md)
- [foundry_sdk.v2.ontologies.models.ContainerDisjunctiveMarkingSummary](ContainerDisjunctiveMarkingSummary.md)
- [foundry_sdk.v2.ontologies.models.DisjunctiveMarkingSummary](DisjunctiveMarkingSummary.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyMarkingSummary.md)
