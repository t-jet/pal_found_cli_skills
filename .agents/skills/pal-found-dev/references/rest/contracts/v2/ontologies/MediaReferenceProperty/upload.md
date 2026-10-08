# v2.ontologies.MediaReferenceProperty.upload


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Uploads a media item to the media set which backs the specified property.  The property must be backed by a single media set and branch, otherwise an error will be thrown.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

## SDK invocation contract

```python
def upload(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, property: ontologies_models.PropertyApiName, body: bytes, *, media_item_path: typing.Optional[core_models.MediaItemPath]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core_models.MediaReference: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| property | ontologies_models.PropertyApiName | required | The API name of the media reference property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint. |
| body | bytes | required | Body of the request |
| media_item_path | typing.Optional[core_models.MediaItemPath] | None | A path for the media item within its backing media set. Required if the backing media set requires paths. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
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
'/v2/ontologies/{ontology}/objectTypes/{objectType}/media/{property}/upload'
```

**query_params**

```python
{'mediaItemPath': media_item_path, 'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type, 'property': property}
```

**header_params**

```python
{'Content-Type': '*/*', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
core_models.MediaReference
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

Ordinary sync return: `core_models.MediaReference`. Ordinary async return: `typing.Awaitable[core_models.MediaReference]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core_models.MediaReference |
| sync_raw | ApiResponse[core_models.MediaReference] |
| sync_streaming | StreamingContextManager[core_models.MediaReference] |
| async_ordinary | typing.Awaitable[core_models.MediaReference] |
| async_raw | Awaitable[AsyncApiResponse[core_models.MediaReference]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[core_models.MediaReference]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.MediaItemPath](../../../../models/v2/core/models/MediaItemPath.md)
- [foundry_sdk.v2.core.models.MediaItemReadToken](../../../../models/v2/core/models/MediaItemReadToken.md)
- [foundry_sdk.v2.core.models.MediaItemRid](../../../../models/v2/core/models/MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaReference](../../../../models/v2/core/models/MediaReference.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.MediaSetViewItem](../../../../models/v2/core/models/MediaSetViewItem.md)
- [foundry_sdk.v2.core.models.MediaSetViewItemWrapper](../../../../models/v2/core/models/MediaSetViewItemWrapper.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../../../models/v2/core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.core.models.MediaType](../../../../models/v2/core/models/MediaType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.Reference](../../../../models/v2/core/models/Reference.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/MediaReferenceProperty.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](upload.md)
