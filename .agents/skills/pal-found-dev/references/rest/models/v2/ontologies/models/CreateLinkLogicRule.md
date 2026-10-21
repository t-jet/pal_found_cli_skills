# foundry_sdk.v2.ontologies.models.CreateLinkLogicRule


CreateLinkLogicRule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| link_type_api_name | linkTypeApiName | LinkTypeApiName | required; no default | No additional field description in SDK source. |
| source_object | sourceObject | ParameterId | required; no default | No additional field description in SDK source. |
| target_object | targetObject | ParameterId | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['createLink'] | 'createLink' | No additional field description in SDK source. |

```python
class CreateLinkLogicRule(core.ModelBase):
    """CreateLinkLogicRule"""

    link_type_api_name: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiName"))  # type: ignore[literal-required]
    source_object: ParameterId = pydantic.Field(alias=str("sourceObject"))  # type: ignore[literal-required]
    target_object: ParameterId = pydantic.Field(alias=str("targetObject"))  # type: ignore[literal-required]
    type: typing.Literal["createLink"] = "createLink"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](ParameterId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateLinkLogicRule.md)
