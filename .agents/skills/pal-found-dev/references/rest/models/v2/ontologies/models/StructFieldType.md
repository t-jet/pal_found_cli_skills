# foundry_sdk.v2.ontologies.models.StructFieldType


StructFieldType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | StructFieldApiName | required; no default | No additional field description in SDK source. |
| rid | rid | StructFieldTypeRid | required; no default | No additional field description in SDK source. |
| data_type | dataType | ObjectPropertyType | required; no default | No additional field description in SDK source. |
| type_classes | typeClasses | typing.Optional[typing.List[TypeClass]] | default None | No additional field description in SDK source. |

```python
class StructFieldType(core.ModelBase):
    """StructFieldType"""

    api_name: StructFieldApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    rid: StructFieldTypeRid
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    type_classes: typing.Optional[typing.List[TypeClass]] = pydantic.Field(alias=str("typeClasses"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldTypeRid](StructFieldTypeRid.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](TypeClass.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StructFieldType.md)
