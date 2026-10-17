# foundry_sdk.v2.admin.models.AuthenticationProvider


AuthenticationProvider

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | AuthenticationProviderRid | required; no default | No additional field description in SDK source. |
| name | name | AuthenticationProviderName | required; no default | No additional field description in SDK source. |
| realm | realm | core_models.Realm | required; no default | No additional field description in SDK source. |
| enabled | enabled | AuthenticationProviderEnabled | required; no default | Whether users can log in using this provider. |
| supported_hosts | supportedHosts | typing.List[HostName] | required; no default | This provider can only be utilized from these hosts. |
| supported_username_patterns | supportedUsernamePatterns | typing.List[str] | required; no default | Users who enter usernames that match these patterns will be redirected to this authentication provider. |
| protocol | protocol | AuthenticationProtocol | required; no default | No additional field description in SDK source. |

```python
class AuthenticationProvider(core.ModelBase):
    """AuthenticationProvider"""

    rid: AuthenticationProviderRid
    name: AuthenticationProviderName
    realm: core_models.Realm
    enabled: AuthenticationProviderEnabled
    """Whether users can log in using this provider."""

    supported_hosts: typing.List[HostName] = pydantic.Field(alias=str("supportedHosts"))  # type: ignore[literal-required]
    """This provider can only be utilized from these hosts."""

    supported_username_patterns: typing.List[str] = pydantic.Field(alias=str("supportedUsernamePatterns"))  # type: ignore[literal-required]
    """Users who enter usernames that match these patterns will be redirected to this authentication provider."""

    protocol: AuthenticationProtocol
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.AuthenticationProtocol](AuthenticationProtocol.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderEnabled](AuthenticationProviderEnabled.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderName](AuthenticationProviderName.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderRid](AuthenticationProviderRid.md)
- [foundry_sdk.v2.admin.models.HostName](HostName.md)
- [foundry_sdk.v2.core.models.Realm](../../core/models/Realm.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AuthenticationProvider.md)
