# v2.admin.Marking.parse_classifications


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Parses classification marking strings (e.g. 'S//NF') into their component marking IDs. Strings that cannot be parsed are returned in 'errors' with a human-readable message.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Marking.parse_classifications`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def parse_classifications(self, *, classification_strings: typing.List[str], preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ParseClassificationsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| classification_strings | typing.List[str] | required | Classification strings to parse, e.g. 'S//NF'. The API requires 1–1000 submitted entries. Duplicates count toward this limit, although each distinct string is parsed once. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

The API returns `MissingBatchRequest` for an empty list and
`BatchRequestSizeExceededLimit` for more than 1000 entries. SDK 1.101.0 forwards
both requests without checking the list length. Validate the count before calling
the SDK. These are API-level boundary errors, separate from the named errors in
the SDK method's `throwable_errors` mapping below.

[Official Parse Classifications API reference](https://www.palantir.com/docs/foundry/api/v2/admin-v2-resources/markings/parse-classifications).

## SDK-declared operation errors

| Error | Meaning |
| --- | --- |
| CbacUnavailable | CBAC is not available. |
| ParseClassificationsPermissionDenied | The provided token does not have permission to parse the given classification strings. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/markings/parseClassifications'
```

**query_params**

```python
{'preview': preview}
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
admin_models.ParseClassificationsRequest(classification_strings=classification_strings)
```

**response_type**

```python
admin_models.ParseClassificationsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CbacUnavailable': admin_errors.CbacUnavailable, 'ParseClassificationsPermissionDenied': admin_errors.ParseClassificationsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ParseClassificationsResponse`. Ordinary async return: `typing.Awaitable[admin_models.ParseClassificationsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ParseClassificationsResponse |
| sync_raw | ApiResponse[admin_models.ParseClassificationsResponse] |
| sync_streaming | StreamingContextManager[admin_models.ParseClassificationsResponse] |
| async_ordinary | typing.Awaitable[admin_models.ParseClassificationsResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ParseClassificationsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ParseClassificationsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.CbacUnavailable](../../../../models/v2/admin/errors/CbacUnavailable.md)
- [foundry_sdk.v2.admin.errors.CbacUnavailableParameters](../../../../models/v2/admin/errors/CbacUnavailableParameters.md)
- [foundry_sdk.v2.admin.errors.ParseClassificationsPermissionDenied](../../../../models/v2/admin/errors/ParseClassificationsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ParseClassificationsPermissionDeniedParameters](../../../../models/v2/admin/errors/ParseClassificationsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.ParseClassificationsRequest](../../../../models/v2/admin/models/ParseClassificationsRequest.md)
- [foundry_sdk.v2.admin.models.ParseClassificationsResponse](../../../../models/v2/admin/models/ParseClassificationsResponse.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Marking.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](parse_classifications.md)
