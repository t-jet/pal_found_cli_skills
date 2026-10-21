# foundry_sdk.v2.connectivity.models.Domain


The domain that the connection is allowed to access.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| scheme | scheme | typing.Optional[UriScheme] | None | The scheme of the domain that the connection is allowed to access.<br>    If not specified, defaults to HTTPS. |
| host | host | str | required; no default | The domain name, IPv4, or IPv6 address. |
| port | port | typing.Optional[int] | None | The port number of the domain that the connection is allowed to access. |
| auth | auth | typing.Optional[RestAuthenticationMode] | None | The URI scheme must be HTTPS if using any authentication.<br>    If not specified, no authentication is required. |

```python
class Domain(core.ModelBase):
    """The domain that the connection is allowed to access."""

    scheme: typing.Optional[UriScheme] = None
    """
    The scheme of the domain that the connection is allowed to access.
    If not specified, defaults to HTTPS.
    """

    host: str
    """The domain name, IPv4, or IPv6 address."""

    port: typing.Optional[int] = None
    """The port number of the domain that the connection is allowed to access."""

    auth: typing.Optional[RestAuthenticationMode] = None
    """
    The URI scheme must be HTTPS if using any authentication.
    If not specified, no authentication is required.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.RestAuthenticationMode](RestAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.UriScheme](UriScheme.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Domain.md)
