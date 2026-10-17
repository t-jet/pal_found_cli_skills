# v2.connectivity.Connection.update_export_settings


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Updates the [export settings on the Connection.](../../../../v2/connectivity/index.md)
Only users with Information Security Officer role can modify the export settings.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.update_export_settings`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def update_export_settings(self, connection_rid: connectivity_models.ConnectionRid, *, export_settings: connectivity_models.ConnectionExportSettings, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| export_settings | connectivity_models.ConnectionExportSettings | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |
| UpdateExportSettingsForConnectionPermissionDenied | Could not updateExportSettings the Connection. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/updateExportSettings'
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
connectivity_models.UpdateExportSettingsForConnectionRequest(export_settings=export_settings)
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
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'UpdateExportSettingsForConnectionPermissionDenied': connectivity_errors.UpdateExportSettingsForConnectionPermissionDenied}
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
- [foundry_sdk.v2.connectivity.errors.UpdateExportSettingsForConnectionPermissionDenied](../../../../models/v2/connectivity/errors/UpdateExportSettingsForConnectionPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.UpdateExportSettingsForConnectionPermissionDeniedParameters](../../../../models/v2/connectivity/errors/UpdateExportSettingsForConnectionPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionExportSettings](../../../../models/v2/connectivity/models/ConnectionExportSettings.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.UpdateExportSettingsForConnectionRequest](../../../../models/v2/connectivity/models/UpdateExportSettingsForConnectionRequest.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/Connection.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Export settings control whether this Connection can be an export destination. Verify the selected source and policy before changing them. [Local procedure](../../../../v2/connectivity/index.md).

[Part 1](update_export_settings.md)
