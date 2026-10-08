# foundry_sdk.v2.admin.models.Enrollment


Enrollment

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.EnrollmentRid | required; no default | No additional field description in SDK source. |
| name | name | EnrollmentName | required; no default | No additional field description in SDK source. |
| created_time | createdTime | typing.Optional[core_models.CreatedTime] | default None | No additional field description in SDK source. |

```python
class Enrollment(core.ModelBase):
    """Enrollment"""

    rid: core_models.EnrollmentRid
    name: EnrollmentName
    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.EnrollmentName](EnrollmentName.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../core/models/EnrollmentRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Enrollment.md)
