# v2.media_sets.MediaSet.metadata


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets detailed metadata about the media item, including type-specific information
such as dimensions for images, duration for audio/video, page count for documents, etc.

## SDK invocation contract

```python
def metadata(self, media_set_rid: core_models.MediaSetRid, media_item_rid: core_models.MediaItemRid, *, preview: typing.Optional[core_models.PreviewMode]=None, read_token: typing.Optional[core_models.MediaItemReadToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> media_sets_models.MediaItemMetadata: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| media_set_rid | core_models.MediaSetRid | required | The RID of the media set. |
| media_item_rid | core_models.MediaItemRid | required | The RID of the media item. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| read_token | typing.Optional[core_models.MediaItemReadToken] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/metadata'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'mediaSetRid': media_set_rid, 'mediaItemRid': media_item_rid}
```

**header_params**

```python
{'ReadToken': read_token, 'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
media_sets_models.MediaItemMetadata
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

Ordinary sync return: `media_sets_models.MediaItemMetadata`. Ordinary async return: `typing.Awaitable[media_sets_models.MediaItemMetadata]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | media_sets_models.MediaItemMetadata |
| sync_raw | ApiResponse[media_sets_models.MediaItemMetadata] |
| sync_streaming | StreamingContextManager[media_sets_models.MediaItemMetadata] |
| async_ordinary | typing.Awaitable[media_sets_models.MediaItemMetadata] |
| async_raw | Awaitable[AsyncApiResponse[media_sets_models.MediaItemMetadata]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[media_sets_models.MediaItemMetadata]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.MediaItemReadToken](../../../../models/v2/core/models/MediaItemReadToken.md)
- [foundry_sdk.v2.core.models.MediaItemRid](../../../../models/v2/core/models/MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.media_sets.models.AffineTransform](../../../../models/v2/media_sets/models/AffineTransform.md)
- [foundry_sdk.v2.media_sets.models.AudioDecodeFormat](../../../../models/v2/media_sets/models/AudioDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.AudioMediaItemMetadata](../../../../models/v2/media_sets/models/AudioMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.AudioSpecification](../../../../models/v2/media_sets/models/AudioSpecification.md)
- [foundry_sdk.v2.media_sets.models.BandInfo](../../../../models/v2/media_sets/models/BandInfo.md)
- [foundry_sdk.v2.media_sets.models.ColorInterpretation](../../../../models/v2/media_sets/models/ColorInterpretation.md)
- [foundry_sdk.v2.media_sets.models.CommonDicomDataElements](../../../../models/v2/media_sets/models/CommonDicomDataElements.md)
- [foundry_sdk.v2.media_sets.models.CoordinateReferenceSystem](../../../../models/v2/media_sets/models/CoordinateReferenceSystem.md)
- [foundry_sdk.v2.media_sets.models.DataType](../../../../models/v2/media_sets/models/DataType.md)
- [foundry_sdk.v2.media_sets.models.DicomDataElementKey](../../../../models/v2/media_sets/models/DicomDataElementKey.md)
- [foundry_sdk.v2.media_sets.models.DicomMediaItemMetadata](../../../../models/v2/media_sets/models/DicomMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.DicomMediaType](../../../../models/v2/media_sets/models/DicomMediaType.md)
- [foundry_sdk.v2.media_sets.models.DicomMetaInformation](../../../../models/v2/media_sets/models/DicomMetaInformation.md)
- [foundry_sdk.v2.media_sets.models.DicomMetaInformationV1](../../../../models/v2/media_sets/models/DicomMetaInformationV1.md)
- [foundry_sdk.v2.media_sets.models.Dimensions](../../../../models/v2/media_sets/models/Dimensions.md)
- [foundry_sdk.v2.media_sets.models.DocumentDecodeFormat](../../../../models/v2/media_sets/models/DocumentDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.DocumentMediaItemMetadata](../../../../models/v2/media_sets/models/DocumentMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.EmailAttachment](../../../../models/v2/media_sets/models/EmailAttachment.md)
- [foundry_sdk.v2.media_sets.models.EmailDecodeFormat](../../../../models/v2/media_sets/models/EmailDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.EmailMediaItemMetadata](../../../../models/v2/media_sets/models/EmailMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.FlipAxis](../../../../models/v2/media_sets/models/FlipAxis.md)
- [foundry_sdk.v2.media_sets.models.GcpList](../../../../models/v2/media_sets/models/GcpList.md)
- [foundry_sdk.v2.media_sets.models.GeoMetadata](../../../../models/v2/media_sets/models/GeoMetadata.md)
- [foundry_sdk.v2.media_sets.models.GpsMetadata](../../../../models/v2/media_sets/models/GpsMetadata.md)
- [foundry_sdk.v2.media_sets.models.GroundControlPoint](../../../../models/v2/media_sets/models/GroundControlPoint.md)
- [foundry_sdk.v2.media_sets.models.Group](../../../../models/v2/media_sets/models/Group.md)
- [foundry_sdk.v2.media_sets.models.GroupWrapper](../../../../models/v2/media_sets/models/GroupWrapper.md)
- [foundry_sdk.v2.media_sets.models.ImageAttributeDomain](../../../../models/v2/media_sets/models/ImageAttributeDomain.md)
- [foundry_sdk.v2.media_sets.models.ImageAttributeKey](../../../../models/v2/media_sets/models/ImageAttributeKey.md)
- [foundry_sdk.v2.media_sets.models.ImageryDecodeFormat](../../../../models/v2/media_sets/models/ImageryDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.ImageryMediaItemMetadata](../../../../models/v2/media_sets/models/ImageryMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.Mailbox](../../../../models/v2/media_sets/models/Mailbox.md)
- [foundry_sdk.v2.media_sets.models.MailboxOrGroup](../../../../models/v2/media_sets/models/MailboxOrGroup.md)
- [foundry_sdk.v2.media_sets.models.MailboxWrapper](../../../../models/v2/media_sets/models/MailboxWrapper.md)
- [foundry_sdk.v2.media_sets.models.MediaItemMetadata](../../../../models/v2/media_sets/models/MediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.Modality](../../../../models/v2/media_sets/models/Modality.md)
- [foundry_sdk.v2.media_sets.models.Model3dDecodeFormat](../../../../models/v2/media_sets/models/Model3dDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.Model3dMediaItemMetadata](../../../../models/v2/media_sets/models/Model3dMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.Model3dType](../../../../models/v2/media_sets/models/Model3dType.md)
- [foundry_sdk.v2.media_sets.models.Orientation](../../../../models/v2/media_sets/models/Orientation.md)
- [foundry_sdk.v2.media_sets.models.PaletteInterpretation](../../../../models/v2/media_sets/models/PaletteInterpretation.md)
- [foundry_sdk.v2.media_sets.models.RotationAngle](../../../../models/v2/media_sets/models/RotationAngle.md)
- [foundry_sdk.v2.media_sets.models.SpreadsheetDecodeFormat](../../../../models/v2/media_sets/models/SpreadsheetDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.SpreadsheetMediaItemMetadata](../../../../models/v2/media_sets/models/SpreadsheetMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.UnitInterpretation](../../../../models/v2/media_sets/models/UnitInterpretation.md)
- [foundry_sdk.v2.media_sets.models.UntypedMediaItemMetadata](../../../../models/v2/media_sets/models/UntypedMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.VideoDecodeFormat](../../../../models/v2/media_sets/models/VideoDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.VideoMediaItemMetadata](../../../../models/v2/media_sets/models/VideoMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.VideoSpecification](../../../../models/v2/media_sets/models/VideoSpecification.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/media_sets/MediaSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](metadata.md)
