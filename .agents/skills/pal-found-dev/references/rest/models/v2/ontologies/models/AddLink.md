# foundry_sdk.v2.ontologies.models.AddLink


AddLink

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| link_type_api_name_ato_b | linkTypeApiNameAtoB | LinkTypeApiName | required; no default | No additional field description in SDK source. |
| link_type_api_name_bto_a | linkTypeApiNameBtoA | LinkTypeApiName | required; no default | No additional field description in SDK source. |
| a_side_object | aSideObject | LinkSideObject | required; no default | No additional field description in SDK source. |
| b_side_object | bSideObject | LinkSideObject | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['addLink'] | 'addLink' | No additional field description in SDK source. |

```python
class AddLink(core.ModelBase):
    """AddLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["addLink"] = "addLink"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.LinkSideObject](LinkSideObject.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AddLink.md)
