# foundry_sdk.v2.ontologies.models.OntologyObjectSetType


OntologyObjectSetType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_api_name | objectApiName | typing.Optional[ObjectTypeApiName] | default None | No additional field description in SDK source. |
| object_type_api_name | objectTypeApiName | typing.Optional[ObjectTypeApiName] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['objectSet'] | 'objectSet' | No additional field description in SDK source. |

```python
class OntologyObjectSetType(core.ModelBase):
    """OntologyObjectSetType"""

    object_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectApiName"), default=None)  # type: ignore[literal-required]
    object_type_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypeApiName"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["objectSet"] = "objectSet"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyObjectSetType.md)
