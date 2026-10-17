# foundry_sdk.v2.filesystem.models.CreateProjectFromTemplateRequest


CreateProjectFromTemplateRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| template_rid | templateRid | ProjectTemplateRid | required; no default | No additional field description in SDK source. |
| variable_values | variableValues | typing.Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue] | required; no default | No additional field description in SDK source. |
| default_roles | defaultRoles | typing.Optional[typing.List[core_models.RoleId]] | default None | No additional field description in SDK source. |
| organization_rids | organizationRids | typing.Optional[typing.List[core_models.OrganizationRid]] | default None | No additional field description in SDK source. |
| project_description | projectDescription | typing.Optional[str] | default None | No additional field description in SDK source. |

```python
class CreateProjectFromTemplateRequest(core.ModelBase):
    """CreateProjectFromTemplateRequest"""

    template_rid: ProjectTemplateRid = pydantic.Field(alias=str("templateRid"))  # type: ignore[literal-required]
    variable_values: typing.Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue] = pydantic.Field(alias=str("variableValues"))  # type: ignore[literal-required]
    default_roles: typing.Optional[typing.List[core_models.RoleId]] = pydantic.Field(alias=str("defaultRoles"), default=None)  # type: ignore[literal-required]
    organization_rids: typing.Optional[typing.List[core_models.OrganizationRid]] = pydantic.Field(alias=str("organizationRids"), default=None)  # type: ignore[literal-required]
    project_description: typing.Optional[str] = pydantic.Field(alias=str("projectDescription"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.RoleId](../../core/models/RoleId.md)
- [foundry_sdk.v2.filesystem.models.ProjectTemplateRid](ProjectTemplateRid.md)
- [foundry_sdk.v2.filesystem.models.ProjectTemplateVariableId](ProjectTemplateVariableId.md)
- [foundry_sdk.v2.filesystem.models.ProjectTemplateVariableValue](ProjectTemplateVariableValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateProjectFromTemplateRequest.md)
