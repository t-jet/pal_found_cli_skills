# v2.ontologies.TimeSeriesValueBankProperty.stream_values


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Stream all of the points of a time series property (this includes geotime series references).

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.TimeSeriesValueBankProperty.stream_values`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def stream_values(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, primary_key: ontologies_models.PropertyValueEscapedString, property: ontologies_models.PropertyApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, range: typing.Optional[ontologies_models.TimeRange]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> bytes: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| primary_key | ontologies_models.PropertyValueEscapedString | required | The primary key of the object with the time series property. |
| property | ontologies_models.PropertyApiName | required | The API name of the time series backed property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to read from. If not specified, the default branch will be used. |
| range | typing.Optional[ontologies_models.TimeRange] | None | Value shape and constraints are in its referenced local type definition. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
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
'/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamValues'
```

**query_params**

```python
{'branch': branch, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type, 'primaryKey': primary_key, 'property': property}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': '*/*'}
```

**body**

```python
ontologies_models.StreamTimeSeriesValuesRequest(range=range)
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
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `bytes`. Ordinary async return: `typing.Awaitable[bytes]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | bytes |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[bytes] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.ontologies.models.AbsoluteTimeRange](../../../../models/v2/ontologies/models/AbsoluteTimeRange.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueEscapedString](../../../../models/v2/ontologies/models/PropertyValueEscapedString.md)
- [foundry_sdk.v2.ontologies.models.RelativeTime](../../../../models/v2/ontologies/models/RelativeTime.md)
- [foundry_sdk.v2.ontologies.models.RelativeTimeRange](../../../../models/v2/ontologies/models/RelativeTimeRange.md)
- [foundry_sdk.v2.ontologies.models.RelativeTimeRelation](../../../../models/v2/ontologies/models/RelativeTimeRelation.md)
- [foundry_sdk.v2.ontologies.models.RelativeTimeSeriesTimeUnit](../../../../models/v2/ontologies/models/RelativeTimeSeriesTimeUnit.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.StreamTimeSeriesValuesRequest](../../../../models/v2/ontologies/models/StreamTimeSeriesValuesRequest.md)
- [foundry_sdk.v2.ontologies.models.TimeRange](../../../../models/v2/ontologies/models/TimeRange.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/TimeSeriesValueBankProperty.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](stream_values.md)
