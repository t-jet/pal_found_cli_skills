# v2.connectivity.VirtualTable.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new [Virtual Table](../../../../v2/connectivity/index.md) from an upstream table. The VirtualTable will be created
in the specified parent folder and can be queried through Foundry's data access APIs.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.VirtualTable.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, connection_rid: connectivity_models.ConnectionRid, *, config: connectivity_models.VirtualTableConfig, name: connectivity_models.TableName, parent_rid: filesystem_models.FolderRid, markings: typing.Optional[typing.List[core_models.MarkingId]]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.VirtualTable: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| config | connectivity_models.VirtualTableConfig | required | Value shape and constraints are in its referenced local type definition. |
| name | connectivity_models.TableName | required | Value shape and constraints are in its referenced local type definition. |
| parent_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| markings | typing.Optional[typing.List[core_models.MarkingId]] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |
| CreateVirtualTablePermissionDenied | Could not create the VirtualTable. |
| InvalidVirtualTableConnection | The specified connection is invalid or inaccessible. |
| VirtualTableAlreadyExists | A VirtualTable with the same name already exists in the parent folder. |
| VirtualTableRegisterFromSourcePermissionDenied | User lacks permission to use the specified connection for virtual table registration. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/virtualTables'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
connectivity_models.CreateVirtualTableRequest(markings=markings, parent_rid=parent_rid, name=name, config=config)
```

**response_type**

```python
connectivity_models.VirtualTable
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'CreateVirtualTablePermissionDenied': connectivity_errors.CreateVirtualTablePermissionDenied, 'InvalidVirtualTableConnection': connectivity_errors.InvalidVirtualTableConnection, 'VirtualTableAlreadyExists': connectivity_errors.VirtualTableAlreadyExists, 'VirtualTableRegisterFromSourcePermissionDenied': connectivity_errors.VirtualTableRegisterFromSourcePermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `connectivity_models.VirtualTable`. Ordinary async return: `typing.Awaitable[connectivity_models.VirtualTable]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | connectivity_models.VirtualTable |
| sync_raw | ApiResponse[connectivity_models.VirtualTable] |
| sync_streaming | StreamingContextManager[connectivity_models.VirtualTable] |
| async_ordinary | typing.Awaitable[connectivity_models.VirtualTable] |
| async_raw | Awaitable[AsyncApiResponse[connectivity_models.VirtualTable]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[connectivity_models.VirtualTable]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFound](../../../../models/v2/connectivity/errors/ConnectionNotFound.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFoundParameters](../../../../models/v2/connectivity/errors/ConnectionNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.errors.CreateVirtualTablePermissionDenied](../../../../models/v2/connectivity/errors/CreateVirtualTablePermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.CreateVirtualTablePermissionDeniedParameters](../../../../models/v2/connectivity/errors/CreateVirtualTablePermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.errors.InvalidVirtualTableConnection](../../../../models/v2/connectivity/errors/InvalidVirtualTableConnection.md)
- [foundry_sdk.v2.connectivity.errors.InvalidVirtualTableConnectionParameters](../../../../models/v2/connectivity/errors/InvalidVirtualTableConnectionParameters.md)
- [foundry_sdk.v2.connectivity.errors.VirtualTableAlreadyExists](../../../../models/v2/connectivity/errors/VirtualTableAlreadyExists.md)
- [foundry_sdk.v2.connectivity.errors.VirtualTableAlreadyExistsParameters](../../../../models/v2/connectivity/errors/VirtualTableAlreadyExistsParameters.md)
- [foundry_sdk.v2.connectivity.errors.VirtualTableRegisterFromSourcePermissionDenied](../../../../models/v2/connectivity/errors/VirtualTableRegisterFromSourcePermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.VirtualTableRegisterFromSourcePermissionDeniedParameters](../../../../models/v2/connectivity/errors/VirtualTableRegisterFromSourcePermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.models.BigQueryVirtualTableConfig](../../../../models/v2/connectivity/models/BigQueryVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.CreateVirtualTableRequest](../../../../models/v2/connectivity/models/CreateVirtualTableRequest.md)
- [foundry_sdk.v2.connectivity.models.DeltaVirtualTableConfig](../../../../models/v2/connectivity/models/DeltaVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.FileFormat](../../../../models/v2/connectivity/models/FileFormat.md)
- [foundry_sdk.v2.connectivity.models.FilesVirtualTableConfig](../../../../models/v2/connectivity/models/FilesVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.GlueVirtualTableConfig](../../../../models/v2/connectivity/models/GlueVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.IcebergVirtualTableConfig](../../../../models/v2/connectivity/models/IcebergVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.InvalidConnectionReason](../../../../models/v2/connectivity/models/InvalidConnectionReason.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeVirtualTableConfig](../../../../models/v2/connectivity/models/SnowflakeVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.TableName](../../../../models/v2/connectivity/models/TableName.md)
- [foundry_sdk.v2.connectivity.models.TableRid](../../../../models/v2/connectivity/models/TableRid.md)
- [foundry_sdk.v2.connectivity.models.UnityVirtualTableConfig](../../../../models/v2/connectivity/models/UnityVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.VirtualTable](../../../../models/v2/connectivity/models/VirtualTable.md)
- [foundry_sdk.v2.connectivity.models.VirtualTableConfig](../../../../models/v2/connectivity/models/VirtualTableConfig.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/VirtualTable.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A Virtual Table represents an upstream table through a Connection. It does not copy every row into a Foundry dataset at creation. [Local procedure](../../../../v2/connectivity/index.md).

[Part 1](create.md)
