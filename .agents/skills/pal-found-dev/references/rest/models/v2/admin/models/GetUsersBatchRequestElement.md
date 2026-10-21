# foundry_sdk.v2.admin.models.GetUsersBatchRequestElement


GetUsersBatchRequestElement

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| user_id | userId | core_models.UserId | required; no default | No additional field description in SDK source. |
| status | status | typing.Optional[core_models.UserStatus] | None | No additional field description in SDK source. |

```python
class GetUsersBatchRequestElement(core.ModelBase):
    """GetUsersBatchRequestElement"""

    user_id: core_models.UserId = pydantic.Field(alias=str("userId"))  # type: ignore[literal-required]
    status: typing.Optional[core_models.UserStatus] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)
- [foundry_sdk.v2.core.models.UserStatus](../../core/models/UserStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetUsersBatchRequestElement.md)
