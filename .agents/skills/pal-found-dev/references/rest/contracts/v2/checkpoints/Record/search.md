# v2.checkpoints.Record.search


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Search for checkpoint records.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.checkpoints.Record.search`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def search(self, *, where: checkpoints_models.SearchCheckpointRecordsRequest, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, sort_direction: typing.Optional[checkpoints_models.SortDirection]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> checkpoints_models.SearchCheckpointRecordsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| where | checkpoints_models.SearchCheckpointRecordsRequest | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size for the search request. If no value is provided, a default of `100` will be used. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| sort_direction | typing.Optional[checkpoints_models.SortDirection] | None | Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC). |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| SearchRecordsPermissionDenied | Could not search the Record. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/checkpoints/records/search'
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
checkpoints_models.SearchRecordsRequest(where=where, page_token=page_token, page_size=page_size, sort_direction=sort_direction)
```

**response_type**

```python
checkpoints_models.SearchCheckpointRecordsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'SearchRecordsPermissionDenied': checkpoints_errors.SearchRecordsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `checkpoints_models.SearchCheckpointRecordsResponse`. Ordinary async return: `typing.Awaitable[checkpoints_models.SearchCheckpointRecordsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | checkpoints_models.SearchCheckpointRecordsResponse |
| sync_raw | ApiResponse[checkpoints_models.SearchCheckpointRecordsResponse] |
| sync_streaming | StreamingContextManager[checkpoints_models.SearchCheckpointRecordsResponse] |
| async_ordinary | typing.Awaitable[checkpoints_models.SearchCheckpointRecordsResponse] |
| async_raw | Awaitable[AsyncApiResponse[checkpoints_models.SearchCheckpointRecordsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[checkpoints_models.SearchCheckpointRecordsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.checkpoints.errors.SearchRecordsPermissionDenied](../../../../models/v2/checkpoints/errors/SearchRecordsPermissionDenied.md)
- [foundry_sdk.v2.checkpoints.errors.SearchRecordsPermissionDeniedParameters](../../../../models/v2/checkpoints/errors/SearchRecordsPermissionDeniedParameters.md)
- [foundry_sdk.v2.checkpoints.models.AcknowledgementJustification](../../../../models/v2/checkpoints/models/AcknowledgementJustification.md)
- [foundry_sdk.v2.checkpoints.models.ActingUser](../../../../models/v2/checkpoints/models/ActingUser.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsMetadata](../../../../models/v2/checkpoints/models/ApprovalsMetadata.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsSubtaskId](../../../../models/v2/checkpoints/models/ApprovalsSubtaskId.md)
- [foundry_sdk.v2.checkpoints.models.ApprovalsTaskId](../../../../models/v2/checkpoints/models/ApprovalsTaskId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointType](../../../../models/v2/checkpoints/models/CheckpointType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedActionType](../../../../models/v2/checkpoints/models/CheckpointedActionType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedActionTypeRid](../../../../models/v2/checkpoints/models/CheckpointedActionTypeRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedGroup](../../../../models/v2/checkpoints/models/CheckpointedGroup.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedGroupId](../../../../models/v2/checkpoints/models/CheckpointedGroupId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIntervention](../../../../models/v2/checkpoints/models/CheckpointedIntervention.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedInterventionRid](../../../../models/v2/checkpoints/models/CheckpointedInterventionRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIssue](../../../../models/v2/checkpoints/models/CheckpointedIssue.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedIssueRid](../../../../models/v2/checkpoints/models/CheckpointedIssueRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedItem](../../../../models/v2/checkpoints/models/CheckpointedItem.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedItemId](../../../../models/v2/checkpoints/models/CheckpointedItemId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJob](../../../../models/v2/checkpoints/models/CheckpointedJob.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobRid](../../../../models/v2/checkpoints/models/CheckpointedJobRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobSpecRid](../../../../models/v2/checkpoints/models/CheckpointedJobSpecRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedJobSpecification](../../../../models/v2/checkpoints/models/CheckpointedJobSpecification.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModel](../../../../models/v2/checkpoints/models/CheckpointedLanguageModel.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelRid](../../../../models/v2/checkpoints/models/CheckpointedLanguageModelRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelSession](../../../../models/v2/checkpoints/models/CheckpointedLanguageModelSession.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedLanguageModelSessionRid](../../../../models/v2/checkpoints/models/CheckpointedLanguageModelSessionRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarketplaceProduct](../../../../models/v2/checkpoints/models/CheckpointedMarketplaceProduct.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarketplaceProductId](../../../../models/v2/checkpoints/models/CheckpointedMarketplaceProductId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarking](../../../../models/v2/checkpoints/models/CheckpointedMarking.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedMarkingId](../../../../models/v2/checkpoints/models/CheckpointedMarkingId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSet](../../../../models/v2/checkpoints/models/CheckpointedObjectSet.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetTypesProxy](../../../../models/v2/checkpoints/models/CheckpointedObjectSetTypesProxy.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetTypesProxyRids](../../../../models/v2/checkpoints/models/CheckpointedObjectSetTypesProxyRids.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedObjectSetVersionedRid](../../../../models/v2/checkpoints/models/CheckpointedObjectSetVersionedRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntology](../../../../models/v2/checkpoints/models/CheckpointedOntology.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedOntologyWithObjectTypes](../../../../models/v2/checkpoints/models/CheckpointedOntologyWithObjectTypes.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPeeringJob](../../../../models/v2/checkpoints/models/CheckpointedPeeringJob.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPeeringJobId](../../../../models/v2/checkpoints/models/CheckpointedPeeringJobId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipal](../../../../models/v2/checkpoints/models/CheckpointedPrincipal.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipalId](../../../../models/v2/checkpoints/models/CheckpointedPrincipalId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedPrincipalRole](../../../../models/v2/checkpoints/models/CheckpointedPrincipalRole.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResource](../../../../models/v2/checkpoints/models/CheckpointedResource.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResourceRid](../../../../models/v2/checkpoints/models/CheckpointedResourceRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResourceType](../../../../models/v2/checkpoints/models/CheckpointedResourceType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedRole](../../../../models/v2/checkpoints/models/CheckpointedRole.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedRoleId](../../../../models/v2/checkpoints/models/CheckpointedRoleId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedSchedule](../../../../models/v2/checkpoints/models/CheckpointedSchedule.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedScheduleRid](../../../../models/v2/checkpoints/models/CheckpointedScheduleRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedToken](../../../../models/v2/checkpoints/models/CheckpointedToken.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedTokenId](../../../../models/v2/checkpoints/models/CheckpointedTokenId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedTokenType](../../../../models/v2/checkpoints/models/CheckpointedTokenType.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeFormInput](../../../../models/v2/checkpoints/models/CheckpointedUserIntakeFormInput.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeFormInputId](../../../../models/v2/checkpoints/models/CheckpointedUserIntakeFormInputId.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeSubmission](../../../../models/v2/checkpoints/models/CheckpointedUserIntakeSubmission.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedUserIntakeSubmissionRid](../../../../models/v2/checkpoints/models/CheckpointedUserIntakeSubmissionRid.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedVersionedObjectSet](../../../../models/v2/checkpoints/models/CheckpointedVersionedObjectSet.md)
- [foundry_sdk.v2.checkpoints.models.ConfigRid](../../../../models/v2/checkpoints/models/ConfigRid.md)
- [foundry_sdk.v2.checkpoints.models.DropdownJustification](../../../../models/v2/checkpoints/models/DropdownJustification.md)
- [foundry_sdk.v2.checkpoints.models.DropdownSelection](../../../../models/v2/checkpoints/models/DropdownSelection.md)
- [foundry_sdk.v2.checkpoints.models.InteractionRid](../../../../models/v2/checkpoints/models/InteractionRid.md)
- [foundry_sdk.v2.checkpoints.models.Justification](../../../../models/v2/checkpoints/models/Justification.md)
- [foundry_sdk.v2.checkpoints.models.JustificationMatchType](../../../../models/v2/checkpoints/models/JustificationMatchType.md)
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
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsAndFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsAndFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsCheckpointedItemIdFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsCheckpointedItemIdFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsEqualsFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsEqualsFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsEqualsFilterField](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsEqualsFilterField.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsGteFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsGteFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsGteFilterField](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsGteFilterField.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsLtFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsLtFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsLtFilterField](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsLtFilterField.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsNotFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsNotFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsOrFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsOrFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsRequest](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsRequest.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsResponse](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsResponse.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsTextSearchFilter](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsTextSearchFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsTextSearchFilterField](../../../../models/v2/checkpoints/models/SearchCheckpointRecordsTextSearchFilterField.md)
- [foundry_sdk.v2.checkpoints.models.SearchRecordsRequest](../../../../models/v2/checkpoints/models/SearchRecordsRequest.md)
- [foundry_sdk.v2.checkpoints.models.SortDirection](../../../../models/v2/checkpoints/models/SortDirection.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/checkpoints/Record.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](search.md)
