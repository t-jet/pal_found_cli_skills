# v2.connectivity.Connection.upload_custom_jdbc_drivers


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Upload custom jdbc drivers to an existing JDBC connection.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.upload_custom_jdbc_drivers`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def upload_custom_jdbc_drivers(self, connection_rid: connectivity_models.ConnectionRid, body: bytes, *, file_name: str, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.Connection: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| body | bytes | required | Body of the request |
| file_name | str | required | The file name of the uploaded JDBC driver. Must end with .jar |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |
| UploadCustomJdbcDriversConnectionPermissionDenied | Could not uploadCustomJdbcDrivers the Connection. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/uploadCustomJdbcDrivers'
```

**query_params**

```python
{'fileName': file_name}
```

**path_params**

```python
{'connectionRid': connection_rid}
```

**header_params**

```python
{'Content-Type': 'application/octet-stream', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
connectivity_models.Connection
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'UploadCustomJdbcDriversConnectionPermissionDenied': connectivity_errors.UploadCustomJdbcDriversConnectionPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `connectivity_models.Connection`. Ordinary async return: `typing.Awaitable[connectivity_models.Connection]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | connectivity_models.Connection |
| sync_raw | ApiResponse[connectivity_models.Connection] |
| sync_streaming | StreamingContextManager[connectivity_models.Connection] |
| async_ordinary | typing.Awaitable[connectivity_models.Connection] |
| async_raw | Awaitable[AsyncApiResponse[connectivity_models.Connection]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[connectivity_models.Connection]] |

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
- [foundry_sdk.v2.connectivity.errors.UploadCustomJdbcDriversConnectionPermissionDenied](../../../../models/v2/connectivity/errors/UploadCustomJdbcDriversConnectionPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.UploadCustomJdbcDriversConnectionPermissionDeniedParameters](../../../../models/v2/connectivity/errors/UploadCustomJdbcDriversConnectionPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.models.ApiKeyAuthentication](../../../../models/v2/connectivity/models/ApiKeyAuthentication.md)
- [foundry_sdk.v2.connectivity.models.AsPlaintextValue](../../../../models/v2/connectivity/models/AsPlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.AsSecretName](../../../../models/v2/connectivity/models/AsSecretName.md)
- [foundry_sdk.v2.connectivity.models.AwsAccessKey](../../../../models/v2/connectivity/models/AwsAccessKey.md)
- [foundry_sdk.v2.connectivity.models.AwsOidcAuthentication](../../../../models/v2/connectivity/models/AwsOidcAuthentication.md)
- [foundry_sdk.v2.connectivity.models.BasicCredentials](../../../../models/v2/connectivity/models/BasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.BearerToken](../../../../models/v2/connectivity/models/BearerToken.md)
- [foundry_sdk.v2.connectivity.models.CloudIdentity](../../../../models/v2/connectivity/models/CloudIdentity.md)
- [foundry_sdk.v2.connectivity.models.CloudIdentityRid](../../../../models/v2/connectivity/models/CloudIdentityRid.md)
- [foundry_sdk.v2.connectivity.models.Connection](../../../../models/v2/connectivity/models/Connection.md)
- [foundry_sdk.v2.connectivity.models.ConnectionConfiguration](../../../../models/v2/connectivity/models/ConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.ConnectionDisplayName](../../../../models/v2/connectivity/models/ConnectionDisplayName.md)
- [foundry_sdk.v2.connectivity.models.ConnectionExportSettings](../../../../models/v2/connectivity/models/ConnectionExportSettings.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.ConnectionWorker](../../../../models/v2/connectivity/models/ConnectionWorker.md)
- [foundry_sdk.v2.connectivity.models.DatabricksAuthenticationMode](../../../../models/v2/connectivity/models/DatabricksAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.DatabricksConnectionConfiguration](../../../../models/v2/connectivity/models/DatabricksConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.Domain](../../../../models/v2/connectivity/models/Domain.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](../../../../models/v2/connectivity/models/EncryptedProperty.md)
- [foundry_sdk.v2.connectivity.models.FoundryWorker](../../../../models/v2/connectivity/models/FoundryWorker.md)
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
- [foundry_sdk.v2.connectivity.models.UnknownWorker](../../../../models/v2/connectivity/models/UnknownWorker.md)
- [foundry_sdk.v2.connectivity.models.UriScheme](../../../../models/v2/connectivity/models/UriScheme.md)
- [foundry_sdk.v2.connectivity.models.WorkflowIdentityFederation](../../../../models/v2/connectivity/models/WorkflowIdentityFederation.md)
- [foundry_sdk.v2.core.models.Duration](../../../../models/v2/core/models/Duration.md)
- [foundry_sdk.v2.core.models.NetworkEgressPolicyRid](../../../../models/v2/core/models/NetworkEgressPolicyRid.md)
- [foundry_sdk.v2.core.models.TimeUnit](../../../../models/v2/core/models/TimeUnit.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/Connection.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](upload_custom_jdbc_drivers.md)
