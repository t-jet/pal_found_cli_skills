# foundry_sdk.v2.admin.models.Marking


Marking

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | core_models.MarkingId | required; no default | No additional field description in SDK source. |
| category_id | categoryId | MarkingCategoryId | required; no default | No additional field description in SDK source. |
| name | name | MarkingName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| organization | organization | typing.Optional[core_models.OrganizationRid] | None | If this marking is associated with an Organization, its RID will be populated here. |
| created_time | createdTime | core_models.CreatedTime | required; no default | No additional field description in SDK source. |
| created_by | createdBy | typing.Optional[core_models.CreatedBy] | default None | No additional field description in SDK source. |

```python
class Marking(core.ModelBase):
    """Marking"""

    id: core_models.MarkingId
    category_id: MarkingCategoryId = pydantic.Field(alias=str("categoryId"))  # type: ignore[literal-required]
    name: MarkingName
    description: typing.Optional[str] = None
    organization: typing.Optional[core_models.OrganizationRid] = None
    """If this marking is associated with an Organization, its RID will be populated here."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingName](MarkingName.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../core/models/OrganizationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Marking.md)
