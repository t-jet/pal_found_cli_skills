# foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectType


OntologyInterfaceObjectType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| interface_type_api_name | interfaceTypeApiName | typing.Optional[InterfaceTypeApiName] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['interfaceObject'] | 'interfaceObject' | No additional field description in SDK source. |

```python
class OntologyInterfaceObjectType(core.ModelBase):
    """OntologyInterfaceObjectType"""

    interface_type_api_name: typing.Optional[InterfaceTypeApiName] = pydantic.Field(alias=str("interfaceTypeApiName"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["interfaceObject"] = "interfaceObject"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyInterfaceObjectType.md)
