# v2.connectivity.TableImport.replace


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the TableImport with the specified rid.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.TableImport.replace`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def replace(self, connection_rid: connectivity_models.ConnectionRid, table_import_rid: connectivity_models.TableImportRid, *, config: connectivity_models.ReplaceTableImportRequestTableImportConfig, display_name: connectivity_models.TableImportDisplayName, import_mode: connectivity_models.TableImportMode, allow_schema_changes: typing.Optional[connectivity_models.TableImportAllowSchemaChanges]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.TableImport: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| table_import_rid | connectivity_models.TableImportRid | required | Value shape and constraints are in its referenced local type definition. |
| config | connectivity_models.ReplaceTableImportRequestTableImportConfig | required | Value shape and constraints are in its referenced local type definition. |
| display_name | connectivity_models.TableImportDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| import_mode | connectivity_models.TableImportMode | required | Value shape and constraints are in its referenced local type definition. |
| allow_schema_changes | typing.Optional[connectivity_models.TableImportAllowSchemaChanges] | None | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ConnectionDetailsNotDetermined | Details of the connection (such as which types of import it supports) could not be determined. |
| ConnectionNotFound | The given Connection could not be found. |
| ReplaceTableImportPermissionDenied | Could not replace the TableImport. |
| TableImportNotFound | The given TableImport could not be found. |
| TableImportNotSupportedForConnection | The specified connection does not support creating or replacing a table import with the specified config. |
| TableImportTypeNotSupported | The specified table import type is not yet supported in the Platform API. |

## Wire request

**method**

```python
'PUT'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
connectivity_models.ReplaceTableImportRequest(import_mode=import_mode, display_name=display_name, allow_schema_changes=allow_schema_changes, config=config)
```

**response_type**

```python
connectivity_models.TableImport
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ConnectionDetailsNotDetermined': connectivity_errors.ConnectionDetailsNotDetermined, 'ConnectionNotFound': connectivity_errors.ConnectionNotFound, 'ReplaceTableImportPermissionDenied': connectivity_errors.ReplaceTableImportPermissionDenied, 'TableImportNotFound': connectivity_errors.TableImportNotFound, 'TableImportNotSupportedForConnection': connectivity_errors.TableImportNotSupportedForConnection, 'TableImportTypeNotSupported': connectivity_errors.TableImportTypeNotSupported}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `connectivity_models.TableImport`. Ordinary async return: `typing.Awaitable[connectivity_models.TableImport]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | connectivity_models.TableImport |
| sync_raw | ApiResponse[connectivity_models.TableImport] |
| sync_streaming | StreamingContextManager[connectivity_models.TableImport] |
| async_ordinary | typing.Awaitable[connectivity_models.TableImport] |
| async_raw | Awaitable[AsyncApiResponse[connectivity_models.TableImport]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[connectivity_models.TableImport]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionDetailsNotDetermined](../../../../models/v2/connectivity/errors/ConnectionDetailsNotDetermined.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionDetailsNotDeterminedParameters](../../../../models/v2/connectivity/errors/ConnectionDetailsNotDeterminedParameters.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFound](../../../../models/v2/connectivity/errors/ConnectionNotFound.md)
- [foundry_sdk.v2.connectivity.errors.ConnectionNotFoundParameters](../../../../models/v2/connectivity/errors/ConnectionNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.errors.ReplaceTableImportPermissionDenied](../../../../models/v2/connectivity/errors/ReplaceTableImportPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.ReplaceTableImportPermissionDeniedParameters](../../../../models/v2/connectivity/errors/ReplaceTableImportPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.errors.TableImportNotFound](../../../../models/v2/connectivity/errors/TableImportNotFound.md)
- [foundry_sdk.v2.connectivity.errors.TableImportNotFoundParameters](../../../../models/v2/connectivity/errors/TableImportNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.errors.TableImportNotSupportedForConnection](../../../../models/v2/connectivity/errors/TableImportNotSupportedForConnection.md)
- [foundry_sdk.v2.connectivity.errors.TableImportNotSupportedForConnectionParameters](../../../../models/v2/connectivity/errors/TableImportNotSupportedForConnectionParameters.md)
- [foundry_sdk.v2.connectivity.errors.TableImportTypeNotSupported](../../../../models/v2/connectivity/errors/TableImportTypeNotSupported.md)
- [foundry_sdk.v2.connectivity.errors.TableImportTypeNotSupportedParameters](../../../../models/v2/connectivity/errors/TableImportTypeNotSupportedParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.DatabricksTableImportConfig](../../../../models/v2/connectivity/models/DatabricksTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.DateColumnInitialIncrementalState](../../../../models/v2/connectivity/models/DateColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.DecimalColumnInitialIncrementalState](../../../../models/v2/connectivity/models/DecimalColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.IntegerColumnInitialIncrementalState](../../../../models/v2/connectivity/models/IntegerColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.JdbcTableImportConfig](../../../../models/v2/connectivity/models/JdbcTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.LongColumnInitialIncrementalState](../../../../models/v2/connectivity/models/LongColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.MicrosoftAccessTableImportConfig](../../../../models/v2/connectivity/models/MicrosoftAccessTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.MicrosoftSqlServerTableImportConfig](../../../../models/v2/connectivity/models/MicrosoftSqlServerTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.OracleTableImportConfig](../../../../models/v2/connectivity/models/OracleTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.PostgreSqlTableImportConfig](../../../../models/v2/connectivity/models/PostgreSqlTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequest](../../../../models/v2/connectivity/models/ReplaceTableImportRequest.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestDatabricksTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestDatabricksTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestJdbcTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestJdbcTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestMicrosoftAccessTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestMicrosoftAccessTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestOracleTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestOracleTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestPostgreSqlTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestPostgreSqlTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestSnowflakeTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestSnowflakeTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestTableImportConfig](../../../../models/v2/connectivity/models/ReplaceTableImportRequestTableImportConfig.md)
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

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/TableImport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
