# v2.connectivity.TableImport.delete


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Delete the TableImport with the specified RID.
Deleting the table import does not delete the destination dataset but the dataset will no longer
be updated by this import.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.TableImport.delete`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def delete(self, connection_rid: connectivity_models.ConnectionRid, table_import_rid: connectivity_models.TableImportRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| table_import_rid | connectivity_models.TableImportRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| DeleteTableImportPermissionDenied | Could not delete the TableImport. |
| TableImportNotFound | The given TableImport could not be found. |

## Wire request

**method**

```python
'DELETE'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}'
```

**query_params**

```python
{}
```

**path_params**

```python
{'connectionRid': connection_rid, 'tableImportRid': table_import_rid}
```

**header_params**

```python
{}
```

**body**

```python
None
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
{'DeleteTableImportPermissionDenied': connectivity_errors.DeleteTableImportPermissionDenied, 'TableImportNotFound': connectivity_errors.TableImportNotFound}
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
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.DeleteTableImportPermissionDenied](../../../../models/v2/connectivity/errors/DeleteTableImportPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.DeleteTableImportPermissionDeniedParameters](../../../../models/v2/connectivity/errors/DeleteTableImportPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.errors.TableImportNotFound](../../../../models/v2/connectivity/errors/TableImportNotFound.md)
- [foundry_sdk.v2.connectivity.errors.TableImportNotFoundParameters](../../../../models/v2/connectivity/errors/TableImportNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.TableImportRid](../../../../models/v2/connectivity/models/TableImportRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/TableImport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](delete.md)
