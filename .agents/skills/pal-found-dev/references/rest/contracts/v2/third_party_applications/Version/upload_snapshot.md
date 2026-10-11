# v2.third_party_applications.Version.upload_snapshot


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.third_party_applications.ThirdPartyApplication.Website.Version.upload_snapshot`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def upload_snapshot(self, third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid, body: bytes, *, version: third_party_applications_models.VersionVersion, preview: typing.Optional[core_models.PreviewMode]=None, snapshot_identifier: typing.Optional[str]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> third_party_applications_models.Version: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| third_party_application_rid | third_party_applications_models.ThirdPartyApplicationRid | required | An RID identifying a third-party application created in Developer Console. |
| body | bytes | required | The zip file that contains the contents of your application. For more information, refer to the [documentation](../../../../../applications/osdk.md) user documentation. |
| version | third_party_applications_models.VersionVersion | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| snapshot_identifier | typing.Optional[str] | None | The identifier of the snapshot. If the identifier follows the format `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>`, PR preview for such identifier will be accessible from foundry code repositories. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| UploadSnapshotVersionPermissionDenied | Could not uploadSnapshot the Version. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/uploadSnapshot'
```

**query_params**

```python
{'version': version, 'preview': preview, 'snapshotIdentifier': snapshot_identifier}
```

**path_params**

```python
{'thirdPartyApplicationRid': third_party_application_rid}
```

**header_params**

```python
{'Content-Type': 'application/octet-stream', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
third_party_applications_models.Version
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'UploadSnapshotVersionPermissionDenied': third_party_applications_errors.UploadSnapshotVersionPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `third_party_applications_models.Version`. Ordinary async return: `typing.Awaitable[third_party_applications_models.Version]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | third_party_applications_models.Version |
| sync_raw | ApiResponse[third_party_applications_models.Version] |
| sync_streaming | StreamingContextManager[third_party_applications_models.Version] |
| async_ordinary | typing.Awaitable[third_party_applications_models.Version] |
| async_raw | Awaitable[AsyncApiResponse[third_party_applications_models.Version]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[third_party_applications_models.Version]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.third_party_applications.errors.UploadSnapshotVersionPermissionDenied](../../../../models/v2/third_party_applications/errors/UploadSnapshotVersionPermissionDenied.md)
- [foundry_sdk.v2.third_party_applications.errors.UploadSnapshotVersionPermissionDeniedParameters](../../../../models/v2/third_party_applications/errors/UploadSnapshotVersionPermissionDeniedParameters.md)
- [foundry_sdk.v2.third_party_applications.models.ThirdPartyApplicationRid](../../../../models/v2/third_party_applications/models/ThirdPartyApplicationRid.md)
- [foundry_sdk.v2.third_party_applications.models.Version](../../../../models/v2/third_party_applications/models/Version.md)
- [foundry_sdk.v2.third_party_applications.models.VersionVersion](../../../../models/v2/third_party_applications/models/VersionVersion.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/third_party_applications/Version.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- The upload body is a ZIP artifact for the selected application version; validate its required manifest and files before deployment. [Local procedure](../../../../../applications/osdk.md).

[Part 1](upload_snapshot.md)
