# v2.models.ExperimentArtifactTable.parquet


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Read raw table data from experiment artifacts in Parquet format.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.Model.Experiment.ArtifactTable.parquet`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def parquet(self, model_rid: models_models.ModelRid, experiment_rid: models_models.ExperimentRid, experiment_artifact_table_name: models_models.ExperimentArtifactName, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.TableResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | Value shape and constraints are in its referenced local type definition. |
| experiment_rid | models_models.ExperimentRid | required | Value shape and constraints are in its referenced local type definition. |
| experiment_artifact_table_name | models_models.ExperimentArtifactName | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ExperimentArtifactNotFound | The requested artifact was not found in the experiment. |
| ModelExperimentNotFound | The requested experiment was not found or the user lacks permission to access it. |
| ParquetExperimentArtifactTablePermissionDenied | Could not parquet the ExperimentArtifactTable. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/{modelRid}/experiments/{experimentRid}/artifactTables/{experimentArtifactTableName}/parquet'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'modelRid': model_rid, 'experimentRid': experiment_rid, 'experimentArtifactTableName': experiment_artifact_table_name}
```

**header_params**

```python
{'Accept': 'application/octet-stream'}
```

**body**

```python
None
```

**response_type**

```python
bytes
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExperimentArtifactNotFound': models_errors.ExperimentArtifactNotFound, 'ModelExperimentNotFound': models_errors.ModelExperimentNotFound, 'ParquetExperimentArtifactTablePermissionDenied': models_errors.ParquetExperimentArtifactTablePermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'PARQUET_TABLE')
```

## Response modes

Ordinary sync return: `core.TableResponse`. Ordinary async return: `typing.Awaitable[core.TableResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.TableResponse |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[core.TableResponse] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.models.errors.ExperimentArtifactNotFound](../../../../models/v2/models/errors/ExperimentArtifactNotFound.md)
- [foundry_sdk.v2.models.errors.ExperimentArtifactNotFoundParameters](../../../../models/v2/models/errors/ExperimentArtifactNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.ModelExperimentNotFound](../../../../models/v2/models/errors/ModelExperimentNotFound.md)
- [foundry_sdk.v2.models.errors.ModelExperimentNotFoundParameters](../../../../models/v2/models/errors/ModelExperimentNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.ParquetExperimentArtifactTablePermissionDenied](../../../../models/v2/models/errors/ParquetExperimentArtifactTablePermissionDenied.md)
- [foundry_sdk.v2.models.errors.ParquetExperimentArtifactTablePermissionDeniedParameters](../../../../models/v2/models/errors/ParquetExperimentArtifactTablePermissionDeniedParameters.md)
- [foundry_sdk.v2.models.models.ExperimentArtifactName](../../../../models/v2/models/models/ExperimentArtifactName.md)
- [foundry_sdk.v2.models.models.ExperimentRid](../../../../models/v2/models/models/ExperimentRid.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ExperimentArtifactTable.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](parquet.md)
