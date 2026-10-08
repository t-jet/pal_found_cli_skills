# v2.connectivity.Connection.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Connection with a [direct connection](../../../../v2/connectivity/index.md) runtime.

Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
up the memory. The secrets are always stored encrypted on our servers.
By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
use the Foundry UI instead.

## SDK invocation contract

```python
def create(self, *, configuration: connectivity_models.CreateConnectionRequestConnectionConfiguration, display_name: connectivity_models.ConnectionDisplayName, parent_folder_rid: filesystem_models.FolderRid, worker: connectivity_models.CreateConnectionRequestConnectionWorker, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.Connection: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| configuration | connectivity_models.CreateConnectionRequestConnectionConfiguration | required | Value shape and constraints are in its referenced local type definition. |
| display_name | connectivity_models.ConnectionDisplayName | required | The display name of the Connection. The display name must not be blank. |
| parent_folder_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| worker | connectivity_models.CreateConnectionRequestConnectionWorker | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |
| ConnectionTypeNotSupported | The specified connection is not yet supported in the Platform API. |
| CreateConnectionPermissionDenied | Could not create the Connection. |
| FolderNotFound | The given Folder could not be found. |
| ParentFolderNotFoundForConnection | The parent folder for the specified connection could not be found. |
| PropertyCannotBeBlank | The specified property cannot be blank. |
| UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections | The UnknownWorker cannot be used for creating or updating connections. Please use the Foundry worker instead. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/connectivity/connections'
```

**query_params**

```python
{}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
connectivity_models.CreateConnectionRequest(parent_folder_rid=parent_folder_rid, configuration=configuration, display_name=display_name, worker=worker)
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
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'ConnectionTypeNotSupported': connectivity_errors.ConnectionTypeNotSupported, 'CreateConnectionPermissionDenied': connectivity_errors.CreateConnectionPermissionDenied, 'FolderNotFound': filesystem_errors.FolderNotFound, 'ParentFolderNotFoundForConnection': connectivity_errors.ParentFolderNotFoundForConnection, 'PropertyCannotBeBlank': connectivity_errors.PropertyCannotBeBlank, 'UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections': connectivity_errors.UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections}
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
- [foundry_sdk.v2.connectivity.errors.ConnectionTypeNotSupported](../../../../models/v2/connectivity/errors/ConnectionTypeNotSupported.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionTypeNotSupportedParameters](../../../../models/v2/connectivity/errors/ConnectionTypeNotSupportedParameters.md)
- [foundry_sdk.v2.connectivity.errors.CreateConnectionPermissionDenied](../../../../models/v2/connectivity/errors/CreateConnectionPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.CreateConnectionPermissionDeniedParameters](../../../../models/v2/connectivity/errors/CreateConnectionPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.errors.ParentFolderNotFoundForConnection](../../../../models/v2/connectivity/errors/ParentFolderNotFoundForConnection.md)
- [foundry_sdk.v2.connectivity.errors.ParentFolderNotFoundForConnectionParameters](../../../../models/v2/connectivity/errors/ParentFolderNotFoundForConnectionParameters.md)
- [foundry_sdk.v2.connectivity.errors.PropertyCannotBeBlank](../../../../models/v2/connectivity/errors/PropertyCannotBeBlank.md)
- [foundry_sdk.v2.connectivity.errors.PropertyCannotBeBlankParameters](../../../../models/v2/connectivity/errors/PropertyCannotBeBlankParameters.md)
- [foundry_sdk.v2.connectivity.errors.UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections](../../../../models/v2/connectivity/errors/UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections.md)
- [foundry_sdk.v2.connectivity.errors.UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnectionsParameters](../../../../models/v2/connectivity/errors/UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnectionsParameters.md)
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
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequest](../../../../models/v2/connectivity/models/CreateConnectionRequest.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestAsPlaintextValue](../../../../models/v2/connectivity/models/CreateConnectionRequestAsPlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestAsSecretName](../../../../models/v2/connectivity/models/CreateConnectionRequestAsSecretName.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestBasicCredentials](../../../../models/v2/connectivity/models/CreateConnectionRequestBasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestConnectionWorker](../../../../models/v2/connectivity/models/CreateConnectionRequestConnectionWorker.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestDatabricksAuthenticationMode](../../../../models/v2/connectivity/models/CreateConnectionRequestDatabricksAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestDatabricksConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestDatabricksConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestEncryptedProperty](../../../../models/v2/connectivity/models/CreateConnectionRequestEncryptedProperty.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestFoundryWorker](../../../../models/v2/connectivity/models/CreateConnectionRequestFoundryWorker.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestJdbcConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestJdbcConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestOauthMachineToMachineAuth](../../../../models/v2/connectivity/models/CreateConnectionRequestOauthMachineToMachineAuth.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestPersonalAccessToken](../../../../models/v2/connectivity/models/CreateConnectionRequestPersonalAccessToken.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestRestConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestRestConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestS3ConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestS3ConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSmbAuth](../../../../models/v2/connectivity/models/CreateConnectionRequestSmbAuth.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSmbConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestSmbConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSmbUsernamePasswordAuth](../../../../models/v2/connectivity/models/CreateConnectionRequestSmbUsernamePasswordAuth.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeAuthenticationMode](../../../../models/v2/connectivity/models/CreateConnectionRequestSnowflakeAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeConnectionConfiguration](../../../../models/v2/connectivity/models/CreateConnectionRequestSnowflakeConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeExternalOauth](../../../../models/v2/connectivity/models/CreateConnectionRequestSnowflakeExternalOauth.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeKeyPairAuthentication](../../../../models/v2/connectivity/models/CreateConnectionRequestSnowflakeKeyPairAuthentication.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestUnknownWorker](../../../../models/v2/connectivity/models/CreateConnectionRequestUnknownWorker.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestWorkflowIdentityFederation](../../../../models/v2/connectivity/models/CreateConnectionRequestWorkflowIdentityFederation.md)
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
- [foundry_sdk.v2.filesystem.errors.FolderNotFound](../../../../models/v2/filesystem/errors/FolderNotFound.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFoundParameters](../../../../models/v2/filesystem/errors/FolderNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/Connection.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A direct connection accesses its source through the configured runtime. Check source reachability and credentials before creating imports. [Local procedure](../../../../v2/connectivity/index.md).

[Part 1](create.md)
