# v2.connectivity.TableImport.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all table imports defined for this connection.
Only table imports that the user has permissions to view will be returned.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.TableImport.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, connection_rid: connectivity_models.ConnectionRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[connectivity_models.TableImport]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionNotFound | The given Connection could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/tableImports'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
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
connectivity_models.ListTableImportsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ConnectionNotFound': connectivity_errors.ConnectionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[connectivity_models.TableImport]`. Ordinary async return: `core.AsyncResourceIterator[connectivity_models.TableImport]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[connectivity_models.TableImport] |
| sync_raw | ApiResponse[connectivity_models.ListTableImportsResponse] |
| sync_streaming | StreamingContextManager[connectivity_models.ListTableImportsResponse] |
| async_ordinary | core.AsyncResourceIterator[connectivity_models.TableImport] |
| async_raw | Awaitable[AsyncApiResponse[connectivity_models.ListTableImportsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[connectivity_models.ListTableImportsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFound](../../../../models/v2/connectivity/errors/ConnectionNotFound.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFoundParameters](../../../../models/v2/connectivity/errors/ConnectionNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.DatabricksTableImportConfig](../../../../models/v2/connectivity/models/DatabricksTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.DateColumnInitialIncrementalState](../../../../models/v2/connectivity/models/DateColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.DecimalColumnInitialIncrementalState](../../../../models/v2/connectivity/models/DecimalColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.IntegerColumnInitialIncrementalState](../../../../models/v2/connectivity/models/IntegerColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.JdbcTableImportConfig](../../../../models/v2/connectivity/models/JdbcTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ListTableImportsResponse](../../../../models/v2/connectivity/models/ListTableImportsResponse.md)
- [foundry_sdk.v2.connectivity.models.LongColumnInitialIncrementalState](../../../../models/v2/connectivity/models/LongColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.MicrosoftAccessTableImportConfig](../../../../models/v2/connectivity/models/MicrosoftAccessTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.MicrosoftSqlServerTableImportConfig](../../../../models/v2/connectivity/models/MicrosoftSqlServerTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.OracleTableImportConfig](../../../../models/v2/connectivity/models/OracleTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.PostgreSqlTableImportConfig](../../../../models/v2/connectivity/models/PostgreSqlTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeTableImportConfig](../../../../models/v2/connectivity/models/SnowflakeTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.StringColumnInitialIncrementalState](../../../../models/v2/connectivity/models/StringColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.TableImport](../../../../models/v2/connectivity/models/TableImport.md)
- [foundry_sdk.v2.connectivity.models.TableImportAllowSchemaChanges](../../../../models/v2/connectivity/models/TableImportAllowSchemaChanges.md)
- [foundry_sdk.v2.connectivity.models.TableImportConfig](../../../../models/v2/connectivity/models/TableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.TableImportDisplayName](../../../../models/v2/connectivity/models/TableImportDisplayName.md)
- [foundry_sdk.v2.connectivity.models.TableImportInitialIncrementalState](../../../../models/v2/connectivity/models/TableImportInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.TableImportMode](../../../../models/v2/connectivity/models/TableImportMode.md)
- [foundry_sdk.v2.connectivity.models.TableImportQuery](../../../../models/v2/connectivity/models/TableImportQuery.md)
- [foundry_sdk.v2.connectivity.models.TableImportRid](../../../../models/v2/connectivity/models/TableImportRid.md)
- [foundry_sdk.v2.connectivity.models.TimestampColumnInitialIncrementalState](../../../../models/v2/connectivity/models/TimestampColumnInitialIncrementalState.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/TableImport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
