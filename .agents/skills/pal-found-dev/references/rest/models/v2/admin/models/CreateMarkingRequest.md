# foundry_sdk.v2.admin.models.CreateMarkingRequest


CreateMarkingRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| initial_role_assignments | initialRoleAssignments | typing.List[MarkingRoleUpdate] | required; no default | The initial roles that will be assigned when the Marking is created. At least one ADMINISTER role must be<br>    provided. This can be changed later through the MarkingRoleAssignment operations.<br><br>    WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of,<br>    you will create a Marking that you cannot administer. |
| initial_members | initialMembers | typing.List[core_models.PrincipalId] | required; no default | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations. |
| name | name | MarkingName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| category_id | categoryId | MarkingCategoryId | required; no default | No additional field description in SDK source. |

```python
class CreateMarkingRequest(core.ModelBase):
    """CreateMarkingRequest"""

    initial_role_assignments: typing.List[MarkingRoleUpdate] = pydantic.Field(alias=str("initialRoleAssignments"))  # type: ignore[literal-required]
    """
    The initial roles that will be assigned when the Marking is created. At least one ADMINISTER role must be
    provided. This can be changed later through the MarkingRoleAssignment operations.

    WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of,
    you will create a Marking that you cannot administer.
    """

    initial_members: typing.List[core_models.PrincipalId] = pydantic.Field(alias=str("initialMembers"))  # type: ignore[literal-required]
    """Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations."""

    name: MarkingName
    description: typing.Optional[str] = None
    category_id: MarkingCategoryId = pydantic.Field(alias=str("categoryId"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingName](MarkingName.md)
- [foundry_sdk.v2.admin.models.MarkingRoleUpdate](MarkingRoleUpdate.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../core/models/PrincipalId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateMarkingRequest.md)
