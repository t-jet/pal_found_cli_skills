# v2.connectivity.Connection.get_configuration


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieves the ConnectionConfiguration of the [Connection](../../../../v2/connectivity/index.md) itself.
This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.get_configuration`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_configuration(self, connection_rid: connectivity_models.ConnectionRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.ConnectionConfiguration: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |
| ConnectionTypeNotSupported | The specified connection is not yet supported in the Platform API. |
| GetConfigurationPermissionDenied | Could not getConfiguration the Connection. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/getConfiguration'
```

**query_params**

```python
{}
```

**path_params**

```python
{'connectionRid': connection_rid}
```

**header_params**

```python
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
connectivity_models.ConnectionConfiguration
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'ConnectionTypeNotSupported': connectivity_errors.ConnectionTypeNotSupported, 'GetConfigurationPermissionDenied': connectivity_errors.GetConfigurationPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `connectivity_models.ConnectionConfiguration`. Ordinary async return: `typing.Awaitable[connectivity_models.ConnectionConfiguration]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | connectivity_models.ConnectionConfiguration |
| sync_raw | ApiResponse[connectivity_models.ConnectionConfiguration] |
| sync_streaming | StreamingContextManager[connectivity_models.ConnectionConfiguration] |
| async_ordinary | typing.Awaitable[connectivity_models.ConnectionConfiguration] |
| async_raw | Awaitable[AsyncApiResponse[connectivity_models.ConnectionConfiguration]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[connectivity_models.ConnectionConfiguration]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFound](../../../../models/v2/connectivity/errors/ConnectionNotFound.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFoundParameters](../../../../models/v2/connectivity/errors/ConnectionNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionTypeNotSupported](../../../../models/v2/connectivity/errors/ConnectionTypeNotSupported.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionTypeNotSupportedParameters](../../../../models/v2/connectivity/errors/ConnectionTypeNotSupportedParameters.md)
- [foundry_sdk.v2.connectivity.errors.GetConfigurationPermissionDenied](../../../../models/v2/connectivity/errors/GetConfigurationPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.GetConfigurationPermissionDeniedParameters](../../../../models/v2/connectivity/errors/GetConfigurationPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.models.ApiKeyAuthentication](../../../../models/v2/connectivity/models/ApiKeyAuthentication.md)
- [foundry_sdk.v2.connectivity.models.AsPlaintextValue](../../../../models/v2/connectivity/models/AsPlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.AsSecretName](../../../../models/v2/connectivity/models/AsSecretName.md)
- [foundry_sdk.v2.connectivity.models.AwsAccessKey](../../../../models/v2/connectivity/models/AwsAccessKey.md)
- [foundry_sdk.v2.connectivity.models.AwsOidcAuthentication](../../../../models/v2/connectivity/models/AwsOidcAuthentication.md)
- [foundry_sdk.v2.connectivity.models.BasicCredentials](../../../../models/v2/connectivity/models/BasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.BearerToken](../../../../models/v2/connectivity/models/BearerToken.md)
- [foundry_sdk.v2.connectivity.models.CloudIdentity](../../../../models/v2/connectivity/models/CloudIdentity.md)
- [foundry_sdk.v2.connectivity.models.CloudIdentityRid](../../../../models/v2/connectivity/models/CloudIdentityRid.md)
- [foundry_sdk.v2.connectivity.models.ConnectionConfiguration](../../../../models/v2/connectivity/models/ConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.DatabricksAuthenticationMode](../../../../models/v2/connectivity/models/DatabricksAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.DatabricksConnectionConfiguration](../../../../models/v2/connectivity/models/DatabricksConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.Domain](../../../../models/v2/connectivity/models/Domain.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](../../../../models/v2/connectivity/models/EncryptedProperty.md)
- [foundry_sdk.v2.connectivity.models.HeaderApiKey](../../../../models/v2/connectivity/models/HeaderApiKey.md)
- [foundry_sdk.v2.connectivity.models.JdbcConnectionConfiguration](../../../../models/v2/connectivity/models/JdbcConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.JdbcDriverArtifactName](../../../../models/v2/connectivity/models/JdbcDriverArtifactName.md)
- [foundry_sdk.v2.connectivity.models.JdbcProperties](../../../../models/v2/connectivity/models/JdbcProperties.md)
- [foundry_sdk.v2.connectivity.models.OauthMachineToMachineAuth](../../../../models/v2/connectivity/models/OauthMachineToMachineAuth.md)
- [foundry_sdk.v2.connectivity.models.PersonalAccessToken](../../../../models/v2/connectivity/models/PersonalAccessToken.md)
- [foundry_sdk.v2.connectivity.models.PlaintextValue](../../../../models/v2/connectivity/models/PlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.Protocol](../../../../models/v2/connectivity/models/Protocol.md)
- [foundry_sdk.v2.connectivity.models.QueryParameterApiKey](../../../../models/v2/connectivity/models/QueryParameterApiKey.md)
- [foundry_sdk.v2.connectivity.models.Region](../../../../models/v2/connectivity/models/Region.md)
- [foundry_sdk.v2.connectivity.models.RestAuthenticationMode](../../../../models/v2/connectivity/models/RestAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.RestConnectionAdditionalSecrets](../../../../models/v2/connectivity/models/RestConnectionAdditionalSecrets.md)
- [foundry_sdk.v2.connectivity.models.RestConnectionConfiguration](../../../../models/v2/connectivity/models/RestConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.RestConnectionOAuth2](../../../../models/v2/connectivity/models/RestConnectionOAuth2.md)
- [foundry_sdk.v2.connectivity.models.RestRequestApiKeyLocation](../../../../models/v2/connectivity/models/RestRequestApiKeyLocation.md)
- [foundry_sdk.v2.connectivity.models.S3AuthenticationMode](../../../../models/v2/connectivity/models/S3AuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.S3ConnectionConfiguration](../../../../models/v2/connectivity/models/S3ConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.S3KmsConfiguration](../../../../models/v2/connectivity/models/S3KmsConfiguration.md)
- [foundry_sdk.v2.connectivity.models.S3ProxyConfiguration](../../../../models/v2/connectivity/models/S3ProxyConfiguration.md)
- [foundry_sdk.v2.connectivity.models.SecretName](../../../../models/v2/connectivity/models/SecretName.md)
- [foundry_sdk.v2.connectivity.models.SecretsNames](../../../../models/v2/connectivity/models/SecretsNames.md)
- [foundry_sdk.v2.connectivity.models.SecretsWithPlaintextValues](../../../../models/v2/connectivity/models/SecretsWithPlaintextValues.md)
- [foundry_sdk.v2.connectivity.models.SmbAuth](../../../../models/v2/connectivity/models/SmbAuth.md)
- [foundry_sdk.v2.connectivity.models.SmbConnectionConfiguration](../../../../models/v2/connectivity/models/SmbConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.SmbProxyConfiguration](../../../../models/v2/connectivity/models/SmbProxyConfiguration.md)
- [foundry_sdk.v2.connectivity.models.SmbProxyType](../../../../models/v2/connectivity/models/SmbProxyType.md)
- [foundry_sdk.v2.connectivity.models.SmbUsernamePasswordAuth](../../../../models/v2/connectivity/models/SmbUsernamePasswordAuth.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeAuthenticationMode](../../../../models/v2/connectivity/models/SnowflakeAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeConnectionConfiguration](../../../../models/v2/connectivity/models/SnowflakeConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeExternalOauth](../../../../models/v2/connectivity/models/SnowflakeExternalOauth.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeKeyPairAuthentication](../../../../models/v2/connectivity/models/SnowflakeKeyPairAuthentication.md)
- [foundry_sdk.v2.connectivity.models.StsRoleConfiguration](../../../../models/v2/connectivity/models/StsRoleConfiguration.md)
- [foundry_sdk.v2.connectivity.models.UriScheme](../../../../models/v2/connectivity/models/UriScheme.md)
- [foundry_sdk.v2.connectivity.models.WorkflowIdentityFederation](../../../../models/v2/connectivity/models/WorkflowIdentityFederation.md)
- [foundry_sdk.v2.core.models.Duration](../../../../models/v2/core/models/Duration.md)
- [foundry_sdk.v2.core.models.TimeUnit](../../../../models/v2/core/models/TimeUnit.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/Connection.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A Connection configuration contains source/runtime settings; read it separately from imported datasets. [Local procedure](../../../../v2/connectivity/index.md).

[Part 1](get_configuration.md)
