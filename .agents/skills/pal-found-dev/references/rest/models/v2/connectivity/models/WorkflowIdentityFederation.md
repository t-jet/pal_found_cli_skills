# foundry_sdk.v2.connectivity.models.WorkflowIdentityFederation


Authenticate as a service principal using workload identity federation. This is the recommended way to connect to Databricks.
Workload identity federation allows workloads running in Foundry to access Databricks APIs without the need for Databricks secrets.
Refer to our [OIDC documentation](https://palantir.com/docs/foundry/data-connection/oidc) for an overview of how OpenID Connect is supported in Foundry.
A service principal federation policy must exist in Databricks to allow Foundry to act as an identity provider.
Refer to the [official documentation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation) for guidance.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| service_principal_application_id | servicePrincipalApplicationId | typing.Optional[str] | default None | The ID of the Databricks [service principal](https://docs.databricks.com/aws/en/admin/users-groups/service-principals). <br>    If provided, a federated JWT token is exchanged using a<br>    service principal federation policy. If not provided, a federated JWT token is exchanged using an account<br>    federation policy. |
| issuer_url | issuerUrl | str | required; no default | Identifies the principal that issued the access token as a string URI. |
| audience | audience | str | required; no default | Identifies the recipients that the access token is intended for as a string URI. <br>    This should be the primary host name where the Connection lives. |
| subject | subject | ConnectionRid | required; no default | The RID of the Connection that is connecting to the external system. |
| type | type | typing.Literal['workflowIdentityFederation'] | 'workflowIdentityFederation' | No additional field description in SDK source. |

```python
class WorkflowIdentityFederation(core.ModelBase):
    """
    Authenticate as a service principal using workload identity federation. This is the recommended way to connect to Databricks.
    Workload identity federation allows workloads running in Foundry to access Databricks APIs without the need for Databricks secrets.
    Refer to our [OIDC documentation](https://palantir.com/docs/foundry/data-connection/oidc) for an overview of how OpenID Connect is supported in Foundry.
    A service principal federation policy must exist in Databricks to allow Foundry to act as an identity provider.
    Refer to the [official documentation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation) for guidance.
    """

    service_principal_application_id: typing.Optional[str] = pydantic.Field(alias=str("servicePrincipalApplicationId"), default=None)  # type: ignore[literal-required]
    """
    The ID of the Databricks [service principal](https://docs.databricks.com/aws/en/admin/users-groups/service-principals). 
    If provided, a federated JWT token is exchanged using a
    service principal federation policy. If not provided, a federated JWT token is exchanged using an account
    federation policy.
    """

    issuer_url: str = pydantic.Field(alias=str("issuerUrl"))  # type: ignore[literal-required]
    """Identifies the principal that issued the access token as a string URI."""

    audience: str
    """
    Identifies the recipients that the access token is intended for as a string URI. 
    This should be the primary host name where the Connection lives.
    """

    subject: ConnectionRid
    """The RID of the Connection that is connecting to the external system."""

    type: typing.Literal["workflowIdentityFederation"] = "workflowIdentityFederation"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](ConnectionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WorkflowIdentityFederation.md)
