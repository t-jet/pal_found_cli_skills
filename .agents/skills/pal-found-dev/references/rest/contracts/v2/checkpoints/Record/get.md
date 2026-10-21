# v2.checkpoints.Record.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieve a single checkpoint record by id.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.checkpoints.Record.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, record_rid: checkpoints_models.RecordRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> checkpoints_models.Record: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| record_rid | checkpoints_models.RecordRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CheckpointRecordNotFound | The checkpoint record could not be found. |
| CheckpointRecordPermissionDenied | The caller does not have permission to access the checkpoint record. |
| RecordNotFound | The given Record could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/checkpoints/records/{recordRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'recordRid': record_rid}
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
checkpoints_models.Record
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CheckpointRecordNotFound': checkpoints_errors.CheckpointRecordNotFound, 'CheckpointRecordPermissionDenied': checkpoints_errors.CheckpointRecordPermissionDenied, 'RecordNotFound': checkpoints_errors.RecordNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `checkpoints_models.Record`. Ordinary async return: `typing.Awaitable[checkpoints_models.Record]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | checkpoints_models.Record |
| sync_raw | ApiResponse[checkpoints_models.Record] |
| sync_streaming | StreamingContextManager[checkpoints_models.Record] |
| async_ordinary | typing.Awaitable[checkpoints_models.Record] |
| async_raw | Awaitable[AsyncApiResponse[checkpoints_models.Record]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[checkpoints_models.Record]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.checkpoints.errors.CheckpointRecordNotFound](../../../../models/v2/checkpoints/errors/CheckpointRecordNotFound.md)
- [foundry_sdk.v2.checkpoints.errors.CheckpointRecordNotFoundParameters](../../../../models/v2/checkpoints/errors/CheckpointRecordNotFoundParameters.md)
- [foundry_sdk.v2.checkpoints.errors.CheckpointRecordPermissionDenied](../../../../models/v2/checkpoints/errors/CheckpointRecordPermissionDenied.md)
- [foundry_sdk.v2.checkpoints.errors.CheckpointRecordPermissionDeniedParameters](../../../../models/v2/checkpoints/errors/CheckpointRecordPermissionDeniedParameters.md)
- [foundry_sdk.v2.checkpoints.errors.RecordNotFound](../../../../models/v2/checkpoints/errors/RecordNotFound.md)
- [foundry_sdk.v2.checkpoints.errors.RecordNotFoundParameters](../../../../models/v2/checkpoints/errors/RecordNotFoundParameters.md)
- [foundry_sdk.v2.checkpoints.models.AcknowledgementJustification](../../../../models/v2/checkpoints/models/AcknowledgementJustification.md)
- [foundry_sdk.v2.checkpoints.models.ActingUser](../../../../models/v2/checkpoints/models/ActingUser.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsMetadata](../../../../models/v2/checkpoints/models/ApprovalsMetadata.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsSubtaskId](../../../../models/v2/checkpoints/models/ApprovalsSubtaskId.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsTaskId](../../../../models/v2/checkpoints/models/ApprovalsTaskId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointType](../../../../models/v2/checkpoints/models/CheckpointType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedActionType](../../../../models/v2/checkpoints/models/CheckpointedActionType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedGroup](../../../../models/v2/checkpoints/models/CheckpointedGroup.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIntervention](../../../../models/v2/checkpoints/models/CheckpointedIntervention.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIssue](../../../../models/v2/checkpoints/models/CheckpointedIssue.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedItem](../../../../models/v2/checkpoints/models/CheckpointedItem.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJob](../../../../models/v2/checkpoints/models/CheckpointedJob.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobSpecification](../../../../models/v2/checkpoints/models/CheckpointedJobSpecification.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModel](../../../../models/v2/checkpoints/models/CheckpointedLanguageModel.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelSession](../../../../models/v2/checkpoints/models/CheckpointedLanguageModelSession.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarketplaceProduct](../../../../models/v2/checkpoints/models/CheckpointedMarketplaceProduct.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarking](../../../../models/v2/checkpoints/models/CheckpointedMarking.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSet](../../../../models/v2/checkpoints/models/CheckpointedObjectSet.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetTypesProxy](../../../../models/v2/checkpoints/models/CheckpointedObjectSetTypesProxy.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntology](../../../../models/v2/checkpoints/models/CheckpointedOntology.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntologyWithObjectTypes](../../../../models/v2/checkpoints/models/CheckpointedOntologyWithObjectTypes.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPeeringJob](../../../../models/v2/checkpoints/models/CheckpointedPeeringJob.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipal](../../../../models/v2/checkpoints/models/CheckpointedPrincipal.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipalRole](../../../../models/v2/checkpoints/models/CheckpointedPrincipalRole.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResource](../../../../models/v2/checkpoints/models/CheckpointedResource.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResourceType](../../../../models/v2/checkpoints/models/CheckpointedResourceType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedRole](../../../../models/v2/checkpoints/models/CheckpointedRole.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedSchedule](../../../../models/v2/checkpoints/models/CheckpointedSchedule.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedToken](../../../../models/v2/checkpoints/models/CheckpointedToken.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedTokenType](../../../../models/v2/checkpoints/models/CheckpointedTokenType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeFormInput](../../../../models/v2/checkpoints/models/CheckpointedUserIntakeFormInput.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeSubmission](../../../../models/v2/checkpoints/models/CheckpointedUserIntakeSubmission.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedVersionedObjectSet](../../../../models/v2/checkpoints/models/CheckpointedVersionedObjectSet.md)
- [foundry_sdk.v2.checkpoints.models.ConfigRid](../../../../models/v2/checkpoints/models/ConfigRid.md)
- [foundry_sdk.v2.checkpoints.models.DropdownJustification](../../../../models/v2/checkpoints/models/DropdownJustification.md)
- [foundry_sdk.v2.checkpoints.models.DropdownSelection](../../../../models/v2/checkpoints/models/DropdownSelection.md)
- [foundry_sdk.v2.checkpoints.models.InteractionRid](../../../../models/v2/checkpoints/models/InteractionRid.md)
- [foundry_sdk.v2.checkpoints.models.Justification](../../../../models/v2/checkpoints/models/Justification.md)
- [foundry_sdk.v2.checkpoints.models.NamespaceRid](../../../../models/v2/checkpoints/models/NamespaceRid.md)
- [foundry_sdk.v2.checkpoints.models.OrganizationRid](../../../../models/v2/checkpoints/models/OrganizationRid.md)
- [foundry_sdk.v2.checkpoints.models.ProjectRid](../../../../models/v2/checkpoints/models/ProjectRid.md)
- [foundry_sdk.v2.checkpoints.models.ReauthenticationJustification](../../../../models/v2/checkpoints/models/ReauthenticationJustification.md)
- [foundry_sdk.v2.checkpoints.models.Record](../../../../models/v2/checkpoints/models/Record.md)
- [foundry_sdk.v2.checkpoints.models.RecordCreatedAt](../../../../models/v2/checkpoints/models/RecordCreatedAt.md)
- [foundry_sdk.v2.checkpoints.models.RecordRid](../../../../models/v2/checkpoints/models/RecordRid.md)
- [foundry_sdk.v2.checkpoints.models.RedactableString](../../../../models/v2/checkpoints/models/RedactableString.md)
- [foundry_sdk.v2.checkpoints.models.RedactionType](../../../../models/v2/checkpoints/models/RedactionType.md)
- [foundry_sdk.v2.checkpoints.models.ResponseJustification](../../../../models/v2/checkpoints/models/ResponseJustification.md)
- [foundry_sdk.v2.checkpoints.models.Scope](../../../../models/v2/checkpoints/models/Scope.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/checkpoints/Record.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
