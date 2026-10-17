# v2.third_party_applications.Website.deploy


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Deploy a version of the Website.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.third_party_applications.ThirdPartyApplication.Website.deploy`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def deploy(self, third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid, *, version: third_party_applications_models.VersionVersion, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> third_party_applications_models.Website: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| third_party_application_rid | third_party_applications_models.ThirdPartyApplicationRid | required | An RID identifying a third-party application created in Developer Console. |
| version | third_party_applications_models.VersionVersion | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| DeployWebsitePermissionDenied | Could not deploy the Website. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/deploy'
```

**query_params**

```python
{}
```

**path_params**

```python
{'thirdPartyApplicationRid': third_party_application_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
third_party_applications_models.DeployWebsiteRequest(version=version)
```

**response_type**

```python
third_party_applications_models.Website
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'DeployWebsitePermissionDenied': third_party_applications_errors.DeployWebsitePermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `third_party_applications_models.Website`. Ordinary async return: `typing.Awaitable[third_party_applications_models.Website]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | third_party_applications_models.Website |
| sync_raw | ApiResponse[third_party_applications_models.Website] |
| sync_streaming | StreamingContextManager[third_party_applications_models.Website] |
| async_ordinary | typing.Awaitable[third_party_applications_models.Website] |
| async_raw | Awaitable[AsyncApiResponse[third_party_applications_models.Website]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[third_party_applications_models.Website]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.third_party_applications.errors.DeployWebsitePermissionDenied](../../../../models/v2/third_party_applications/errors/DeployWebsitePermissionDenied.md)
- [foundry_sdk.v2.third_party_applications.errors.DeployWebsitePermissionDeniedParameters](../../../../models/v2/third_party_applications/errors/DeployWebsitePermissionDeniedParameters.md)
- [foundry_sdk.v2.third_party_applications.models.DeployWebsiteRequest](../../../../models/v2/third_party_applications/models/DeployWebsiteRequest.md)
- [foundry_sdk.v2.third_party_applications.models.Subdomain](../../../../models/v2/third_party_applications/models/Subdomain.md)
- [foundry_sdk.v2.third_party_applications.models.ThirdPartyApplicationRid](../../../../models/v2/third_party_applications/models/ThirdPartyApplicationRid.md)
- [foundry_sdk.v2.third_party_applications.models.VersionVersion](../../../../models/v2/third_party_applications/models/VersionVersion.md)
- [foundry_sdk.v2.third_party_applications.models.Website](../../../../models/v2/third_party_applications/models/Website.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/third_party_applications/Website.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](deploy.md)
