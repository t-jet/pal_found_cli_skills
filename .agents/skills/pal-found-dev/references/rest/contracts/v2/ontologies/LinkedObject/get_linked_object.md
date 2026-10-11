# v2.ontologies.LinkedObject.get_linked_object


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get a specific linked object that originates from another object.

If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.LinkedObject.get_linked_object`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_linked_object(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, primary_key: ontologies_models.PropertyValueEscapedString, link_type: ontologies_models.LinkTypeApiName, linked_object_primary_key: ontologies_models.PropertyValueEscapedString, *, branch: typing.Optional[core_models.FoundryBranch]=None, exclude_rid: typing.Optional[bool]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, select: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.OntologyObjectV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| primary_key | ontologies_models.PropertyValueEscapedString | required | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**. |
| link_type | ontologies_models.LinkTypeApiName | required | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**. |
| linked_object_primary_key | ontologies_models.PropertyValueEscapedString | required | The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the object set for multiple object types. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| exclude_rid | typing.Optional[bool] | None | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
| select | typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] | None | The properties of the object type that should be included in the response. Omit this parameter to get all the properties. |
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
'/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}'
```

**query_params**

```python
{'branch': branch, 'excludeRid': exclude_rid, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version, 'select': select}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type, 'primaryKey': primary_key, 'linkType': link_type, 'linkedObjectPrimaryKey': linked_object_primary_key}
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
ontologies_models.OntologyObjectV2
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

Ordinary sync return: `ontologies_models.OntologyObjectV2`. Ordinary async return: `typing.Awaitable[ontologies_models.OntologyObjectV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.OntologyObjectV2 |
| sync_raw | ApiResponse[ontologies_models.OntologyObjectV2] |
| sync_streaming | StreamingContextManager[ontologies_models.OntologyObjectV2] |
| async_ordinary | typing.Awaitable[ontologies_models.OntologyObjectV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.OntologyObjectV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.OntologyObjectV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](../../../../models/v2/ontologies/models/OntologyObjectV2.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueEscapedString](../../../../models/v2/ontologies/models/PropertyValueEscapedString.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApiName](../../../../models/v2/ontologies/models/SelectedPropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/LinkedObject.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_linked_object.md)
