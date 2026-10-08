# foundry_sdk.v2.admin.models.UserProviderInfo


UserProviderInfo

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| provider_id | providerId | ProviderId | required; no default | The ID of the User in the external authentication provider. This value is determined by the authentication provider.<br>    At most one User can have a given provider ID in a given Realm. |

```python
class UserProviderInfo(core.ModelBase):
    """UserProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias=str("providerId"))  # type: ignore[literal-required]
    """
    The ID of the User in the external authentication provider. This value is determined by the authentication provider.
    At most one User can have a given provider ID in a given Realm.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.ProviderId](ProviderId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UserProviderInfo.md)
