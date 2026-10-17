# foundry_sdk.v2.connectivity.models.RestConnectionConfiguration


The REST Connection limits requests to its configured domains. An optional `oauth2_client_rid` selects one preconfigured outbound application for OAuth 2.0; replacing it changes the OAuth selection for all configured domains. Check approved egress to the domains and the external server's authorization settings before using the Connection.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| domains | domains | typing.List[Domain] | required; no default | The domains that the connection is allowed to access.<br>    At least one domain must be specified. |
| additional_secrets | additionalSecrets | typing.Optional[RestConnectionAdditionalSecrets] | default None | Additional secrets that can be referenced in code and webhook configurations.<br>    If not provided, no additional secrets will be created. |
| oauth2_client_rid | oauth2ClientRid | typing.Optional[core.RID] | default None | The RID of the Outbound application that is used to authenticate to the external system via OAuth2.<br>    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.<br>    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization. |
| type | type | typing.Literal['rest'] | 'rest' | No additional field description in SDK source. |

```python
class RestConnectionConfiguration(core.ModelBase):
    """The configuration needed to connect to a [REST external system](https://palantir.com/docs/foundry/available-connectors/rest-apis)."""

    domains: typing.List[Domain]
    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    additional_secrets: typing.Optional[RestConnectionAdditionalSecrets] = pydantic.Field(alias=str("additionalSecrets"), default=None)  # type: ignore[literal-required]
    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2_client_rid: typing.Optional[core.RID] = pydantic.Field(alias=str("oauth2ClientRid"), default=None)  # type: ignore[literal-required]
    """
    The RID of the [Outbound application](https://palantir.com/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    type: typing.Literal["rest"] = "rest"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.connectivity.models.Domain](Domain.md)
- [foundry_sdk.v2.connectivity.models.RestConnectionAdditionalSecrets](RestConnectionAdditionalSecrets.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RestConnectionConfiguration.md)
