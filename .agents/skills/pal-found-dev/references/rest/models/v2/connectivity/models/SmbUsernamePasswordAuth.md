# foundry_sdk.v2.connectivity.models.SmbUsernamePasswordAuth


SmbUsernamePasswordAuth

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| username | username | str | required; no default | No additional field description in SDK source. |
| password | password | EncryptedProperty | required; no default | No additional field description in SDK source. |
| domain | domain | typing.Optional[str] | None | Optionally specify a Windows domain to use when authenticating. Normal DNS domain restrictions apply<br>    but the top-level domain might be something non-standard like .local. Defaults to WORKGROUP |
| type | type | typing.Literal['usernamePassword'] | 'usernamePassword' | No additional field description in SDK source. |

```python
class SmbUsernamePasswordAuth(core.ModelBase):
    """SmbUsernamePasswordAuth"""

    username: str
    password: EncryptedProperty
    domain: typing.Optional[str] = None
    """
    Optionally specify a Windows domain to use when authenticating. Normal DNS domain restrictions apply
    but the top-level domain might be something non-standard like .local. Defaults to WORKGROUP
    """

    type: typing.Literal["usernamePassword"] = "usernamePassword"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](EncryptedProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SmbUsernamePasswordAuth.md)
