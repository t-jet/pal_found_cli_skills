# v2.connectivity.Connection.update_secrets


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Updates the secrets on the connection to the specified secret values.
Secrets that are currently configured on the connection but are omitted in the request will remain unchanged.

Secrets are transmitted over the network encrypted using TLS. Once the secrets reach Foundry's servers,
they will be temporarily decrypted and remain in plaintext in memory to be processed as needed.
They will stay in plaintext in memory until the garbage collection process cleans up the memory.
The secrets are always stored encrypted on our servers.

By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
use the Foundry UI instead.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.update_secrets`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def update_secrets(self, connection_rid: connectivity_models.ConnectionRid, *, secrets: typing.Dict[connectivity_models.SecretName, connectivity_models.PlaintextValue], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| secrets | typing.Dict[connectivity_models.SecretName, connectivity_models.PlaintextValue] | required | The secrets to be updated. The specified secret names must already be configured on the connection. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |
| SecretNamesDoNotExist | The secret names provided do not exist on the connection. |
| UpdateSecretsForConnectionPermissionDenied | Could not update secrets for the Connection. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/updateSecrets'
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
{'Content-Type': 'application/json'}
```

**body**

```python
connectivity_models.UpdateSecretsForConnectionRequest(secrets=secrets)
```

**response_type**

```python
None
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'SecretNamesDoNotExist': connectivity_errors.SecretNamesDoNotExist, 'UpdateSecretsForConnectionPermissionDenied': connectivity_errors.UpdateSecretsForConnectionPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `None`. Ordinary async return: `typing.Awaitable[None]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | None |
| sync_raw | ApiResponse[None] |
| sync_streaming | Not exposed |
| async_ordinary | typing.Awaitable[None] |
| async_raw | Awaitable[AsyncApiResponse[None]] |
| async_streaming | Not exposed |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFound](../../../../models/v2/connectivity/errors/ConnectionNotFound.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFoundParameters](../../../../models/v2/connectivity/errors/ConnectionNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.errors.SecretNamesDoNotExist](../../../../models/v2/connectivity/errors/SecretNamesDoNotExist.md)
- [foundry_sdk.v2.connectivity.errors.SecretNamesDoNotExistParameters](../../../../models/v2/connectivity/errors/SecretNamesDoNotExistParameters.md)
- [foundry_sdk.v2.connectivity.errors.UpdateSecretsForConnectionPermissionDenied](../../../../models/v2/connectivity/errors/UpdateSecretsForConnectionPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.UpdateSecretsForConnectionPermissionDeniedParameters](../../../../models/v2/connectivity/errors/UpdateSecretsForConnectionPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.PlaintextValue](../../../../models/v2/connectivity/models/PlaintextValue.md)
- [foundry_sdk.v2.connectivity.models.SecretName](../../../../models/v2/connectivity/models/SecretName.md)
- [foundry_sdk.v2.connectivity.models.UpdateSecretsForConnectionRequest](../../../../models/v2/connectivity/models/UpdateSecretsForConnectionRequest.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/Connection.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](update_secrets.md)
