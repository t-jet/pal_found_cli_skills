# foundry_sdk.v2.connectivity.models.CreateConnectionRequestDatabricksAuthenticationMode


The method of authentication for connecting to an external Databricks system.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CreateConnectionRequestDatabricksAuthenticationMode: typing_extensions.TypeAlias = (
    typing_extensions.Annotated[
        typing.Union[
            "CreateConnectionRequestWorkflowIdentityFederation",
            "CreateConnectionRequestOauthMachineToMachineAuth",
            "CreateConnectionRequestPersonalAccessToken",
            "CreateConnectionRequestBasicCredentials",
        ],
        pydantic.Field(discriminator="type"),
    ]
)
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestBasicCredentials](CreateConnectionRequestBasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestOauthMachineToMachineAuth](CreateConnectionRequestOauthMachineToMachineAuth.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestPersonalAccessToken](CreateConnectionRequestPersonalAccessToken.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestWorkflowIdentityFederation](CreateConnectionRequestWorkflowIdentityFederation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestDatabricksAuthenticationMode.md)
