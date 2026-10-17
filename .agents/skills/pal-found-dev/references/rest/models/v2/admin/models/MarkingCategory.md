# foundry_sdk.v2.admin.models.MarkingCategory


MarkingCategory

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | MarkingCategoryId | required; no default | No additional field description in SDK source. |
| name | name | MarkingCategoryName | required; no default | No additional field description in SDK source. |
| description | description | MarkingCategoryDescription | required; no default | No additional field description in SDK source. |
| category_type | categoryType | MarkingCategoryType | required; no default | No additional field description in SDK source. |
| marking_type | markingType | MarkingType | required; no default | No additional field description in SDK source. |
| markings | markings | typing.List[core_models.MarkingId] | required; no default | No additional field description in SDK source. |
| created_time | createdTime | core_models.CreatedTime | required; no default | No additional field description in SDK source. |
| created_by | createdBy | typing.Optional[core_models.CreatedBy] | default None | No additional field description in SDK source. |

```python
class MarkingCategory(core.ModelBase):
    """MarkingCategory"""

    id: MarkingCategoryId
    name: MarkingCategoryName
    description: MarkingCategoryDescription
    category_type: MarkingCategoryType = pydantic.Field(alias=str("categoryType"))  # type: ignore[literal-required]
    marking_type: MarkingType = pydantic.Field(alias=str("markingType"))  # type: ignore[literal-required]
    markings: typing.List[core_models.MarkingId]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryDescription](MarkingCategoryDescription.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryName](MarkingCategoryName.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryType](MarkingCategoryType.md)
- [foundry_sdk.v2.admin.models.MarkingType](MarkingType.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MarkingCategory.md)
