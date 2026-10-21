# foundry_sdk.v2.admin.errors.CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters


Provider information for Principals in this Realm cannot be replaced.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| principalId | principalId | core_models.PrincipalId | TypedDict key required | No additional field description in SDK source. |
| realm | realm | core_models.Realm | TypedDict key required | No additional field description in SDK source. |

```python
class CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters(typing_extensions.TypedDict):
    """Provider information for Principals in this Realm cannot be replaced."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalId: core_models.PrincipalId
    realm: core_models.Realm
```

## Referenced definitions

- [foundry_sdk.v2.core.models.PrincipalId](../../core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.Realm](../../core/models/Realm.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters.md)
