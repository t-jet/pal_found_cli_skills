# v2.datasets.Dataset.put_schema


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Adds a schema on an existing dataset using a PUT request.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.put_schema`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def put_schema(self, dataset_rid: core_models.DatasetRid, *, schema: core_models.DatasetSchema, branch_name: typing.Optional[core_models.BranchName]=None, dataframe_reader: typing.Optional[datasets_models.DataframeReader]=None, end_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.GetDatasetSchemaResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| schema | core_models.DatasetSchema | required | The schema that will be added. |
| branch_name | typing.Optional[core_models.BranchName] | None | Value shape and constraints are in its referenced local type definition. |
| dataframe_reader | typing.Optional[datasets_models.DataframeReader] | None | The dataframe reader used for reading the dataset schema. Defaults to PARQUET. |
| end_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the end Transaction. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| DatasetViewNotFound | The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it. |
| InvalidSchema | The schema failed validations |
| PutDatasetSchemaPermissionDenied | Could not putSchema the Dataset. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/putSchema'
```

**query_params**

```python
{}
```

**path_params**

```python
{'datasetRid': dataset_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
datasets_models.PutDatasetSchemaRequest(branch_name=branch_name, dataframe_reader=dataframe_reader, end_transaction_rid=end_transaction_rid, schema_=schema)
```

**response_type**

```python
datasets_models.GetDatasetSchemaResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'DatasetViewNotFound': datasets_errors.DatasetViewNotFound, 'InvalidSchema': core_errors.InvalidSchema, 'PutDatasetSchemaPermissionDenied': datasets_errors.PutDatasetSchemaPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.GetDatasetSchemaResponse`. Ordinary async return: `typing.Awaitable[datasets_models.GetDatasetSchemaResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.GetDatasetSchemaResponse |
| sync_raw | ApiResponse[datasets_models.GetDatasetSchemaResponse] |
| sync_streaming | StreamingContextManager[datasets_models.GetDatasetSchemaResponse] |
| async_ordinary | typing.Awaitable[datasets_models.GetDatasetSchemaResponse] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.GetDatasetSchemaResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.GetDatasetSchemaResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.errors.InvalidSchema](../../../../models/v2/core/errors/InvalidSchema.md)
- [foundry_sdk.v2.core.errors.InvalidSchemaParameters](../../../../models/v2/core/errors/InvalidSchemaParameters.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CustomMetadata](../../../../models/v2/core/models/CustomMetadata.md)
- [foundry_sdk.v2.core.models.DatasetFieldSchema](../../../../models/v2/core/models/DatasetFieldSchema.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.DatasetSchema](../../../../models/v2/core/models/DatasetSchema.md)
- [foundry_sdk.v2.core.models.FieldName](../../../../models/v2/core/models/FieldName.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../../../models/v2/core/models/SchemaFieldType.md)
- [foundry_sdk.v2.core.models.VersionId](../../../../models/v2/core/models/VersionId.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetViewNotFound](../../../../models/v2/datasets/errors/DatasetViewNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetViewNotFoundParameters](../../../../models/v2/datasets/errors/DatasetViewNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.PutDatasetSchemaPermissionDenied](../../../../models/v2/datasets/errors/PutDatasetSchemaPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.PutDatasetSchemaPermissionDeniedParameters](../../../../models/v2/datasets/errors/PutDatasetSchemaPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.models.DataframeReader](../../../../models/v2/datasets/models/DataframeReader.md)
- [foundry_sdk.v2.datasets.models.GetDatasetSchemaResponse](../../../../models/v2/datasets/models/GetDatasetSchemaResponse.md)
- [foundry_sdk.v2.datasets.models.PutDatasetSchemaRequest](../../../../models/v2/datasets/models/PutDatasetSchemaRequest.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Dataset-2.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](put_schema.md)
