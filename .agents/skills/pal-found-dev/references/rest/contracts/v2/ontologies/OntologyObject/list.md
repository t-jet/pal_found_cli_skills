# v2.ontologies.OntologyObject.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the objects for the given Ontology and object type.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyObject.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, exclude_rid: typing.Optional[bool]=None, order_by: typing.Optional[ontologies_models.OrderBy]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]]=None, snapshot: typing.Optional[bool]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.OntologyObjectV2]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to list objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| exclude_rid | typing.Optional[bool] | None | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2. |
| order_by | typing.Optional[ontologies_models.OrderBy] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](../../../../client-behavior.md) for details. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
| select | typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] | None | The properties of the object type that should be included in the response. Omit this parameter to get all the properties. |
| snapshot | typing.Optional[bool] | None | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/ontologies/{ontology}/objects/{objectType}'
```

**query_params**

```python
{'branch': branch, 'excludeRid': exclude_rid, 'orderBy': order_by, 'pageSize': page_size, 'pageToken': page_token, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version, 'select': select, 'snapshot': snapshot}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type}
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
ontologies_models.ListObjectsResponseV2
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
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[ontologies_models.OntologyObjectV2]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.OntologyObjectV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.OntologyObjectV2] |
| sync_raw | ApiResponse[ontologies_models.ListObjectsResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.ListObjectsResponseV2] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.OntologyObjectV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListObjectsResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListObjectsResponseV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.TotalCount](../../../../models/v2/core/models/TotalCount.md)
- [foundry_sdk.v2.ontologies.models.ListObjectsResponseV2](../../../../models/v2/ontologies/models/ListObjectsResponseV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](../../../../models/v2/ontologies/models/OntologyObjectV2.md)
- [foundry_sdk.v2.ontologies.models.OrderBy](../../../../models/v2/ontologies/models/OrderBy.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApiName](../../../../models/v2/ontologies/models/SelectedPropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyObject.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
