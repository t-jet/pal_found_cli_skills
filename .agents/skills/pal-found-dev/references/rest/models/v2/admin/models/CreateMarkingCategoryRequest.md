# foundry_sdk.v2.admin.models.CreateMarkingCategoryRequest


CreateMarkingCategoryRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| initial_permissions | initialPermissions | MarkingCategoryPermissions | required; no default | The initial permissions for the Marking Category. This can be changed later through MarkingCategoryPermission operations.<br>    The provided permissions must include at least one ADMINISTER role assignment.<br><br>    WARNING: If you do not list your own principal ID or the ID of a Group that you are a member of as an<br>    ADMINISTER, you will create a Marking Category that you cannot administer. |
| name | name | MarkingCategoryName | required; no default | No additional field description in SDK source. |
| description | description | MarkingCategoryDescription | required; no default | No additional field description in SDK source. |

```python
class CreateMarkingCategoryRequest(core.ModelBase):
    """CreateMarkingCategoryRequest"""

    initial_permissions: MarkingCategoryPermissions = pydantic.Field(alias=str("initialPermissions"))  # type: ignore[literal-required]
    """
    The initial permissions for the Marking Category. This can be changed later through MarkingCategoryPermission operations.
    The provided permissions must include at least one ADMINISTER role assignment.

    WARNING: If you do not list your own principal ID or the ID of a Group that you are a member of as an
    ADMINISTER, you will create a Marking Category that you cannot administer.
    """

    name: MarkingCategoryName
    description: MarkingCategoryDescription
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryDescription](MarkingCategoryDescription.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryName](MarkingCategoryName.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryPermissions](MarkingCategoryPermissions.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateMarkingCategoryRequest.md)
