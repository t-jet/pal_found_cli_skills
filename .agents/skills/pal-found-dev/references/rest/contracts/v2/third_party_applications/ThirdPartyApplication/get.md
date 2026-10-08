# v2.third_party_applications.ThirdPartyApplication.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the ThirdPartyApplication with the specified rid.

## SDK invocation contract

```python
def get(self, third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> third_party_applications_models.ThirdPartyApplication: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| third_party_application_rid | third_party_applications_models.ThirdPartyApplicationRid | required | An RID identifying a third-party application created in Developer Console. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ThirdPartyApplicationNotFound | The given ThirdPartyApplication could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/thirdPartyApplications/{thirdPartyApplicationRid}'
```

**query_params**

```python
{'preview': preview}
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
third_party_applications_models.ThirdPartyApplication
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ThirdPartyApplicationNotFound': third_party_applications_errors.ThirdPartyApplicationNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `third_party_applications_models.ThirdPartyApplication`. Ordinary async return: `typing.Awaitable[third_party_applications_models.ThirdPartyApplication]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | third_party_applications_models.ThirdPartyApplication |
| sync_raw | ApiResponse[third_party_applications_models.ThirdPartyApplication] |
| sync_streaming | StreamingContextManager[third_party_applications_models.ThirdPartyApplication] |
| async_ordinary | typing.Awaitable[third_party_applications_models.ThirdPartyApplication] |
| async_raw | Awaitable[AsyncApiResponse[third_party_applications_models.ThirdPartyApplication]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[third_party_applications_models.ThirdPartyApplication]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.third_party_applications.errors.ThirdPartyApplicationNotFound](../../../../models/v2/third_party_applications/errors/ThirdPartyApplicationNotFound.md)
- [foundry_sdk.v2.third_party_applications.errors.ThirdPartyApplicationNotFoundParameters](../../../../models/v2/third_party_applications/errors/ThirdPartyApplicationNotFoundParameters.md)
- [foundry_sdk.v2.third_party_applications.models.ThirdPartyApplication](../../../../models/v2/third_party_applications/models/ThirdPartyApplication.md)
- [foundry_sdk.v2.third_party_applications.models.ThirdPartyApplicationRid](../../../../models/v2/third_party_applications/models/ThirdPartyApplicationRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/third_party_applications/ThirdPartyApplication.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
