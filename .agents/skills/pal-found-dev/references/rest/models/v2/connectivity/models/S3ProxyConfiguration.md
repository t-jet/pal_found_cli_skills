# foundry_sdk.v2.connectivity.models.S3ProxyConfiguration


S3ProxyConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| host | host | str | required; no default | Domain name, IPv4, or IPv6 address. <br>    `protocol` and `port` must be specified separately. |
| port | port | int | required; no default | No additional field description in SDK source. |
| non_proxy_hosts | nonProxyHosts | typing.Optional[typing.List[str]] | default None | A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards. |
| protocol | protocol | typing.Optional[Protocol] | None | If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS". |
| credentials | credentials | typing.Optional[BasicCredentials] | None | No additional field description in SDK source. |

```python
class S3ProxyConfiguration(core.ModelBase):
    """S3ProxyConfiguration"""

    host: str
    """
    Domain name, IPv4, or IPv6 address. 
    `protocol` and `port` must be specified separately.
    """

    port: int
    non_proxy_hosts: typing.Optional[typing.List[str]] = pydantic.Field(alias=str("nonProxyHosts"), default=None)  # type: ignore[literal-required]
    """A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards."""

    protocol: typing.Optional[Protocol] = None
    """If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS"."""

    credentials: typing.Optional[BasicCredentials] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.BasicCredentials](BasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.Protocol](Protocol.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](S3ProxyConfiguration.md)
