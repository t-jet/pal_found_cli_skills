# v2.datasets.Dataset.get_schema_batch


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Fetch schemas for multiple datasets in a single request. Datasets not found
or inaccessible to the user will be omitted from the response.


The maximum batch size for this endpoint is 1000.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.get_schema_batch`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_schema_batch(self, body: typing_extensions.Annotated[typing.List[datasets_models.GetSchemaDatasetsBatchRequestElement], annotated_types.Len(min_length=1, max_length=1000)], *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.GetSchemaDatasetsBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| body | typing_extensions.Annotated[typing.List[datasets_models.GetSchemaDatasetsBatchRequestElement], annotated_types.Len(min_length=1, max_length=1000)] | required | Body of the request |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/datasets/getSchemaBatch'
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
body
```

**response_type**

```python
datasets_models.GetSchemaDatasetsBatchResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.GetSchemaDatasetsBatchResponse`. Ordinary async return: `typing.Awaitable[datasets_models.GetSchemaDatasetsBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.GetSchemaDatasetsBatchResponse |
| sync_raw | ApiResponse[datasets_models.GetSchemaDatasetsBatchResponse] |
| sync_streaming | StreamingContextManager[datasets_models.GetSchemaDatasetsBatchResponse] |
| async_ordinary | typing.Awaitable[datasets_models.GetSchemaDatasetsBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.GetSchemaDatasetsBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.GetSchemaDatasetsBatchResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CustomMetadata](../../../../models/v2/core/models/CustomMetadata.md)
- [foundry_sdk.v2.core.models.DatasetFieldSchema](../../../../models/v2/core/models/DatasetFieldSchema.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.DatasetSchema](../../../../models/v2/core/models/DatasetSchema.md)
- [foundry_sdk.v2.core.models.FieldName](../../../../models/v2/core/models/FieldName.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../../../models/v2/core/models/SchemaFieldType.md)
- [foundry_sdk.v2.core.models.VersionId](../../../../models/v2/core/models/VersionId.md)
- [foundry_sdk.v2.datasets.models.GetDatasetSchemaResponse](../../../../models/v2/datasets/models/GetDatasetSchemaResponse.md)
- [foundry_sdk.v2.datasets.models.GetSchemaDatasetsBatchRequestElement](../../../../models/v2/datasets/models/GetSchemaDatasetsBatchRequestElement.md)
- [foundry_sdk.v2.datasets.models.GetSchemaDatasetsBatchResponse](../../../../models/v2/datasets/models/GetSchemaDatasetsBatchResponse.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_schema_batch.md)
