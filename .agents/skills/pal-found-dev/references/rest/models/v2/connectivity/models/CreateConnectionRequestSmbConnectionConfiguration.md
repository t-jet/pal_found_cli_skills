# foundry_sdk.v2.connectivity.models.CreateConnectionRequestSmbConnectionConfiguration


CreateConnectionRequestSmbConnectionConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| proxy | proxy | typing.Optional[SmbProxyConfiguration] | None | No additional field description in SDK source. |
| hostname | hostname | str | required; no default | Any identifier that can resolve to a server hosting an SMB share. This includes IP addresses, local <br>    network names (e.g. FS-SERVER-01) or FQDNs. Should not include any protocol information like https://, smb://, etc |
| port | port | typing.Optional[int] | None | 445 by default |
| auth | auth | CreateConnectionRequestSmbAuth | required; no default | No additional field description in SDK source. |
| share | share | str | required; no default | Must be a valid SMB share name.<br>    https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/dc9978d7-6299-4c5a-a22d-a039cdc716ea |
| base_directory | baseDirectory | typing.Optional[str] | default None | All reads and writes in this source will happen in this subdirectory |
| require_message_signing | requireMessageSigning | typing.Optional[bool] | default None | If true, the client will request that the server sign all messages. If the server does not support <br>    message signing, the connection will fail. Defaults to true. |
| type | type | typing.Literal['smb'] | 'smb' | No additional field description in SDK source. |

```python
class CreateConnectionRequestSmbConnectionConfiguration(core.ModelBase):
    """CreateConnectionRequestSmbConnectionConfiguration"""

    proxy: typing.Optional[SmbProxyConfiguration] = None
    hostname: str
    """
    Any identifier that can resolve to a server hosting an SMB share. This includes IP addresses, local 
    network names (e.g. FS-SERVER-01) or FQDNs. Should not include any protocol information like https://, smb://, etc
    """

    port: typing.Optional[int] = None
    """445 by default"""

    auth: CreateConnectionRequestSmbAuth
    share: str
    """
    Must be a valid SMB share name.
    https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/dc9978d7-6299-4c5a-a22d-a039cdc716ea
    """

    base_directory: typing.Optional[str] = pydantic.Field(alias=str("baseDirectory"), default=None)  # type: ignore[literal-required]
    """All reads and writes in this source will happen in this subdirectory"""

    require_message_signing: typing.Optional[bool] = pydantic.Field(alias=str("requireMessageSigning"), default=None)  # type: ignore[literal-required]
    """
    If true, the client will request that the server sign all messages. If the server does not support 
    message signing, the connection will fail. Defaults to true.
    """

    type: typing.Literal["smb"] = "smb"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSmbAuth](CreateConnectionRequestSmbAuth.md)
- [foundry_sdk.v2.connectivity.models.SmbProxyConfiguration](SmbProxyConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestSmbConnectionConfiguration.md)
