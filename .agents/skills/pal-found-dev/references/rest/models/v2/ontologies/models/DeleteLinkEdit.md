# foundry_sdk.v2.ontologies.models.DeleteLinkEdit


DeleteLinkEdit

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_type | objectType | ObjectTypeApiName | required; no default | No additional field description in SDK source. |
| primary_key | primaryKey | PrimaryKeyValue | required; no default | No additional field description in SDK source. |
| link_type | linkType | LinkTypeApiName | required; no default | No additional field description in SDK source. |
| linked_object_primary_key | linkedObjectPrimaryKey | PrimaryKeyValue | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['removeLink'] | 'removeLink' | No additional field description in SDK source. |

```python
class DeleteLinkEdit(core.ModelBase):
    """DeleteLinkEdit"""

    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: PrimaryKeyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    link_type: LinkTypeApiName = pydantic.Field(alias=str("linkType"))  # type: ignore[literal-required]
    linked_object_primary_key: PrimaryKeyValue = pydantic.Field(alias=str("linkedObjectPrimaryKey"))  # type: ignore[literal-required]
    type: typing.Literal["removeLink"] = "removeLink"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.PrimaryKeyValue](PrimaryKeyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DeleteLinkEdit.md)
