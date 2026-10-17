# foundry_sdk.v2.connectivity.models.AwsOidcAuthentication


Foundry issues an OIDC token when this Connection runs. The external trust policy must accept the configured issuer (`iss`), audience (`aud`) and this Connection RID as subject (`sub`). A token from another Connection does not satisfy that subject check; token issuance does not create the external trust policy.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| audience | audience | str | required; no default | The configured audience that identifies the external system. |
| issuer_url | issuerUrl | str | required; no default | The URL that identifies Foundry as an OIDC identity provider. |
| subject | subject | ConnectionRid | required; no default | The RID of the Connection that is connecting to the external system. |
| type | type | typing.Literal['oidc'] | 'oidc' | No additional field description in SDK source. |

```python
class AwsOidcAuthentication(core.ModelBase):
    """
    [OpenID Connect (OIDC)](https://palantir.com/docs/foundry/data-connection/oidc/) is an open authentication protocol that allows
    you to authenticate to external system resources without the use of static credentials.
    """

    audience: str
    """The configured audience that identifies the external system."""

    issuer_url: str = pydantic.Field(alias=str("issuerUrl"))  # type: ignore[literal-required]
    """The URL that identifies Foundry as an OIDC identity provider."""

    subject: ConnectionRid
    """The RID of the Connection that is connecting to the external system."""

    type: typing.Literal["oidc"] = "oidc"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](ConnectionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AwsOidcAuthentication.md)
