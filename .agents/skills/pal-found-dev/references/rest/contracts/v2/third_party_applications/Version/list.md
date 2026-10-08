# v2.third_party_applications.Version.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all Versions.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

## SDK invocation contract

```python
def list(self, third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[third_party_applications_models.Version]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| third_party_application_rid | third_party_applications_models.ThirdPartyApplicationRid | required | An RID identifying a third-party application created in Developer Console. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
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
'/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'thirdPartyApplicationRid': third_party_application_rid}
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
third_party_applications_models.ListVersionsResponse
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

Ordinary sync return: `core.ResourceIterator[third_party_applications_models.Version]`. Ordinary async return: `core.AsyncResourceIterator[third_party_applications_models.Version]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[third_party_applications_models.Version] |
| sync_raw | ApiResponse[third_party_applications_models.ListVersionsResponse] |
| sync_streaming | StreamingContextManager[third_party_applications_models.ListVersionsResponse] |
| async_ordinary | core.AsyncResourceIterator[third_party_applications_models.Version] |
| async_raw | Awaitable[AsyncApiResponse[third_party_applications_models.ListVersionsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[third_party_applications_models.ListVersionsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.third_party_applications.models.ListVersionsResponse](../../../../models/v2/third_party_applications/models/ListVersionsResponse.md)
- [foundry_sdk.v2.third_party_applications.models.ThirdPartyApplicationRid](../../../../models/v2/third_party_applications/models/ThirdPartyApplicationRid.md)
- [foundry_sdk.v2.third_party_applications.models.Version](../../../../models/v2/third_party_applications/models/Version.md)
- [foundry_sdk.v2.third_party_applications.models.VersionVersion](../../../../models/v2/third_party_applications/models/VersionVersion.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/third_party_applications/Version.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
