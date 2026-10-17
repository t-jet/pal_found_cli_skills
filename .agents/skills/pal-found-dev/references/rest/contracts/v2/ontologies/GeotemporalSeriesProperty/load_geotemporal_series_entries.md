# v2.ontologies.GeotemporalSeriesProperty.load_geotemporal_series_entries


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Load the geotemporal series entries for a given object's geotemporal series reference property within the
specified time range.

Each entry in the response is a map of property names to values, following the same structure as
`OntologyObjectV2`. Use the `additionalProperties` field in the request to control which properties are included
in each entry depending on the underlying geotemporal integration.

Results are paginated. Use the `nextPageToken` from the response to retrieve subsequent pages.

:::callout{theme=warning title=Warning}
  Geotemporal series integrations with only "dataset archive" enabled are not supported.
:::

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.GeotemporalSeriesProperty.load_geotemporal_series_entries`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def load_geotemporal_series_entries(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, primary_key: ontologies_models.PropertyValueEscapedString, property: ontologies_models.PropertyApiName, *, additional_properties: typing.List[ontologies_models.SelectedPropertyApiName], range: ontologies_models.AbsoluteTimeRange, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.LoadGeotemporalSeriesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| primary_key | ontologies_models.PropertyValueEscapedString | required | The primary key of the object with the geotemporal series property. |
| property | ontologies_models.PropertyApiName | required | The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint. |
| additional_properties | typing.List[ontologies_models.SelectedPropertyApiName] | required | The additional property API names to include in each entry. The "time" and "position" properties are always included and do not need to be specified here. Use this to request additional geotemporal series metadata properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal integration will be omitted from the response entries. |
| range | ontologies_models.AbsoluteTimeRange | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package RID of the generated SDK. |
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
'/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{property}/loadEntries'
```

**query_params**

```python
{'preview': preview, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type, 'primaryKey': primary_key, 'property': property}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.LoadGeotemporalSeriesRequest(range=range, additional_properties=additional_properties, page_token=page_token, page_size=page_size)
```

**response_type**

```python
ontologies_models.LoadGeotemporalSeriesResponse
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

Ordinary sync return: `ontologies_models.LoadGeotemporalSeriesResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.LoadGeotemporalSeriesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.LoadGeotemporalSeriesResponse |
| sync_raw | ApiResponse[ontologies_models.LoadGeotemporalSeriesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.LoadGeotemporalSeriesResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.LoadGeotemporalSeriesResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.LoadGeotemporalSeriesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.LoadGeotemporalSeriesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.AbsoluteTimeRange](../../../../models/v2/ontologies/models/AbsoluteTimeRange.md)
- [foundry_sdk.v2.ontologies.models.GeotemporalSeriesEntry](../../../../models/v2/ontologies/models/GeotemporalSeriesEntry.md)
- [foundry_sdk.v2.ontologies.models.LoadGeotemporalSeriesRequest](../../../../models/v2/ontologies/models/LoadGeotemporalSeriesRequest.md)
- [foundry_sdk.v2.ontologies.models.LoadGeotemporalSeriesResponse](../../../../models/v2/ontologies/models/LoadGeotemporalSeriesResponse.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueEscapedString](../../../../models/v2/ontologies/models/PropertyValueEscapedString.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApiName](../../../../models/v2/ontologies/models/SelectedPropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/GeotemporalSeriesProperty.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](load_geotemporal_series_entries.md)
